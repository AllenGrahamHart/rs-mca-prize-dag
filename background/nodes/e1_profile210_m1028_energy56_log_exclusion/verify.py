#!/usr/bin/env python3
"""Verify the profile-(2,10), cofactor-1028 energy-five/six exclusion."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_profile210_m1028_energy56_log_exclusion"
TARGET = "e1_official_low_square_mass_pair_budget"
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
COFACTOR = 1028


def main() -> None:
    crossover = Fraction(277, 36)
    if not 0 < crossover < 12:
        raise RuntimeError("log-majorant critical point drift")

    # log(5/3) is below this two-term atanh sum plus geometric tail.
    series_head = 2 * (Fraction(1, 4) + Fraction(1, 3 * 4**3))
    series_tail = Fraction(32, 15 * 5 * 4**5)
    series_upper = series_head + series_tail
    endpoint_threshold = Fraction(2, 3) - Fraction(144, 925)
    if series_head != Fraction(49, 96):
        raise RuntimeError("atanh series head drift")
    if series_tail != Fraction(1, 2400):
        raise RuntimeError("atanh tail drift")
    if series_upper != Fraction(613, 1200):
        raise RuntimeError("atanh upper bound drift")
    if not series_upper < endpoint_threshold:
        raise RuntimeError("log-majorant endpoint separation failed")
    endpoint_margin = endpoint_threshold - series_upper
    if endpoint_margin != Fraction(7, 44400):
        raise RuntimeError("log-majorant endpoint margin drift")

    # For integral A_d, |A_d|<=A_d^2. Energies five and six therefore
    # place every x_u below 2*sum|A_d|<=12.
    for energy in (5, 6):
        if 2 * energy > 12:
            raise RuntimeError("deviation cap drift")
        if Fraction(128 * energy, 925) < Fraction(128, 185):
            raise RuntimeError("energy deficit drift")

    z = Fraction(128, 185)
    exponential_lower = 1 + z + z**2 / 2 + z**3 / 6
    required_ratio = Fraction(18**64, COFACTOR * P_MIN)
    if not exponential_lower > required_ratio:
        raise RuntimeError("exact prize-floor separation failed")

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
        "E1_PROFILE210_M1028_ENERGY56_LOG_EXCLUSION_PASS "
        f"endpoint_margin={endpoint_margin} "
        f"floor_margin={exponential_lower-required_ratio} "
        "remaining_energies=2,3,4"
    )


if __name__ == "__main__":
    main()
