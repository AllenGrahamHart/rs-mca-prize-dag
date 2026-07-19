#!/usr/bin/env python3
"""Verify the H3 ideal-star prime-alignment criterion contract."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_ideal_star_prime_alignment_criterion"
DEPENDENCY = "f3_h3_low_distance_ideal_star_router"
CONSUMER = "f3_h3_mobius_excess_half"
PILOT = ROOT / "experiments/prize_resolution/h3_low_distance_ideal_star_alignment_pilot_result.json"


def exact_order_roots(prime: int, order: int) -> set[int]:
    return {
        value for value in range(1, prime)
        if pow(value, order, prime) == 1
        and pow(value, order // 2, prime) == prime - 1
    }


def root_and_dilation_check() -> int:
    checked = 0
    for order, prime in ((8, 17), (8, 41), (16, 97)):
        roots = exact_order_roots(prime, order)
        assert len(roots) == order // 2
        generator = min(roots)
        assert {pow(generator, r, prime) for r in range(1, order, 2)} == roots
        for left in range(1, order):
            for right in range(left, order):
                for r in range(1, order, 2):
                    beta_conjugate = (
                        (1 - pow(generator, r * left, prime))
                        * (1 - pow(generator, r * right, prime))
                    ) % prime
                    moved_left, moved_right = sorted((r * left % order, r * right % order))
                    beta_moved = (
                        (1 - pow(generator, moved_left, prime))
                        * (1 - pow(generator, moved_right, prime))
                    ) % prime
                    assert beta_conjugate == beta_moved
                    checked += 1
    return checked


def dag_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    refs = set(nodes[NODE]["refs"])
    for name in (
        "statement.md", "proof.md", "claim_contract.md",
        "dependency_subdag.md", "audit.md", "result.md",
        "verify.py", "verify_audit.py",
    ):
        assert f"background/nodes/{NODE}/{name}" in refs
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges


def pilot_check() -> tuple[int, int]:
    rows = json.loads(PILOT.read_text())["results"]
    counts = tuple(len(row["aligned_ideal_star_primes"]) for row in rows)
    assert counts == (18, 162)
    assert all(row["complete"] for row in rows)
    return counts


def main() -> None:
    dilation_checks = root_and_dilation_check()
    dag_check()
    small, large = pilot_check()
    print(
        "F3_H3_IDEAL_STAR_PRIME_ALIGNMENT_CRITERION_PASS "
        f"dilation_checks={dilation_checks} pilot={small}/{large} dag=1/1"
    )


if __name__ == "__main__":
    main()
