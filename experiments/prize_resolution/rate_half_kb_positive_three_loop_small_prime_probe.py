#!/usr/bin/env python3
"""Bounded F_13 probe of the eight positive three-loop Vieta lanes."""

import itertools
import json
import os
import time


PRIME = int(os.environ.get("KB_PROBE_PRIME", "13"))
TIME_LIMIT_SECONDS = int(os.environ.get("KB_PROBE_SECONDS", "45"))
SURVIVOR_LIMIT = int(os.environ.get("KB_PROBE_SURVIVORS", "20"))
EDGE_LABELS = (
    "colored-left",
    "colored-right",
    "de-plus",
    "de-minus",
    "df-plus",
    "df-minus",
    "ef-cycle",
)

COMMON_RECORDS = {
    "442_root_low": lambda b, c, x, y: ((x, b, 1 + b), (y, -b, 1 - b)),
    "442_root_high": lambda b, c, x, y: ((x, c, 1 + c), (y, -c, 1 - c)),
    "433_root_low": lambda b, c, x, y: ((x, b, 1 + b), (y, c, 1 + c)),
    "433_root_high": lambda b, c, x, y: ((x, c, 1 + c), (y, b * c, b + c)),
}

COLORED_ENDPOINTS = {
    "442_root_low": lambda b, c: (c, c),
    "442_root_high": lambda b, c: (b, b),
    "433_root_low": lambda b, c: (b, c),
    "433_root_high": lambda b, c: (1, b),
}


def inverse(value):
    return pow(value % PRIME, PRIME - 2, PRIME)


def matrix_rows(b, c, records):
    rows = []
    for source, product, target_sum in records:
        w = source * source % PRIME
        rows.append((
            -1 + (1 - c * c) * w - product,
            -(c * c + product) * w,
            (b * b - c * c) * w - (b * b + product) * w * w,
            0,
        ))
        rows.append((target_sum, target_sum * w, target_sum * w * w,
                     source * (w - 1)))
    return [[value % PRIME for value in row] for row in rows]


def nullspace(matrix):
    rows = [row[:] for row in matrix]
    pivot_columns = []
    pivot_row = 0
    for column in range(4):
        selected = next(
            (row for row in range(pivot_row, len(rows)) if rows[row][column]),
            None,
        )
        if selected is None:
            continue
        rows[pivot_row], rows[selected] = rows[selected], rows[pivot_row]
        scale = inverse(rows[pivot_row][column])
        rows[pivot_row] = [value * scale % PRIME for value in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row or rows[row][column] == 0:
                continue
            factor = rows[row][column]
            rows[row] = [
                (left - factor * right) % PRIME
                for left, right in zip(rows[row], rows[pivot_row])
            ]
        pivot_columns.append(column)
        pivot_row += 1
    free_columns = [column for column in range(4) if column not in pivot_columns]
    basis = []
    for free in free_columns:
        vector = [0] * 4
        vector[free] = 1
        for row, pivot in enumerate(pivot_columns):
            vector[pivot] = -rows[row][free] % PRIME
        basis.append(tuple(vector))
    return tuple(basis)


def projective_kernel_vectors(basis):
    dimension = len(basis)
    for first_nonzero in range(dimension):
        tail_length = dimension - first_nonzero - 1
        for tail in itertools.product(range(PRIME), repeat=tail_length):
            coefficients = (0,) * first_nonzero + (1,) + tail
            yield tuple(
                sum(coefficients[index] * basis[index][coordinate]
                    for index in range(dimension)) % PRIME
                for coordinate in range(4)
            )


def coefficient_values(b, c, kernel, w):
    d0, d1, d2, beta = kernel
    denominator = (d0 + d1 * w + d2 * w * w) % PRIME
    middle = ((1 - c * c) * d0 - c * c * d1
              + (b * b - c * c) * d2) % PRIME
    numerator = (-d0 + middle * w - b * b * d2 * w * w) % PRIME
    return denominator, numerator, beta


def outside_record_map(b, c, x, y, kernel):
    forbidden = {0, 1, x * x % PRIME, y * y % PRIME}
    result = {}
    for w in range(PRIME):
        if w in forbidden:
            continue
        denominator, numerator, beta = coefficient_values(b, c, kernel, w)
        if denominator == 0 or beta == 0:
            continue
        product = numerator * inverse(denominator) % PRIME
        squared_sum = (
            beta * beta * w * (w - 1) * (w - 1)
            * inverse(denominator * denominator)
        ) % PRIME
        result.setdefault((product, squared_sum), set()).add(w)
    return result


def target_edges(placement, cycle_sign, b, c, d, e, f):
    left, right = COLORED_ENDPOINTS[placement](b, c)
    signed = (
        (left, e, 1),
        (right, f, 1),
        (d, e, 1),
        (d, e, -1),
        (d, f, 1),
        (d, f, -1),
        (e, f, cycle_sign),
    )
    return tuple(
        (
            edge_sign * source * target % PRIME,
            (source * source + target * target
             + 2 * edge_sign * source * target) % PRIME,
        )
        for source, target, edge_sign in signed
    )


def distinct_matching(candidate_sets):
    ordered = sorted(candidate_sets, key=len)

    def search(index, used):
        if index == len(ordered):
            return ()
        for label in sorted(ordered[index] - used):
            suffix = search(index + 1, used | {label})
            if suffix is not None:
                return (label,) + suffix
        return None

    return search(0, set())


def common_guard(b, c, x, y, kernel):
    target_squares = {1, b * b % PRIME, c * c % PRIME}
    source_squares = {x * x % PRIME, y * y % PRIME}
    if len(target_squares) != 3 or 0 in target_squares:
        return False
    if len(source_squares) != 2 or source_squares & {0, 1}:
        return False
    d0, _, d2, beta = kernel
    if d0 == 0 or d2 == 0 or beta == 0:
        return False
    for w in (1, x * x % PRIME, y * y % PRIME):
        if coefficient_values(b, c, kernel, w)[0] == 0:
            return False
    return True


def outside_assignments(b, c):
    common_squares = {1, b * b % PRIME, c * c % PRIME}
    values = [value for value in range(1, PRIME)
              if value * value % PRIME not in common_squares]
    for d, e, f in itertools.permutations(values, 3):
        if len({d * d % PRIME, e * e % PRIME, f * f % PRIME}) == 3:
            yield d, e, f


def run_probe():
    started = time.monotonic()
    counts = {
        "common_tuples": 0,
        "singular_common_matrices": 0,
        "admissible_kernels": 0,
        "target_assignments": 0,
        "record_complete": 0,
        "distinct_matchings": 0,
    }
    lane_counts = {
        f"{placement}:{cycle_sign:+d}": 0
        for placement in COMMON_RECORDS
        for cycle_sign in (-1, 1)
    }
    analytics = {
        lane: {"max_present": 0, "best": None}
        for lane in lane_counts
    }
    survivors = []
    timed_out = False
    for placement, records_function in COMMON_RECORDS.items():
        for b in range(1, PRIME):
            for c in range(1, PRIME):
                if len({1, b * b % PRIME, c * c % PRIME}) != 3:
                    continue
                for x in range(1, PRIME):
                    for y in range(1, PRIME):
                        if time.monotonic() - started >= TIME_LIMIT_SECONDS:
                            timed_out = True
                            return counts, lane_counts, analytics, survivors, timed_out
                        if len({0, 1, x * x % PRIME, y * y % PRIME}) != 4:
                            continue
                        counts["common_tuples"] += 1
                        records = records_function(b, c, x, y)
                        basis = nullspace(matrix_rows(b, c, records))
                        if not basis:
                            continue
                        counts["singular_common_matrices"] += 1
                        for kernel in projective_kernel_vectors(basis):
                            if not common_guard(b, c, x, y, kernel):
                                continue
                            counts["admissible_kernels"] += 1
                            record_map = outside_record_map(b, c, x, y, kernel)
                            for d, e, f in outside_assignments(b, c):
                                counts["target_assignments"] += 1
                                for cycle_sign in (-1, 1):
                                    edges = target_edges(
                                        placement, cycle_sign, b, c, d, e, f
                                    )
                                    candidates = [record_map.get(edge, set()) for edge in edges]
                                    lane = f"{placement}:{cycle_sign:+d}"
                                    present = tuple(
                                        EDGE_LABELS[index]
                                        for index, candidate in enumerate(candidates)
                                        if candidate
                                    )
                                    if len(present) > analytics[lane]["max_present"]:
                                        analytics[lane] = {
                                            "max_present": len(present),
                                            "best": {
                                                "b": b,
                                                "c": c,
                                                "x": x,
                                                "y": y,
                                                "kernel": kernel,
                                                "d": d,
                                                "e": e,
                                                "f": f,
                                                "present": present,
                                            },
                                        }
                                    if any(not candidate for candidate in candidates):
                                        continue
                                    counts["record_complete"] += 1
                                    matching = distinct_matching(candidates)
                                    if matching is None:
                                        continue
                                    counts["distinct_matchings"] += 1
                                    lane_counts[lane] += 1
                                    survivors.append({
                                        "lane": lane,
                                        "b": b,
                                        "c": c,
                                        "x": x,
                                        "y": y,
                                        "kernel": kernel,
                                        "d": d,
                                        "e": e,
                                        "f": f,
                                        "matching_sorted_order": matching,
                                    })
                                    if len(survivors) >= SURVIVOR_LIMIT:
                                        return counts, lane_counts, analytics, survivors, timed_out
    return counts, lane_counts, analytics, survivors, timed_out


def main():
    counts, lane_counts, analytics, survivors, timed_out = run_probe()
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_SMALL_PRIME_PROBE "
        f"prime={PRIME} timed_out={int(timed_out)} survivors={len(survivors)} "
        f"counts={json.dumps(counts, sort_keys=True, separators=(',', ':'))} "
        f"lane_counts={json.dumps(lane_counts, sort_keys=True, separators=(',', ':'))} "
        f"max_present={json.dumps({lane: data['max_present'] for lane, data in analytics.items()}, sort_keys=True, separators=(',', ':'))}"
    )
    print("BEST_PARTIAL " + json.dumps(analytics, sort_keys=True))
    if survivors:
        print("FIRST_SURVIVOR " + json.dumps(survivors[0], sort_keys=True))


if __name__ == "__main__":
    main()
