#!/usr/bin/env python3
"""Verify the higher-rank uniform split-pencil reduction packet."""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_higher_rank_uniform_split_pencil_reduction"
DEPENDENCIES = {
    "xr_rs_flat_nullity_basis_charge",
    "xr_poststrip_affine_pencil_charge",
}
CONSUMER = "xr_highcore_collision_count"
PRIME = 1_000_003


def inverse(value: int) -> int:
    return pow(value % PRIME, PRIME - 2, PRIME)


def locator_dual_check() -> int:
    cases = 0
    for a in range(1, 10):
        for h in range(1, 6):
            points = list(range(1, a + h + 1))
            for degree in range(h):
                values = []
                for x in points:
                    numerator = 1
                    for root in points[:degree]:
                        numerator = numerator * (x - root) % PRIME
                    derivative = 1
                    for y in points:
                        if y != x:
                            derivative = derivative * (x - y) % PRIME
                    values.append(numerator * inverse(derivative) % PRIME)
                assert sum(value != 0 for value in values) >= a + 1
                for power in range(a):
                    assert sum(
                        value * pow(x, power, PRIME)
                        for x, value in zip(points, values)
                    ) % PRIME == 0
                cases += 1

    # The coordinate columns of dual RS_2 annihilate both slope moments.
    for t in range(4, 13):
        slopes = list(range(1, t + 1))
        for degree in range(t - 2):
            column = []
            for x in slopes:
                derivative = 1
                for y in slopes:
                    if y != x:
                        derivative = derivative * (x - y) % PRIME
                column.append(pow(x, degree, PRIME) * inverse(derivative) % PRIME)
            assert sum(column) % PRIME == 0
            assert sum(x * value for x, value in zip(slopes, column)) % PRIME == 0
            cases += 1
    return cases


def rank_two_arithmetic() -> tuple[int, int]:
    parameter_cases = 0
    profile_cases = 0
    for a in range(2, 33):
        for h in range(1, 9):
            for t in range(4, a + 3):
                for rho in range(a + 2, 2 * a + 1):
                    if rho * (t - 2) > a * t:
                        continue
                    assert t <= a + 2
                    assert rho <= 2 * a
                    assert rho - a - 1 <= a - 1
                    zero_packing = rho <= a + h or t * (rho - a - h) <= rho
                    assert zero_packing == ((t - 1) * rho <= t * (a + h))
                    parameter_cases += 1

    # Exhaust the exact zero-set inequalities at small ranks. Pairwise
    # disjoint zero sets are encoded only by their sizes.
    for a in range(2, 6):
        for t in range(4, a + 3):
            for rho in range(a + 2, 2 * a + 1):
                max_zero = rho - a - 1
                if max_zero < 1:
                    continue
                for zeros in product(range(1, max_zero + 1), repeat=t):
                    if sum(zeros) > rho:
                        continue
                    if any(
                        rho - zeros[i] - zeros[j] > a
                        for i in range(t)
                        for j in range(i + 1, t)
                    ):
                        continue
                    pair_sum = sum(
                        rho - zeros[i] - zeros[j]
                        for i in range(t)
                        for j in range(i + 1, t)
                    )
                    assert rho * (t - 1) * (t - 2) // 2 <= pair_sum
                    assert pair_sum <= a * t * (t - 1) // 2
                    assert rho * (t - 2) <= a * t
                    profile_cases += 1
    assert parameter_cases > 10_000
    assert profile_cases > 0
    return parameter_cases, profile_cases


def maxwell_arithmetic() -> int:
    cases = 0
    for a in range(1, 33):
        for h in range(1, 9):
            for e in range(h):
                for private in range((h - e - 1) // 2 + 1):
                    assert e + 2 * private <= h - 1
                    cases += 1
            for n in range(a + h, a + h + 20):
                bound = (2 * n + h - (2 * a + 1)) // h
                assert h * bound <= 2 * n + h - (2 * a + 1)
                assert h * (bound + 1) > 2 * n + h - (2 * a + 1)
    return cases


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    for dependency in DEPENDENCIES:
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md",
        "dependency_subdag.md", "audit.md", "result.md", "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = (base / "statement.md").read_text() + (base / "proof.md").read_text()
    for marker in ("h|G|=2v_G-2a+e", "rank M_G<=2v_G-(2a+1)", "4<=t<=a+2"):
        assert marker in text


def main() -> None:
    parameters, profiles = rank_two_arithmetic()
    maxwell = maxwell_arithmetic()
    locator = locator_dual_check()
    packet_check()
    print(
        "XR_HIGHER_RANK_UNIFORM_SPLIT_PENCIL_PASS "
        f"parameters={parameters} profiles={profiles} maxwell={maxwell} "
        f"locator={locator}"
    )


if __name__ == "__main__":
    main()
