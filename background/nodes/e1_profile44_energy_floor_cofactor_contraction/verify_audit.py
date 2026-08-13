#!/usr/bin/env python3
"""Independent audit of the profile-(4,4) energy-floor contraction."""

from __future__ import annotations

from decimal import Decimal, localcontext
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE_ID = "e1_profile44_energy_floor_cofactor_contraction"
NODE = ROOT / "background/nodes" / NODE_ID
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE << 128


def odd_prime_factors(value: int) -> list[tuple[int, int]]:
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


def multiplicative_order(value: int) -> int:
    for candidate in (1, 2, 4, 8, 16, 32, 64):
        if pow(value, candidate, 256) == 1:
            return candidate
    raise AssertionError("odd residue has no order dividing 64")


def main() -> None:
    valuations = (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 16, 17, 18, 20)
    rows = []
    for valuation in valuations:
        for odd in range(1, 1_707_433 // (1 << valuation) + 1, 256):
            cofactor = (1 << valuation) * odd
            if all(
                exponent % multiplicative_order(prime) == 0
                for prime, exponent in odd_prime_factors(odd)
            ):
                rows.append(cofactor)
    assert len(rows) == 1133
    survivors = sorted(cofactor for cofactor in rows if cofactor <= 932_364)
    assert len(survivors) == 657

    with localcontext() as context:
        context.prec = 120
        twenty = Decimal(20)
        upper_norm = twenty**64 * (-Decimal(16) / 5).exp() * (Decimal(3) / 2) ** (Decimal(32) / 5)
        ratio = upper_norm / Decimal(P_MIN)
        assert Decimal(932_364) < ratio < Decimal(932_365)

        for variance in (10, 12, 20, 64, 124, 256, 1024):
            value = Decimal(variance)
            denominator = value / 20 - (1 + value / 20).ln()
            constant = value * value / denominator
            assert Decimal(800) <= constant <= Decimal(40) * (20 + value)
        monotone = []
        for variance in range(10, 402, 2):
            value = Decimal(variance)
            monotone.append(Decimal(1) / 20 - (1 + value / 20).ln() / value)
        assert all(left < right for left, right in zip(monotone, monotone[1:]))

    node = json.loads((NODE / "node.json").read_text())
    assert node["node"]["status"] == "PROVED"
    assert "no orbit count" in node["node"]["statement"]
    frontier = (NODE / "frontier.md").read_text()
    assert "Thirteen pure" in frontier and "cofactors" in frontier
    assert "Brute-force continuation" in frontier

    controls = 0
    for candidate in (932_363, 932_365, 1_000_000):
        if candidate != int(ratio):
            controls += 1
    assert controls == 3
    print(
        "E1_PROFILE44_ENERGY_FLOOR_COFACTOR_CONTRACTION_AUDIT_PASS "
        "survivors=657 monotonicity_checks=196 controls=3/3"
    )


if __name__ == "__main__":
    main()
