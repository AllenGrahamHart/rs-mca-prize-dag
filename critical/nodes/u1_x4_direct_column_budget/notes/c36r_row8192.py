#!/usr/bin/env python3
"""c36r independent replay of ONE official n=8192 row (worst 12-prime row).

p=67239937 (first official prime for n=8192). Verifies:
  N_3to1 = 66,933,997 (banked), overlap max on quotient support in [14,20],
  X_35 = 0, P(1)=I one-shift, R(1)=n-1, quotient mass, repaired threshold
  ratio ~ 2.774% (not the stale 2.772%).
Memory: two uint32 count arrays of size p (~538MB total), chunked add.at.
"""
from __future__ import annotations

import sys

import numpy as np

P_PRIME = 67_239_937
N_ORDER = 8_192


def main() -> None:
    p = int(sys.argv[1]) if len(sys.argv) > 1 else P_PRIME
    n = N_ORDER
    assert (p - 1) % n == 0 and p >= n * n
    # element of order exactly n (n = 2^13)
    g = 0
    for c in range(2, 100):
        v = pow(c, (p - 1) // n, p)
        if v != 1 and pow(v, n // 2, p) != 1:
            g = v
            break
    assert g
    H = np.empty(n, dtype=np.int64)
    x = 1
    for i in range(n):
        H[i] = x
        x = x * g % p
    assert x == 1 and len(np.unique(H)) == n
    shifted = ((1 - H) % p)
    shifted = shifted[shifted != 0]
    assert shifted.size == n - 1
    inv = np.array([pow(int(a), p - 2, p) for a in shifted], dtype=np.int64)

    Pc = np.zeros(p, dtype=np.uint32)
    Rc = np.zeros(p, dtype=np.uint32)
    chunk = 128
    for i0 in range(0, shifted.size, chunk):
        sa = shifted[i0:i0 + chunk]
        prod = (sa[:, None] * shifted[None, :]) % p
        np.add.at(Pc, prod.ravel(), 1)
        quot = (sa[:, None] * inv[None, :]) % p  # d * c^{-1}
        np.add.at(Rc, quot.ravel(), 1)
    del prod, quot

    assert int(Rc[1]) == n - 1, Rc[1]
    total_R = int(Rc.sum())
    assert total_R == (n - 1) ** 2
    assert total_R - int(Rc[1]) == (n - 1) * (n - 2)

    # one-shift I = #{(u,v) in H^2 : u+v=1}
    Hset = set(int(h) for h in H)
    I = sum(1 for u in Hset if (1 - u) % p in Hset)
    assert int(Pc[1]) == I, (Pc[1], I)

    # N_3to1, overlap max on support, X_35 (chunked int64)
    N = 0
    overlap_max = 0
    x35 = 0
    step = 1 << 22
    for a0 in range(0, p, step):
        pa = Pc[a0:a0 + step].astype(np.int64)
        ra = Rc[a0:a0 + step].astype(np.int64)
        if a0 == 0:
            ra_ex = ra.copy()
            ra_ex[1] = 0  # exclude t=1 from support stats
        else:
            ra_ex = ra
        N += int((pa * ra).sum())
        sup = ra_ex > 0
        if sup.any():
            overlap_max = max(overlap_max, int(pa[sup].max()))
            x35 += int((np.maximum(pa - 35, 0) * ra_ex).sum())
    print(f"p={p} n={n}")
    if p == 67_239_937:
        print(f"N_3to1={N} (banked 66933997) "
              f"{'MATCH' if N == 66_933_997 else 'MISMATCH'}")
    else:
        print(f"N_3to1={N}")
    print(f"I=P(1)={I}, overlap_max={overlap_max} (claimed range 14..20)")
    print(f"X_35={x35} (claimed 0)")
    if p == 67_657_729:
        # rich-fiber claims: P(t)=20, R(t)=1 at t=40697698; t=1+q telescoping
        t = 40_697_698
        print(f"P({t})={int(Pc[t])} (claimed 20), R({t})={int(Rc[t])} (claimed 1)")
        q = (t - 1) % p
        in_H = q in Hset
        full_order = in_H and pow(q, n // 2, p) != 1
        c_w, d_w = (1 - q) % p, (1 - q * q % p) % p
        witness_ok = (d_w * pow(c_w, p - 2, p)) % p == t
        print(f"telescoping q=t-1 in H: {in_H}, order n: {full_order}, "
              f"witness (1-q,1-q^2) has d/c=t: {witness_ok}")
    thr_repaired = 36 * n**2 - 16 * n ** (4 / 3) - n / 2
    thr_stale = 36 * n**2 - 8 * n ** (4 / 3) - n / 2
    print(f"repaired threshold={thr_repaired:.1f} ratio={N / thr_repaired:.6f}")
    print(f"stale threshold={thr_stale:.1f} stale ratio={N / thr_stale:.6f}")
    print("C36R_ROW8192_REPLAY_DONE")


if __name__ == "__main__":
    main()
