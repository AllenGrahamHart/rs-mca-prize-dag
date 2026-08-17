#!/usr/bin/env python3
"""Outcome-neutral checker for the exact root-free O0b FFI chart."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
BASIS = HERE / "rate_half_kb_positive_433_1b_cell3_global_common_basis_result.json"
COMPILER = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
ROOTFREE = HERE / "rate_half_kb_positive_433_1b_o0b_ffi_rootfree_program.py"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_ffi_exact_rootfree_program.py"
COLLAPSED = HERE / "rate_half_kb_positive_433_1b_o0b_ffi_collapsed_result.json"
SLOPE_ANCHORS = HERE / "rate_half_kb_positive_433_1b_o0b_collapsed_finite_slope_anchors.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_ffi_exact_rootfree_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
COMPILER_SHA256 = "048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03"
ROOTFREE_SHA256 = "dfdbfb078ab594d18b53e511e8e17b0375b25a551aa4d58a7d1fc82c7b3689eb"
COLLAPSED_SHA256 = "86d8686abf3d178bef2e1adaa17ca62e7d8b6dc0f5021b95cc8ee2f398f64335"
SLOPE_ANCHORS_SHA256 = "1059e49271b06104353ad61c2e3c766c56e253ae3480c0410fb6afa08802ac99"
CASE = [3, "S0", -1, -1, -1, 2, 0]
CHART_MASK = ["finite", "finite", "infinity"]
SLOPE_NODE = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_"
    "xi2_pairing0_collapsed_finite_slope_anchors"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(BASIS.read_bytes()).hexdigest() == BASIS_SHA256,
            "basis custody")
    require(hashlib.sha256(COMPILER.read_bytes()).hexdigest() == COMPILER_SHA256,
            "compiler custody")
    require(hashlib.sha256(ROOTFREE.read_bytes()).hexdigest() == ROOTFREE_SHA256,
            "root-free source custody")
    require(hashlib.sha256(COLLAPSED.read_bytes()).hexdigest() == COLLAPSED_SHA256,
            "collapsed-input custody")
    require(hashlib.sha256(SLOPE_ANCHORS.read_bytes()).hexdigest() ==
            SLOPE_ANCHORS_SHA256, "slope-anchor custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-ffi-exact-rootfree-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and
            payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_basis_sha256"] == BASIS_SHA256 and
            payload["source_compiler_sha256"] == COMPILER_SHA256 and
            payload["source_rootfree_sha256"] == ROOTFREE_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest() and
            payload["source_collapsed_sha256"] == COLLAPSED_SHA256 and
            payload["source_slope_anchors_sha256"] == SLOPE_ANCHORS_SHA256,
            "source fields")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"}, "row status")
    require(row["case"] == CASE and row["chart_mask"] == CHART_MASK and
            row["relation"] == "exact collapsed FFI finite-root chart" and
            row["finite_slope_guards"] == ["m4p1", "m5p1"] and
            row["slope_anchor_node"] == SLOPE_NODE and
            row["variable_count"] == 14 and
            row["eliminated_root_variables"] == ["u4", "u5"] and
            row["retained_kernel_indices"] == [0, 1, 3, 4, 6, 7] and
            row["collapsed_kernel_indices"] == [2, 5] and
            row["kernel_graph_equation_count"] == 8 and
            row["common_basis_size"] == 21 and
            row["determinant_equation_count"] == 2 and
            row["boundary_guards"] == ["f", "d^2-e^2", "b+1"] and
            row["rabinowitsch_equation_count"] == 1 and
            row["generator_count"] == 34,
            "exact input ledger")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout transcript")
        return {"status": "TIMEOUT", "unit": False}
    require(row["stderr"] == "" and "END" in row["stdout"] and
            "?" not in row["stdout"], "complete transcript")
    if row["unit"]:
        require(row["dimension"] == -1 and row["basis_size"] == 1 and
                row["input_program"] == "" and "UNIT=1" in row["stdout"],
                "unit result")
    else:
        require(row["input_program"] != "" and "UNIT=0" in row["stdout"],
                "retained nonunit result")
    return {"status": "COMPLETE", "unit": row["unit"]}


def expect_rejected(payload, label):
    try:
        verify(payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def hostile_audit():
    payload = json.loads(RESULT.read_text())
    mutation = deepcopy(payload)
    mutation["collection_complete"] = False
    expect_rejected(mutation, "incomplete collection")
    mutation = deepcopy(payload)
    mutation["row"]["finite_slope_guards"] = ["m4p1"]
    expect_rejected(mutation, "missing slope guard")
    mutation = deepcopy(payload)
    mutation["row"]["relation"] = "necessary determinant superset"
    expect_rejected(mutation, "lost exact relation")
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFI_EXACT_ROOTFREE_CHECK_PASS "
          f"status={result['status']} unit={int(result['unit'])} "
          f"mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()
