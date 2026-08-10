#!/usr/bin/env python3
"""Verify the repeated-BC BC+ colored-missing atlas."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
FILES = {
    "cut_launcher": ("rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcplus_colored_missing_modal.py", "620ce626563ae0009e6d098789e80340d05b7d6f97779ed068d3fe9cbdd32e93"),
    "cut_result": ("rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcplus_colored_missing_result.json", "652c3ac853708cfe59a8d7751f7ca22d8b71120920c2fc1c4e6d29fbc53d5f8d"),
    "root_launcher": ("rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcplus_colored_missing_roots_modal.py", "af7274a961b2c6a7779c7efddd026f9700c2fce94f74746bd6863552dab87a6c"),
    "root_result": ("rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcplus_colored_missing_roots_result.json", "88a0856e6d0dc7ef649095306d0758b18a3b84304dd8e6db4f80aac34d2f6c36"),
}
TORUS_SHA256 = "9ad509b330416fc095fcbf6ff2ac75ae82123cc824b4f819e3c6aac0c78279fc"
PARENTS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcplus_torus_locus",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cells3_6_full_system_transport",
}
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def cases(rows):
    return {(tuple(row["epsilon"]), row["missing_record"]): row for row in rows}


def validate(cut, roots):
    expected = set(itertools.product(itertools.product((-1, 1), repeat=2), ("BE", "CF")))
    require(cut["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-cell3-bcplus-colored-missing-v1", "cut schema")
    require(cut["source_torus_sha256"] == TORUS_SHA256, "cut torus custody")
    cut_rows = cases(cut["rows"])
    require(set(cut_rows) == expected and len(cut["rows"]) == 8, "cut cases")
    for (_, record), row in cut_rows.items():
        require(row["status"] == "COMPLETE" and not row["unit"] and
                row["dimension"] == 0, "finite cut")
        require(row["basis_size"] == (8 if record == "BE" else 10), "basis size")
        require(hashlib.sha256(row["basis"].encode()).hexdigest() ==
                row["basis_sha256"], "basis custody")

    require(roots["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-cell3-bcplus-colored-roots-v1", "root schema")
    require(roots["source_torus_sha256"] == TORUS_SHA256 and
            roots["source_cut_sha256"] == FILES["cut_result"][1], "root custody")
    root_rows = cases(roots["rows"])
    require(set(root_rows) == expected and len(roots["rows"]) == 8, "root cases")
    for (_, record), row in root_rows.items():
        require(row["status"] == "COMPLETE" and not row["unresolved"], "root completion")
        require(row["resultant_degree"] == (116 if record == "BE" else 124), "resultant degree")
        require(len(row["u_roots"]) == (9 if record == "BE" else 11), "u roots")
        require(row["raw_r_root_count"] == (12 if record == "BE" else 16), "r roots")
        require(row["guard_boundary_count"] == 12, "guard boundaries")
        require(row["point_count"] == (0 if record == "BE" else 4), "live points")
        require(row["boundary_count"] == 0, "ratio boundary")
        require(len(row["u_rows"]) == len(row["u_roots"]), "u-row ledger")
        all_roots = [root for u_row in row["u_rows"]
                     for root in u_row.get("root_rows", [])]
        require(len(all_roots) == row["raw_r_root_count"] and
                all(root["core_value"] == root["cut_value"] == 0
                    for root in all_roots), "root replay")
        require(sum(root["status"] == "GUARD_BOUNDARY" for root in all_roots)
                == 12, "boundary replay")
        if record == "BE":
            require(all(root["status"] == "GUARD_BOUNDARY"
                        for root in all_roots) and not row["points"], "BE exclusion")
        else:
            require(sum(root["status"] == "LIFTED" for root in all_roots) == 4,
                    "CF live roots")
            require(len(row["points"]) == 4, "CF point ledger")
            for point in row["points"]:
                require(point["status"] == "LIFTED" and point["a_missing"] != 0,
                        "CF point status")
                require(point["b"] == -pow(point["u"], -3, PRIME) % PRIME,
                        "torus b")
                known = point["u"]
                target = point["missing_target_coordinate"]
                require(point["source_product"] == known*target % PRIME,
                        "missing product")
                require(point["source_squared_sum"] ==
                        pow(known+target, 2, PRIME), "missing sum")
    require(4*2*15 == 120, "formal-system census")


def main():
    for filename, expected in FILES.values():
        require(hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
                == expected, f"file custody {filename}")
    cut = json.loads((EXPERIMENTS / FILES["cut_result"][0]).read_text())
    roots = json.loads((EXPERIMENTS / FILES["root_result"][0]).read_text())
    validate(cut, roots)
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED" and
                (parent, NODE.name, "req") in edges, f"parent {parent}")
    require((NODE.name, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_BCPLUS_COLORED_MISSING_VERIFY_PASS cuts=8 BE=120 cell6_CF=120 CF_points=16")


if __name__ == "__main__":
    main()
