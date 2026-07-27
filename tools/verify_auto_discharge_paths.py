#!/usr/bin/env python3
"""Verify partition-aware auto-discharge artifacts and regression lookup."""

import json
import os
import tempfile

import auto_discharge


def main():
    with tempfile.TemporaryDirectory() as root:
        critical = os.path.join(root, "critical", "nodes", "c")
        background = os.path.join(root, "background", "nodes", "b")
        os.makedirs(critical)
        os.makedirs(background)
        checks = {
            "critical": (auto_discharge.node_folder("c", root), critical),
            "background": (auto_discharge.node_folder("b", root), background),
            "legacy": (
                auto_discharge.node_folder("legacy", root),
                os.path.join(root, "nodes", "legacy"),
            ),
        }
        bad_paths = [name for name, (actual, expected) in checks.items()
                     if actual != expected]
        if bad_paths:
            raise RuntimeError(f"partition lookup failed: {', '.join(bad_paths)}")

        # Put consumers before suppliers to ensure regression is a fixpoint,
        # not an accidental consequence of dag.json ordering.
        chain_nodes = {
            "top": {"id": "top", "status": "PROVED"},
            "middle": {"id": "middle", "status": "PROVED"},
            "leaf": {"id": "leaf", "status": "TARGET"},
        }
        for node_id in ("top", "middle"):
            folder = os.path.join(root, "critical", "nodes", node_id)
            os.makedirs(folder)
            with open(os.path.join(folder, "proof.md"), "w", encoding="utf-8") as handle:
                handle.write(f"# proof: {node_id} (auto-discharged)\n")
        regressed = auto_discharge.regress_to_fixpoint(
            chain_nodes,
            {"top": ["middle"], "middle": ["leaf"]},
            {},
            root,
        )
        if regressed != ["middle", "top"]:
            raise RuntimeError(f"non-fixpoint regression order: {regressed}")
        if any(chain_nodes[node_id]["status"] != "CONDITIONAL"
               for node_id in ("top", "middle")):
            raise RuntimeError("reversed-order chain retained a false green")

        gate_folder = os.path.join(root, "background", "nodes", "gate")
        os.makedirs(gate_folder)
        with open(os.path.join(gate_folder, "proof.md"), "w", encoding="utf-8") as handle:
            handle.write("# proof: gate (auto-discharged)\n")
        gate_nodes = {
            "gate": {"id": "gate", "status": "PROVED", "gate": "any"},
            "alternative": {"id": "alternative", "status": "TARGET"},
        }
        gate_regressed = auto_discharge.regress_to_fixpoint(
            gate_nodes, {}, {"gate": ["alternative"]}, root
        )
        if gate_regressed != ["gate"] or gate_nodes["gate"]["status"] != "CONDITIONAL":
            raise RuntimeError("gate:any retained a false green after its alternatives failed")

    with open(auto_discharge.DAG, encoding="utf-8") as handle:
        dag = json.load(handle)
    stale = []
    for node in dag["nodes"]:
        if node["status"] in auto_discharge.GREEN:
            continue
        folder = auto_discharge.node_folder(node["id"])
        for artifact in ("proof.md", "sketch.md"):
            path = os.path.join(folder, artifact)
            if not os.path.isfile(path):
                continue
            with open(path, encoding="utf-8") as handle:
                text = handle.read()
            if "(auto-discharged)" in text:
                stale.append(f"{node['id']}:{artifact}")
    if stale:
        raise RuntimeError(
            "non-green nodes retain auto-discharge artifacts: " + ", ".join(stale)
        )

    print("AUTO_DISCHARGE_PATHS_VERIFIED")


if __name__ == "__main__":
    main()
