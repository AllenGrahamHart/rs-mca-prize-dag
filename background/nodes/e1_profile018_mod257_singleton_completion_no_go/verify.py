#!/usr/bin/env python3
"""Verify the profile-(0,18) mod-257 completion no-go fence."""

from __future__ import annotations

from math import comb
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_profile018_mod257_singleton_completion_no_go"
ROUTER = "e1_profile018_split_prime_payment_router"
OCCUPANCY = "e1_profile018_m514_five_ideal_occupancy"
TARGET = "e1_official_low_square_mass_pair_budget"
MODULUS = 257
GENERATOR = 3
SUPPORT = tuple(range(16)) + (17, 78)


def energy(support: tuple[int, ...]) -> int:
    autocorrelation = [0] * 64
    for left_index, left in enumerate(support):
        for right in support[left_index + 1 :]:
            difference = right - left
            if difference < 64:
                autocorrelation[difference] += 1
            elif difference > 64:
                autocorrelation[128 - difference] -= 1
    return sum(value * value for value in autocorrelation[1:])


def main() -> None:
    if pow(GENERATOR, 128, MODULUS) != MODULUS - 1:
        raise RuntimeError("primitive-root half-power drift")
    if pow(GENERATOR, 256, MODULUS) != 1:
        raise RuntimeError("primitive-root order drift")
    oriented = {}
    for exponent in range(128):
        value = pow(GENERATOR, exponent, MODULUS)
        for sign in (-1, 1):
            residue = sign * value % MODULUS
            if residue in oriented:
                raise RuntimeError("oriented singleton collision")
            oriented[residue] = (exponent, sign)
    if set(oriented) != set(range(1, MODULUS)):
        raise RuntimeError("oriented singleton completion is not bijective")

    if len(SUPPORT) != 18 or len(set(SUPPORT)) != 18:
        raise RuntimeError("explicit support drift")
    if sum(pow(GENERATOR, exponent, MODULUS) for exponent in SUPPORT) % MODULUS:
        raise RuntimeError("explicit root equation drift")
    multiplicity = next(
        derivative
        for derivative in range(16)
        if sum(comb(exponent, derivative) for exponent in SUPPORT) % 2
    )
    if multiplicity != 1 or sum(SUPPORT) != 215:
        raise RuntimeError("explicit local multiplicity drift")
    if energy(SUPPORT) != 1478:
        raise RuntimeError("explicit energy guard drift")

    for unit in range(1, 256, 2):
        transported = []
        for exponent in SUPPORT:
            image = unit * exponent % 256
            transported.append((image % 128, -1 if image >= 128 else 1))
        if len({position for position, _ in transported}) != 18:
            raise RuntimeError("Galois transport position collision")
        root = pow(GENERATOR, pow(unit, -1, 256), MODULUS)
        if sum(
            sign * pow(root, position, MODULUS)
            for position, sign in transported
        ) % MODULUS:
            raise RuntimeError("Galois transport root drift")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    if nodes[NODE]["status"] != "PROVED" or nodes[ROUTER]["status"] != "PROVED":
        raise RuntimeError("DAG status drift")
    if nodes[OCCUPANCY]["status"] != "CONDITIONAL" or nodes[TARGET]["status"] != "TARGET":
        raise RuntimeError("target status drift")
    if (ROUTER, NODE, "req") not in edges:
        raise RuntimeError("missing router edge")
    if (NODE, OCCUPANCY, "ev") not in edges or (NODE, TARGET, "ev") not in edges:
        raise RuntimeError("missing no-go evidence edge")

    print(
        "E1_PROFILE018_MOD257_SINGLETON_COMPLETION_NO_GO_PASS "
        f"oriented_values={len(oriented)} transported_roots=128 energy={energy(SUPPORT)}"
    )


if __name__ == "__main__":
    main()
