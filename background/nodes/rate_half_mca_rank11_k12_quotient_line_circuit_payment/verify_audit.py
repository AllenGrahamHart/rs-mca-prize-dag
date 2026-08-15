#!/usr/bin/env python3
"""Independent arithmetic and circuit-shadow audit of the K'=12 payment."""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "8189f852eb61e3df83bec0d7158a71a8d0b5f6bbe8d38b2b60521ae875956d3c"


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length))


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    p = json.loads(CONTRACT.read_text())["parameters"]
    assert p["K_prime"] == 12
    n, m = p["n_prime"], p["m_prime"]

    # Reconstruct the d=1 canonical-basis record cap independently.
    corank = 1
    evaluation_rank = 10 - corank
    shortened_k = 12 - evaluation_rank
    endpoint_zero = Fraction(
        falling(1048576 + shortened_k, corank + 1),
        (67472 + shortened_k) * rising(67473, corank - 1),
    )
    endpoint_max = Fraction(
        falling(1048576 + corank, corank + 1),
        rising(67473, corank),
    )
    record_cap = max(endpoint_zero, endpoint_max)
    record_cap = record_cap.numerator // record_cap.denominator
    assert record_cap == 16295594
    kernel = comb(n, 9) * record_cap
    assert kernel == p["kernel_incidence_cap"]

    shadow_checks = 0
    for support in range(1, 12):
        rank8 = rank9 = 0
        for omitted in itertools.combinations(range(11), 2):
            if set(omitted).isdisjoint(range(support)):
                rank8 += 1
            else:
                rank9 += 1
        assert rank8 == comb(11 - support, 2)
        assert rank9 == 55 - rank8
        shadow_checks += 55
    assert min(55 - comb(11 - support, 2) for support in range(6, 12)) == 45

    records = p["residual_record_floor"]
    high = comb(n, 9) * max(p["rank9_core_caps"]) // 45
    low = records * p["low_circuit_per_record_cap"]
    total = kernel + high + low
    required = Fraction(990810934 * records * comb(m, 11), 10**9)
    demand = (required.numerator + required.denominator - 1) // required.denominator
    coefficient = Fraction(990810934 * comb(m, 11), 10**9) - p["low_circuit_per_record_cap"]
    assert coefficient > 0
    assert total == p["total_capacity_at_record_floor"]
    assert demand == p["required_incidence_at_record_floor"]
    assert demand - total == p["demand_capacity_gap"] > 0

    print(
        "PASS K12 quotient-line circuit payment audit: "
        f"record cap {record_cap}, {shadow_checks} shadow omissions, "
        f"gap {demand-total}"
    )


if __name__ == "__main__":
    main()
