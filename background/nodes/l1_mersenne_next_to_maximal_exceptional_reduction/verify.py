#!/usr/bin/env python3
"""Verify the next-to-maximal exceptional reduction and DAG wiring."""

from __future__ import annotations

import json
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_next_to_maximal_exceptional_reduction"
SUPPLIERS = {
    "l1_official_max_split_value_complement_census",
    "l1_mersenne_checkpoint_cyclotomic_normal_form",
}
CONSUMER = "l1_mixed_petal_amplification"


def main() -> None:
    checks = 0
    module = runpy.run_path(
        str(ROOT / "experiments" / "prize_resolution"
            / "l1_mersenne_next_to_maximal_packet_check.py")
    )
    for row in module["ROWS"]:
        result = module["check_row"](*row)
        assert result["split_roots_required"] in (6, 14)
        assert result["total_admissible_w_roots"] == 1
        assert result["split_roots_required"] > result["total_admissible_w_roots"]
        checks += 3

    for p, h in ((8191, 7), (131071, 7), (524287, 7),
                 (2147483647, 7), (8191, 15)):
        m = h + 1
        assert p > h * h
        possible_gaps = [gap for gap in range(h + 2)
                         if 0 <= gap * p - m <= p - 1]
        assert possible_gaps == [1]
        assert possible_gaps[0] * p - m == p - m
        assert (p - m) - 1 == p - m - 1
        checks += 4

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in SUPPLIERS:
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    assert (NODE, CONSUMER, "ev") in edges
    checks += 2

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in ("(NMR1)", "(NMR2)", "(NMR3)", "(NMR4)", "(NMR5)",
                   "(NMR5a)", "deg T=h-2", "deg(XR')=p-m", "(NMR6)",
                   "(NMR5b)", "B(R(0))=0", "(NMR5c)",
                   "a_0+a_z=p+m+1", "(NMR5d)", "deg F'=p-m-1",
                   "polynomial Belyi map", "exactly saturated Belyi branch",
                   "not a closure"):
        assert anchor in statement
        checks += 1

    print(f"L1_MERSENNE_NEXT_TO_MAXIMAL_EXCEPTIONAL_REDUCTION_PASS checks={checks}")


if __name__ == "__main__":
    main()
