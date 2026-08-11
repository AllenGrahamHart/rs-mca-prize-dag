#!/usr/bin/env python3
"""Independent audit of the (SAT3) realizability ledger record.

Second code path, deliberately different from verify.py:
  - the (L2)/(BIV-G)/DEF-ID rows proved as POLYNOMIAL IDENTITIES in m
    (coefficient tuples over Z), not as point evaluations;
  - the four banked binomials computed through factorials;
  - the D9-recovered gate formula EVALUATED at both m = 1 calibration
    points and matched to the banked +13.75 / -0.94 to two decimals --
    the check the draft verifier could not perform before the formula's
    recovery;
  - the 2^9.75 safe-direction overestimate and the stacking arithmetic.

Run: tools/ramguard tiny -- python3 \
  background/nodes/rate_half_sat3_realizability_ledger_record/verify_audit.py
(RAMGUARD_TIMEOUT 60s)
"""

import json
from math import factorial, log2
from pathlib import Path

cert = json.loads(Path(__file__).with_name("certificate.json").read_text())


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_sub(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
            for i in range(n)]


def poly_add(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
            for i in range(n)]


M = [0, 1]                                   # the polynomial m
# (m+2)(4m+1) - 16m = 4m^2 - 7m + 2, as a polynomial identity
lhs = poly_sub(poly_mul([2, 1], [1, 4]), [0, 16])
assert lhs == [2, -7, 4], lhs
# the reduced form m(4m+1) - (8m-2) is the same polynomial
assert poly_sub(poly_mul(M, [1, 4]), [-2, 8]) == [2, -7, 4]
# the (BIV-G) deficit (7m^2-9m+2) - (3m^2-2m) is the same polynomial
assert poly_sub([2, -9, 7], [0, -2, 3]) == [2, -7, 4]
# its values at m = 1..4
for i, m in enumerate((1, 2, 3, 4)):
    assert 4 * m * m - 7 * m + 2 == cert["l2_row"][i]
# DEF-ID: (m+2)(4m+1) + m(3m-2) = (m-1)(7m-2) + 16m = 7m^2 + 7m + 2
d1 = poly_add(poly_mul([2, 1], [1, 4]), poly_mul(M, [-2, 3]))
d2 = poly_add(poly_mul([-1, 1], [-2, 7]), [0, 16])
assert d1 == d2 == [2, 7, 7]

# the banked binomials, through factorials
C = lambda n, k: factorial(n) // (factorial(k) * factorial(n - k))
for key, want in cert["binomials"].items():
    n, k = map(int, key[2:-1].split(","))
    assert C(n, k) == want, key

# the recovered gate formula at both calibration points
def gate(m, q, T):
    rho = 4 * m - 1
    return ((m + 1) * (rho + 1) - 4) * log2(q) + log2(C(q + 1, T)) \
        + T * (log2(C(16 * m, 4 * m - 1)) - rho * log2(q))


for cal in cert["calibrations"]:
    got = gate(cal["m"], cal["q"], cal["T"])
    assert abs(got - cal["banked_log2E"]) < 0.01, (cal, got)

# 16 = 2^4 realized at q = 17: the overestimate is 13.75 - 4 = 9.75 bits,
# in the SAFE direction (gate > reality)
assert abs(cert["calibrations"][0]["banked_log2E"]
           - log2(cert["calibrations"][0]["realized"])
           - cert["overestimate_bits"]) < 0.01
assert cert["calibrations"][0]["banked_log2E"] > log2(16)

# stacking arithmetic: -1-O + 5 = +4-O; adding the independent +4..+6
# orbit-side correction gives +8..+10
st = cert["stacking"]
assert -1 + st["erc2_units"] == 4
assert [4 + a for a in st["aut_range"]] == st["stacked_range"]

print(
    "RATE_HALF_SAT3_REALIZABILITY_LEDGER_RECORD_AUDIT_PASS "
    "rows proved as polynomial identities; binomials by factorials; the "
    "D9-recovered gate reproduces both calibrations (+13.75@q17, "
    "-0.94@q97) to two decimals; overestimate 9.75 bits safe direction"
)
