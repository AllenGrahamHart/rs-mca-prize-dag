#!/usr/bin/env python3
"""Verify the derived-background Johnson bound and strict boundary."""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from pathlib import Path


BOUNDARY = (
    Path(__file__).resolve().parents[1]
    / "l1_background_overlap_singleton_payment"
    / "verify.py"
)
SPEC = spec_from_file_location("l1_background_boundary", BOUNDARY)
assert SPEC is not None and SPEC.loader is not None
V = module_from_spec(SPEC)
SPEC.loader.exec_module(V)


def interpolate_line(
    x_0: int, y_0: int, x_1: int, y_1: int, p: int
) -> tuple[int, int]:
    slope = (y_1 - y_0) * pow(x_1 - x_0, -1, p) % p
    return (y_0 - slope * x_0) % p, slope


def positive_fixture() -> tuple[int, int, int]:
    p = 7
    background = (0, 1, 2)
    received = {x: x * x % p for x in background}
    lines = []
    agreement_sets = []
    for x_0, x_1 in combinations(background, 2):
        line = interpolate_line(x_0, received[x_0], x_1, received[x_1], p)
        agreement = frozenset(
            x for x in background if (line[0] + line[1] * x) % p == received[x]
        )
        assert len(agreement) == 2
        lines.append(line)
        agreement_sets.append(agreement)
    assert len(set(lines)) == 3
    assert all(len(left & right) == 1 for left, right in combinations(agreement_sets, 2))

    b, u, c = 3, 2, 1
    denominator = u * u - b * c
    assert denominator == 1
    assert len(lines) * denominator == b * (u - c)
    return len(lines), denominator, c


def boundary_fixture() -> tuple[int, int, int, int]:
    p_0 = V.check_pair(V.D0, V.F0, V.W0)
    p_1 = V.check_pair(V.D1, V.F1, V.W1)
    support_values = {x: V.evaluate(p_0, x) for x in V.SUPPORT}
    assert all(V.evaluate(p_1, x) == support_values[x] for x in V.SUPPORT)

    # Interpolate on the three petal support points.
    interpolant = (0,)
    for x in V.SUPPORT:
        numerator = (1,)
        denominator = 1
        for y in V.SUPPORT:
            if x == y:
                continue
            numerator = V.mul(numerator, ((-y) % V.P, 1))
            denominator = denominator * (x - y) % V.P
        term = tuple(
            coefficient * support_values[x] * pow(denominator, -1, V.P) % V.P
            for coefficient in numerator
        )
        size = max(len(interpolant), len(term))
        interpolant = V.trim([
            (interpolant[i] if i < len(interpolant) else 0)
            + (term[i] if i < len(term) else 0)
            for i in range(size)
        ])

    petal_locator = V.locator(V.SUPPORT)
    quotients = []
    for codeword in (p_0, p_1):
        quotient, remainder = divmod_poly(V.sub(codeword, interpolant), petal_locator)
        assert remainder == (0,)
        quotients.append(quotient)
    assert quotients[0] != quotients[1]

    derived = (
        V.evaluate((0,), V.BACKGROUND[0]) - V.evaluate(interpolant, V.BACKGROUND[0])
    ) * pow(V.evaluate(petal_locator, V.BACKGROUND[0]), -1, V.P) % V.P
    assert all(V.evaluate(q, V.BACKGROUND[0]) == derived for q in quotients)

    b = len(V.BACKGROUND)
    d, h = len(V.D0), len(V.SUPPORT)
    s = h - d
    u = V.ELL - s
    c = len(V.CORE) - h
    assert (b, u, c) == (1, 1, 1)
    return len(quotients), b, u, c


def divmod_poly(
    numerator: tuple[int, ...], denominator: tuple[int, ...]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    work = list(V.trim(numerator))
    divisor = V.trim(denominator)
    quotient = [0] * max(1, len(work) - len(divisor) + 1)
    while len(work) >= len(divisor) and V.trim(work) != (0,):
        shift = len(work) - len(divisor)
        factor = work[-1] * pow(divisor[-1], -1, V.P) % V.P
        quotient[shift] = factor
        for index, value in enumerate(divisor):
            work[index + shift] = (work[index + shift] - factor * value) % V.P
        work = list(V.trim(work))
    return V.trim(quotient), V.trim(work)


def arithmetic_audit() -> tuple[int, int]:
    positive = 0
    tail = 0
    for ell in range(1, 31):
        for gap in range(1, ell + 1):
            b = ell - gap
            for a in range(1, 41):
                for c in range(a + 1):
                    s = a - c
                    u = ell - s
                    if not (0 <= u <= b):
                        continue
                    denominator = u * u - b * c
                    if denominator > 0:
                        assert u > c
                        positive += 1
                    else:
                        assert (ell - a + c) ** 2 <= (ell - gap) * c
                        tail += 1
    return positive, tail


def main() -> None:
    sharp, positive_denominator, degree = positive_fixture()
    boundary_count, b, u, c = boundary_fixture()
    assert u * u - b * c == 0
    positive, tail = arithmetic_audit()
    assert positive > 0 and tail > 0

    print(
        "L1_BACKGROUND_QUOTIENT_JOHNSON_PASS "
        f"sharp={sharp} positive_denominator={positive_denominator} "
        f"degree={degree} boundary={boundary_count} "
        f"positive={positive} tail={tail}"
    )


if __name__ == "__main__":
    main()
