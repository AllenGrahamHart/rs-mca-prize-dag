#!/usr/bin/env python3
"""Fail closed on the unsafe-at-crossing row-instantiation correction."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    dag = json.loads((ROOT / "dag.json").read_text(encoding="utf-8"))
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }

    payload = "unsafe_crossing_family_instantiation"
    crossing = "unsafe_at_crossing"
    identity = "identity_prefix_flexible_budget_unsafe_floor"
    deployed = "deployed_identity_prefix_owner_scope_audit"

    require(nodes[payload]["status"] == "TARGET", "row payload is not TARGET")
    require(nodes[crossing]["status"] == "CONDITIONAL", "crossing is false-green")
    require(nodes["mca_unsafe"]["status"] == "CONDITIONAL", "unsafe assembly drift")
    require(nodes[identity]["status"] == "PROVED", "identity supplier regressed")
    require(nodes[deployed]["status"] == "PROVED", "deployed audit regressed")

    payload_statement = nodes[payload]["statement"]
    for token in ("(Q)", "(V)", "(M)", "nu(A)", ">B*", "ambient MCA slope field"):
        require(token in payload_statement, f"payload contract lost {token}")
    require(">B*-1" not in payload_statement, "off-by-one occupancy premise returned")

    averaged = nodes["averaged_slope_conversion"]["statement"]
    require("B=B*+1" in averaged and "nu(A)>B*" in averaged,
            "strict unsafe occupancy specialization is missing")

    qfloor = nodes["qfloor_exact"]["statement"]
    for token in ("prime-field", "p>(2ell')^(N'/2)", "No below-threshold"):
        require(token in qfloor, f"qfloor scope lost {token}")

    crossing_req = {
        source for source, target, kind in edges
        if target == crossing and kind == "req"
    }
    require(
        crossing_req == {payload, "qfloor_exact", "averaged_slope_conversion"},
        f"crossing req parents drifted: {sorted(crossing_req)}",
    )
    require(
        not any(target == payload and kind == "req" for _, target, kind in edges),
        "unresolved payload gained req parents",
    )

    require(("zone_b", "mca_unsafe", "ev") in edges,
            "zone_b is not retained as route evidence")
    require(("zone_b", "mca_unsafe", "req") not in edges,
            "zone_b returned as a duplicated unsafe premise")
    require((payload, crossing, "req") in edges, "payload does not gate crossing")
    require((identity, payload, "ev") in edges,
            "identity-prefix theorem is not target evidence")
    require((deployed, payload, "ev") in edges,
            "deployed identity rows are not target evidence")

    mca_req = {
        source for source, target, kind in edges
        if target == "mca_unsafe" and kind == "req"
    }
    require(mca_req == {"cap_theorem", crossing},
            f"mca_unsafe req parents drifted: {sorted(mca_req)}")

    folder = ROOT / "critical" / "nodes" / payload
    for name in (
        "statement.md",
        "claim_contract.md",
        "attack.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
    ):
        require((folder / name).is_file(), f"payload packet missing {name}")
    require(not (ROOT / "critical/nodes/unsafe_at_crossing/proof.md").exists(),
            "stale auto-discharged crossing proof remains")
    require((ROOT / "notes/UNSAFE_AT_CROSSING_FALSE_GREEN_AUDIT_20260726.md").is_file(),
            "false-green audit is missing")

    identity_folder = ROOT / "background" / "nodes" / identity
    for name in (
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "source_pin.json",
        "verify.py",
    ):
        require((identity_folder / name).is_file(), f"identity packet missing {name}")
    identity_statement = (identity_folder / "statement.md").read_text()
    for token in ("binom(n,m) > |B|^w B*", "binom(B*+1,2) k < q-n", "B*+1"):
        require(token in identity_statement, f"identity theorem lost {token}")

    print(
        "UNSAFE_CROSSING_STATUS_REGRESSION_VERIFIED "
        f"payload={payload} crossing_req={len(crossing_req)}"
    )


if __name__ == "__main__":
    main()
