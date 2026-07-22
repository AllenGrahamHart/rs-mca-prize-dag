#!/usr/bin/env python3
"""Exact replay of the saturated cyclic-design residue route fence."""

from __future__ import annotations


P = 151
E = 5
V = 15
ZETA = 38
S = (0, 1, 5, 6, 10)
T = (0, 1, 5, 6, 11)
U = (0, 3, 6, 9, 12)
OMEGA = {0, 1, 3, 4, 5, 6, 7, 9, 10}


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % P == 0:
        poly.pop()
    return [value % P for value in poly]


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] = (out[i + j] + left_value * right_value) % P
    return trim(out)


def divide_exact(dividend: list[int], divisor: list[int]) -> list[int]:
    work = dividend[:]
    quotient = [0] * (len(dividend) - len(divisor) + 1)
    inverse_lead = pow(divisor[-1], P - 2, P)
    for shift in range(len(quotient) - 1, -1, -1):
        coefficient = work[shift + len(divisor) - 1] * inverse_lead % P
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            work[shift + index] = (work[shift + index] - coefficient * value) % P
    need(all(value == 0 for value in work[: len(divisor) - 1]), "division failed")
    return trim(quotient)


def locator(block: tuple[int, ...]) -> list[int]:
    out = [1]
    for exponent in block:
        out = multiply(out, [(-pow(ZETA, exponent, P)) % P, 1])
    return out


def translate(block: tuple[int, ...], shift: int) -> tuple[int, ...]:
    return tuple(sorted((value + shift) % V for value in block))


def orbit(block: tuple[int, ...]) -> set[tuple[int, ...]]:
    return {translate(block, shift) for shift in range(V)}


def rank(rows: list[list[int]]) -> int:
    width = max(len(row) for row in rows)
    work = [row + [0] * (width - len(row)) for row in rows]
    pivot_row = 0
    for column in range(width):
        pivot = next(
            (index for index in range(pivot_row, len(work)) if work[index][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        factor = pow(work[pivot_row][column], P - 2, P)
        work[pivot_row] = [factor * value % P for value in work[pivot_row]]
        for index in range(len(work)):
            if index == pivot_row or work[index][column] == 0:
                continue
            factor = work[index][column]
            work[index] = [
                (value - factor * pivot_value) % P
                for value, pivot_value in zip(work[index], work[pivot_row], strict=True)
            ]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def quadratic_row(poly: list[int]) -> list[int]:
    return [
        poly[i] * poly[j] % P
        for i in range(E + 1)
        for j in range(i, E + 1)
    ]


def remainder(dividend: list[int], divisor: list[int]) -> list[int]:
    work = dividend[:]
    inverse_lead = pow(divisor[-1], P - 2, P)
    for shift in range(len(work) - len(divisor), -1, -1):
        coefficient = work[shift + len(divisor) - 1] * inverse_lead % P
        for index, value in enumerate(divisor):
            work[shift + index] = (work[shift + index] - coefficient * value) % P
    return trim(work[: len(divisor) - 1])


def main() -> None:
    need(pow(ZETA, V, P) == 1, "zeta does not have order dividing 15")
    need(all(pow(ZETA, divisor, P) != 1 for divisor in (1, 3, 5)), "zeta order is not 15")

    s_orbit = orbit(S)
    t_orbit = orbit(T)
    u_orbit = orbit(U)
    need((len(s_orbit), len(t_orbit), len(u_orbit)) == (15, 15, 3), "bad orbit sizes")
    need(not (s_orbit & t_orbit or s_orbit & u_orbit or t_orbit & u_orbit), "orbits meet")
    blocks = sorted(s_orbit | t_orbit | u_orbit)
    need(len(blocks) == 6 * E + 3, "wrong block count")
    need(all(len(block) == E for block in blocks), "wrong block size")
    replications = [sum(point in block for block in blocks) for point in range(V)]
    need(replications == [2 * E + 1] * V, "design is not exactly biregular")

    p_z = [(-1) % P] + [0] * (V - 1) + [1]
    locators = [locator(block) for block in blocks]
    complements = [divide_exact(p_z, poly) for poly in locators]
    need(rank([quadratic_row(poly) for poly in locators]) == 3 * E + 1, "bad quadratic rank")
    need(rank(complements) == E + 4, "bad complement rank")

    seed_s = locator(S)
    seed_t = locator(T)
    need(seed_s == [149, 46, 150, 2, 105, 1], "S locator drift")
    need(seed_t == [75, 135, 92, 32, 118, 1], "T locator drift")
    h_s = divide_exact(p_z, seed_s)
    h_t = divide_exact(p_z, seed_t)
    need(h_s == [76, 87, 0, 108, 68, 0, 42, 60, 0, 46, 1], "S complement drift")
    need(h_t == [2, 87, 0, 130, 68, 0, 17, 60, 0, 33, 1], "T complement drift")
    support = {
        degree
        for poly in complements
        for degree, coefficient in enumerate(poly)
        if coefficient
    }
    need(support == OMEGA, "complement coordinate support drift")

    # Deterministic split internal locators confirm the universal rank >= 4
    # conclusion used in the proof. Their roots avoid mu_15 and zero.
    domain = {pow(ZETA, exponent, P) for exponent in range(V)}
    available = [value for value in range(1, P) if value not in domain]
    residue_ranks = []
    for offset in range(24):
        roots = tuple(available[offset + 7 * index] for index in range(E))
        i_poly = [1]
        for root in roots:
            i_poly = multiply(i_poly, [(-root) % P, 1])
        need(i_poly[0] != 0, "sample internal locator has zero constant")
        residue_rank = rank([remainder(poly, i_poly) for poly in complements])
        need(residue_rank >= 4, "sample residue rank fell below four")
        residue_ranks.append(residue_rank)

    # Universal symbolic obstruction: W has no degree-two coordinate, while
    # z^2 I has that nonzero coordinate for every I with I(0) != 0.
    need(2 not in OMEGA, "universal residue obstruction disappeared")

    print(
        "RATE_HALF_DISTANCE_THREE_SATURATED_CYCLIC_DESIGN_RESIDUE_ROUTE_FENCE_PASS "
        f"blocks={len(blocks)} replication={replications[0]} quadratic_rank={3 * E + 1} "
        f"complement_rank={E + 4} residue_samples={len(residue_ranks)} "
        f"residue_min={min(residue_ranks)}"
    )


if __name__ == "__main__":
    main()
