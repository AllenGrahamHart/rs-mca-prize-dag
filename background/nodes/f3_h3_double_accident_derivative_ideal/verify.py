#!/usr/bin/env python3
"""Exact order-eight fixture for the joint C36' derivative ideal."""

from __future__ import annotations

import json
from collections import Counter
from itertools import combinations, permutations
from math import gcd, isqrt, prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_double_accident_derivative_ideal"
OLD = "f3_h3_global_derivative_ideal_valuation"
REDUCTION = "f3_h3_cutoff18_double_accident_reduction"
FIBER_CAP = "f3_h3_uniform_product_fiber_stepanov"
CONSUMER = "f3_h3_mobius_excess_half"


class Zeta8Ring:
    """Z[zeta_8] in the basis 1,zeta,zeta^2,zeta^3."""

    zero = (0, 0, 0, 0)
    one = (1, 0, 0, 0)

    @staticmethod
    def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(a + b for a, b in zip(left, right, strict=True))

    @classmethod
    def sub(cls, left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(a - b for a, b in zip(left, right, strict=True))

    @staticmethod
    def mul(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
        raw = [0] * 7
        for i, a in enumerate(left):
            for j, b in enumerate(right):
                raw[i + j] += a * b
        for exponent in range(6, 3, -1):
            raw[exponent - 4] -= raw[exponent]
        return tuple(raw[:4])

    @staticmethod
    def root(exponent: int) -> tuple[int, ...]:
        exponent %= 8
        sign = 1
        if exponent >= 4:
            sign = -1
            exponent -= 4
        out = [0, 0, 0, 0]
        out[exponent] = sign
        return tuple(out)

    @classmethod
    def shifted(cls, exponent: int) -> tuple[int, ...]:
        return cls.sub(cls.one, cls.root(exponent))

    @classmethod
    def power(cls, value: tuple[int, ...], exponent: int) -> tuple[int, ...]:
        out = cls.one
        while exponent:
            if exponent & 1:
                out = cls.mul(out, value)
            value = cls.mul(value, value)
            exponent //= 2
        return out


def permutation_sign(values: tuple[int, ...]) -> int:
    inversions = sum(
        values[i] > values[j]
        for i in range(len(values))
        for j in range(i + 1, len(values))
    )
    return -1 if inversions % 2 else 1


PERMUTATIONS = tuple((perm, permutation_sign(perm)) for perm in permutations(range(4)))


def determinant(columns: tuple[tuple[int, ...], ...]) -> int:
    return sum(
        sign * prod(columns[col][row] for row, col in enumerate(perm))
        for perm, sign in PERMUTATIONS
    )


def ideal_norm(generators: list[tuple[int, ...]]) -> int:
    columns = [
        Zeta8Ring.mul(generator, Zeta8Ring.root(exponent))
        for generator in generators
        for exponent in range(4)
    ]
    index = 0
    for selected in combinations(columns, 4):
        index = gcd(index, abs(determinant(selected)))
        if index == 1:
            break
    if index == 0:
        raise AssertionError("ideal has rank below four")
    return index


def odd_part(value: int) -> int:
    return value // (value & -value)


def fourth_root(value: int) -> int:
    root = isqrt(isqrt(value))
    while (root + 1) ** 4 <= value:
        root += 1
    while root**4 > value:
        root -= 1
    if root**4 != value:
        raise AssertionError("odd ideal norm is not a fourth power")
    return root


def ceil_cube_root(value: int) -> int:
    lower = 0
    upper = 1
    while upper**3 < value:
        upper *= 2
    while upper - lower > 1:
        middle = (lower + upper) // 2
        if middle**3 >= value:
            upper = middle
        else:
            lower = middle
    return upper


def check_official_separator_caps() -> None:
    for order_exponent in range(13, 42):
        n = 1 << order_exponent
        stepanov_ceiling = ceil_cube_root(33**3 * n * n)
        separator_exponent = min(n - 19, stepanov_ceiling - 19)
        assert separator_exponent >= 1
        assert separator_exponent <= n - 19
        assert separator_exponent <= stepanov_ceiling - 19
        assert separator_exponent == (
            n - 19 if order_exponent <= 15 else stepanov_ceiling - 19
        )


def coefficient_ideal(
    shifted: dict[int, tuple[int, ...]],
    products: list[tuple[int, ...]],
    u: int,
    v: int,
    cutoff: int,
) -> list[tuple[int, ...]]:
    c_u = shifted[u]
    d_v = shifted[v]
    coefficients = [Zeta8Ring.one] + [Zeta8Ring.zero] * cutoff
    degree = 0
    for root_product in products:
        constant = Zeta8Ring.sub(d_v, Zeta8Ring.mul(c_u, root_product))
        following = [Zeta8Ring.zero] * (cutoff + 1)
        for index in range(min(degree, cutoff) + 1):
            following[index] = Zeta8Ring.add(
                following[index],
                Zeta8Ring.mul(coefficients[index], constant),
            )
            if index < cutoff:
                following[index + 1] = Zeta8Ring.add(
                    following[index + 1],
                    Zeta8Ring.mul(coefficients[index], c_u),
                )
        coefficients = following
        degree += 1
    return coefficients


def separator(
    shifted: dict[int, tuple[int, ...]],
    indices: tuple[tuple[int, int], ...],
    selected: tuple[int, int],
) -> tuple[int, ...]:
    u, v = selected
    out = Zeta8Ring.one
    for other in indices:
        if other == selected:
            continue
        u_other, v_other = other
        numerator = Zeta8Ring.sub(
            Zeta8Ring.mul(shifted[v], shifted[u_other]),
            Zeta8Ring.mul(shifted[v_other], shifted[u]),
        )
        if numerator == Zeta8Ring.zero:
            raise AssertionError("characteristic-zero quotient collision")
        out = Zeta8Ring.mul(out, numerator)
    return out


def quotient_discriminant_odd_part() -> int:
    shifted = {exponent: Zeta8Ring.shifted(exponent) for exponent in range(1, 8)}
    indices = tuple((u, v) for u in range(1, 8) for v in range(1, 8) if u != v)
    ordered_product = Zeta8Ring.one
    for index in indices:
        ordered_product = Zeta8Ring.mul(
            ordered_product,
            separator(shifted, indices, index),
        )
    assert ordered_product[1:] == Zeta8Ring.zero[1:]
    return odd_part(abs(ordered_product[0]))


def joint_integer(cutoff: int) -> tuple[int, int, int]:
    shifted = {exponent: Zeta8Ring.shifted(exponent) for exponent in range(1, 8)}
    products = [
        Zeta8Ring.mul(left, right)
        for left in shifted.values()
        for right in shifted.values()
    ]
    indices = tuple((u, v) for u in range(1, 8) for v in range(1, 8) if u != v)
    # For the generalized cutoff-two fixture, every nonzero fiber has at most
    # seven representations, so its excess is at most 7-2=5.
    exponent = len(shifted) - cutoff
    old_norms: list[int] = []
    joint_norms: list[int] = []

    for index in indices:
        generators = coefficient_ideal(shifted, products, *index, cutoff)
        delta = separator(shifted, indices, index)
        old_norms.append(ideal_norm(generators))
        joint_norms.append(
            ideal_norm(generators + [Zeta8Ring.power(delta, exponent)])
        )

    old_odd_norm = prod(odd_part(value) for value in old_norms)
    joint_odd_norm = prod(odd_part(value) for value in joint_norms)
    old_integer = fourth_root(old_odd_norm)
    joint = fourth_root(joint_odd_norm)
    if old_integer % joint:
        raise AssertionError("joint exceptional integer does not divide the old one")
    return old_integer, joint, len(indices)


def prime_factors(value: int) -> tuple[int, ...]:
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
    return tuple(factors)


def subgroup(prime: int) -> set[int]:
    factors = prime_factors(prime - 1)
    primitive = next(
        value
        for value in range(2, prime)
        if all(pow(value, (prime - 1) // factor, prime) != 1 for factor in factors)
    )
    root = pow(primitive, (prime - 1) // 8, prime)
    return {pow(root, exponent, prime) for exponent in range(8)}


def excesses(prime: int, cutoff: int) -> tuple[int, int]:
    shifted = [(1 - value) % prime for value in subgroup(prime) if value != 1]
    product_fibers = Counter(a * b % prime for a in shifted for b in shifted)
    quotient_fibers = Counter(
        b * pow(a, -1, prime) % prime for a in shifted for b in shifted
    )
    x = sum(
        max(product_fibers[target] - cutoff, 0) * quotient_fibers[target]
        for target in product_fibers
        if target != 1
    )
    y = sum(
        max(product_fibers[target] - cutoff, 0)
        * max(quotient_fibers[target] - 1, 0)
        for target in product_fibers
        if target != 1
    )
    return x, y


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] in ("TARGET", "CONDITIONAL")  # 2026-07-19 amber re-pose
    assert (OLD, NODE, "req") in edges
    assert (REDUCTION, NODE, "req") in edges
    assert (FIBER_CAP, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges


def main() -> None:
    check_official_separator_caps()
    old, joint, ideals = joint_integer(cutoff=2)
    quotient_discriminant = quotient_discriminant_odd_part()
    expected_old = 3**168 * 5**22 * 17**48 * 41**2
    expected_joint = 3**168 * 5**14 * 17**48 * 41**2
    assert old == expected_old
    assert joint == expected_joint
    assert old // joint == 5**8
    assert quotient_discriminant.bit_length() == 893
    assert prime_factors(quotient_discriminant) == (3, 5, 17, 41)
    assert gcd(old, quotient_discriminant**5) == old

    fixtures = []
    positive = 0
    for prime in (17, 41, 73, 89, 97, 113, 137, 193):
        x, y = excesses(prime, cutoff=2)
        assert (joint % prime == 0) == (y > 0)
        assert joint % (prime**y) == 0
        positive += y > 0
        fixtures.append((prime, x, y))
    assert positive == 2
    check_dag()

    print(
        "F3_H3_DOUBLE_ACCIDENT_DERIVATIVE_IDEAL_PASS "
        f"old_over_joint={old // joint} joint_bits={joint.bit_length()} "
        f"discriminant_bits={quotient_discriminant.bit_length()} "
        "discriminant_gcd=old "
        f"positive_rows={positive}/8 ideals={ideals} fixtures={fixtures} dag=4/4"
    )


if __name__ == "__main__":
    main()
