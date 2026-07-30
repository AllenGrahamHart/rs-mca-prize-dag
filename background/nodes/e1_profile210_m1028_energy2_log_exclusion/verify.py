#!/usr/bin/env python3
"""Verify the profile-(2,10), cofactor-1028 energy-two exclusion."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_profile210_m1028_energy2_log_exclusion"
TARGET = "e1_official_low_square_mass_pair_budget"
B_PRIZE = 317494674775468773183020924238786383963
P_MAX = (B_PRIZE + 1) * 2**128 - 1
COFACTOR = 1028


def main() -> None:
    crossover = Fraction(-11, 4)
    if not -4 < crossover < 0:
        raise RuntimeError("log-minorant critical point drift")

    # log(9/7) is below this one-term atanh sum plus geometric tail.
    series_head = Fraction(1, 4)
    series_tail = Fraction(1, 756)
    series_upper = series_head + series_tail
    endpoint_threshold = Fraction(2, 9) + Fraction(16, 549)
    if series_upper != Fraction(95, 378):
        raise RuntimeError("atanh upper bound drift")
    if endpoint_threshold != Fraction(46, 183):
        raise RuntimeError("endpoint threshold drift")
    if not series_upper < endpoint_threshold:
        raise RuntimeError("log-minorant endpoint separation failed")
    endpoint_margin = endpoint_threshold - series_upper
    if endpoint_margin != Fraction(1, 23058):
        raise RuntimeError("log-minorant endpoint margin drift")

    energy = 2
    if 2 * energy != 4 or 128 * energy != 256:
        raise RuntimeError("energy moment drift")

    z = Fraction(256, 549)
    exponential_lower = 1 - z
    if exponential_lower != Fraction(293, 549):
        raise RuntimeError("exponential lower bound drift")
    if not 18**64 * exponential_lower > COFACTOR * P_MAX:
        raise RuntimeError("exact prize-ceiling separation failed")
    floor_margin = 18**64 * 293 - COFACTOR * P_MAX * 549

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    suppliers = (
        "e1_profile210_split_prime_ideal_router",
        "e1_s18_m1028_global_energy_window",
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
        "E1_PROFILE210_M1028_ENERGY2_LOG_EXCLUSION_PASS "
        f"endpoint_margin={endpoint_margin} floor_margin={floor_margin} "
        "remaining_energies=3,4"
    )


if __name__ == "__main__":
    main()
