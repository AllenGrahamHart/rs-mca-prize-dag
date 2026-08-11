"""r34 D3 -- the m = 4 fork of (BIV-CURVE).

m=4: N=64, rho=15, T=17, a=27, e=4, delta=3, |S_g^S_h| = m-1 = 3,
|S_g D S_h| = 6m = 24, T_2 = rho = 15 type-2 slopes, X cap 2m-2 = 6,
per-side cap m-1 = 3, sum X = (m-1)(7m-2) = 78.

(SPLIT-m) at m=4 needs THREE linear-in-Z factors of total x-degree 3m-3 = 9.
The m=3 witness got its slope-count economy from the involution sigma(x) = -x
(one orbit -> ONE shared slope tuple, so the tuple multiplicity is 2 <= m-1).
The order-3 analogue does not exist on mu_N (gcd(3,N) = 1 for N = 64), so the
m=4 sigma-design is

  G(Z,x) = (B(x)Z-A(x))(B(-x)Z-A(-x))(S(x^2)Z-R(x^2)),  deg A,B <= 3,
           deg R,S <= 1 in u = x^2

i.e. two sigma-swapped degree-3 pencils and one sigma-INVARIANT degree-2 pencil.
deg_x G <= 3+3+2 = 8 <= 9 = 3m-3, deg_Z G = 3 = m-1.  Each orbit {x,-x} then
carries ONE shared type-2 TRIPLE {phi(x), phi(-x), chi(x)}.

Consequence measured here (the new constraint that m=3 did not have):
|S_al ^ S_be| >= 2 for every pair inside a triple, and the cap is 2rho-a = m-1
= 3, so ANY TWO SLOPES MAY CO-OCCUR IN AT MOST ONE TRIPLE -- the 12 selected
orbit-triples must form a LINEAR (partial-Steiner) 3-uniform hypergraph on the
15 slopes, with every slope-degree k in {2,3} and sum k = 36.

This script measures whether that is reachable, and reports the exact layer
that binds if it is not.
"""

import random
import sys

sys.path.insert(0, "notes/pilots_20260811/r34_bivcurve_m34")
from biv_core import mu_N

m = 4
N, rho, T, a, R = 16 * m, 4 * m - 1, 4 * m + 1, 7 * m - 1, 8 * m
NEDGE = 3 * m          # 12 orbits carrying S_g D S_h
NSLOPE = rho           # 15
KMAX = m - 1           # 3
out = []
P = out.append


def cev(c, x, q):
    v = 0
    for co in reversed(c):
        v = (v * x + co) % q
    return v


def best_linear(triples, nedge, kmax, nslope, budget):
    """largest set of triples, pairwise sharing <= 1 slope, slope degree <= kmax,
    total distinct slopes <= nslope.  DFS with a node budget; returns (best_size,
    best_selection)."""
    n = len(triples)
    deg, pairs, chosen = {}, set(), []
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
            t = triples[j]
            u, v, w = t
            if any(deg.get(z, 0) >= kmax for z in t):
                continue
            key = [(min(x1, y1), max(x1, y1)) for x1, y1 in
                   ((u, v), (u, w), (v, w))]
            if any(k in pairs for k in key):
                continue
            newv = sum(1 for z in t if z not in deg)
            if len(deg) + newv > nslope:
                continue
            for z in t:
                deg[z] = deg.get(z, 0) + 1
            for k in key:
                pairs.add(k)
            chosen.append(j)
            rec(j + 1)
            chosen.pop()
            for k in key:
                pairs.discard(k)
            for z in t:
                deg[z] -= 1
                if deg[z] == 0:
                    del deg[z]
            if cnt[0] > budget:
                return
        return

    rec(0)
    return best


def run(q, seed, trials):
    D = mu_N(q, N)
    Dset = set(D)
    orbits, seen = [], set()
    for x in D:
        if x in seen:
            continue
        y = (q - x) % q
        seen.add(x); seen.add(y)
        orbits.append((x, y))
    rnd = random.Random(seed)
    hist = {}
    bestever = (0, None)
    for tr in range(trials):
        A = [rnd.randrange(q) for _ in range(4)]
        B = [rnd.randrange(q) for _ in range(4)]
        Rr = [rnd.randrange(q) for _ in range(2)]
        S = [rnd.randrange(q) for _ in range(2)]
        tri, ok = [], True
        for (x, y) in orbits:
            bx, by = cev(B, x, q), cev(B, y, q)
            u = x * x % q
            sx = cev(S, u, q)
            if bx == 0 or by == 0 or sx == 0:
                ok = False
                break
            p1 = cev(A, x, q) * pow(bx, q - 2, q) % q
            p2 = cev(A, y, q) * pow(by, q - 2, q) % q
            p3 = cev(Rr, u, q) * pow(sx, q - 2, q) % q
            if len({p1, p2, p3}) == 3:
                tri.append((p1, p2, p3))
        if not ok or len(tri) < NEDGE:
            continue
        sz, sel = best_linear(tri, NEDGE, KMAX, NSLOPE, 4000)
        hist[sz] = hist.get(sz, 0) + 1
        if sz > bestever[0]:
            bestever = (sz, (A, B, Rr, S, [tri[j] for j in sel]))
        if sz >= NEDGE:
            break
        if tr % 100 == 99:
            with open("notes/pilots_20260811/r34_bivcurve_m34/m4_ckpt.txt", "a") as fh:
                fh.write("q=%d trial=%d hist=%s best=%d\n"
                         % (q, tr, sorted(hist.items()), bestever[0]))
    return hist, bestever, orbits


P("=" * 78)
P("r34 D3 -- (BIV-CURVE) AT m = 4   [(SPLIT-m) + sigma, two-swapped + one-fixed]")
P("=" * 78)
P("m=%d N=%d rho=%d T=%d a=%d ; sum X = (m-1)(7m-2) = %d ; cap 2m-2 = %d ;"
  % (m, N, rho, T, a, (m - 1) * (7 * m - 2), 2 * m - 2))
P("per-side cap m-1 = %d ; T_2 = %d slopes ; need %d orbit-triples, sum k = %d"
  % (m - 1, rho, NEDGE, 3 * NEDGE))
P("")
P("NEW BINDING CONSTRAINT AT m>=4 (absent at m=3): a shared TRIPLE puts 2")
P("points in every one of its 3 slope-pairs, and the (OV) pair cap is m-1 = 3,")
P("so two slopes co-occur in AT MOST ONE triple => the 12 triples must be a")
P("LINEAR 3-uniform hypergraph with all degrees <= 3 on <= 15 vertices.")
P("Counting: 12 triples * 3 = 36 slope-slots, 15 slopes, degree cap 3 => 45.")
P("Feasible on paper (slack 9).  Measured reachability below.")
P("")

for q, tri in ((193, 800), (257, 800)):
    P("-" * 78)
    P("q = %d   (64 | q-1 : %s)" % (q, (q - 1) % 64 == 0))
    hist, bestever, orbits = run(q, 440000 + q, tri)
    P("  histogram of MAX linear-hypergraph size over %d random (phi,chi):" % tri)
    for k in sorted(hist):
        P("    size %2d : %d" % (k, hist[k]))
    P("  BEST = %d  (need %d)" % (bestever[0], NEDGE))
    if bestever[0] >= NEDGE:
        A, B, Rr, S, sel = bestever[1]
        P("  *** REACHED: A=%s B=%s R=%s S=%s" % (A, B, Rr, S))
        for t in sel:
            P("      triple %s" % (t,))
    elif bestever[1]:
        A, B, Rr, S, sel = bestever[1]
        P("  best witness A=%s B=%s R=%s S=%s ; %d triples" % (A, B, Rr, S, len(sel)))
        for t in sel:
            P("      triple %s" % (t,))

P("")
P("=" * 78)
print("\n".join(out))
with open("notes/pilots_20260811/r34_bivcurve_m34/m4_search_results.txt", "w") as f:
    f.write("\n".join(out) + "\n")
