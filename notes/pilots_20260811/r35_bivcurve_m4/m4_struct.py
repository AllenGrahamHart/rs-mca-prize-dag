"""r35 D1 -- STRUCTURED (value-prescribed) pencils at m = 4.

r34's m=4 negative sampled (phi,chi) at RANDOM and declared itself zero-power
over structured pencils (its ZP item 5: "a structured (non-random) pencil
could beat the ensemble").  This script builds the structured pencils.

KEY LINEAR-ALGEBRA FACT (registered as R5.1): phi = A/B with deg A,B <= 3 has
8 coefficients; the condition phi(x) = t is A(x) - t B(x) = 0, LINEAR in the
coefficients for a FIXED target t.  So SEVEN prescribed values can be imposed
exactly by solving a 7 x 8 system -- phi is then determined projectively (the
8th dimension is the scale).  This is the exact analogue of prescribing two
size-3 fibres (6 conditions) with one parameter left over.

TARGET (from sel_layer.py's A1 certificate): the Z_12 design
   T_i = {c_i, c_{i+1}, c_{i+3}},  c_i = chi-value of orbit i,
   i.e.  {phi(x_i), phi(-x_i)} = {c_{i+1}, c_{i+3}}     (24 conditions)
chi is Mobius in u = x^2 hence injective on orbits, so the c_i are distinct,
and this design uses only 12 slopes of the 15 available with every degree = 3.

Two allocations of the 7 affordable conditions:
   ALLOC-A : 3 orbits fully targeted (6 conditions) + 1 spare arrow
   ALLOC-B : 7 orbits with one arrow each
plus the RANDOM baseline under an identical DFS budget and draw count.

Stdlib only.  Checkpointed.
"""

import random
import sys
import time

T0 = time.time()
DEADLINE = float(sys.argv[1]) if len(sys.argv) > 1 else 240.0
CK = "notes/pilots_20260811/r35_bivcurve_m4/m4_struct_ckpt.txt"
out = []
P = out.append
m, N, rho, a = 4, 64, 15, 27
NEDGE, DEGCAP, NSLOPE, PAIRCAP = 12, 3, 15, 1


def ckpt(s):
    with open(CK, "a") as fh:
        fh.write("%7.1fs %s\n" % (time.time() - T0, s))


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


def nullspace(rows, ncol, q):
    """returns a basis of the nullspace of the given rows over F_q."""
    M = [r[:] for r in rows]
    piv = []
    r = 0
    for c in range(ncol):
        p = None
        for i in range(r, len(M)):
            if M[i][c] % q:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = pow(M[r][c], q - 2, q)
        M[r] = [v * inv % q for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % q:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % q for j in range(ncol)]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    free = [c for c in range(ncol) if c not in piv]
    basis = []
    for fc in free:
        v = [0] * ncol
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-M[i][fc]) % q
        basis.append(v)
    return basis


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
    return best[0], best[1]


def triples_of(q, orbits, A, B, R, S):
    tri, owner = [], []
    for idx, (x, y) in enumerate(orbits):
        bx, by = cev(B, x, q), cev(B, y, q)
        u = x * x % q
        sx = cev(S, u, q)
        if bx == 0 or by == 0 or sx == 0:
            continue
        p1 = cev(A, x, q) * pow(bx, q - 2, q) % q
        p2 = cev(A, y, q) * pow(by, q - 2, q) % q
        p3 = cev(R, u, q) * pow(sx, q - 2, q) % q
        if len({p1, p2, p3}) == 3:
            tri.append((p1, p2, p3))
            owner.append(idx)
    return tri, owner


def run(q, mode, trials, seed, budget):
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
    hist, best, bestdata = {}, 0, None
    ntargeted = []
    done = 0
    for tr in range(trials):
        if time.time() - T0 > DEADLINE:
            break
        # --- chi: Mobius in u = x^2 (3 projective parameters)
        while True:
            R = [rnd.randrange(q), rnd.randrange(q)]
            S = [rnd.randrange(q), rnd.randrange(q)]
            if (R[1] * S[0] - R[0] * S[1]) % q:
                break
        if mode == "RANDOM":
            A = [rnd.randrange(q) for _ in range(4)]
            B = [rnd.randrange(q) for _ in range(4)]
        else:
            sel = rnd.sample(range(len(orbits)), 12)
            cval, okc = [], True
            for i in sel:
                u = orbits[i][0] ** 2 % q
                s = cev(S, u, q)
                if s == 0:
                    okc = False
                    break
                cval.append(cev(R, u, q) * pow(s, q - 2, q) % q)
            if not okc or len(set(cval)) < 12:
                continue
            # Z_12 target: orbit i sends its two phi-values to c_{i+1}, c_{i+3}
            conds = []
            for i in range(12):
                x, y = orbits[sel[i]]
                if rnd.random() < 0.5:
                    conds.append((x, cval[(i + 1) % 12]))
                    conds.append((y, cval[(i + 3) % 12]))
                else:
                    conds.append((y, cval[(i + 1) % 12]))
                    conds.append((x, cval[(i + 3) % 12]))
            if mode == "ALLOC-A":     # 3 orbits fully + 1 arrow
                use = conds[0:6] + [conds[6]]
            else:                      # ALLOC-B: 7 orbits, one arrow each
                use = [conds[2 * i] for i in range(7)]
            rows = []
            for (x, t) in use:
                rows.append([pow(x, j, q) for j in range(4)] +
                            [(-t) * pow(x, j, q) % q for j in range(4)])
            bas = nullspace(rows, 8, q)
            if not bas:
                continue
            v = bas[0]
            if len(bas) > 1:
                v = [0] * 8
                for b in bas:
                    c = rnd.randrange(q)
                    v = [(v[i] + c * b[i]) % q for i in range(8)]
            A, B = v[0:4], v[4:8]
            if all(z == 0 for z in B) or all(z == 0 for z in A):
                continue
            # reject degenerate (constant) phi: A = t B
            deg_ok = False
            for i in range(4):
                if B[i]:
                    lam = A[i] * pow(B[i], q - 2, q) % q
                    deg_ok = any((A[j] - lam * B[j]) % q for j in range(4))
                    break
            if not deg_ok:
                continue
        tri, owner = triples_of(q, orbits, A, B, R, S)
        if len(tri) < NEDGE:
            continue
        done += 1
        if mode != "RANDOM":
            # how many of the 12 TARGETED triples actually materialised?
            hit = 0
            for i in range(12):
                x, y = orbits[sel[i]]
                bx, by = cev(B, x, q), cev(B, y, q)
                if bx == 0 or by == 0:
                    continue
                p1 = cev(A, x, q) * pow(bx, q - 2, q) % q
                p2 = cev(A, y, q) * pow(by, q - 2, q) % q
                if {p1, p2} == {cval[(i + 1) % 12], cval[(i + 3) % 12]}:
                    hit += 1
            ntargeted.append(hit)
        s, sl = best_sel(tri, NEDGE, DEGCAP, NSLOPE, PAIRCAP, budget)
        hist[s] = hist.get(s, 0) + 1
        if s > best:
            best = s
            bestdata = (A, B, R, S, [tri[j] for j in sl])
        if tr % 50 == 49:
            ckpt("q=%d %s tr=%d best=%d" % (q, mode, tr, best))
    P("  q=%-4d %-9s : %4d usable draws, budget %d -> BEST = %2d of %d   hist %s"
      % (q, mode, done, budget, best, NEDGE, sorted(hist.items())))
    if ntargeted:
        P("           targeted triples realised per draw: min %d mean %.2f max %d"
          " (7 of 24 arrows forced -> 3 guaranteed under ALLOC-A)"
          % (min(ntargeted), sum(ntargeted) / len(ntargeted), max(ntargeted)))
    if bestdata and best >= 9:
        P("           best A=%s B=%s R=%s S=%s" % bestdata[:4])
        for t in bestdata[4]:
            P("             triple %s" % (t,))
    return best


P("=" * 78)
P("r35 D1 -- STRUCTURED vs RANDOM PENCILS AT m = 4")
P("=" * 78)
P("prescribing 7 of phi's 8 coefficients' worth of conditions EXACTLY by")
P("linear algebra (R5.1).  Same DFS, same budget, same draw count as the")
P("RANDOM baseline in the same run -- so the comparison is apples-to-apples.")
P("")
for q in (193, 257):
    P("-" * 78)
    for mode in ("RANDOM", "ALLOC-A", "ALLOC-B"):
        run(q, mode, 220, 770000 + q + hash(mode) % 1000, 12000)
P("")
P("=" * 78)
print("\n".join(out))
with open("notes/pilots_20260811/r35_bivcurve_m4/m4_struct_results.txt", "w") as f:
    f.write("\n".join(out) + "\n")
