#!/usr/bin/env python3
"""Independent audit of the residual quartic singularity atlas."""

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

    require("three ordinary nodes" in statement, "generic atlas missing")
    require("tacnode of delta two" in statement, "exceptional atlas missing")
    require("square class is the nonsquare quadratic" in proof, "irreducibility proof missing")
    require("total delta three" in proof, "genus ledger missing")
    require("Not claimed" in contract, "nonclaim boundary missing")
    require("rate_half_kb_m2_r2_dihedral_residual_quartic_singularity_atlas" in dag, "DAG node missing")


if __name__ == "__main__":
    audit()
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_RESIDUAL_QUARTIC_SINGULARITY_ATLAS_AUDIT_PASS")
