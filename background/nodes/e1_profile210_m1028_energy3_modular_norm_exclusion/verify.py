#!/usr/bin/env python3
"""Verify the profile-(2,10), cofactor-1028 energy-three exclusion."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_profile210_m1028_energy3_modular_norm_exclusion"
TARGET = "e1_official_low_square_mass_pair_budget"
SCRIPT = ROOT / "experiments/prize_resolution/e1_profile210_m1028_e3_modular_norm.py"
RESULT = ROOT / "experiments/prize_resolution/e1_profile210_m1028_e3_modular_norm_result.json"
SOURCE_PIN = Path(__file__).with_name("source_pin.json")
SCRIPT_SHA256 = "4e0d837414ad03cf221914078828e864c148742abca89b9ecae766ed1faf9c66"
RESULT_SHA256 = "ba8a7a920800d163d660376b8f9d4c735cbd894215f1e839e0c68f8797c5f2a8"
LEDGER_DIGEST = "d462adc241981e2e3aa9747a5ba582808d8ebf505e2df6a86fdad2df52a7d3cc"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    source_pin = json.loads(SOURCE_PIN.read_text())
    if source_pin != {
        "schema": "e1-profile210-m1028-e3-source-pin-v1",
        "script": SCRIPT.relative_to(ROOT).as_posix(),
        "script_sha256": SCRIPT_SHA256,
        "result": RESULT.relative_to(ROOT).as_posix(),
        "result_sha256": RESULT_SHA256,
        "ledger_digest": LEDGER_DIGEST,
        "types": 329,
    }:
        raise RuntimeError("source pin metadata drift")
    if digest(SCRIPT) != SCRIPT_SHA256 or digest(RESULT) != RESULT_SHA256:
        raise RuntimeError("source/result pin drift")
    expected = json.loads(RESULT.read_text())
    namespace = runpy.run_path(str(SCRIPT))
    replayed = namespace["census"]()
    if replayed != expected:
        raise RuntimeError("exact modular norm replay drift")
    if replayed["types"] != 329 or replayed["above"] != 329:
        raise RuntimeError("energy-three type census drift")
    if replayed["below"] or replayed["inside"]:
        raise RuntimeError("energy-three interval exclusion failed")
    if replayed["digest"] != LEDGER_DIGEST:
        raise RuntimeError("energy-three ledger digest drift")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    suppliers = (
        "e1_profile210_split_prime_ideal_router",
        "e1_s18_m1028_global_energy_window",
        "e1_profile210_m1028_energy2_log_exclusion",
        "e1_profile210_m1028_energy56_log_exclusion",
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
        "E1_PROFILE210_M1028_ENERGY3_MODULAR_NORM_EXCLUSION_PASS "
        f"types={replayed['types']} above={replayed['above']} "
        f"digest={replayed['digest']} remaining_energy=4"
    )


if __name__ == "__main__":
    main()
