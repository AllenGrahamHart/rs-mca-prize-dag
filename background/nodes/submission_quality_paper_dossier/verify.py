#!/usr/bin/env python3
"""Fail-closed scope and wiring check for the final submission artifact."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "submission_quality_paper_dossier"


def packet_check():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}

    assert nodes[NODE]["status"] == "TARGET"
    assert nodes[NODE]["closure"] == "artifact"
    assert nodes["packaging"]["status"] == "CONDITIONAL"
    assert ("mca_grand", NODE, "req") in edges
    assert ("list_grand", NODE, "req") in edges
    assert (NODE, "packaging", "req") in edges

    incoming = {source for source, target, kind in edges
                if target == "packaging" and kind == "req"}
    assert incoming == {
        "compiler", "harness", "dossier_partial", "bridge_ledger", NODE
    }


def scope_check():
    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    acceptance = (ROOT / "background" / "nodes" / NODE / "acceptance.md").read_text()
    partial = (ROOT / "notes" / "dossier" / "PARTIAL_DOSSIER.md").read_text()
    packaging = (ROOT / "background" / "nodes" / "packaging" /
                 "conditional.md").read_text()

    for token in (
        "every admissible smooth Reed--Solomon row",
        "all four official rates",
        "full required constant-arity scope",
        "open_required_claims",
        "required_scope_nonclaims",
        "clean-checkout replay",
        "upstream-facing packets",
    ):
        assert token in statement + acceptance, token
    assert "This is not a full prize resolution" in partial
    assert NODE in packaging


def main():
    packet_check()
    scope_check()
    print(
        "SUBMISSION_QUALITY_PAPER_DOSSIER_SCOPE_PASS "
        "grand_reqs=2 packaging_reqs=5 scope_axes=7"
    )


if __name__ == "__main__":
    main()
