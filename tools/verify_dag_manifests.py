#!/usr/bin/env python3
"""Fail closed when node manifests and generated dag.json diverge."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from dag_manifest import (
    DAG,
    ROOT,
    ManifestError,
    canonical_dag_text,
    manifest_paths,
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n")


def mutation_tests():
    with tempfile.TemporaryDirectory() as raw:
        root = Path(raw)
        write_json(root / "graph/dag_meta.json", {
            "schema": "prize-dag-meta-v1",
            "dag": {
                "schema": "fixture",
                "description": "fixture",
                "root": "b",
            },
        })
        base = {
            "schema": "prize-dag-node-v1",
            "node": {"id": "a", "status": "PROVED"},
            "requires": [],
            "alternatives": [],
            "evidence_for": [],
            "refutes": [],
        }
        write_json(root / "background/nodes/a/node.json", base)
        consumer = json.loads(json.dumps(base))
        consumer["node"] = {"id": "b", "status": "PROVED"}
        consumer["requires"] = [{"from": "a"}]
        consumer_path = root / "background/nodes/b/node.json"
        write_json(consumer_path, consumer)
        baseline = canonical_dag_text(root)
        require(len(json.loads(baseline)["edges"]) == 1, "fixture edge")

        caught = 0
        missing = json.loads(json.dumps(consumer))
        missing["requires"][0]["from"] = "ghost"
        write_json(consumer_path, missing)
        try:
            canonical_dag_text(root)
        except ManifestError:
            caught += 1
        write_json(consumer_path, consumer)

        duplicate_order = json.loads(json.dumps(consumer))
        duplicate_order["order"] = 0
        first_path = root / "background/nodes/a/node.json"
        first = json.loads(first_path.read_text())
        first["order"] = 0
        write_json(first_path, first)
        write_json(consumer_path, duplicate_order)
        try:
            canonical_dag_text(root)
        except ManifestError:
            caught += 1
        first.pop("order")
        write_json(first_path, first)
        write_json(consumer_path, consumer)

        generated = root / "dag.json"
        generated.write_text(baseline)
        generated.write_text(
            baseline.replace('"status": "PROVED"', '"status": "TARGET"', 1)
        )
        caught += generated.read_text() != canonical_dag_text(root)
        require(caught == 3, f"manifest mutations caught {caught}/3")
    return caught


def main():
    try:
        expected = canonical_dag_text(ROOT)
    except (ManifestError, ValueError) as error:
        raise RuntimeError(f"manifest compilation: {error}") from error
    require(DAG.is_file() and DAG.read_text() == expected,
            "dag.json is not the exact compiled manifest view")
    dag = json.loads(expected)
    paths = manifest_paths(ROOT)
    require(len(paths) == len(dag["nodes"]), "one manifest per DAG node")
    manifest_ids = {
        json.loads(path.read_text())["node"]["id"] for path in paths
    }
    require(manifest_ids == {node["id"] for node in dag["nodes"]},
            "manifest node cover")
    require(all(path.parent.name in manifest_ids for path in paths),
            "folder ownership")
    caught = mutation_tests()
    print(
        f"DAG_MANIFEST_PASS nodes={len(paths)} edges={len(dag['edges'])} "
        f"bytes={len(expected.encode())} mutations={caught}/3"
    )


if __name__ == "__main__":
    main()
