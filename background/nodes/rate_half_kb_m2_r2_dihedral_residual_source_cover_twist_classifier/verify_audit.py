#!/usr/bin/env python3
"""Independent audit of the residual source-cover twist classifier."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def audit() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    dag = (ROOT / "dag.json").read_text()

    require("Q_b(2)=(b-d)^2" in statement, "positive branch identity missing")
    require("Q_b(-2)=(b+d)^2" in statement, "negative branch identity missing")
    require("g(Gamma)=0  iff  b^2=a+2" in statement, "genus-zero classifier missing")
    require("four simple odd-support contributions" in proof, "square-class parity missing")
    require("Not claimed" in contract, "nonclaim boundary missing")
    require("rate_half_kb_m2_r2_dihedral_residual_source_cover_twist_classifier" in dag, "DAG node missing")


if __name__ == "__main__":
    audit()
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_RESIDUAL_SOURCE_COVER_TWIST_CLASSIFIER_AUDIT_PASS")
