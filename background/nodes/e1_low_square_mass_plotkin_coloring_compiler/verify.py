#!/usr/bin/env python3
"""Verify the exact E1 low-square-mass Plotkin/coloring compiler."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_low_square_mass_plotkin_coloring_compiler"
TARGET = "e1_official_low_square_mass_collision_coloring"
PAIR_TARGET = "e1_official_low_square_mass_pair_budget"

ROWS = (
    ("RowC 1/4", 256, 65,
     1146852336572689151906730465296195854216377730651578907904,
     5316911983139663491615228241121378304,
     3268165922105543787, 215698950858965889942,
     5316911983139663491945071196031276118, 116,
     2132541774042092125849554674828524585055987163412031204420185928301781984965),
    ("RowC 1/8", 256, 33,
     38001322036274275320505631960233903602944,
     5316911983139663491615228241121378304,
     210, 7140, 5322314010682671613516194952413711990, 52,
     5198328219133082279450279571536097879858211),
    ("RowC 1/16", 512, 33,
     3413962861332812601133559951042096138635313539480064,
     5316911983139663491615228241121378304,
     18885148505476, 642095049186184,
     5316911983139880370678024748494484621, 64,
     34251385177613611176287134568778412711317979539714751534312745145),
    ("prize 1/4", 256, 65,
     1146852336572689151906730465296195854216377730651578907904,
     317494674775468773183020924238786383963,
     54730211038721500, 3612193928555619000,
     317494674775468776604028242834763517703, 116,
     35712526268255974159379339912208386438781917770706964119574629107623252261),
    ("prize 1/8", 256, 33,
     38001322036274275320505631960233903602944,
     317494674775468773183020924238786383963,
     3, 102, 372561980747787012946133646668959839245, 52,
     62622678770648913918718317914905517790930),
    ("prize 1/16", 512, 33,
     3413962861332812601133559951042096138635313539480064,
     317494674775468773183020924238786383963,
     316259390691, 10752819283494,
     317494674775514892450411471699202449213, 64,
     573589463880641840437695913758879780711186889526196156445743653),
)


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    checks = 0

    for (name, N, ell, K, budget, expected_c, expected_cap, expected_floor,
         expected_C, expected_edges) in ROWS:
        c_max = (K - 1) // (budget * (ell + 1))
        cap = c_max * (ell + 1)
        image_floor = ceil_div(K, cap)
        assert c_max == expected_c, name
        assert cap == expected_cap, name
        assert image_floor == expected_floor, name
        assert cap * budget < K, name
        assert (c_max + 1) * (ell + 1) * budget >= K, name
        assert image_floor > budget, name
        d0 = 16 if N == 256 else 4
        C = 2 * ell + 2 - d0
        edge_cap = (K * K - 1 - budget * (ell + 1) * K) // (budget * C)
        denominator = (ell + 1) * K + C * edge_cap
        edge_image_floor = ceil_div(K * K, denominator)
        assert C == expected_C, name
        assert edge_cap == expected_edges, name
        assert budget * denominator < K * K, name
        assert budget * (denominator + C) >= K * K, name
        assert edge_image_floor == budget + 1, name
        checks += 11

    # Symbolic Plotkin rearrangement for a range containing both official ell.
    for ell in range(1, 80):
        for M in range(ell + 2, ell + 30):
            lower = Fraction(M * (M - 1), 2) * (2 * ell + 2)
            upper = M * M * ell
            assert lower > upper
            checks += 1

    pins = json.loads((Path(__file__).with_name("source_pin.json")).read_text())
    for file_key, hash_key in (
        ("square_mass_statement_file", "square_mass_statement_sha256"),
        ("allowance_statement_file", "allowance_statement_sha256"),
        ("class_count_proof_file", "class_count_proof_sha256"),
        ("norm_radius_statement_file", "norm_radius_statement_sha256"),
    ):
        assert sha256(ROOT / pins[file_key]) == pins[hash_key]
        checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[TARGET]["status"] == "TARGET"
    assert nodes[PAIR_TARGET]["status"] == "TARGET"
    for supplier in ("acl_count", "e1_clean_anchor_exact_collision_allowance",
                     "e1_collision_square_mass_reparametrization",
                     "e1_prime_field_l2_norm_collision_radius"):
        assert (supplier, NODE, "req") in edges
        checks += 1
    assert (NODE, TARGET, "ev") in edges
    assert (NODE, TARGET, "req") not in edges
    assert (TARGET, "unsafe_crossing_family_instantiation", "ev") in edges
    assert (NODE, PAIR_TARGET, "ev") in edges
    assert (NODE, PAIR_TARGET, "req") not in edges
    assert (PAIR_TARGET, "unsafe_crossing_family_instantiation", "ev") in edges
    checks += 9

    print(
        "E1_LOW_SQUARE_MASS_PLOTKIN_COLORING_COMPILER_PASS "
        f"rows={len(ROWS)} tight_colors=3 tight_fiber_cap=102 "
        "tight_edge_ratio_lt=1.648 checks=" + str(checks)
    )


if __name__ == "__main__":
    main()
