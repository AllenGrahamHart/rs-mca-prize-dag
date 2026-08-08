#!/usr/bin/env python3
"""Audit the positive-DE pairing-14 common-f resultant and scope."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
RESULT = ROOT / "experiments/prize_resolution" / (
    "rate_half_kb_positive_433_1b_cell4_positive_de_pairing14_"
    "common_f_resultant_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    b0, b1, b2, c0, c1, c2, f = sp.symbols(
        "b0 b1 b2 c0 c1 c2 f"
    )
    pb = b0 + b1*f + b2*f**2
    pc = c0 + c1*f + c2*f**2
    resultant = sp.resultant(pb, pc, f)
    printed = (
        (b2*c0-b0*c2)**2
        - (b2*c1-b1*c2)*(b1*c0-b0*c1)
    )
    require(sp.expand(resultant-printed) == 0,
            "division-free quadratic resultant identity")

    payload = json.loads(RESULT.read_text())
    rows = payload["rows"]
    require(len(rows) == 16 and all(
        row["status"] == "COMPLETE" and row["excluded"] and
        not row["witnesses"] and not row["unresolved"]
        for row in rows
    ), "complete exact rows")
    require(sum(row["candidate_root_count"] for row in rows) == 152 and
            sum(row["source_point_count"] for row in rows) == 80 and
            sum(row["uf_candidate_count"] for row in rows) == 128 and
            sum(len(row["target_boundary_rows"]) for row in rows) == 0,
            "printed terminal ledger")
    require(all(row["common_f_resultant"] and
                (row["p_b_degree"], row["p_c_degree"]) == (2, 2)
                for row in rows), "quadratic source ledger")
    require("outside the printed positive-`DE` scope" in
            (NODE / "audit.md").read_text(), "scope fence")
    require("incomplete common-root or quartic" in
            (NODE / "statement.md").read_text(), "root-completeness falsifier")
    print("audit=ok resultant=quadratic rows=16 candidates=152 witnesses=0")


if __name__ == "__main__":
    main()
