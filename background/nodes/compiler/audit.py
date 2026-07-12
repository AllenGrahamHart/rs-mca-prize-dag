#!/usr/bin/env python3
"""Independent behavior audit for the prize certificate compiler."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from prize_certificate_compiler import compile_certificate  # noqa: E402


def fixture() -> dict:
    return {
        "schema": "prize-certificate-input-v1",
        "object": "MCA_FINITE_SLOPE",
        "epsilon_bits": 128,
        "denominator": str(17**32),
        "n": 512,
        "k": 256,
        "axes": [
            {"id": "object_identity", "status": "PROVED"},
            {"id": "field_scope", "status": "PROVED"},
            {"id": "denominator", "status": "PROVED"},
            {"id": "endpoint", "status": "PROVED"},
        ],
        "cells": [
            {"agreement": 506, "lower": {"count": 7, "status": "PROVED"}},
            {"agreement": 507, "upper": {"count": 6, "status": "PROVED"}},
        ],
    }


def expect_error(source: dict) -> None:
    try:
        compile_certificate(source)
    except ValueError:
        return
    raise AssertionError("invalid compiler input was accepted")


def main() -> None:
    result = compile_certificate(fixture())
    assert result["status"] == "CERTIFIED_ADJACENT_CROSSING"
    assert result["prize_facing"]
    assert result["B_star"] == "6"
    cert = result["certificate"]
    assert cert["largest_safe_closed_radius"] == {"numerator": 5, "denominator": 512}
    assert cert["closed_ball_boundary_supremum"] == {
        "numerator": 6,
        "denominator": 512,
        "attained": False,
    }

    source = fixture()
    source["axes"][0]["status"] = "OPEN"
    assert compile_certificate(source)["status"] == "REFUSED_OPEN_AXES"

    source = fixture()
    source["cells"][1]["upper"]["status"] = "CONDITIONAL"
    source["cells"][1]["upper"]["claim_ids"] = ["open_upper"]
    assert compile_certificate(source)["status"] == "REFUSED_CONJECTURAL_LEDGER"

    source = fixture()
    source["cells"][1]["agreement"] = 508
    assert compile_certificate(source)["status"] == "UNKNOWN_NO_ADJACENT_CROSSING"

    source = fixture()
    source["cells"][0]["upper"] = {"count": 6, "status": "PROVED"}
    expect_error(source)

    source = fixture()
    source["epsilon_bits"] = 127
    expect_error(source)

    source = fixture()
    source["axes"] = source["axes"][:-1]
    expect_error(source)

    source = fixture()
    source["cells"][0]["agreement"] = 508
    expect_error(source)

    print("PRIZE_CERTIFICATE_COMPILER_PASS positive=1 refusal_mutations=7")


if __name__ == "__main__":
    main()
