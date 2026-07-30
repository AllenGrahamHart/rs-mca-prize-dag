#!/usr/bin/env python3
"""Verify the profile-(0,18) diagonal-Galois occupancy dictionary."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_profile018_galois_norm_occupancy_dictionary"
ROUTER = "e1_profile018_split_prime_payment_router"
IDEALS = "e1_profile210_split_prime_ideal_router"
OCCUPANCY = "e1_profile018_m514_five_ideal_occupancy"
TARGET = "e1_official_low_square_mass_pair_budget"


def inverse_odd(value: int) -> int:
    return pow(value, -1, 256)


def main() -> None:
    units = tuple(range(1, 256, 2))
    if len(units) != 128:
        raise RuntimeError("Galois group order drift")

    for base in (1, 3, 127, 255):
        orbit = {base * unit % 256 for unit in units}
        if orbit != set(units):
            raise RuntimeError(f"primitive-root regularity failed: {base}")

    relative_classes = set()
    for row_exponent in units:
        for split_exponent in units:
            relative_classes.add(split_exponent * inverse_odd(row_exponent) % 256)
    if relative_classes != set(units):
        raise RuntimeError("diagonal relative-class dictionary drift")
    for relative in units:
        fiber = {
            (row_exponent, relative * row_exponent % 256)
            for row_exponent in units
        }
        if len(fiber) != 128:
            raise RuntimeError("diagonal orbit size drift")
        for fixed_row in (1, 3, 127, 255):
            if sum(row == fixed_row for row, _ in fiber) != 1:
                raise RuntimeError("fixed-row fiber intersection drift")

    statement = (ROOT / "background/nodes" / NODE / "statement.md").read_text()
    proof = (ROOT / "background/nodes" / NODE / "proof.md").read_text()
    for text in ("O_514(p,r)", "exact norm", "independent"):
        if text not in statement:
            raise RuntimeError(f"statement pin missing: {text}")
    for text in ("regular", "exactly once", "injective"):
        if text not in proof:
            raise RuntimeError(f"proof pin missing: {text}")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    if nodes[NODE]["status"] != "PROVED":
        raise RuntimeError("dictionary status drift")
    if nodes[OCCUPANCY]["status"] != "PROVED" or nodes[TARGET]["status"] != "TARGET":
        raise RuntimeError("target status drift")
    for supplier in (ROUTER, IDEALS):
        if nodes[supplier]["status"] != "PROVED":
            raise RuntimeError(f"supplier status drift: {supplier}")
        if (supplier, NODE, "req") not in edges:
            raise RuntimeError(f"missing supplier edge: {supplier}")
    if (NODE, OCCUPANCY, "ev") not in edges or (NODE, TARGET, "ev") not in edges:
        raise RuntimeError("dictionary output edge drift")

    print(
        "E1_PROFILE018_GALOIS_NORM_OCCUPANCY_DICTIONARY_PASS "
        f"group_order={len(units)} relative_classes={len(relative_classes)}"
    )


if __name__ == "__main__":
    main()
