#!/usr/bin/env python3
"""Independent consumer-backward audit of the C36' double split."""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_cutoff18_double_accident_reduction"
CONSUMER = "f3_h3_mobius_excess_half"


def main() -> None:
    aggregate_checks = 0
    values = tuple(product((0, 18, 19, 20, 36), (0, 1, 2, 7)))
    for left in values:
        for right in values:
            profile = (left, right)
            excess = tuple(max(p - 18, 0) for p, _ in profile)
            x18 = sum(q * r for q, (_, r) in zip(excess, profile, strict=True))
            y18 = sum(
                q * max(r - 1, 0)
                for q, (_, r) in zip(excess, profile, strict=True)
            )
            paid = x18 - y18
            expected_paid = sum(
                q for q, (_, r) in zip(excess, profile, strict=True) if r > 0
            )
            assert paid == expected_paid
            assert paid <= sum(p for p, _ in profile)
            aggregate_checks += 1

    implication_checks = 0
    for exponent in range(13, 42):
        n = 1 << exponent
        paid_cap = (n - 1) ** 2
        residual = 283 * n * n + 34 * n - 17
        assert 17 * paid_cap + residual == 300 * n * n

        largest_integral_y = residual // 17
        assert 17 * (paid_cap + largest_integral_y) <= 300 * n * n
        assert 17 * (paid_cap + largest_integral_y + 1) > 300 * n * n
        implication_checks += 1

    # The measured two-fiber profile exercises the load-bearing R=1 removal.
    boundary_profile = ((20, 1), (20, 1))
    boundary_x = sum(max(p - 18, 0) * r for p, r in boundary_profile)
    boundary_y = sum(max(p - 18, 0) * max(r - 1, 0) for p, r in boundary_profile)
    assert (boundary_x, boundary_y) == (4, 0)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    evidence = [
        edge
        for edge in dag["edges"]
        if edge["from"] == NODE and edge["to"] == CONSUMER
    ]
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] in ("TARGET", "CONDITIONAL")  # 2026-07-19 amber re-pose
    assert evidence == [{"from": NODE, "to": CONSUMER, "kind": "ev"}]

    print(
        "AUDIT_F3_H3_CUTOFF18_DOUBLE_ACCIDENT_REDUCTION_PASS "
        f"aggregate_checks={aggregate_checks} "
        f"implication_checks={implication_checks} "
        f"boundary_X18={boundary_x} boundary_Y18={boundary_y}"
    )


if __name__ == "__main__":
    main()
