#!/usr/bin/env python3
"""Verify the exact profile-(2,10) payment and residual E1 ledger."""

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
NODE = "e1_profile210_exact_weighted_payment"
TARGET = "e1_official_low_square_mass_pair_budget"
PRIOR_RESIDUAL = 64417827807586372161179904588832830040487
M210 = 1227527050040565145269313275179180544
ORIENTED_VECTORS = 68096
EXPECTED_CHARGE = 41794840999781162066129578393300739162112
EXPECTED_RESIDUAL = 22622986807805210095050326195532090878375
EXPECTED_NEXT = (1154418456451360735963226152798543872, 1, 14, 18)
EXPECTED_CAP = 39193


def load_dictionary():
    digest = sha256(DICTIONARY_PATH.read_bytes()).hexdigest()
    if digest != EXPECTED_DICTIONARY_SHA256:
        raise RuntimeError(f"dictionary verifier hash drift: {digest}")
    spec = importlib.util.spec_from_file_location("e1_profile210_dictionary", DICTIONARY_PATH)
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
            if not ((b > 0 and square_mass >= 18) or (b == 0 and a >= 15)):
                continue
            weight = dictionary.multiplicity(h, ell, a, b)
            if weight:
                profiles.append((weight, a, b, square_mass))
    profiles.sort(reverse=True)
    if len(profiles) != 271:
        raise RuntimeError("eligible profile count drift")
    if profiles[0][1:] != (4, 2, 18):
        raise RuntimeError("empty maximum profile drift")
    if profiles[1][1:] != (3, 6, 18) or profiles[2][1:] != (2, 10, 18):
        raise RuntimeError("paid profile ordering drift")
    if profiles[2][0] != M210 or profiles[3] != EXPECTED_NEXT:
        raise RuntimeError("next profile ordering drift")

    if ORIENTED_VECTORS != 256 * 266:
        raise RuntimeError("oriented-vector envelope drift")
    charge = M210 * ORIENTED_VECTORS // 2
    residual = PRIOR_RESIDUAL - charge
    if charge != EXPECTED_CHARGE or residual != EXPECTED_RESIDUAL:
        raise RuntimeError("exact profile payment drift")
    next_weight = EXPECTED_NEXT[0]
    cap = 2 * residual // next_weight
    if cap != EXPECTED_CAP:
        raise RuntimeError("residual cap drift")
    if not next_weight * cap <= 2 * residual < next_weight * (cap + 1):
        raise RuntimeError("residual cap boundary failed")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    suppliers = (
        "e1_profile36_exact_weighted_payment",
        "e1_low_square_mass_weighted_kernel_dictionary",
        "e1_profile210_split_prime_ideal_router",
        "e1_profile210_m1538_collision_exclusion",
    )
    if nodes[NODE]["status"] != "PROVED" or nodes[TARGET]["status"] != "TARGET":
        raise RuntimeError("DAG status drift")
    for supplier in suppliers:
        if nodes[supplier]["status"] != "PROVED":
            raise RuntimeError(f"supplier status drift: {supplier}")
        if (supplier, NODE, "req") not in edges:
            raise RuntimeError(f"missing supplier edge: {supplier}")
    if (NODE, TARGET, "ev") not in edges:
        raise RuntimeError("missing evidence edge")

    print(
        "E1_PROFILE210_EXACT_WEIGHTED_PAYMENT_PASS "
        f"charge={charge} residual={residual} "
        f"next_profile=1,14,18 residual_oriented_cap={cap}"
    )


if __name__ == "__main__":
    main()
