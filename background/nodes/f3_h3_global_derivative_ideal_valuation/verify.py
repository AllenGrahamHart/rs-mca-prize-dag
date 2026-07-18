#!/usr/bin/env python3
"""Verify a small exact derivative-ideal fixture and the DAG interface."""

from __future__ import annotations

import json
from collections import Counter
from math import prod
from pathlib import Path

from sympy import Matrix, ZZ, factorint, integer_nthroot
from sympy.matrices.normalforms import smith_normal_form


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_global_derivative_ideal_valuation"
DEPENDENCY = "f3_h3_shifted_product_sidon"
CONSUMER = "f3_h3_mobius_excess_half"


class DyadicCyclotomicRing:
    """Z[zeta_n] in the basis 1,zeta,...,zeta^(n/2-1)."""

    def __init__(self, order: int) -> None:
        if order < 4 or order & (order - 1):
            raise ValueError("order must be a power of two at least four")
        self.order = order
        self.degree = order // 2
        self.zero = (0,) * self.degree
        self.one = (1,) + (0,) * (self.degree - 1)

    def add(self, left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(a + b for a, b in zip(left, right))

    def neg(self, value: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(-entry for entry in value)

    def sub(self, left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
        return self.add(left, self.neg(right))

    def mul(self, left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
        raw = [0] * (2 * self.degree - 1)
        for i, a in enumerate(left):
            for j, b in enumerate(right):
                raw[i + j] += a * b
        for exponent in range(len(raw) - 1, self.degree - 1, -1):
            raw[exponent - self.degree] -= raw[exponent]
        return tuple(raw[: self.degree])

    def root(self, exponent: int) -> tuple[int, ...]:
        exponent %= self.order
        sign = 1
        if exponent >= self.degree:
            sign = -1
            exponent -= self.degree
        result = [0] * self.degree
        result[exponent] = sign
        return tuple(result)

    def shifted_root(self, exponent: int) -> tuple[int, ...]:
        return self.sub(self.one, self.root(exponent))


def ideal_norm(ring: DyadicCyclotomicRing, generators: list[tuple[int, ...]]) -> int:
    columns: list[list[int]] = []
    for generator in generators:
        for exponent in range(ring.degree):
            columns.append(list(ring.mul(generator, ring.root(exponent))))
    matrix = Matrix(ring.degree, len(columns), lambda row, col: columns[col][row])
    diagonal = smith_normal_form(matrix, domain=ZZ)
    entries = [abs(int(diagonal[i, i])) for i in range(ring.degree)]
    if any(entry == 0 for entry in entries):
        raise AssertionError("derivative ideal unexpectedly vanished")
    return prod(entries)


def odd_part(value: int) -> int:
    while value % 2 == 0:
        value //= 2
    return value


def derivative_integer(order: int, cutoff: int) -> tuple[int, int, list[int]]:
    ring = DyadicCyclotomicRing(order)
    shifted = [ring.shifted_root(exponent) for exponent in range(1, order)]
    products = [ring.mul(left, right) for left in shifted for right in shifted]
    ideal_norms: list[int] = []

    for u in range(1, order):
        c_u = shifted[u - 1]
        for v in range(1, order):
            if u == v:
                continue
            d_v = shifted[v - 1]
            coefficients = [ring.one] + [ring.zero] * cutoff
            degree = 0
            for root_product in products:
                constant = ring.sub(d_v, ring.mul(c_u, root_product))
                next_coefficients = [ring.zero] * (cutoff + 1)
                for index in range(min(degree, cutoff) + 1):
                    next_coefficients[index] = ring.add(
                        next_coefficients[index],
                        ring.mul(coefficients[index], constant),
                    )
                    if index < cutoff:
                        next_coefficients[index + 1] = ring.add(
                            next_coefficients[index + 1],
                            ring.mul(coefficients[index], c_u),
                        )
                coefficients = next_coefficients
                degree += 1
            ideal_norms.append(ideal_norm(ring, coefficients))

    total_odd_norm = prod(odd_part(value) for value in ideal_norms)
    root, exact = integer_nthroot(total_odd_norm, ring.degree)
    if not exact or root % 2 == 0:
        raise AssertionError("odd norm is not the predicted perfect power")
    return int(root), total_odd_norm, ideal_norms


def prime_factors(value: int) -> list[int]:
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return factors


def subgroup(prime: int, order: int) -> set[int]:
    generator = next(
        value
        for value in range(2, prime)
        if all(pow(value, (prime - 1) // factor, prime) != 1 for factor in prime_factors(prime - 1))
    )
    root = pow(generator, (prime - 1) // order, prime)
    return {pow(root, exponent, prime) for exponent in range(order)}


def weighted_excess(prime: int, order: int, cutoff: int) -> tuple[int, int, int]:
    group = subgroup(prime, order)
    shifted = [(1 - value) % prime for value in group if value != 1]
    product_fibers = Counter(left * right % prime for left in shifted for right in shifted)
    quotient_fibers = Counter(right * pow(left, -1, prime) % prime for left in shifted for right in shifted)
    excess = sum(
        max(product_fibers[target] - cutoff, 0) * quotient_fibers[target]
        for target in product_fibers
        if target != 1
    )
    return excess, max(product_fibers.values()), max(quotient_fibers.values())


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    if nodes.get(NODE, {}).get("status") != "PROVED":
        raise AssertionError("global derivative-ideal node is not PROVED")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    if (DEPENDENCY, NODE, "req") not in edges:
        raise AssertionError("Sidon dependency edge is missing")
    if (NODE, CONSUMER, "ev") not in edges:
        raise AssertionError("critical evidence edge is missing")
    if any(left == NODE and kind == "req" and right == CONSUMER for left, right, kind in edges):
        raise AssertionError("open exceptional-prime bound must not be consumed as proved")


def main() -> None:
    e_8_cut2, norm_8_cut2, norms = derivative_integer(8, 2)
    e_8_cut18, norm_8_cut18, _ = derivative_integer(8, 18)
    if norm_8_cut2 != e_8_cut2**4 or norm_8_cut18 != e_8_cut18**4:
        raise AssertionError("perfect-power replay failed")

    fixtures = []
    nonzero = 0
    for prime in (17, 41, 73, 89, 97, 113, 137, 193):
        excess, max_product, max_quotient = weighted_excess(prime, 8, 2)
        if excess:
            nonzero += 1
        if e_8_cut2 % (prime**excess) != 0:
            raise AssertionError((prime, excess, "valuation shortfall"))
        fixtures.append((prime, excess, max_product, max_quotient))
    if nonzero == 0:
        raise AssertionError("cutoff-two valuation fixture is vacuous")
    if e_8_cut18 != 1:
        raise AssertionError("cutoff-eighteen small-order fixture drifted")
    factorization = {int(prime): int(exponent) for prime, exponent in factorint(e_8_cut2).items()}
    if factorization != {3: 168, 5: 22, 17: 48, 41: 2}:
        raise AssertionError((factorization, "cutoff-two ideal mutation"))
    if len(norms) != 42 or any(value <= 0 for value in norms):
        raise AssertionError("ordered quotient ideal inventory drifted")
    check_dag()

    print(
        "F3_H3_GLOBAL_DERIVATIVE_IDEAL_VALUATION_PASS "
        f"e8_cut2_factors={factorization} e8_cut18={e_8_cut18} "
        f"nonzero_rows={nonzero}/8 ideals={len(norms)} fixtures={fixtures} dag=2/2"
    )


if __name__ == "__main__":
    main()
