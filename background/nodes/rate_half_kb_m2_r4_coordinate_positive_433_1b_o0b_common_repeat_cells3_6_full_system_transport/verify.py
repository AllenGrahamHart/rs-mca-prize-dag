#!/usr/bin/env python3
"""Verify repeated-BC cells 3/6 full-system transport."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
SCRIPT = ROOT / "experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_common_repeat_cells3_6_transport.py"
SCRIPT_HASH = "7560d2ba46fb43bf0879e48690d27e3586ed3a65835fae1e590835bcfd2bbbe5"
PARENTS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cells3_6_compact_locus",
}
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_transport():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_HASH,
            "script custody")
    spec = importlib.util.spec_from_file_location("cells3_6_transport", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate(transport):
    labels, systems = transport.validate()
    require(transport.common_cell_image(3) == 6 and
            transport.common_cell_image(6) == 3, "cell involution")
    require(len(labels) == 105 and len(systems) == 1680, "exact census")
    require(tuple(transport.OUTSIDE_RECORD_SWAP[index]
                  for index in transport.OUTSIDE_RECORD_SWAP) == tuple(range(7)),
            "record involution")


def main():
    transport = load_transport(); validate(transport)
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED" and
                (parent, NODE_ID, "req") in edges, f"parent {parent}")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELLS3_6_TRANSPORT_VERIFY_PASS labels=105 systems=1680")


if __name__ == "__main__":
    main()
