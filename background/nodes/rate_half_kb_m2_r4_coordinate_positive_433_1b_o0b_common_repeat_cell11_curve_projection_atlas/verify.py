#!/usr/bin/env python3
"""Verify the repeated-BC cell-11 target-curve projection atlas."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
PREFIX = "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_"
FILES = {
    "input_launcher": (PREFIX + "principal_input_modal.py", "209bee5314d35ed807015c4749da27e974cdf099e12ba14f41b5bd72dd73ad59"),
    "input_result": (PREFIX + "principal_input_result.json", "a9c3f10fc7e368f88599bce085598d641d0a73352a1f7d54e06abcd9b4aabbf7"),
    "projection_launcher": (PREFIX + "principal_projection_modal.py", "5ca01ab995b91a87e90b9fb3373537d1373797ec1b7f67e583b2b2c425adb994"),
    "projection_result": (PREFIX + "principal_projection_result.json", "83a160c52d59a1d1bb5171db264fc33e09080ff727614aef8d9ae3b3ef8c0a51"),
    "geometry_launcher": (PREFIX + "curve_geometry_modal.py", "8028f07bf8ae02334ae87d5307250c0528c921a0f50b3656e079a4baef70fad7"),
    "geometry_result": (PREFIX + "curve_geometry_result.json", "3ce4c9de7d6266f115eb8ce35afe1ef7cd6740de725ff1fea7324b8139c8df01"),
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_vieta_minor_atlas",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_saturation_classification",
)
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
PLANE = {
    -1: "c5b3+c3b5-c5b2+3c4b3+3c3b4-c2b5-5c4b2+8c3b3-5c2b4-2c4b-2c3b2-2c2b3-2cb4-5c3b+8c2b2-5cb3-c3+3c2b+3cb2-b3+c2+b2",
    1: "c4b2+c2b4-2c3b-8c2b2-2cb3+c2+b2",
}
SYMMETRIC = {
    -1: "-2*x**4 + x**3*y**2 + 6*x**3*y + 18*x**3 - x**2*y**3 - 5*x**2*y**2 + 4*x**2*y + 18*x**2 - 2*x*y**3 - 5*x*y**2 + 6*x*y - 2*x - y**3 + y**2",
    1: "-2*x**3 + x**2*y**2 - 4*x**2 - 2*x*y**2 - 2*x + y**2",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load(name):
    return json.loads((EXPERIMENTS / FILES[name][0]).read_text())


def validate_input(payload):
    require(payload["schema"] == "rate-half-kb-positive-433-1b-o0b-common-repeat-cell11-principal-input-v1", "input schema")
    require(payload["status_counts"] == {"COMPLETE": 10}, "input completion")
    expected = set(itertools.product((-1, 1), (-1, 1), (-1, 1)))
    actual = set()
    for row in payload["common_rows"]:
        key = (*row["epsilon"], row["bc_sign"])
        require(key in expected and key not in actual, "input row")
        actual.add(key)
        require(row["status"] == "COMPLETE" and len(row["equations"]) == 6, "input equations")
        require(len(row["equation_sha256"]) == 6 and len(row["guard_sha256"]) == 64, "input digests")
    require(actual == expected and len(payload["product_rows"]) == 2, "input coverage")
    require({row["bc_sign"] for row in payload["product_rows"]} == {-1, 1}, "product signs")
    for row in payload["product_rows"]:
        require(row["status"] == "COMPLETE" and row["rank_minor_column"] == 4 and row["rank_minor_degree"] == 7 and row["rank_minor_terms"] == 20, "product cofactor")


def validate_projection(payload):
    require(payload["schema"] == "rate-half-kb-positive-433-1b-o0b-common-repeat-cell11-principal-projection-v1", "projection schema")
    require(payload["source_sha256"] == FILES["input_result"][1], "projection source")
    require(payload["status_counts"] == {"COMPLETE": 8} and payload["case_count"] == 8, "projection completion")
    expected = set(itertools.product((-1, 1), (-1, 1), (-1, 1)))
    actual = set()
    for row in payload["rows"]:
        key = (*row["epsilon"], row["bc_sign"])
        require(key in expected and key not in actual, "projection row")
        actual.add(key)
        sign = row["bc_sign"]
        require(row["status"] == "COMPLETE" and row["full_dimension"] == 1, "common dimension")
        require(row["full_size"] == (21 if sign == -1 else 17), "full basis size")
        require(row["elimination_size"] == 1 and not row["product_rank_saturated"], "elimination contract")
        require(row["elimination_output"].splitlines()[-1] == PLANE[sign], "plane equation")
    require(actual == expected, "projection coverage")


def validate_geometry(payload):
    require(payload["schema"] == "rate-half-kb-positive-433-1b-o0b-common-repeat-cell11-curve-geometry-v1", "geometry schema")
    require(payload["source_sha256"] == FILES["input_result"][1] and payload["projection_sha256"] == FILES["projection_result"][1], "geometry sources")
    require(payload["status_counts"] == {"COMPLETE": 2}, "geometry completion")
    rows = {row["bc_sign"]: row for row in payload["rows"]}
    require(set(rows) == {-1, 1}, "geometry signs")
    for sign, row in rows.items():
        require(row["status"] == "COMPLETE" and not row["stderr"], "geometry row")
        require(row["full_basis_size"] == (21 if sign == -1 else 17), "geometry full size")
        require(row["basis_sizes"] == {"source_r": 6 if sign == -1 else 5, "source_t": 7}, "staged basis sizes")
        require(row["plane_total_degree"] == (8 if sign == -1 else 6), "plane degree")
        require(row["symmetric_xy"] == SYMMETRIC[sign], "symmetric equation")
        require(row["factor_unit"] == 1 and len(row["factors_over_q"]) == 1 and row["factors_over_q"][0]["multiplicity"] == 1, "rational factorization")
    require(SYMMETRIC[1] == "-2*x**3 + x**2*y**2 - 4*x**2 - 2*x*y**2 - 2*x + y**2", "BC+ compact identity")


def main():
    for filename, digest in FILES.values():
        require(hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest() == digest, f"file custody {filename}")
    validate_input(load("input_result"))
    validate_projection(load("projection_result"))
    validate_geometry(load("geometry_result"))
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED" and (parent, NODE_ID, "req") in edges, "parent")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELL11_CURVE_PROJECTION_VERIFY_PASS rows=8 curves=2 dimensions=1")


if __name__ == "__main__":
    main()
