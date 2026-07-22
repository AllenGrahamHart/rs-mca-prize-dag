#!/usr/bin/env python3
"""Verify the tame fixed-petal refinement census and wild boundary."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_tame_fixed_petal_refinement_census"


def polynomial_multiply(left: tuple[int, ...], right: tuple[int, ...], prime: int) -> tuple[int, ...]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return tuple(out)


def polynomial_power(base: tuple[int, ...], exponent: int, prime: int) -> tuple[int, ...]:
    out = (1,)
    for _ in range(exponent):
        out = polynomial_multiply(out, base, prime)
    return out


def verify_tame_triangularity() -> int:
    checks = 0
    cases = ((3, 5, 7), (5, 4, 6), (7, 4, 5), (11, 3, 4))
    for prime, maximum_s, maximum_r in cases:
        for s in range(2, maximum_s + 1):
            for r in range(2, maximum_r + 1):
                if r % prime == 0:
                    continue
                seen: dict[tuple[int, ...], tuple[int, ...]] = {}
                for middle in itertools.product(range(prime), repeat=s - 1):
                    polynomial = (0,) + middle + (1,)
                    power = polynomial_power(polynomial, r, prime)
                    key = tuple(power[r * s - j] for j in range(1, s))
                    assert key not in seen or seen[key] == polynomial
                    seen[key] = polynomial
                    checks += 1
                assert len(seen) == prime ** (s - 1)
                checks += 1
    return checks


# GF(9)=F_3[w]/(w^2+1), represented by pairs a+bw.
Element = tuple[int, int]
ZERO: Element = (0, 0)
ONE: Element = (1, 0)


def field_add(left: Element, right: Element) -> Element:
    return ((left[0] + right[0]) % 3, (left[1] + right[1]) % 3)


def field_neg(value: Element) -> Element:
    return ((-value[0]) % 3, (-value[1]) % 3)


def field_multiply(left: Element, right: Element) -> Element:
    return (
        (left[0] * right[0] - left[1] * right[1]) % 3,
        (left[0] * right[1] + left[1] * right[0]) % 3,
    )


def field_scale(scalar: int, value: Element) -> Element:
    return ((scalar * value[0]) % 3, (scalar * value[1]) % 3)


def extension_add(left: tuple[Element, ...], right: tuple[Element, ...]) -> tuple[Element, ...]:
    out = [ZERO] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = field_add(
            left[index] if index < len(left) else ZERO,
            right[index] if index < len(right) else ZERO,
        )
    while len(out) > 1 and out[-1] == ZERO:
        out.pop()
    return tuple(out)


def extension_multiply(left: tuple[Element, ...], right: tuple[Element, ...]) -> tuple[Element, ...]:
    out = [ZERO] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = field_add(out[i + j], field_multiply(a, b))
    while len(out) > 1 and out[-1] == ZERO:
        out.pop()
    return tuple(out)


def extension_evaluate(polynomial: tuple[Element, ...], value: Element) -> Element:
    out = ZERO
    for coefficient in reversed(polynomial):
        out = field_add(field_multiply(out, value), coefficient)
    return out


def extension_compose(outer: tuple[Element, ...], inner: tuple[Element, ...]) -> tuple[Element, ...]:
    out = (ZERO,)
    for coefficient in reversed(outer):
        out = extension_add(extension_multiply(out, inner), (coefficient,))
    return out


def verify_wild_fixture() -> int:
    elements = tuple((a, b) for a in range(3) for b in range(3))
    lines: list[frozenset[Element]] = []
    seen: set[frozenset[Element]] = set()
    for value in elements[1:]:
        line = frozenset(field_scale(scalar, value) for scalar in range(3))
        if line not in seen:
            seen.add(line)
            lines.append(line)
    assert len(lines) == 4

    target = (ZERO, field_neg(ONE)) + (ZERO,) * 7 + (ONE,)
    right_components: set[tuple[Element, ...]] = set()
    for line in lines:
        right = (ONE,)
        for root in line:
            right = extension_multiply(right, (field_neg(root), ONE))
        image = frozenset(extension_evaluate(right, value) for value in elements)
        assert len(image) == 3
        outer = (ONE,)
        for root in image:
            outer = extension_multiply(outer, (field_neg(root), ONE))
        assert extension_compose(outer, right) == target
        assert right[0] == ZERO
        right_components.add(right)
    assert len(right_components) == 4
    assert len({right[1] for right in right_components}) == 4
    return 4 * len(lines) + 4


def main() -> None:
    checks = verify_tame_triangularity() + verify_wild_fixture()

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_general_first_layout_domination",
        "l1_fixed_source_quotient_partition_anchor_census",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    for consumer in (
        "l1_mixed_residual_intersection_pin",
        "l1_mixed_petal_amplification",
        "petal_mixed_amplification",
    ):
        assert (NODE, consumer, "ev") in edges
        checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "L_(T_i)(X)=product_(a in A)(P(X)-a)=F_A(P(X))",
        "p does not divide r=ell/s",
        "M_src tau(ell) <= M_src ell <= n",
        "3^(n/s)",
        "not asserted to be an admissible multiplicative-domain",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_TAME_FIXED_PETAL_REFINEMENT_PASS checks={checks}")


if __name__ == "__main__":
    main()
