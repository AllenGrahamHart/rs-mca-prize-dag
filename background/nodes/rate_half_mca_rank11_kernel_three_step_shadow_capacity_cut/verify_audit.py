#!/usr/bin/env python3
"""Independent hierarchy-tree recurrence audit of the capacity cut."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def short_fall(value: int, length: int) -> int:
    return prod(value - offset for offset in range(length))


def short_rise(value: int, length: int) -> int:
    return prod(value + offset for offset in range(length))


def local_record_cap(p: dict[str, int], kprime: int, rank: int) -> int:
    d = 10 - rank
    if d == 9:
        return p["rank9_record_cap"]
    shortened = kprime - rank
    first = Fraction(
        short_fall(p["n_offset"] + shortened, d + 1),
        (p["m_offset"] + shortened) * short_rise(p["m_offset"] + 1, d - 1),
    )
    second = Fraction(
        short_fall(p["n_offset"] + d, d + 1),
        short_rise(p["m_offset"] + 1, d),
    )
    return int(max(first, second))


def audit_data(p: dict[str, int], kprime: int):
    nprime, mprime = p["n_offset"] + kprime, p["m_offset"] + kprime
    caps, shadow, containment = [], [], []
    for rank in range(9, 0, -1):
        d = 10 - rank
        extension = comb(kprime - 10, d + 1)
        ambient = Fraction(
            comb(nprime, rank) * local_record_cap(p, kprime, rank) * extension // (d + 2),
            p["residual_record_floor"],
        )
        support = Fraction(comb(mprime, rank) * extension // (d + 2))
        caps.append(min(ambient, support))
        shadow.append(Fraction(comb(d + 2, 2), comb(kprime - d - 9, 2)))
        if d == 1:
            e0 = comb(mprime - 9, 2)
            containment.append(52 + Fraction(3 * e0, comb(kprime - 10, 2)))
        elif d == 2:
            containment.append(55 + Fraction(6 * comb(67474, 2), comb(kprime - 11, 2)))
        else:
            containment.append(Fraction(55))
    return (
        caps,
        shadow,
        containment,
        Fraction(comb(mprime, 9)),
        Fraction(comb(mprime - 9, 2) * comb(mprime, 9)),
    )


def edge_data(kprime: int, step: int, source: int) -> tuple[Fraction, int]:
    return (
        Fraction(
            comb(source + 2, step) * comb(67472 + source, step),
            comb(kprime - source - 11 + step, step),
        ),
        comb(9 - source + step, step),
    )


def recurrence_certificate(p: dict[str, object], kprime: int) -> Fraction:
    caps, shadow, containment, shadow_budget, containment_budget = audit_data(p, kprime)
    tree = [tuple(edge) for edge in p["dual_tree"]]
    parent = {source: (step, source) for step, source in tree}
    children: dict[int, list[tuple[int, int]]] = {d: [] for d in range(1, 10)}
    for step, source in tree:
        children[source - step].append((step, source))

    factors = [Fraction(0) for _ in range(9)]
    roots = [0 for _ in range(9)]
    factors[0] = factors[1] = Fraction(1)
    roots[0], roots[1] = 1, 2
    for source in range(3, 10):
        if source not in parent:
            continue
        step, _ = parent[source]
        target = source - step
        require(roots[target - 1] != 0, f"tree order source={source}")
        raising, multiplicity = edge_data(kprime, step, source)
        factors[source - 1] = multiplicity * factors[target - 1] / raising
        roots[source - 1] = roots[target - 1]

    x1 = caps[0]
    first_price = sum(containment[i] * factors[i] for i in range(9) if roots[i] == 1)
    second_price = sum(containment[i] * factors[i] for i in range(9) if roots[i] == 2)
    x2 = (containment_budget - first_price * x1) / second_price
    allocation = [factors[i] * (x1 if roots[i] == 1 else x2) for i in range(9)]

    def tree_multipliers(mu: Fraction) -> dict[tuple[int, int], Fraction]:
        values: dict[tuple[int, int], Fraction] = {}
        for source in range(9, 2, -1):
            if source not in parent:
                continue
            edge = parent[source]
            raising, _ = edge_data(kprime, *edge)
            child_charge = sum(
                edge_data(kprime, *child)[1] * values[child]
                for child in children[source]
            )
            values[edge] = (1 - mu * containment[source - 1] + child_charge) / raising
        return values

    def root_two_equation(mu: Fraction) -> Fraction:
        values = tree_multipliers(mu)
        child_charge = sum(
            edge_data(kprime, *child)[1] * values[child]
            for child in children[2]
        )
        return mu * containment[1] - child_charge - 1

    at_zero, at_one = root_two_equation(Fraction(0)), root_two_equation(Fraction(1))
    mu = -at_zero / (at_one - at_zero)
    hierarchy_dual = tree_multipliers(mu)
    root_one_charge = sum(
        edge_data(kprime, *child)[1] * hierarchy_dual[child]
        for child in children[1]
    )
    eta = 1 - mu * containment[0] + root_one_charge
    require(mu >= 0 and eta >= 0, f"root dual signs K={kprime}")
    require(all(value >= 0 for value in hierarchy_dual.values()), f"tree dual signs K={kprime}")

    for d in range(1, 10):
        coverage = mu * containment[d - 1]
        if d == 1:
            coverage += eta
        if d in parent:
            raising, _ = edge_data(kprime, *parent[d])
            coverage += raising * hierarchy_dual[parent[d]]
        coverage -= sum(
            edge_data(kprime, *child)[1] * hierarchy_dual[child]
            for child in children[d]
        )
        require(coverage == 1, f"dual equality d={d} K={kprime}")

    require(all(0 < value <= cap for value, cap in zip(allocation, caps)), f"primal caps K={kprime}")
    require(allocation[0] == caps[0], f"cap equality K={kprime}")
    require(sum(shadow[i] * allocation[i] for i in range(9)) < shadow_budget, f"shadow slack K={kprime}")
    require(sum(containment[i] * allocation[i] for i in range(9)) == containment_budget, f"containment K={kprime}")
    optimum = sum(allocation, Fraction(0))
    require(mu * containment_budget + eta * caps[0] == optimum, f"strong duality K={kprime}")
    return optimum


def demand_ratio(p: dict[str, int], kprime: int) -> Fraction:
    return Fraction(
        p["lane_density_numerator"] * comb(p["m_offset"] + kprime, 11),
        p["lane_density_denominator"],
    )


def main() -> None:
    p = json.loads(CONTRACT.read_text())["parameters"]
    checked = 0
    for kprime in range(p["replay_minimum"], p["closed_dimension_maximum"] + 1):
        require(demand_ratio(p, kprime) > recurrence_certificate(p, kprime), f"closed row K={kprime}")
        checked += 1
    endpoint = recurrence_certificate(p, p["closed_dimension_maximum"])
    wall = recurrence_certificate(p, p["first_open_dimension"])
    require(endpoint == Fraction(p["endpoint_optimum_numerator"], p["endpoint_optimum_denominator"]), "endpoint optimum")
    require(wall == Fraction(p["wall_optimum_numerator"], p["wall_optimum_denominator"]), "wall optimum")
    require(demand_ratio(p, p["first_open_dimension"]) < wall, "wall sign")
    endpoint_scaled = p["residual_record_floor"] * endpoint
    wall_scaled = p["residual_record_floor"] * wall
    require(endpoint_scaled.numerator // endpoint_scaled.denominator == p["endpoint_capacity"], "endpoint capacity")
    require(wall_scaled.numerator // wall_scaled.denominator == p["wall_capacity"], "wall capacity")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_THREE_STEP_SHADOW_CAPACITY_CUT_AUDIT_PASS "
        f"checked={checked + 1} wall={p['first_open_dimension']} tree_edges={len(p['dual_tree'])}"
    )


if __name__ == "__main__":
    main()
