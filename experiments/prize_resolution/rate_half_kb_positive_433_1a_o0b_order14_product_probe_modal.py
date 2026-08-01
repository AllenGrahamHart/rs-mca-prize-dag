#!/usr/bin/env python3
"""Cross-characteristic order-14 product probe for 433-1a/O0b."""

import itertools
import json
import time
from collections import Counter

import modal


app = modal.App("rs-mca-positive-433-1a-o0b-order14-product-probe")
PRIMES = (29, 43, 71, 113)


def order14_representatives(prime):
    generator = next(
        value
        for value in range(2, prime)
        if len({pow(value, exponent, prime) for exponent in range(14)}) == 14
        and pow(value, 7, prime) == prime - 1
    )
    representatives = tuple(sorted({
        min(pow(generator, exponent, prime),
            -pow(generator, exponent, prime) % prime)
        for exponent in range(7)
    }))
    if len(representatives) != 7:
        raise RuntimeError("order-14 antipodal representatives")
    return generator, representatives


def product_row(kappa, product, prime):
    kappa %= prime
    product %= prime
    return [
        -product % prime,
        -product * kappa % prime,
        -product * kappa * kappa % prime,
        1,
        kappa,
        kappa * kappa % prime,
    ]


def rank_five_kernel(rows, prime):
    matrix = [[value % prime for value in row] for row in rows]
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
        inverse = pow(matrix[pivot_row][column], -1, prime)
        matrix[pivot_row] = [value * inverse % prime for value in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row:
                continue
            scale = matrix[row][column]
            if scale:
                matrix[row] = [
                    (left - scale * right) % prime
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
        kernel[column] = -matrix[row][free_column] % prime
    return 5, kernel


def evaluate(coefficients, point, prime):
    return (
        coefficients[0]
        + coefficients[1] * point
        + coefficients[2] * point * point
    ) % prime


def elementary_symmetric(values, prime):
    coefficients = [1] + [0] * len(values)
    used = 0
    for value in values:
        used += 1
        for degree in range(used, 0, -1):
            coefficients[degree] = (
                coefficients[degree] + value * coefficients[degree - 1]
            ) % prime
    return tuple(coefficients[1:])


@app.function(cpu=0.5, memory=256, timeout=60, max_containers=8)
def probe_case(case):
    prime, cycle_sign = case
    generator, pair_representatives = order14_representatives(prime)
    started = time.monotonic()
    deadline = started + 50.0
    counters = {
        "target_assignments": 0,
        "distinct_common_row_placements": 0,
        "rank_below_five": 0,
        "leading_support_failures": 0,
        "separator_survivors": 0,
        "complete_product_survivors": 0,
    }
    elementary_equal_counts = [0] * 6
    prefix_equal_counts = [0] * 7
    overlap_histogram = [0] * 7
    maximum_overlap = -1
    maximum_overlap_examples = []
    examples = []
    completed = True
    for values in itertools.permutations(pair_representatives, 6):
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
        common_placements = set(itertools.permutations(common_products))
        internal_products = [d * e, -d * e, d * f, -d * f,
                             cycle_sign * e * f]
        colored_products = [b * e, c * f]

        for placement in common_placements:
            counters["distinct_common_row_placements"] += 1
            rank, kernel = rank_five_kernel(
                [product_row(kappa, product, prime)
                 for kappa, product in zip(source_k, placement)],
                prime,
            )
            if rank != 5:
                counters["rank_below_five"] += 1
                continue
            denominator = kernel[:3]
            numerator = kernel[3:]
            denominator_values = [
                evaluate(denominator, point % prime, prime)
                for point in all_source
            ]
            if any(value == 0 for value in denominator_values):
                counters["leading_support_failures"] += 1
                continue
            predicted = [
                evaluate(numerator, point % prime, prime)
                * pow(denominator_values[index], -1, prime) % prime
                for index, point in enumerate(all_source)
            ]
            eta_product = predicted[5]
            reduced_internal = [value % prime for value in internal_products]
            try:
                reduced_internal.remove(eta_product)
            except ValueError:
                continue
            counters["separator_survivors"] += 1
            expected_lc = sorted(
                reduced_internal + [value % prime for value in colored_products]
            )
            predicted_lc = sorted(predicted[6:])
            observed_es = elementary_symmetric(predicted_lc, prime)
            expected_es = elementary_symmetric(expected_lc, prime)
            for index, (observed, expected) in enumerate(zip(observed_es, expected_es)):
                if observed == expected:
                    elementary_equal_counts[index] += 1
            prefix = 0
            while prefix < 6 and observed_es[prefix] == expected_es[prefix]:
                prefix += 1
            prefix_equal_counts[prefix] += 1
            overlap = sum((Counter(predicted_lc) & Counter(expected_lc)).values())
            overlap_histogram[overlap] += 1
            if overlap > maximum_overlap:
                maximum_overlap = overlap
                maximum_overlap_examples = []
            if overlap == maximum_overlap and len(maximum_overlap_examples) < 6:
                maximum_overlap_examples.append({
                    "pair_assignment": values,
                    "common_placement": placement,
                    "eta_product": eta_product,
                    "predicted_lc": predicted_lc,
                    "expected_lc": expected_lc,
                    "elementary_observed": observed_es,
                    "elementary_expected": expected_es,
                })
            if predicted_lc != expected_lc:
                continue
            counters["complete_product_survivors"] += 1
            if len(examples) < 4:
                examples.append({
                    "pair_assignment": values,
                    "common_placement": placement,
                    "kernel": kernel,
                    "eta_product": eta_product,
                })
    return {
        "prime": prime,
        "order14_generator": generator,
        "pair_representatives": pair_representatives,
        "cycle_sign": cycle_sign,
        "completed": completed,
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "counters": counters,
        "elementary_equal_counts": elementary_equal_counts,
        "prefix_equal_counts": prefix_equal_counts,
        "multiset_overlap_histogram": overlap_histogram,
        "maximum_overlap_examples": maximum_overlap_examples,
        "examples": examples,
    }


@app.local_entrypoint()
def main():
    cases = tuple(itertools.product(PRIMES, (-1, 1)))
    results = list(probe_case.map(cases))
    print(json.dumps({
        "results": sorted(results, key=lambda row: (row["prime"], row["cycle_sign"])),
        "scope": (
            "aligned order-14 subgroup fixture product rows only; no source-sum, "
            "universal-field, or packet-existence conclusion"
        ),
    }, indent=2, sort_keys=True))
