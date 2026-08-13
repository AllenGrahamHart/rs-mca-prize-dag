#!/usr/bin/env python3
"""Scan every e=7 excess partition for all-excess MDS rank loss."""

import random

from verify import (
    all_excess_matrix,
    matrix_rank,
    primitive_root,
    switched_copy,
)


TRIALS = 20


def partitions(total, ceiling=None):
    if total == 0:
        yield ()
        return
    if ceiling is None or ceiling > total:
        ceiling = total
    for first in range(ceiling, 0, -1):
        for tail in partitions(total - first, first):
            yield (first, *tail)


def incidence_with_column_degrees(column_degrees, offset):
    incidence = [set() for _ in range(28)]
    remaining = [5] * 28
    order = sorted(
        range(21), key=lambda column: (-column_degrees[column], column)
    )
    for column in order:
        degree = column_degrees[column]
        choices = sorted(
            range(28),
            key=lambda row: (-remaining[row], (row - offset * column) % 28),
        )
        chosen = [row for row in choices if remaining[row] > 0][:degree]
        if len(chosen) != degree:
            raise AssertionError("non-graphical degree sequence")
        for row in chosen:
            incidence[row].add(column)
            remaining[row] -= 1
    if any(remaining) or any(len(row) != 5 for row in incidence):
        raise AssertionError("row degree construction")
    return incidence


def replay():
    profiles = list(partitions(7))
    assert len(profiles) == 15
    report = {}
    minimum_rank = 28
    deficient = []
    for modulus in (337, 421):
        generator = primitive_root(modulus)
        domain = [
            pow(generator, (modulus - 1) // 28 * exponent, modulus)
            for exponent in range(28)
        ]
        slopes = [
            pow(generator, (modulus - 1) // 21 * exponent, modulus)
            for exponent in range(21)
        ]
        field_histogram = {}
        for profile_index, profile in enumerate(profiles):
            deficits = list(profile) + [0] * (21 - len(profile))
            column_degrees = [7 - deficit for deficit in deficits]
            base = incidence_with_column_degrees(
                column_degrees, profile_index + 1
            )
            candidates = [base]
            rng = random.Random(20260813 + 1000 * profile_index + modulus)
            candidates.extend(
                switched_copy(base, rng) for _ in range(TRIALS)
            )
            profile_histogram = {}
            for candidate in candidates:
                rows, columns = all_excess_matrix(
                    candidate, domain, slopes, modulus
                )
                rank = matrix_rank(rows, columns, modulus)
                profile_histogram[rank] = profile_histogram.get(rank, 0) + 1
                minimum_rank = min(minimum_rank, rank)
                if rank < columns:
                    deficient.append((modulus, profile, rank))
            field_histogram[profile] = profile_histogram
        report[modulus] = field_histogram
    return profiles, minimum_rank, deficient, report


if __name__ == "__main__":
    profiles, minimum_rank, deficient, report = replay()
    print(
        "RATE_HALF_SHAPE_A_ALL_EXCESS_PARTITION_PROBE "
        f"profiles={len(profiles)} cases={sum(sum(hist.values()) for field in report.values() for hist in field.values())} "
        f"minimum_rank={minimum_rank} deficient={deficient}"
    )
