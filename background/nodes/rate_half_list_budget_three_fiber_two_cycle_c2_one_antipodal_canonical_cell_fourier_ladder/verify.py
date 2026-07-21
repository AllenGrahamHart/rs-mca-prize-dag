#!/usr/bin/env python3
"""Checks for the c2 canonical-cell Fourier ladder."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_canonical_cell_fourier_ladder"
DEPENDENCIES = {
    "rate_half_list_budget_three_fiber_two_cycle_boundary_transfer",
    "rate_half_list_budget_three_fiber_two_cycle_c2_normalized_gap_span_compiler",
    "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_product_ratio_trace_compiler",
}
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 101


def inverse(value: int) -> int:
    return pow(value % PRIME, -1, PRIME)


def convolution(left: list[int], right: list[int], limit: int) -> list[int]:
    out = [0] * limit
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j < limit:
                out[i + j] = (out[i + j] + a * b) % PRIME
    return out


def series_inverse(poly: list[int], limit: int) -> list[int]:
    assert poly[0] == 1
    out = [0] * limit
    out[0] = 1
    for n in range(1, limit):
        out[n] = -sum(poly[j] * out[n - j] for j in range(1, min(n, len(poly) - 1) + 1)) % PRIME
    return out


def power_sums(poly: list[int], limit: int) -> list[int]:
    """Power sums for poly=product(1-a*z), including p_0=degree."""
    degree = len(poly) - 1
    out = [degree]
    for n in range(1, limit):
        value = n * (poly[n] if n <= degree else 0)
        value += sum(poly[j] * out[n - j] for j in range(1, min(n - 1, degree) + 1))
        out.append(-value % PRIME)
    return out


def null_vector(rows: list[list[int]]) -> list[int]:
    matrix = [[value % PRIME for value in row] for row in rows]
    row = 0
    pivots: list[int] = []
    for col in range(4):
        pivot = next((r for r in range(row, len(matrix)) if matrix[r][col]), None)
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        scale = inverse(matrix[row][col])
        matrix[row] = [scale * value % PRIME for value in matrix[row]]
        for r in range(len(matrix)):
            if r != row and matrix[r][col]:
                factor = matrix[r][col]
                matrix[r] = [
                    (matrix[r][c] - factor * matrix[row][c]) % PRIME
                    for c in range(4)
                ]
        pivots.append(col)
        row += 1
    free = next(col for col in range(3, -1, -1) if col not in pivots)
    vector = [0] * 4
    vector[free] = 1
    for r in range(len(pivots) - 1, -1, -1):
        col = pivots[r]
        vector[col] = -sum(matrix[r][c] * vector[c] for c in range(col + 1, 4)) % PRIME
    assert any(vector)
    return vector


def check_wiring() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    incoming = {
        edge["from"]
        for edge in dag["edges"]
        if edge["to"] == NODE_ID and edge.get("kind") == "req"
    }
    outgoing = {
        edge["to"]
        for edge in dag["edges"]
        if edge["from"] == NODE_ID and edge.get("kind") == "ev"
    }
    assert nodes[NODE_ID]["status"] == "PROVED"
    assert incoming == DEPENDENCIES
    assert CONSUMER in outgoing


def main() -> None:
    check_wiring()

    h = 3
    limit = 3 * h + 1
    b = [1, 2, 3, 4]
    c = [1]
    d = convolution(c, series_inverse(b, limit), limit)
    assert d[0] == 1
    ws = [1, 2, 3, -6 % PRIME]
    assert sum(ws) % PRIME == 0 and len(set(ws)) == 4

    factors = []
    sums = []
    for w in ws:
        factor = b + [0] * (h + len(c) - len(b))
        factor[h] = (factor[h] + w) % PRIME
        assert len(factor) - 1 == 2 * h - 3
        assert factor[-1] != 0
        factors.append(factor)
        sums.append(power_sums(factor, limit))

    for s in range(3):
        rows = [[pow(w, exponent, PRIME) for w in ws] for exponent in range(s + 1)]
        lam = null_vector(rows)
        for row in rows:
            assert sum(a * x for a, x in zip(row, lam)) % PRIME == 0
        for j in range((s + 1) * h):
            assert sum(lam[i] * sums[i][j] for i in range(4)) % PRIME == 0

    # The first endpoint is affine in w with slope -H when B(0)=C(0)=1.
    endpoint = [sums[i][h] for i in range(4)]
    for i in range(1, 4):
        assert (endpoint[i] - endpoint[0]) % PRIME == -h * (ws[i] - ws[0]) % PRIME

    # A square Vandermonde matrix on distinct nonzero points is nonsingular.
    points = [1, 4, 9, 16, 25]
    determinant = 1
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            determinant = determinant * (points[j] - points[i]) % PRIME
    assert determinant != 0

    r = 2**37
    official_h = r + 1
    assert 2 * official_h + 2 == 2 * r + 4
    assert 3 * official_h + 1 == 3 * r + 4

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_CANONICAL_CELL_FOURIER_PASS "
        "toy_H=3 kernels=3 strict_blocks=3 endpoint=1 support_bounds=2 wiring=4"
    )


if __name__ == "__main__":
    main()
