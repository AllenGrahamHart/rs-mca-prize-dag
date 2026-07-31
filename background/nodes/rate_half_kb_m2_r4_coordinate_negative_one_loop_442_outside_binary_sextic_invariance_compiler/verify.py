#!/usr/bin/env python3
"""Verify the binary-sextic invariance and forced-cell census."""

import itertools
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_binary_sextic_invariance_compiler"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def transform(cell, sign_multiplier=None, sign_permutation=None,
              record_map=None):
    signs, forced = cell
    if sign_permutation is not None:
        signs = tuple(signs[index] for index in sign_permutation)
    if sign_multiplier is not None:
        signs = tuple(left*right for left, right in zip(
            signs, sign_multiplier
        ))
    return signs, (record_map or {}).get(forced, forced)


def classify(records, sign_dimension, generators):
    universe = {(signs, forced)
                for signs in itertools.product((-1, 1), repeat=sign_dimension)
                for forced in records}
    remaining = set(universe)
    orbits = []
    while remaining:
        current = {next(iter(remaining))}
        frontier = list(current)
        while frontier:
            cell = frontier.pop()
            for generator in generators:
                image = transform(cell, **generator)
                require(image in universe, "action closure")
                if image not in current:
                    current.add(image)
                    frontier.append(image)
        orbits.append(current)
        remaining -= current
    return universe, orbits


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41BI-2" in statement and "twenty invariant-form" in statement,
            "claim")
    require("does not evaluate" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_explicit_involution_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_template_orbit_classifier",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    # Matrix involution and a direct invariant-sextic fixture.
    alpha, beta, gamma = sp.symbols("Alpha Beta Gamma")
    matrix = sp.Matrix(((alpha, beta), (gamma, -alpha)))
    require(matrix*matrix == (alpha**2+beta*gamma)*sp.eye(2),
            "trace-zero square")
    x, z = sp.symbols("X Z")
    sextic = (x**2-z**2)*(x**2-4*z**2)*(x**2-9*z**2)
    require(sp.expand(sextic.subs({x: x, z: -z}, simultaneous=True)-sextic)
            == 0, "negation fixture")

    s0_records = ("CE", "CF", "DE+", "DE-", "DF+", "DF-", "EF")
    s0_generators = (
        {"record_map": {"DE+": "DE-", "DE-": "DE+",
                        "DF+": "DF-", "DF-": "DF+"}},
        {"sign_multiplier": (-1, 1, -1),
         "record_map": {"DE+": "DE-", "DE-": "DE+"}},
        {"sign_multiplier": (1, -1, -1),
         "record_map": {"DF+": "DF-", "DF-": "DF+"}},
        {"sign_permutation": (1, 0, 2),
         "record_map": {"CE": "CF", "CF": "CE",
                        "DE+": "DF+", "DF+": "DE+",
                        "DE-": "DF-", "DF-": "DE-"}},
    )
    s0_universe, s0_orbits = classify(s0_records, 3, s0_generators)

    s1_records = ("CE", "CF", "DD", "DE", "DF", "EF+", "EF-")
    s1_generators = (
        {"sign_multiplier": (1, 1, -1, -1)},
        {"sign_multiplier": (-1, 1, -1, 1),
         "record_map": {"EF+": "EF-", "EF-": "EF+"}},
        {"sign_multiplier": (1, -1, 1, -1),
         "record_map": {"EF+": "EF-", "EF-": "EF+"}},
        {"sign_permutation": (1, 0, 3, 2),
         "record_map": {"CE": "CF", "CF": "CE",
                        "DE": "DF", "DF": "DE"}},
    )
    s1_universe, s1_orbits = classify(s1_records, 4, s1_generators)

    s2_records = ("CD+", "CD-", "EE", "DF+", "DF-", "EF+", "EF-")
    s2_generators = (
        {"record_map": {"CD+": "CD-", "CD-": "CD+",
                        "DF+": "DF-", "DF-": "DF+"}},
        {"record_map": {"EF+": "EF-", "EF-": "EF+"}},
        {"record_map": {"DF+": "DF-", "DF-": "DF+",
                        "EF+": "EF-", "EF-": "EF+"}},
    )
    s2_universe, s2_orbits = classify(s2_records, 0, s2_generators)

    require((len(s0_universe), len(s1_universe), len(s2_universe))
            == (56, 112, 7), "raw forced cells")
    require((len(s0_orbits), len(s1_orbits), len(s2_orbits))
            == (6, 10, 4), "forced orbit counts")

    def distribution(orbits):
        return {size: sum(len(orbit) == size for orbit in orbits)
                for size in {len(orbit) for orbit in orbits}}

    require(distribution(s0_orbits) == {4: 2, 8: 2, 16: 2},
            "S0 distribution")
    require(distribution(s1_orbits) == {8: 6, 16: 4},
            "S1 distribution")
    require(distribution(s2_orbits) == {1: 1, 2: 3},
            "S2 distribution")
    require((len(s0_orbits)+len(s1_orbits)+len(s2_orbits))*4 == 80,
            "four-row cap")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_BINARY_PASS "
        "forced_orbits=6,10,4 per_common=20 four_rows=80"
    )


if __name__ == "__main__":
    main()
