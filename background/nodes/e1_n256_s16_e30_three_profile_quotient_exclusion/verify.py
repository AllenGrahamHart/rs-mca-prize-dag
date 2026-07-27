#!/usr/bin/env python3
"""Verify the E30 three-profile quotient exclusion."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e30_three_profile_quotient_exclusion"
REDUCTION = "e1_n256_s16_e30_profile_parity_light_reduction"
NORM = "collision_norm_criterion"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
CLOSED = ("0,3,2", "6,2,0,1", "3,0,3")
EXPECTED_PIN = {
    "base_census_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e34_nested_quotient_census.cpp",
    "base_census_file_sha256": "ccdcefeb71d7805183c763aca062fe4da6a86ff6ff542ab8a0200267021f69f4",
    "checker_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_eight_profile_quotient_probe_check.py",
    "checker_file_sha256": "157275395a2bf09c7c4a8e17f980fcd6faa17c0e23555b00b61cf9ef29f114e3",
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "launcher_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_eight_profile_quotient_probe_modal.py",
    "launcher_file_sha256": "13087c885fc72c901593cfe708704097458b98006e0184ddd4abe3fdf65bf033",
    "profile_reduction_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/statement.md",
    "profile_reduction_file_sha256": "7d988ae69d03e78167eea76ca9746782b35627bb9fde645a187a121ee291aef4",
    "result_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_eight_profile_quotient_probe_result.json",
    "result_file_sha256": "bf441e338cced58d72a8490dd08bd95cca08c2cc1ba1d23327d0dab837e27538",
    "wrapper_census_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_eight_profile_quotient_census.cpp",
    "wrapper_census_file_sha256": "ec5a71ea442bcbd96ab5109d8d6356989997a30083bc78230d7bdecb6a164e66",
}


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]

    checker_path = ROOT / pin["checker_file"]
    spec = importlib.util.spec_from_file_location("e30_quotient_checker", checker_path)
    assert spec is not None and spec.loader is not None
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    checker.main()

    packet = json.loads((ROOT / pin["result_file"]).read_text())
    assert packet["complete"] is True
    assert packet["completed_tasks"] == packet["expected_tasks"] == 128
    maxima = {
        profile: max(packet["summary"][profile][str(order)]["maximum"] for order in (128, 64))
        for profile in packet["profiles"]
    }
    assert {profile for profile, maximum in maxima.items() if maximum <= 1087} == set(CLOSED)
    assert {profile: maxima[profile] for profile in CLOSED} == {
        "0,3,2": 936,
        "6,2,0,1": 1058,
        "3,0,3": 1002,
    }
    assert sum(row["tested"] for row in packet["rows"]) == 24_124_690
    assert 44**32 < 2**250

    proof = Path(__file__).with_name("proof.md").read_text()
    assert "If `S_1` contains an odd distance" in proof
    assert "even but not contained in `4Z`" in proof
    assert "`S_1 subset 4Z`" in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == nodes[REDUCTION]["status"] == nodes[NORM]["status"] == "PROVED"
    incoming = {source for source, target, kind in edges if target == NODE and kind == "req"}
    assert incoming == {REDUCTION, NORM}
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert all(profile in nodes[NODE]["statement"] for profile in ("(0,3,2)", "(6,2,0,1)", "(3,0,3)"))

    print(
        "E1_N256_S16_E30_THREE_PROFILE_QUOTIENT_EXCLUSION_PASS "
        "tasks=128 allocations=24124690 closed=3 threshold=1087 mutations=5"
    )


if __name__ == "__main__":
    main()
