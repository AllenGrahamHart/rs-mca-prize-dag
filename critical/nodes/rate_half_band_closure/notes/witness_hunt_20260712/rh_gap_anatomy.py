#!/usr/bin/env python3
"""rh_gap_anatomy: TASK 1 — exact gap anatomy at the rate-1/2 razor rows.

Row: n = 2^41, k = 2^40 (rate 1/2, the banked cap row), q prime = 1 mod n,
log2 q in (255.900, 256) — the razor slice. Band slack cells:
t in [2^33 + 1, sigma*], sigma* = 8,592,912,738 (banked radius 2,978,147
= off-by-one endpoint convention vs sigma* - 2^33 = 2,978,146).

Need per cell (list-side / eps* = 2^-128 convention, w2_spend_map + W2):
    T + 1 = floor(q / 2^128) + 1.
Supply columns at slack cell t (agreement A = k + t):
    qcore/staircase: Q_M = C(n/M - 1, k/M) at dyadic M | k with M > t
    planted:         floor((n-k+1)/(t+1))     [e22_reconstruction sec 2]
    tangent:         n - A + 1 = n - k - t + 1 [B_tan pin, dyadic_profile]
All exact integers; log2 via bit-shift trick (no float overflow).
"""
from math import comb, log2
from fractions import Fraction

def lg(x):
    if x <= 0: return float("-inf")
    b = x.bit_length()
    return b - 53 + log2(x >> (b - 53)) if b > 53 else log2(x)

n, k = 2**41, 2**40
sigma_star = 8_592_912_738
band_lo, band_hi = 2**33 + 1, sigma_star
TWO128 = 1 << 128

print("=" * 88)
print("A. THE SCALE LADDER at rate 1/2 (n = 2^41, k = 2^40): qcore reach vs count")
print("=" * 88)
print(f"{'M':>6} {'N=n/M':>7} {'h=k/M':>6} {'reach t<=M-1':>16} {'count C(N-1,h)':>20} {'log2':>9}  band-admissible?")
for e in range(30, 41):
    M = 2**e
    N = n // M
    h = k // M
    c = comb(N - 1, h)
    adm = "YES (t<M for all band t)" if M - 1 >= band_hi else (
          "boundary" if M - 1 >= band_lo else "no (reach below band)")
    print(f"2^{e:<4} {N:>7} {h:>6} {M-1:>16,} {('2^%.4f' % lg(c)):>20} {lg(c):>9.3f}  {adm}")

C_plateau = comb(255, 128)   # covers t <= 2^33 - 1 only
C_band = comb(127, 64)       # the best band-admissible scale M = 2^34
print(f"\n  plateau (M=2^33, covers t <= 2^33-1): C(255,128) = 2^{lg(C_plateau):.4f}")
print(f"  band-admissible max (M=2^34):         C(127,64)  = {C_band}")
print(f"                                                   = 2^{lg(C_band):.6f}")

print()
print("=" * 88)
print("B. NEED vs SUPPLY per razor q (list-side need T+1 = floor(q/2^128)+1)")
print("=" * 88)
# razor edges: log2 q = 255.900 (bottom, open) and log2 q -> 256 (top edge conv.)
# T+1 at the conservative edge convention (log2 q = 256): T = 2^128
edges = [("razor bottom log2 q = 255.900", 2**1279 * 10**0, None),]
# exact bottom: q = 2^255.9 -> T = floor(2^127.9). compute 2^0.9 via Fraction pow? use float-safe:
import decimal
decimal.getcontext().prec = 60
T_bot = int(decimal.Decimal(2) ** decimal.Decimal("127.9"))
T_top = TWO128  # conservative edge (spend-map convention log2 q = 256)

for label, T in [("bottom of razor (log2 q = 255.900+)", T_bot),
                 ("top edge convention (log2 q = 256)", T_top)]:
    need = T + 1
    for t in (band_lo, band_hi):
        planted = (n - k + 1) // (t + 1)
        tangent = n - k - t + 1
        supply = C_band + planted + tangent
        deficit = need - supply
        print(f"[{label}]  t = {t:,}")
        print(f"   need T+1              = {need}  = 2^{lg(need):.4f}")
        print(f"   qcore (M=2^34)        = {C_band}  = 2^{lg(C_band):.4f}  ({100*C_band/need:.3f}% of need)")
        print(f"   tangent n-k-t+1       = {tangent:,}  = 2^{lg(tangent):.4f}  ({100*tangent/need:.1e}% of need)")
        print(f"   planted               = {planted}")
        print(f"   TOTAL proved supply   = 2^{lg(supply):.6f}")
        print(f"   DEFICIT (need-supply) = {deficit}  = 2^{lg(deficit):.4f}")
        print(f"   bit-gap  log2(need/supply) = {lg(need)-lg(supply):.4f} bits;  multiplicative x{Fraction(need, supply).__float__():.2f}")
        print()

print("=" * 88)
print("C. CLEAN-RATE ANALOGUE CHECK (the '192-480' other-column numbers) ")
print("=" * 88)
for label, nn, kk, Nstar in [("prize 1/4 ", 2**41, 2**39, 256),
                             ("prize 1/8 ", 2**41, 2**38, 256),
                             ("prize 1/16", 2**41, 2**37, 512)]:
    Mstar = nn // Nstar
    t_u = Mstar - 1
    planted = (nn - kk + 1) // (t_u + 1)
    tangent = nn - kk - t_u + 1
    qc = comb(Nstar - 1, kk // Mstar)
    print(f"  {label}: t_u = M*-1 = {t_u:,}; planted = {planted}; tangent = {tangent:,} = 2^{lg(tangent):.2f}; "
          f"qcore = 2^{lg(qc):.2f} (margin {lg(qc)-128:+.2f} bits)")
print("  -> rate-1/2 band analogues: planted = 127 (vs 192/224/480), tangent ~ 2^39.99 (vs 2^40.6),")
print("     qcore = 2^123.17 vs needed 2^127.9..128 — the ONLY column that changes materially.")

print()
print("=" * 88)
print("D. WHERE THE GAP LIVES + WHAT WOULD CLOSE IT")
print("=" * 88)
w = band_hi - band_lo + 1
print(f"  band cells: t = {band_lo:,} .. {band_hi:,}  ({w:,} cells; banked radius 2,978,147 endpoint conv.)")
# deficit flat across band: supply varies only via tangent+planted
s_lo = C_band + (n - k + 1)//(band_lo + 1) + (n - k - band_lo + 1)
s_hi = C_band + (n - k + 1)//(band_hi + 1) + (n - k - band_hi + 1)
print(f"  supply at t=band_lo:  2^{lg(s_lo):.9f}")
print(f"  supply at t=band_hi:  2^{lg(s_hi):.9f}   (delta = {s_lo - s_hi:,} = 2^{lg(s_lo-s_hi):.2f} — < 2^-83 relative)")
print(f"  -> the gap is FLAT: every one of the {w:,} cells needs the same ~2^127.63 new members;")
print("     no easier sub-cell exists inside the band.")
# effective quotient points needed
for x in range(1, 16):
    if comb(127 + 2*x, 64 + x) > T_top:
        print(f"  effective-scale framing: C(127+{2*x},64+{x}) = 2^{lg(comb(127+2*x,64+x)):.3f} > 2^128"
              f" — a new family must simulate >= {2*x} extra effective quotient points (N: 128 -> {128+2*x});")
        print(f"     the next admissible dyadic scale N = 256 (needs t < 2^33) overshoots to 2^{lg(C_plateau):.1f}.")
        break
# what fraction of the requirement is missing
miss = (T_top + 1) - s_lo
print(f"  missing count at edge: {miss}  = 2^{lg(miss):.4f}  ({100*miss/(T_top+1):.3f}% of the need)")
print(f"  i.e. the hunt is NOT for a 'top-up' family: the new family must carry ~96.5% of the load alone.")

print()
print("=" * 88)
print("E. MCA-side secondary framing (pro brief trigger (q-n)/k ~ 2^216, for the record)")
print("=" * 88)
trig = (2**256 - n) // k
print(f"  (q-n)/k at edge = 2^{lg(trig):.3f}; qcore band supply 2^{lg(C_band):.3f} -> deficit {lg(trig)-lg(C_band):.1f} bits")
print("  (the list-side eps* = 2^-128 need above is the witness lane's binding target; the")
print("   MCA-side list-size trigger is ~92.8 bits away and is NOT the lane's near miss.)")
