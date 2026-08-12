#!/usr/bin/env python3
"""Independent audit of the type-2 vacuity fence.

Second code path, deliberately different from verify.py:
  - pure integer arithmetic, no fractions module;
  - the razor floor derived through the rho-decomposition
    floor = 64*rho + 1 - 126*rho = 1 - 62*rho, not through (R+1) - w*;
  - the bracket handled by MONOTONICITY + one endpoint, not by sampling:
    floor(a) = R + 1 - 2(n-a) is strictly increasing in a, so
    floor(a_top - 1) = -1 < 0 covers the entire half-open bracket at once;
  - the equivalence chain checked as 4a >= 3n, cross-multiplied, never
    through rationals.
All target values come from certificate.json.

Run: tools/ramguard tiny -- python3 \
  background/nodes/rate_half_type2_ledger_vacuous_by_sign_fence/verify_audit.py
"""

import json
from pathlib import Path

cert = json.loads(Path(__file__).with_name("certificate.json").read_text())

n, k, R, rho = cert["n"], cert["k"], cert["R"], cert["rho"]
a, r = cert["a"], cert["r"]

# shape identities via powers of two only
assert n == 2 ** 41 and k == R == 2 ** 40 and rho == 2 ** 34
assert a == k + rho and r == n - a == 63 * rho

# the floor through the rho-decomposition (different route than verify.py)
floor = 1 - 62 * rho
assert floor == cert["floor_at_adversary"] == -1065151889407
assert R + 1 - cert["adversary_wstar"] == floor
assert cert["adversary_wstar"] == 2 * r

# threshold as 126*rho - 64*rho, ratio 62/63 by cross-multiplication
threshold = 126 * rho - 64 * rho
assert threshold == cert["overlap_threshold"] == 62 * rho
assert 63 * threshold == 62 * r
assert cert["threshold_numerator"] * r == cert["threshold_denominator"] * threshold
# 62/63 = 98.412698% to six decimal digits, in integers
assert (62 * 10 ** 8) // 63 == 98412698

# equivalence 2r <= R <=> 4a >= 3n, integers only, every even n <= 398
for n_ in range(8, 400, 2):
    R_ = n_ // 2
    for a_ in range(1, n_ + 1):
        assert (2 * (n_ - a_) <= R_) == (4 * a_ >= 3 * n_), (n_, a_)

# the bracket by monotonicity + endpoint
a_top = cert["flip_offset"]
assert 4 * a_top == 3 * n and a_top == k + 2 ** 39
flr = lambda a_: R + 1 - 2 * (n - a_)
assert flr(a_top) == cert["floor_at_flip"] == 1
assert flr(a_top - 1) == -1
assert flr(a) == floor
# strictly increasing in a (slope +2), so every offset in [a, a_top) is
# vacuous because the top-minus-one endpoint already is
assert flr(a + 1) - flr(a) == 2 > 0

# the small worked cell
sc = cert["small_cell"]
assert sc["r"] == sc["n"] - sc["a"] == sc["R"] - sc["rho"]
assert sc["R"] + 1 - 2 * sc["r"] == sc["floor"] == -6
assert 2 * sc["r"] - sc["R"] == sc["threshold"] == 7
assert 4 * sc["a"] < 3 * sc["n"]

print(
    "RATE_HALF_TYPE2_LEDGER_VACUOUS_BY_SIGN_FENCE_AUDIT_PASS "
    "floor=1-62*rho=%d threshold=62r/63 flip@3n/4=+1 bracket-by-monotonicity"
    % floor
)
