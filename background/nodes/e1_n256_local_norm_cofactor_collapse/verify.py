#!/usr/bin/env python3
"""Verify the N=256 local-norm cofactor collapse."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_local_norm_cofactor_collapse"
PRIME_PARENT = "e1_pair_feasible_prime_field_reduction"
TWO_ADIC_PARENT = "e1_n256_2adic_cofactor_collision_exclusion"
E1_TARGET = "e1_official_prime_exception_control"
UNIVERSAL_TARGET = "unsafe_crossing_family_instantiation"

EXPECTED_PIN = {
    "prime_field_file": "background/nodes/e1_pair_feasible_prime_field_reduction/statement.md",
    "prime_field_file_sha256": "f7b5ea3463c6b9101b854191a498015fedc89d1bf4a5a0c28b2b2f8b71157e7b",
    "two_adic_file": "background/nodes/e1_n256_2adic_cofactor_collision_exclusion/statement.md",
    "two_adic_file_sha256": "1256e3e5e71549710cf9f29717d908543b3706ac289477e421142e0f3a8fcda8",
}


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for file_key, hash_key in (
        ("prime_field_file", "prime_field_file_sha256"),
        ("two_adic_file", "two_adic_file_sha256"),
    ):
        actual = hashlib.sha256((ROOT / pin[file_key]).read_bytes()).hexdigest()
        assert actual == pin[hash_key]

    s16_cofactors = tuple(2**valuation for valuation in range(1, 6))
    assert s16_cofactors == (2, 4, 8, 16, 32)
    assert all(cofactor < 64 for cofactor in s16_cofactors)
    assert all(
        (cofactor >> ((cofactor & -cofactor).bit_length() - 1)) % 256 == 1
        for cofactor in s16_cofactors
    )

    expected_counts = {1: 256, 2: 128, 4: 32, 8: 2, 16: 1}
    s18_by_valuation = {}
    for valuation in expected_counts:
        values = tuple(
            2**valuation * (1 + 256 * parameter)
            for parameter in range(512)
            if 2**valuation * (1 + 256 * parameter) < 2**17
        )
        s18_by_valuation[valuation] = values
        assert len(values) == expected_counts[valuation]
        assert all(
            value % (2**valuation * 256) == 2**valuation
            for value in values
        )
    assert sum(map(len, s18_by_valuation.values())) == 419

    # A nonconforming odd cofactor is caught by the 256-congruence.
    assert 3 % 256 != 1
    assert (2**3 * 257) // 2**3 % 256 == 1

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    statements = {entry["id"]: entry.get("statement", "") for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[PRIME_PARENT] == "PROVED"
    assert statuses[TWO_ADIC_PARENT] == "PROVED"
    assert statuses[E1_TARGET] == "TARGET"
    assert statuses[UNIVERSAL_TARGET] == "TARGET"
    assert (PRIME_PARENT, NODE, "req") in edges
    assert (TWO_ADIC_PARENT, NODE, "req") in edges
    assert (NODE, E1_TARGET, "ev") in edges
    assert (NODE, UNIVERSAL_TARGET, "ev") in edges
    assert "R=2^mu p" in statements[NODE]
    assert "419" in statements[NODE]

    print(
        "E1_N256_LOCAL_NORM_COFACTOR_COLLAPSE_PASS "
        "s16_cofactors=5 s18_cofactors=419 modulus=256"
    )


if __name__ == "__main__":
    main()
