#!/usr/bin/env python3
"""Bounded Modal hunt for an m=2 endpoint product-code/Hankel lift."""

from __future__ import annotations

import json

import modal


app = modal.App("rs-mca-rh-type2-m2-product-lift")
image = modal.Image.debian_slim().pip_install("numpy")


@app.function(image=image, cpu=1.0, memory=512, timeout=60)
def search(worker: int) -> dict:
    import random
    import time

    import numpy as np

    prime = 97
    n = 32
    dimension = 8
    rng = random.Random(0xA32F17 + 1000003 * worker)

    def primitive_root() -> int:
        for candidate in range(2, prime):
            if pow(candidate, 48, prime) != 1 and pow(candidate, 32, prime) != 1:
                return candidate
        raise RuntimeError("no primitive root")

    generator = primitive_root()
    omega = pow(generator, (prime - 1) // n, prime)
    domain = np.array([pow(omega, j, prime) for j in range(n)], dtype=np.int64)
    if len(set(map(int, domain))) != n:
        return {"status": "void", "reason": "domain_order", "worker": worker}

    parity = np.empty((n - dimension, n), dtype=np.int64)
    for row in range(n - dimension):
        parity[row, :] = np.array(
            [pow(int(x), row + 1, prime) for x in domain], dtype=np.int64
        )

    missing = {(0, 1), (0, 2), (3, 4), (5, 6), (7, 8)}
    edges = [
        (i, j)
        for i in range(9)
        for j in range(i + 1, 9)
        if (i, j) not in missing
    ]
    if len(edges) != 31:
        return {"status": "void", "reason": "edge_count", "worker": worker}

    def rref(matrix: np.ndarray) -> tuple[np.ndarray, list[int]]:
        array = matrix.copy() % prime
        rows, columns = array.shape
        pivots: list[int] = []
        pivot_row = 0
        for column in range(columns):
            candidates = np.flatnonzero(array[pivot_row:, column])
            if candidates.size == 0:
                continue
            selected = pivot_row + int(candidates[0])
            if selected != pivot_row:
                array[[pivot_row, selected], :] = array[[selected, pivot_row], :]
            inverse = pow(int(array[pivot_row, column]), -1, prime)
            array[pivot_row, :] = array[pivot_row, :] * inverse % prime
            factors = array[:, column].copy()
            factors[pivot_row] = 0
            array = (array - factors[:, None] * array[pivot_row, :]) % prime
            pivots.append(column)
            pivot_row += 1
            if pivot_row == rows:
                break
        return array, pivots

    def nullspace(matrix: np.ndarray) -> np.ndarray:
        reduced, pivots = rref(matrix)
        columns = matrix.shape[1]
        free = [column for column in range(columns) if column not in pivots]
        basis = np.zeros((len(free), columns), dtype=np.int64)
        for index, column in enumerate(free):
            basis[index, column] = 1
            for row, pivot in enumerate(pivots):
                basis[index, pivot] = -reduced[row, column] % prime
        return basis

    def full_support_vector(basis: np.ndarray) -> np.ndarray | None:
        if basis.shape[0] == 0 or np.any(np.all(basis == 0, axis=0)):
            return None
        for _ in range(256):
            coefficients = np.array(
                [rng.randrange(prime) for _ in range(basis.shape[0])], dtype=np.int64
            )
            vector = coefficients @ basis % prime
            if np.all(vector):
                return vector
        return None

    inverse_n = pow(n, -1, prime)

    def interpolate(values: np.ndarray) -> np.ndarray:
        coefficients = []
        for degree in range(dimension):
            total = sum(
                int(value) * pow(int(x), -degree, prime)
                for value, x in zip(values, domain)
            )
            coefficients.append(total * inverse_n % prime)
        return np.array(coefficients, dtype=np.int64)

    def hankel_nullity(q_coefficients: list[np.ndarray]) -> int:
        # q_coefficients[d] is the X-coefficient vector of Gamma^d.
        equations = np.zeros((4 * 9, 32), dtype=np.int64)
        for layer in range(4):
            for row in range(9):
                target = equations[layer * 9 + row]
                if layer <= 2:
                    q = q_coefficients[layer]
                    for column in range(8):
                        target[row + column] += q[column]
                if 0 <= layer - 1 <= 2:
                    q = q_coefficients[layer - 1]
                    for column in range(8):
                        target[16 + row + column] += q[column]
        return 32 - len(rref(equations % prime)[1])

    deadline = time.monotonic() + 52.0
    trials = 0
    rank_histogram: dict[int, int] = {}
    positive_nullity = 0
    coordinate_live = 0
    full_support = 0
    hankel_compatible = 0
    first_survivor = None

    while time.monotonic() < deadline:
        trials += 1
        slopes = rng.sample(range(prime), 9)
        residual_choices = [value for value in range(prime) if value not in slopes]
        residual = rng.choice(residual_choices)
        row_labels = edges + [(0, -1)]
        rng.shuffle(row_labels)

        quadratic = np.empty((n, 3), dtype=np.int64)
        for row, (left, right) in enumerate(row_labels):
            alpha = slopes[left]
            beta = residual if right == -1 else slopes[right]
            quadratic[row, :] = (alpha * beta % prime, -(alpha + beta) % prime, 1)

        stacked = np.vstack(
            [(parity * quadratic[:, coefficient][None, :]) % prime for coefficient in range(3)]
        )
        basis = nullspace(stacked)
        rank = n - basis.shape[0]
        rank_histogram[rank] = rank_histogram.get(rank, 0) + 1
        if basis.shape[0] == 0:
            continue
        positive_nullity += 1
        if np.any(np.all(basis == 0, axis=0)):
            continue
        coordinate_live += 1
        scales = full_support_vector(basis)
        if scales is None:
            continue
        full_support += 1

        evaluations = [scales * quadratic[:, coefficient] % prime for coefficient in range(3)]
        q_coefficients = [interpolate(values) for values in evaluations]
        if any(np.any(parity @ values % prime) for values in evaluations):
            return {"status": "void", "reason": "parity_recheck", "worker": worker}
        nullity = hankel_nullity(q_coefficients)
        hankel_compatible += int(nullity > 0)
        if first_survivor is None:
            first_survivor = {
                "slopes": slopes,
                "residual": residual,
                "row_labels": row_labels,
                "row_scales": list(map(int, scales)),
                "q_coefficients_low_to_high_gamma": [
                    list(map(int, vector)) for vector in q_coefficients
                ],
                "hankel_nullity": nullity,
            }
        if nullity > 0:
            break

    return {
        "status": "hankel_survivor" if hankel_compatible else "complete",
        "worker": worker,
        "trials": trials,
        "rank_histogram": rank_histogram,
        "positive_nullity": positive_nullity,
        "coordinate_live": coordinate_live,
        "full_support": full_support,
        "hankel_compatible": hankel_compatible,
        "first_survivor": first_survivor,
    }


@app.local_entrypoint()
def main(workers: int = 8) -> None:
    results = list(search.map(range(workers)))
    print(json.dumps({"workers": workers, "results": results}, sort_keys=True))
