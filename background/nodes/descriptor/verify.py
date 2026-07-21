#!/usr/bin/env python3
"""Verify the exact descriptor contract and independent row regressions."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RATES = ("1/2", "1/4", "1/8", "1/16")
PINNED_HASHES = {
    "tools/prize_row_descriptor.py": "ee125103c9d31fc4ceed7b16e129b025aef9facd9437b61fc614a716f7ce7ce9",
    "critical/nodes/wild_row_audit/wild_row_audit.json": "9b17c2adcf938310230b066a148f2674ba78b558c0bf7fbed03ec700bcde0aab",
}


def check_pins() -> None:
    for rel, expected in PINNED_HASHES.items():
        assert hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() == expected


check_pins()
sys.path.insert(0, str(ROOT / "tools"))

from prize_row_descriptor import INPUT_SCHEMA, describe_row  # noqa: E402


def row(p: int, extension_degree: int, n: int, rate: str) -> dict:
    if n <= 0 or n & (n - 1):
        raise AssertionError("regression order is not a power of two")
    return {
        "schema": INPUT_SCHEMA,
        "p": str(p),
        "extension_degree": extension_degree,
        "subgroup_log2": n.bit_length() - 1,
        "rate": rate,
    }


def rejected(source: dict, phrase: str) -> bool:
    try:
        describe_row(source)
    except ValueError as exc:
        return phrase in str(exc)
    return False


def main() -> None:
    check_pins()

    pinned = describe_row(row(17, 32, 512, "1/2"))
    assert pinned["field"]["order_decimal"] == str(17**32)
    assert pinned["evaluation_domain"]["order_decimal"] == "512"
    assert pinned["code"]["dimension_decimal"] == "256"
    assert pinned["target"]["B_star_decimal"] == "6"
    assert pinned["target"]["denominator_decimal"] == str(17**32)

    wild = json.loads(
        (ROOT / "critical" / "nodes" / "wild_row_audit" / "wild_row_audit.json").read_text()
    )["admissible_wild_rows"]
    regressions = 0
    for fixture in wild:
        p = fixture["mersenne_p"]
        extension_degree = fixture["extension_degree"]
        n = fixture["n"]
        for rate in RATES:
            descriptor = describe_row(row(p, extension_degree, n, rate))
            assert descriptor["field"]["order_decimal"] == fixture["q"]
            assert descriptor["evaluation_domain"]["order_decimal"] == str(n)
            assert int(descriptor["evaluation_domain"]["subgroup_cofactor_decimal"]) * n == int(fixture["q"]) - 1
            expected_k = n * int(rate.split("/")[0]) // int(rate.split("/")[1])
            assert descriptor["code"]["dimension_decimal"] == str(expected_k)
            regressions += 1

    mutations = [
        rejected(row(17, 32, 512, "1/3"), "rate must be one of"),
        rejected(row(2, 256, 2, "1/2"), "q < 2^256"),
        rejected(row(17, 1, 32, "1/2"), "must divide q-1"),
        rejected(row(3, 1, 1 << 42, "1/2"), "k <= 2^40"),
        rejected(
            {
                "schema": INPUT_SCHEMA,
                "p": "2",
                "extension_degree": 10**9,
                "subgroup_log2": 1,
                "rate": "1/2",
            },
            "q < 2^256",
        ),
        rejected(
            {
                "schema": INPUT_SCHEMA,
                "p": "17",
                "extension_degree": 1,
                "subgroup_log2": 10**9,
                "rate": "1/2",
            },
            "subgroup order must be below",
        ),
        rejected(
            {
                "schema": INPUT_SCHEMA,
                "p": True,
                "extension_degree": 1,
                "subgroup_log2": 1,
                "rate": "1/2",
            },
            "p must be an integer",
        ),
    ]
    assert all(mutations)
    print(
        "PRIZE_ROW_DESCRIPTOR_PASS "
        f"pinned=1 dependencies={len(PINNED_HASHES)} wild_regressions={regressions} "
        f"mutations={sum(mutations)}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
