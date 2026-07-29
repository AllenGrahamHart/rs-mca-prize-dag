#!/usr/bin/env python3
"""Verify the conditional two-ideal profile-018 weighted payment."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_profile018_two_ideal_exact_weighted_payment"
CERT = "e1_qzeta128_p257_class_orbit_certificate"
DESCENT = "e1_profile018_qzeta128_class_descent_two_ideal_bound"
SUPPLIERS = {
    "e1_profile018_split_prime_payment_router",
    "e1_profile018_galois_norm_occupancy_dictionary",
    "e1_low_square_mass_weighted_kernel_dictionary",
}
TARGET = "e1_official_low_square_mass_pair_budget"

PURE_FAMILIES = 10
SPLIT_FAMILIES = 2
ORBIT_SIZE = 256
WEIGHT = 1_117_325_838_856_821_897_682_125_205_459_304_448
RESIDUAL_BEFORE = 2_231_339_193_048_374_054_995_899_432_498_611_923_367
NEXT_WEIGHT = 522_452_937_039_935_372_855_706_187_881_128_712


def main() -> None:
    family_cap = PURE_FAMILIES + SPLIT_FAMILIES
    vector_cap = ORBIT_SIZE * family_cap
    charge = WEIGHT * vector_cap // 2
    residual = RESIDUAL_BEFORE - charge
    next_cap, remainder = divmod(2 * residual, NEXT_WEIGHT)

    assert family_cap == 12
    assert vector_cap == 3_072
    assert charge == 1_716_212_488_484_078_434_839_744_315_585_491_632_128
    assert residual == 515_126_704_564_295_620_156_155_116_913_120_291_239
    assert next_cap == 1_971
    assert remainder == 498_670_222_878_620_413_713_337_512_535_891_126
    assert NEXT_WEIGHT - remainder == 23_782_714_161_314_959_142_368_675_345_237_586
    assert 7 * ORBIT_SIZE <= next_cap < 8 * ORBIT_SIZE

    node_dir = ROOT / "background/nodes" / NODE
    statement = (node_dir / "statement.md").read_text()
    proof = (node_dir / "proof.md").read_text()
    for text in ("3072", "1971", CERT):
        assert text in statement
    for text in ("R_before", "M_next*1972", "23782714161314959142368675345237586"):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[CERT]["status"] == "TARGET"
    assert nodes[DESCENT]["status"] == "CONDITIONAL"
    assert nodes[NODE]["status"] == "CONDITIONAL"
    assert nodes[TARGET]["status"] == "TARGET"
    for supplier in SUPPLIERS:
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
    assert (DESCENT, NODE, "req") in edges
    assert (NODE, TARGET, "ev") in edges

    print(
        "E1_PROFILE018_TWO_IDEAL_EXACT_WEIGHTED_PAYMENT_PASS "
        f"conditional_on={CERT} vectors={vector_cap} residual={residual} "
        f"next_cap={next_cap} orbit_allowance={next_cap // ORBIT_SIZE}"
    )


if __name__ == "__main__":
    main()
