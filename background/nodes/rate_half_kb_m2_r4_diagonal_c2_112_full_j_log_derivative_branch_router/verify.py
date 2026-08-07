#!/usr/bin/env python3
"""Verify the full-J logarithmic-derivative branch router."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE_OUTPUT = HERE.parent / (
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_r20_"
    "quadratic_branch_reduction/modal_log_derivative_j_f04_output.json"
)
SOURCE_SHA256 = "58a53a4cf44ee8a030e78753900cd31d8d1f21eec957495bfbd0af56df99a98f"
QUOTIENT_OUTPUT = HERE.parent / (
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_r20_"
    "quadratic_branch_reduction/"
    "modal_quadratic_quotient_full_j_log_derivative_r02_output.json"
)
QUOTIENT_SHA256 = "8a150098f20b68f91c5509a50e01d2a712312f4ca595e7de0e0994e85e5d9204"
CACHE_OUTPUTS = {
    HERE / "modal_contribution_cache_r02_output.json": (
        "58242c442a6dbb821f3245c828ec23d9058fd18ec75b4c3ecb23c062b0c72001",
        {"FAIL": 0, "PASS": 7, "REMOTE_ERROR": 0, "TIMEOUT": 6},
        set(range(6, 13)),
    ),
    HERE / "modal_contribution_cache_r02_observed_output.json": (
        "465125f24313440a5f690b50a822a18b962499a62aa0bb2e1f3cb6d15fc7a36a",
        {"FAIL": 0, "PASS": 2, "REMOTE_ERROR": 0, "TIMEOUT": 4},
        {2, 3},
    ),
    HERE / "modal_contribution_cache_r02_slow_output.json": (
        "6c5a3827e60b5fef2394fa9f492f7952bfe9809884619340d22d4fdedb6a6477",
        {"FAIL": 0, "PASS": 0, "REMOTE_ERROR": 0, "TIMEOUT": 4},
        set(),
    ),
}


def main() -> None:
    source_raw = SOURCE_OUTPUT.read_bytes()
    assert hashlib.sha256(source_raw).hexdigest() == SOURCE_SHA256
    source = json.loads(source_raw)
    assert source["counts"] == {
        "FAIL": 0,
        "PASS": 1,
        "REMOTE_ERROR": 0,
        "TIMEOUT": 0,
    }
    row = source["results"][0]
    assert row["status"] == "PASS" and row["assignment"] == "F04"
    compiled = next(
        record
        for record in row["records"]
        if record["phase"] == "LOG_DERIVATIVE_COMPILED"
    )
    assert compiled["raw_numerator"] == {
        "degree": 89,
        "degrees": [34, 25, 25, 15],
        "sha256": "588f5710ed373635173a5dcc0df2d404c3da30940efd61146d322b405ca522d1",
        "terms": 311837,
    }
    assert compiled["descended"] == {
        "degree": 67,
        "degrees": [34, 24, 24, 15],
        "sha256": "57f0d18de937af8c9bebb7e59b079861571ecd9cdf156f3fa4d0ab574331437e",
        "terms": 162322,
    }
    factors = compiled["denominator_factors"]
    assert [factor["metric"]["degree"] for factor in factors] == [
        1,
        1,
        4,
        5,
        7,
        7,
        11,
        11,
    ]
    assert [factor["named_unit"] for factor in factors] == [
        True,
        True,
        True,
        True,
        False,
        False,
        False,
        False,
    ]
    assert [factor["exponent"] for factor in factors[4:]] == [2, 2, 2, 2]
    done = next(record for record in row["records"] if record["phase"] == "DONE")
    assert not done["denominator_all_named"]
    assert len(done["factors"]) == 1
    assert done["factors"][0]["metric"] == {
        "degree": 67,
        "degrees": [34, 24, 24, 15],
        "sha256": "73fbe05427ffc5723871c21b9fc5479f7f671d6f62cd131eeaffa324d7d83713",
        "terms": 162322,
    }

    quotient_raw = QUOTIENT_OUTPUT.read_bytes()
    assert hashlib.sha256(quotient_raw).hexdigest() == QUOTIENT_SHA256
    quotient = json.loads(quotient_raw)
    assert quotient["counts"] == {
        "FAIL": 0,
        "PASS": 0,
        "REMOTE_ERROR": 0,
        "TIMEOUT": 1,
    }
    quotient_row = quotient["results"][0]
    assert quotient_row["status"] == "TIMEOUT"
    base = next(
        record
        for record in quotient_row["records"]
        if record["phase"] == "BASE_GROEBNER_DONE"
    )
    assert (base["basis_size"], base["dimension"]) == (36, 1)
    assert not any(
        record["phase"] == "LOG_DERIVATIVE_MAPPED"
        for record in quotient_row["records"]
    )
    for path, (expected_hash, expected_counts, pass_indices) in CACHE_OUTPUTS.items():
        cache_raw = path.read_bytes()
        assert hashlib.sha256(cache_raw).hexdigest() == expected_hash
        cache = json.loads(cache_raw)
        assert cache["counts"] == expected_counts
        assert {
            cache_row["contribution_index"]
            for cache_row in cache["results"]
            if cache_row["status"] == "PASS"
        } == pass_indices
        assert all(
            cache_row["status"] in {"PASS", "TIMEOUT"}
            for cache_row in cache["results"]
        )
    print(
        "KB_C2_112_FULL_J_LOG_DERIVATIVE_ROUTER_PASS "
        "numerator_degree=67 denominator_branches=7,7,11,11"
    )


if __name__ == "__main__":
    main()
