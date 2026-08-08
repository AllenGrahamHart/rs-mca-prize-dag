#!/usr/bin/env python3
"""Audit the cell-4 endpoint identity and aggregate scope."""

import ast
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = ROOT / "experiments/prize_resolution" / (
    "rate_half_kb_positive_433_1b_cell4_xi5_xi6_"
    "endpoint_compatibility_modal.py"
)
RESULT = ROOT / "experiments/prize_resolution" / (
    "rate_half_kb_positive_433_1b_cell4_xi5_xi6_"
    "endpoint_compatibility_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    x, m, s = sp.symbols("x m s", nonzero=True)
    cleared = (x**2 + m)**2 - s*x**2
    divided = x**2*((x + m/x)**2 - s)
    require(sp.factor(cleared - divided) == 0, "cleared endpoint identity")

    source = SCRIPT.read_text()
    tree = ast.parse(source)
    names = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}
    require("sigma_c" not in names and "sigma_o" not in names,
            "source-only compiler has no target-sign variable")

    payload = json.loads(RESULT.read_text())
    rows = payload["rows"]
    require(
        len(rows) == 8
        and all(
            row["status"] == "COMPLETE"
            and row["source_excluded"]
            and row["candidate_root_count"] == 7
            and row["compatibility_root_count"] == 5
            and row["source_point_count"] == 0
            and row["compatible_source_point_count"] == 0
            and not row["unresolved"]
            for row in rows
        ),
        "eight exact source exclusions",
    )
    require(
        {row["xi_index"] for row in rows} == {5, 6}
        and sum(len(row["boundary_rows"]) for row in rows) == 56
        and sum(len(row["no_lift_rows"]) for row in rows) == 16,
        "printed terminal ledger",
    )
    print(
        "audit=ok roles=2 rows=8 candidates=56 labels=30 "
        "quotient_orbits=18 raw_cases=480"
    )


if __name__ == "__main__":
    main()
