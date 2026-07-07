#!/usr/bin/env python3
"""M_B-vs-f1-ledger audit at the KoalaBear-shaped official row.
Exact integer arithmetic (math.comb / pow) with log2 read off bit lengths;
cross-checked against lgamma. Small: seconds, <200MB."""
import math
from math import lgamma, log2

def log2_int(x):
    """log2 of a positive int, accurate to ~1e-12."""
    b = x.bit_length()
    if b <= 64:
        return log2(x)
    top = x >> (b - 64)
    return (b - 64) + log2(top)

def log2_comb(n, m):
    return (lgamma(n+1) - lgamma(m+1) - lgamma(n-m+1)) / math.log(2)

# ---- rows ----
KB_P  = 2**31 - 2**24 + 1      # KoalaBear prime
M31_P = 2**31 - 1              # Mersenne-31
N     = 2**21
K     = 2**20
rows = [
    ("KoalaBear list", KB_P, 6, 1116046),
    ("M31 list",       M31_P, 2, 1116022),   # their deployed (K,m); M31 tower deg 2 for the circle rows
]

for name, p, ext_deg, m in rows:
    w  = m - K
    lp = log2(p)
    print(f"\n===== {name}: n=2^21 K=2^20 m={m} w'={w} log2p={lp:.6f} =====")
    print(f"{'d1':>10} {'m~':>9} {'log2C(m~,m)':>12} {'log2C(n,m~)':>14} {'(d1-1)log2p':>14} {'log2 M_B':>10} {'E_tan=C*p^(K-m~)':>18}")
    for j in range(0, 5):
        d1 = w + 1 + j
        mp = K - 1 + d1          # m' level
        assert mp == m + j
        lc_spray = log2_comb(mp, m)          # C(m', m)
        lc_big   = log2_comb(N, mp)          # C(n, m')
        floor_bits = lc_spray + lc_big - (d1-1)*lp
        # weld identity check: p^{-(d1-1)} == p^{K-m'}
        assert (d1 - 1) == (mp - K)
        etan = lc_big - (mp - K)*lp          # log2 of the base tangent mean
        print(f"{d1:>10} {mp:>9} {lc_spray:>12.2f} {lc_big:>14.2f} {(d1-1)*lp:>14.2f} {floor_bits:>10.1f} {etan:>18.1f}")

# exact-integer verification of the two headline boundary values
print("\n--- exact-integer boundary verification (bit-length arithmetic) ---")
for name, p, m in [("KoalaBear", KB_P, 1116046), ("M31", M31_P, 1116022)]:
    w = m - K
    num = math.comb(N, m)
    den = pow(p, w)
    bits = log2_int(num) - log2_int(den)
    print(f"{name}: log2( C(2^21,{m}) / p^{w} ) = {bits:.2f}  (printed upstream: {'67.1' if name=='KoalaBear' else '52.1'})")

# ---- per-level tower table at the KoalaBear row (levels d | 6) ----
p, m = KB_P, 1116046
w = m - K; lp = log2(p)
print("\n===== per-level tower floors at KoalaBear row: M_{p^d}(d1), d in {1,2,3,6} =====")
print(f"{'d1':>8} " + " ".join(f"{'lvl d='+str(d):>16}" for d in (1,2,3,6)))
for j in range(0, 3):
    d1 = w + 1 + j
    mp = m + j
    lc = log2_comb(mp, m) + log2_comb(N, mp)
    vals = [lc - (d1-1)*d*lp for d in (1,2,3,6)]
    print(f"{d1:>8} " + " ".join(f"{v:>16.1f}" for v in vals))

# ---- gate at the F-row ----
gate = 6*lp - 128
print(f"\nF-row gate log2(q * 2^-128) = 6*log2(p) - 128 = {gate:.2f}")
print(f"boundary floor {log2_comb(N,m)- (w)*lp + 0:.1f} vs gate {gate:.2f} vs first interior — straddle check")

# ---- F2 window arithmetic at the KoalaBear-shaped row ----
print("\n===== F2 EXTRAS-BUDGET window audit at the KoalaBear-shaped row =====")
lq = 6*lp
t_min = math.ceil(N / lq)               # q-scale global-balance minimum t
t_2pc = math.ceil(1.02 * N / lq)        # with the ~2% margin
for t in (t_min, t_2pc):
    q_side = t * lq
    p_side = t * lp
    print(f"t={t}:  q-scale t*log2q = {q_side:,.0f} vs n = {N:,}  -> q-window {'ADMITS (sub-balance)' if q_side>=N else 'excludes'}")
    print(f"        TRUE value scale t*log2p = {p_side:,.0f} vs n = {N:,} -> deficit 2^{N-p_side:,.0f} (above balance at base scale)")
    # pigeonhole mass at half-fill
    half = log2_comb(N, N//2)
    print(f"        pigeonhole: some prefix fiber >= C(n,n/2)/p^t = 2^{half - p_side:,.0f}  (budget n^3 = 2^63)")
    # NB: n^3 at THIS row = (2^21)^3 = 2^63; the floor's 2^123 was n=2^41 prize-max
print(f"\ncoset-union family bound at t={t_2pc}: #unions <= 2^(n/t) = 2^{N/t_2pc:.0f} (negligible vs the fiber mass)")
