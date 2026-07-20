#!/usr/bin/env python3
"""Verify the polarized support-profile count and DAG contract."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_polarized_petal_entropy_ledger"


def main() -> None:
    checks = 0
    profiles = 0

    for ell in range(2, 8):
        for petals in range(1, 6):
            for cap in range(0, 5):
                exact_weight = 0
                profile_count = 0
                for sizes in itertools.product(range(ell + 1), repeat=petals):
                    polar = sum(min(a, ell - a) for a in sizes)
                    if polar > cap:
                        continue
                    profile_count += 1
                    exact_weight += math.prod(math.comb(ell, a) for a in sizes)
                vector_bound = (2**petals) * math.comb(petals + cap, cap)
                assert profile_count <= vector_bound
                assert exact_weight <= vector_bound * (ell**cap)
                checks += 2
                profiles += profile_count

    # The new coordinate is strictly stronger on a singleton/full profile.
    for ell in range(3, 30):
        sizes = (1, ell, ell)
        polar = sum(min(a, ell - a) for a in sizes)
        deficit = sum(ell - a for a in sizes)
        assert polar == 1
        assert deficit == ell - 1
        assert polar < deficit
        checks += 3

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge["kind"])
        for edge in dag["edges"]
    }
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["pma_petal_pattern_root_pinning_ledger"]["status"] == "PROVED"
    assert ("pma_petal_pattern_root_pinning_ledger", NODE, "req") in edges
    assert (NODE, "l1_mixed_residual_intersection_pin", "req") in edges
    checks += 4
    for consumer in (
        "l1_mixed_petal_amplification",
        "petal_mixed_amplification",
    ):
        assert (NODE, consumer, "ev") in edges
        checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "p=sum_i min(a_i,ell-a_i)",
        "2^M binom(M+E,E) n^(E+1)",
        "singleton petal contributes `1`",
    ):
        assert anchor in statement
        checks += 1

    print(
        "L1_POLARIZED_PETAL_ENTROPY_PASS "
        f"checks={checks} profiles={profiles}"
    )


if __name__ == "__main__":
    main()
