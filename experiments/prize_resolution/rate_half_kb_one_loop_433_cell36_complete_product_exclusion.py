#!/usr/bin/env python3
"""Exact complete-product exclusion for one-loop 433 cells 3 and 6."""

import argparse
import itertools

import sympy as sp


P = 2130706433
ORBIT_PACKETS = (
    (3, 1375161449, 1621120540, 1375161449, 1621120540),
    (3, 477266026, 1039843884, 477266026, 1039843884),
    (6, 1621120540, 1375161449, 1375161449, 1621120540),
    (6, 1039843884, 477266026, 477266026, 1039843884),
)
D, E, F = sp.symbols("D E F")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def matchings(items):
    if not items:
        yield ()
        return
    first = items[0]
    for index in range(1, len(items)):
        for tail in matchings(items[1:index]+items[index+1:]):
            yield ((first, items[index]),)+tail


MATCHINGS = tuple(matchings(tuple(range(6))))


def involution_data(singleton, paired):
    gamma = (paired-1) % P
    alpha = paired*(singleton*singleton % P*paired-1) % P
    beta = (
        singleton*singleton % P*paired % P*paired % P*(1-paired) % P
    )
    delta = (alpha*alpha+beta*gamma) % P
    denominator = (gamma*singleton-alpha) % P
    require(delta != 0 and denominator != 0, "involution guard")
    mate = (
        (alpha*singleton+beta)*pow(denominator, -1, P) % P
    )
    product = singleton*paired % P
    common = {P-1, singleton, paired, product, -product % P}
    require(mate not in common, "forced mate collision")
    require(
        (-gamma*paired-alpha*(paired-1)-beta) % P == 0,
        "first common pair",
    )
    require(
        (-gamma*product*product-beta) % P == 0,
        "second common pair",
    )
    return gamma, alpha, beta, mate


def skeleton_rows(name, b, c):
    if name == "S0":
        for alpha, beta, gamma in itertools.product((-1, 1), repeat=3):
            yield (
                alpha*b*D, beta*c*E, gamma*D*E,
                D*F, -D*F, E*F, -E*F,
            )
    elif name == "S1":
        for alpha, beta, gamma, delta in itertools.product(
            (-1, 1), repeat=4
        ):
            yield (
                alpha*b*E, beta*c*F, -D**2,
                gamma*D*E, delta*D*F, E*F, -E*F,
            )
    elif name == "S2":
        for alpha, beta in itertools.product((-1, 1), repeat=2):
            yield (
                alpha*b*D, beta*c*D, -E**2,
                D*F, -D*F, E*F, -E*F,
            )
    else:
        raise RuntimeError(name)


def is_unit_ideal(equations, variable_order):
    basis = sp.groebner(equations, *variable_order, modulus=P)
    return len(basis.polys) == 1 and basis.polys[0].total_degree() == 0


def verify(variable_order=(D, E, F), controls=False):
    if controls:
        require(
            not is_unit_ideal((D-1, E-2, F-3), variable_order),
            "positive control",
        )
        require(is_unit_ideal((D, D-1), variable_order), "unit control")

    counts = {"S0": 0, "S1": 0, "S2": 0}
    for cell, b, c, singleton, paired in ORBIT_PACKETS:
        gamma, alpha, beta, mate = involution_data(singleton, paired)
        for name in counts:
            for products in skeleton_rows(name, b, c):
                for forced_index in range(7):
                    residual = (
                        products[:forced_index]+products[forced_index+1:]
                    )
                    for matching in MATCHINGS:
                        equations = [products[forced_index]-mate]
                        for left, right in matching:
                            y_value = residual[left]
                            z_value = residual[right]
                            equations.append(
                                gamma*y_value*z_value
                                -alpha*(y_value+z_value)-beta
                            )
                        require(
                            is_unit_ideal(equations, variable_order),
                            f"survivor {name}/{cell}/{b}/{forced_index}/{matching}",
                        )
                        counts[name] += 1
    require(
        counts == {"S0": 3360, "S1": 6720, "S2": 1680},
        f"cell counts {counts}",
    )
    return counts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reverse-order", action="store_true")
    parser.add_argument("--controls", action="store_true")
    arguments = parser.parse_args()
    order = (F, E, D) if arguments.reverse_order else (D, E, F)
    counts = verify(order, arguments.controls)
    print(
        "RATE_HALF_KB_ONE_LOOP_433_CELL36_PRODUCT_EXCLUSION_PASS "
        f"order={''.join(str(value) for value in order)} "
        f"S0={counts['S0']} S1={counts['S1']} S2={counts['S2']} "
        f"total={sum(counts.values())}"
    )


if __name__ == "__main__":
    main()
