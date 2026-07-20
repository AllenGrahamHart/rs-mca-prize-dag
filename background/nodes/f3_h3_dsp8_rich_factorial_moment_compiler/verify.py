#!/usr/bin/env python3
"""Verify the DSP8 rich factorial-moment compiler."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_rich_factorial_moment_compiler"
DEPENDENCIES = {
    "f3_h3_disjoint_distance_six_split_pencil_router",
    "f3_h3_dsp8_primitive_shift_pair_adapter",
    "f3_h3_dsp8_global_overlap_cover_payment",
}
CONSUMER = "f3_h3_dsp8_correlation_bound"


def subgroup(prime: int, order: int) -> list[int]:
    for base in range(2, prime):
        generator = pow(base, (prime - 1) // order, prime)
        if pow(generator, order // 2, prime) != 1:
            return [pow(generator, exponent, prime) for exponent in range(order)]
    raise AssertionError("subgroup generator not found")


def support(x: int, y: int, prime: int) -> frozenset[int] | None:
    coefficients: dict[int, int] = defaultdict(int)
    coefficients[x * y % prime] += 1
    coefficients[x] -= 1
    coefficients[y] -= 1
    coefficients = {key: value for key, value in coefficients.items() if value}
    if len(coefficients) == 3 and all(abs(value) == 1 for value in coefficients.values()):
        return frozenset(coefficients)
    return None


def finite_row_check(prime: int = 193, order: int = 64) -> tuple[int, int]:
    group = subgroup(prime, order)
    roots = [value for value in group if value != 1]
    group_set = set(group)
    product_count: dict[int, int] = defaultdict(int)
    generic: dict[int, list[frozenset[int]]] = defaultdict(list)
    antipodal: set[int] = set()

    for left_index, x in enumerate(roots):
        for y in roots[left_index:]:
            target = (1 - x) * (1 - y) % prime
            product_count[target] += 1 if x == y else 2
            atom_support = support(x, y, prime)
            if atom_support is not None:
                generic[target].append(atom_support)
            if x == -y % prime:
                antipodal.add(target)

    quotient_count: dict[int, int] = defaultdict(int)
    for target in range(1, prime):
        if target == 1:
            continue
        quotient_count[target] = sum(
            1
            for z in roots
            if (1 - target * (1 - z)) % prime in group_set
            and (1 - target * (1 - z)) % prime != 1
        )

    d0 = d_a = f0 = f_a = m21 = 0
    retained = 0
    for target, product in product_count.items():
        if target == 1:
            continue
        quotient = quotient_count[target]
        m21 += product * (product - 1) * quotient
        if product < 25:
            continue
        retained += 1
        vertices = generic[target]
        disjoint = sum(
            vertices[i].isdisjoint(vertices[j])
            for i in range(len(vertices))
            for j in range(i + 1, len(vertices))
        )
        factorial = product * (product - 2) * quotient
        if target in antipodal:
            d_a += disjoint * quotient
            f_a += factorial
        else:
            d0 += disjoint * quotient
            f0 += factorial

    k_weight = 20 * d0 + 34 * d_a
    f_weight = 10 * f0 + 17 * f_a
    assert 4 * k_weight <= f_weight
    assert f_weight <= 17 * m21
    assert retained > 0
    return retained, k_weight


def arithmetic_check() -> None:
    for product in range(25, 400):
        for generic in range(product // 2 + 1):
            assert 4 * generic * (generic - 1) <= product * (product - 2)
    assert Fraction(17, 4) * Fraction(76599, 680) == Fraction(76599, 160)
    assert 680 * 69 == 46920 < 76599


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    statement = "".join((base / "statement.md").read_text().split())
    proof = "".join((base / "proof.md").read_text().split())
    for marker in (
        "<=(1/4)(10F_25^0+17F_25^A)",
        "<=(17/4)M_21",
        "40(10F_25^0+17F_25^A)<=76599n^2",
        "680M_21<=76599n^2",
        "2g(t)<=P(t)",
        "K_25^c=2D_6,25^c",
    ):
        assert marker in statement + proof

    target = "".join(
        (ROOT / "critical" / "nodes" / CONSUMER / "statement.md")
        .read_text()
        .split()
    )
    assert "PROVEDRICHFACTORIALMOMENTCOMPILER" in target
    assert "680M_21<=76599n^2" in target


def main() -> None:
    arithmetic_check()
    retained, k_weight = finite_row_check()
    packet_check()
    print(
        "F3_H3_DSP8_RICH_FACTORIAL_MOMENT_COMPILER_PASS "
        f"control_retained={retained} control_k_weight={k_weight} "
        "unweighted_numerator=76599 denominator=680"
    )


if __name__ == "__main__":
    main()
