#!/usr/bin/env python3
"""Verify the profile-(0,18) split-prime router and payment threshold."""

from __future__ import annotations

from hashlib import sha256
import importlib.util
from itertools import combinations
from math import comb
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_profile018_split_prime_payment_router"
OCCUPANCY = "e1_profile018_m514_five_ideal_occupancy"
TARGET = "e1_official_low_square_mass_pair_budget"
B_PRIZE = 317494674775468773183020924238786383963
CURRENT_RESIDUAL = 2231339193048374054995899432498611923367
CURRENT_CAP = 3994
M018 = 1117325838856821897682125205459304448
EXPECTED_COFACTORS = (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 514, 1028, 1538)
EXPECTED_CHARGE = 2145265610605098043549680394481864540160
EXPECTED_RESIDUAL = 86073582443276011446219038016747383207
EXPECTED_NEXT = (522452937039935372855706187881128712, 4, 4, 20)
EXPECTED_NEXT_CAP = 329
DICTIONARY_PATH = ROOT / "background/nodes/e1_low_square_mass_weighted_kernel_dictionary/verify.py"
DICTIONARY_SHA256 = "e2dbf6100547365b4b686e51269e9af601f5b5dfa776fbd9e0c2eb20faffacb1"


def local_valuations() -> tuple[set[int], dict[int, tuple[int, ...]]]:
    values = set()
    witnesses = {}
    for size in range(2, 17, 2):
        for support in combinations(range(16), size):
            valuation = next(
                order
                for order in range(16)
                if sum(comb(residue, order) for residue in support) % 2
            )
            if valuation <= 10:
                values.add(valuation)
                witnesses.setdefault(valuation, support)
    return values, witnesses


def lift_to_eighteen(support: tuple[int, ...]) -> tuple[int, ...]:
    counts = [int(residue in support) for residue in range(16)]
    remaining = 18 - len(support)
    for residue in range(16):
        while remaining >= 2 and counts[residue] <= 6:
            counts[residue] += 2
            remaining -= 2
    if remaining:
        raise RuntimeError("cannot lift local support to eighteen exponents")
    exponents = tuple(
        residue + 16 * layer
        for residue, count in enumerate(counts)
        for layer in range(count)
    )
    if len(exponents) != 18 or len(set(exponents)) != 18 or max(exponents) >= 128:
        raise RuntimeError("invalid eighteen-exponent lift")
    return exponents


def multiplicative_order(value: int, modulus: int) -> int:
    residue = 1
    for exponent in range(1, modulus + 1):
        residue = residue * value % modulus
        if residue == 1:
            return exponent
    raise RuntimeError("multiplicative order not found")


def factor(value: int) -> list[tuple[int, int]]:
    factors = []
    prime = 2
    while prime * prime <= value:
        exponent = 0
        while value % prime == 0:
            value //= prime
            exponent += 1
        if exponent:
            factors.append((prime, exponent))
        prime += 1
    if value > 1:
        factors.append((value, 1))
    return factors


def load_dictionary():
    if sha256(DICTIONARY_PATH.read_bytes()).hexdigest() != DICTIONARY_SHA256:
        raise RuntimeError("dictionary hash drift")
    spec = importlib.util.spec_from_file_location("e1_profile018_dictionary", DICTIONARY_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load dictionary verifier")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    valuations, witnesses = local_valuations()
    if valuations != set(range(1, 11)) or set(witnesses) != valuations:
        raise RuntimeError("profile018 local valuation census drift")
    for expected, support in witnesses.items():
        exponents = lift_to_eighteen(support)
        actual = next(
            order
            for order in range(16)
            if sum(comb(exponent, order) for exponent in exponents) % 2
        )
        if actual != expected:
            raise RuntimeError("eighteen-exponent valuation lift failed")

    cofactor_bound = 18**64 // (B_PRIZE * 2**128)
    raw = [
        2**valuation * (1 + 256 * parameter)
        for valuation in valuations
        for parameter in range(8)
        if 2**valuation * (1 + 256 * parameter) <= cofactor_bound
    ]
    live = []
    for cofactor in raw:
        if all(
            prime == 2 or exponent % multiplicative_order(prime, 256) == 0
            for prime, exponent in factor(cofactor)
        ):
            live.append(cofactor)
    if cofactor_bound != 2013 or set(live) != set(EXPECTED_COFACTORS):
        raise RuntimeError("profile018 cofactor census drift")

    coarse_orbits = 10 + 128
    threshold_orbits = 10 + 5
    threshold_vectors = 256 * threshold_orbits
    if coarse_orbits != 138 or threshold_vectors != 3840:
        raise RuntimeError("profile018 orbit envelope drift")
    if not threshold_vectors <= CURRENT_CAP < 256 * (threshold_orbits + 1):
        raise RuntimeError("profile018 payment threshold drift")

    charge = M018 * threshold_vectors // 2
    residual = CURRENT_RESIDUAL - charge
    if charge != EXPECTED_CHARGE or residual != EXPECTED_RESIDUAL:
        raise RuntimeError("profile018 payment arithmetic drift")

    dictionary = load_dictionary()
    profiles = []
    for a in range(129):
        for b in range(129 - a):
            square_mass = 4 * a + b
            if not 0 < square_mass <= 66:
                continue
            if not ((b > 0 and square_mass >= 18) or (b == 0 and a >= 15)):
                continue
            weight = dictionary.multiplicity(128, 33, a, b)
            if weight:
                profiles.append((weight, a, b, square_mass))
    profiles.sort(reverse=True)
    if len(profiles) != 271 or profiles[4][1:] != (0, 18, 18):
        raise RuntimeError("active profile ordering drift")
    if profiles[4][0] != M018 or profiles[5] != EXPECTED_NEXT:
        raise RuntimeError("next profile ordering drift")
    next_weight = EXPECTED_NEXT[0]
    next_cap = 2 * residual // next_weight
    if next_cap != EXPECTED_NEXT_CAP:
        raise RuntimeError("profile018 next cap drift")
    if not next_weight * next_cap <= 2 * residual < next_weight * (next_cap + 1):
        raise RuntimeError("profile018 next cap boundary failed")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    suppliers = (
        "e1_profile114_exact_weighted_payment",
        "e1_profile210_split_prime_ideal_router",
        "e1_profile210_m1538_collision_exclusion",
        "e1_s18_m1028_global_energy_window",
        "e1_profile210_m1028_energy2_log_exclusion",
        "e1_profile210_m1028_energy3_modular_norm_exclusion",
        "e1_s18_m1028_energy4_cubic_exclusion",
        "e1_profile210_m1028_energy56_log_exclusion",
        "e1_s18_m514_sharp_product_ceiling",
        "e1_profile210_m514_outer_energy_log_exclusion",
        "e1_profile210_m514_middle_shape_log_router",
        "e1_profile210_m514_parity_trace_cap",
        "e1_low_square_mass_weighted_kernel_dictionary",
    )
    if nodes[NODE]["status"] != "PROVED":
        raise RuntimeError("router status drift")
    if nodes[OCCUPANCY]["status"] != "CONDITIONAL" or nodes[TARGET]["status"] != "TARGET":
        raise RuntimeError("target status drift")
    for supplier in suppliers:
        if nodes[supplier]["status"] != "PROVED":
            raise RuntimeError(f"supplier status drift: {supplier}")
        if (supplier, NODE, "req") not in edges:
            raise RuntimeError(f"missing supplier edge: {supplier}")
    if (NODE, OCCUPANCY, "ev") not in edges or (NODE, TARGET, "ev") not in edges:
        raise RuntimeError("router output edge drift")

    print(
        "E1_PROFILE018_SPLIT_PRIME_PAYMENT_ROUTER_PASS "
        f"valuations={len(valuations)} cofactors={len(live)} "
        f"coarse_orbits={coarse_orbits} threshold_orbits={threshold_orbits} "
        f"next_profile=4,4,20 next_cap={next_cap}"
    )


if __name__ == "__main__":
    main()
