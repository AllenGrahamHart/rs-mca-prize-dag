#!/usr/bin/env python3
"""Verify the XR support-only exponential-width route fence."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_nongeneric_support_only_exponential_width_fence"
CONSUMER = "xr_tangent_support_mismatch_bridge"

ROWS = (
    ("RowC-1/4", 10, 261, 6, 163),
    ("RowC-1/8", 10, 133, 6, 83),
    ("RowC-1/16", 10, 67, 4, 41),
    ("prize-1/4", 41, 558_345_748_481, 8_589_934_594, 348_966_092_800),
    ("prize-1/8", 41, 283_467_841_537, 8_589_934_594, 177_167_400_960),
    ("prize-1/16", 41, 141_733_920_769, 4_294_967_298, 88_583_700_480),
)


def official_arithmetic() -> None:
    for _name, log_n, agreement, capital_h, floor_exponent in ROWS:
        n = 1 << log_n
        assert 2 * agreement <= n
        assert 16 * capital_h <= agreement
        assert 5 * agreement // 8 == floor_exponent
        assert 5 * agreement > 8 * (4 + 3 * log_n)

    # This integer inequality proves log_2(16/15)<2/15.
    assert 16**15 < 4 * 15**15


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
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
        "|mathcal Y|>16n^3",
        "|mathcal Y|>2^(5A/8)",
        "not a counterexample",
        "support packing alone",
    ):
        assert marker in text


def main() -> None:
    official_arithmetic()
    packet_check()
    print("XR_NONGENERIC_SUPPORT_ONLY_EXPONENTIAL_WIDTH_FENCE_PASS rows=6")


if __name__ == "__main__":
    main()
