#!/usr/bin/env python3
"""Independent audit of the cubic endpoint-cofactor compiler fixture."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = Path(__file__).resolve().parent
P = 47
ALPHAS = [5, 10, 17, 19, 21, 23, 24, 26, 28, 30, 37, 42]
ROOTS = [3, 6, 8, 11, 12, 13, 14, 15, 16, 18, 20, 21,
         26, 27, 29, 31, 32, 33, 34, 35, 36, 39, 41, 44]
OWNED = [
    [32, 31], [11, 36], [6, 41], [16, 33],
    [3, 39], [12, 35], [18, 29], [34, 14],
    [20, 27], [44, 13], [21, 26], [15, 8],
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def multiply(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = (result[i + j] + a * b) % P
    return result


def from_roots(roots: list[int]) -> list[int]:
    result = [1]
    for root in roots:
        result = multiply(result, [-root % P, 1])
    return result


def component_value(alpha: int, root: int) -> int:
    unit = root * root + 1
    return (2 * unit * alpha * alpha - 2 * root * (root * root + 3) * alpha + unit * unit) % P


def determinant(matrix: list[list[int]]) -> int:
    rows = [row[:] for row in matrix]
    result = 1
    for column in range(len(rows)):
        pivot = next((row for row in range(column, len(rows)) if rows[row][column]), None)
        require(pivot is not None, "audit minor singular")
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            result = -result
        pivot_value = rows[column][column]
        result = result * pivot_value % P
        pivot_inverse = pow(pivot_value, P - 2, P)
        for row in range(column + 1, len(rows)):
            factor = rows[row][column] * pivot_inverse % P
            rows[row] = [
                (value - factor * pivot_entry) % P
                for value, pivot_entry in zip(rows[row], rows[column])
            ]
    return result % P


def main() -> None:
    proof = (NODE / "proof.md").read_text()
    statement = (NODE / "statement.md").read_text()
    dag = (ROOT / "dag.json").read_text()
    require("unique interpolant" in proof, "interpolation proof")
    require("does not prove that every admissible locator ownership" in statement, "nonclaim")
    require("rate_half_kb_m2_r2_dihedral_degree3_endpoint_cofactor_interpolation_compiler" in dag,
            "DAG node")

    # Reconstruct each cofactor directly from its 18 roots, independently of
    # the primary verifier's division from the complete-source polynomial.
    cofactors: list[list[int]] = []
    for label, alpha in enumerate(ALPHAS):
        star = {root for root in ROOTS if component_value(alpha, root) == 0}
        require(len(star) == 4 and not star.intersection(OWNED[label]), "audit locator support")
        cofactor_roots = [root for root in ROOTS if root not in star and root not in OWNED[label]]
        require(len(cofactor_roots) == 18, "audit cofactor degree")
        cofactors.append(from_roots(cofactor_roots))

    rows = [[cofactors[column][degree] for column in range(12)] for degree in range(11)]
    rows.append([ALPHAS[column] * cofactors[column][0] % P for column in range(12)])
    require(determinant(rows) == 7, "independent pinned determinant")
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_DEGREE3_ENDPOINT_COFACTOR_INTERPOLATION_COMPILER_AUDIT_PASS")


if __name__ == "__main__":
    main()
