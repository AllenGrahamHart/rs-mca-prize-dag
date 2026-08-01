#!/usr/bin/env python3
"""Capped Modal product-rank probe for the positive 433-1a/O0b lanes."""

import itertools
import json
import time

import modal


app = modal.App("rs-mca-positive-433-1a-o0b-f29-product-probe")
PRIME = 29
PAIR_REPRESENTATIVES = (1, 4, 5, 6, 7, 9, 13)


def product_row(kappa, product):
    kappa %= PRIME
    product %= PRIME
    return [
        -product % PRIME,
        -product * kappa % PRIME,
        -product * kappa * kappa % PRIME,
        1,
        kappa,
        kappa * kappa % PRIME,
    ]


def rank_five_kernel(rows):
    matrix = [[value % PRIME for value in row] for row in rows]
    pivot_columns = []
    pivot_row = 0
    for column in range(6):
        pivot = next(
            (row for row in range(pivot_row, len(matrix)) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column], -1, PRIME)
        matrix[pivot_row] = [value * inverse % PRIME for value in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row:
                continue
            scale = matrix[row][column]
            if scale:
                matrix[row] = [
                    (left - scale * right) % PRIME
                    for left, right in zip(matrix[row], matrix[pivot_row])
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    if pivot_row != 5:
        return pivot_row, None
    free_column = next(column for column in range(6) if column not in pivot_columns)
    kernel = [0] * 6
    kernel[free_column] = 1
    for row, column in enumerate(pivot_columns):
        kernel[column] = -matrix[row][free_column] % PRIME
    return 5, kernel


def evaluate(coefficients, point):
    return (
        coefficients[0]
        + coefficients[1] * point
        + coefficients[2] * point * point
    ) % PRIME


def unique_permutations(values):
    return tuple(sorted(set(itertools.permutations(values))))


@app.function(cpu=0.5, memory=256, timeout=60, max_containers=2)
def probe_cycle(cycle_sign):
    started = time.monotonic()
    deadline = started + 50.0
    counters = {
        "target_assignments": 0,
        "common_placements": 0,
        "rank_below_five": 0,
        "leading_support_failures": 0,
        "separator_survivors": 0,
        "complete_product_survivors": 0,
    }
    examples = []
    completed = True
    for values in itertools.permutations(PAIR_REPRESENTATIVES, 6):
        if time.monotonic() >= deadline:
            completed = False
            break
        counters["target_assignments"] += 1
        a, b, c, d, e, f = values
        source_k = (d, -d, e, -e, f)
        source_eta = -f
        source_lc = (a, -a, b, -b, c, -c)
        all_source = source_k + (source_eta,) + source_lc
        common_products = (-c * c, a * b, a * b, -a * b, a * c)
        internal_products = [d * e, -d * e, d * f, -d * f,
                             cycle_sign * e * f]
        colored_products = [b * e, c * f]

        for placement in unique_permutations(common_products):
            counters["common_placements"] += 1
            rank, kernel = rank_five_kernel(
                [product_row(kappa, product)
                 for kappa, product in zip(source_k, placement)]
            )
            if rank != 5:
                counters["rank_below_five"] += 1
                continue
            denominator = kernel[:3]
            numerator = kernel[3:]
            denominator_values = [
                evaluate(denominator, point % PRIME) for point in all_source
            ]
            if any(value == 0 for value in denominator_values):
                counters["leading_support_failures"] += 1
                continue
            predicted = [
                evaluate(numerator, point % PRIME)
                * pow(denominator_values[index], -1, PRIME) % PRIME
                for index, point in enumerate(all_source)
            ]
            eta_product = predicted[5]
            reduced_internal = [value % PRIME for value in internal_products]
            try:
                reduced_internal.remove(eta_product)
            except ValueError:
                continue
            counters["separator_survivors"] += 1
            expected_lc = sorted(
                reduced_internal + [value % PRIME for value in colored_products]
            )
            if sorted(predicted[6:]) != expected_lc:
                continue
            counters["complete_product_survivors"] += 1
            if len(examples) < 8:
                examples.append({
                    "pair_assignment": values,
                    "common_placement": placement,
                    "kernel": kernel,
                    "eta_product": eta_product,
                    "predicted_lc": predicted[6:],
                    "expected_lc": expected_lc,
                })

    return {
        "field": PRIME,
        "cycle_sign": cycle_sign,
        "completed": completed,
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "counters": counters,
        "examples": examples,
        "scope": (
            "banked aligned F29 fixture product rows only; source-sum rows, "
            "universal fields, and packet existence are not decided"
        ),
    }


@app.local_entrypoint()
def main():
    results = list(probe_cycle.map((-1, 1)))
    print(json.dumps({"results": results}, indent=2, sort_keys=True))
