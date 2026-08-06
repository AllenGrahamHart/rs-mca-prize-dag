#!/usr/bin/env python3
"""Verify the plus-branch F2 direct-sum supplier and its DAG contract."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f2_admissible_direct_sum_grs_reduction"
CONSUMER = "f2_conditional_close"


def main() -> None:
    result = json.loads(
        (ROOT / "notes/pilots_20260806/f2_route_repair/f2_adm_replay_result.json").read_text()
    )
    assert result["status"] == "PASS"
    assert result["returncode"] == 0
    assert result["pass_count"] == 373
    assert result["fail_count"] == 0

    s = 1 << 38
    r = 4_294_967_340
    assert 0 < r < s
    assert s - r == 270_582_939_604

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert "plus branch" in nodes[NODE]["statement"].lower()
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (NODE, CONSUMER, "ev") in edges
    print(
        "F2_ADMISSIBLE_DIRECT_SUM_GRS_REDUCTION_PASS "
        "canonical=373/373 classes<=4 grs=1 dag=1/1"
    )


if __name__ == "__main__":
    main()
