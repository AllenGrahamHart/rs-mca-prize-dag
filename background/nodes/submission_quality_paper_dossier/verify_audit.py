#!/usr/bin/env python3
"""Mutation audit for final submission artifact wiring."""

import json
from pathlib import Path

import verify


ROOT = Path(__file__).resolve().parents[3]
NODE = verify.NODE


def valid_wiring(dag):
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    required = {
        ("mca_grand", NODE, "req"),
        ("list_grand", NODE, "req"),
        (NODE, "packaging", "req"),
    }
    return (
        nodes.get(NODE, {}).get("status") == "TARGET"
        and nodes.get(NODE, {}).get("closure") == "artifact"
        and required <= edges
    )


def main():
    verify.packet_check()
    verify.scope_check()
    dag = json.loads((ROOT / "dag.json").read_text())
    assert valid_wiring(dag)

    caught = 0
    for edge in (
        ("mca_grand", NODE, "req"),
        ("list_grand", NODE, "req"),
        (NODE, "packaging", "req"),
    ):
        mutation = json.loads(json.dumps(dag))
        mutation["edges"] = [item for item in mutation["edges"]
                             if (item["from"], item["to"], item["kind"]) != edge]
        caught += not valid_wiring(mutation)
    assert caught == 3

    mutation = json.loads(json.dumps(dag))
    for node in mutation["nodes"]:
        if node["id"] == NODE:
            node["status"] = "PROVED"
    assert not valid_wiring(mutation)

    print(
        "SUBMISSION_QUALITY_PAPER_DOSSIER_AUDIT_PASS "
        "edge_mutations=3 status_mutations=1"
    )


if __name__ == "__main__":
    main()
