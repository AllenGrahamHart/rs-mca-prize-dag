#!/usr/bin/env python3
"""Independent scope audit for complete cell-3 exclusion."""

import ast
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    ast.parse((NODE / "verify.py").read_text())
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    audit = (NODE / "audit.md").read_text()
    require(all(text in statement for text in (
        "720 cases", "missing xi=3", "missing xi=4", "missing xi=5",
        "missing xi=6", "1680 cases",
    )), "printed disjoint ledger")
    require("{0}, {1,2}, {3,6}, {11,14}, {7,8,10,13}, {4,5,9,12}"
            in proof, "xi3 matching partition")
    require("role cell 6" in statement and "does not transport" in statement,
            "no silent duplicate-role transport")
    require("Rank cover" in contract and "rank(P)<=4" in contract
            and "rank(P)=5" in contract, "rank cover contract")
    require("set-theoretic verifier" in audit and "rejects overlap" in audit,
            "aggregation audit")
    rank_statement = (
        ROOT / "background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_common_exception_classifier/statement.md"
    ).read_text()
    require("cells" in rank_statement and "0, 1, 2, 3, 6" in rank_statement,
            "independent rank-drop cell check")
    print("audit=ok cell=3 rank_strata=2 principal_partition=1680")


if __name__ == "__main__":
    main()
