#!/usr/bin/env python3
"""One-time migration from monolithic dag.json to local node manifests."""

from __future__ import annotations

import argparse
import json

from dag_manifest import (
    META_SCHEMA,
    NODE_SCHEMA,
    ROOT,
    canonical_dag_text,
)


def critical_ids(dag):
    nodes = {node["id"]: node for node in dag["nodes"]}
    reverse = {}
    for edge in dag["edges"]:
        if edge["kind"] == "req":
            reverse.setdefault(edge["to"], []).append(edge["from"])
    critical = {value for value in ("mca_grand", "list_grand")
                if value in nodes}
    stack = list(critical)
    while stack:
        value = stack.pop()
        for parent in reverse.get(value, []):
            if parent not in critical:
                critical.add(parent)
                stack.append(parent)
    changed = True
    while changed:
        changed = False
        for edge in dag["edges"]:
            if (
                edge["kind"] == "alt"
                and edge["to"] in critical
                and edge["from"] not in critical
                and nodes[edge["from"]]["status"] in ("PROVED", "PROVABLE")
                and nodes[edge["to"]].get("gate") == "any"
            ):
                critical.add(edge["from"])
                stack = [edge["from"]]
                changed = True
                while stack:
                    value = stack.pop()
                    for parent in reverse.get(value, []):
                        if parent not in critical:
                            critical.add(parent)
                            stack.append(parent)
    return critical


def owner_directory(node_id, critical):
    candidates = (
        ROOT / "critical" / "nodes" / node_id,
        ROOT / "background" / "nodes" / node_id,
    )
    existing = [path for path in candidates if path.is_dir()]
    if len(existing) > 1:
        raise RuntimeError(f"duplicate node folders for {node_id}")
    if existing:
        return existing[0]
    tree = "critical" if node_id in critical else "background"
    return ROOT / tree / "nodes" / node_id


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    dag_path = ROOT / "dag.json"
    dag = json.loads(dag_path.read_text())
    critical = critical_ids(dag)
    manifests = {}
    for order, node in enumerate(dag["nodes"]):
        folder = owner_directory(node["id"], critical)
        manifests[node["id"]] = {
            "path": folder / "node.json",
            "payload": {
                "schema": NODE_SCHEMA,
                "order": order,
                "node": node,
                "requires": [],
                "alternatives": [],
                "evidence_for": [],
                "refutes": [],
            },
        }
    section_for_kind = {
        "req": ("requires", "from", "to"),
        "alt": ("alternatives", "from", "to"),
        "ev": ("evidence_for", "to", "from"),
        "ref": ("refutes", "to", "from"),
    }
    for order, edge in enumerate(dag["edges"]):
        section, endpoint, owner = section_for_kind[edge["kind"]]
        owner_id = edge[owner]
        row = {
            endpoint: edge[endpoint],
            "order": order,
        }
        if list(edge) != ["from", "to", "kind"]:
            row["key_order"] = list(edge)
        manifests[owner_id]["payload"][section].append(row)

    existing = [str(value["path"].relative_to(ROOT))
                for value in manifests.values() if value["path"].exists()]
    if existing:
        raise RuntimeError(
            f"refusing to overwrite {len(existing)} manifests; first={existing[0]}"
        )
    if not args.apply:
        print(
            f"DAG_MANIFEST_MIGRATION_READY nodes={len(manifests)} "
            f"critical={len(critical)} edges={len(dag['edges'])}"
        )
        return 0

    meta = {
        "schema": META_SCHEMA,
        "dag": {
            "schema": dag["schema"],
            "description": dag["description"],
            "root": dag["root"],
        },
    }
    meta_path = ROOT / "graph" / "dag_meta.json"
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=True) + "\n")
    for value in manifests.values():
        path = value["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(value["payload"], indent=2, ensure_ascii=True) + "\n"
        )
    expected = canonical_dag_text(ROOT)
    if expected != dag_path.read_text():
        raise RuntimeError("compiled DAG differs from migration source")
    print(
        f"DAG_MANIFEST_MIGRATION_PASS nodes={len(manifests)} "
        f"critical={len(critical)} edges={len(dag['edges'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
