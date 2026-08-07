#!/usr/bin/env python3
"""Fail-closed verifier for the exact R02/R20 generic route cuts."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
BALANCED = HERE.parent / "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_balanced_quadratic_branch_reduction"
FILES = {
    BALANCED / "modal_remaining_representative_probe_output.json": "75d000ee65bcab90be7e2f23eebc3c5a7d05db5a83cdefebc150e06a6449af6c",
    HERE / "modal_generic_representatives_output.json": "bfc7e4e7055f6e302763c719f0011dc02bfef8b1c74236840ed2b1d6fa03a3eb",
    HERE / "modal_full_identity_single_c0_output.json": "cd074c216eecee9bdd285bb47fb3048a3ee8f5651b4bc3dd3bc14b82bb372a69",
    HERE / "modal_full_identity_single_c1_output.json": "d8570af94aac04a20fdb9cda2c7c4fd2cc40b91a330a1ed93f60d72ccc8db433",
    HERE / "modal_full_identity_single_i_c0_output.json": "026e43ff1333dec1d7b0ab719575b41dacf88d88174c55df149e24a35265e1fe",
    HERE / "modal_full_identity_representatives_output.json": "bba7fa12dcc7f5908944793267bbf4567b7622c6c3fc16bef1d4bea269c95fe5",
    HERE / "modal_f04_full_j_intersections_output.json": "a5342189f495f77194ee9463e09a236f9eb8e554dbb92ad1a3dba961e6a60a9a",
    HERE / "modal_quotient_full_j_output.json": "9d473d3279ef4919d9e5439575ab6d9c29b6218a660c9747a4bc5ba0489d7997",
    HERE / "modal_quadratic_quotient_full_j_r02_output.json": "3e484c6e2903d2202ff9f8864cbf1f6f4dca0167422f3793ce6cef7bbc8bc6a5",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def done(row: dict[str, object]) -> dict[str, object] | None:
    return next((record for record in row.get("records", []) if record.get("phase") == "DONE"), None)


def main() -> None:
    for path, expected in FILES.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected, f"hash {path.name}")

    generic = json.loads((HERE / "modal_generic_representatives_output.json").read_text())
    require(generic["counts"] == {"FAIL": 0, "PASS": 8, "REMOTE_ERROR": 0, "TIMEOUT": 4}, "generic counts")
    for row in generic["results"]:
        if row["factor_index"] == 2:
            require(row["status"] == "TIMEOUT" and done(row) is None, "degree-12 timeout")
            continue
        terminal = done(row)
        require(row["status"] == "PASS" and terminal is not None, "cubic completion")
        expected_empty = (row["cell"].endswith("R02") and row["factor_index"] == 1) or (row["cell"].endswith("R20") and row["factor_index"] == 0)
        require((terminal["localizer_nilpotence_index"] is not None) == expected_empty, "cubic classification")

    j0 = json.loads((HERE / "modal_full_identity_single_c0_output.json").read_text())
    j0_done = done(j0["results"][0])
    factors = j0_done["identities"]["J"]["descended_factors"]
    require([(factor["metric"]["degree"], factor["exponent"]) for factor in factors] == [(1, 4), (8, 2), (8, 2), (11, 1), (12, 1)], "J0 factors")
    require(all(factor["polynomial"] is not None for factor in factors), "J0 polynomial custody")

    intersections = json.loads((HERE / "modal_f04_full_j_intersections_output.json").read_text())
    require(intersections["counts"] == {"FAIL": 0, "PASS": 8, "REMOTE_ERROR": 0, "TIMEOUT": 0}, "intersection counts")
    for row in intersections["results"]:
        terminal = done(row)
        require(terminal is not None, "intersection done")
        require((terminal["localizer_nilpotence_index"] is None) == (row["j_factor_index"] == 2), "J factor route")

    j1 = json.loads((HERE / "modal_full_identity_single_c1_output.json").read_text())
    require(j1["coefficient_index"] == 1 and j1["results"][0]["coefficient_index"] == 1, "J1 task data")
    j1_factors = done(j1["results"][0])["identities"]["J"]["descended_factors"]
    require([(factor["metric"]["degree"], factor["metric"]["terms"]) for factor in j1_factors] == [(1, 1), (70, 182336)], "J1 fence")

    i0 = json.loads((HERE / "modal_full_identity_single_i_c0_output.json").read_text())
    require(i0["counts"]["TIMEOUT"] == 1 and i0["results"][0]["status"] == "TIMEOUT", "I0 fence")
    full_product = json.loads((HERE / "modal_full_identity_representatives_output.json").read_text())
    require(full_product["counts"]["TIMEOUT"] == 2, "full-product fence")

    quotient = json.loads((HERE / "modal_quotient_full_j_output.json").read_text())
    require(quotient["counts"] == {"FAIL": 0, "PASS": 0, "REMOTE_ERROR": 0, "TIMEOUT": 2}, "quotient fence")
    require(
        [[record["phase"] for record in row["records"]] for row in quotient["results"]]
        == [["START", "BASE_GROEBNER_BEGIN", "BASE_GROEBNER_DONE"], ["START", "BASE_GROEBNER_BEGIN"]],
        "quotient phases",
    )
    quadratic = json.loads((HERE / "modal_quadratic_quotient_full_j_r02_output.json").read_text())
    require(quadratic["counts"] == {"FAIL": 0, "PASS": 0, "REMOTE_ERROR": 0, "TIMEOUT": 1}, "quadratic quotient fence")
    require(
        [record["phase"] for record in quadratic["results"][0]["records"]]
        == ["START", "BASE_GROEBNER_BEGIN", "BASE_GROEBNER_DONE"],
        "quadratic quotient phases",
    )
    print("KB_C2_112_FIXED_R02_R20_GENERIC_ROUTE_PASS reps=4 cubic=8 timeout=4 j_intersections=8 quotient_fences=3")


if __name__ == "__main__":
    main()
