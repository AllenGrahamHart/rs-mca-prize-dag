#!/usr/bin/env python3
"""Compile exact staircase packets with fail-closed prize-facing semantics."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


SCHEMA = "prize-certificate-input-v1"
OUTPUT_SCHEMA = "prize-certificate-output-v1"
TRUSTED = "PROVED"
OBJECTS = {"MCA_FINITE_SLOPE", "MCA_PROJECTIVE_SLOPE", "LIST", "INTERLEAVED_LIST"}
REQUIRED_AXES = {"object_identity", "field_scope", "denominator", "endpoint"}


def exact_int(value: Any, label: str) -> int:
    if isinstance(value, bool):
        raise ValueError(f"{label} must be an integer")
    if isinstance(value, int):
        result = value
    elif isinstance(value, str) and value and value.lstrip("-").isdigit():
        result = int(value)
    else:
        raise ValueError(f"{label} must be a decimal integer")
    if result < 0:
        raise ValueError(f"{label} must be nonnegative")
    return result


def packet(packet: Any, label: str) -> dict[str, Any] | None:
    if packet is None:
        return None
    if not isinstance(packet, dict):
        raise ValueError(f"{label} must be an object")
    status = packet.get("status")
    if not isinstance(status, str):
        raise ValueError(f"{label}.status must be a string")
    claims = packet.get("claim_ids", [])
    if not isinstance(claims, list) or not all(isinstance(item, str) for item in claims):
        raise ValueError(f"{label}.claim_ids must be a string list")
    return {
        "count": exact_int(packet.get("count"), f"{label}.count"),
        "status": status,
        "claim_ids": claims,
    }


def classify_cell(cell: dict[str, Any], threshold: int) -> dict[str, Any]:
    agreement = exact_int(cell.get("agreement"), "agreement")
    upper = packet(cell.get("upper"), f"cell[{agreement}].upper")
    lower = packet(cell.get("lower"), f"cell[{agreement}].lower")

    proved_safe = upper is not None and upper["status"] == TRUSTED and upper["count"] <= threshold
    proved_unsafe = lower is not None and lower["status"] == TRUSTED and lower["count"] > threshold
    if proved_safe and proved_unsafe:
        raise ValueError(f"contradictory proved packets at agreement {agreement}")

    conditional_reasons: list[str] = []
    if upper is not None and upper["count"] <= threshold and upper["status"] != TRUSTED:
        conditional_reasons.extend(upper["claim_ids"] or [f"upper:{upper['status']}"])
    if lower is not None and lower["count"] > threshold and lower["status"] != TRUSTED:
        conditional_reasons.extend(lower["claim_ids"] or [f"lower:{lower['status']}"])

    if proved_safe:
        verdict = "SAFE"
    elif proved_unsafe:
        verdict = "UNSAFE"
    elif conditional_reasons:
        verdict = "CONDITIONAL"
    else:
        verdict = "UNKNOWN"
    return {
        "agreement": agreement,
        "verdict": verdict,
        "upper": upper,
        "lower": lower,
        "conditional_on": sorted(set(conditional_reasons)),
    }


def compile_certificate(source: dict[str, Any]) -> dict[str, Any]:
    if source.get("schema") != SCHEMA:
        raise ValueError(f"schema must be {SCHEMA}")
    epsilon_bits = exact_int(source.get("epsilon_bits"), "epsilon_bits")
    if epsilon_bits != 128:
        raise ValueError("the official compiler requires epsilon_bits=128")
    denominator = exact_int(source.get("denominator"), "denominator")
    if denominator == 0:
        raise ValueError("denominator must be positive")
    n = exact_int(source.get("n"), "n")
    k = exact_int(source.get("k"), "k")
    if not 0 < k < n:
        raise ValueError("need 0<k<n")
    threshold = denominator // (1 << epsilon_bits)

    object_name = source.get("object")
    if object_name not in OBJECTS:
        raise ValueError(f"object must be one of {sorted(OBJECTS)}")
    axes = source.get("axes")
    if not isinstance(axes, list) or not axes:
        raise ValueError("axes must be a nonempty list")
    open_axes = []
    axis_ids = set()
    for axis in axes:
        if not isinstance(axis, dict) or not isinstance(axis.get("id"), str):
            raise ValueError("every axis needs a string id")
        if axis["id"] in axis_ids:
            raise ValueError(f"duplicate axis: {axis['id']}")
        axis_ids.add(axis["id"])
        if axis.get("status") != TRUSTED:
            open_axes.append(axis["id"])
    missing_axes = REQUIRED_AXES - axis_ids
    if missing_axes:
        raise ValueError(f"missing required axes: {sorted(missing_axes)}")

    raw_cells = source.get("cells")
    if not isinstance(raw_cells, list) or not raw_cells:
        raise ValueError("cells must be a nonempty list")
    cells = sorted((classify_cell(cell, threshold) for cell in raw_cells), key=lambda row: row["agreement"])
    agreements = [cell["agreement"] for cell in cells]
    if len(set(agreements)) != len(agreements):
        raise ValueError("agreements must be unique")
    if agreements[0] < 0 or agreements[-1] > n:
        raise ValueError("agreement outside [0,n]")

    seen_safe = False
    for cell in cells:
        if cell["verdict"] == "SAFE":
            seen_safe = True
        elif seen_safe and cell["verdict"] == "UNSAFE":
            raise ValueError("proved verdicts violate agreement monotonicity")

    conditional_claims = sorted({claim for cell in cells for claim in cell["conditional_on"]})
    crossings = []
    by_agreement = {cell["agreement"]: cell for cell in cells}
    for agreement, cell in by_agreement.items():
        next_cell = by_agreement.get(agreement + 1)
        if cell["verdict"] == "UNSAFE" and next_cell and next_cell["verdict"] == "SAFE":
            safe_agreement = agreement + 1
            crossings.append(
                {
                    "unsafe_agreement": agreement,
                    "safe_agreement": safe_agreement,
                    "largest_safe_closed_radius": {
                        "numerator": n - safe_agreement,
                        "denominator": n,
                    },
                    "closed_ball_boundary_supremum": {
                        "numerator": n - agreement,
                        "denominator": n,
                        "attained": False,
                    },
                }
            )

    prize_facing = not open_axes and not conditional_claims and len(crossings) == 1
    if open_axes:
        status = "REFUSED_OPEN_AXES"
    elif conditional_claims:
        status = "REFUSED_CONJECTURAL_LEDGER"
    elif len(crossings) == 0:
        status = "UNKNOWN_NO_ADJACENT_CROSSING"
    elif len(crossings) > 1:
        status = "REFUSED_AMBIGUOUS_CROSSING"
    else:
        status = "CERTIFIED_ADJACENT_CROSSING"

    return {
        "schema": OUTPUT_SCHEMA,
        "status": status,
        "prize_facing": prize_facing,
        "object": object_name,
        "n": n,
        "k": k,
        "denominator": str(denominator),
        "B_star": str(threshold),
        "open_axes": sorted(open_axes),
        "conditional_claims": conditional_claims,
        "cells": cells,
        "certificate": crossings[0] if prize_facing else None,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    result = compile_certificate(json.loads(args.input.read_text()))
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")
    return 0 if result["prize_facing"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
