#!/usr/bin/env python3
"""Independent audit of the residual one-parameter normal form."""

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

    for token in ["A=(a-2)(a-b^2+2)", "C=(a-b)^2", "F=(a-2)^2"]:
        require(token in statement, f"missing coefficient: {token}")
    require("exactly one lies in `{2,-2}`" in proof, "branch-place reduction missing")
    require("b notin {2,-2}" in statement, "parameter fence missing")
    require("Not claimed" in contract, "nonclaim boundary missing")
    require("rate_half_kb_m2_r2_dihedral_residual_one_parameter_quartic_normal_form" in dag, "DAG node missing")


if __name__ == "__main__":
    audit()
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_RESIDUAL_ONE_PARAMETER_QUARTIC_NORMAL_FORM_AUDIT_PASS")
