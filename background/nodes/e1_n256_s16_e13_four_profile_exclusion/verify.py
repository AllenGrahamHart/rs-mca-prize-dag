#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
NODE = "e1_n256_s16_e13_four_profile_exclusion"
DEPENDENCIES = {
    "e1_n256_s16_e13_profile_parity_light_reduction",
    "e1_n256_proper_conductor_collision_exclusion",
    "collision_norm_criterion",
    "e1_pair_feasible_prime_field_reduction",
}
TARGETS = {"e1_official_prime_exception_control", "unsafe_crossing_family_instantiation"}
MAXIMUM_NORM = 4937981356753691307652038461254907642619144628263052811320856547919621259264
MAXIMUM_ODD = 2099233185140600860850973089797376067771315496789913419840767568645748406017


def main() -> None:
    pin = json.loads((HERE / "source_pin.json").read_text())
    for key, value in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / value).read_bytes()).hexdigest() == pin[key + "_sha256"]
    census = json.loads((ROOT / pin["census_result_file"]).read_text())
    norm = json.loads((ROOT / pin["norm_result_file"]).read_text())
    candidates = json.loads((ROOT / pin["candidate_result_file"]).read_text())
    assert census["complete"]
    assert census["summary"]["profile_counts"] == [418, 252, 104, 46]
    assert census["summary"]["full_conductor_counts"] == [112, 0, 16, 8]
    assert census["summary"]["proper_conductor_counts"] == [306, 252, 88, 38]
    assert census["summary"]["collected_full_conductor"] == 136
    assert norm["complete"] and norm["agreement"]
    summary = norm["summary"]
    assert summary["vectors"] == 136 and summary["distinct_norms"] == 36
    assert summary["maximum_norm"] == MAXIMUM_NORM and summary["maximum_norm_bits"] == 252
    assert summary["norms_at_or_above_2_250"] == 112
    assert summary["maximum_odd_part"] == MAXIMUM_ODD and summary["maximum_odd_part_bits"] == 251
    assert summary["odd_parts_at_or_above_2_250"] == 4
    assert 2**250 <= MAXIMUM_ODD < 2**251
    assert candidates["complete"] and candidates["agreement"]
    assert candidates["summary"] == {
        "candidates": 4, "congruence_candidates": 4,
        "distinct_odd_parts": 2, "pair_feasible_prime_candidates": 0,
        "prime_candidates": 0,
    }
    assert all(2**250 <= int(row["odd_part"]) < 2**251 for row in candidates["candidates"])
    assert all(row["residue_mod_256"] == 1 for row in candidates["candidates"])
    assert all(row["is_prime"] is False for row in candidates["candidates"])
    markers = (
        (pin["census_checker_file"], "profile=820 full=136 engines=2 mutations=1"),
        (pin["norm_checker_file"], "odd_hits=4 engines=2 mutations=1"),
        (pin["candidate_checker_file"], "candidates=4 distinct=2 primes=0 congruent=4 eligible=0 engines=2 mutations=1"),
    )
    for path, marker in markers:
        run = subprocess.run([sys.executable, str(ROOT / path)], cwd=ROOT,
                             capture_output=True, text=True, timeout=30, check=True)
        assert marker in run.stdout
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert all(nodes[dependency]["status"] == "PROVED" for dependency in DEPENDENCIES)
    assert {source for source, target, kind in edges if target == NODE and kind == "req"} == DEPENDENCIES
    assert all((NODE, target, "ev") in edges for target in TARGETS)
    print("E1_N256_S16_E13_FOUR_PROFILE_EXCLUSION_PASS "
          "templates=111 vectors=2203120896 profile=820 full=136 distinct=36 "
          "norm_hits=112 odd_hits=4 composite_candidates=2 engines=6 mutations=3")


if __name__ == "__main__":
    main()
