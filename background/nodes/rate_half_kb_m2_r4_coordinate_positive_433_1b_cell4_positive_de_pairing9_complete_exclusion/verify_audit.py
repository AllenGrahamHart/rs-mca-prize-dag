#!/usr/bin/env python3
"""Audit positive-DE pairing-9 signs, scope, and aggregate terminals."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
RESULT = ROOT / "experiments/prize_resolution" / (
    "rate_half_kb_positive_433_1b_cell4_positive_de_pairing9_"
    "nested_quadratic_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    products = ("de", "de", "-de", "df", "sigma_o*ef", "bf", "sigma_c*cf")
    residual = products[1:]
    matching = ((0, 4), (1, 2), (3, 5))
    pairs = tuple((residual[a], residual[b]) for a, b in matching)
    require(pairs == (("de", "bf"), ("-de", "df"),
                      ("sigma_o*ef", "sigma_c*cf")),
            "signed matching-9 pairs")
    payload = json.loads(RESULT.read_text())
    rows = payload["rows"]
    require(len(rows) == 16 and all(
        row["xi_index"] == 0 and row["pairing_index"] == 9 and
        row["status"] == "COMPLETE" and row["excluded"] and
        not row["witnesses"] and not row["unresolved"]
        for row in rows
    ), "exact row scope")
    require(sum(row["candidate_root_count"] for row in rows) == 288 and
            sum(row["source_point_count"] for row in rows) == 544 and
            sum(row["uf_candidate_count"] for row in rows) == 192 and
            sum(len(row["target_boundary_rows"]) for row in rows) == 0,
            "aggregate terminal ledger")
    require("previously transported negative omission is not counted" in
            (NODE / "audit.md").read_text(), "negative scope fence")
    print("audit=ok rows=16 candidates=288 colored_nonzero=192 witnesses=0")


if __name__ == "__main__":
    main()
