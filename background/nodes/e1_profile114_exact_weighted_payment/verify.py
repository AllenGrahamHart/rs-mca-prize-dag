#!/usr/bin/env python3
"""Verify the exact profile-(1,14) payment and residual E1 ledger."""

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
NODE = "e1_profile114_exact_weighted_payment"
TARGET = "e1_official_low_square_mass_pair_budget"
PRIOR_RESIDUAL = 22622986807805210095050326195532090878375
M114 = 1154418456451360735963226152798543872
ORIENTED_VECTORS = 35328
EXPECTED_CHARGE = 20391647614756836040054426763033478955008
EXPECTED_RESIDUAL = 2231339193048374054995899432498611923367
EXPECTED_NEXT = (1117325838856821897682125205459304448, 0, 18, 18)
EXPECTED_CAP = 3994


def load_dictionary():
    digest = sha256(DICTIONARY_PATH.read_bytes()).hexdigest()
    if digest != EXPECTED_DICTIONARY_SHA256:
        raise RuntimeError(f"dictionary verifier hash drift: {digest}")
    spec = importlib.util.spec_from_file_location("e1_profile114_payment_dictionary", DICTIONARY_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load dictionary verifier")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    dictionary = load_dictionary()
    profiles = []
    for a in range(129):
        for b in range(129 - a):
            square_mass = 4 * a + b
            if not 0 < square_mass <= 66:
                continue
            if not ((b > 0 and square_mass >= 18) or (b == 0 and a >= 15)):
                continue
            weight = dictionary.multiplicity(128, 33, a, b)
            if weight:
                profiles.append((weight, a, b, square_mass))
    profiles.sort(reverse=True)
    if len(profiles) != 271:
        raise RuntimeError("eligible profile count drift")
    if profiles[3][1:] != (1, 14, 18) or profiles[3][0] != M114:
        raise RuntimeError("active profile ordering drift")
    if profiles[4] != EXPECTED_NEXT:
        raise RuntimeError("next profile ordering drift")

    if ORIENTED_VECTORS != 256 * (10 + 128):
        raise RuntimeError("oriented-vector envelope drift")
    charge = M114 * ORIENTED_VECTORS // 2
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
        "e1_profile210_exact_weighted_payment",
        "e1_low_square_mass_weighted_kernel_dictionary",
        "e1_profile114_split_prime_payment_router",
        "e1_s18_m1028_energy4_cubic_exclusion",
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
        "E1_PROFILE114_EXACT_WEIGHTED_PAYMENT_PASS "
        f"charge={charge} residual={residual} "
        f"next_profile=0,18,18 residual_oriented_cap={cap}"
    )


if __name__ == "__main__":
    main()
