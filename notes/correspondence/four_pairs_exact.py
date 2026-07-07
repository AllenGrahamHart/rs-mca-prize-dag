#!/usr/bin/env python3
"""Exact-integer replay of ALL FOUR upstream adjacent pairs from the single
tangent-mean formula family:
  list row : unsafe(m)  <=>  C(n,m) > p^(m-K)   * floor(q * eps)
  MCA row  : unsafe(m)  <=>  C(n,m) > p^(m-K-1) * floor(q * eps)   [pencil dof]
Their printed pairs/margins: KB MCA 1116047/1116048 @22.2 (+9.0/-22.2),
KB list 1116046/1116047 @22.0, M31 MCA 1116023/1116024 @3.3 (+27.9/-3.3),
M31 list 1116022/1116023 @3.1."""
import math

def log2_int(x):
    b = x.bit_length()
    if b <= 64: return math.log2(x)
    return (b - 64) + math.log2(x >> (b - 64))

N, K = 2**21, 2**20
rows = [
    ("KoalaBear MCA ", 2**31-2**24+1, 6, 128, 1, 1116047),
    ("KoalaBear list", 2**31-2**24+1, 6, 128, 0, 1116046),
    ("M31 MCA       ", 2**31-1,       4, 100, 1, 1116023),
    ("M31 list      ", 2**31-1,       4, 100, 0, 1116022),
]
print(f"{'row':>15} {'a0':>8} {'unsafe@a0':>10} {'safe@a0+1':>10} {'margin(bits)':>13} {'printed':>8}")
for name, p, e, eps, pencil, a0 in rows:
    gate = pow(p, e) >> eps          # floor(q * 2^-eps)
    res = {}
    for m in (a0, a0+1):
        lhs = math.comb(N, m)
        rhs = pow(p, m - K - pencil) * gate
        res[m] = (lhs > rhs, log2_int(lhs) - log2_int(rhs))
    ok = res[a0][0] and not res[a0+1][0]
    print(f"{name:>15} {a0:>8} {'+%.3f'%res[a0][1]:>10} {'%.3f'%res[a0+1][1]:>10} "
          f"{abs(res[a0+1][1]):>13.3f} {'PAIR OK' if ok else 'MISMATCH':>8}")
