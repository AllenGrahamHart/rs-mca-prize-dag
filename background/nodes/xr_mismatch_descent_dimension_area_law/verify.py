#!/usr/bin/env python3
"""Verify the XR mismatch-descent dimension area law."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_mismatch_descent_dimension_area_law"
DEPENDENCY = "xr_mismatch_nongeneric_invariant_excess_descent"
CONSUMER = "xr_tangent_support_mismatch_bridge"


@lru_cache(maxsize=None)
def extrema(n: int, k: int, h: int, kappa: int) -> tuple[int, int, int]:
    """Return maximum area, total d, and threshold occupancy over all chains."""
    area_max = 0
    drop_max = 0
    occupancy_max = 0
    for d in range(k):
        next_k = k - d
        next_a = next_k + h
        max_next_n = n - k - h
        for next_n in range(next_a, max_next_n + 1):
            area, drop, occupancy = extrema(next_n, next_k, h, kappa)
            area_max = max(area_max, k + h + area)
            drop_max = max(drop_max, d + drop)
            occupancy_max = max(
                occupancy_max, int(k >= kappa) + occupancy
            )
    return area_max, drop_max, occupancy_max


def recurrence_check() -> int:
    checks = 0
    for n in range(2, 31):
        for h in range(1, n):
            H = h + 1
            for k in range(1, n - h + 1):
                if k + h > n:
                    continue
                for kappa in range(1, k + 2):
                    area, drop, occupancy = extrema(n, k, h, kappa)
                    assert area <= n - H
                    assert drop <= k - 1
                    assert occupancy <= (n - H) // (kappa + h)
                    checks += 1
    return checks


def official_check() -> None:
    rows = (
        ("RowC-1/4", 1024, 256, 261, (92, 59, 35, 19, 10, 5)),
        ("RowC-1/8", 1024, 128, 133, (92, 59, 35, 19, 10, None)),
        ("RowC-1/16", 1024, 64, 67, (145, 92, 53, 29, 15, None)),
        (
            "prize-1/4",
            2**41,
            2**39,
            558_345_748_481,
            (127, 84, 50, 28, 14, 7),
        ),
        (
            "prize-1/8",
            2**41,
            2**38,
            283_467_841_537,
            (127, 84, 50, 28, 14, None),
        ),
        (
            "prize-1/16",
            2**41,
            2**37,
            141_733_920_769,
            (255, 170, 102, 56, 30, None),
        ),
    )
    for _name, n, k, agreement, expected in rows:
        h = agreement - k
        H = h + 1
        actual = []
        for multiplier in (1, 2, 4, 8, 16, 32):
            kappa = multiplier * H
            actual.append(None if kappa > k else (n - H) // (kappa + h))
        assert tuple(actual) == expected


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join(
        (base / name).read_text() for name in required if name.endswith(".md")
    )
    for marker in (
        "sum_(j<L)(K_j+h)<=N_0-H",
        "sum_(j<L)d_j=K_0-K_L<=K_0-1",
        "L_kappa<=floor((N_0-H)/(kappa+h))",
        "sum_(j<L)(K_j-1)<=r+sH",
        "No branch-width or slope bound is claimed",
    ):
        assert marker in text


def main() -> None:
    checks = recurrence_check()
    official_check()
    packet_check()
    print(
        "XR_MISMATCH_DESCENT_DIMENSION_AREA_LAW_PASS "
        f"recurrence_checks={checks} official_rows=6"
    )


if __name__ == "__main__":
    main()

