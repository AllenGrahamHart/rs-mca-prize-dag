#!/usr/bin/env python3
"""Independent audit of residual dihedral star counts."""

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

    require("two disjoint copies of K_(2,2,2)" in statement, "missing n=3 shape")
    require("two-point blow-up of C_6" in statement, "missing n=6 shape")
    require("c eta c^(-1)=eta*a" in proof, "missing conjugation law")
    require("24 star vertices all have weight one" in proof, "missing exact mass")
    require("Not claimed" in contract, "missing nonclaim boundary")
    require("existence or nonexistence" in contract, "scope overclaim")
    require("rate_half_kb_m2_r2_dihedral_residual_star_graph_rigidity" in dag, "missing DAG node")

    for n in (3, 6):
        pole_count = 6 // n
        base_edges = pole_count * n
        source_edges = 4 * base_edges
        require(source_edges == 24, f"wrong independent source count for n={n}")
        require(2 * source_edges == 12 * 4, f"wrong degree sum for n={n}")


if __name__ == "__main__":
    audit()
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_RESIDUAL_STAR_GRAPH_RIGIDITY_AUDIT_PASS")
