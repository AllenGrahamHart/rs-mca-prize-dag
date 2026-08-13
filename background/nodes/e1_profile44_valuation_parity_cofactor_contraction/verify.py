#!/usr/bin/env python3
"""Verify the profile-(4,4) valuation-parity cofactor contraction."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
from itertools import combinations
import json
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_profile44_valuation_parity_cofactor_contraction"
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE << 128
VALUATIONS = (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 16, 17, 18, 20)
ENERGY_SIX = {3, 5, 6, 9, 10, 12, 17, 18, 20}
PARENT_BOUND = 932_364
BRANCH_BOUND = 853_574


def hasse_order(support: tuple[int, ...]) -> int:
    residues = Counter(position % 32 for position in support)
    odd = tuple(residue for residue, count in residues.items() if count & 1)
    if not odd:
        return 32
    for derivative in range(32):
        if sum((derivative & ~residue) == 0 for residue in odd) & 1:
            return derivative
    raise AssertionError("nonzero residue polynomial vanished")


def parity_weight(support: tuple[int, ...]) -> int:
    mask = 0
    for left, right in combinations(support, 2):
        delta = (right - left) % 128
        if delta != 64:
            mask ^= 1 << min(delta, 128 - delta)
    return mask.bit_count()


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


def legal_cofactors() -> list[int]:
    rows = []
    for valuation in VALUATIONS:
        odd = 1
        while (cofactor := (1 << valuation) * odd) <= PARENT_BOUND:
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


def validate(packet: dict[str, object]) -> None:
    joint = Counter()
    for tail in combinations(range(1, 128), 3):
        support = (0,) + tail
        joint[(hasse_order(support), parity_weight(support))] += 1
    encoded = {f"{valuation},{weight}": count for (valuation, weight), count in sorted(joint.items())}
    assert packet["normalized_supports"] == sum(joint.values()) == 333_375
    assert packet["joint_counts"] == encoded
    weights = {
        str(valuation): sorted(weight for mu, weight in joint if mu == valuation)
        for valuation in VALUATIONS
    }
    assert packet["relevant_weights_by_valuation"] == weights
    assert set(packet["energy_six_valuations"]) == ENERGY_SIX
    assert all(set(weights[str(valuation)]) <= {2, 4, 6} for valuation in ENERGY_SIX)

    exp_lower, exp_upper = exp_interval(Fraction(48, 5), 27)
    numerator = Fraction(20**192 * 8**16, 5**16)
    assert (BRANCH_BOUND * P_MIN) ** 3 * exp_upper < numerator
    assert numerator < ((BRANCH_BOUND + 1) * P_MIN) ** 3 * exp_lower

    parent = legal_cofactors()
    assert len(parent) == 657
    survivors = [
        cofactor
        for cofactor in parent
        if (cofactor & -cofactor).bit_length() - 1 not in ENERGY_SIX
        or cofactor <= BRANCH_BOUND
    ]
    excluded = sorted(set(parent) - set(survivors))
    assert packet["parent_cofactors"] == 657
    assert packet["surviving_cofactors"] == len(survivors) == 645
    assert packet["excluded_cofactors"] == excluded


def main() -> None:
    node_dir = ROOT / "background/nodes" / NODE
    packet = json.loads((node_dir / "certificate.json").read_text())
    contract = json.loads((node_dir / "source_contract.json").read_text())
    assert hashlib.sha256((ROOT / contract["source"]).read_bytes()).hexdigest() == contract["sha256"]
    validate(packet)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in (
        "e1_profile44_official_energy_le4_exclusion",
        "e1_profile44_energy_floor_cofactor_contraction",
    ):
        assert (parent, NODE, "req") in edges
    for target in ("e1_official_low_square_mass_pair_budget", "unsafe_crossing_family_instantiation"):
        assert (NODE, target, "ev") in edges

    controls = 0
    mutation = json.loads(json.dumps(packet))
    mutation["joint_counts"]["3,2"] += 1
    try:
        validate(mutation)
    except AssertionError:
        controls += 1
    mutation = json.loads(json.dumps(packet))
    mutation["excluded_cofactors"].pop()
    try:
        validate(mutation)
    except AssertionError:
        controls += 1
    mutation = json.loads(json.dumps(packet))
    mutation["energy_six_valuations"].remove(3)
    try:
        validate(mutation)
    except AssertionError:
        controls += 1
    assert controls == 3
    print(
        "E1_PROFILE44_VALUATION_PARITY_COFACTOR_CONTRACTION_PASS "
        "supports=333375 parent=657 survivors=645 controls=3/3"
    )


if __name__ == "__main__":
    main()
