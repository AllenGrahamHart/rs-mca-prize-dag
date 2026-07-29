#!/usr/bin/env python3
"""Verify the square-mass-18 cofactor-1028 energy-four cubic exclusion."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_s18_m1028_energy4_cubic_exclusion"
TARGET = "e1_official_low_square_mass_pair_budget"
SCRIPT = ROOT / "experiments/prize_resolution/e1_m1028_e4_third_moment_screen.py"
RESULT = ROOT / "experiments/prize_resolution/e1_m1028_e4_third_moment_screen_result.json"
SOURCE_PIN = Path(__file__).with_name("source_pin.json")
SCRIPT_SHA256 = "58899fb2cd23ed7370baa4c82399c4ed4ec7d8eee6f2ae2021e386b37fba91f2"
RESULT_SHA256 = "b4e50fe2565be620d66316727ecc0d7555282242e0638491e17d98c1ce427a4b"
LEDGER_DIGEST = "401203ca53dbd51a859b702767576b50aca05c73216194120a60eff251d1d442"
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
COFACTOR = 1028


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    source_pin = json.loads(SOURCE_PIN.read_text())
    if source_pin != {
        "schema": "e1-s18-m1028-energy4-cubic-source-pin-v1",
        "script": SCRIPT.relative_to(ROOT).as_posix(),
        "script_sha256": SCRIPT_SHA256,
        "result": RESULT.relative_to(ROOT).as_posix(),
        "result_sha256": RESULT_SHA256,
        "ledger_digest": LEDGER_DIGEST,
        "types": 8385,
        "maximum_cubic_index": 24,
    }:
        raise RuntimeError("source pin metadata drift")
    if digest(SCRIPT) != SCRIPT_SHA256 or digest(RESULT) != RESULT_SHA256:
        raise RuntimeError("source/result pin drift")

    expected = json.loads(RESULT.read_text())
    namespace = runpy.run_path(str(SCRIPT))
    replayed = json.loads(json.dumps(namespace["census"]()))
    if replayed != expected:
        raise RuntimeError("third-moment screen replay drift")
    if replayed["types"] != 8385 or replayed["maximum_cubic_index"] != 24:
        raise RuntimeError("third-moment cap drift")
    if replayed["high_count"] or replayed["ledger_digest"] != LEDGER_DIGEST:
        raise RuntimeError("third-moment ledger drift")

    energy = 4
    maximum_index = 24
    second_moment = 128 * energy
    third_moment = 64 * maximum_index
    deficit = (
        Fraction(second_moment, 2 * 18**2)
        - Fraction(third_moment, 3 * 18**3)
    )
    if deficit != Fraction(512, 729):
        raise RuntimeError("cubic logarithm deficit drift")
    exponential_lower = sum(
        (deficit**degree / factorial(degree) for degree in range(4)),
        Fraction(),
    )
    if not exponential_lower > Fraction(18**64, COFACTOR * P_MIN):
        raise RuntimeError("exact field-floor separation failed")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    suppliers = (
        "e1_profile210_split_prime_ideal_router",
        "e1_prize_n256_s18_variance_cofactor_windows",
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
        "E1_S18_M1028_ENERGY4_CUBIC_EXCLUSION_PASS "
        f"types={replayed['types']} maximum_K={maximum_index} "
        f"deficit={deficit} digest={replayed['ledger_digest']}"
    )


if __name__ == "__main__":
    main()
