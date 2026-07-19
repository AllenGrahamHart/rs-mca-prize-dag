#!/usr/bin/env python3
"""Finite-field and exact-arithmetic replay of full-petal CRT injectivity."""

from itertools import product
from math import ceil, comb


def multiply(left: tuple[int, ...], right: tuple[int, ...], p: int) -> tuple[int, ...]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return tuple(out)


def locator(points: tuple[int, ...], p: int) -> tuple[int, ...]:
    out = (1,)
    for point in points:
        out = multiply(out, ((-point) % p, 1), p)
    return out


def evaluate(coeffs: tuple[int, ...], x: int, p: int) -> int:
    value = 0
    for coeff in reversed(coeffs):
        value = (value * x + coeff) % p
    return value


def replay_cell(
    p: int,
    retained: tuple[int, ...],
    missed: tuple[int, ...],
    labels: tuple[int, ...],
    petals: tuple[tuple[int, ...], ...],
) -> int:
    ell = len(petals[0])
    d = len(missed)
    effective = d - len(retained)
    agreement = ell + effective
    loc_r = locator(retained, p)
    loc_d = locator(missed, p)
    seen: dict[tuple[int, ...], tuple[int, ...]] = {}

    for quotient in product(range(p), repeat=effective + 1):
        touched: list[int] = []
        mixed = False
        for i, petal in enumerate(petals):
            hits = sum(
                evaluate(quotient, x, p) * evaluate(loc_r, x, p) % p
                == labels[i] * evaluate(loc_d, x, p) % p
                for x in petal
            )
            if hits == ell:
                touched.append(i)
            elif hits != 0:
                mixed = True
        if mixed or len(touched) * ell < agreement:
            continue
        key = tuple(touched)
        if key in seen and seen[key] != quotient:
            raise AssertionError((key, seen[key], quotient))
        seen[key] = quotient

    tail = sum(comb(len(petals), t) for t in range(ceil(agreement / ell), len(petals) + 1))
    if len(seen) > tail:
        raise AssertionError((len(seen), tail))
    return len(seen)


def main() -> None:
    counts = [
        replay_cell(11, (8,), (5, 6, 7), (1, 2, 3, 4, 5), ((0,), (1,), (2,), (3,), (4,))),
        replay_cell(11, (8,), (5, 6, 7), (2, 2, 3, 3, 4), ((0,), (1,), (2,), (3,), (4,))),
        replay_cell(11, (9,), (6, 7, 8), (1, 2, 3), ((0, 1), (2, 3), (4, 5))),
    ]
    if sum(counts) == 0:
        raise AssertionError("finite-field replay was vacuous")

    arithmetic_rows = 0
    for ell in range(1, 33):
        for petals in range(2, 65):
            tails = [0] * (petals + 2)
            for t in range(petals, -1, -1):
                tails[t] = tails[t + 1] + comb(petals, t)
            for effective in range(0, petals * ell - ell + 1):
                agreement = ell + effective
                first = ceil(agreement / ell)
                tail = tails[first]
                if first * ell <= effective or tail > 1 << petals:
                    raise AssertionError((ell, petals, effective, first, tail))
                arithmetic_rows += 1

    # If the touched modulus has degree only d_eff, uniqueness is false:
    # every scalar multiple of that locator has the same zero residue.
    p = 7
    petal_locator = locator((0, 1), p)
    collision = {multiply((scalar,), petal_locator, p) for scalar in range(p)}
    if len(collision) != p:
        raise AssertionError("degree-endpoint mutation did not collide")

    print(
        "PETAL_FULL_TOUCHED_SET_INJECTION_PASS "
        f"finite_cells={len(counts)} realized={sum(counts)} "
        f"arithmetic_rows={arithmetic_rows} endpoint_collision={len(collision)}"
    )


if __name__ == "__main__":
    main()
