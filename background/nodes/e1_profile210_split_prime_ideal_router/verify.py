#!/usr/bin/env python3
"""Verify the profile-(2,10) cofactor and split-prime ideal router."""

from __future__ import annotations

from itertools import combinations
from math import comb, isqrt
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_profile210_split_prime_ideal_router"
TARGET = "e1_official_low_square_mass_pair_budget"
B_P = 317494674775468773183020924238786383963
M210 = 1227527050040565145269313275179180544
EXPECTED_COFACTORS = (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 514, 1028, 1538)
EXPECTED_CHARGE = 61906644187645781406222007093836433195008


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


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, isqrt(value) + 1))


def local_valuations() -> tuple[set[int], dict[int, tuple[int, ...]]]:
    values = set()
    witnesses = {}
    for size in (2, 4, 6, 8, 10):
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


def lift_to_ten_exponents(support: tuple[int, ...]) -> tuple[int, ...]:
    counts = [int(residue in support) for residue in range(16)]
    remaining = 10 - len(support)
    for residue in range(16):
        while remaining >= 2 and counts[residue] <= 6:
            counts[residue] += 2
            remaining -= 2
    if remaining:
        raise RuntimeError(f"cannot lift parity support: {support}")
    exponents = tuple(
        residue + 16 * layer
        for residue, count in enumerate(counts)
        for layer in range(count)
    )
    if len(exponents) != 10 or len(set(exponents)) != 10:
        raise RuntimeError(f"invalid ten-exponent lift: {exponents}")
    return exponents


def main() -> None:
    valuations, witnesses = local_valuations()
    if valuations != set(range(1, 11)) or set(witnesses) != valuations:
        raise RuntimeError(f"local valuation census drift: {sorted(valuations)}")
    for expected, support in witnesses.items():
        exponents = lift_to_ten_exponents(support)
        actual = next(
            order
            for order in range(16)
            if sum(comb(exponent, order) for exponent in exponents) % 2
        )
        if actual != expected:
            raise RuntimeError(f"valuation witness lift failed: {expected}, {actual}")

    cofactor_bound = 18**64 // (B_P * 2**128)
    if cofactor_bound != 2013:
        raise RuntimeError(f"cofactor bound drift: {cofactor_bound}")

    raw = []
    for valuation in sorted(valuations):
        parameter = 0
        while True:
            cofactor = 2**valuation * (1 + 256 * parameter)
            if cofactor > cofactor_bound:
                break
            raw.append(cofactor)
            parameter += 1
    if len(raw) != 14 or 1026 not in raw:
        raise RuntimeError(f"raw cofactor census drift: {raw}")

    live = []
    for cofactor in raw:
        valid = True
        for prime, exponent in factor(cofactor):
            if prime == 2:
                continue
            if exponent % multiplicative_order(prime, 256):
                valid = False
        if valid:
            live.append(cofactor)
    if set(live) != set(EXPECTED_COFACTORS):
        raise RuntimeError(f"live cofactor census drift: {sorted(live)}")

    if not is_prime(257) or not is_prime(769):
        raise RuntimeError("split rational prime check failed")
    if 257 % 256 != 1 or 769 % 256 != 1:
        raise RuntimeError("complete splitting congruence failed")
    pure = [cofactor for cofactor in live if cofactor & (cofactor - 1) == 0]
    split = [cofactor for cofactor in live if cofactor not in pure]
    if len(pure) != 10 or set(split) != {514, 1028, 1538}:
        raise RuntimeError("ideal-family partition drift")

    maximum_orbits = len(pure) + 128 * len(split)
    oriented_vectors = 256 * maximum_orbits
    charge = 128 * M210 * maximum_orbits
    if maximum_orbits != 394 or oriented_vectors != 100864:
        raise RuntimeError("orbit envelope drift")
    if charge != EXPECTED_CHARGE:
        raise RuntimeError(f"weighted charge drift: {charge}")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    suppliers = (
        "e1_profile36_exact_weighted_payment",
        "e1_pair_feasible_prime_field_reduction",
        "e1_prize_field_floor_even_norm_exclusion",
        "e1_conductor256_full_unit_circular_basis",
        "e1_high_cofactor_schinzel_height_collapse",
        "e1_cofactor2_smyth_height_collapse",
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
        "E1_PROFILE210_SPLIT_PRIME_IDEAL_ROUTER_PASS "
        f"valuations={len(valuations)} raw={len(raw)} live={len(live)} "
        f"pure={len(pure)} split_ideal_families={128 * len(split)} "
        f"maximum_orbits={maximum_orbits} charge={charge}"
    )


if __name__ == "__main__":
    main()
