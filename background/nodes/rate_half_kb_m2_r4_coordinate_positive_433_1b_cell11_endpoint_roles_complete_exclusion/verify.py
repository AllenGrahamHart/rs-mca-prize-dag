#!/usr/bin/env python3
"""Verify complete exclusion of the two cell-11 endpoint roles."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
PRIME = 2130706433
FILES = {
    "pilot_script": EXP / "rate_half_kb_positive_433_1b_cell11_endpoint_compatibility_pilot_modal.py",
    "pilot": EXP / "rate_half_kb_positive_433_1b_cell11_endpoint_compatibility_pilot_result.json",
    "replay_script": EXP / "rate_half_kb_positive_433_1b_cell11_endpoint_compatibility_replay_modal.py",
    "replay": EXP / "rate_half_kb_positive_433_1b_cell11_endpoint_compatibility_replay_result.json",
    "root_script": EXP / "rate_half_kb_positive_433_1b_cell11_endpoint_eliminant_frobenius_roots_modal.py",
    "root": EXP / "rate_half_kb_positive_433_1b_cell11_endpoint_eliminant_frobenius_roots_result.json",
}
PINNED = {
    "pilot_script": "c1a1389c3b02b964ebff3b5b7c482b69e4e167aa45c0b37d61d84014cf5f4287",
    "pilot": "878c5e1eaacba6b646c9f01208e89ac1780b73f1bd20508f8a966c4c1c0c6467",
    "replay_script": "b6515eb36e50370bc1007baeb95c2e378bc4ce673f85b2361bfd4d2bbb613583",
    "replay": "46868d3f0a964d0a7b5e487da9385b181dd57bc1109c2974fba1e012c02cc746",
    "root_script": "8a6fa3415b815feea1ae4815eb265e0414758f088855793023718e38e114b4f7",
    "root": "635a0f6e507fa18ddb9c7e7fb6ea9e893a4c696bc2fb7730e79a2844e71746dd",
}
STRUCTURE = EXP / "rate_half_kb_positive_433_1b_cell11_complete_pivot_scout_result.json"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell11_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
SIGNS = tuple(itertools.product((-1, 1), repeat=2))
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell11_quadratic_four_basis_common_locus",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell11_global_common_kernel",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_universal_generic_outside_label_orbit_quotient",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name):
    return json.loads(FILES[name].read_text())


def validate(pilot, replay, root, kernel):
    expected = {(sign, endpoint) for sign in SIGNS for endpoint in ("b", "c")}
    require(
        pilot["schema"] == "rate-half-kb-positive-433-1b-cell11-endpoint-pilot-v1"
        and pilot["field"] == PRIME
        and pilot["source_structure_sha256"] == digest(STRUCTURE)
        and pilot["source_kernel_sha256"] == digest(KERNEL),
        "pilot custody",
    )
    pilot_rows = {}
    for row in pilot["rows"]:
        key = (tuple(row["epsilon"]), row["endpoint"])
        require(key in expected and key not in pilot_rows, "pilot coverage")
        terms = 1487 if row["endpoint"] == "b" else 1479
        require(
            row["status"] == "COMPLETE"
            and row["dimension"] == 0
            and row["basis_size"] == 41
            and not row["unit"]
            and row["r_elimination_dimension"] == 4
            and row["r_elimination_size"] == 1
            and row["cut_degree"] == 36
            and row["cut_terms"] == terms,
            "pilot exact result",
        )
        pilot_rows[key] = row
    require(set(pilot_rows) == expected, "pilot Cartesian cover")

    require(
        replay["schema"] == "rate-half-kb-positive-433-1b-cell11-endpoint-replay-v1"
        and replay["field"] == PRIME
        and replay["source_pilot_sha256"] == digest(FILES["pilot"])
        and replay["source_tower_sha256"] == digest(TOWER)
        and replay["source_kernel_sha256"] == digest(KERNEL),
        "replay custody",
    )
    replay_rows = {}
    for row in replay["rows"]:
        key = (tuple(row["epsilon"]), row["endpoint"])
        require(key in pilot_rows and key not in replay_rows, "replay coverage")
        require(
            row["status"] == "COMPLETE"
            and row["eliminant_degree"] == 32
            and row["r_root_count"] == 1
            and len(row["r_roots"]) == 1
            and row["lifted_point_count"] == 2
            and row["generic_point_count"] == 0
            and not row["generic_points"]
            and not row["route_boundary"]
            and not row["leading_boundary"]
            and len(row["no_lift"]) == 1
            and row["no_lift"][0]["stage"] == "NO_B",
            "replay complete incompatibility",
        )
        replay_rows[key] = row
    require(set(replay_rows) == expected, "replay Cartesian cover")

    require(
        root["schema"] == (
            "rate-half-kb-positive-433-1b-cell11-endpoint-"
            "eliminant-frobenius-roots-v1"
        )
        and root["field"] == PRIME
        and root["source_pilot_sha256"] == digest(FILES["pilot"])
        and root["complete"],
        "Frobenius custody",
    )
    root_rows = {}
    for row in root["rows"]:
        key = (tuple(row["epsilon"]), row["endpoint"])
        require(key in pilot_rows and key not in root_rows, "Frobenius coverage")
        require(
            row["degree"] == 32
            and row["eliminant_sha256"] == hashlib.sha256(
                pilot_rows[key]["r_elimination"].encode()
            ).hexdigest()
            and row["root_count"] == 1
            and len(row["root_gcd"]) == 2
            and row["roots"] == replay_rows[key]["r_roots"],
            "independent Frobenius roots",
        )
        root_rows[key] = row
    require(set(root_rows) == expected, "Frobenius Cartesian cover")

    kernel_signatures = {
        tuple(item["sha256"] for item in row["kernel"])
        for row in kernel["rows"]
    }
    require(
        {tuple(row["epsilon"]) for row in kernel["rows"]} == set(SIGNS)
        and len(kernel_signatures) == 1,
        "sign-independent common kernel",
    )
    return {"eliminants": 8, "roots": 8, "lifts": 16}


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE.name, "req") in edges, f"missing parent {parent}")
    require((NODE.name, "rate_half_band_closure", "ev") in edges,
            "DAG consumer")


def main():
    for name, expected in PINNED.items():
        require(digest(FILES[name]) == expected, f"hash drift: {name}")
    result = validate(
        load("pilot"), load("replay"), load("root"),
        json.loads(KERNEL.read_text()),
    )
    verify_dag()
    print(
        "PASS cell-11 endpoint roles: "
        f"eliminants={result['eliminants']} roots={result['roots']} "
        f"guarded_lifts={result['lifts']} compatible=0 labels=30"
    )


if __name__ == "__main__":
    main()
