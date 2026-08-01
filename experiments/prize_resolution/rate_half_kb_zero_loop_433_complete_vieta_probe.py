#!/usr/bin/env python3
"""Exact complete-Vieta probe for retained negative zero-loop 433 products.

The product routers describe D,E,F by discrete logarithms in F_(p^6).
This script realizes the same generator in the explicit field

    F_p[X]/(X^6+X+6)

and tests all seven outside sum rows.  It is deliberately a probe: a product
family is reported as unresolved and is never deleted from sampled points.
"""

import argparse
import importlib.util
import itertools
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def load(name, relative):
    specification = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


PRODUCT = load(
    "zero_loop_product",
    "experiments/prize_resolution/rate_half_kb_zero_loop_433_cell2_product_probe.py",
)
BC_PRODUCT = load(
    "zero_loop_bc_product",
    "experiments/prize_resolution/rate_half_kb_zero_loop_433_bc_product_probe.py",
)
ATLAS = load(
    "zero_loop_atlas",
    "experiments/prize_resolution/rate_half_kb_zero_loop_433_common_atlas.py",
)

P = PRODUCT.P
N = PRODUCT.EXTENSION_ORDER
M = PRODUCT.EMBEDDING_MULTIPLIER
ZERO = (0, 0, 0, 0, 0, 0)
ONE = (1, 0, 0, 0, 0, 0)
X = (0, 1, 0, 0, 0, 0)
GENERATOR_EXPONENT = 1768759633
ORDER_PRIMES = (2, 3, 7, 67, 127, 283, 1254833,
                9679978477096567, 1513303300498959019)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def add(left, right):
    return tuple((left[index] + right[index]) % P for index in range(6))


def neg(value):
    return tuple(-coefficient % P for coefficient in value)


def sub(left, right):
    return add(left, neg(right))


def mul(left, right):
    raw = [0] * 11
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            raw[left_index + right_index] = (
                raw[left_index + right_index] + left_value * right_value
            ) % P
    # X^6=-X-6 in the pinned polynomial basis.
    for degree in range(10, 5, -1):
        value = raw[degree]
        raw[degree] = 0
        raw[degree - 5] = (raw[degree - 5] - value) % P
        raw[degree - 6] = (raw[degree - 6] - 6 * value) % P
    return tuple(raw[:6])


def power(value, exponent):
    result = ONE
    while exponent:
        if exponent & 1:
            result = mul(result, value)
        value = mul(value, value)
        exponent >>= 1
    return result


def inverse(value):
    require(value != ZERO, "division by zero")
    return power(value, N - 1)


def divide(numerator, denominator):
    return mul(numerator, inverse(denominator))


def base(value):
    return (value % P, 0, 0, 0, 0, 0)


GENERATOR = power(X, GENERATOR_EXPONENT)


def field_audit():
    require(power(X, N) == ONE, "field order")
    require(all(power(X, N // prime) != ONE for prime in ORDER_PRIMES),
            "X is not primitive")
    require(power(GENERATOR, M) == base(3), "base-compatible generator")
    require(all(power(GENERATOR, N // prime) != ONE for prime in ORDER_PRIMES),
            "generator order")


POWER_CACHE = {}


def generator_power(exponent):
    exponent %= N
    if exponent not in POWER_CACHE:
        POWER_CACHE[exponent] = power(GENERATOR, exponent)
    return POWER_CACHE[exponent]


def evaluate_monomial(expression, logs):
    powers, coefficient = PRODUCT.monomial(expression)
    exponent = PRODUCT.extension_log(coefficient)
    exponent += sum(powers[index] * logs[index] for index in range(3))
    return generator_power(exponent)


def edge_forms(name, b, c):
    D, E, F = PRODUCT.VARIABLES

    def colored(first_index, second_index):
        outside = (D, E, F)
        for first_sign, second_sign in itertools.product((-1, 1), repeat=2):
            yield (
                (b, first_sign * outside[first_index]),
                (c, second_sign * outside[second_index]),
            )

    if name == "Z0":
        for prefix in colored(2, 2):
            yield prefix + ((E, -E), (D, E), (D, -E), (D, F), (D, -F))
    elif name == "Z1":
        for prefix in colored(2, 2):
            for de, df, ef in itertools.product((-1, 1), repeat=3):
                yield prefix + (
                    (D, -D), (E, -E), (D, de * E),
                    (D, df * F), (E, ef * F),
                )
    elif name == "Z2":
        for first_index, second_index in ((1, 2), (2, 1)):
            for prefix in colored(first_index, second_index):
                for ef in (-1, 1):
                    yield prefix + (
                        (D, E), (D, -E), (D, F), (D, -F), (E, ef * F),
                    )
    elif name == "Z3":
        for first_index, second_index in ((1, 2), (2, 1)):
            for prefix in colored(first_index, second_index):
                for de, df in itertools.product((-1, 1), repeat=2):
                    yield prefix + (
                        (D, -D), (D, de * E), (D, df * F),
                        (E, F), (E, -F),
                    )
    elif name == "Z4":
        for first_index, second_index in ((1, 2), (2, 1)):
            for prefix in colored(first_index, second_index):
                for ef in (-1, 1):
                    yield prefix + (
                        (D, -D), (F, -F), (D, E), (D, -E), (E, ef * F),
                    )
    else:
        raise RuntimeError(name)


COMMON_RECORDS = {
    2: (
        (1, 1, 2122238824, 2130706431, 374290000, 583634934),
        (1, 1, 1069587021, 1065353216, 374290000, 583634934),
        (1, 1, 1061119412, 1065353216, 1722993073, 1547071505),
        (1, 1, 8467609, 2130706431, 1722993073, 1547071505),
        (-1, -1, 2122238824, 2130706431, 1764884040, 1547071505),
        (-1, -1, 1069587021, 1065353216, 1764884040, 1547071505),
        (-1, -1, 1061119412, 1065353216, 399245749, 583634934),
        (-1, -1, 8467609, 2130706431, 399245749, 583634934),
    ),
    12: (
        (1, 1, 1361855312, 1859271856, 1587494773, 1299348518),
        (1, 1, 1859271856, 1361855312, 1608564875, 823002076),
        (1, 1, 271434577, 768851121, 1587494773, 1299348518),
        (1, 1, 768851121, 271434577, 1608564875, 823002076),
        (1, -1, 33423358, 1056997377, 1056997377, 8355839),
        (1, -1, 1073709056, 2097283075, 2097283075, 16711678),
        (1, -1, 1056997377, 33423358, 1056997377, 8355839),
        (1, -1, 2097283075, 1073709056, 2097283075, 16711678),
        (-1, 1, 1056997377, 33423358, 33423358, 2113994753),
        (-1, 1, 2097283075, 1073709056, 1073709056, 2122350593),
        (-1, 1, 33423358, 1056997377, 33423358, 2113994753),
        (-1, 1, 1073709056, 2097283075, 1073709056, 2122350593),
        (-1, -1, 271434577, 768851121, 1608564875, 263421243),
        (-1, -1, 768851121, 271434577, 1587494773, 1875641030),
        (-1, -1, 1361855312, 1859271856, 1608564875, 263421243),
        (-1, -1, 1859271856, 1361855312, 1587494773, 1875641030),
    ),
    13: (
        (1, 1, 1061119412, 2122238824, 583634928, 407713360),
        (1, 1, 1069587021, 8467609, 1547071499, 1756416433),
        (1, 1, 8467609, 1069587021, 583634928, 407713360),
        (1, 1, 2122238824, 1061119412, 1547071499, 1756416433),
        (-1, -1, 1069587021, 8467609, 583634928, 365822393),
        (-1, -1, 1061119412, 2122238824, 1547071499, 1731460684),
        (-1, -1, 2122238824, 1061119412, 583634928, 365822393),
        (-1, -1, 8467609, 1069587021, 1547071499, 1731460684),
    ),
    14: (
        (1, 1, 1061119412, 8467609, 583634928, 1764884040),
        (1, 1, 1069587021, 2122238824, 1547071499, 399245749),
        (1, 1, 8467609, 1061119412, 583634928, 1764884040),
        (1, 1, 2122238824, 1069587021, 1547071499, 399245749),
        (-1, -1, 1069587021, 2122238824, 583634928, 1722993073),
        (-1, -1, 1061119412, 8467609, 1547071499, 374290000),
        (-1, -1, 2122238824, 1069587021, 583634928, 1722993073),
        (-1, -1, 8467609, 1061119412, 1547071499, 374290000),
    ),
}


def null_vector(rows):
    matrix = [[value % P for value in row] for row in rows]
    pivots = []
    row = 0
    for column in range(len(matrix[0])):
        pivot = next((index for index in range(row, len(matrix))
                      if matrix[index][column]), None)
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        scale = pow(matrix[row][column], -1, P)
        matrix[row] = [value * scale % P for value in matrix[row]]
        for index in range(len(matrix)):
            if index == row or matrix[index][column] == 0:
                continue
            scale = matrix[index][column]
            matrix[index] = [
                (matrix[index][j] - scale * matrix[row][j]) % P
                for j in range(len(matrix[0]))
            ]
        pivots.append(column)
        row += 1
        if row == len(matrix):
            break
    require(len(pivots) == len(rows), "unexpected row rank")
    free = [column for column in range(len(matrix[0])) if column not in pivots]
    require(len(free) == 1, "kernel dimension")
    answer = [0] * len(matrix[0])
    answer[free[0]] = 1
    for index in range(len(pivots) - 1, -1, -1):
        answer[pivots[index]] = -sum(
            matrix[index][column] * answer[column]
            for column in free
        ) % P
    require(all(sum(a * b for a, b in zip(row_values, answer)) % P == 0
                for row_values in rows), "kernel replay")
    return tuple(answer)


def common_data(cell, record):
    epsilon_1, epsilon_2, b, c, r, t = record
    singleton, matching = ATLAS.BASE.cells()[cell]
    roots = [None] * 5
    roots[matching[0][0]] = 1
    roots[matching[0][1]] = epsilon_1 * ATLAS.IOTA % P
    roots[matching[1][0]] = r
    roots[matching[1][1]] = epsilon_2 * ATLAS.IOTA * r % P
    roots[singleton] = t
    labels = tuple(root * root % P for root in roots)
    products = (b, -b % P, c, -c % P, b * c % P)
    sums = (1 + b, 1 - b, 1 + c, 1 - c, b + c)
    q_values = tuple(roots[index] * sums[index] % P for index in range(5))
    rows = [(-product, -product * label, 1, label)
            for product, label in zip(products[:3], labels[:3])]
    d0, d1, n0, n1 = null_vector(rows)
    require(all(
        (-product * d0 - product * label * d1 + n0 + label * n1) % P == 0
        for product, label in zip(products, labels)
    ), "common product replay")
    qd = tuple(
        -q_values[index] * (d0 + d1 * labels[index]) % P
        for index in range(5)
    )
    a0, a1, a2 = null_vector(
        [(1, label, label * label, -value)
         for label, value in zip(labels[:3], qd[:3])]
    )[:3]
    # The previous kernel has a free scale in its fourth coordinate.  Normalize
    # that coordinate to one by construction and replay all five values.
    require(all(
        (a0 + a1 * label + a2 * label * label - value) % P == 0
        for label, value in zip(labels, qd)
    ), "common q replay")
    return labels, (d0, d1, n0, n1), (a0, a1, a2)


def complete_vieta(cell, record, name, form_index, logs):
    b, c = record[2], record[3]
    products = tuple(PRODUCT.product_forms(name, b, c))[form_index]
    edges = tuple(edge_forms(name, b, c))[form_index]
    require(len(products) == len(edges) == 7, "outside row count")
    require(all(
        PRODUCT.monomial(product) == PRODUCT.monomial(left * right)
        for product, (left, right) in zip(products, edges)
    ), "edge/product alignment")
    common_labels, mobius, quadratic = common_data(cell, record)
    d0, d1, n0, n1 = map(base, mobius)
    a0, a1, a2 = map(base, quadratic)
    outside_labels = []
    failures = []
    for index, (product_expression, edge) in enumerate(zip(products, edges)):
        product = evaluate_monomial(product_expression, logs)
        label = divide(
            sub(n0, mul(product, d0)),
            sub(mul(product, d1), n1),
        )
        denominator = add(d0, mul(d1, label))
        required_q = neg(divide(
            add(add(a0, mul(a1, label)), mul(a2, mul(label, label))),
            denominator,
        ))
        left = evaluate_monomial(edge[0], logs)
        right = evaluate_monomial(edge[1], logs)
        observed_square = mul(label, mul(add(left, right), add(left, right)))
        if mul(required_q, required_q) != observed_square:
            failures.append(index)
            break
        outside_labels.append(label)
    if not failures:
        require(len(set(common_labels)) == 5, "common label guard")
        require(len(set(map(base, common_labels)) | set(outside_labels)) == 12,
                "complete quotient injectivity")
    return tuple(failures)


def product_packet_index(cell, b, c):
    packets = PRODUCT.PACKETS if cell == 2 else BC_PRODUCT.PACKETS[cell]
    return packets.index((b, c))


def product_assignments(cell, packet_index, name):
    if cell == 2:
        result = PRODUCT.group_probe(
            packet_index, name, verbose=False, print_limit=0
        )
        guarded, families = result[4], result[5]
    else:
        result = BC_PRODUCT.probe(
            cell, packet_index, name, verbose=False, print_limit=0
        )
        guarded, families = result["guarded"], result["families"]
    assignments = sorted({(entry[0], entry[3]) for entry in guarded})
    return tuple(assignments), tuple(families)


def probe(cell, packet_index, name):
    assignments, families = product_assignments(cell, packet_index, name)
    packets = PRODUCT.PACKETS if cell == 2 else BC_PRODUCT.PACKETS[cell]
    b, c = packets[packet_index]
    records = tuple(record for record in COMMON_RECORDS[cell]
                    if record[2:4] == (b, c))
    require(records, "common record lookup")
    survivors = []
    failure_histogram = {}
    for record_index, record in enumerate(records):
        for form_index, logs in assignments:
            failures = complete_vieta(cell, record, name, form_index, logs)
            failure_histogram[failures] = failure_histogram.get(failures, 0) + 1
            if not failures:
                survivors.append((record_index, form_index, logs))
    return {
        "records": records,
        "assignments": assignments,
        "families": families,
        "unresolved_families": tuple(
            family for family in families if family[4] == "unresolved"
        ),
        "survivors": tuple(survivors),
        "failure_histogram": failure_histogram,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cell", type=int, choices=(2, 12, 13, 14), required=True)
    parser.add_argument("--packet", type=int, required=True)
    parser.add_argument("--skeleton", choices=PRODUCT.SKELETONS, required=True)
    arguments = parser.parse_args()
    field_audit()
    packets = PRODUCT.PACKETS if arguments.cell == 2 else BC_PRODUCT.PACKETS[arguments.cell]
    require(0 <= arguments.packet < len(packets), "packet index")
    result = probe(arguments.cell, arguments.packet, arguments.skeleton)
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_COMPLETE_VIETA "
        f"cell={arguments.cell} packet={arguments.packet} "
        f"skeleton={arguments.skeleton} records={len(result['records'])} "
        f"products={len(result['assignments'])} families={len(result['families'])} "
        f"unresolved_families={len(result['unresolved_families'])} "
        f"survivors={len(result['survivors'])} "
        f"failure_patterns={len(result['failure_histogram'])}",
        flush=True,
    )
    for survivor in result["survivors"][:5]:
        print(f"COMPLETE_VIETA_SURVIVOR {survivor}", flush=True)


if __name__ == "__main__":
    main()
