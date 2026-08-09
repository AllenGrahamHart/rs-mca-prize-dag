#!/usr/bin/env python3
"""Verify complete exclusion of all 105 cell-5 labels."""

import importlib.util
import json
from pathlib import Path

NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
ACTIVE = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell5_active_labels_complete_exclusion"
)
ENDPOINT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell5_endpoint_roles_complete_exclusion"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_module(identifier):
    path = ROOT / "background/nodes" / identifier / "verify.py"
    spec = importlib.util.spec_from_file_location(identifier, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_statuses():
    statuses = {}
    for identifier in (ACTIVE, ENDPOINT):
        payload = json.loads(
            (ROOT / "background/nodes" / identifier / "node.json").read_text()
        )
        require(payload["node"]["id"] == identifier, "dependency identity")
        statuses[identifier] = payload["node"]["status"]
    return statuses


def validate(statuses, active_labels, endpoint_labels):
    require(
        statuses == {ACTIVE: "PROVED", ENDPOINT: "PROVED"},
        "proved dependency cover",
    )
    require(
        active_labels == {(xi, pairing) for xi in range(5) for pairing in range(15)}
        and len(active_labels) == 75,
        "active-label cover",
    )
    require(
        endpoint_labels
        == {(xi, pairing) for xi in (5, 6) for pairing in range(15)}
        and len(endpoint_labels) == 30,
        "endpoint-label cover",
    )
    require(not active_labels & endpoint_labels, "disjoint child cover")
    complete = active_labels | endpoint_labels
    require(
        complete == {(xi, pairing) for xi in range(7) for pairing in range(15)}
        and len(complete) == 105,
        "complete raw-label cover",
    )
    return len(complete)


def main():
    manifest = json.loads((NODE / "node.json").read_text())
    require(
        manifest["node"]["id"] == NODE.name
        and manifest["node"]["status"] == "PROVED"
        and {row["from"] for row in manifest["requires"]} == {ACTIVE, ENDPOINT},
        "node manifest",
    )
    active = load_module(ACTIVE)
    active.validate(active.OWNERS, active.load_statuses())
    endpoint = load_module(ENDPOINT)
    endpoint.validate(
        endpoint.load("pilot"), endpoint.load("replay"), endpoint.load("root"),
        json.loads(endpoint.KERNEL.read_text()),
    )
    active_labels = {
        label for orbit in active.compile_active_orbits() for label in orbit
    }
    endpoint_labels = {(xi, pairing) for xi in (5, 6) for pairing in range(15)}
    total = validate(load_statuses(), active_labels, endpoint_labels)
    print(f"PASS cell-5 complete exclusion: labels=75+30={total}")


if __name__ == "__main__":
    main()
