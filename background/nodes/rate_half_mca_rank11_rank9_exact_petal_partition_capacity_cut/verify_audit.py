#!/usr/bin/env python3
"""Independent audit for the exact residual-petal capacity cut."""

from __future__ import annotations

import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "df54f15d0ba1f4e335eb606f8f47c496e240ac7e2fe3beb209e100a3a4a7dd39"


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def line(a: int) -> tuple[int, int]:
    d = 981105
    count, tail = 1 + d // a, d % a
    return (
        d + a,
        (d + a) * (67462 - a)
        + (count * a * (a - 1) + tail * (tail - 1)) // 2,
    )


def value(a: int, k: int) -> int:
    slope, intercept = line(a)
    return slope * k + intercept


def demand_fraction(k: int) -> tuple[int, int]:
    n, m = 1048576 + k, 67472 + k
    return (
        495405467 * 274980728111260126 * comb(m, 9) * comb(m - 9, 2),
        10**9 * comb(n, 9),
    )


def small_partition_oracle(total: int, ceiling: int, linear: int) -> int:
    charge = lambda size: size * linear + size * (size - 1) // 2
    best = [0] + [-1] * total
    for used in range(1, total + 1):
        best[used] = max(
            best[used - size] + charge(size)
            for size in range(1, min(ceiling, used) + 1)
        )
    return best[total]


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]

    kmax = 15634
    baseline = value(67472, kmax)
    checked_a = 0
    for a in range(67472, 67462 + kmax + 1):
        candidate = value(a, kmax)
        assert candidate <= baseline, (a, candidate, baseline)
        if a > 67472:
            assert candidate < baseline, (a, candidate, baseline)
        checked_a += 1

    transfer_checks = 0
    for a, x, y, linear in (
        (67472, 0, 1, 0),
        (67472, 101, 202, 7),
        (70079, 35000, 36000, 11),
        (81759, 50000, 50000, 0),
        (83096, 83094, 83095, 15625),
    ):
        q = lambda size: size * linear + size * (size - 1) // 2
        if x + y <= a:
            assert q(x + y) - q(x) - q(y) == x * y
        else:
            assert q(a) + q(x + y - a) - q(x) - q(y) == (a - x) * (a - y)
        transfer_checks += 1

    oracle_checks = 0
    for total in range(2, 35):
        for ceiling in range(1, total + 1):
            for linear in (0, 1, 7):
                full, tail = divmod(total, ceiling)
                charge = lambda size: size * linear + size * (size - 1) // 2
                packed = full * charge(ceiling) + charge(tail)
                assert small_partition_oracle(total, ceiling, linear) == packed
                oracle_checks += 1

    cap_slope, cap_intercept = line(67472)
    owner_cap = 981105
    row_checks = 0
    for k in range(10, 15635):
        numerator, denominator = demand_fraction(k)
        upper = owner_cap * (cap_slope * k + cap_intercept)
        raw = numerator - upper * denominator
        assert (raw > 0) == (k >= 15529), k
        assert ceil_div(numerator, denominator) > upper if k >= 15529 else ceil_div(numerator, denominator) <= upper
        row_checks += 1

    assert p["last_open_raw_cross"] < 0 < p["first_closed_raw_cross"]
    assert p["remaining_rank9_interval"] == [10, 15528]
    print(
        "PASS exact-petal audit: "
        f"{checked_a} ceilings, {row_checks} rows, "
        f"{oracle_checks} small partitions, {transfer_checks} transfers"
    )


if __name__ == "__main__":
    main()
