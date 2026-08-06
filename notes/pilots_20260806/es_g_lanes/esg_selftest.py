"""ES-G-LANES selftest -- FAIL-CLOSED.  Exits nonzero on any failure.

Validates, before any pilot number is believed:
  (A) closure_size_fast == closure_size_brute over all p of order 1,2,4
      at n = 2^m, m = 5..16, and many W < 2^(m-2).
  (B) the balance comparator on hand-checkable cases.
  (C) reproduction of three BANKED constants from other pilots:
      - mun REPORT.md:59  Lambda(2^34) = -2.20e12 at log2 q_char = 256
      - mun REPORT.md:59  Lambda(2^34) = +1.4943e12 at q_char = 2^41
      - mun REPORT.md:59  crossing crossover at log2 q_char = 127.977
      - sl2_unstructured descent.json  log2_q_critical = 208.47593052630532
  (D) the round-16 witness table's own |Z_w| values (es REPORT.md:29-33).
"""
import sys
import math
from esg_lib import (closure_size_brute, closure_size_fast, mult_order,
                     p_classes, balance, log2_binom, log2_bracket,
                     BAND_ROWS, N)

FAILS = []
CHECKS = 0


def check(name, cond, detail=""):
    global CHECKS
    CHECKS += 1
    if not cond:
        FAILS.append(f"{name}: {detail}")
        print(f"  FAIL  {name}  {detail}")
    return cond


# ---------------------------------------------------------------- (A)
print("(A) closure_size_fast vs brute force")
for m in range(5, 17):
    n = 1 << m
    half = 1 << (m - 2)
    classes = p_classes(m)
    # a spread of W values, always < 2^(m-2), including the extremes
    Ws = sorted({1, 2, 3, 4, 5, half - 1, half - 2, half // 2,
                 half // 2 - 1, half // 2 + 1, half // 4, max(1, half // 8),
                 max(1, half - half // 3)})
    for p, order in classes.items():
        for W in Ws:
            if not (1 <= W < half):
                continue
            a = closure_size_fast(m, W, p)
            b = closure_size_brute(n, W, p)
            check(f"closure m={m} p={p} W={W}", a == b, f"fast={a} brute={b}")
        check(f"order m={m} p={p}", mult_order(p, n) in (1, 2, 4), f"ord={order}")

# also: closure must lie inside the round-15 bracket [W, delta*W]
print("(A2) round-15 bracket [w-1, delta(w-1)] containment")
for m in (12, 16, 41):
    half = 1 << (m - 2)
    for p, order in p_classes(m).items():
        for W in (1, 3, 17, half // 2, half - 1):
            if not (1 <= W < half):
                continue
            z = closure_size_fast(m, W, p)
            check(f"bracket m={m} p={p} W={W}", W <= z <= order * W,
                  f"z={z} not in [{W},{order*W}]")

# ---------------------------------------------------------------- (B)
print("(B) balance comparator")
v, mlo, mhi = balance(1, 1 << 200, 1 << 200, 200)
check("balance exact 2^200", v == "ALWAYS", v)
v, _, _ = balance(1, (1 << 200) - 1, (1 << 200) - 1, 200)
check("balance just below", v == "NEVER", v)
v, _, _ = balance(10, 1 << 20, 1 << 21, 205)
check("balance flips", v == "FLIPS", v)
v, _, _ = balance((1 << 34) - 1, 1 << 128, 1 << 128, 1 << 41)
check("crossing w=2^34 at p=2^128 fails", v == "NEVER", v)

# ---------------------------------------------------------------- (C)
print("(C) reproduction of banked constants")
w = 1 << 34
rprime = (1 << 40) - w
lcb = log2_binom(N, rprime)
lam_256 = lcb - (w - 1) * 256.0
lam_41 = lcb - (w - 1) * 41.0
check("mun Lambda(2^34)@256bit = -2.20e12", abs(lam_256 - (-2.20e12)) < 5e9,
      f"{lam_256:.5e}")
check("mun Lambda(2^34)@2^41 = +1.4943e12", abs(lam_41 - 1.4943e12) < 1e9,
      f"{lam_41:.5e}")
crossover = lcb / (w - 1)
check("mun crossover log2 q_char = 127.977", abs(crossover - 127.977) < 5e-3,
      f"{crossover:.6f}")

k, h, dlo, dhi = BAND_ROWS["1/4"]
rb = N - k - dlo
budget = math.log2(0.68) + 2 * 41
crit = (log2_binom(N, rb) - budget) / (2.0 * dlo)
check("descent log2_q_critical(1/4) = 208.47593052630532",
      abs(crit - 208.47593052630532) < 1e-6, f"{crit:.11f}")
# the mun reading (no budget subtracted) must differ by exactly budget/(2d)
crit_nb = log2_binom(N, rb) / (2.0 * dlo)
check("mun/descent gap = budget/(2d) ~ 9.5e-9",
      abs((crit_nb - crit) - budget / (2.0 * dlo)) < 1e-12
      and abs(crit_nb - crit - 9.48e-9) < 1e-10, f"{crit_nb-crit:.4e}")
for rate, want in (("1/8", 140.550), ("1/16", 174.640)):
    k, h, dlo, dhi = BAND_ROWS[rate]
    c = (log2_binom(N, N - k - dlo) - budget) / (2.0 * dlo)
    check(f"mun band critical field {rate} ~ {want}", abs(c - want) < 0.5,
          f"{c:.3f}")

# ---------------------------------------------------------------- (D)
print("(D) round-16 witness table |Z_w| (n=32) recomputed")
# es_boundary_adversary/REPORT.md:29-33 -- (r', w, p, delta, |Z_w|)
WITNESSES = [(6, 4, 7, 4, 10), (6, 3, 47, 2, 4), (6, 4, 17, 2, 5),
             (5, 2, 23, 4, 4), (5, 2, 463, 2, 2)]
for (rp, wv, p, delta, zw) in WITNESSES:
    n32 = 32
    check(f"witness ord({p} mod 32) = {delta}", mult_order(p, n32) == delta,
          f"{mult_order(p, n32)}")
    z = closure_size_brute(n32, wv - 1, p)
    check(f"witness |Z_{wv}| p={p} = {zw}", z == zw, f"got {z}")

print()
print(f"{CHECKS} checks, {len(FAILS)} failures")
if FAILS:
    for f in FAILS:
        print("  " + f)
    sys.exit(1)
print("SELFTEST PASS")
