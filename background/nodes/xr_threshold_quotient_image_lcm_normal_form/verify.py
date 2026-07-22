#!/usr/bin/env python3
"""Verify the XR threshold quotient-image lcm normal form."""

from __future__ import annotations

from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_threshold_quotient_image_lcm_normal_form"
DEPENDENCY = "xr_agreement_raise_quotient_safe_sum_fence"
CONSUMER = "xr_tangent_support_mismatch_bridge"


def roots(prime: int, left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    if all(value == 0 for value in left + right):
        return ()
    return tuple(
        slope
        for slope in range(prime)
        if all((a + slope * b) % prime == 0 for a, b in zip(left, right))
    )


def transformed(
    prime: int,
    left: tuple[int, ...],
    right: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    if len(left) == 1:
        return tuple((2 * value) % prime for value in left), tuple(
            (2 * value) % prime for value in right
        )
    new_left = list(left)
    new_right = list(right)
    new_left[0] = (left[0] + left[1]) % prime
    new_right[0] = (right[0] + right[1]) % prime
    new_left[0], new_left[1] = new_left[1], new_left[0]
    new_right[0], new_right[1] = new_right[1], new_right[0]
    return tuple(new_left), tuple(new_right)


def finite_checks() -> tuple[int, int, int]:
    fixed = 0
    basis = 0
    unions = 0
    for prime in (3, 5, 7):
        for dimension in range(1, 4):
            vectors = tuple(product(range(prime), repeat=dimension))
            family: list[tuple[int, ...]] = []
            for left in vectors:
                for right in vectors:
                    support_roots = roots(prime, left, right)
                    assert len(support_roots) <= 1
                    fixed += 1

                    next_left, next_right = transformed(prime, left, right)
                    assert roots(prime, next_left, next_right) == support_roots
                    basis += 1

                    family.append(support_roots)
                    if len(family) == 11:
                        union = {root for item in family for root in item}
                        factors = {item[0] for item in family if item}
                        assert union == factors
                        unions += 1
                        family.clear()
            if family:
                union = {root for item in family for root in item}
                factors = {item[0] for item in family if item}
                assert union == factors
                unions += 1
    return fixed, basis, unions


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "g_S(Z)=1",
        "#distinctbadslopeswitnessedbyS=degR_S",
        "doesnotbound`degR_S`",
    ):
        assert marker in statement


def main() -> None:
    fixed, basis, unions = finite_checks()
    packet_check()
    print(
        "XR_THRESHOLD_QUOTIENT_IMAGE_LCM_NORMAL_FORM_PASS "
        f"fixed={fixed} basis={basis} unions={unions}"
    )


if __name__ == "__main__":
    main()
