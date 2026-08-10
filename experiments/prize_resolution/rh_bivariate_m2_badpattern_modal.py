#!/usr/bin/env python3
"""Bounded Modal search for m=2 bad-overlap bivariate kernel survivors."""

from __future__ import annotations

import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
RESULT = HERE / "rh_bivariate_m2_badpattern_result.json"
APP = modal.App("rate-half-bivariate-m2-badpattern")

P = 97
M = 2
N = 32
RHO = 7
R = 16
SLOPES = tuple(range(9))


def inverse(value: int) -> int:
    return pow(value % P, P - 2, P)


def primitive_root() -> int:
    for candidate in range(2, P):
        if pow(candidate, 48, P) != 1 and pow(candidate, 32, P) != 1:
            return candidate
    raise AssertionError("no primitive root")


GENERATOR = primitive_root()
ZETA = pow(GENERATOR, 3, P)
DOMAIN = tuple(pow(ZETA, index, P) for index in range(N))
assert len(set(DOMAIN)) == N and pow(ZETA, N, P) == 1


def poly_multiply(left: list[int], right: list[int]) -> list[int]:
    output = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] = (output[i + j] + a * b) % P
    return output


def root_product(roots: tuple[int, ...]) -> list[int]:
    output = [1]
    for root in roots:
        output = poly_multiply(output, [(-root) % P, 1])
    return output


def matrix_rank(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    rows = [row[:] for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next(
            (row for row in range(rank, len(rows)) if rows[row][column]),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = inverse(rows[rank][column])
        rows[rank] = [entry * scale % P for entry in rows[rank]]
        for row in range(len(rows)):
            if row == rank or not rows[row][column]:
                continue
            factor = rows[row][column]
            rows[row] = [
                (entry - factor * base) % P
                for entry, base in zip(rows[row], rows[rank])
            ]
        rank += 1
    return rank


def nullspace(matrix: list[list[int]]) -> list[list[int]]:
    rows = [row[:] for row in matrix]
    width = len(rows[0])
    pivots = []
    rank = 0
    for column in range(width):
        pivot = next(
            (row for row in range(rank, len(rows)) if rows[row][column]),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = inverse(rows[rank][column])
        rows[rank] = [entry * scale % P for entry in rows[rank]]
        for row in range(len(rows)):
            if row == rank or not rows[row][column]:
                continue
            factor = rows[row][column]
            rows[row] = [
                (entry - factor * base) % P
                for entry, base in zip(rows[row], rows[rank])
            ]
        pivots.append(column)
        rank += 1
    free = [column for column in range(width) if column not in pivots]
    basis = []
    for free_column in free:
        vector = [0] * width
        vector[free_column] = 1
        for row, pivot_column in enumerate(pivots):
            vector[pivot_column] = -rows[row][free_column] % P
        basis.append(vector)
    return basis


def solve_square(matrix: list[list[int]], target: list[int]) -> list[int] | None:
    size = len(matrix)
    rows = [matrix[row][:] + [target[row] % P] for row in range(size)]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if rows[row][column]),
            None,
        )
        if pivot is None:
            return None
        rows[column], rows[pivot] = rows[pivot], rows[column]
        scale = inverse(rows[column][column])
        rows[column] = [entry * scale % P for entry in rows[column]]
        for row in range(size):
            if row == column or not rows[row][column]:
                continue
            factor = rows[row][column]
            rows[row] = [
                (entry - factor * base) % P
                for entry, base in zip(rows[row], rows[column])
            ]
    return [rows[index][-1] for index in range(size)]


def random_incidence(rng) -> tuple[list[set[int]], list[tuple[int, ...]], int] | None:
    deficient = rng.randrange(N)
    column_stubs = []
    for column in range(N):
        column_stubs.extend([column] * (1 if column == deficient else 2))
    row_stubs = [slope for slope in SLOPES for _ in range(RHO)]
    for _ in range(24):
        rng.shuffle(row_stubs)
        owners = [[] for _ in range(N)]
        for slope, column in zip(row_stubs, column_stubs):
            owners[column].append(slope)
        if all(len(values) == len(set(values)) for values in owners):
            root_sets = [set() for _ in SLOPES]
            for column, values in enumerate(owners):
                for slope in values:
                    root_sets[slope].add(column)
            assert all(len(row) == RHO for row in root_sets)
            return root_sets, [tuple(sorted(values)) for values in owners], deficient
    return None


def build_matrix(
    owners: list[tuple[int, ...]],
    deficient: int,
    first: int,
    second: int,
    rng,
):
    first_set = {column for column, values in enumerate(owners) if first in values}
    second_set = {column for column, values in enumerate(owners) if second in values}
    support = tuple(sorted(first_set | second_set))
    blocks = []
    columns = []
    mus = {}
    for column in support:
        values = owners[column]
        in_first = first in values
        in_second = second in values
        if in_first and not in_second:
            mu = second
        elif in_second and not in_first:
            mu = first
        else:
            choices = [slope for slope in SLOPES if slope not in (first, second)]
            mu = rng.choice(choices)
        mus[column] = mu
        base = poly_multiply([(-mu) % P, 1], root_product(values))
        delta = M - len(values)
        indices = []
        for quotient_degree in range(delta + 1):
            indices.append(len(columns))
            columns.append((column, [0] * quotient_degree + base))
        blocks.append((column, tuple(indices), values))

    matrix = []
    for moment in range(4 * M + 1):
        for degree in range(M + 2):
            matrix.append(
                [
                    (poly[degree] if degree < len(poly) else 0)
                    * pow(DOMAIN[column], moment, P)
                    % P
                    for column, poly in columns
                ]
            )
    return matrix, blocks, support, mus


def blockwise_vector(basis: list[list[int]], blocks, rng) -> list[int] | None:
    if not basis:
        return None

    def valid(vector):
        return all(any(vector[index] for index in indices) for _, indices, _ in blocks)

    if len(basis) == 1:
        return basis[0] if valid(basis[0]) else None
    candidates = basis[:]
    for _ in range(256):
        coefficients = [rng.randrange(P) for _ in basis]
        if not any(coefficients):
            continue
        candidates.append(
            [
                sum(coefficient * vector[index] for coefficient, vector in zip(coefficients, basis))
                % P
                for index in range(len(basis[0]))
            ]
        )
    return next((vector for vector in candidates if valid(vector)), None)


def interpolate_extension(vector, blocks, support):
    q_values = [[0] * len(support) for _ in range(M + 1)]
    for support_index, (column, indices, roots) in enumerate(blocks):
        quotient = [vector[index] for index in indices]
        q_at_x = poly_multiply(root_product(roots), quotient)
        q_at_x += [0] * (M + 1 - len(q_at_x))
        for degree in range(M + 1):
            q_values[degree][support_index] = q_at_x[degree]

    sample = support[: RHO + 1]
    vandermonde = [
        [pow(DOMAIN[column], degree, P) for degree in range(RHO + 1)]
        for column in sample
    ]
    coefficient_polys = []
    for parameter_degree in range(M + 1):
        coefficients = solve_square(
            vandermonde,
            q_values[parameter_degree][: RHO + 1],
        )
        if coefficients is None:
            return None
        for support_index, column in enumerate(support):
            value = sum(
                coefficient * pow(DOMAIN[column], degree, P)
                for degree, coefficient in enumerate(coefficients)
            ) % P
            if value != q_values[parameter_degree][support_index]:
                return None
        coefficient_polys.append(coefficients)
    if matrix_rank(coefficient_polys) != M + 1:
        return None
    return coefficient_polys


def verify_full_witness(coefficient_polys, owners, first, second, mus):
    def q_at(column, parameter):
        values = [
            sum(
                coefficient * pow(DOMAIN[column], degree, P)
                for degree, coefficient in enumerate(poly)
            )
            % P
            for poly in coefficient_polys
        ]
        if parameter is None:
            return values[M]
        return sum(value * pow(parameter, index, P) for index, value in enumerate(values)) % P

    for column, roots in enumerate(owners):
        values = [q_at(column, slope) for slope in SLOPES]
        if {slope for slope, value in zip(SLOPES, values) if value == 0} != set(roots):
            return None

    supported = {}
    for parameter in tuple(range(P)) + (None,):
        roots = tuple(column for column in range(N) if q_at(column, parameter) == 0)
        if len(roots) == RHO:
            supported[parameter] = roots
    if len(supported) != len(SLOPES):
        return None
    for slope in SLOPES:
        expected = tuple(column for column, roots in enumerate(owners) if slope in roots)
        if supported.get(slope) != expected:
            return None

    c0 = [0] * N
    c1 = [0] * N
    for column, mu in mus.items():
        c0[column] = -mu % P
        c1[column] = 1
    y0 = [sum(c0[column] * pow(DOMAIN[column], moment, P) for column in range(N)) % P for moment in range(R)]
    y1 = [sum(c1[column] * pow(DOMAIN[column], moment, P) for column in range(N)) % P for moment in range(R)]
    for slope in SLOPES:
        moments = [(a + slope * b) % P for a, b in zip(y0, y1)]
        hankel = [[moments[row + column] for column in range(RHO + 1)] for row in range(R - RHO)]
        locator = [
            sum(
                pow(slope, parameter_degree, P)
                * coefficient_polys[parameter_degree][x_degree]
                for parameter_degree in range(M + 1)
            )
            % P
            for x_degree in range(RHO + 1)
        ]
        assert all(
            sum(entry * coefficient for entry, coefficient in zip(row, locator)) % P == 0
            for row in hankel
        )
        if matrix_rank(hankel) != RHO:
            return None
    first_support = {column for column, roots in enumerate(owners) if first in roots}
    second_support = {column for column, roots in enumerate(owners) if second in roots}
    if {column for column in mus if (c0[column] + first * c1[column]) % P} != first_support:
        return None
    if {column for column in mus if (c0[column] + second * c1[column]) % P} != second_support:
        return None
    return {
        "coefficient_polys": coefficient_polys,
        "supported_slopes": sorted(SLOPES),
        "y0": y0,
        "y1": y1,
    }


def search_core(seed: int, seconds: float, trial_cap: int) -> dict[str, object]:
    import random
    import time

    rng = random.Random(seed)
    started = time.monotonic()
    counters = {
        "attempted": 0,
        "regular_incidence": 0,
        "open_pair": 0,
        "bad_overlap": 0,
        "rank_deficient": 0,
        "blockwise_kernel": 0,
        "degree_extension": 0,
        "full_witness": 0,
    }
    witnesses = []
    while counters["attempted"] < trial_cap and time.monotonic() - started < seconds:
        counters["attempted"] += 1
        generated = random_incidence(rng)
        if generated is None:
            continue
        root_sets, owners, deficient = generated
        counters["regular_incidence"] += 1
        intersections = {
            (first, second): len(root_sets[first] & root_sets[second])
            for first in SLOPES
            for second in SLOPES
            if first < second
        }
        maximum = max(intersections.values())
        a_star = 2 * RHO - maximum
        if not (11 <= a_star <= 13):
            continue
        pairs = [pair for pair, value in intersections.items() if value == maximum]
        rng.shuffle(pairs)
        for first, second in pairs[:4]:
            counters["open_pair"] += 1
            support = root_sets[first] | root_sets[second]
            need_x = RHO - ((N - len(support)) * M // (len(SLOPES) - 2) + 1)
            worst_x = max(
                len(root_sets[slope] & support)
                for slope in SLOPES
                if slope not in (first, second)
            )
            if worst_x <= need_x:
                continue
            counters["bad_overlap"] += 1
            matrix, blocks, ordered_support, mus = build_matrix(
                owners,
                deficient,
                first,
                second,
                rng,
            )
            basis = nullspace(matrix)
            if not basis:
                continue
            counters["rank_deficient"] += 1
            vector = blockwise_vector(basis, blocks, rng)
            if vector is None:
                continue
            counters["blockwise_kernel"] += 1
            extension = interpolate_extension(vector, blocks, ordered_support)
            if extension is None:
                continue
            counters["degree_extension"] += 1
            full = verify_full_witness(extension, owners, first, second, mus)
            if full is None:
                continue
            counters["full_witness"] += 1
            if len(witnesses) < 2:
                witnesses.append(
                    {
                        "seed": seed,
                        "deficient": deficient,
                        "owners": [list(values) for values in owners],
                        "pair": [first, second],
                        "a_star": a_star,
                        "need_x": need_x,
                        "worst_x": worst_x,
                        "mus": {str(column): mu for column, mu in mus.items()},
                        "kernel": vector,
                        **full,
                    }
                )
    return {
        "seed": seed,
        "elapsed": time.monotonic() - started,
        "counters": counters,
        "witnesses": witnesses,
    }


@APP.function(cpu=1.0, memory=256, timeout=60, max_containers=40)
def search_seed(seed: int, seconds: float, trial_cap: int) -> dict[str, object]:
    return search_core(seed, seconds, trial_cap)


@APP.local_entrypoint()
def main(tasks: int = 32, seconds: float = 45.0, trial_cap: int = 200000) -> None:
    rows = []

    def checkpoint(complete: bool, error: str | None = None):
        keys = (
            "attempted",
            "regular_incidence",
            "open_pair",
            "bad_overlap",
            "rank_deficient",
            "blockwise_kernel",
            "degree_extension",
            "full_witness",
        )
        totals = {
            key: sum(int(row["counters"][key]) for row in rows) for key in keys
        }
        packet = {
            "schema": "rate-half-bivariate-m2-badpattern-v1",
            "complete": complete,
            "error": error,
            "parameters": {
                "field": P,
                "m": M,
                "tasks": tasks,
                "seconds_per_task": seconds,
                "trial_cap_per_task": trial_cap,
            },
            "completed_tasks": len(rows),
            "totals": totals,
            "witnesses": [witness for row in rows for witness in row["witnesses"]],
            "rows": sorted(rows, key=lambda row: int(row["seed"])),
        }
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        return packet

    checkpoint(False)
    try:
        for row in search_seed.map(
            range(tasks),
            [seconds] * tasks,
            [trial_cap] * tasks,
        ):
            rows.append(row)
            checkpoint(False)
    except BaseException as error:
        packet = checkpoint(False, f"{type(error).__name__}: {error}")
        print("RATE_HALF_BIVARIATE_M2_BADPATTERN_INCOMPLETE " + json.dumps(packet["totals"], sort_keys=True))
        raise
    packet = checkpoint(len(rows) == tasks)
    print("RATE_HALF_BIVARIATE_M2_BADPATTERN " + json.dumps(packet["totals"], sort_keys=True))
    print(f"RATE_HALF_BIVARIATE_M2_BADPATTERN_COMPLETE {packet['complete']}")
    print(f"RATE_HALF_BIVARIATE_M2_BADPATTERN_RESULT {RESULT}")
