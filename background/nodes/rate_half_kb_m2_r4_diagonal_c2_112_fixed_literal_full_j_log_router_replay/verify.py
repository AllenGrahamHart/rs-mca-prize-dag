#!/usr/bin/env python3
"""Verify the literal F05--F07 full-J/logarithmic router replay."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROUTER = HERE.parent / "rate_half_kb_m2_r4_diagonal_c2_112_full_j_log_derivative_branch_router"
FULL = ROUTER / "modal_full_identity_literal_replay_output.json"
LOG = ROUTER / "modal_log_derivative_literal_replay_output.json"
FULL_SHA256 = "9947669bfc40766d351dffde93e45414326dad36bf3b9643c2d09553dc1aa035"
LOG_SHA256 = "a575ff83ef4a8cb35a356c910d13665daf1d14103e8e9ef3729d54b093424baa"
ASSIGNMENTS = {"F05", "F06", "F07"}


def done(row: dict[str, object]) -> dict[str, object]:
    return next(record for record in row["records"] if record["phase"] == "DONE")


def main() -> None:
    assert hashlib.sha256(FULL.read_bytes()).hexdigest() == FULL_SHA256
    assert hashlib.sha256(LOG.read_bytes()).hexdigest() == LOG_SHA256
    full = json.loads(FULL.read_text())
    log = json.loads(LOG.read_text())
    passed = {"FAIL": 0, "PASS": 3, "REMOTE_ERROR": 0, "TIMEOUT": 0}
    assert full["counts"] == passed and log["counts"] == passed
    assert {row["assignment"] for row in full["results"]} == ASSIGNMENTS
    assert {row["assignment"] for row in log["results"]} == ASSIGNMENTS
    for row in full["results"]:
        assert row["status"] == "PASS"
        terminal = done(row)
        assert terminal["assignment"] == row["assignment"]
        assert terminal["terminal"] == "FULL_IDENTITY_NECESSARY_COEFFICIENTS_COMPILED"
        factors = terminal["identities"]["J"]["descended_factors"]
        assert [(factor["metric"]["degree"], factor["exponent"]) for factor in factors] == [
            (1, 4),
            (8, 2),
            (8, 2),
            (11, 1),
            (12, 1),
        ]
        assert all(factor["polynomial"] is not None for factor in factors)
    for row in log["results"]:
        assert row["status"] == "PASS"
        compiled = next(
            record for record in row["records"] if record["phase"] == "LOG_DERIVATIVE_COMPILED"
        )
        assert compiled["expected_linear_factor_count"] == 24
        assert compiled["observed_factor_count"] == 6
        assert compiled["descended"]["degree"] == 67
        assert compiled["descended"]["degrees"] == [34, 24, 24, 15]
        assert compiled["descended"]["terms"] in (162321, 162322)
        nonnamed = [
            factor for factor in compiled["denominator_factors"] if not factor["named_unit"]
        ]
        assert [(factor["metric"]["degree"], factor["exponent"]) for factor in nonnamed] == [
            (7, 2),
            (7, 2),
            (11, 2),
            (11, 2),
        ]
        terminal = done(row)
        assert terminal["assignment"] == row["assignment"]
        assert terminal["terminal"] == "FULL_J_LOG_DERIVATIVE_NECESSARY_CONDITION_COMPILED"
        assert len(terminal["factors"]) == 1
        assert terminal["factors"][0]["metric"]["degree"] == 67
    print("KB_C2_112_FIXED_LITERAL_FULL_J_LOG_ROUTER_REPLAY_PASS assignments=3")


if __name__ == "__main__":
    main()
