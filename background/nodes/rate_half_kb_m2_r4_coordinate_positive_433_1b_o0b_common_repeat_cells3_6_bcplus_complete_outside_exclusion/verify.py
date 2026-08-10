#!/usr/bin/env python3
"""Verify complete repeated-BC BC+ outside exclusion in cells 3 and 6."""

from collections import Counter
import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
E = ROOT / "experiments/prize_resolution"
PREFIX = "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcplus_"
LAUNCHER = E / f"{PREFIX}uncolored_exceptional_fibers_modal.py"
MASTER = E / f"{PREFIX}uncolored_exceptional_fibers_result.json"
SHARDS = {
    "DE+": E / f"{PREFIX}uncolored_exceptional_DEplus_result.json",
    "DF+": E / f"{PREFIX}uncolored_exceptional_DFplus_result.json",
    "EF": E / f"{PREFIX}uncolored_exceptional_EF_result.json",
}
LAUNCHER_SHA256 = "f6bb5864d7bc1c672cb4d61960d991478ef86952487d550f31d6db76198da86d"
MASTER_SHA256 = "43b8bff0fee4a24b7e44be47b9c7b22be91a75cf0a7ac4e08cf0a798e064f9ca"
SHARD_SHA256 = {
    "DE+": "99314fbf20e1c6935cea1ca0ca9e0fa4c142096b793a63b6f9594d40c673caaa",
    "DF+": "1cf9d55db8e263d3aa2ece86b72602fb50330d7894b4bd1b3b7d33c1c03f21ca",
    "EF": "2bf7ca06b66ec2bb825e6a149a20788174a16ef5f87ba6ff7f4d350ef060a7f1",
}
PARENTS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcplus_colored_missing_atlas",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcplus_cf_residual_pairing_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcplus_uncolored_de_residual_pairing_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcplus_uncolored_df_residual_pairing_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcplus_uncolored_ef_residual_pairing_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cells3_6_full_system_transport",
}
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def case_key(row):
    return (tuple(row["epsilon"]), row["missing_record"],
            row["sigma_o"], row["pairing_index"])


def digest_values(values):
    return hashlib.sha256(json.dumps(
        values, separators=(",", ":")
    ).encode()).hexdigest()


def compact(row):
    fibers = row["fibers"]
    endpoints = [endpoint for fiber in fibers
                 for endpoint in fiber.get("endpoint_rows", [])]
    return {
        "epsilon": row["epsilon"],
        "missing_record": row["missing_record"],
        "sigma_o": row["sigma_o"],
        "pairing_index": row["pairing_index"],
        "status": row["status"],
        "u_count": len(row["u_values"]),
        "u_sha256": digest_values(row["u_values"]),
        "fiber_count": row["fiber_count"],
        "fiber_status_counts": dict(sorted(Counter(
            fiber["status"] for fiber in fibers
        ).items())),
        "endpoint_status_counts": dict(sorted(Counter(
            endpoint["status"] for endpoint in endpoints
        ).items())),
        "endpoint_root_count": sum(
            len(fiber.get("endpoint_roots") or []) for fiber in fibers
        ),
        "residual_root_count": sum(
            len(endpoint.get("y_roots") or []) for endpoint in endpoints
        ),
        "survivor_count": row["survivor_count"],
        "unresolved_count": len(row["unresolved"]),
        "seconds": row["seconds"],
    }


def validate(master, shards):
    require(master["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-cell3-bcplus-uncolored-exceptional-v1",
            "master schema")
    require(master["case_count"] == 360
            and master["status_counts"] == {"COMPLETE": 360}
            and master["survivor_count"] == 0
            and master["unresolved_count"] == 0, "master status")
    detailed = {}
    total_fibers = 0
    for record, payload in shards.items():
        require(payload["missing_record"] == record
                and payload["case_count"] == 120
                and payload["status_counts"] == {"COMPLETE": 120}
                and payload["survivor_count"] == 0
                and payload["unresolved_count"] == 0, "shard status")
        metadata = master["shards"][record]
        require(metadata == {
            "file": SHARDS[record].name,
            "sha256": SHARD_SHA256[record],
            "case_count": 120,
            "fiber_count": payload["fiber_count"],
        }, "shard metadata")
        total_fibers += payload["fiber_count"]
        for row in payload["rows"]:
            key = case_key(row)
            require(key not in detailed, "duplicate detailed row")
            detailed[key] = compact(row)

    master_rows = {case_key(row): row for row in master["rows"]}
    require(len(detailed) == len(master_rows) == 360
            and detailed == master_rows, "compact master replay")
    require(total_fibers == 7000
            and sum(row["u_count"] for row in master_rows.values()) == 5840
            and sum(row["endpoint_root_count"]
                    for row in master_rows.values()) == 3520
            and sum(row["residual_root_count"]
                    for row in master_rows.values()) == 0,
            "global finite census")


def load_payloads():
    return (json.loads(MASTER.read_text()), {
        record: json.loads(path.read_text()) for record, path in SHARDS.items()
    })


def main():
    require(hashlib.sha256(LAUNCHER.read_bytes()).hexdigest() ==
            LAUNCHER_SHA256, "launcher custody")
    require(hashlib.sha256(MASTER.read_bytes()).hexdigest() ==
            MASTER_SHA256, "master custody")
    for record, path in SHARDS.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() ==
                SHARD_SHA256[record], f"{record} shard custody")
    validate(*load_payloads())
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG status")
    require(all(nodes[parent]["status"] == "PROVED"
                and (parent, NODE.name, "req") in edges
                for parent in PARENTS), "parents")
    require((NODE.name, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_BCPLUS_COMPLETE_OUTSIDE_VERIFY_PASS cell3=840 cell6=840 representative_cases=360 exceptional_fibers=7000")


if __name__ == "__main__":
    main()
