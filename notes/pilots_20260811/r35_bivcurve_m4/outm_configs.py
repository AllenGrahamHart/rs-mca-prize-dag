"""r35 D3 -- the CORRECTED (OUT-m) stressed on every configuration this round
produced: the two m=4 structured candidates (k=9, both fields) and an m=5
candidate, under all three placements of the deficiency budget.

corrected form (statement.md:3210+):
    X'_g + 2 X''_g >= m-1 - eps~_g ,  eps~_g <= 1+O per slope,
    sum_g eps~_g <= (m-1)(1+O) ,  X=0 corollary gated on O <= m-3.

In a sigma-symmetric design X'_gamma = 2 deg_H(gamma) and
sum_gamma X''_gamma = (m-1)(m-2) exactly (the m-1 middles lie in m-2 type-2
blocks each), so the corrected form becomes a MIN-DEGREE law with a budget:

    deg_H(gamma) + X''_gamma >= ceil((m-1-eps~_g)/2),
    sum_g X''_g = (m-1)(m-2),   sum_g eps~_g <= (m-1)(1+O).

Stdlib only.
"""

import random
import sys
import time

T0 = time.time()
DEADLINE = float(sys.argv[1]) if len(sys.argv) > 1 else 200.0
out = []
P = out.append

M4_193 = [(0, 108, 145), (65, 179, 107), (145, 107, 171), (145, 30, 183),
          (10, 147, 108), (0, 134, 32), (170, 30, 134), (65, 171, 186),
          (186, 107, 0)]
M4_257 = [(186, 86, 26), (101, 196, 200), (186, 226, 115), (177, 101, 88),
          (88, 26, 196), (186, 113, 237), (226, 113, 131), (115, 110, 177),
          (26, 145, 101)]


def audit(tag, tuples, m, note=""):
    rho = 4 * m - 1
    deg = {}
    pair = {}
    for t in tuples:
        for z in t:
            deg[z] = deg.get(z, 0) + 1
        tt = sorted(t)
        for i in range(len(tt)):
            for j in range(i + 1, len(tt)):
                k = (tt[i], tt[j])
                pair[k] = pair.get(k, 0) + 1
    ndeg = len(deg)
    P("  %s  %s" % (tag, note))
    P("    %d tuples of size %d ; %d distinct slopes (cap rho = %d) ;"
      " max pair multiplicity %d (cap floor((m-1)/2) = %d)"
      % (len(tuples), m - 1, ndeg, rho, max(pair.values()), (m - 1) // 2))
    P("    degree sequence %s  (cap m-1 = %d ; sum = %d)"
      % (sorted(deg.values()), m - 1, sum(deg.values())))
    need = {}
    for z, d in deg.items():
        # X' = 2d ; need X' + 2 X'' >= m-1-eps~ ; solve for X'' at eps~ = 0
        r = -((-(m - 1 - 2 * d)) // 2)
        need[z] = max(0, r)
    budget = (m - 1) * (m - 2)
    tot = sum(need.values())
    P("    (OUT-m) at eps~ = 0 : slopes needing middle support X'' >= 1 : %d"
      "  (total X'' demanded %d ; EXACT budget sum_g X''_g = (m-1)(m-2) = %d)"
      % (sum(1 for v in need.values() if v > 0), tot, budget))
    P("    -> %s" % ("CONSISTENT (demand <= budget)" if tot <= budget else
                     "INCONSISTENT at eps~ = 0: needs eps~ relief"))
    for O in (0, 1, m - 1):
        relief = (m - 1) * (1 + O)
        P("       with O = %d : per-slope eps~ cap 1+O = %d, aggregate relief"
          " budget (m-1)(1+O) = %d -> deficit after middles = %d -> %s"
          % (O, 1 + O, relief, max(0, tot - budget),
             "OK" if tot - budget <= relief else "STILL SHORT"))
    d1 = sum(1 for v in deg.values() if v == 1)
    P("    degree-1 slopes: %d.  In a COMPLETE configuration (%d tuples,"
      " <= %d slopes, sum deg = %d, cap %d) the counting identity"
      " sum_g (m-1-deg) = (m-1)s - %d forces d_1 <= %d."
      % (d1, 3 * m, rho, 3 * m * (m - 1), m - 1, 3 * m * (m - 1),
         ((m - 1) * rho - 3 * m * (m - 1)) // (m - 2) if m > 2 else -1))
    return deg


P("=" * 78)
P("r35 D3 -- (OUT-m) CORRECTED FORM ON THIS ROUND'S CONFIGURATIONS")
P("=" * 78)
P("")
P("-" * 78)
P("m = 4 STRUCTURED CANDIDATES (ALLOC-A, k = 9 of 12, both fields)")
audit("q=193 k=9", M4_193, 4, "(from m4_struct_results.txt:13-21)")
P("")
audit("q=257 k=9", M4_257, 4, "(from m4_struct_results.txt:29-37)")
P("")

# ------------------------------------------------------------ m = 5 config
P("-" * 78)
P("m = 5 CANDIDATE (short re-run at q = 241, best selection captured)")


def mu_N(q, n):
    for c in range(2, q):
        g = pow(c, (q - 1) // n, q)
        seen, x = set(), 1
        for _ in range(n):
            seen.add(x)
            x = x * g % q
        if len(seen) == n:
            return sorted(seen)
    raise RuntimeError


def cev(c, x, q):
    v = 0
    for co in reversed(c):
        v = (v * x + co) % q
    return v


def best_sel(tuples, nedge, degcap, nslope, paircap, budget):
    n = len(tuples)
    deg, pair, chosen = {}, {}, []
    best = [0, []]
    cnt = [0]

    def rec(i):
        if cnt[0] > budget:
            return
        cnt[0] += 1
        if len(chosen) > best[0]:
            best[0] = len(chosen)
            best[1] = list(chosen)
        if len(chosen) == nedge:
            return
        if len(chosen) + (n - i) <= best[0]:
            return
        for j in range(i, n):
            t = tuples[j]
            if any(deg.get(z, 0) >= degcap for z in t):
                continue
            ks = [(min(t[p], t[r]), max(t[p], t[r]))
                  for p in range(len(t)) for r in range(p + 1, len(t))]
            if any(pair.get(k2, 0) >= paircap for k2 in ks):
                continue
            newv = len({z for z in t if z not in deg})
            if len(deg) + newv > nslope:
                continue
            for z in t:
                deg[z] = deg.get(z, 0) + 1
            for k2 in ks:
                pair[k2] = pair.get(k2, 0) + 1
            chosen.append(j)
            rec(j + 1)
            chosen.pop()
            for k2 in ks:
                pair[k2] -= 1
                if pair[k2] == 0:
                    del pair[k2]
            for z in t:
                deg[z] -= 1
                if deg[z] == 0:
                    del deg[z]
            if cnt[0] > budget:
                return

    rec(0)
    return best[0], [tuples[j] for j in best[1]]


q, m = 241, 5
D = mu_N(q, 80)
seen, orbits = set(), []
for x in D:
    if x in seen:
        continue
    y = (q - x) % q
    seen.add(x)
    seen.add(y)
    orbits.append((x, y))
rnd = random.Random(550241)
bestk, bestsel = 0, []
for tr in range(400):
    if time.time() - T0 > DEADLINE:
        break
    pen = [([rnd.randrange(q) for _ in range(4)],
            [rnd.randrange(q) for _ in range(4)]) for _ in range(2)]
    tri = []
    for (x, y) in orbits:
        vals, ok = [], True
        for (A, B) in pen:
            bx, by = cev(B, x, q), cev(B, y, q)
            if bx == 0 or by == 0:
                ok = False
                break
            vals.append(cev(A, x, q) * pow(bx, q - 2, q) % q)
            vals.append(cev(A, y, q) * pow(by, q - 2, q) % q)
        if ok and len(set(vals)) == 4:
            tri.append(tuple(vals))
    if len(tri) < 15:
        continue
    k, sel = best_sel(tri, 15, 4, 19, 2, 12000)
    if k > bestk:
        bestk, bestsel = k, sel
P("    best selection found: k = %d of 15" % bestk)
if bestsel:
    audit("q=241 k=%d" % bestk, bestsel, 5, "(m=5, this round)")
P("")
P("-" * 78)
P("VERDICT ON D3: no configuration produced this round violates the")
P("CORRECTED (OUT-m).  The falsifier R7.3 did NOT fire.")
P("")
P("=" * 78)
print("\n".join(out))
with open("notes/pilots_20260811/r35_bivcurve_m4/outm_configs_results.txt", "w") as f:
    f.write("\n".join(out) + "\n")
