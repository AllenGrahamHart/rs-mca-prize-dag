#!/usr/bin/env python3
"""Fail-closed verifier for the degree-12 leading-branch decomposition."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
FILES = {
    "modal_degree12_leading_factors_output.json": "4519ecb07310dc449ad5144deabcadc44b72d15ea9c0552132c714cec9764533",
    "modal_degree12_leading_syzygy_r02_output.json": "bfb094b44c48836473c7cf33824256e6defd29afd24db195a1ef1d5d876df8ba",
    "modal_degree12_function_field_r02_output.json": "c95e5c29c51c9b6b3f1fc25b2d40dd970b4fecf0172a7fca4cdc164e33180d36",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def done(row: dict[str, object]) -> dict[str, object] | None:
    return next((record for record in row.get("records", []) if record.get("phase") == "DONE"), None)


def validate(leading: dict[str, object], syzygy: dict[str, object], fence: dict[str, object]) -> None:
    require(leading["counts"] == {"FAIL": 0, "PASS": 2, "REMOTE_ERROR": 0, "TIMEOUT": 0}, "leading counts")
    expected = {
        "F04-R02": {
            "R12": [(6, 15, False)],
            "E2": [(1, 1, False), (22, 235, False)],
            "E3": [(23, 247, False)],
        },
        "F04-R20": {
            "R12": [(6, 15, False)],
            "E2": [(1, 1, False), (23, 248, False)],
            "E3": [(24, 267, False)],
        },
    }
    for row in leading["results"]:
        terminal = done(row)
        require(row["status"] == "PASS" and terminal is not None, "leading completion")
        observed = {}
        for record in terminal["records"]:
            observed[record["name"]] = [
                (factor["degree"], factor["terms"], factor["named_unit_factor"])
                for factor in record["factors"]
            ]
        require(observed == expected[row["cell"]], f"leading census {row['cell']}")
    r02 = expected["F04-R02"]
    r20 = expected["F04-R20"]
    require(r02["R12"] == r20["R12"], "common R12 leading census")

    require(syzygy["counts"] == {"FAIL": 0, "PASS": 1, "REMOTE_ERROR": 0, "TIMEOUT": 0}, "syzygy counts")
    terminal = done(syzygy["results"][0])
    require(terminal is not None and terminal["cell"] == "F04-R02", "syzygy completion")
    require(
        [step["primitive"]["degrees"][0] for step in terminal["steps"]] == [35, 34, 34],
        "syzygy x degrees",
    )
    require(
        [step["primitive"]["terms"] for step in terminal["steps"]] == [40921, 83811, 149340],
        "syzygy term growth",
    )
    require([step["content"]["degree"] for step in terminal["steps"]] == [0, 0, 23], "syzygy contents")

    require(fence["counts"] == {"FAIL": 0, "PASS": 0, "REMOTE_ERROR": 0, "TIMEOUT": 1}, "function-field fence counts")
    row = fence["results"][0]
    require(row["status"] == "TIMEOUT" and done(row) is None, "function-field timeout only")
    phases = [record["phase"] for record in row["records"]]
    require(phases == ["START", "CONVERTED"], "function-field phase fence")


def main() -> None:
    for name, expected_hash in FILES.items():
        require(hashlib.sha256((HERE / name).read_bytes()).hexdigest() == expected_hash, f"hash {name}")
    leading = json.loads((HERE / "modal_degree12_leading_factors_output.json").read_text())
    syzygy = json.loads((HERE / "modal_degree12_leading_syzygy_r02_output.json").read_text())
    fence = json.loads((HERE / "modal_degree12_function_field_r02_output.json").read_text())
    validate(leading, syzygy, fence)
    mutant = copy.deepcopy(leading)
    done(mutant["results"][0])["records"][1]["factors"][1]["named_unit_factor"] = True
    rejected = False
    try:
        validate(mutant, syzygy, fence)
    except AssertionError:
        rejected = True
    require(rejected, "mutation rejection")
    print("KB_C2_112_FIXED_R02_R20_DEGREE12_LEADING_PASS targets=2 prs_steps=3 mutations=1/1")


if __name__ == "__main__":
    main()
