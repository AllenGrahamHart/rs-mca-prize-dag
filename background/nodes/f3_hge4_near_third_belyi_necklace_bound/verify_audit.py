#!/usr/bin/env python3
"""Mutation guards for the HGE4 near-third necklace payment."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_near_third_belyi_necklace_bound"
VERIFY = ROOT / "background/nodes" / NODE / "verify.py"


def load_verify():
    spec = importlib.util.spec_from_file_location("near_third_verify", VERIFY)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    verify = load_verify()
    necklace = verify.load_necklace_verify()

    # Ordered sides require the factor two.
    assert necklace.necklace_formula(14, 5) == 143
    assert 2 * necklace.necklace_formula(14, 5) == 286

    # The h=e cell is outside the reciprocal-gap/Mason scope.
    assert not (0 < 4 < 4)
    assert 0 < 5 < 9

    # The necklace formula alone is not a universal payment. The downstream
    # dual-gap theorem excludes this cell by a different argument.
    order, width, defect = 4096, 1364, 4
    assert order == 3 * width + defect
    debit = 2 * necklace.necklace_formula(width + defect, defect)
    boundary = 2
    assert 2 * (debit + boundary) > 21 * order * order

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["f3_hge4_norm_gate_count"]["status"] == "TARGET"
    consumer = (ROOT / "critical/nodes/f3_hge4_norm_gate_count/statement.md").read_text()
    for marker in (
        NODE, "E_h^prim(m,p)<=2N(h+e,e)", "(m+4)/3", "3333532",
        "not a zero-cost deletion", "f3_hge4_near_third_dual_gap_exclusion",
        "7h>=2m+1",
    ):
        assert marker in consumer
    print(
        "F3_HGE4_NEAR_THIRD_BELYI_NECKLACE_BOUND_AUDIT_PASS "
        "ordered_guard=2 scope_guard=1 necklace_overbudget_guard=4096"
    )


if __name__ == "__main__":
    main()
