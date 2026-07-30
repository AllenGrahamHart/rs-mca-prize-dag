#!/usr/bin/env python3
"""Verify the cubic endpoint-cofactor interpolation compiler."""

from __future__ import annotations

from pathlib import Path


NODE = Path(__file__).resolve().parent
P = 47
ALPHAS = [5, 10, 17, 19, 21, 23, 24, 26, 28, 30, 37, 42]
X_ROOTS = [3, 6, 8, 11, 12, 13, 14, 15, 16, 18, 20, 21,
           26, 27, 29, 31, 32, 33, 34, 35, 36, 39, 41, 44]
OWNED = [
    [32, 31], [11, 36], [6, 41], [16, 33],
    [3, 39], [12, 35], [18, 29], [34, 14],
    [20, 27], [44, 13], [21, 26], [15, 8],
]
INVARIANT = {1, 2, 5, 6, 8, 10}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def inverse(value: int) -> int:
    require(value % P != 0, "modular inverse")
    return pow(value % P, P - 2, P)


def poly_mul(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = (result[i + j] + a * b) % P
    return result


def root_poly(roots: list[int]) -> list[int]:
    result = [1]
    for root in roots:
        result = poly_mul(result, [-root % P, 1])
    return result


def divide_linear(poly: list[int], root: int) -> list[int]:
    quotient = [0] * (len(poly) - 1)
    quotient[-1] = poly[-1]
    for degree in range(len(quotient) - 1, 0, -1):
        quotient[degree - 1] = (poly[degree] + root * quotient[degree]) % P
    require((poly[0] + root * quotient[0]) % P == 0, "exact linear division")
    return quotient


def divide_roots(poly: list[int], roots: list[int]) -> list[int]:
    result = poly
    for root in roots:
        result = divide_linear(result, root)
    return result


def evaluate(poly: list[int], value: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = (result * value + coefficient) % P
    return result


def phi(value: int) -> int:
    denominator = (value * value - 1) % P
    require(denominator != 0, "phi pole")
    numerator = (value * value + 2) * (2 * value**4 - 10 * value * value - 1)
    return numerator * inverse(denominator**3) % P


def psi(value: int) -> int:
    return 2 * inverse(value * value + 1) % P


def component_poly(alpha: int) -> list[int]:
    # H(alpha,X), in ascending powers of X.
    return [
        (1 + 2 * alpha * alpha) % P,
        (-6 * alpha) % P,
        (2 + 2 * alpha * alpha) % P,
        (-2 * alpha) % P,
        1,
    ]


def matrix_rank(matrix: list[list[int]]) -> tuple[int, list[list[int]], list[int]]:
    rows = [row[:] for row in matrix]
    rank = 0
    pivots: list[int] = []
    for column in range(len(rows[0])):
        pivot = next((row for row in range(rank, len(rows)) if rows[row][column] % P), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = inverse(rows[rank][column])
        rows[rank] = [(scale * value) % P for value in rows[rank]]
        for row in range(len(rows)):
            if row == rank or rows[row][column] == 0:
                continue
            scale = rows[row][column]
            rows[row] = [
                (value - scale * pivot_value) % P
                for value, pivot_value in zip(rows[row], rows[rank])
            ]
        pivots.append(column)
        rank += 1
    return rank, rows, pivots


def determinant(matrix: list[list[int]]) -> int:
    rows = [row[:] for row in matrix]
    result = 1
    for column in range(len(rows)):
        pivot = next((row for row in range(column, len(rows)) if rows[row][column] % P), None)
        require(pivot is not None, "nonsingular pinned minor")
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            result = -result
        value = rows[column][column] % P
        result = result * value % P
        scale = inverse(value)
        for row in range(column + 1, len(rows)):
            factor = rows[row][column] * scale % P
            for entry in range(column, len(rows)):
                rows[row][entry] = (rows[row][entry] - factor * rows[column][entry]) % P
    return result % P


def verify_lagrange_leading_terms() -> None:
    locator = root_poly(ALPHAS)
    source_sum = sum(ALPHAS) % P
    for index, alpha in enumerate(ALPHAS):
        quotient = divide_linear(locator, alpha)
        derivative = 1
        for other_index, other in enumerate(ALPHAS):
            if other_index != index:
                derivative = derivative * (alpha - other) % P
        lagrange = [coefficient * inverse(derivative) % P for coefficient in quotient]
        for other_index, other in enumerate(ALPHAS):
            expected = int(index == other_index)
            require(evaluate(lagrange, other) == expected, "Lagrange evaluation")
        require(lagrange[11] == inverse(derivative), "T^11 coefficient")
        require(lagrange[10] == (alpha - source_sum) * inverse(derivative) % P,
                "T^10 coefficient")


def build_fixture() -> tuple[list[list[int]], list[list[int]]]:
    require([alpha for alpha in ALPHAS if phi(alpha) == 7] == [5, 17, 21, 26, 30, 42],
            "first cubic fiber")
    require([alpha for alpha in ALPHAS if phi(alpha) == 18] == [10, 19, 23, 24, 28, 37],
            "second cubic fiber")
    complete_roots = []
    for value in range(P):
        if (value * value + 1) % P == 0:
            continue
        image = psi(value)
        if (image * image - 1) % P != 0 and phi(image) in (7, 18):
            complete_roots.append(value)
    require(complete_roots == X_ROOTS, "complete source roots")

    stars: dict[int, list[int]] = {}
    star_roots: list[list[int]] = [[] for _ in ALPHAS]
    for root in X_ROOTS:
        labels = [
            index for index, alpha in enumerate(ALPHAS)
            if evaluate(component_poly(alpha), root) == 0
        ]
        require(len(labels) == 2, "star size")
        stars[root] = labels
        for label in labels:
            star_roots[label].append(root)
    require(all(len(roots) == 4 for roots in star_roots), "quartic star degree")

    require(sorted(sum(OWNED, [])) == X_ROOTS, "locator partition")
    for label, roots in enumerate(OWNED):
        require(len(roots) == 2 and not set(roots) & set(star_roots[label]), "locator avoidance")

    fibers = {label: sorted(root for root in X_ROOTS if psi(root) == alpha)
              for label, alpha in enumerate(ALPHAS)}
    invariant = {
        label for label, roots in enumerate(OWNED)
        if roots[0] + roots[1] == P and psi(roots[0]) == psi(roots[1])
    }
    require(invariant == INVARIANT, "six invariant locators")
    sigma = {
        owner: next(label for label, roots in fibers.items() if sorted(OWNED[owner]) == roots)
        for owner in INVARIANT
    }
    require(sigma == {1: 10, 2: 8, 5: 6, 6: 5, 8: 2, 10: 1}, "invariant fiber map")
    require(set(sigma.values()) == INVARIANT and all(owner != target for owner, target in sigma.items()),
            "fixed-point-free invariant bijection")

    noninvariant = set(range(12)) - INVARIANT
    right_degrees = {label: 0 for label in noninvariant}
    for owner in noninvariant:
        targets = [next(label for label, roots in fibers.items() if root in roots) for root in OWNED[owner]]
        require(len(set(targets)) == 2 and set(targets) <= noninvariant, "simple pole graph")
        for target in targets:
            right_degrees[target] += 1
    require(set(right_degrees.values()) == {2}, "two-regular pole graph")
    color_count = sum(
        owner in stars[-root % P]
        for owner in noninvariant
        for root in OWNED[owner]
    )
    require(color_count == 4, "degree-two component edge count")

    complete = root_poly(X_ROOTS)
    cofactors: list[list[int]] = []
    for label in range(12):
        require(component_poly(ALPHAS[label]) == root_poly(star_roots[label]), "component quartic")
        cofactor = divide_roots(complete, star_roots[label] + OWNED[label])
        require(len(cofactor) == 19, "cofactor degree")
        cofactors.append(cofactor)

    first = [[cofactors[column][row] for column in range(12)] for row in range(19)]
    second = [
        [ALPHAS[column] * cofactors[column][row] % P for column in range(12)]
        for row in range(19)
    ]
    return first, second


def verify_square_holonomy(first: list[list[int]]) -> None:
    cofactors = [
        [first[degree][label] for degree in range(19)]
        for label in range(12)
    ]
    owner_by_root = {
        root: owner
        for owner, roots in enumerate(OWNED)
        for root in roots
    }
    edge_root: dict[frozenset[int], int] = {}
    for root in X_ROOTS:
        labels = [
            label for label, alpha in enumerate(ALPHAS)
            if evaluate(component_poly(alpha), root) == 0
        ]
        edge = frozenset(labels)
        require(len(edge) == 2 and edge not in edge_root, "distinct star edge")
        edge_root[edge] = root

    def transport(source: int, target: int) -> int:
        root = edge_root[frozenset((source, target))]
        owner = owner_by_root[root]
        require(owner not in (source, target), "transport locator avoidance")
        numerator = (
            -(ALPHAS[source] - ALPHAS[owner])
            * evaluate(cofactors[source], root)
        ) % P
        denominator = (
            (ALPHAS[target] - ALPHAS[owner])
            * evaluate(cofactors[target], root)
        ) % P
        require(numerator != 0 and denominator != 0, "nonzero edge transport")
        return numerator * inverse(denominator) % P

    components = [
        [(0, 11), (2, 9), (4, 7)],
        [(1, 10), (3, 8), (5, 6)],
    ]
    products: list[int] = []
    for component in components:
        for first_part, second_part in (
            (component[0], component[1]),
            (component[0], component[2]),
            (component[1], component[2]),
        ):
            cycle = [
                first_part[0], second_part[0],
                first_part[1], second_part[1],
            ]
            product = 1
            for index, source in enumerate(cycle):
                product = product * transport(source, cycle[(index + 1) % 4]) % P
            products.append(product)
    require(products == [11, 26, 17, 2, 41, 31], "canonical square holonomies")
    require(all(product != 1 for product in products), "nontrivial square holonomies")


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("full-support kernel" in statement, "kernel criterion")
    require("Not claimed" in contract, "scope boundary")
    verify_lagrange_leading_terms()
    first, second = build_fixture()
    rank_first, reduced, pivots = matrix_rank(first)
    require(rank_first == 11, "first-block rank")
    free = next(column for column in range(12) if column not in pivots)
    kernel = [0] * 12
    kernel[free] = 1
    for row, pivot in enumerate(pivots):
        kernel[pivot] = -reduced[row][free] % P
    require(kernel == [0, 13, 0, 0, 0, 19, 14, 0, 0, 0, 1, 0], "sparse kernel")
    stacked = first + second
    require(matrix_rank(stacked)[0] == 12, "stacked full rank")
    selected = list(range(11)) + [19]
    require(determinant([stacked[row] for row in selected]) == 7, "pinned minor")
    verify_square_holonomy(first)
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_DEGREE3_ENDPOINT_COFACTOR_INTERPOLATION_COMPILER_PASS")


if __name__ == "__main__":
    main()
