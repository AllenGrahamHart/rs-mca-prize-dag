#!/usr/bin/env python3
"""Verify the exact profile-(3,6) payment and residual E1 ledger."""

from __future__ import annotations

from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
DICTIONARY_PATH = (
    ROOT / "background/nodes/e1_low_square_mass_weighted_kernel_dictionary/verify.py"
)
EXPECTED_DICTIONARY_SHA256 = (
    "e2dbf6100547365b4b686e51269e9af601f5b5dfa776fbd9e0c2eb20faffacb1"
)
NODE = "e1_profile36_exact_weighted_payment"
TARGET = "e1_official_low_square_mass_pair_budget"
EDGE_CAP = 65127585921474870475467050631501738502567
M36 = 1386246316188473270092082114587711840
EXPECTED_CHARGE = 709758113888498314287146042668908462080
EXPECTED_RESIDUAL = 64417827807586372161179904588832830040487
EXPECTED_NEXT = (1227527050040565145269313275179180544, 2, 10, 18)
EXPECTED_CAP = 104955


def load_dictionary():
    digest = sha256(DICTIONARY_PATH.read_bytes()).hexdigest()
    if digest != EXPECTED_DICTIONARY_SHA256:
        raise RuntimeError(f"dictionary verifier hash drift: {digest}")
    spec = importlib.util.spec_from_file_location("e1_payment_dictionary", DICTIONARY_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load dictionary verifier")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    dictionary = load_dictionary()
    profiles = []
    h = 128
    ell = 33
    for a in range(h + 1):
        for b in range(h - a + 1):
            square_mass = 4 * a + b
            if not 0 < square_mass <= 2 * ell:
                continue
            if not (
                (b > 0 and square_mass >= 18)
                or (b == 0 and a >= 15)
            ):
                continue
            weight = dictionary.multiplicity(h, ell, a, b)
            if weight:
                profiles.append((weight, a, b, square_mass))

    profiles.sort(reverse=True)
    if len(profiles) != 271:
        raise RuntimeError(f"profile count drift: {len(profiles)}")
    if profiles[0][1:] != (4, 2, 18):
        raise RuntimeError(f"excluded maximum profile drift: {profiles[0]}")
    if profiles[1] != (M36, 3, 6, 18):
        raise RuntimeError(f"paid profile drift: {profiles[1]}")
    if profiles[2] != EXPECTED_NEXT:
        raise RuntimeError(f"next profile drift: {profiles[2]}")

    charge = 128 * M36 * 4
    residual = EDGE_CAP - charge
    if charge != EXPECTED_CHARGE or residual != EXPECTED_RESIDUAL:
        raise RuntimeError("exact payment drift")

    next_weight = EXPECTED_NEXT[0]
    cap = 2 * residual // next_weight
    if cap != EXPECTED_CAP:
        raise RuntimeError(f"residual cap drift: {cap}")
    if not next_weight * cap <= 2 * residual < next_weight * (cap + 1):
        raise RuntimeError("residual cap boundary failed")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]
    }
    if nodes[NODE]["status"] != "PROVED" or nodes[TARGET]["status"] != "TARGET":
        raise RuntimeError("DAG status drift")
    for supplier in (
        "e1_low_square_mass_weighted_kernel_dictionary",
        "e1_prize_n256_s18_profile_exclusion",
        "e1_high_cofactor_schinzel_height_collapse",
        "e1_cofactor2_smyth_height_collapse",
    ):
        if nodes[supplier]["status"] != "PROVED":
            raise RuntimeError(f"supplier status drift: {supplier}")
        if (supplier, NODE, "req") not in edges:
            raise RuntimeError(f"missing supplier edge: {supplier}")
    if (NODE, TARGET, "ev") not in edges:
        raise RuntimeError("missing evidence edge")

    print(
        "E1_PROFILE36_EXACT_WEIGHTED_PAYMENT_PASS "
        f"profiles={len(profiles)} charge={charge} residual={residual} "
        f"next_profile=2,10,18 residual_oriented_cap={cap}"
    )


if __name__ == "__main__":
    main()

