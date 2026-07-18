#!/usr/bin/env python3
"""Emit exact rate-half list certificates on the proved B*=1,2 branches."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from prize_certificate_compiler import SCHEMA as COMPILER_SCHEMA
from prize_certificate_compiler import compile_certificate
from prize_row_descriptor import INPUT_SCHEMA as ROW_INPUT_SCHEMA
from prize_row_descriptor import describe_row


OUTPUT_SCHEMA = "rate-half-list-low-budget-certificate-v1"
SUPPORTED_OBJECTS = {"LIST", "INTERLEAVED_LIST"}
ROW_KEYS = {"schema", "p", "extension_degree", "subgroup_log2", "rate"}
AXES = (
    "object_identity",
    "field_scope",
    "denominator",
    "endpoint",
)


def canonical_descriptor(row_source: Any) -> dict[str, Any]:
    if not isinstance(row_source, dict):
        raise ValueError("row input must be an object")
    unknown = set(row_source) - ROW_KEYS
    missing = ROW_KEYS - set(row_source)
    if unknown:
        raise ValueError(f"unknown row-input fields: {sorted(unknown)}")
    if missing:
        raise ValueError(f"missing row-input fields: {sorted(missing)}")
    if row_source.get("schema") != ROW_INPUT_SCHEMA:
        raise ValueError(f"row schema must be {ROW_INPUT_SCHEMA}")
    return describe_row(row_source)


def generate_certificate(row_source: Any, object_name: str) -> dict[str, Any]:
    if object_name not in SUPPORTED_OBJECTS:
        raise ValueError(f"object must be one of {sorted(SUPPORTED_OBJECTS)}")

    descriptor = canonical_descriptor(row_source)
    if descriptor["code"]["rate"] != "1/2":
        raise ValueError("the low-budget theorem requires rate 1/2")

    n = int(descriptor["evaluation_domain"]["order_decimal"])
    k = int(descriptor["code"]["dimension_decimal"])
    budget = int(descriptor["target"]["B_star_decimal"])
    if n % 4:
        raise ValueError("the low-budget theorem requires evaluation order divisible by 4")
    if k != n // 2:
        raise ValueError("the low-budget theorem requires k=n/2")
    if budget not in {1, 2}:
        raise ValueError("the proved certificate generator requires B*=1 or B*=2")

    if object_name == "LIST":
        claim_id = "rate_half_list_low_budget_exact_crossing"
        arity_scope: dict[str, Any] = {"kind": "fixed", "value": 1}
    else:
        claim_id = "rate_half_list_low_budget_all_arity_crossing"
        arity_scope = {"kind": "all_positive_integers"}

    safe_agreement = 3 * n // 4
    unsafe_agreement = safe_agreement - 1
    compiler_input = {
        "schema": COMPILER_SCHEMA,
        "object": object_name,
        "row_descriptor": descriptor,
        "axes": [{"id": axis, "status": "PROVED"} for axis in AXES],
        "cells": [
            {
                "agreement": unsafe_agreement,
                "lower": {
                    "count": budget + 1,
                    "status": "PROVED",
                    "claim_ids": [claim_id],
                },
            },
            {
                "agreement": safe_agreement,
                "upper": {
                    "count": budget,
                    "status": "PROVED",
                    "claim_ids": [claim_id],
                },
            },
        ],
    }
    compiler_output = compile_certificate(compiler_input)
    expected_certificate = {
        "unsafe_agreement": unsafe_agreement,
        "safe_agreement": safe_agreement,
        "largest_safe_closed_radius": {"numerator": n // 4, "denominator": n},
        "closed_ball_boundary_supremum": {
            "numerator": n // 4 + 1,
            "denominator": n,
            "attained": False,
        },
    }
    if (
        compiler_output["status"] != "CERTIFIED_ADJACENT_CROSSING"
        or not compiler_output["prize_facing"]
        or compiler_output["certificate"] != expected_certificate
    ):
        raise RuntimeError("the compiler did not reproduce the proved adjacent crossing")

    return {
        "schema": OUTPUT_SCHEMA,
        "status": compiler_output["status"],
        "prize_facing": True,
        "scope": {
            "object": object_name,
            "arity": arity_scope,
            "rate": "1/2",
            "B_star": str(budget),
        },
        "theorem_packet": {
            "claim_id": claim_id,
            "status": "PROVED",
            "safe_agreement": safe_agreement,
            "unsafe_agreement": unsafe_agreement,
        },
        "external_preconditions": descriptor["external_preconditions"],
        "row_descriptor": descriptor,
        "compiler_input": compiler_input,
        "compiler_output": compiler_output,
        "certificate": expected_certificate,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="canonical prize-row-input-v1 JSON")
    parser.add_argument("--object", required=True, choices=sorted(SUPPORTED_OBJECTS))
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    result = generate_certificate(json.loads(args.input.read_text()), args.object)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
