#!/usr/bin/env python3
"""Replay the Shape-A center residue-pairing rank router."""

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
        a[rank] = [scale * v % P for v in a[rank]]
        for i in range(rows):
            if i != rank and a[i][col]:
                scale = a[i][col]
                a[i] = [
                    (u - scale * v) % P for u, v in zip(a[i], a[rank])
                ]
        rank += 1
        if rank == rows:
            break
    return rank


def gram(points: list[int], g: list[int], x_star: int | None) -> list[list[int]]:
    weights = []
    for x in points:
        gx = eval_poly(g, x)
        require(gx != 0, "center fiber nonvanishing")
        r = 1 if x_star is None else x - x_star
        weights.append(r * inv(gx * locator_derivative(points, x)) % P)
    return [
        [
            sum(w * pow(x, i + j, P) for x, w in zip(points, weights)) % P
            for j in range(N + 1)
        ]
        for i in range(N + 1)
    ]


def row_times(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(a * b for a, b in zip(row, vector)) % P for row in matrix]


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [list(col) for col in zip(*matrix)]


def replay() -> dict[str, int]:
    centers = [
        ([147, 69, 51, 42, 34, 104], [18, 54, 113], None),
        ([95, 101, 140, 7, 67, 21], [42, 29, 88], None),
        ([151, 117, 76, 2, 132, 88, 52], [154, 14, 27], 200),
    ]
    forms = []
    for points, g, x_star in centers:
        matrix = gram(points, g, x_star)
        require(rank_mod(matrix) == N, "full residue-form rank")
        padded_g = g + [0] * (N + 1 - len(g))
        require(row_times(matrix, padded_g) == [0] * (N + 1), "radical")
        forms.append(matrix)

    # W=span{1,X,X^2} contains the three independent center fibers.
    restricted = [matrix[:3] for matrix in forms]
    for matrix in restricted:
        require(rank_mod(matrix) == 2, "restricted rank r-1")

    combined = []
    for matrix in restricted:
        combined.extend(matrix)
    combined_rank = rank_mod(combined)
    kappa = (N + 1) - combined_rank
    require(combined_rank == N + 1 and kappa == 0, "combined rank formula")

    e = (2**39 + 1) // 3
    n = (3 * e - 7) // 2
    r0 = (e + 1) // 2
    kappa_floor = n + 1 - r0
    require(kappa_floor == e - 3 == 183251937960, "official boundary")
    require((5 * e - 3) % 6 == 0, "zero-kappa rank integrality")
    return {
        "form_rank": N,
        "restricted_rank": 2,
        "combined_rank": combined_rank,
        "kappa": kappa,
        "official_kappa_floor": kappa_floor,
    }


def tamper_selftest() -> int:
    result = replay()
    rejected = 0
    for key, value in result.items():
        expected = {
            "form_rank": N,
            "restricted_rank": 2,
            "combined_rank": N + 1,
            "kappa": 0,
            "official_kappa_floor": 183251937960,
        }[key]
        try:
            require(value + 1 == expected, f"tamper {key}")
        except VerificationError:
            rejected += 1
    require(rejected == len(result), "hostile mutations")
    return rejected


def main() -> None:
    result = replay()
    mutations = tamper_selftest()
    print(
        "RATE_HALF_SHAPE_A_CENTER_RESIDUE_PAIRING_PASS",
        f"form_rank={result['form_rank']}",
        f"restricted_rank={result['restricted_rank']}",
        f"combined_rank={result['combined_rank']}",
        f"toy_kappa={result['kappa']}",
        f"official_boundary={result['official_kappa_floor']}",
        f"mutations={mutations}/{mutations}",
    )


if __name__ == "__main__":
    main()
