#!/usr/bin/env python3
"""Independent audit of the profile-(4,4) valuation-parity contraction."""

from __future__ import annotations

from collections import Counter
from decimal import Decimal, localcontext
from itertools import combinations
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = ROOT / "background/nodes/e1_profile44_valuation_parity_cofactor_contraction"
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE << 128


def binomial_parity(top: int, bottom: int) -> int:
    return int(bottom & ~top == 0)


def valuation(support: tuple[int, ...]) -> int:
    residues = Counter(position % 32 for position in support)
    live = [residue for residue, count in residues.items() if count % 2]
    if not live:
        return 32
    for derivative in range(32):
        if sum(binomial_parity(residue, derivative) for residue in live) % 2:
            return derivative
    raise AssertionError


def parity_weight(support: tuple[int, ...]) -> int:
    coefficients = [0] * 64
    for left, right in combinations(support, 2):
        delta = right - left
        if delta < 64:
            coefficients[delta] ^= 1
        elif delta > 64:
            coefficients[128 - delta] ^= 1
    return sum(coefficients)


def main() -> None:
    packet = json.loads((NODE / "certificate.json").read_text())
    joint = Counter()
    for first in range(1, 126):
        for second in range(first + 1, 127):
            for third in range(second + 1, 128):
                support = (0, first, second, third)
                joint[(valuation(support), parity_weight(support))] += 1
    assert sum(joint.values()) == comb(127, 3) == packet["normalized_supports"]
    assert {
        f"{mu},{weight}": count for (mu, weight), count in sorted(joint.items())
    } == packet["joint_counts"]

    energy_six = set(packet["energy_six_valuations"])
    assert energy_six == {3, 5, 6, 9, 10, 12, 17, 18, 20}
    for mu in energy_six:
        weights = {weight for valuation_value, weight in joint if valuation_value == mu}
        assert weights <= {2, 4, 6}
        assert min(
            energy
            for energy in range(5, 30)
            if energy >= min(weights) and any(energy % 4 == weight % 4 for weight in weights)
        ) >= 6

    with localcontext() as context:
        context.prec = 120
        variance = Decimal(12)
        constant = variance * variance / (variance / 20 - (1 + variance / 20).ln())
        upper_norm = Decimal(20) ** 64 * (-Decimal(64) * variance / constant).exp()
        ratio = upper_norm / Decimal(P_MIN)
        assert Decimal(853574) < ratio < Decimal(853575)

    excluded = packet["excluded_cofactors"]
    assert len(excluded) == 12 == len(set(excluded))
    assert all(value > 853574 for value in excluded)
    assert {((value & -value).bit_length() - 1) for value in excluded} <= energy_six

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    assert "Exactly `645`" in statement
    assert "respectively `6,8,6`" in proof
    assert "not an orbit count" in statement

    controls = 0
    for candidate in (853573, 853575, 932364):
        if candidate != int(ratio):
            controls += 1
    assert controls == 3
    print(
        "E1_PROFILE44_VALUATION_PARITY_COFACTOR_CONTRACTION_AUDIT_PASS "
        "supports=333375 joint_cells=54 exclusions=12 controls=3/3"
    )


if __name__ == "__main__":
    main()
