#!/usr/bin/env python3
"""Verify the L1 core bipolar signed-quotient normal form."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_core_bipolar_signed_quotient_normal_form"


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def mul(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % prime
    return trim(out)


def locator(roots: set[int], prime: int) -> list[int]:
    out = [1]
    for root in sorted(roots):
        out = mul(out, [(-root) % prime, 1], prime)
    return out


def fiber_factor(ell: int, label: int, prime: int) -> list[int]:
    out = [0] * (ell + 1)
    out[0] = (-label) % prime
    out[ell] = 1
    return out


def check_field(prime: int, ell: int, fiber_count: int) -> tuple[int, int]:
    fibers_by_label: dict[int, set[int]] = {}
    for label in range(1, prime):
        roots = {x for x in range(1, prime) if pow(x, ell, prime) == label}
        if len(roots) == ell:
            fibers_by_label[label] = roots
    labels = tuple(sorted(fibers_by_label)[:fiber_count])
    assert len(labels) == fiber_count
    fibers = {label: fibers_by_label[label] for label in labels}
    core = tuple(root for label in labels for root in sorted(fibers[label]))

    checks = 0
    for mask in range(1 << len(core)):
        defect = {core[index] for index in range(len(core)) if mask >> index & 1}
        dense = tuple(
            label for label in labels if len(defect & fibers[label]) > ell / 2
        )
        dense_roots = set().union(*(fibers[label] for label in dense)) if dense else set()
        holes = dense_roots - defect
        sparse = defect - dense_roots

        assert not (holes & sparse)
        reconstructed = (dense_roots - holes) | sparse
        assert reconstructed == defect

        left = mul(locator(defect, prime), locator(holes, prime), prime)
        right = locator(sparse, prime)
        for label in dense:
            right = mul(right, fiber_factor(ell, label, prime), prime)
        assert left == right

        polarity = sum(
            min(len(defect & fibers[label]), ell - len(defect & fibers[label]))
            for label in labels
        )
        assert len(holes) + len(sparse) == polarity
        checks += 5

    return checks, 1 << len(core)


def main() -> None:
    checks = 0
    profiles = 0
    for prime, ell, fiber_count in ((13, 2, 3), (13, 3, 3), (17, 4, 3)):
        field_checks, field_profiles = check_field(prime, ell, fiber_count)
        checks += field_checks
        profiles += field_profiles

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_marked_common_pencil_quotient_boundary_router",
        "l1_quotient_chart_bipolar_entropy_closure",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    for consumer in (
        "l1_mixed_residual_intersection_pin",
        "l1_mixed_petal_amplification",
        "petal_mixed_amplification",
    ):
        assert (NODE, consumer, "ev") in edges
        checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "F_D L_(H_D)",
        "=p_core(D)",
        "reconstructs",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_SIGNED_QUOTIENT_PASS checks={checks} profiles={profiles}")


if __name__ == "__main__":
    main()

