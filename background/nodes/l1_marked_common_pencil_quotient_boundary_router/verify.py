#!/usr/bin/env python3
"""Verify the marked common-pencil quotient-boundary router."""

from __future__ import annotations

import itertools
import json
import math
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_marked_common_pencil_quotient_boundary_router"


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


def locator(roots: tuple[int, ...], prime: int) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [(-root) % prime, 1], prime)
    return out


def fiber_factor(ell: int, label: int, prime: int) -> list[int]:
    out = [0] * (ell + 1)
    out[0] = (-label) % prime
    out[ell] = 1
    return out


def check_field(prime: int, ell: int, fiber_count: int) -> tuple[int, int]:
    fibers_by_label: dict[int, tuple[int, ...]] = {}
    for label in range(1, prime):
        roots = tuple(x for x in range(1, prime) if pow(x, ell, prime) == label)
        if len(roots) == ell:
            fibers_by_label[label] = roots

    labels = tuple(sorted(fibers_by_label)[:fiber_count])
    assert len(labels) == fiber_count
    fibers = {label: fibers_by_label[label] for label in labels}
    core = tuple(root for label in labels for root in fibers[label])
    assert len(core) == len(set(core)) == ell * fiber_count

    seen: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    profile_count: Counter[tuple[int, int]] = Counter()
    checks = 0

    for mask in range(1 << len(core)):
        defect = {core[index] for index in range(len(core)) if mask >> index & 1}
        full = tuple(label for label in labels if set(fibers[label]) <= defect)
        full_roots = {root for label in full for root in fibers[label]}
        boundary = tuple(sorted(defect - full_roots))

        assert all(not set(fibers[label]) <= set(boundary) for label in labels)
        key = (boundary, full)
        assert key not in seen
        seen.add(key)

        reconstructed = set(boundary)
        for label in full:
            reconstructed.update(fibers[label])
        assert reconstructed == defect

        left = locator(tuple(sorted(defect)), prime)
        right = locator(boundary, prime)
        for label in full:
            right = mul(right, fiber_factor(ell, label, prime), prime)
        assert left == right

        beta = len(boundary)
        degree = len(defect)
        assert (degree - beta) % ell == 0
        assert len(full) == (degree - beta) // ell
        profile_count[(beta, len(full))] += 1
        checks += 7

    for (beta, full_count), count in profile_count.items():
        assert count <= math.comb(len(core), beta) * math.comb(fiber_count, full_count)
        checks += 1

    return checks, len(profile_count)


def main() -> None:
    checks = 0
    profiles = 0
    for prime, ell, fiber_count in ((13, 2, 3), (13, 3, 3), (17, 4, 3)):
        field_checks, field_profiles = check_field(prime, ell, fiber_count)
        checks += field_checks
        profiles += field_profiles

    # Fixed-boundary and fixed-polarity factors remain polynomial.
    for n in range(8, 65):
        for boundary_cap in range(5):
            boundary_choices = sum(math.comb(n, beta) for beta in range(boundary_cap + 1))
            assert boundary_choices <= (boundary_cap + 1) * n**boundary_cap
            checks += 1
        for p in range(5):
            q = n**3
            assert q ** (2 * p) == n ** (6 * p)
            checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_marked_common_pencil_crt_fiber_bound",
        "pma_quotient_closure_scope",
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
        "F_D=L_(B_D) product_(a in A_full(D))(P-a)",
        "q^(2P_0) binom(|C|,beta) max_B Q(B)",
        "does not prove that `Q(B)` is paid",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_QUOTIENT_BOUNDARY_PASS checks={checks} profiles={profiles}")


if __name__ == "__main__":
    main()

