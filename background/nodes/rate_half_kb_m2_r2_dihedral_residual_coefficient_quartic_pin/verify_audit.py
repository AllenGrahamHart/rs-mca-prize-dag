#!/usr/bin/env python3
"""Independent audit of the canonical coefficient-quartic pin."""

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

    required_terms = [
        "A P^4",
        "B S^2 P^2",
        "-2B P^3",
        "C S^4",
        "-4C S^2 P",
        "(2C+D)P^2",
        "E S^2",
        "-2E P",
    ]
    require(all(term in statement for term in required_terms), "printed quartic is incomplete")
    require("They are therefore siblings" in proof, "sibling semantic pin missing")
    require("irreducible plane quartic" in proof, "degree-four equality gate missing")
    require("Not claimed" in contract, "nonclaim boundary missing")
    require("rate_half_kb_m2_r2_dihedral_residual_coefficient_quartic_pin" in dag, "DAG node missing")


if __name__ == "__main__":
    audit()
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_RESIDUAL_COEFFICIENT_QUARTIC_PIN_AUDIT_PASS")
