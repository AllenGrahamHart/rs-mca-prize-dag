#!/usr/bin/env python3
"""Exact relation certificates for the low-weight rows of the 2N=32 sweep.

A ternary relation sum_i d_i omega^i = 0 (mod q) with omega of exact order 2N
is the statement that the polynomial f(x) = sum d_i x^i (deg < N, coefficients
in {-1,0,1}) satisfies f(omega) = 0 in F_q, i.e.

        q  |  Norm(f) := Res(f(x), x^N + 1) = prod_{j odd} f(zeta_{2N}^j),

an EXACT nonzero integer of absolute value at most wt(f)^N and independent of q.
So the rows carrying a weight-w relation are exactly the prime divisors
q = 1 (mod 2N) of the finite integer list {Norm(f) : wt(f) = w}: a q-independent
height certificate and an exact resultant router on the RELATION side (the
analogue of, and much sharper than, the small-doubling-orbit router
q | 2^(2N r) - 1 on the dynamics side).

This script recovers an actual minimum-weight relation for each requested q and
verifies q | Norm(f) in exact integer arithmetic.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations, product

import orbit_spectrum as osp


def find_min_relation(coeffs: list[int], q: int, wmax: int):
    """Smallest-weight nonzero d in {-1,0,1}^N with sum d_i coeffs_i = 0 (mod q)."""
    n = len(coeffs)
    for w in range(1, wmax + 1):
        for pos in combinations(range(n), w):
            for signs in product((1, -1), repeat=w - 1):
                s = coeffs[pos[0]]
                d = [0] * n
                d[pos[0]] = 1
                for p, sg in zip(pos[1:], signs):
                    s += sg * coeffs[p]
                    d[p] = sg
                if s % q == 0:
                    return w, d
    return None, None


def norm_mod_xN_plus_1(d: list[int]) -> int:
    """Res(f, x^N+1) = det of multiplication-by-f on Z[x]/(x^N+1) (exact, Bareiss)."""
    n = len(d)
    # circulant-with-sign (negacyclic) matrix M[i][j] = coefficient of x^i in x^j f(x)
    M = [[0] * n for _ in range(n)]
    for j in range(n):
        for i, c in enumerate(d):
            k = i + j
            M[k % n][j] += c * (-1 if k >= n else 1)
    # fraction-free Gaussian elimination (Bareiss)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            for r in range(k + 1, n):
                if M[r][k]:
                    M[k], M[r] = M[r], M[k]
                    sign = -sign
                    break
            else:
                return 0
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
            M[i][k] = 0
        prev = M[k][k]
    return sign * M[n - 1][n - 1]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--twoN", type=int, default=32)
    ap.add_argument("--qs", required=True)
    ap.add_argument("--wmax", type=int, default=8)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    N = args.twoN // 2
    out = []
    for q in [int(x) for x in args.qs.split(",")]:
        omega = osp.root_of_order(q, args.twoN)
        coeffs = [pow(omega, i, q) for i in range(N)]
        w, d = find_min_relation(coeffs, q, args.wmax)
        rec = {"q": q, "twoN": args.twoN, "min_weight_found": w, "relation": d}
        if d is not None:
            nrm = norm_mod_xN_plus_1(d)
            rec.update({
                "Norm_f": str(nrm), "abs_Norm_f": str(abs(nrm)),
                "bound_w_pow_N": str(w ** N),
                "q_divides_Norm": (nrm % q == 0) if nrm else None,
                "Norm_nonzero": nrm != 0,
                "cofactor": str(abs(nrm) // q) if nrm and nrm % q == 0 else None,
            })
        out.append(rec)
        print(json.dumps(rec))
    with open(args.out, "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main()
