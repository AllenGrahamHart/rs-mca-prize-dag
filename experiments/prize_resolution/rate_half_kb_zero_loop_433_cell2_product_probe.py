#!/usr/bin/env python3
"""Sharded complete-product probe for zero-loop 433 common cell 2."""

import argparse
import itertools
import math
import time

import sympy as sp
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp


P = 2130706433
BASE_ORDER = P - 1
EXTENSION_ORDER = P**6 - 1
EMBEDDING_MULTIPLIER = EXTENSION_ORDER // BASE_ORDER
GENERATOR = 3
D, E, F = sp.symbols("D E F")
VARIABLES = (D, E, F)
PACKETS = (
    (2122238824, 2130706431),
    (1069587021, 1065353216),
    (1061119412, 1065353216),
    (8467609, 2130706431),
)
SKELETONS = ("Z0", "Z1", "Z2", "Z3", "Z4")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def matchings(items):
    if not items:
        yield ()
        return
    first = items[0]
    for index in range(1, len(items)):
        for tail in matchings(items[1:index] + items[index + 1:]):
            yield ((first, items[index]),) + tail


MATCHINGS = tuple(matchings(tuple(range(6))))


def colored_rows(first_index, second_index, b, c):
    outside = VARIABLES
    for first_sign, second_sign in itertools.product((-1, 1), repeat=2):
        yield (
            first_sign * b * outside[first_index],
            second_sign * c * outside[second_index],
        )


def product_forms(name, b, c):
    if name == "Z0":
        for colored in colored_rows(2, 2, b, c):
            yield colored + (-E**2, D * E, -D * E, D * F, -D * F)
    elif name == "Z1":
        for colored in colored_rows(2, 2, b, c):
            for de, df, ef in itertools.product((-1, 1), repeat=3):
                yield colored + (
                    -D**2, -E**2, de * D * E, df * D * F, ef * E * F
                )
    elif name == "Z2":
        for first_index, second_index in ((1, 2), (2, 1)):
            for colored in colored_rows(first_index, second_index, b, c):
                for ef in (-1, 1):
                    yield colored + (
                        D * E, -D * E, D * F, -D * F, ef * E * F
                    )
    elif name == "Z3":
        for first_index, second_index in ((1, 2), (2, 1)):
            for colored in colored_rows(first_index, second_index, b, c):
                for de, df in itertools.product((-1, 1), repeat=2):
                    yield colored + (
                        -D**2, de * D * E, df * D * F, E * F, -E * F
                    )
    elif name == "Z4":
        for first_index, second_index in ((1, 2), (2, 1)):
            for colored in colored_rows(first_index, second_index, b, c):
                for ef in (-1, 1):
                    yield colored + (
                        -D**2, -F**2, D * E, -D * E, ef * E * F
                    )
    else:
        raise RuntimeError(name)


def involution_data(b, c):
    gamma = b * (c - 1) % P
    alpha = c * (c - b * b) % P
    beta = -b * c * c * (c - 1) % P
    delta = (alpha * alpha + beta * gamma) % P
    require(gamma != 0 and alpha == 0 and delta != 0, "involution collapse")
    mate = -c * c * pow(b, -1, P) % P
    common = {b, -b % P, c, -c % P, b * c % P}
    require(mate not in common, "forced mate collision")
    return mate


def is_unit_ideal(equations, variable_order):
    basis = sp.groebner(equations, *variable_order, modulus=P)
    return len(basis.polys) == 1 and basis.polys[0].total_degree() == 0


def monomial(expression):
    terms = sp.Poly(expression, *VARIABLES, modulus=P).terms()
    require(len(terms) == 1, "monomial product")
    powers, coefficient = terms[0]
    return tuple(int(value) for value in powers), int(coefficient) % P


LOG_CACHE = {1: 0, P - 1: BASE_ORDER // 2}


def base_log(value):
    value %= P
    require(value != 0, "nonzero logarithm")
    if value not in LOG_CACHE:
        LOG_CACHE[value] = int(sp.discrete_log(P, value, GENERATOR))
    return LOG_CACHE[value]


SMITH_CACHE = {}


def smith_data(rows):
    key = tuple(tuple(int(value) for value in row) for row in rows)
    if key not in SMITH_CACHE:
        matrix = DomainMatrix(
            [[ZZ(value) for value in row] for row in key],
            (len(key), len(key[0])),
            ZZ,
        )
        diagonal, left, right = smith_normal_decomp(matrix)
        SMITH_CACHE[key] = (
            tuple(tuple(int(value) for value in row) for row in diagonal.to_list()),
            tuple(tuple(int(value) for value in row) for row in left.to_list()),
            tuple(tuple(int(value) for value in row) for row in right.to_list()),
        )
    return SMITH_CACHE[key]


def solve_congruences(rows, values, modulus=EXTENSION_ORDER, family_sample_size=32):
    diagonal, left, right = smith_data(rows)
    transformed = tuple(
        sum(left[row][column] * values[column] for column in range(len(values)))
        % modulus
        for row in range(len(values))
    )
    scalar_solutions = []
    rank = 0
    for index in range(len(VARIABLES)):
        value = diagonal[index][index]
        if value == 0:
            if transformed[index] % modulus:
                return rank, (), False
            scalar_solutions.append(None)
            continue
        rank += 1
        divisor = math.gcd(abs(value), modulus)
        if transformed[index] % divisor:
            return rank, (), False
        reduced_modulus = modulus // divisor
        base = (
            (transformed[index] // divisor)
            * pow((value // divisor) % reduced_modulus, -1, reduced_modulus)
        ) % reduced_modulus
        scalar_solutions.append(
            tuple(base + offset * reduced_modulus for offset in range(divisor))
        )
    for index in range(len(VARIABLES), len(values)):
        if transformed[index] % modulus:
            return rank, (), False

    family = rank < len(VARIABLES)
    if family:
        scalar_solutions = [
            tuple(range(family_sample_size)) if values is None else values
            for values in scalar_solutions
        ]

    answers = []
    for smith_vector in itertools.product(*scalar_solutions):
        answer = tuple(
            sum(right[row][column] * smith_vector[column]
                for column in range(len(VARIABLES))) % modulus
            for row in range(len(VARIABLES))
        )
        require(
            all(
                sum(rows[row][column] * answer[column]
                    for column in range(len(VARIABLES))) % modulus
                == values[row] % modulus
                for row in range(len(rows))
            ),
            "Smith replay",
        )
        answers.append(answer)
    return rank, tuple(sorted(set(answers))), family


def extension_log(base_field_value):
    return EMBEDDING_MULTIPLIER * base_log(base_field_value) % EXTENSION_ORDER


def guarded_assignment(logs, b, c, products):
    target_logs = (
        0,
        extension_log(b),
        extension_log(c),
    ) + tuple(logs)
    if len({2 * value % EXTENSION_ORDER for value in target_logs}) != 6:
        return False

    product_logs = [
        extension_log(b),
        extension_log(-b),
        extension_log(c),
        extension_log(-c),
        extension_log(b * c % P),
    ]
    for expression in products:
        powers, coefficient = monomial(expression)
        product_logs.append(
            (extension_log(coefficient)
             + sum(powers[index] * logs[index] for index in range(3)))
            % EXTENSION_ORDER
        )
    return len(set(product_logs)) == 12


def forced_guard_collision(equations, b, c, products):
    basis = sp.groebner(equations, *VARIABLES, modulus=P)
    target_values = tuple(map(sp.sympify, (1, b, c))) + VARIABLES
    for left, right in itertools.combinations(range(6), 2):
        difference = target_values[left] ** 2 - target_values[right] ** 2
        if basis.reduce(difference)[1] == 0:
            return f"target-square:{left}:{right}"

    product_values = tuple(map(sp.sympify, (
        b, -b, c, -c, b * c,
    ))) + products
    for left, right in itertools.combinations(range(12), 2):
        if basis.reduce(product_values[left] - product_values[right])[1] == 0:
            return f"product:{left}:{right}"
    return None


def group_probe(packet_index, name, max_cases=None, stop_on_survivor=False,
                print_limit=5, verbose=True):
    b, c = PACKETS[packet_index]
    mate = involution_data(b, c)
    forms = tuple(product_forms(name, b, c))
    expected = {"Z0": 4, "Z1": 32, "Z2": 16, "Z3": 32, "Z4": 16}
    require(len(forms) == expected[name], "form census")
    checked = 0
    algebraic = 0
    extension_solutions = 0
    family_samples = 0
    guarded = []
    families = []
    started = time.monotonic()
    for form_index, products in enumerate(forms):
        data = tuple(monomial(expression) for expression in products)
        for forced_index in range(7):
            residual_indices = tuple(
                index for index in range(7) if index != forced_index
            )
            for matching_index, matching in enumerate(MATCHINGS):
                forced_powers, forced_coefficient = data[forced_index]
                rows = [forced_powers]
                values = [
                    extension_log(
                        mate * pow(forced_coefficient, -1, P) % P
                    )
                ]
                for left, right in matching:
                    left_powers, left_coefficient = data[residual_indices[left]]
                    right_powers, right_coefficient = data[residual_indices[right]]
                    rows.append(tuple(
                        left_powers[index] + right_powers[index]
                        for index in range(3)
                    ))
                    coefficient = left_coefficient * right_coefficient % P
                    values.append(extension_log(-c * c * pow(coefficient, -1, P) % P))
                rank, solutions, family = solve_congruences(
                    tuple(rows), tuple(values)
                )
                if family:
                    residual = products[:forced_index] + products[forced_index + 1:]
                    equations = [products[forced_index] - mate]
                    equations.extend(
                        residual[left] * residual[right] + c * c
                        for left, right in matching
                    )
                    collision = forced_guard_collision(equations, b, c, products)
                    require(collision is not None, "unresolved multiplicative family")
                    families.append(
                        (form_index, forced_index, matching_index, rank, collision)
                    )
                    if verbose and len(families) <= print_limit:
                        print(
                            "GROUP_FAMILY "
                            f"packet={packet_index} skeleton={name} "
                            f"form={form_index} forced={forced_index} "
                            f"matching={matching_index} rank={rank} "
                            f"collision={collision}",
                            flush=True,
                        )
                if solutions:
                    algebraic += 1
                    if family:
                        family_samples += len(solutions)
                    else:
                        extension_solutions += len(solutions)
                    for logs in solutions:
                        if guarded_assignment(logs, b, c, products):
                            guarded.append(
                                (form_index, forced_index, matching_index, logs)
                            )
                            if verbose and len(guarded) <= print_limit:
                                print(
                                    "GROUP_GUARDED_SURVIVOR "
                                    f"packet={packet_index} skeleton={name} "
                                    f"form={form_index} forced={forced_index} "
                                    f"matching={matching_index} logs={logs}",
                                    flush=True,
                                )
                            if stop_on_survivor:
                                return (
                                    checked + 1,
                                    algebraic,
                                    extension_solutions,
                                    family_samples,
                                    guarded,
                                    families,
                                )
                checked += 1
                if verbose and checked % 1000 == 0:
                    print(
                        "GROUP_PROGRESS "
                        f"packet={packet_index} skeleton={name} checked={checked} "
                        f"soluble={algebraic} guarded={len(guarded)} "
                        f"families={len(families)} seconds={time.monotonic()-started:.2f}",
                        flush=True,
                    )
                if max_cases is not None and checked >= max_cases:
                    return (
                        checked,
                        algebraic,
                        extension_solutions,
                        family_samples,
                        guarded,
                        families,
                    )
    return (
        checked,
        algebraic,
        extension_solutions,
        family_samples,
        guarded,
        families,
    )


def probe(packet_index, name, variable_order=VARIABLES, max_cases=None):
    b, c = PACKETS[packet_index]
    mate = involution_data(b, c)
    forms = tuple(product_forms(name, b, c))
    expected = {"Z0": 4, "Z1": 32, "Z2": 16, "Z3": 32, "Z4": 16}
    require(len(forms) == expected[name], "form census")
    checked = 0
    survivors = []
    started = time.monotonic()
    for form_index, products in enumerate(forms):
        require(len(products) == 7, "outside product count")
        for forced_index in range(7):
            residual = products[:forced_index] + products[forced_index + 1:]
            for matching_index, matching in enumerate(MATCHINGS):
                equations = [products[forced_index] - mate]
                equations.extend(
                    residual[left] * residual[right] + c * c
                    for left, right in matching
                )
                if not is_unit_ideal(equations, variable_order):
                    survivors.append((form_index, forced_index, matching_index))
                    print(
                        "SURVIVOR "
                        f"packet={packet_index} skeleton={name} "
                        f"form={form_index} forced={forced_index} "
                        f"matching={matching_index}",
                        flush=True,
                    )
                checked += 1
                if checked % 250 == 0:
                    print(
                        "PROGRESS "
                        f"packet={packet_index} skeleton={name} "
                        f"checked={checked} survivors={len(survivors)} "
                        f"seconds={time.monotonic()-started:.2f}",
                        flush=True,
                    )
                    sp.core.cache.clear_cache()
                if max_cases is not None and checked >= max_cases:
                    return checked, survivors
    return checked, survivors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--packet", type=int, choices=range(len(PACKETS)), required=True)
    parser.add_argument("--skeleton", choices=SKELETONS, required=True)
    parser.add_argument("--reverse-order", action="store_true")
    parser.add_argument("--max-cases", type=int)
    parser.add_argument("--group", action="store_true")
    parser.add_argument("--stop-on-survivor", action="store_true")
    parser.add_argument("--print-limit", type=int, default=5)
    arguments = parser.parse_args()
    if arguments.group:
        checked, soluble, solutions, family_samples, guarded, families = group_probe(
            arguments.packet,
            arguments.skeleton,
            max_cases=arguments.max_cases,
            stop_on_survivor=arguments.stop_on_survivor,
            print_limit=arguments.print_limit,
        )
        print(
            "RATE_HALF_KB_ZERO_LOOP_433_CELL2_PRODUCT_GROUP "
            f"packet={arguments.packet} skeleton={arguments.skeleton} "
            f"checked={checked} soluble={soluble} solutions={solutions} "
            f"family_samples={family_samples} guarded={len(guarded)} "
            f"families={len(families)}",
            flush=True,
        )
        return
    order = tuple(reversed(VARIABLES)) if arguments.reverse_order else VARIABLES
    checked, survivors = probe(
        arguments.packet,
        arguments.skeleton,
        variable_order=order,
        max_cases=arguments.max_cases,
    )
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_CELL2_PRODUCT_PROBE "
        f"packet={arguments.packet} skeleton={arguments.skeleton} "
        f"order={''.join(str(value) for value in order)} "
        f"checked={checked} survivors={len(survivors)}",
        flush=True,
    )


if __name__ == "__main__":
    main()
