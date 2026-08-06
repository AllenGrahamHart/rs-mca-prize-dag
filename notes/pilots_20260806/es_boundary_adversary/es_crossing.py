#!/usr/bin/env python3
"""Round 16 -- (ES) boundary adversary: THE CROSSING SHAPE at n = 32.

The crossing row is  r' = n - k - w  with k = n/2, i.e.  r' + w = n/2.
At n = 32 the census-reachable crossing row is  r' = 8, w = 8.

Why this row matters: at (n=32, r'=8, w=8, delta=1) we have |Z_w| = 7, so
p^{|Z_w|} >= 97^7 = 2^46.2 >= 2^32 = 2^n.  An accident here would be below
BOTH balance readings -- the per-weight one AND the global one
(2^n <= p^{|Z_w|}) used by the HARDENED floor node
critical/nodes/u2c_giant_tnull_dichotomy.  So this row can break the strong
reading, unlike the five witnesses already banked by this pilot.

Exact bad-prime census over ALL characteristics, orbit-reduced on the
fundamental domain {0 in S} (every orbit contains such a set), with a lazy
norm ladder: I_S contains (x_1, x_2), so gcd(N(x_1), N(x_2)) = 1 already
kills every window w >= 3.

run:  tools/ramguard local -- python3 -u notes/pilots_20260806/\
es_boundary_adversary/es_crossing.py
"""

import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from es_lib import (M_of, UnfactoredCofactor, coord_vector, cyclotomic_closure,
                    factorize, field_norm, mult_order, pgcd, phi_n_poly, pnorm)

N = 32
RP = 8
WMAX = 8
# only the CROSSING window r' + w = n/2 is measured here (w = 8); the other
# windows at this weight are not the crossing shape and are covered by the
# es_census.py runs at r' <= 6.
WLIST = [8]


def colex(n, r):
    c = list(range(r))
    while True:
        yield tuple(c)
        i = 0
        while i < r and c[i] + 1 == (c[i + 1] if i + 1 < r else n):
            i += 1
        if i == r:
            return
        c[i] += 1
        for j in range(i):
            c[j] = j


def main():
    n, rp = N, RP
    binom = [[math.comb(a, b) for b in range(rp + 2)] for a in range(n + 1)]
    # fundamental domain: subsets containing 0, indexed by the other rp-1
    # elements (values 1..n-1 shifted to 0..n-2) in colex rank
    tot = math.comb(n - 1, rp - 1)
    seen = bytearray(tot)
    print("=" * 78)
    print("ROUND 16 -- CROSSING SHAPE  n=%d, r'=%d (r'+w = n/2 at w=%d)"
          % (n, rp, n // 2 - rp))
    print("=" * 78)
    print("fundamental domain {0 in S}: %d sets" % tot)

    def rank0(S):
        """colex rank of a 0-containing set S within the domain."""
        return sum(binom[v - 1][j + 1] for j, v in enumerate(S[1:]))

    reps = 0
    accid = {w: 0 for w in WLIST}
    badp = {w: {} for w in WLIST}
    unfact = []
    PHI = phi_n_poly(n)

    for pos, rest in enumerate(colex(n - 1, rp - 1)):
        if seen[pos]:
            continue
        reps += 1
        S = (0,) + tuple(v + 1 for v in rest)
        # mark the whole orbit's 0-containing members
        for c in range(1, n, 2):
            base = [(c * i) % n for i in S]
            for shift in base:
                img = tuple(sorted((i - shift) % n for i in base))
                seen[rank0(img)] = 1
        Sl = list(S)
        # lazy norm ladder
        norms = {}
        for s in (1, 2):
            norms[s] = field_norm(coord_vector(Sl, s, n), n)
        smin = None
        for s in (1, 2):
            if norms[s] != 0:
                smin = s
                break
        if 2 in WLIST and norms[1] != 0:
            accid[2] += 1
            try:
                for p in factorize(abs(norms[1])):
                    if p != 2:
                        badp[2].setdefault(p, S)
            except UnfactoredCofactor as e:
                unfact.append((2, S, str(e)))
        g12 = math.gcd(abs(norms[1]), abs(norms[2]))
        if g12 == 1 and smin is not None:
            # I_S contains x_1, x_2 with coprime norms -> no prime divides
            # N(I_S); no bad primes for any w >= 3
            for w in WLIST:
                if w >= 3 and smin < w:
                    accid[w] += 1
            continue
        for w in [x for x in WLIST if x >= 3]:
            for s in range(1, w):
                if s not in norms:
                    norms[s] = field_norm(coord_vector(Sl, s, n), n)
            sm = None
            for s in range(1, w):
                if norms[s] != 0:
                    sm = s
                    break
            if sm is None:
                continue            # periodic in char 0 -> structural
            accid[w] += 1
            g = 0
            for s in range(1, w):
                if norms[s]:
                    g = math.gcd(g, abs(norms[s]))
            if g <= 1:
                continue
            try:
                facs = factorize(g)
            except UnfactoredCofactor as e:
                unfact.append((w, S, str(e)))
                continue
            for p in sorted(facs):
                if p == 2:
                    continue
                gg = PHI
                for s in range(1, w):
                    v = pnorm(coord_vector(Sl, s, n), p)
                    if not v:
                        continue
                    gg = pgcd(gg, v, p)
                    if len(gg) - 1 < 1:
                        break
                if len(gg) - 1 >= 1:
                    badp[w].setdefault(p, S)

    print("orbit representatives processed: %d" % reps)
    print()
    print("  %-4s %-5s %-9s %-12s %-11s %-7s %-9s %-9s"
          % ("w", "M", "struct", "acc-orbits", "max in-sc p", "delta", "Lam",
             "global?"))
    hits = []
    for w in WLIST:
        M = M_of(w)
        st = binom[n // M][rp // M] if rp % M == 0 else 0
        prim = badp[w]
        insc = [p for p in prim if mult_order(p, n) in (1, 2, 4) and p > w]
        if not insc:
            print("  %-4d %-5d %-9d %-12d %-11s %-7s %-9s %-9s"
                  % (w, M, st, accid[w], max(prim) if prim else "-", "-",
                     "-", "-"))
            continue
        best = max(insc)
        zw = len(cyclotomic_closure(w, n, best))
        lam = math.log2(math.comb(n, rp)) - zw * math.log2(best)
        glob = best ** zw >= 2 ** n
        print("  %-4d %-5d %-9d %-12d %-11d %-7d %-9.2f %-9s"
              % (w, M, st, accid[w], best, mult_order(best, n), lam,
                 "YES" if glob else "no"))
        for p in sorted(insc):
            zwp = len(cyclotomic_closure(w, n, p))
            lamp = math.log2(math.comb(n, rp)) - zwp * math.log2(p)
            if lamp < 0:
                hits.append((w, p, mult_order(p, n), zwp, lamp,
                             p ** zwp >= 2 ** n, prim[p]))

    print("\n" + "=" * 78)
    print("SUB-BALANCE ACCIDENTS AT THE CROSSING SHAPE: %d" % len(hits))
    for w, p, d, zw, lam, glob, S in sorted(hits, key=lambda z: z[4]):
        print("  w=%d p=%d delta=%d |Z_w|=%d Lam=%+.3f GLOBAL-sub=%s S=%s"
              % (w, p, d, zw, lam, "YES" if glob else "no", list(S)))
    if unfact:
        print("UNFACTORED COFACTORS (honest gap): %d" % len(unfact))
        for u in unfact[:4]:
            print("   w=%d %s" % (u[0], u[2]))
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
