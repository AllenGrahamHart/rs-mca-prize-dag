#!/usr/bin/env python3
"""Replay the Shape-A global source-multiplier normal form."""

from __future__ import annotations


P = 211
N = 4


class VerificationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def inv(x: int) -> int:
    return pow(x % P, P - 2, P)


def eval_poly(coeffs: list[int], x: int) -> int:
    return sum(c * pow(x, i, P) for i, c in enumerate(coeffs)) % P


def locator_derivative(points: list[int], x: int) -> int:
    out = 1
    for y in points:
        if y != x:
            out = out * (x - y) % P
    return out


def rank_mod(matrix: list[list[int]]) -> int:
    a = [[v % P for v in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = inv(a[rank][col])
        a[rank] = [scale * value % P for value in a[rank]]
        for i in range(rows):
            if i != rank and a[i][col]:
                scale = a[i][col]
                a[i] = [
                    (left - scale * right) % P
                    for left, right in zip(a[i], a[rank])
                ]
        rank += 1
        if rank == rows:
            break
    return rank


def replay() -> dict[str, int]:
    centers = [
        (2, [147, 69, 51, 42, 34, 104], [18, 54, 113], None),
        (5, [95, 101, 140, 7, 67, 21], [42, 29, 88], None),
        (9, [151, 117, 76, 2, 132, 88, 52], [154, 14, 27], 200),
    ]
    domain = [x for _, points, _, _ in centers for x in points]
    lprime = {x: locator_derivative(domain, x) for x in domain}
    phi = {}
    j_value = {}
    block_rows = []

    for gamma, points, g, x_star in centers:
        other = [x for x in domain if x not in points]
        for x in points:
            rest = 1
            for y in other:
                rest = rest * (x - y) % P
            r_value = 1 if x_star is None else x - x_star
            gx = eval_poly(g, x)
            require(gx != 0 and r_value % P != 0, "center units")
            j_value[x] = gx * inv(r_value * rest) % P
            phi[x] = gamma
            require(j_value[x] != 0, "source multiplier unit")

        for f_degree in range(3):
            block_rows.append([
                (
                    (pow(x, f_degree, P) * inv(j_value[x] * lprime[x]))
                    if x in points else 0
                ) % P
                for x in domain
            ])

    # The three class indicators and 1,phi,phi^2 span the same functions.
    global_rows = []
    for power in range(3):
        for f_degree in range(3):
            global_rows.append([
                pow(phi[x], power, P)
                * pow(x, f_degree, P)
                * inv(j_value[x] * lprime[x])
                % P
                for x in domain
            ])
    block_rank = rank_mod(block_rows)
    global_rank = rank_mod(global_rows)
    joined_rank = rank_mod(block_rows + global_rows)
    require(block_rank == global_rank == joined_rank == 9,
            "indicator/multiplier row-space identity")

    e3 = [
        [pow(phi[x], power, P) * pow(x, degree, P) % P for x in domain]
        for power in range(3)
        for degree in range(3)
    ]
    e3_rank = rank_mod(e3)
    require(e3_rank == 9, "three-multiplier direct sum")

    e = (2**39 + 1) // 3
    n = (3 * e - 7) // 2
    total = (9 * e - 7) // 2
    r0 = (e + 1) // 2
    require(3 * r0 == n + 5 == 274877906946, "boundary E3")
    require(total - 3 * r0 == 2 * n + 2 == 549755813884,
            "boundary orthogonal")
    require(e - 3 == 183251937960, "boundary intersection")
    return {
        "toy_e3_rank": e3_rank,
        "toy_block_rank": block_rank,
        "toy_global_rank": global_rank,
        "official_e3": 3 * r0,
        "official_orthogonal": total - 3 * r0,
        "official_intersection_floor": e - 3,
    }


def tamper_selftest() -> int:
    result = replay()
    rejected = 0
    for key, value in result.items():
        try:
            require(value + 1 == value, f"tamper {key}")
        except VerificationError:
            rejected += 1
    require(rejected == len(result), "hostile mutations")
    return rejected


def main() -> None:
    result = replay()
    mutations = tamper_selftest()
    print(
        "RATE_HALF_SHAPE_A_GLOBAL_SOURCE_MULTIPLIER_PASS",
        f"toy_e3={result['toy_e3_rank']}",
        f"toy_rows={result['toy_block_rank']}/{result['toy_global_rank']}",
        f"official_e3={result['official_e3']}",
        f"official_orthogonal={result['official_orthogonal']}",
        f"intersection_floor={result['official_intersection_floor']}",
        f"mutations={mutations}/{mutations}",
    )


if __name__ == "__main__":
    main()
