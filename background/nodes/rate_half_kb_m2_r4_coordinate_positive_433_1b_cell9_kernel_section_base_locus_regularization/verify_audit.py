#!/usr/bin/env python3
"""Reconstruct the eight pointwise common kernels independently."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell9_kernel_null_residual_result.json"
SECTION = EXP / "rate_half_kb_positive_433_1b_cell9_compact_kernel_result.json"
PRIME = 2130706433
IOTA = 16711679


def rank_kernel(rows):
    matrix = [[value % PRIME for value in row] for row in rows]
    pivots = []
    rank = 0
    for column in range(8):
        pivot = next((row for row in range(rank, len(matrix))
                      if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], -1, PRIME)
        matrix[rank] = [value * inverse % PRIME for value in matrix[rank]]
        for row in range(len(matrix)):
            if row != rank and matrix[row][column]:
                scale = matrix[row][column]
                matrix[row] = [(a-scale*b) % PRIME
                               for a, b in zip(matrix[row], matrix[rank])]
        pivots.append(column)
        rank += 1
    if rank != 7:
        raise RuntimeError(f"rank={rank}")
    free = next(column for column in range(8) if column not in pivots)
    kernel = [0] * 8
    kernel[free] = 1
    for row, column in enumerate(pivots):
        kernel[column] = -matrix[row][free] % PRIME
    return kernel


def main():
    rows = json.loads(RESULT.read_text())["rows"]
    section_rows = {
        tuple(row["epsilon"]): row
        for row in json.loads(SECTION.read_text())["rows"]
    }
    representatives = [row for row in rows if row["sigma"] == [-1, -1]]
    if len(representatives) != 8:
        raise RuntimeError("source representative count")
    t, r, c, b = sp.symbols("t r c b")
    for row in representatives:
        epsilon_1, epsilon_2 = row["epsilon"]
        point = row["point"]
        substitutions = {t: point["t"], r: point["r"],
                         c: point["c"], b: point["b"]}
        section = [
            int(sp.sympify(item["expression"]).subs(substitutions)) % PRIME
            for item in section_rows[tuple(row["epsilon"])]["kernel"]
        ]
        if section != [0] * 8:
            raise RuntimeError("stored section is nonzero")
        roots = (1, epsilon_1*IOTA % PRIME, point["r"], point["t"],
                 epsilon_2*IOTA*point["r"] % PRIME)
        labels = tuple(value*value % PRIME for value in roots)
        products = (-1, point["b"], point["c"],
                    point["b"]*point["c"], -point["b"]*point["c"])
        sums = (0, 1+point["b"], 1+point["c"],
                point["b"]+point["c"], point["b"]-point["c"])
        q_values = tuple(root*value % PRIME
                         for root, value in zip(roots, sums))
        common = [
            [-p, -p*x, -p*x*x, 1, x, x*x, 0, 0]
            for p, x in zip(products, labels)
        ]
        common.extend(
            [q, q*x, q*x*x, 0, 0, 0, x, x*x]
            for q, x in zip(q_values, labels)
        )
        kernel = rank_kernel(common)
        if any(sum(a*b for a, b in zip(source, kernel)) % PRIME
               for source in common):
            raise RuntimeError("kernel dot")
        x = -point["t"]*point["t"] % PRIME
        values = [
            sum(kernel[offset+i]*pow(x, i, PRIME) for i in range(length))
            % PRIME
            for offset, length in ((0, 3), (3, 3), (6, 2))
        ]
        if values != row["missing_values"] or not values[0]:
            raise RuntimeError("missing-value mismatch")
    print("audit=ok pointwise_kernels=8")


if __name__ == "__main__":
    main()
