#!/usr/bin/env python3
"""Verify the prize-field-floor even-norm exclusion."""

from __future__ import annotations

import hashlib
import json
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_field_floor_even_norm_exclusion"
DICTIONARY = "e1_low_square_mass_weighted_kernel_dictionary"
TARGET = "e1_official_low_square_mass_pair_budget"
B_PRIZE = 317494674775468773183020924238786383963


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    checks = 0
    p_min = B_PRIZE * 2**128
    assert B_PRIZE > 2**127
    assert 2 * p_min > 2**256
    assert 16**64 == 2**256
    assert 4**128 == 2**256
    assert 18**64 > 2**256
    assert 6**128 > 2**256
    checks += 6

    # Exhaust the class-vector parity input at small dimensions.
    for h, ell in ((4, 2), (5, 3), (6, 4)):
        T = min(ell, 2 * h - ell)
        classes = []
        for vector in product((-1, 0, 1), repeat=h):
            support = sum(value != 0 for value in vector)
            if support <= T and support % 2 == ell % 2:
                classes.append(vector)
        for x in classes:
            for y in classes:
                if x == y:
                    continue
                assert sum(left - right for left, right in zip(x, y)) % 2 == 0
                checks += 1

    pins = json.loads((Path(__file__).with_name("source_pin.json")).read_text())
    for file_key, hash_key in (
        ("prime_reduction_proof_file", "prime_reduction_proof_sha256"),
        ("square_mass_statement_file", "square_mass_statement_sha256"),
        ("norm_radius_statement_file", "norm_radius_statement_sha256"),
    ):
        assert sha256(ROOT / pins[file_key]) == pins[hash_key]
        checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "e1_pair_feasible_prime_field_reduction",
        "e1_collision_square_mass_reparametrization",
        "e1_prime_field_l2_norm_collision_radius",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    assert (NODE, DICTIONARY, "req") in edges
    assert (NODE, TARGET, "ev") in edges
    assert (NODE, TARGET, "req") not in edges
    checks += 5

    print(
        "E1_PRIZE_FIELD_FLOOR_EVEN_NORM_EXCLUSION_PASS "
        f"n256_mass_cap=16 n512_mass_cap=4 checks={checks}"
    )


if __name__ == "__main__":
    main()
