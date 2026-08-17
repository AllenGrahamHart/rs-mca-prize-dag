#!/usr/bin/env python3
"""Outcome-neutral checker for the O0b FFI msolve pilot."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
BASIS = HERE / "rate_half_kb_positive_433_1b_cell3_global_common_basis_result.json"
COMPILER = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
INPUT_CORE = HERE / "rate_half_kb_positive_433_1b_o0b_ffi_msolve_input.py"
SMOKE = HERE / "msolve_prime_field_smoke_result.json"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_ffi_msolve_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
COMPILER_SHA256 = "048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03"
SMOKE_SHA256 = "4bf0791c422e83438b65c2c871119eee0a7124be1e2a6d508185ce7a13e11d70"
CASE = [3, "S0", -1, -1, -1, 2, 0]
CHART_MASK = ["finite", "finite", "infinity"]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def unit_output(text):
    return bool(re.search(
        r"#length of basis:\s+1 element\s+#---\s+\[\s*1\s*\]:\s*$",
        text, re.DOTALL,
    ))


def verify(payload=None):
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(BASIS.read_bytes()).hexdigest() == BASIS_SHA256,
            "basis custody")
    require(hashlib.sha256(COMPILER.read_bytes()).hexdigest() == COMPILER_SHA256,
            "compiler custody")
    require(hashlib.sha256(SMOKE.read_bytes()).hexdigest() == SMOKE_SHA256,
            "smoke custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-ffi-msolve-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and payload["case"] == CASE and
            payload["chart_mask"] == CHART_MASK,
            "scope")
    require(payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_basis_sha256"] == BASIS_SHA256 and
            payload["source_compiler_sha256"] == COMPILER_SHA256 and
            payload["source_input_core_sha256"] ==
            hashlib.sha256(INPUT_CORE.read_bytes()).hexdigest() and
            payload["source_smoke_sha256"] == SMOKE_SHA256,
            "source fields")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"}, "row status")
    require(row["case"] == CASE and row["chart_mask"] == CHART_MASK and
            row["generator_count"] == 38 and
            row["explicit_polynomial_count"] == 38 and
            row["kernel_graph_equation_count"] == 8 and
            row["matching_chart_equation_count"] == 6 and
            row["rabinowitsch_equation_count"] == 1 and
            len(row["variables"]) == 18 and row["msolve_version"] == "0.7.5",
            "input ledger")
    msolve_input = row["msolve_input"]
    require(hashlib.sha256(msolve_input.encode()).hexdigest() ==
            row["msolve_input_sha256"], "input hash")
    lines = msolve_input.splitlines()
    require(lines[0] == ",".join(row["variables"]) and
            lines[1] == "2130706433" and
            len(msolve_input.split(",\n")) == 38,
            "msolve input format")
    require(unit_output(row["msolve_smoke_output"]), "remote smoke")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str) and
                isinstance(row["partial_output"], str),
                "timeout transcript")
        return {"status": "TIMEOUT", "unit": False}
    require(row["stderr"] == "" and
            row["output_sha256"] == hashlib.sha256(row["output"].encode()).hexdigest(),
            "complete output custody")
    if row["unit"]:
        require(row["output_bytes"] == len(row["output"].encode()) and
                unit_output(row["output"]), "unit basis")
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
    mutation["row"]["generator_count"] = 37
    expect_rejected(mutation, "missing generator")
    mutation = deepcopy(payload)
    mutation["row"]["msolve_input_sha256"] = "0" * 64
    expect_rejected(mutation, "wrong input hash")
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFI_MSOLVE_CHECK_PASS "
          f"status={result['status']} unit={int(result['unit'])} "
          f"mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()
