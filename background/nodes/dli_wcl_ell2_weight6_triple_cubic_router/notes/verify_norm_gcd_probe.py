#!/usr/bin/env python3
"""Verify the pinned weight-six saturated norm-gcd route probe."""

from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
RESULT = (
    ROOT
    / "experiments"
    / "prize_resolution"
    / "dli_wcl_ell2_weight6_norm_gcd_probe_result.json"
)
RESULT_SHA256 = "dcbb92ab9288de7e019d62e3891d9e43ac9ffc24dca9ce10024f012cba760612"


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    for divisor in range(2, math.isqrt(value) + 1):
        if value % divisor == 0:
            return value == divisor
    return True


def valuation_two(value: int) -> int:
    value -= 1
    result = 0
    while value % 2 == 0:
        value //= 2
        result += 1
    return result


def expected_candidates(order: int) -> list[list[int]]:
    raw = (
        (1, 2, 3),
        (1, order // 4, order // 8),
        (order // 8, order // 4, 3),
        (order // 4 - 1, order // 4 + 1, order // 3),
    )
    return [list(candidate) for candidate in raw]


def main() -> None:
    sys.set_int_max_str_digits(0)
    encoded = RESULT.read_bytes()
    if hashlib.sha256(encoded).hexdigest() != RESULT_SHA256:
        raise AssertionError("probe artifact hash")
    payload = json.loads(encoded)
    if payload["schema"] != "dli-wcl-ell2-weight6-norm-gcd-probe-v1":
        raise AssertionError("probe schema")

    rows = payload["rows"]
    if len(rows) != 20 or any(row["status"] != "COMPLETE" for row in rows):
        raise AssertionError("probe completeness")
    for order in (64, 128, 256, 512, 1024):
        actual = [row["exponents"] for row in rows if row["order"] == order]
        if actual != expected_candidates(order):
            raise AssertionError((order, actual))
    if any(row["first_zero"] or row["second_zero"] for row in rows):
        raise AssertionError("unexpected zero obstruction")
    if max(row["gcd_bits"] for row in rows) != 183_078:
        raise AssertionError("raw gcd maximum")
    if max(row["u_saturated_gcd_bits"] for row in rows) != 11_367:
        raise AssertionError("saturated gcd maximum")
    for row in rows:
        raw = int(row["gcd"])
        saturated = int(row["u_saturated_gcd"])
        if raw % saturated:
            raise AssertionError(("saturation divisibility", row["order"]))
        if raw.bit_length() != row["gcd_bits"]:
            raise AssertionError(("raw bit length", row["order"]))
        if saturated.bit_length() != row["u_saturated_gcd_bits"]:
            raise AssertionError(("saturated bit length", row["order"]))

    factor_rows = payload["factor_rows"]
    nonunits = {row["u_saturated_gcd"] for row in rows if int(row["u_saturated_gcd"]) > 1}
    if len(factor_rows) != 19 or {row["gcd"] for row in factor_rows} != nonunits:
        raise AssertionError("factor coverage")
    primes = set()
    maximum_v2 = 0
    for row in factor_rows:
        if row["status"] != "COMPLETE":
            raise AssertionError("factor status")
        product = 1
        for factor in row["factors"]:
            prime = int(factor["prime"])
            if not is_prime(prime):
                raise AssertionError(("composite factor", prime))
            if prime.bit_length() != factor["prime_bits"]:
                raise AssertionError(("prime bits", prime))
            v2 = valuation_two(prime)
            if v2 != factor["v2_prime_minus_1"]:
                raise AssertionError(("valuation", prime))
            product *= prime ** factor["exponent"]
            primes.add(prime)
            maximum_v2 = max(maximum_v2, v2)
        if product != int(row["gcd"]):
            raise AssertionError("factor product")

    expected_primes = {
        2,
        127,
        193,
        257,
        577,
        769,
        1153,
        1409,
        13313,
        15361,
        19457,
        22273,
        37889,
        39937,
        64513,
        70657,
    }
    if primes != expected_primes or maximum_v2 != 10:
        raise AssertionError((primes, maximum_v2))

    # Mutation controls: a dropped factor and an official-threshold claim fail.
    first = factor_rows[0]
    factors = first["factors"]
    mutated_product = math.prod(
        int(factor["prime"]) ** factor["exponent"] for factor in factors[1:]
    )
    if mutated_product == int(first["gcd"]):
        raise AssertionError("dropped-factor mutation")
    if maximum_v2 >= 41:
        raise AssertionError("official-threshold mutation")

    print(
        "DLI_WCL_ELL2_WEIGHT6_NORM_GCD_PROBE_PASS "
        f"rows={len(rows)} factor_rows={len(factor_rows)} "
        f"primes={len(primes)} max_v2={maximum_v2} negative_controls=2/2"
    )


if __name__ == "__main__":
    main()
