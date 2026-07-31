#!/usr/bin/env python3
"""Exact F_29 falsifier for the coordinate common-K Vieta gates.

The search fixes one honest signed six-pair label configuration, removes one
I-label to form K, and exhausts all five-fold signed J-edge-orbit assignments.
Only the two proved coordinate degree profiles are retained.  Surviving
kernel vectors are also tested against the aligned full quotient identities.
"""

from __future__ import annotations

import itertools
import json
import time
from collections import Counter
from typing import Iterable

import modal


P = 29
I_BASES = (1, 4, 9)
J_BASES = (2, 3, 5)
XI = 20
K_POINTS = (1, 28, 4, 25, 9)
DEADLINE_SECONDS = 52.0

app = modal.App("kb-coordinate-vieta-f29-falsifier")
image = modal.Image.debian_slim(python_version="3.12")


def inv(value: int) -> int:
    return pow(value % P, P - 2, P)


def sqrt29(value: int) -> int:
    roots = [candidate for candidate in range(P) if candidate * candidate % P == value % P]
    if not roots:
        raise ValueError(f"{value} is not a square modulo {P}")
    return min(roots)


def rref_and_kernel(matrix: list[list[int]]) -> tuple[int, list[list[int]]]:
    if not matrix:
        return 0, []
    work = [[entry % P for entry in row] for row in matrix]
    row_count = len(work)
    column_count = len(work[0])
    pivots: list[int] = []
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = inv(work[pivot_row][column])
        work[pivot_row] = [entry * scale % P for entry in work[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or not work[row][column]:
                continue
            scale = work[row][column]
            work[row] = [
                (left - scale * right) % P
                for left, right in zip(work[row], work[pivot_row])
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break

    free = [column for column in range(column_count) if column not in pivots]
    basis: list[list[int]] = []
    for free_column in free:
        vector = [0] * column_count
        vector[free_column] = 1
        for row, pivot_column in enumerate(pivots):
            vector[pivot_column] = -work[row][free_column] % P
        basis.append(vector)
    return len(pivots), basis


def dot(left: Iterable[int], right: Iterable[int]) -> int:
    return sum(a * b for a, b in zip(left, right)) % P


def first_supported_vector(
    basis: list[list[int]],
    leading_slice: slice,
    odd_slice: slice,
) -> list[int] | None:
    if not basis:
        return None
    dimension = len(basis)
    if dimension > 3:
        return None
    for coefficients in itertools.product(range(P), repeat=dimension):
        if not any(coefficients):
            continue
        vector = [
            sum(coefficient * basis[index][column]
                for index, coefficient in enumerate(coefficients)) % P
            for column in range(len(basis[0]))
        ]
        leading = vector[leading_slice]
        if any(dot(leading, (1, kappa, kappa * kappa)) == 0
               if len(leading) == 3 else dot(leading, (1, kappa)) == 0
               for kappa in K_POINTS):
            continue
        if not any(vector[odd_slice]):
            continue
        return vector
    return None


def edge_records() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for pair, value in enumerate(J_BASES):
        degree = [0, 0, 0]
        degree[pair] = 2
        records.append({
            "kind": f"loop-{pair}",
            "pair_degree": degree,
            "product": -value * value % P,
            "sum": 0,
            "edge": [value, -value % P],
        })
    for left, right in ((0, 1), (0, 2), (1, 2)):
        degree = [0, 0, 0]
        degree[left] = degree[right] = 1
        a, b = J_BASES[left], J_BASES[right]
        for edge_kind, product, edge_sum, edge in (
            ("same", a * b, a + b, [a, b]),
            ("cross", -a * b, a - b, [a, -b % P]),
        ):
            for orientation in (1, -1):
                oriented_edge = edge if orientation == 1 else [-x % P for x in edge]
                records.append({
                    "kind": f"{left}{right}-{edge_kind}-{'plus' if orientation == 1 else 'minus'}",
                    "pair_degree": degree,
                    "product": product % P,
                    "sum": orientation * edge_sum % P,
                    "edge": oriented_edge,
                })
    assert len(records) == 15
    return records


RECORDS = edge_records()


def matrices(sequence: tuple[int, ...]) -> tuple[list[list[int]], list[list[int]]]:
    positive: list[list[int]] = []
    negative: list[list[int]] = []
    for kappa, record_index in zip(K_POINTS, sequence):
        record = RECORDS[record_index]
        product = int(record["product"])
        weighted_sum = sqrt29(kappa) * int(record["sum"]) % P
        v2 = [1, kappa, kappa * kappa % P]
        positive.extend((
            [(-product * value) % P for value in v2] + v2 + [0, 0],
            [(weighted_sum * value) % P for value in v2]
            + [0, 0, 0, kappa, kappa * kappa % P],
        ))
        negative.extend((
            [-product % P, -product * kappa % P, 1, kappa, 0, 0, 0],
            [weighted_sum, weighted_sum * kappa % P, 0, 0,
             1, kappa, kappa * kappa % P],
        ))
    return positive, negative


def sequence_defect(sequence: tuple[int, ...]) -> int:
    stars = []
    for record_index in sequence:
        edge = tuple(sorted(int(value) % P for value in RECORDS[record_index]["edge"]))
        conjugate = tuple(sorted((-value) % P for value in edge))
        stars.extend((edge, conjugate))
    return sum(count * (count - 1) // 2 for count in Counter(stars).values())


def trim(poly: list[int]) -> list[int]:
    result = [entry % P for entry in poly]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    ])


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * entry for entry in poly])


def multiply(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = (result[i + j] + a * b) % P
    return trim(result)


def product(polynomials: Iterable[list[int]]) -> list[int]:
    result = [1]
    for poly in polynomials:
        result = multiply(result, poly)
    return result


def root_poly(roots: Iterable[int]) -> list[int]:
    return product([[-root % P, 1] for root in roots])


def monic(poly: list[int]) -> list[int]:
    poly = trim(poly)
    if poly == [0]:
        return poly
    return scale(poly, inv(poly[-1]))


def phi_positive(vector: list[int], y_value: int) -> list[int]:
    a2, a0, b1 = vector[0:3], vector[3:6], vector[6:8]
    base = add(scale(a2, y_value), a0)
    return add(multiply(base, base), scale([0] + multiply(b1, b1), -y_value))


def phi_negative(vector: list[int], y_value: int) -> list[int]:
    b2, b0, a1 = vector[0:2], vector[2:4], vector[4:7]
    base = add(scale(b2, y_value), b0)
    return add([0] + multiply(base, base), scale(multiply(a1, a1), -y_value))


def full_quotient_choices(vector: list[int], parity: str) -> list[list[int]]:
    phi = phi_positive if parity == "positive" else phi_negative
    r_j = product(phi(vector, value * value % P) for value in J_BASES)
    r_i = product(phi(vector, value * value % P) for value in I_BASES)
    k5 = root_poly(K_POINTS)
    j_labels = [value for base in J_BASES for value in (base, -base % P)]
    r7 = root_poly([XI, *j_labels])
    matches: list[list[int]] = []
    for roots in itertools.combinations(j_labels, 2):
        c = root_poly(roots)
        if monic(r_j) != monic(multiply(multiply(k5, k5), c)):
            continue
        if monic(multiply(c, r_i)) != monic(multiply(r7, r7)):
            continue
        matches.append(list(roots))
    return matches


def witness(
    sequence: tuple[int, ...],
    pair_degrees: tuple[int, ...],
    rank: int,
    vector: list[int],
    parity: str,
) -> dict[str, object]:
    rows = []
    for kappa, record_index in zip(K_POINTS, sequence):
        record = RECORDS[record_index]
        rows.append({
            "kappa": kappa,
            "sqrt_kappa": sqrt29(kappa),
            "record_index": record_index,
            "kind": record["kind"],
            "edge": record["edge"],
            "product": record["product"],
            "weighted_sum": sqrt29(kappa) * int(record["sum"]) % P,
        })
    return {
        "parity": parity,
        "rank": rank,
        "kernel_vector": vector,
        "pair_degrees": list(pair_degrees),
        "defect": sequence_defect(sequence),
        "rows": rows,
        "aligned_full_quotient_c_roots": full_quotient_choices(vector, parity),
    }


@app.function(image=image, cpu=1.0, memory=256, timeout=60)
def search() -> dict[str, object]:
    started = time.monotonic()
    checked = 0
    profile_sequences = 0
    profile_defect_sequences = 0
    positive_survivors = 0
    negative_survivors = 0
    positive_witness = None
    negative_witness = None
    positive_full_witness = None
    negative_full_witness = None

    for sequence in itertools.product(range(len(RECORDS)), repeat=5):
        checked += 1
        if checked % 4096 == 0 and time.monotonic() - started > DEADLINE_SECONDS:
            return {
                "complete": False,
                "checked_sequences": checked,
                "profile_sequences": profile_sequences,
                "profile_defect_sequences": profile_defect_sequences,
                "positive_gate_survivors": positive_survivors,
                "negative_gate_survivors": negative_survivors,
                "positive_witness": positive_witness,
                "negative_witness": negative_witness,
                "positive_full_witness": positive_full_witness,
                "negative_full_witness": negative_full_witness,
            }
        pair_degrees = tuple(
            sum(int(RECORDS[index]["pair_degree"][pair]) for index in sequence)
            for pair in range(3)
        )
        if sorted(pair_degrees) not in ([2, 4, 4], [3, 3, 4]):
            continue
        profile_sequences += 1
        if sequence_defect(sequence) > 3:
            continue
        profile_defect_sequences += 1
        positive, negative = matrices(sequence)

        positive_rank, positive_basis = rref_and_kernel(positive)
        if positive_rank <= 7:
            vector = first_supported_vector(positive_basis, slice(0, 3), slice(6, 8))
            if vector is not None:
                positive_survivors += 1
                current = witness(
                    sequence, pair_degrees, positive_rank, vector, "positive"
                )
                if positive_witness is None:
                    positive_witness = current
                if current["aligned_full_quotient_c_roots"] and positive_full_witness is None:
                    positive_full_witness = current

        negative_rank, negative_basis = rref_and_kernel(negative)
        if negative_rank <= 6:
            vector = first_supported_vector(negative_basis, slice(0, 2), slice(0, 4))
            if vector is not None:
                negative_survivors += 1
                current = witness(
                    sequence, pair_degrees, negative_rank, vector, "negative"
                )
                if negative_witness is None:
                    negative_witness = current
                if current["aligned_full_quotient_c_roots"] and negative_full_witness is None:
                    negative_full_witness = current

    return {
        "complete": True,
        "field": P,
        "I_bases": list(I_BASES),
        "J_bases": list(J_BASES),
        "xi": XI,
        "K": list(K_POINTS),
        "record_count": len(RECORDS),
        "checked_sequences": checked,
        "profile_sequences": profile_sequences,
        "profile_defect_sequences": profile_defect_sequences,
        "positive_gate_survivors": positive_survivors,
        "negative_gate_survivors": negative_survivors,
        "positive_witness": positive_witness,
        "negative_witness": negative_witness,
        "positive_full_witness": positive_full_witness,
        "negative_full_witness": negative_full_witness,
        "elapsed_seconds": round(time.monotonic() - started, 3),
    }


@app.local_entrypoint()
def main() -> None:
    print("KB_COORDINATE_VIETA_F29 " + json.dumps(search.remote(), sort_keys=True))
