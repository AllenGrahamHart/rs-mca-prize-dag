#!/usr/bin/env python3
"""Outcome-neutral checker for the sparse lifted O0b FFI boundary test."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
BASIS = HERE / "rate_half_kb_positive_433_1b_cell3_global_common_basis_result.json"
COMPILER = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_lifted_boundary_program.py"
BOUNDARY = HERE / "rate_half_kb_positive_433_1b_o0b_chart_multifinite_boundary_result.json"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_chart_ffi_lifted_boundary_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
COMPILER_SHA256 = "048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03"
BOUNDARY_SHA256 = "9e5dd9324b1fe7575c7d16135465bd1c560f3cce9d3effbee5ecece6391109c6"
CASE = [3, "S0", -1, -1, -1, 2, 0]
CHART_MASK = ["finite", "finite", "infinity"]


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
    require(hashlib.sha256(BOUNDARY.read_bytes()).hexdigest() == BOUNDARY_SHA256,
            "boundary-pilot custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-chart-ffi-lifted-boundary-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and payload["case"] == CASE and
            payload["chart_mask"] == CHART_MASK,
            "scope")
    require(payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_basis_sha256"] == BASIS_SHA256 and
            payload["source_compiler_sha256"] == COMPILER_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest() and
            payload["source_boundary_pilot_sha256"] == BOUNDARY_SHA256,
            "source fields")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"}, "row status")
    require(row["chart_mask"] == CHART_MASK and row["variable_count"] == 18 and
            row["finite_root_count"] == 2 and
            row["kernel_lift_variable_count"] == 8 and
            row["kernel_graph_equation_count"] == 8 and
            row["common_basis_size"] == 21 and
            row["outside_equation_count"] == 8 and
            row["matching_chart_equation_count"] == 6 and
            row["rabinowitsch_equation_count"] == 1 and
            row["boundary_guard"] == "b+1" and row["generator_count"] == 38,
            "input ledger")
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
    mutation["row"]["kernel_graph_equation_count"] = 7
    expect_rejected(mutation, "missing graph equation")
    mutation = deepcopy(payload)
    mutation["row"]["boundary_guard"] = "b-1"
    expect_rejected(mutation, "wrong boundary")
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_CHART_FFI_LIFTED_BOUNDARY_CHECK_PASS "
          f"status={result['status']} unit={int(result['unit'])} "
          f"mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()
