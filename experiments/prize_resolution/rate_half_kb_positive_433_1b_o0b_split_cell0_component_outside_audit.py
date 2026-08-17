#!/usr/bin/env python3
"""Independent audit of the complete O0b split cell-0 outside exclusion."""

import ast
from copy import deepcopy
import hashlib
import importlib.util
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
LAUNCHER = HERE / "rate_half_kb_positive_433_1b_o0b_split_cell0_component_outside_modal.py"
CHECKER = HERE / "rate_half_kb_positive_433_1b_o0b_split_cell0_component_outside_check.py"
CORE = HERE / "rate_half_kb_positive_433_1b_o0b_split_cell0_outside_core.py"
REPRESENTATIVES = (
    HERE / "rate_half_kb_positive_433_1b_o0b_split_cell0_component_representatives.json"
)
COMPONENTS = HERE / "rate_half_kb_positive_433_1b_cell0_principal_component_compiler_result.json"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_split_cell0_component_outside_result.json"
HASHES = {
    LAUNCHER: "04ae51440703ad0116e33ce6a4c7f3312eff748cd8c3fa1a1d326c4d465f5d48",
    CHECKER: "74770cfadbfa1275fe58fbee187b40e00cea8e8526ff3dc07347a8011c8046b5",
    CORE: "5cd86020b601b68e9a4295d55d057ec0e029dede334397e6bc51f9d840e5561f",
    REPRESENTATIVES: "658ae5f1f3c0667df2cece818e0c89a752ce9cdf7c4f6f421fc4a721134b8fa4",
    COMPONENTS: "2fd2d65ebd033d8cd784f428d31d9b49eb66c4b6a059326ed7efcd60d53ed100",
    RESULT: "6aed35275a09c9ceaa55f2e47ad07409f7d3ed0ffd8f77010ce080ba862b95aa",
}
SATURATION = re.compile(r"SAT=(\d+),DIM=(-?\d+),SIZE=(\d+)")


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


def validate_payload(result, representatives):
    expected = tuple(map(tuple, representatives["representatives"]))
    require(result["scope"] == "all" and result["complete"] is True,
            "complete full scope")
    require(result["expected_case_count"] == result["processed_case_count"] == 708,
            "complete case census")
    require(result["status_counts"] == {"COMPLETE": 708} and
            result["unit_count"] == 708, "complete unit aggregate")
    require(tuple(case_tuple(row) for row in result["rows"]) == expected,
            "ordered representative cover")

    program_hashes = set()
    guard_profile = {30: 0, 31: 0}
    for row in result["rows"]:
        require(row["status"] == "COMPLETE" and row["unit"] is True and
                row["dimension"] == -1 and row["basis_size"] == 1,
                "unit row summary")
        require(row["stderr"] == "" and row["input_polynomials"] == [] and
                row["guard_factors"] == [], "compact clean row")
        require(re.fullmatch(r"[0-9a-f]{64}", row["program_sha256"]) is not None,
                "program digest form")
        program_hashes.add(row["program_sha256"])
        stdout = row["stdout"]
        require("BEGIN\nDIM=-1\nSIZE=1\nUNIT=1\nEND\n" in stdout and
                "?" not in stdout, "Singular terminal certificate")
        stages = [(int(index), int(dimension), int(size))
                  for index, dimension, size in SATURATION.findall(stdout)]
        require(len(stages) in guard_profile and
                [row[0] for row in stages] == list(range(len(stages))),
                "contiguous saturation stages")
        first_unit = next((index for index, (_, dimension, size) in
                           enumerate(stages) if dimension == -1 and size == 1), None)
        require(first_unit is not None and
                all(dimension == -1 and size == 1
                    for _, dimension, size in stages[first_unit:]),
                "stable unit tail")
        guard_profile[len(stages)] += 1
    require(len(program_hashes) == 708, "distinct program census")
    require(guard_profile == {30: 354, 31: 354}, "guard-stage profile")
    return guard_profile


def hostile_controls(result, representatives):
    caught = 0
    mutations = (
        lambda value: value["rows"][0].update({"unit": False}),
        lambda value: value["rows"].__setitem__(0, value["rows"][1]),
        lambda value: value.update({"unit_count": 707}),
    )
    for mutation in mutations:
        trial = deepcopy(result)
        mutation(trial)
        try:
            validate_payload(trial, representatives)
        except RuntimeError:
            caught += 1
    require(caught == 3, "hostile mutation census")
    return caught


def main():
    for path, expected in HASHES.items():
        require(digest(path) == expected, f"custody {path.name}")
    source = LAUNCHER.read_text()
    ast.parse(source)
    for snippet in (
        "relation_x",
        "records[xi_index]*a2_missing-a0_missing",
        "(p2*q0-p0*q2)**2 - (p2*q1-p1*q2)*(p1*q0-p0*q1)",
        "missing_label*b1_missing*b1_missing",
        "target_values[left]**2 - target_values[right]**2",
        "evaluate((d0, d1, d2), label)",
        "list S{index}=sat(G,H{index})",
        "write_checkpoint(scope, cases, rows, complete=False)",
    ):
        require(snippet in source, f"launcher construction {snippet}")

    spec = importlib.util.spec_from_file_location("outside_core", CORE)
    core = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    require(core.verify() == (6, 42), "signed outside-record core")

    representatives = json.loads(REPRESENTATIVES.read_text())
    require(representatives["raw_cases"] == 2520 and
            representatives["representative_count"] == 708 and
            representatives["s0_profile"] == {"2": 36, "4": 192} and
            representatives["repeated_profile"] == {"2": 120, "4": 360},
            "quotient manifest")
    result = json.loads(RESULT.read_text())
    guard_profile = validate_payload(result, representatives)
    mutations = hostile_controls(result, representatives)
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELL0_OUTSIDE_AUDIT_PASS "
          f"raw_component_cases=2520 representatives=708 unit=708 "
          f"guards={guard_profile} mutations={mutations}/3")


if __name__ == "__main__":
    main()
