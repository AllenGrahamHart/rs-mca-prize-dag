"""D4: the margin ladder at the razor row.

The unsafe side of (RH-ADJ) is driven by the LIST profile
   Lmax(a) = max_U #{c in C : agreement(U,c) >= a},
converted to MCA-bad slopes by the PROVED simple-pole conversion
   M >= L(q-n)/(q-n+kL)  >  B* = floor(q/2^128)   <=>   roughly L > 2^128.

Facts (all exact, from d1_rungs.py):
  * the PROVED family supplies L = 2^242.6503 at sigma = 2^34-1
    (114.6503 bits of slack over the 2^128 the conversion needs);
  * its own next reach supplies only 2^116.13 (11.87 bits short);
    so the FAMILY's profile has a 126.5-bit CLIFF at sigma = 2^34,
    with the budget 2^128 strictly inside the cliff.

So the endpoint question is exactly: how many units of sigma does
114.65 bits of slack buy in the TRUE profile?  That is the decay rate
F_DECAY = log2 Lmax(a) - log2 Lmax(a+1).
"""
import math

n, k = 1 << 41, 1 << 40
LOGQ = 256.0
BUDGET_BITS = 128.0
SLACK = 114.6503                    # measured exactly in d1_rungs.py
SIG_LO = (1 << 34)                  # (RH-AC-lo): a_RH = k + 2^34
SIG_HI = (1 << 39)                  # (RH-AC-hi): a_RH = 3n/4 = k + 2^39

# measured F_DECAY / log2 q at the scaled cells.
# 0.6865 = EXACT at (n_s,q,a)=(8,17,5): F_LMAX(5)=7, F_LMAX(6)=1, both
#          brute-force verified (d3_lmax.py validation block).
# 0.1451 = LOWER BOUND at (8,65537,5) from the normal-triple candidate family,
#          whose anchor FAILED (it returns 5 where the exact value is 7), so it
#          under-counts F_LMAX(5) and therefore UNDER-states F_DECAY.
#          It also carries a known downward bias: at fixed small n_s, F_LMAX is
#          capped by a q-INDEPENDENT combinatorial constant while log2 q grows,
#          so the ratio decays with q for a reason that does NOT transport to
#          the razor row (where F_LMAX = 2^242.65 at sigma = 2^34-1).
DECAY_RATIOS = [0.6865, 0.1451]

print("=== mean-model decay rate at the razor row (exact) ===")
for sig in (1 << 33, 1 << 34, 1 << 36, 1 << 39):
    a = k + sig
    # lambda_FM(a) = C(n,a) q^(k-a);  ratio lambda(a)/lambda(a+1) = q(a+1)/(n-a)
    d = LOGQ + math.log2((a + 1) / (n - a))
    print(f"  sigma=2^{math.log2(sig):.0f}: mean-model decay = {d:.4f} bits per unit of a "
          f"(log2 q = {LOGQ})")

print()
print("=== how far 114.65 bits of slack reaches, as a function of the decay rate ===")
print(f"{'decay (bits/unit)':>20} {'units bought':>14} {'a_RH - (k+2^34-1)':>20} {'endpoint':>12}")
for dec in (LOGQ * 4, LOGQ, LOGQ / 4, LOGQ / 100, LOGQ / 1e6, LOGQ / 1.2e12):
    units = SLACK / dec
    ep = "-lo" if units < 2 else ("intermediate" if units < SIG_HI - SIG_LO else "-hi")
    print(f"{dec:>20.6g} {units:>14.6g} {units:>20.6g} {ep:>12}")

print()
print("=== what (RH-AC-hi) requires of the true max list profile ===")
steps = SIG_HI - SIG_LO + 1
print(f"  steps from sigma=2^34 to sigma=2^39: {steps:,} = 2^{math.log2(steps):.4f}")
print(f"  total decay budget available: {SLACK:.4f} bits (slack over the 2^128 need)")
print(f"  => required average decay <= {SLACK/steps:.6e} bits per unit of agreement")
print(f"  => a factor {LOGQ/(SLACK/steps):.6e} = 2^{math.log2(LOGQ/(SLACK/steps)):.2f} "
      f"BELOW the mean-model decay of {LOGQ} bits/unit")

print()
print("=== what (RH-AC-lo) requires ===")
print(f"  the profile must fall from >2^{BUDGET_BITS+SLACK:.2f} to <=2^{BUDGET_BITS:.0f} "
      f"within 1 unit of a")
print(f"  => required decay >= {SLACK:.4f} bits per unit, i.e. >= log2 q / "
      f"{LOGQ/SLACK:.4f} = log2 q * {SLACK/LOGQ:.4f}")
print(f"  the mean-model decay is log2 q = {LOGQ}, which is {LOGQ/SLACK:.4f}x MORE "
      f"than needed -> -lo is satisfied with room to spare under the mean law")

print()
print("=== the family's own cliff (exact) ===")
print(f"  L(sigma <= 2^34-1) = 2^242.6503  (rotated N=256,d=1; s-independent, so the")
print(f"      whole interval sigma in [2^33+1, 2^34-1] carries the SAME count)")
print(f"  L(sigma in [2^34+1, 2^35-1]) = 2^116.1263  (rotated N=128,d=1)")
print(f"  cliff = {242.6503-116.1263:.4f} bits in one step of the RUNG (not of a)")
print(f"  budget 2^128 lies strictly inside the cliff: "
      f"{116.1263 < BUDGET_BITS < 242.6503}")

if DECAY_RATIOS:
    print()
    print("=== transported bound from the MEASURED scaled decay ===")
    mn, mx = min(DECAY_RATIOS), max(DECAY_RATIOS)
    print(f"  measured F_DECAY/log2 q in [{mn:.4f}, {mx:.4f}] over the scaled cells")
    for tag, ratio in (("slowest measured", mn), ("fastest measured", mx)):
        dec = ratio * LOGQ
        units = SLACK / dec
        print(f"  {tag}: decay {dec:.4f} bits/unit -> slack buys {units:.4f} units "
              f"-> a_RH <= k + 2^34 - 1 + {math.ceil(units)}")
