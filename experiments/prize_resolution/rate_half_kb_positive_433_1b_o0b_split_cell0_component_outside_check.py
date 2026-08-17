#!/usr/bin/env python3
"""Validate preregistration and output of the O0b cell-0 outside campaign."""

import argparse
from copy import deepcopy
import hashlib
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
LAUNCHER = HERE / "rate_half_kb_positive_433_1b_o0b_split_cell0_component_outside_modal.py"
COMPONENTS = HERE / "rate_half_kb_positive_433_1b_cell0_principal_component_compiler_result.json"
REPRESENTATIVES = (
    HERE / "rate_half_kb_positive_433_1b_o0b_split_cell0_component_representatives.json"
)
CORE = HERE / "rate_half_kb_positive_433_1b_o0b_split_cell0_outside_core.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_split_cell0_component_outside_result.json"
LAUNCHER_SHA256 = "d1e49937e287e2542b0999f81a9afee0e6302c563f7c11f8ab01c6abf70ff2ec"
COMPONENTS_SHA256 = "2fd2d65ebd033d8cd784f428d31d9b49eb66c4b6a059326ed7efcd60d53ed100"
REPRESENTATIVES_SHA256 = "658ae5f1f3c0667df2cece818e0c89a752ce9cdf7c4f6f421fc4a721134b8fa4"
CORE_SHA256 = "5cd86020b601b68e9a4295d55d057ec0e029dede334397e6bc51f9d840e5561f"
FULL_CASES_SHA256 = "23d7e403e420307b5466ffaf6d2af59d0cf9a4a93766b4d0bcf68231aba1a741"
PILOT_CASES_SHA256 = "47ef7c3a9a92ac2bcb08462377195c0576c2495b0ff1f7c0948103d10e02bc27"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def case_tuple(row):
    return (
        row["component"], row["lane"], row["sigma_o"], row["source_sign"],
        row["xi_index"], row["pairing_index"],
    )


def preregistration():
    require(digest(LAUNCHER) == LAUNCHER_SHA256, "launcher custody")
    require(digest(COMPONENTS) == COMPONENTS_SHA256, "component custody")
    require(digest(REPRESENTATIVES) == REPRESENTATIVES_SHA256,
            "representative manifest custody")
    require(digest(CORE) == CORE_SHA256, "outside core custody")
    spec = importlib.util.spec_from_file_location("cell0_outside_core", CORE)
    core = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    require(core.verify() == (6, 42), "outside core result")
    payload = json.loads(REPRESENTATIVES.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-split-cell0-component-representatives-v1",
            "representative schema")
    require(payload["raw_cases"] == 2520 and
            payload["representative_count"] == 708 and
            len(payload["representatives"]) == 708, "full representative census")
    require(payload["representatives_sha256"] == FULL_CASES_SHA256,
            "full representative-list hash")
    require(payload["pilot_stratum_count"] == 56 and
            payload["pilot_representative_count"] == 24 and
            len(payload["pilot_representatives"]) == 24,
            "pilot cover census")
    require(payload["pilot_representatives_sha256"] == PILOT_CASES_SHA256,
            "pilot representative-list hash")
    require(len({tuple(row) for row in payload["representatives"]}) == 708,
            "unique full representatives")
    require(set(map(tuple, payload["pilot_representatives"])) <=
            set(map(tuple, payload["representatives"])), "pilot subset")
    return payload


def validate_result(payload, representatives=None):
    representatives = representatives or preregistration()
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-split-cell0-outside-v1",
            "result schema")
    require(payload["app"] ==
            "rs-mca-positive-433-1b-o0b-split-cell0-outside", "result app")
    require(payload["field"] == 2130706433, "result field")
    require(payload["source_components_sha256"] == COMPONENTS_SHA256,
            "result component source")
    require(payload["source_representatives_sha256"] == REPRESENTATIVES_SHA256,
            "result representative source")
    require(payload["source_outside_core_sha256"] == CORE_SHA256,
            "result outside core source")
    require(payload["full_representatives_sha256"] == FULL_CASES_SHA256,
            "result router hash")
    scope = payload["scope"]
    if scope == "pilot":
        expected = tuple(map(tuple, representatives["pilot_representatives"]))
        expected_hash = PILOT_CASES_SHA256
    elif scope == "all":
        expected = tuple(map(tuple, representatives["representatives"]))
        expected_hash = FULL_CASES_SHA256
    else:
        raise RuntimeError("result scope")
    require(payload["selected_cases_sha256"] == expected_hash,
            "selected case hash")
    require(payload["expected_case_count"] == len(expected),
            "expected case count")
    rows = payload["rows"]
    require(payload["processed_case_count"] == len(rows) <= len(expected),
            "processed case count")
    require(tuple(case_tuple(row) for row in rows) == expected[:len(rows)],
            "ordered case prefix")
    require(len({case_tuple(row) for row in rows}) == len(rows),
            "unique result cases")
    statuses = {row["status"] for row in rows}
    require(payload["status_counts"] == {
        status: sum(row["status"] == status for row in rows)
        for status in sorted(statuses)
    }, "status count")
    require(payload["unit_count"] == sum(row.get("unit", False) for row in rows),
            "unit count")
    for row in rows:
        require(row["component"] in {"A", "B"} and
                row["lane"] in {"S0", "SDE", "SDF"} and
                row["sigma_o"] in {-1, 1} and
                row["source_sign"] in {-1, 1} and
                0 <= row["xi_index"] < 7 and
                0 <= row["pairing_index"] < 15, "row domain")
        if row["status"] == "COMPLETE":
            require(len(row["program_sha256"]) == 64, "program hash")
            require(isinstance(row["unit"], bool), "unit flag")
            if row["unit"]:
                require(row["dimension"] == -1 and row["basis_size"] == 1,
                        "unit certificate shape")
                require(row["input_polynomials"] == [] and
                        row["guard_factors"] == [], "compact unit row")
            else:
                require(isinstance(row["dimension"], int) and
                        isinstance(row["basis_size"], int) and
                        len(row["input_polynomials"]) == 6 and
                        len(row["guard_factors"]) > 0, "nonunit witness payload")
        else:
            require(row["status"] in {"TIMEOUT", "ERROR", "REMOTE_ERROR"},
                    "failure status")
    complete = (len(rows) == len(expected) and
                all(row["status"] == "COMPLETE" for row in rows))
    require(payload["complete"] is complete, "completeness bit")
    return {
        "scope": scope,
        "complete": complete,
        "processed": len(rows),
        "expected": len(expected),
        "unit": sum(row.get("unit", False) for row in rows),
        "nonunit": sum(row["status"] == "COMPLETE" and not row.get("unit", False)
                       for row in rows),
    }


def hostile_self_test(representatives):
    cases = representatives["pilot_representatives"]
    rows = []
    for case in cases:
        rows.append({
            "component": case[0], "lane": case[1], "sigma_o": case[2],
            "source_sign": case[3], "xi_index": case[4],
            "pairing_index": case[5], "status": "COMPLETE", "unit": True,
            "dimension": -1, "basis_size": 1, "stdout": "UNIT=1\nEND\n",
            "stderr": "", "program_sha256": "0"*64,
            "input_polynomials": [], "guard_factors": [],
        })
    baseline = {
        "schema": "rate-half-kb-positive-433-1b-o0b-split-cell0-outside-v1",
        "app": "rs-mca-positive-433-1b-o0b-split-cell0-outside",
        "scope": "pilot", "complete": True, "field": 2130706433,
        "source_components_sha256": COMPONENTS_SHA256,
        "source_representatives_sha256": REPRESENTATIVES_SHA256,
        "source_outside_core_sha256": CORE_SHA256,
        "full_representatives_sha256": FULL_CASES_SHA256,
        "selected_cases_sha256": PILOT_CASES_SHA256,
        "expected_case_count": 24, "processed_case_count": 24,
        "status_counts": {"COMPLETE": 24}, "unit_count": 24, "rows": rows,
    }
    require(validate_result(baseline, representatives)["complete"],
            "synthetic baseline")
    caught = 0
    for mutate in (
        lambda row: row["rows"].pop(),
        lambda row: row["rows"][0].update({"xi_index": 6}),
        lambda row: row.update({"unit_count": 23}),
    ):
        trial = deepcopy(baseline)
        mutate(trial)
        try:
            validate_result(trial, representatives)
        except RuntimeError:
            caught += 1
    require(caught == 3, "hostile controls")
    return caught


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-result", action="store_true")
    parser.add_argument("--require-complete", action="store_true")
    args = parser.parse_args()
    representatives = preregistration()
    mutations = hostile_self_test(representatives)
    if not RESULT.is_file():
        require(not args.require_result and not args.require_complete,
                "result required but absent")
        print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELL0_OUTSIDE_CHECK_PASS "
              f"state=PRELAUNCH full=708 pilot=24 mutations={mutations}/3")
        return
    summary = validate_result(json.loads(RESULT.read_text()), representatives)
    require(not args.require_complete or summary["complete"],
            "complete result required")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELL0_OUTSIDE_CHECK_PASS "
          f"state={'COMPLETE' if summary['complete'] else 'INCOMPLETE'} "
          f"scope={summary['scope']} rows={summary['processed']}/{summary['expected']} "
          f"unit={summary['unit']} nonunit={summary['nonunit']} "
          f"mutations={mutations}/3")


if __name__ == "__main__":
    main()
