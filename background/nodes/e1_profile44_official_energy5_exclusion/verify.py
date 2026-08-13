#!/usr/bin/env python3
"""Verify the profile-(4,4) official energy-five exclusion."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
from itertools import combinations
import json
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_profile44_official_energy5_exclusion"
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE << 128
VALUATIONS = (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 16, 17, 18, 20)
ENERGY_SIX_VALUATIONS = {3, 5, 6, 9, 10, 12, 17, 18, 20}


def parity_mask(support: tuple[int, ...]) -> tuple[int, ...]:
    live = set()
    for left, right in combinations(support, 2):
        delta = right - left
        if delta == 64:
            continue
        lag = min(delta, 128 - delta)
        if lag in live:
            live.remove(lag)
        else:
            live.add(lag)
    return tuple(sorted(live))


def hasse_order(support: tuple[int, ...]) -> int:
    residues = Counter(position % 32 for position in support)
    odd = tuple(residue for residue, count in residues.items() if count & 1)
    if not odd:
        return 32
    for derivative in range(32):
        if sum((derivative & ~residue) == 0 for residue in odd) & 1:
            return derivative
    raise AssertionError


def factor_odd(value: int) -> list[tuple[int, int]]:
    rows = []
    divisor = 3
    while divisor * divisor <= value:
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        if exponent:
            rows.append((divisor, exponent))
        divisor += 2
    if value > 1:
        rows.append((value, 1))
    return rows


def order_mod_256(value: int) -> int:
    current = value % 256
    order = 1
    while current != 1:
        current = current * value % 256
        order += 1
        assert order <= 64
    return order


def legal_cofactors(bound: int) -> list[int]:
    rows = []
    for valuation in VALUATIONS:
        odd = 1
        while (cofactor := (1 << valuation) * odd) <= bound:
            if all(
                exponent % order_mod_256(prime) == 0
                for prime, exponent in factor_odd(odd)
            ):
                rows.append(cofactor)
            odd += 256
    return rows


def exp_interval(value: Fraction, degree: int) -> tuple[Fraction, Fraction]:
    lower = sum(value**term / factorial(term) for term in range(degree + 1))
    first = value ** (degree + 1) / factorial(degree + 1)
    upper = lower + first / (1 - value / (degree + 2))
    return lower, upper


def validate(packet: dict[str, object], contract: dict[str, object]) -> None:
    masks = {1: set(), 5: set()}
    support_counts = Counter()
    for tail in combinations(range(1, 128), 3):
        support = (0,) + tail
        mask = parity_mask(support)
        if len(mask) in masks:
            masks[len(mask)].add(mask)
            support_counts[(len(mask), hasse_order(support))] += 1
    mask_packet = packet["mask_census"]
    assert mask_packet["normalized_supports"] == 333_375
    assert mask_packet["unique_masks"] == {"1": len(masks[1]), "5": len(masks[5])}
    assert (len(masks[1]), len(masks[5])) == (31, 1785)
    assert mask_packet["support_counts"] == {
        f"{weight},{valuation}": count
        for (weight, valuation), count in sorted(support_counts.items())
    }

    expected_spectra = 1785 * 2**5 + 31 * 62 * 4
    assert expected_spectra == 64_808
    assert packet["primary"]["shards"] == packet["independent_audit"]["shards"] == 8
    assert packet["primary"]["spectra"] == expected_spectra
    assert packet["independent_audit"]["spectra"] == expected_spectra
    assert sum(packet["primary"]["valuation_counts"].values()) == expected_spectra
    assert packet["primary"]["hits"] == packet["independent_audit"]["hits"] == []
    assert packet["independent_audit"]["integer_cofactor_intervals"] == 0

    exp_lower, exp_upper = exp_interval(Fraction(48, 5), 27)
    numerator = Fraction(20**192 * 8**16, 5**16)
    assert (853_574 * P_MIN) ** 3 * exp_upper < numerator
    assert numerator < (853_575 * P_MIN) ** 3 * exp_lower

    parent657 = legal_cofactors(932_364)
    parent645 = [
        cofactor
        for cofactor in parent657
        if (cofactor & -cofactor).bit_length() - 1 not in ENERGY_SIX_VALUATIONS
        or cofactor <= 853_574
    ]
    survivors = legal_cofactors(853_574)
    assert (len(parent657), len(parent645), len(survivors)) == (657, 645, 608)
    consequence = packet["consequence"]
    assert consequence == {
        "energy_floor": 6,
        "variance_floor": 12,
        "cofactor_ceiling": 853574,
        "previous_cofactors": 645,
        "surviving_cofactors": 608,
    }

    for source in contract["sources"]:
        assert hashlib.sha256((ROOT / source["path"]).read_bytes()).hexdigest() == source["sha256"]


def main() -> None:
    node_dir = ROOT / "background/nodes" / NODE
    packet = json.loads((node_dir / "certificate.json").read_text())
    contract = json.loads((node_dir / "source_contract.json").read_text())
    validate(packet, contract)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert ("e1_profile44_valuation_parity_cofactor_contraction", NODE, "req") in edges
    for target in ("e1_official_low_square_mass_pair_budget", "unsafe_crossing_family_instantiation"):
        assert (NODE, target, "ev") in edges

    controls = 0
    mutation = json.loads(json.dumps(packet))
    mutation["mask_census"]["unique_masks"]["5"] -= 1
    try:
        validate(mutation, contract)
    except AssertionError:
        controls += 1
    mutation = json.loads(json.dumps(packet))
    mutation["independent_audit"]["integer_cofactor_intervals"] = 1
    try:
        validate(mutation, contract)
    except AssertionError:
        controls += 1
    mutation_contract = json.loads(json.dumps(contract))
    mutation_contract["sources"][1]["sha256"] = "0" * 64
    try:
        validate(packet, mutation_contract)
    except AssertionError:
        controls += 1
    assert controls == 3
    print(
        "E1_PROFILE44_OFFICIAL_ENERGY5_EXCLUSION_PASS "
        "supports=333375 spectra=64808 survivors=608 controls=3/3"
    )


if __name__ == "__main__":
    main()
