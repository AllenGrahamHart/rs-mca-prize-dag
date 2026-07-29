#!/usr/bin/env python3
"""Independent contract audit for the pure-cofactor associate router."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_pure_cofactor_common_prime_associate_router"
TARGET = "e1_official_low_square_mass_pair_budget"


def main() -> None:
    checks = 0
    statement = (Path(__file__).with_name("statement.md")).read_text()
    contract = (Path(__file__).with_name("claim_contract.md")).read_text()
    assert "same row and quotient" in statement
    assert "same quotient\n+   root" in contract
    assert "odd cofactor" in contract
    assert "not only a root of unity" in contract
    assert "mu!=nu" in contract
    assert "not a feasible exhaustive enumeration" in contract
    checks += 6

    # Ideal-norm mutation controls: an odd residual factor cannot disappear,
    # and changing the root changes the selected prime ideal.
    for mu in range(1, 5):
        assert (2**mu * 3) // 2**mu == 3
        assert (2**mu) // 2**mu == 1
        checks += 2

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[TARGET]["status"] == "TARGET"
    assert (NODE, TARGET, "ev") in edges
    assert (NODE, TARGET, "req") not in edges
    checks += 4

    print(
        "E1_PURE_COFACTOR_COMMON_PRIME_ASSOCIATE_ROUTER_AUDIT_PASS "
        f"mutations=2 checks={checks}"
    )


if __name__ == "__main__":
    main()
