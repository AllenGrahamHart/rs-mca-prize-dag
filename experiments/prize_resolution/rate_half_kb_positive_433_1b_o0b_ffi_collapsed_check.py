#!/usr/bin/env python3
"""Outcome-neutral checker for the collapsed O0b FFI pilot."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
BASIS = HERE / "rate_half_kb_positive_433_1b_cell3_global_common_basis_result.json"
COMPILER = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_ffi_collapsed_program.py"
MSOLVE = HERE / "rate_half_kb_positive_433_1b_o0b_ffi_msolve_result.json"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_ffi_collapsed_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
COMPILER_SHA256 = "048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03"
MSOLVE_SHA256 = "f0846e25f26981e045d4416233bd81d36dac6c3a44b0da7b2cd19912a02c57dd"
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
    require(hashlib.sha256(MSOLVE.read_bytes()).hexdigest() == MSOLVE_SHA256,
            "msolve-input custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-ffi-collapsed-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and
            payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_basis_sha256"] == BASIS_SHA256 and
            payload["source_compiler_sha256"] == COMPILER_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest() and
            payload["source_msolve_sha256"] == MSOLVE_SHA256,
            "source fields")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"}, "row status")
    require(row["case"] == CASE and row["chart_mask"] == CHART_MASK and
            row["variable_count"] == 16 and
            row["retained_kernel_indices"] == [0, 1, 3, 4, 6, 7] and
            row["collapsed_kernel_indices"] == [2, 5] and
            row["kernel_graph_equation_count"] == 8 and
            row["common_basis_size"] == 21 and
            row["finite_chart_equation_count"] == 4 and
            row["boundary_guards"] == ["f", "d^2-e^2", "b+1"] and
            row["rabinowitsch_equation_count"] == 1 and
            row["generator_count"] == 36,
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
    mutation["row"]["collapsed_kernel_indices"] = [2]
    expect_rejected(mutation, "missing collapse")
    mutation = deepcopy(payload)
    mutation["row"]["boundary_guards"] = ["f", "b+1"]
    expect_rejected(mutation, "missing square guard")
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFI_COLLAPSED_CHECK_PASS "
          f"status={result['status']} unit={int(result['unit'])} "
          f"mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()
