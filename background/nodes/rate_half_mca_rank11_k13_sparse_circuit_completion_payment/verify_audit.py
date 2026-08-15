#!/usr/bin/env python3
"""Independent arithmetic and shadow audit of the K'=13 payment."""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "12473a9dbffe68438eb813e042d666c9ab08b25ac48bc8cdc0c5dcc2d3b4b30b"


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length))


def record_cap(kprime: int, corank: int) -> int:
    rank = 10 - corank
    shortened = kprime - rank
    candidates = (
        Fraction(
            falling(1048576 + shortened, corank + 1),
            (67472 + shortened) * rising(67473, corank - 1),
        ),
        Fraction(
            falling(1048576 + corank, corank + 1),
            rising(67473, corank),
        ),
    )
    winner = max(candidates)
    return winner.numerator // winner.denominator


def independent_offset_capacity(petal_mass: int, total: int, offset: int) -> int:
    heavy = total // (petal_mass // 2 + 1)
    cross_floor = petal_mass * petal_mass // 4
    balanced = comb(total, 2) * (cross_floor + offset * petal_mass) // cross_floor
    collision = comb(heavy, 2) * (comb(petal_mass - 1, 2) + offset * petal_mass)

    vertex = Fraction(total, 2) + Fraction(heavy * offset * petal_mass, petal_mass - 2)
    floor_vertex = vertex.numerator // vertex.denominator
    candidates = {0, total, floor_vertex, floor_vertex + 1}
    clean = max(
        light * (
            (petal_mass - 2) * (total - light)
            + 2 * heavy * offset * petal_mass
        ) // 2
        for light in candidates
        if 0 <= light <= total
    )
    return clean + balanced + collision


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    p = json.loads(CONTRACT.read_text())["parameters"]
    assert p["K_prime"] == 13
    n, m = p["n_prime"], p["m_prime"]

    caps = [record_cap(13, corank) for corank in (1, 2)]
    assert caps == [16295594, 253241283] == p["kernel_record_caps"]
    extensions = [comb(3, corank + 1) for corank in (1, 2)]
    terms = [
        comb(n, 10 - corank) * cap * extension
        for corank, cap, extension in zip((1, 2), caps, extensions)
    ]
    assert terms == p["kernel_incidence_terms"]
    assert sum(terms) == p["kernel_incidence_cap"]

    core_caps = [
        independent_offset_capacity(m - core, n - core, core - 9)
        for core in range(9, 13)
    ]
    assert core_caps == p["rank9_core_caps"]
    assert max(core_caps) == p["uniform_rank9_chart_cap"]

    shadow_checks = 0
    for support in range(1, 12):
        rank8 = rank9 = 0
        for omitted in itertools.combinations(range(11), 2):
            if set(omitted).isdisjoint(range(support)):
                rank8 += 1
            else:
                rank9 += 1
        assert rank8 == comb(11 - support, 2)
        assert rank9 == 55 - rank8
        shadow_checks += 55
    assert min(55 - comb(11 - support, 2) for support in range(6, 12)) == 45

    high = comb(n, 9) * max(core_caps) // 45
    assert high == p["high_circuit_incidence_cap"]
    records = p["residual_record_floor"]
    low_per_record = p["low_circuit_per_record_cap"]
    assert low_per_record == sum(
        2 * comb(m, support - 1) * comb(m - support - 1, 11 - support) // support
        for support in range(2, 6)
    )
    low = records * low_per_record
    total = sum(terms) + high + low
    required = Fraction(990810934 * records * comb(m, 11), 10**9)
    demand = (required.numerator + required.denominator - 1) // required.denominator
    coefficient = Fraction(990810934 * comb(m, 11), 10**9) - low_per_record
    assert coefficient > 0
    assert low == p["low_circuit_incidence_cap_at_record_floor"]
    assert total == p["total_capacity_at_record_floor"]
    assert demand == p["required_incidence_at_record_floor"]
    assert demand - total == p["demand_capacity_gap"] > 0

    print(
        "PASS K13 sparse-circuit completion payment audit: "
        f"record caps {caps}, {shadow_checks} shadow omissions, "
        f"gap {demand-total}"
    )


if __name__ == "__main__":
    main()
