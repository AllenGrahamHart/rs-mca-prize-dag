#!/usr/bin/env python3
"""Verify the nu=2 base-field normalization ledger and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m4_h3_nu2_base_field_normalization"
SUPPLIERS = {
    "l1_m4_h3_nu2_prime_field_belyi_normal_form",
    "l1_m4_positive_value_coset_certificate",
}
CONSUMER = "l1_mixed_petal_amplification"


def main() -> None:
    checks = 0
    for p in (524287, 2147483647):
        assert p % 5 == 2
        assert pow(5, (p - 1) // 2, p) == p - 1
        inverse_three = pow(3, -1, p)
        tangent_scale = 4 * inverse_three % p
        assert 3 * tangent_scale % p == 4
        discriminant = 5
        assert pow(discriminant, (p - 1) // 2, p) == p - 1
        checks += 4

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in SUPPLIERS:
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (NODE, CONSUMER, "ev") in edges
    checks += 3

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in ("(BFN2)", "(BFN3)", "(BFN4)", "(BFN5)",
                   "D_0 in F_p[Z]", "does not exclude"):
        assert anchor in statement
        checks += 1

    print(f"L1_M4_H3_NU2_BASE_FIELD_NORMALIZATION_PASS checks={checks}")


if __name__ == "__main__":
    main()
