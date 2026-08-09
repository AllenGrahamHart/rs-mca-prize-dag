#!/usr/bin/env python3
"""pincer_formalization (round 27) -- D0 arithmetic + D2 negative control.

D0 : the exact load-bearing arithmetic of the "safe side above sigma*" claim.
D2 : the negative control -- the RANDOM-WORD first-moment crossing
     sigma_FM^rand(q) = t*(q) vs the PROVED worst-word crossing
     sigma_RH(q) = a_RH(q) - k on the determined region 2^128 < q < 2^166.5,
     where a_RH(q) = n - floor(q/2^128) + 1 is unconditional
     (background/nodes/rate_half_quadratic_exact_range, (RQ1)).

Stdlib only.  Functionals named in PREREG R0.
"""
from math import lgamma, log

LOG2 = log(2.0)
n, k = 1 << 41, 1 << 40


def log2C(N, m):
    if m < 0 or m > N:
        return float("-inf")
    return (lgamma(N + 1) - lgamma(m + 1) - lgamma(N - m + 1)) / LOG2


def t_star(L):
    """sigma_FM^rand: min { t : t*L >= log2 C(n, n-k-t) + 128 }."""
    lo, hi = 1, n - k
    while lo < hi:
        mid = (lo + hi) // 2
        if mid * L >= log2C(n, n - k - mid) + 128.0:
            hi = mid
        else:
            lo = mid + 1
    return lo


SIGMA_STAR = 8_592_912_738           # s* = t*(255.9) - 1
SIGMA_0 = 8_594_128_895              # dc+c-1, c=2^22, d=2048 (wave-9 floor)
SIGMA_OPT = (1 << 34) - 1            # c=2^33, d=1 (wave-10 optimized floor)
B_Q = 389_500_552_609

print("=== D0.A  the three constants that decide the verdict ===")
print(f"  s*      (random-word FM last-unsafe excess, L=255.9) = {SIGMA_STAR:,}")
print(f"  sigma_0 (PROVED unsafe reach, wave-9)                = {SIGMA_0:,}")
print(f"  2^34-1  (PROVED unsafe reach, wave-10 optimized)     = {SIGMA_OPT:,}")
print(f"  sigma_0 - s*      = {SIGMA_0 - SIGMA_STAR:,}   (expect 1,216,157)")
print(f"  (2^34-1) - s*     = {SIGMA_OPT - SIGMA_STAR:,}   (expect 8,586,956,445)")
print(f"  (2^34-1) / s*     = {SIGMA_OPT / SIGMA_STAR:.6f}")
print(f"  s* inside proved-unsafe interval (0, 2^34-1]?  "
      f"{'YES -- SAFE-ABOVE-SIGMA* IS FALSE' if SIGMA_STAR <= SIGMA_OPT else 'no'}")

print("\n=== D0.B  the only in-repo rate-half MCA SAFE theorem (HD1) ===")
hd_sigma = 3 * n // 4 - k
print(f"  rate_half_half_distance_safe_bracket: B_mca(3n/4) <= n <= floor(q/2^128)")
print(f"  its excess  3n/4 - k = {hd_sigma:,}  = 2^{hd_sigma.bit_length()-1}")
print(f"  ratio to the claimed safe point s*: {hd_sigma / SIGMA_STAR:.3f}x")
print(f"  ratio to the proved unsafe reach 2^34-1: {hd_sigma / SIGMA_OPT:.3f}x")

print("\n=== D0.C  FLOOR v2 band vs the PROVED bracket at the razor rows ===")
floor_v2_band = SIGMA_STAR - (1 << 33)
true_band = (1 << 39) - (1 << 34)
print(f"  FLOOR v2 band  (2^33, s*]            width = {floor_v2_band:,}")
print(f"  PROVED bracket [2^34, 2^39] width          = {true_band:,}")
print(f"  widening factor                            = {true_band / floor_v2_band:,.1f}"
      f"   (= 2^{log(true_band/floor_v2_band, 2):.3f})")
print(f"  is s* inside the proved bracket [2^34, 2^39]? "
      f"{'yes' if (1 << 34) <= SIGMA_STAR <= (1 << 39) else 'NO -- s* < 2^34, outside'}")

print("\n=== D2  negative control: FM vs the PROVED crossing, determined region ===")
print(f"{'log2 q':>8} {'B=q/2^128':>16} {'sigma_RH (PROVED)':>20} "
      f"{'sigma_FM (random)':>19} {'rho':>8}")
rows = []
for Lint in list(range(129, 167)) + [166.502834419]:
    L = float(Lint)
    B = int(2 ** (L - 128)) if L != 166.502834419 else B_Q
    if B > B_Q:
        continue
    s_rh = n - B + 1 - k
    s_fm = t_star(L)
    rho = s_rh / s_fm
    rows.append((L, B, s_rh, s_fm, rho))
for L, B, s_rh, s_fm, rho in rows:
    if L in (129.0, 140.0, 150.0, 160.0, 166.0, 166.502834419):
        print(f"{L:>8} {B:>16,} {s_rh:>20,} {s_fm:>19,} {rho:>8.2f}")
rhos = [r[4] for r in rows]
print(f"  rho range over 2^129..2^166.503 : [{min(rhos):.2f}, {max(rhos):.2f}]  "
      f"(registered window [30, 80])")
print(f"  rho at 2^129 = {rows[0][4]:.2f} (registered 64 +/- 6);  "
      f"rho at 2^166 = {[r for r in rows if r[0]==166.0][0][4]:.2f} "
      f"(registered 62 +/- 6)")
print(f"  min rho = {min(rhos):.2f}  -> the random-word FM model UNDERSHOOTS the")
print(f"  PROVED worst-word crossing by at least {min(rhos):.1f}x at EVERY determined row.")

print("\n=== D2.B  what FM claims safe that is PROVED unsafe (one row) ===")
L = 166.0
B = 1 << 38
a_rh = n - B + 1
s_fm = t_star(L)
print(f"  row: n=2^41, k=2^40, log2 q = 166, B* = 2^38 = {B:,}")
print(f"  FM says SAFE from agreement a = k + t*   = {k + s_fm:,}")
print(f"  PROVED unsafe at agreement a_RH - 1 = n-B = {a_rh - 1:,}  "
      f"(B_mca >= B*+1, (RQ1))")
print(f"  interval FM calls safe but is PROVED unsafe: "
      f"[{k + s_fm:,}, {a_rh - 1:,}]  width {a_rh - 1 - (k + s_fm):,} agreements")
print(f"  = {100.0 * (a_rh - 1 - (k + s_fm)) / (n - k):.2f}% of the whole excess range")

print("\n=== D2.C  FM prediction at the PROVED crossing (order-of-magnitude) ===")
for L, Bexp in ((166.0, 38), (129.0, 1)):
    B = 1 << Bexp
    a_rh = n - B + 1
    j = n - a_rh
    t = a_rh - k
    fm_log2 = log2C(n, j) + (1.0 - t) * L
    print(f"  log2 q={L:.0f}: at a_RH={a_rh:,}  log2 FM = {fm_log2:,.1f} ; "
          f"PROVED B_mca(a_RH) = B* = {B:,} (log2 = {Bexp})")
    print(f"     -> FM understates the truth by {Bexp - fm_log2:,.1f} bits")
