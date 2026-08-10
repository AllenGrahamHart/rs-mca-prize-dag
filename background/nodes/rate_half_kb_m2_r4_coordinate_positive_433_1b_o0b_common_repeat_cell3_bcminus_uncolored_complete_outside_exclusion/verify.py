#!/usr/bin/env python3
"""Verify the complete cell-3 BC- uncolored outside exclusion."""

from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
E = ROOT / "experiments/prize_resolution"
PREFIX = "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcminus_"
MASTER = E / f"{PREFIX}uncolored_exceptional_fibers_result.json"
MASTER_SHA256 = "f88db7c36a247f02c14689e9b6db755b345f3c9a6712cea229c22068280ce096"
RECORDS = {
    "DE+": (
        "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcminus_uncolored_de_residual_pairing_exclusion",
        "fcb5c90cc87762372691368921863e6db04d58205d67e53e8317e96e4d8aa0fd",
        640, 512,
    ),
    "DF+": (
        "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcminus_uncolored_df_residual_pairing_exclusion",
        "921f8a76d5b426617e6a6d437bd14e26092f29dd902eb6c5f6502b21c3707315",
        864, 1408,
    ),
    "EF": (
        "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcminus_uncolored_ef_residual_pairing_exclusion",
        "519418c3a1fc95f78ec58005481c49769ae14d5119e8bc45eb01f0db3f2919c1",
        832, 1152,
    ),
}
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def import_verifier(node_id):
    path = ROOT / "background/nodes" / node_id / "verify.py"
    spec = importlib.util.spec_from_file_location(node_id+"_verify", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_master(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-cell3-bcminus-uncolored-exceptional-v1",
            "schema")
    require(payload["case_count"] == 360 and
            payload["status_counts"] == {"COMPLETE": 360}, "cases")
    require(payload["survivor_count"] == payload["unresolved_count"] == 0,
            "closure summary")
    require(len(payload["rows"]) == 360, "row coverage")
    require(Counter(row["missing_record"] for row in payload["rows"]) ==
            Counter({"DE+": 120, "DF+": 120, "EF": 120}), "records")
    require(sum(row["fiber_count"] for row in payload["rows"]) == 2336,
            "fiber total")
    require(sum(row["endpoint_root_count"] for row in payload["rows"]) == 3072,
            "endpoint total")
    require(sum(row["residual_root_count"] for row in payload["rows"]) == 0,
            "residual roots")
    for record, (_, digest, fibers, _) in RECORDS.items():
        shard = payload["shards"][record]
        require(shard["sha256"] == digest and shard["case_count"] == 120
                and shard["fiber_count"] == fibers, f"{record} shard")


def main():
    require(hashlib.sha256(MASTER.read_bytes()).hexdigest() == MASTER_SHA256,
            "master custody")
    master = json.loads(MASTER.read_text())
    validate_master(master)
    parents = set()
    for record, (node_id, digest, _, endpoints) in RECORDS.items():
        verifier = import_verifier(node_id)
        summary = verifier.validate(*verifier.load_payloads())
        require(summary["cases"] == 120 and
                summary["endpoint_rows"] == endpoints, f"{record} replay")
        require(hashlib.sha256(verifier.RESULT.read_bytes()).hexdigest() == digest,
                f"{record} custody")
        parents.add(node_id)
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG status")
    require(all(nodes[parent]["status"] == "PROVED"
                and (parent, NODE.name, "req") in edges
                for parent in parents), "parents")
    require((NODE.name, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_BCMINUS_UNCOLORED_COMPLETE_VERIFY_PASS representatives=360 fibers=2336 endpoints=3072 labels=600")


if __name__ == "__main__":
    main()
