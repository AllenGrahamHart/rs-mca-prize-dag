#!/usr/bin/env python3
"""Audit positive-DE pairing-13 signs, scope, and aggregate terminals."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
RESULT = ROOT / "experiments/prize_resolution" / (
    "rate_half_kb_positive_433_1b_cell4_positive_de_pairing13_"
    "nested_quadratic_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    products = ("de", "de", "-de", "df", "sigma_o*ef", "bf", "sigma_c*cf")
    residual = products[1:]
    matching = ((0, 5), (1, 3), (2, 4))
    pairs = tuple((residual[a], residual[b]) for a, b in matching)
    require(pairs == (("de", "sigma_c*cf"), ("-de", "sigma_o*ef"),
                      ("df", "bf")),
            "signed matching-13 pairs")
    payload = json.loads(RESULT.read_text())
    rows = payload["rows"]
    require(len(rows) == 16 and all(
        row["xi_index"] == 0 and row["pairing_index"] == 13 and
        row["status"] == "COMPLETE" and row["excluded"] and
        not row["witnesses"] and not row["unresolved"]
        for row in rows
    ), "exact row scope")
    require(sum(row["candidate_root_count"] for row in rows) == 224 and
            sum(row["target_root_count"] for row in rows) == 208 and
            sum(row["source_point_count"] for row in rows) == 320 and
            sum(sum(len(finite["uf_rows"])
                    for finite in row["finite_rows"]) for row in rows) == 1088 and
            sum(sum(uf_row["status"] == "MISSING_RELATION_NONZERO"
                    for finite in row["finite_rows"]
                    for uf_row in finite["uf_rows"]) for row in rows) == 960 and
            sum(row["uf_candidate_count"] for row in rows) == 128 and
            sum(sum(uf_row["status"] == "COLORED_PAIR_NONZERO"
                    for finite in row["finite_rows"]
                    for uf_row in finite["uf_rows"]) for row in rows) == 128 and
            sum(len(row["target_boundary_rows"]) for row in rows) == 0,
            "aggregate terminal ledger")
    require("previously transported negative omission is not counted" in
            (NODE / "audit.md").read_text(), "negative scope fence")
    print("audit=ok rows=16 candidates=224 relation_nonzero=960 colored_nonzero=128 witnesses=0")


if __name__ == "__main__":
    main()
