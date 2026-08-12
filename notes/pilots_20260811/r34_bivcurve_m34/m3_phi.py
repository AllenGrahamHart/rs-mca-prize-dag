"""r34 D1/D2 -- CONSTRUCTIVE (BIV-CURVE) search at m = 3.

Registered ansatz (PREREG R1, (SPLIT-m)) specialised with an involution:

  G(Z,x) = ( B(x)Z - A(x) ) * ( B(-x)Z - A(-x) ),   deg A,B <= 3

so deg_Z G = 2 = m-1 and deg_x G <= 6 = 3m-3 (the budget, met with equality).
phi = A/B (degree 3), psi = phi o sigma with sigma(x) = -x, an involution of
D = mu_48.  Then for every orbit O = {x,-x} the two points carry the SAME
unordered slope pair {phi(x), phi(-x)} -- the "crossed pair" structure, which is
what makes the pair multiplicity exactly 2 = m-1 = the (OV) pair-intersection
cap, automatically.

Combinatorial target derived by hand in PREREG R2 and refined here:
  * 10 sigma-orbits of D form W (a = 20 points);
  * 9 of them realise 9 DISTINCT slope pairs whose graph H has max degree 2 and
    spans EXACTLY 10 vertices (=> exactly one path component);
  * the 10th orbit is S_g ^ S_h (the m-1 = 2 middle points), pair {al0, be0}
    with al0, be0 outside V(H); al0 is the 11th type-2 slope, be0 = mu.
  * X_gamma = 2*deg_H(gamma) in {2,4}; X_al0 = 2.  Sum X = 38.  Per-side
    counts = deg_H <= 2 = m-1.  All caps automatic.

This script only searches for phi and the subgraph H; m3_build.py completes
the configuration outside W and verifies everything.
"""

import random
import sys

sys.path.insert(0, "notes/pilots_20260811/r34_bivcurve_m34")
from biv_core import mu_N

m = 3
N, rho, T, a, R = 16 * m, 4 * m - 1, 4 * m + 1, 7 * m - 1, 8 * m

out = []
P = out.append


def cev(c, x, q):
    v = 0
    for co in reversed(c):
        v = (v * x + co) % q
    return v


def find_H(edges, nedge=9, nvert=10):
    """edges : list of (orbit_index, (u,v)).  Return a list of nedge orbit
    indices whose pairs are distinct, have max degree <= 2, and span exactly
    nvert vertices; else None."""
    n = len(edges)
    deg = {}
    chosen = []
    used_pairs = set()

    def rec(i):
        if len(chosen) == nedge:
            return len(deg) == nvert
        if n - i < nedge - len(chosen):
            return False
        for j in range(i, n):
            oi, (u, v) = edges[j]
            key = (u, v) if u < v else (v, u)
            if key in used_pairs:
                continue
            if deg.get(u, 0) >= 2 or deg.get(v, 0) >= 2:
                continue
            newv = (0 if u in deg else 1) + (0 if v in deg else 1)
            if len(deg) + newv > nvert:
                continue
            # feasibility: remaining edges must still allow nvert exactly
            deg[u] = deg.get(u, 0) + 1
            deg[v] = deg.get(v, 0) + 1
            used_pairs.add(key)
            chosen.append(oi)
            if rec(j + 1):
                return True
            chosen.pop()
            used_pairs.discard(key)
            for w in (u, v):
                deg[w] -= 1
                if deg[w] == 0:
                    del deg[w]
        return False

    if rec(0):
        return list(chosen)
    return None


def search(q, seed, trials):
    D = mu_N(q, N)
    Dset = set(D)
    # sigma-orbits {x,-x}; -x is in mu_48 since 2 | 48
    orbits, seen = [], set()
    for x in D:
        if x in seen:
            continue
        y = (q - x) % q
        assert y in Dset
        seen.add(x)
        seen.add(y)
        orbits.append((x, y))
    assert len(orbits) == N // 2
    rnd = random.Random(seed)
    best = None
    for tr in range(trials):
        A = [rnd.randrange(q) for _ in range(4)]
        B = [rnd.randrange(q) for _ in range(4)]
        phi, ok = {}, True
        for x in D:
            bx = cev(B, x, q)
            if bx == 0:
                ok = False
                break
            phi[x] = cev(A, x, q) * pow(bx, q - 2, q) % q
        if not ok:
            continue
        edges = []
        for oi, (x, y) in enumerate(orbits):
            if phi[x] != phi[y]:
                edges.append((oi, (phi[x], phi[y])))
        if len(edges) < 10:
            continue
        # a quick necessary condition: >= 8 values with >= 2 incidences
        cnt = {}
        for _, (u, v) in edges:
            cnt[u] = cnt.get(u, 0) + 1
            cnt[v] = cnt.get(v, 0) + 1
        hubs = sum(1 for c in cnt.values() if c >= 2)
        if hubs < 8:
            continue
        H = find_H(edges, 9, 10)
        if H is None:
            continue
        VH = set()
        for oi in H:
            x, y = orbits[oi]
            VH.add(phi[x])
            VH.add(phi[y])
        # the middle orbit: pair disjoint from V(H)
        mid = None
        for oi, (u, v) in edges:
            if oi in H:
                continue
            if u not in VH and v not in VH and u != v:
                mid = (oi, u, v)
                break
        if mid is None:
            continue
        best = dict(q=q, A=A, B=B, orbits=orbits, phi=phi, H=H, VH=sorted(VH),
                    mid=mid, trial=tr, D=D)
        return best
    return None


P("=" * 78)
P("r34 D1/D2 -- CONSTRUCTIVE (BIV-CURVE) SEARCH AT m = 3   [(SPLIT-m) + sigma]")
P("=" * 78)
P("m=%d  N=%d  rho=%d  T=rho+2=%d  a=7m-1=%d  R=%d  e=m=%d" % (m, N, rho, T, a, R, m))
P("G(Z,x) = (B(x)Z-A(x))(B(-x)Z-A(-x)) : deg_Z = %d = m-1, deg_x <= %d = 3m-3"
  % (m - 1, 3 * m - 3))
P("")

for q in ((97, 193) if __name__ == "__main__" else ()):
    P("-" * 78)
    P("q = %d   (48 | q-1 : %s)" % (q, (q - 1) % 48 == 0))
    cfg = search(q, 340000 + q, 400000)
    if cfg is None:
        P("  NO phi found within the search budget")
        continue
    phi, orbits = cfg["phi"], cfg["orbits"]
    P("  FOUND at trial %d :  A = %s   B = %s  (ascending coeffs)"
      % (cfg["trial"], cfg["A"], cfg["B"]))
    P("  selected orbits H (9) :")
    degH = {}
    for oi in cfg["H"]:
        x, y = orbits[oi]
        P("    orbit %2d : x=%3d  -x=%3d   pair {%d, %d}" % (oi, x, y, phi[x], phi[y]))
        degH[phi[x]] = degH.get(phi[x], 0) + 1
        degH[phi[y]] = degH.get(phi[y], 0) + 1
    P("  V(H) = %s   (|V(H)| = %d)" % (cfg["VH"], len(cfg["VH"])))
    P("  deg_H = %s" % sorted(degH.values()))
    oi, u, v = cfg["mid"]
    x, y = orbits[oi]
    P("  middle orbit %d : m1=%d m2=%d  pair {al0=%d, be0=%d}" % (oi, x, y, u, v))
    P("  => X_gamma = 2*deg_H : %s  plus X_al0 = 2 ; sum X = %d (target 38)"
      % (sorted(2 * d for d in degH.values()),
         sum(2 * d for d in degH.values()) + 2))
    P("  slopes = %d (10 in V(H) + al0) = T_2 = rho = %d : %s"
      % (len(cfg["VH"]) + 1, rho, len(cfg["VH"]) + 1 == rho))
    W = []
    for ooi in cfg["H"] + [oi]:
        W.extend(orbits[ooi])
    P("  W (a=%d) = %s" % (len(W), sorted(W)))

if __name__ == "__main__":
    P("")
    P("=" * 78)
    print("\n".join(out))
    with open("notes/pilots_20260811/r34_bivcurve_m34/m3_phi_results.txt", "w") as f:
        f.write("\n".join(out) + "\n")
