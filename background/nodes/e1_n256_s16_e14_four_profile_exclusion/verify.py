#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
NODE = "e1_n256_s16_e14_four_profile_exclusion"
DEPENDENCIES = {
    "e1_n256_s16_e14_profile_parity_light_reduction",
    "e1_n256_proper_conductor_collision_exclusion",
    "collision_norm_criterion",
    "e1_pair_feasible_prime_field_reduction",
}
TARGETS = {"e1_official_prime_exception_control", "unsafe_crossing_family_instantiation"}
MAXIMUM_NORM = 5848948255836721605243059534285585250067895734911016890819011517212606236162
MAXIMUM_ODD = 2924474127918360802621529767142792625033947867455508445409505758606303118081


def main() -> None:
    pin = json.loads((HERE / "source_pin.json").read_text())
    for key, value in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / value).read_bytes()).hexdigest() == pin[key + "_sha256"]
    census = json.loads((ROOT / pin["census_result_file"]).read_text())
    norm = json.loads((ROOT / pin["norm_result_file"]).read_text())
    candidates = json.loads((ROOT / pin["candidate_result_file"]).read_text())
    assert census["complete"]
    assert census["summary"]["profile_counts"] == [982, 714, 100, 40]
    assert census["summary"]["full_conductor_counts"] == [540, 184, 8, 4]
    assert census["summary"]["proper_conductor_counts"] == [442, 530, 92, 36]
    assert census["summary"]["collected_full_conductor"] == 736
    assert norm["complete"] and norm["agreement"]
    summary = norm["summary"]
    assert summary["vectors"] == 736 and summary["distinct_norms"] == 262
    assert summary["maximum_norm"] == MAXIMUM_NORM
    assert summary["maximum_norm_bits"] == 252
    assert summary["norms_at_or_above_2_250"] == 152
    assert summary["maximum_odd_part"] == MAXIMUM_ODD
    assert summary["maximum_odd_part_bits"] == 251
    assert summary["odd_parts_at_or_above_2_250"] == 6
    assert 2**250 <= MAXIMUM_ODD < 2**251
    assert candidates["complete"] and candidates["agreement"]
    assert candidates["summary"] == {
        "candidates": 6, "congruence_candidates": 6,
        "distinct_odd_parts": 3, "pair_feasible_prime_candidates": 0,
        "prime_candidates": 0,
    }
    assert all(2**250 <= int(row["odd_part"]) < 2**251 for row in candidates["candidates"])
    assert all(row["residue_mod_256"] == 1 for row in candidates["candidates"])
    assert all(row["is_prime"] is False for row in candidates["candidates"])
    markers = (
        (pin["census_checker_file"], "profile=1836 full=736 engines=2 mutations=1"),
        (pin["norm_checker_file"], "odd_hits=6 shortcut_below_2_250=0 engines=2 mutations=1"),
        (pin["candidate_checker_file"], "candidates=6 distinct=3 primes=0 congruent=6 eligible=0 engines=2 mutations=1"),
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
    print("E1_N256_S16_E14_FOUR_PROFILE_EXCLUSION_PASS "
          "templates=1321 vectors=26219123456 profile=1836 full=736 distinct=262 "
          "norm_hits=152 odd_hits=6 composite_candidates=3 engines=6 mutations=3")


if __name__ == "__main__":
    main()
