#!/usr/bin/env python3
"""Verify the positive 433-1b cell-14 quadratic-curve decomposition."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
STRUCTURE_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell14_kernel_structure_modal.py"
STRUCTURE_RESULT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell14_kernel_structure_result.json"
CURVE_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell14_curve_kernel_modal.py"
CURVE_RESULT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell14_curve_kernel_result.json"
EXCEPTION_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell14_c_exception_modal.py"
EXCEPTION_RESULT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell14_c_exception_result.json"
BOUNDARY_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell14_kernel_denominator_boundary_modal.py"
BOUNDARY_RESULT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell14_kernel_denominator_boundary_result.json"
STRUCTURE_SCRIPT_SHA256 = "fb3c41e59c9eabcd25026a59810c70d72452d8d0745fbdd9b4c9c192acece15d"
STRUCTURE_RESULT_SHA256 = "3edb40907f5607986b0e8667675e0d325fcb837442ee8acce9221c85c80581e6"
CURVE_SCRIPT_SHA256 = "772cb45bea78d28fe4fdcecb25c0e440d3de7128a1e3b61dfecf0237895dc1e2"
CURVE_RESULT_SHA256 = "0edd681c3557e6847eaad06eb328793a30237f5ddd7dda8d1741c3a5b8c33d81"
EXCEPTION_SCRIPT_SHA256 = "e034b350b8e88d8df79131cc139bd13d95a3a1550f3c05f747434ff860d036fe"
EXCEPTION_RESULT_SHA256 = "f2a4d8f8d996e624dec6a661dbe22f78a4bc5204b9da66e14ccf09a46f9548db"
BOUNDARY_SCRIPT_SHA256 = "045dd963a21456cdf16e47cca20e4441cc1ea5872f318a5b3ac446355acf3f77"
BOUNDARY_RESULT_SHA256 = "3ad8dcc60cf604e2f648ebb8474622da0abcf974f0b131f02d9a07d7e92de95c"
PRODUCT = EXPERIMENTS / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_common_vieta_minor_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_common_exception_classifier",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_complete_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
    "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_structure(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell14-kernel-structure-v1", "schema")
    require(payload["field"] == 2130706433 and
            payload["source_product_sha256"] == digest(PRODUCT), "source custody")
    expected = set(itertools.product((-1, 1), (-1, 1), range(6)))
    actual = set()
    relation_signatures = {}
    program_hashes = set()
    for row in payload["rows"]:
        key = (*row["epsilon"], row["chart"])
        require(key not in actual, "duplicate structure row")
        actual.add(key)
        require(row["status"] == "COMPLETE" and not row["unit"] and
                row["dimension"] == 1 and row["basis_size"] == 17,
                "curve chart")
        require(row["etr_dimension"] == 3 and row["etr_size"] == 1 and
                row["erb_dimension"] == 3 and row["erb_size"] == 1,
                "projection dimensions")
        require(row["relation_t"]["degree"] == 4 and
                row["relation_t"]["terms"] == 6 and
                row["relation_c"]["degree"] == 3 and
                row["relation_c"]["terms"] == 6 and
                row["relation_rb"]["degree"] == 7 and
                row["relation_rb"]["terms"] == 17,
                "projection summaries")
        require(row["t_denominator_unit"] and
                row["t_exception_dimension"] == -1 and
                row["t_exception_size"] == 1, "t denominator")
        require(not row["c_denominator_unit"] and
                row["c_exception_dimension"] == 0 and
                row["c_exception_size"] == 4, "c exception")
        require(not row["reference_cofactor_unit"] and
                row["reference_exception_dimension"] == 0 and
                row["reference_exception_size"] == 33, "cofactor exception")
        require("BEGIN" in row["stdout"] and "END" in row["stdout"] and
                "UNIT=0" in row["stdout"] and not row["stderr"], "Singular transcript")
        signature = tuple(
            row[name]["expression"]
            for name in ("relation_t", "relation_c", "relation_rb")
        )
        signs = tuple(row["epsilon"])
        require(signs not in relation_signatures or
                relation_signatures[signs] == signature, "chart projection mismatch")
        relation_signatures[signs] = signature
        program_hashes.add(row["program_sha256"])
    require(actual == expected and len(program_hashes) == 24, "24-chart census")
    require(len(relation_signatures) == 4, "source-sign projections")
    return relation_signatures


def verify_curve(payload, relation_signatures):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell14-curve-kernel-v1", "curve schema")
    require(payload["field"] == 2130706433 and
            payload["source_structure_sha256"] == digest(STRUCTURE_RESULT),
            "curve source custody")
    expected = set(itertools.product((-1, 1), (-1, 1)))
    actual = set()
    degree_profile = (10, 10, 7, 11, 11, 9, 10, 10)
    for row in payload["rows"]:
        signs = tuple(row["epsilon"])
        require(signs not in actual, "duplicate curve row")
        actual.add(signs)
        require(row["status"] == "COMPLETE" and row["all_rows_zero"],
                "kernel completion")
        require(len(row["kernel"]) == 8 and
                tuple(item["degree"] for item in row["kernel"]) == degree_profile,
                "kernel profile")
        require(len(row["normalized_kernel"]) == 8 and
                row["normalized_kernel"][-2]["numerator"]["expression"] == "-1" and
                row["normalized_kernel"][-1]["numerator"]["expression"] == "1",
                "kernel normalization")
        require(len(row["row_checks"]) == 10 and
                all(check == {"zero": True, "denominator": "1"}
                    for check in row["row_checks"]), "ten row checks")
        require(row["relation_rb"]["expression"] == relation_signatures[signs][2],
                "relation custody")
    require(actual == expected, "four kernel rows")


def verify_exception(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell14-c-exception-v1", "exception schema")
    require(payload["field"] == 2130706433 and
            payload["source_product_sha256"] == digest(PRODUCT),
            "exception source custody")
    expected = set(itertools.product((-1, 1), (-1, 1)))
    actual = set()
    program_hashes = set()
    for row in payload["rows"]:
        signs = tuple(row["epsilon"])
        require(signs not in actual, "duplicate exception row")
        actual.add(signs)
        require(row["status"] == "COMPLETE" and not row["unit"] and
                row["dimension"] == 0 and row["basis_size"] == 4,
                "closure exception")
        require(row["open_unit"] and row["open_dimension"] == -1 and
                row["open_basis_size"] == 1, "open exception unit")
        require("LEX_BEGIN" in row["stdout"] and "LEX_END" in row["stdout"] and
                "OPEN_UNIT=1" in row["stdout"] and "END" in row["stdout"] and
                not row["stderr"], "exception transcript")
        program_hashes.add(row["program_sha256"])
    require(actual == expected and len(program_hashes) == 4,
            "four-sign exception census")


def verify_boundary(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell14-kernel-denominator-boundary-v1",
            "boundary schema")
    require(payload["field"] == 2130706433 and
            payload["source_curve_sha256"] == digest(CURVE_RESULT),
            "boundary source custody")
    expected = set(itertools.product((-1, 1), (-1, 1)))
    actual = set()
    program_hashes = set()
    for row in payload["rows"]:
        signs = tuple(row["epsilon"])
        require(signs not in actual, "duplicate boundary row")
        actual.add(signs)
        require(row["status"] == "COMPLETE" and row["unit"] and
                row["dimension"] == -1 and row["basis_size"] == 1,
                "kernel denominator boundary")
        require("INITIAL_DIM=1" in row["stdout"] and
                "UNIT=1" in row["stdout"] and "END" in row["stdout"] and
                not row["stderr"], "boundary transcript")
        program_hashes.add(row["program_sha256"])
    require(actual == expected and len(program_hashes) == 4,
            "four-sign boundary census")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED", "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"missing parent {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")


def main():
    require(digest(STRUCTURE_SCRIPT) == STRUCTURE_SCRIPT_SHA256, "structure script")
    require(digest(STRUCTURE_RESULT) == STRUCTURE_RESULT_SHA256, "structure result")
    require(digest(CURVE_SCRIPT) == CURVE_SCRIPT_SHA256, "curve script")
    require(digest(CURVE_RESULT) == CURVE_RESULT_SHA256, "curve result")
    require(digest(EXCEPTION_SCRIPT) == EXCEPTION_SCRIPT_SHA256, "exception script")
    require(digest(EXCEPTION_RESULT) == EXCEPTION_RESULT_SHA256, "exception result")
    require(digest(BOUNDARY_SCRIPT) == BOUNDARY_SCRIPT_SHA256, "boundary script")
    require(digest(BOUNDARY_RESULT) == BOUNDARY_RESULT_SHA256, "boundary result")
    signatures = verify_structure(json.loads(STRUCTURE_RESULT.read_text()))
    verify_curve(json.loads(CURVE_RESULT.read_text()), signatures)
    verify_exception(json.loads(EXCEPTION_RESULT.read_text()))
    verify_boundary(json.loads(BOUNDARY_RESULT.read_text()))
    verify_dag()
    print("cell=14 charts=24 curve_dim=1 kernels=4 open_exception=unit kernel_boundary=unit")


if __name__ == "__main__":
    main()
