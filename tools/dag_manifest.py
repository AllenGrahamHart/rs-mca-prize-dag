#!/usr/bin/env python3
"""Compile the prize DAG from node-local manifests."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
META = ROOT / "graph" / "dag_meta.json"
DAG = ROOT / "dag.json"
NODE_SCHEMA = "prize-dag-node-v1"
META_SCHEMA = "prize-dag-meta-v1"
NODE_TREES = ("critical", "background")
EDGE_SECTIONS = {
    "requires": ("req", "incoming"),
    "alternatives": ("alt", "incoming"),
    "evidence_for": ("ev", "outgoing"),
    "refutes": ("ref", "outgoing"),
}


class ManifestError(RuntimeError):
    """Raised when local graph manifests are incomplete or inconsistent."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ManifestError(message)


def manifest_paths(root: Path = ROOT) -> list[Path]:
    paths: list[Path] = []
    for tree in NODE_TREES:
        base = root / tree / "nodes"
        if base.is_dir():
            paths.extend(base.glob("*/node.json"))
    return sorted(paths)


def _order_key(
    order: int | None,
    fallback: tuple[str, ...],
) -> tuple[int, int, tuple[str, ...]]:
    return (order is None, order if order is not None else 0, fallback)


def _load_meta(root: Path) -> dict[str, Any]:
    path = root / META.relative_to(ROOT)
    _require(path.is_file(), f"missing graph metadata: {path}")
    payload = json.loads(path.read_text())
    _require(payload.get("schema") == META_SCHEMA, "graph metadata schema")
    dag = payload.get("dag")
    _require(isinstance(dag, dict), "graph metadata dag object")
    _require(list(dag) == ["schema", "description", "root"],
             "graph metadata key order")
    return dag


def _entry_order(entry: dict[str, Any], label: str) -> int | None:
    order = entry.get("order")
    _require(order is None or (
        isinstance(order, int) and not isinstance(order, bool) and order >= 0
    ), f"{label}: invalid order")
    return order


def load_manifest_graph(root: Path = ROOT) -> dict[str, Any]:
    """Load and validate all node manifests, returning the compiled DAG."""
    nodes: list[tuple[int | None, dict[str, Any], Path]] = []
    edges: list[tuple[int | None, dict[str, str], Path]] = []
    node_ids: set[str] = set()
    explicit_node_orders: set[int] = set()
    explicit_edge_orders: set[int] = set()

    for path in manifest_paths(root):
        payload = json.loads(path.read_text())
        rel = path.relative_to(root)
        _require(payload.get("schema") == NODE_SCHEMA,
                 f"{rel}: node manifest schema")
        node = payload.get("node")
        _require(isinstance(node, dict) and isinstance(node.get("id"), str),
                 f"{rel}: node object")
        node_id = node["id"]
        _require(path.parent.name == node_id,
                 f"{rel}: folder/id mismatch {node_id}")
        _require(node_id not in node_ids, f"duplicate manifest id {node_id}")
        node_ids.add(node_id)
        order = _entry_order(payload, str(rel))
        if order is not None:
            _require(order not in explicit_node_orders,
                     f"duplicate node order {order}")
            explicit_node_orders.add(order)
        nodes.append((order, node, path))

        allowed = {"schema", "order", "node", *EDGE_SECTIONS}
        extra = set(payload) - allowed
        _require(not extra, f"{rel}: unexpected keys {sorted(extra)}")
        for section, (kind, direction) in EDGE_SECTIONS.items():
            rows = payload.get(section, [])
            _require(isinstance(rows, list), f"{rel}: {section} is not a list")
            endpoint_key = "from" if direction == "incoming" else "to"
            for index, row in enumerate(rows):
                label = f"{rel}:{section}[{index}]"
                _require(isinstance(row, dict), f"{label}: object required")
                _require(set(row) <= {endpoint_key, "order", "key_order"} and
                         isinstance(row.get(endpoint_key), str),
                         f"{label}: malformed endpoint")
                edge_order = _entry_order(row, label)
                if edge_order is not None:
                    _require(edge_order not in explicit_edge_orders,
                             f"duplicate edge order {edge_order}")
                    explicit_edge_orders.add(edge_order)
                if direction == "incoming":
                    raw_edge = {
                        "from": row[endpoint_key],
                        "to": node_id,
                        "kind": kind,
                    }
                else:
                    raw_edge = {
                        "from": node_id,
                        "to": row[endpoint_key],
                        "kind": kind,
                    }
                key_order = row.get("key_order", ["from", "to", "kind"])
                _require(
                    isinstance(key_order, list)
                    and len(key_order) == 3
                    and set(key_order) == {"from", "to", "kind"},
                    f"{label}: invalid key_order",
                )
                edge = {key: raw_edge[key] for key in key_order}
                edges.append((edge_order, edge, path))

    _require(nodes, "no node manifests found")
    nodes.sort(key=lambda item: _order_key(
        item[0], (item[1]["id"],)
    ))
    edges.sort(key=lambda item: _order_key(
        item[0], (item[1]["from"], item[1]["to"], item[1]["kind"])
    ))
    ordered_nodes = [item[1] for item in nodes]
    ordered_edges = [item[1] for item in edges]
    compiled_ids = {node["id"] for node in ordered_nodes}
    for edge in ordered_edges:
        _require(edge["from"] in compiled_ids and edge["to"] in compiled_ids,
                 f"edge endpoint missing: {edge}")

    dag = dict(_load_meta(root))
    dag["nodes"] = ordered_nodes
    dag["edges"] = ordered_edges
    return dag


def canonical_dag_text(root: Path = ROOT) -> str:
    return json.dumps(
        load_manifest_graph(root), indent=1, ensure_ascii=True
    ) + "\n"


def write_compiled_dag(root: Path = ROOT) -> Path:
    path = root / DAG.relative_to(ROOT)
    payload = canonical_dag_text(root)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(payload)
    os.replace(temporary, path)
    return path


def manifest_index(root: Path = ROOT) -> dict[str, Path]:
    output: dict[str, Path] = {}
    for path in manifest_paths(root):
        payload = json.loads(path.read_text())
        node_id = payload.get("node", {}).get("id")
        _require(isinstance(node_id, str), f"{path}: missing node id")
        _require(node_id not in output, f"duplicate manifest id {node_id}")
        output[node_id] = path
    return output


def update_node_objects(
    nodes: Iterable[dict[str, Any]],
    root: Path = ROOT,
) -> None:
    """Replace node objects while retaining local edge ownership metadata."""
    index = manifest_index(root)
    for node in nodes:
        node_id = node["id"]
        _require(node_id in index, f"no manifest for node {node_id}")
        path = index[node_id]
        payload = json.loads(path.read_text())
        payload["node"] = node
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n")
