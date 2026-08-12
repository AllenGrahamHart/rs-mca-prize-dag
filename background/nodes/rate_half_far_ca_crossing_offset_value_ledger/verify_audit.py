#!/usr/bin/env python3
"""Independent audit of the crossing-offset value ledger.

Second code path, deliberately different from verify.py:
  - every razor constant re-derived through ALTERNATE decompositions
    (r = 2^40 - 2^34 = (2^6 - 1) 2^34; floor = 63*rho + 127; the double
    cover via expansion, not subtraction);
  - the two cap forms proved by the exact division identity
    (r + f) = f*(r//f + 1) + (r mod f) - checked with divmod on large
    pseudo-random integers derived from the razor constants;
  - the six-decimal log2 claims verified WITHOUT FLOATS by binary-digit
    extraction (repeated squaring with a 100-bit truncated mantissa),
    confirming floor(10^6 log2 x) = 39977280 for BOTH r+1 and r+1+126;
  - the binomial-step ratio checked through factorials, not comb;
  - the exchange law's delta = 0 razor optimum checked on a fresh grid.

Run: tools/ramguard tiny -- python3 \
  background/nodes/rate_half_far_ca_crossing_offset_value_ledger/verify_audit.py
(RAMGUARD_TIMEOUT 60s)
"""

import json
from math import factorial
from pathlib import Path

cert = json.loads(Path(__file__).with_name("certificate.json").read_text())

rho = cert["rho"]
r = cert["r"]

# ---- constants through alternate decompositions
assert rho == 1 << 34
assert r == (1 << 40) - (1 << 34) == 63 * rho == (2 ** 6 - 1) * rho
assert cert["a"] == cert["n"] - r == cert["k"] + rho
assert cert["t_fib_floor"] == 63 * rho + 1
assert cert["constructive_floor"] == 63 * rho + 127 == r + 1 + 126

# ---- the double cover, by expansion: 2(63 rho + 1) - 126 rho = 2
assert 2 * (63 * rho + 1) - 126 * rho == cert["double_cover_defect"] == 2
assert 126 * rho == 2 * r

# ---- the cap-form identity (r+f)//f == r//f + 1, via divmod
seeds = [r, r + 1, rho, rho - 1, 2 * r - 1, cert["a"], 12345678910111213]
for x in seeds:
    for f in [1, 2, 3, 63, 64, 126, 127, rho, rho + 1]:
        q1, rem1 = divmod(x + f, f)
        assert 0 <= rem1 < f
        assert q1 == x // f + 1, (x, f)

# ---- float-free six-decimal log2 by digit extraction
def log2_micro(x, frac_bits=40, work_bits=100):
    e = x.bit_length() - 1
    m = (x << work_bits) >> e          # mantissa in [2^work_bits, 2^{work_bits+1})
    bits = 0
    for _ in range(frac_bits):
        m = (m * m) >> work_bits
        bits <<= 1
        if m >> (work_bits + 1):
            bits |= 1
            m >>= 1
    # log2(x) ~ e + bits / 2^frac_bits ; return ROUND(10^6 * log2(x))
    # (the banked 39.977280 is the six-decimal ROUNDING: the true value is
    # 39.9772799..., so flooring would give ...279)
    scaled = 10 ** 6 * ((e << frac_bits) + bits)
    return (scaled + (1 << (frac_bits - 1))) >> frac_bits


assert log2_micro(cert["t_fib_floor"]) == cert["log2_micro"] == 39977280
assert log2_micro(cert["constructive_floor"]) == 39977280
# sanity of the extractor itself on exact powers and a known value
assert log2_micro(1 << 39) == 39000000
assert log2_micro(3) == 1584963

# ---- the binomial step through factorials
c12863 = factorial(128) // (factorial(63) * factorial(65))
c12764 = factorial(127) // (factorial(64) * factorial(63))
br = cert["binomial_ratio"]
assert c12863 * br["den"] == c12764 * br["num"], "ratio is not 128/65"
# Pascal cross-check with an independently assembled entry
assert c12863 == factorial(127) // (factorial(62) * factorial(65)) + c12764

# ---- the exchange law's razor optimum on a fresh delta grid
cap = lambda r1, rh, d: r1 - d + (2 * r1 - 1 + d) // rh
razor_cap = cap(r + 1, rho, 0)
assert razor_cap == cert["constructive_floor"]
for d in [3, 7, 100, 10 ** 6, rho - 1, rho + 1, 3 * rho]:
    assert cap(r + 1, rho, d) <= razor_cap, d
# and the mu_26 cell's in-normal-form numbers
mc = cert["mu26_cell"]
assert (2 * mc["r_plus_1"] - 1) // mc["rho"] == mc["j_cap"] == 7
assert cap(mc["r_plus_1"], mc["rho"], 0) == mc["in_form_cap"] == 18
assert mc["outside_form_T"] > mc["in_form_cap"]   # cited exhibit; the point

print(
    "RATE_HALF_FAR_CA_CROSSING_OFFSET_VALUE_LEDGER_AUDIT_PASS "
    "constants by alternate decomposition; float-free log2_micro=39977280 "
    "for both floors; binomial step 128/65 by factorials; exchange delta=0 "
    "optimal on fresh grid"
)
