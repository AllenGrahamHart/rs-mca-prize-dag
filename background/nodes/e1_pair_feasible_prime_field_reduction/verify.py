#!/usr/bin/env python3
"""Verify the exact prime-field reduction on pair-feasible E1 anchors."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_pair_feasible_prime_field_reduction"
PARENT = "e1_pair_feasible_ambient_generation"
E1_TARGET = "e1_official_prime_exception_control"
UNIVERSAL_TARGET = "unsafe_crossing_family_instantiation"
PRIZE_BUDGET = 317494674775468773183020924238786383963

EXPECTED_PIN = {
    "allowance_file": "background/nodes/e1_clean_anchor_exact_collision_allowance/statement.md",
    "allowance_file_sha256": "1380aed931775cb434e67586f0346b470afca4d19b52985f037a64793a26068a",
    "ambient_generation_file": "background/nodes/e1_pair_feasible_ambient_generation/statement.md",
    "ambient_generation_file_sha256": "8853bf362f81ab9e44d9795ef3d0449eac300eafd999a4058c0a00530bb392c7",
}


def integer_root(n: int, exponent: int) -> int:
    low = 0
    high = 1 << ((n.bit_length() + exponent - 1) // exponent + 1)
    while low + 1 < high:
        middle = (low + high) // 2
        if middle**exponent <= n:
            low = middle
        else:
            high = middle
    return low


def multiplicative_order(value: int, modulus: int) -> int:
    assert math.gcd(value, modulus) == 1
    current = 1
    for order in range(1, modulus + 1):
        current = current * value % modulus
        if current == 1:
            return order
    raise AssertionError("order not found")


def root_interval(low: int, high: int, exponent: int) -> tuple[int, int]:
    return integer_root(low - 1, exponent) + 1, integer_root(high, exponent)


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for file_key, hash_key in (
        ("allowance_file", "allowance_file_sha256"),
        ("ambient_generation_file", "ambient_generation_file_sha256"),
    ):
        assert hashlib.sha256((ROOT / pin[file_key]).read_bytes()).hexdigest() == pin[hash_key]

    intervals = {
        "RowC": ((1 << 122) << 128, ((1 << 122) + 1) << 128),
        "prize": (PRIZE_BUDGET << 128, (PRIZE_BUDGET + 1) << 128),
    }
    # Store half-open intervals and convert to inclusive high endpoints below.
    expected = {
        "RowC": {
            2: (42535295865117307932921825928971026432,
                42535295865117307932921825928971026435),
            4: (6521908912666391107, 6521908912666391106),
            8: (2553802834, 2553802833),
            16: (50536, 50535),
            32: (225, 224),
            64: (15, 14),
            128: (4, 3),
        },
        "prize": {
            2: (328691100301468598864521198461975482798,
                328691100301468598864521198461975482797),
            4: (18129840051734284368, 18129840051734284367),
            8: (4257914989, 4257914988),
            16: (65253, 65252),
            32: (256, 255),
            64: (16, 15),
            128: (4, 3),
        },
    }

    interval_checks = 0
    for label, (low, high_exclusive) in intervals.items():
        for exponent in (2, 4, 8, 16, 32, 64, 128):
            got = root_interval(low, high_exclusive - 1, exponent)
            assert got == expected[label][exponent], (label, exponent, got)
            interval_checks += 1

    rowc_square_low, rowc_square_high = expected["RowC"][2]
    rowc_square_candidates = tuple(range(rowc_square_low, rowc_square_high + 1))
    assert rowc_square_candidates == tuple((1 << 125) + offset for offset in range(4))
    assert rowc_square_candidates[0] % 2 == 0
    assert multiplicative_order(rowc_square_candidates[1] % 256, 256) == 1
    assert rowc_square_candidates[2] % 2 == 0
    assert multiplicative_order(rowc_square_candidates[3] % 256, 256) == 64
    assert multiplicative_order(rowc_square_candidates[3] % 512, 512) == 128

    for label in expected:
        for exponent, (low_root, high_root) in expected[label].items():
            if label == "RowC" and exponent == 2:
                continue
            assert low_root > high_root

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    statements = {entry["id"]: entry.get("statement", "") for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[PARENT] == "PROVED"
    assert statuses[E1_TARGET] == "TARGET"
    assert statuses[UNIVERSAL_TARGET] == "TARGET"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, E1_TARGET, "ev") in edges
    assert (NODE, UNIVERSAL_TARGET, "ev") in edges
    assert "q=p" in statements[NODE]
    assert "p=1 mod N" in statements[NODE]

    print(
        "E1_PAIR_FEASIBLE_PRIME_FIELD_REDUCTION_PASS "
        f"interval_checks={interval_checks} rowc_square_candidates=4"
    )


if __name__ == "__main__":
    main()
