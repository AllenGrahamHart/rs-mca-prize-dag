#!/usr/bin/env python3
"""Verify the E1 energy-12 root/parity screen no-go witness."""

from __future__ import annotations

from math import comb, gcd
import json
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_profile018_e12_root_parity_screen_no_go"
PARENTS = {
    "e1_profile018_split_prime_payment_router",
    "e1_s18_m514_hermite_two_profile_exclusion",
}
TARGETS = {
    "e1_profile018_m514_five_ideal_occupancy",
    "e1_official_low_square_mass_pair_budget",
}
MODULUS = 257
GENERATOR = 3
ROOT_EXPONENT = 59
LAGS = tuple(range(1, 12)) + (15,)
EXPECTED_NORM = int(
    "41935541092226372874956803950285349034303208235991339945900329155204479015326718"
)
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128


def cubic_index_direct() -> int:
    oriented = tuple(value for lag in LAGS for value in (-lag, lag))
    result = 0
    for first in oriented:
        for second in oriented:
            for third in oriented:
                total = first + second + third
                if total == 0:
                    result += 1
                elif abs(total) == 128:
                    result -= 1
    return result


def cubic_index_by_relations() -> int:
    result = 0
    lag_set = set(LAGS)
    for first_index, first in enumerate(LAGS):
        for second in LAGS[first_index + 1 :]:
            for third in LAGS:
                if third in (first, second):
                    continue
                if first + second == third:
                    result += 12
                if first + second + third == 128 and first < second < third:
                    result -= 12
    for source in LAGS:
        for target in LAGS:
            if source == target:
                continue
            if 2 * source == target:
                result += 6
            if 2 * source + target == 128:
                result -= 6
    return result


def main() -> None:
    assert len(LAGS) == 12 and len(set(LAGS)) == 12
    assert sum(1 for lag in LAGS if lag % 2) == 7
    exponents = tuple(value for lag in LAGS for value in (lag, 128 - lag))
    hasse = [sum(comb(exponent, order) for exponent in exponents) % 2 for order in range(3)]
    assert hasse == [0, 0, 1]

    assert pow(GENERATOR, 128, MODULUS) == MODULUS - 1
    assert gcd(ROOT_EXPONENT, 256) == 1
    root = pow(GENERATOR, ROOT_EXPONENT, MODULUS)
    assert root == 148 and pow(root, 128, MODULUS) == MODULUS - 1
    trace_sum = sum(
        pow(root, lag, MODULUS) + pow(root, -lag, MODULUS) for lag in LAGS
    ) % MODULUS
    assert trace_sum == 239 and (18 + trace_sum) % MODULUS == 0

    # The Fejer decomposition leaves the exact uniform lower bound 4.
    assert sum(range(1, 12)) == 66
    assert 17 - 66 / 6 - 2 == 4

    assert cubic_index_direct() == 378
    assert cubic_index_by_relations() == 378

    variable = sympy.symbols("X")
    cleared = 18 * variable**15 + sum(
        variable ** (15 + lag) + variable ** (15 - lag) for lag in LAGS
    )
    resultant = int(sympy.resultant(variable**128 + 1, cleared, variable))
    assert resultant == EXPECTED_NORM**2
    assert EXPECTED_NORM % 514 == 0
    assert EXPECTED_NORM // 514 < P_MIN

    node_dir = ROOT / "background/nodes" / NODE
    statement = (node_dir / "statement.md").read_text()
    proof = (node_dir / "proof.md").read_text()
    for text in ("{1,2,...,11,15}", "s=148", "K=378", str(EXPECTED_NORM)):
        assert text in statement
    for text in ("Fejer", "239=-18", "=4", str(EXPECTED_NORM // 514)):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in PARENTS:
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    for target in TARGETS:
        assert nodes[target]["status"] == "TARGET"
        assert (NODE, target, "ev") in edges

    print(
        "E1_PROFILE018_E12_ROOT_PARITY_SCREEN_NO_GO_PASS "
        "lags=12 root=148 multiplicity=2 positivity_floor=4 cubic_index=378 "
        f"norm_quotient={EXPECTED_NORM // 514} verdict=below"
    )


if __name__ == "__main__":
    main()
