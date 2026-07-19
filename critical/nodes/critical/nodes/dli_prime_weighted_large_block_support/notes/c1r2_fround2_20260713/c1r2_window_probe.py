#!/usr/bin/env python3
"""Window-robustness probe: is the C1' kill specific to the pose window w in
[L+1,L+5], or robust to extending the ledger window? For each kill q (L=1),
compute primitive-orbit counts at weights 2..WMAX and report cumulative W_cl and
K' as the window's upper edge grows. NOTE: extending w_max beyond L+5 CHANGES
the conjecture; this only informs round-3 (a possible reposed C1'').

argv: L  q1,q2,...  WMAX
Enumerator verbatim shape from m2_c1prime_level_scaled_modal.py.
"""
from __future__ import annotations
import itertools, sys
from fractions import Fraction
import numpy as np

N = 32
NPRIME = 64


def primitive_root(q):
    rem = q - 1; fac = set(); d = 2
    while d * d <= rem:
        while rem % d == 0:
            fac.add(d); rem //= d
        d += 1
    if rem > 1:
        fac.add(rem)
    c = 2
    while any(pow(c, (q - 1) // f, q) == 1 for f in fac):
        c += 1
    return c


def omega_of(q):
    return pow(primitive_root(q), (q - 1) // NPRIME, q)


def orbit_key(vec):
    best = None
    for shift in range(NPRIME):
        moved = [0] * N
        for e, c in enumerate(vec):
            if c == 0:
                continue
            t = (e + shift) % NPRIME
            if t >= N:
                moved[t - N] -= c
            else:
                moved[t] += c
        k = tuple(moved)
        if best is None or k < best:
            best = k
    return best


def primitive_orbit_count(q, level, weight):
    omega = omega_of(q)
    odd_powers = [np.array([pow(omega, (2 * ell - 1) * e, q) for e in range(N)], dtype=np.int64)
                  for ell in range(1, level + 1)]
    signs = np.array(list(itertools.product((1, -1), repeat=weight - 1)), dtype=np.int64)
    signs = np.hstack([np.ones((len(signs), 1), dtype=np.int64), signs])
    combos = itertools.combinations(range(N), weight)
    reps = set()
    while True:
        block = list(itertools.islice(combos, 100_000))
        if not block:
            break
        sup = np.asarray(block, dtype=np.int64)
        hit = np.ones((len(sup), len(signs)), dtype=bool)
        for powers in odd_powers:
            hit &= (powers[sup] @ signs.T) % q == 0
        for si, gi in np.argwhere(hit):
            support = tuple(int(v) for v in sup[si]); signed = tuple(int(v) for v in signs[gi])
            prim = True
            for mask in range(1, (1 << weight) - 1):
                if all(sum(signed[k] * pow(omega, (2 * ell - 1) * support[k], q)
                           for k in range(weight) if (mask >> k) & 1) % q != 0
                       for ell in range(1, level + 1)):
                    continue
                if all(sum(signed[k] * pow(omega, (2 * ell - 1) * support[k], q)
                           for k in range(weight) if (mask >> k) & 1) % q == 0
                       for ell in range(1, level + 1)):
                    prim = False; break
            if not prim:
                continue
            vec = [0] * N
            for e, c in zip(support, signed):
                vec[e] = c
            reps.add(orbit_key(tuple(vec)))
    return len(reps)


def a_total(q, L):
    z = omega_of(q)
    dp = np.zeros((q,) * L, dtype=np.int64); dp[(0,) * L] = 1
    axes = tuple(range(L))
    for i in range(N):
        vp = tuple(pow(z, ((2 * ell - 1) * i) % NPRIME, q) for ell in range(1, L + 1))
        vm = tuple((q - x) % q for x in vp)
        dp = 2 * dp + np.roll(dp, vp, axis=axes) + np.roll(dp, vm, axis=axes)
    return int(dp[(0,) * L])


def main():
    L = int(sys.argv[1]); qs = [int(x) for x in sys.argv[2].split(",")]; WMAX = int(sys.argv[3])
    for q in qs:
        em1 = Fraction(q ** L * a_total(q, L), 4 ** N) - 1
        r = Fraction(q ** L, 2 ** N)
        counts = {w: primitive_orbit_count(q, L, w) for w in range(2, WMAX + 1)}
        print(f"\nq={q} L={L} (E-1)/r={float(em1/r):.4f}  orbit counts={counts}")
        # cumulative W_cl over window [L+1 .. edge] for each edge from L+5 up to WMAX
        for edge in range(L + 5, WMAX + 1):
            W = sum(Fraction(counts[w] * NPRIME, 2 ** w) for w in range(L + 1, edge + 1))
            k = em1 / (r * (1 + W))
            tag = "POSE(w_max=L+5)" if edge == L + 5 else f"window[2..{edge}]"
            print(f"   {tag:>18}: W_cl={float(W):.3f}  K'={float(k):.4f}  "
                  f"{'KILL(>4)' if k > 4 else 'amber(>=1)' if k >= 1 else 'survives'}")


if __name__ == "__main__":
    main()
