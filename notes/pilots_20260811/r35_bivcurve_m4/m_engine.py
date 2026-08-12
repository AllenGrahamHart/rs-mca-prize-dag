"""r35 D1/D2 -- ONE ENGINE for (SPLIT-m)+sigma at m = 3, 4, 5.

Unifies r34's m=3 and m=4 searches so the m-comparison is apples-to-apples
(same DFS, same budget, same ensemble), and adds the general law r34 stated
only at m=4:

    a shared (m-1)-tuple puts 2 points into each of its C(m-1,2) slope pairs;
    the (OV) cap is |S_al ^ S_be| <= 2rho-a = m-1;  hence

        PAIR MULTIPLICITY CAP  =  floor((m-1)/2)
        m=3 -> 1 (distinct pairs)   m=4 -> 1 (LINEAR)   m=5 -> 2 (not linear)

    and (DEG-m), from the coordinator-corrected (OUT-m):
        deg_H(gamma) >= ceil((m-1)/2)      m=3 -> 1, m=4 -> 2, m=5 -> 2

factor structure: (m-1) linear-in-Z factors = floor((m-1)/2) sigma-SWAPPED
degree-3 pencils (phi, phi o sigma) + ((m-1) mod 2) sigma-INVARIANT factors
(Mobius in u = x^2, deg_x 2, injective on orbits).

    m=3 : 1 swapped pair                 P = 7  parameters
    m=4 : 1 swapped pair + 1 invariant   P = 7+3 = 10
    m=5 : 2 swapped pairs                P = 14

m=3 is the POSITIVE CONTROL: the harness must reach 9 of 9 there, or its
failures at m=4/5 mean nothing.

Stdlib only.  Checkpointed.
"""

import random
import sys
import time

STEP = sys.argv[2] if len(sys.argv) > 2 else "all"
CKPT = "notes/pilots_20260811/r35_bivcurve_m4/m_engine_ckpt.txt"
RES = "notes/pilots_20260811/r35_bivcurve_m4/m_engine_results_%s.txt" % STEP
T0 = time.time()
DEADLINE = float(sys.argv[1]) if len(sys.argv) > 1 else 240.0
out = []
P = out.append


def ckpt(s):
    with open(CKPT, "a") as fh:
        fh.write("%7.1fs %s\n" % (time.time() - T0, s))


def mu_N(q, N):
    assert (q - 1) % N == 0
    for c in range(2, q):
        g = pow(c, (q - 1) // N, q)
        seen, x = set(), 1
        for _ in range(N):
            seen.add(x)
            x = x * g % q
        if len(seen) == N:
            return sorted(seen)
    raise RuntimeError


def cev(c, x, q):
    v = 0
    for co in reversed(c):
        v = (v * x + co) % q
    return v


def best_sel(tuples, nedge, degcap, nslope, paircap, mindeg, budget):
    """max selection of shared tuples with: slope-degree <= degcap, distinct
    slopes <= nslope, slope-PAIR multiplicity <= paircap.  Returns
    (best_any, best_sel_any, best_mindeg, nodes): best_mindeg is the largest
    selection all of whose used slopes have degree >= mindeg."""
    n = len(tuples)
    deg, pair, chosen = {}, {}, []
    best = [0, []]
    bestmd = [0, []]
    cnt = [0]

    def rec(i):
        if cnt[0] > budget:
            return
        cnt[0] += 1
        k = len(chosen)
        if k > best[0]:
            best[0] = k
            best[1] = list(chosen)
        if k > bestmd[0] and k and all(d >= mindeg for d in deg.values()):
            bestmd[0] = k
            bestmd[1] = list(chosen)
        if k == nedge:
            return
        if k + (n - i) <= best[0] and k + (n - i) <= bestmd[0]:
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
    return best[0], best[1], bestmd[0], cnt[0]


def params(m):
    return 7 * ((m - 1) // 2) + 3 * ((m - 1) % 2)


def draw_tuples(q, m, rnd, D, orbits):
    """random (SPLIT-m)+sigma data; returns list of shared (m-1)-tuples, one
    per orbit with all values distinct, plus the raw pencil data."""
    npair, ninv = (m - 1) // 2, (m - 1) % 2
    pencils = [([rnd.randrange(q) for _ in range(4)],
                [rnd.randrange(q) for _ in range(4)]) for _ in range(npair)]
    invs = [([rnd.randrange(q) for _ in range(2)],
             [rnd.randrange(q) for _ in range(2)]) for _ in range(ninv)]
    tup = []
    for (x, y) in orbits:
        vals, ok = [], True
        for (A, B) in pencils:
            bx, by = cev(B, x, q), cev(B, y, q)
            if bx == 0 or by == 0:
                ok = False
                break
            vals.append(cev(A, x, q) * pow(bx, q - 2, q) % q)
            vals.append(cev(A, y, q) * pow(by, q - 2, q) % q)
        if ok:
            u = x * x % q
            for (R, S) in invs:
                sx = cev(S, u, q)
                if sx == 0:
                    ok = False
                    break
                vals.append(cev(R, u, q) * pow(sx, q - 2, q) % q)
        if ok and len(set(vals)) == m - 1:
            tup.append(tuple(vals))
    return tup, (pencils, invs)


def run(m, q, trials, seed, budget, variants=None, label=""):
    N, rho, a = 16 * m, 4 * m - 1, 7 * m - 1
    nedge, ksize = 3 * m, m - 1
    degcap, nslope = m - 1, rho
    paircap, mindeg = (m - 1) // 2, -((-(m - 1)) // 2)
    D = mu_N(q, N)
    seen, orbits = set(), []
    for x in D:
        if x in seen:
            continue
        y = (q - x) % q
        seen.add(x)
        seen.add(y)
        orbits.append((x, y))
    rnd = random.Random(seed)
    if variants is None:
        variants = [("FULL", degcap, nslope, paircap, mindeg)]
    hist = {v[0]: {} for v in variants}
    bestv = {v[0]: 0 for v in variants}
    bestmd = {v[0]: 0 for v in variants}
    ntup = []
    done = 0
    for tr in range(trials):
        if time.time() - T0 > DEADLINE:
            break
        tup, raw = draw_tuples(q, m, rnd, D, orbits)
        ntup.append(len(tup))
        if len(tup) < nedge:
            continue
        done += 1
        for (nm, dc, ns, pc, md) in variants:
            s, sel, smd, nodes = best_sel(tup, nedge, dc, ns, pc, md, budget)
            hist[nm][s] = hist[nm].get(s, 0) + 1
            if s > bestv[nm]:
                bestv[nm] = s
            if smd > bestmd[nm]:
                bestmd[nm] = smd
        if tr % 25 == 24:
            ckpt("m=%d q=%d %s tr=%d best=%s" % (m, q, label, tr, bestv))
    P("  m=%d q=%d %s : %d draws (%d usable), tuples/draw avg %.1f of %d orbits"
      % (m, q, label, done, done, sum(ntup) / max(1, len(ntup)), len(orbits)))
    P("    NEED %d tuples ; deg cap %d ; <= %d slopes ; pair cap %d ; "
      "(DEG-m) min deg %d ; params P = %d"
      % (nedge, degcap, nslope, paircap, mindeg, params(m)))
    for (nm, dc, ns, pc, md) in variants:
        h = hist[nm]
        P("    [%-14s deg<=%d slopes<=%-3d paircap=%-2d] BEST = %2d of %2d"
          "   (min-deg-%d-clean BEST = %d)   hist %s"
          % (nm, dc, ns, pc, bestv[nm], nedge, md, bestmd[nm],
             sorted(h.items())))
    return bestv, bestmd


P("=" * 78)
P("r35 -- (SPLIT-m)+sigma UNDER ONE ENGINE:  m = 3 (control), 4, 5")
P("=" * 78)
P("")
P("registered (SUPPLY-CODIM) excess E = P - D, D = 3m^2-7m+2 (coincidences")
P("needed by the shared tuples), P = pencil parameters:")
for m in (2, 3, 4, 5):
    D_ = 3 * m * m - 7 * m + 2
    Pp = 7 if m == 2 else params(m)
    P("    m=%d : slots 3m(m-1) = %2d ; slopes rho-1 = %2d ; D = %2d ; P = %2d"
      " ; E = %+d" % (m, 3 * m * (m - 1), 4 * m - 2, D_, Pp, Pp - D_))
P("")
V4 = [("V1 FULL", 3, 15, 1, 2), ("V2 NO-LINEAR", 3, 15, 99, 2),
      ("V3 NO-SLOPES", 3, 999, 1, 2)]
V5 = [("FULL", 4, 19, 2, 2), ("NO-PAIRCAP", 4, 19, 99, 2),
      ("NO-SLOPES", 4, 999, 2, 2)]
V3v = [("V1 FULL", 2, 11, 1, 1), ("V3 NO-SLOPES", 2, 999, 1, 1)]

if STEP in ("all", "s1"):
    P("-" * 78)
    P("STEP 1 -- POSITIVE CONTROL at m = 3 (the harness must reach 9 of 9)")
    ckpt("start m=3 control")
    for q in (97, 193):
        run(3, q, 400, 350000 + q, 30000, variants=V3v, label="control")

if STEP in ("all", "s2a", "s2b"):
    P("")
    P("-" * 78)
    P("STEP 2 -- m = 4, THE LAYER SEPARATION (which constraint binds?)")
    P("  V1 FULL      = r34's constraint set (linear, deg<=3, <=15 slopes)")
    P("  V2 NO-LINEAR = drop the (OV) linearity -> isolates the SELECTION layer")
    P("  V3 NO-SLOPES = drop the <=15 slope cap -> isolates the ARITHMETIC layer")
    ckpt("start m=4 layers")
    for q in ((193,) if STEP == "s2a" else (257,) if STEP == "s2b" else (193, 257)):
        run(4, q, 300, 440000 + q, 12000, variants=V4, label="layers")

if STEP in ("all", "s3a", "s3b"):
    P("")
    P("-" * 78)
    P("STEP 3 -- m = 5, THE PARITY FALSIFIER ((SPLIT-5)+sigma, ALL-SWAPPED,")
    P("          m-1 = 4 factors, NO sigma-invariant factor forced)")
    ckpt("start m=5")
    for q in ((241,) if STEP == "s3a" else (401,) if STEP == "s3b" else (241, 401)):
        run(5, q, 250, 550000 + q, 12000, variants=V5, label="parity")

P("")
P("=" * 78)
print("\n".join(out))
with open(RES, "w") as f:
    f.write("\n".join(out) + "\n")
