#!/usr/bin/env python3
"""Exact product-block rank compiler for the positive 433-1b route."""

import argparse
import hashlib
import itertools
import json

import sympy as sp


PRIME = 2130706433
ROLES = ("LA", "AB", "AC", "BC+", "BC-")


def pairings(values):
    values = tuple(values)
    first = values[0]
    for index in range(1, len(values)):
        second = values[index]
        rest = values[1:index] + values[index + 1:]
        yield ((first, second), (rest[0], rest[1]))


def cells():
    output = []
    for singleton in range(5):
        rest = tuple(index for index in range(5) if index != singleton)
        for matching in pairings(rest):
            output.append((singleton, matching))
    return tuple(output)


def monic(expression, variables):
    polynomial = sp.Poly(sp.expand(expression), *variables, modulus=PRIME)
    if polynomial.is_zero:
        return sp.Integer(0)
    return polynomial.monic().as_expr()


def strip_factors_with_ledger(expression, factors, variables):
    polynomial = sp.Poly(expression, *variables, modulus=PRIME)
    if polynomial.is_zero:
        return sp.Integer(0), []
    ledger = []
    for factor in factors:
        divisor = sp.Poly(factor, *variables, modulus=PRIME)
        if divisor.total_degree() == 0:
            continue
        multiplicity = 0
        while True:
            quotient, remainder = sp.div(polynomial, divisor)
            if not remainder.is_zero:
                break
            polynomial = quotient
            multiplicity += 1
        if multiplicity:
            ledger.append({
                "factor": str(divisor.monic().as_expr()),
                "multiplicity": multiplicity,
            })
    return polynomial.monic().as_expr(), ledger


def summary(expression, variables):
    polynomial = sp.Poly(expression, *variables, modulus=PRIME)
    if polynomial.is_zero:
        return {
            "degree": None,
            "terms": 0,
            "sha256": hashlib.sha256(b"0").hexdigest(),
            "constant": False,
        }
    text = str(polynomial.as_expr())
    return {
        "degree": polynomial.total_degree(),
        "terms": len(polynomial.terms()),
        "sha256": hashlib.sha256(text.encode()).hexdigest(),
        "constant": polynomial.total_degree() == 0,
    }


def compile_cell(cell_index, dump=False):
    b, c, r, t = sp.symbols("b c r t")
    variables = (t, r, c, b)
    singleton, matching = cells()[cell_index]
    labels = [None] * 5
    labels[matching[0][0]] = sp.Integer(1)
    labels[matching[0][1]] = sp.Integer(-1)
    labels[matching[1][0]] = r**2
    labels[matching[1][1]] = -r**2
    labels[singleton] = t**2
    products = (-1, b, c, b*c, -b*c)
    rows = [
        [-product, -product*label, -product*label**2,
         1, label, label**2]
        for product, label in zip(products, labels)
    ]
    matrix = sp.Matrix(rows)
    kernel_cofactors = tuple(
        (-1)**omitted
        * matrix[:, [column for column in range(6) if column != omitted]].det(
            method="domain-ge"
        )
        for omitted in range(6)
    )
    raw = tuple(monic(value, variables) for value in kernel_cofactors)
    source_guards = [
        labels[left] - labels[right]
        for left, right in itertools.combinations(range(5), 2)
    ]
    target_guards = [
        r, t, b, c, b - 1, b + 1, c - 1, c + 1, b - c, b + c,
    ]
    stripped_records = tuple(
        strip_factors_with_ledger(
            value, [*source_guards, *target_guards], variables
        )
        for value in raw
    )
    stripped = tuple(value for value, _ in stripped_records)
    output = {
        "cell": cell_index,
        "singleton": ROLES[singleton],
        "matching": [[ROLES[value] for value in pair] for pair in matching],
        "raw": [summary(value, variables) for value in raw],
        "stripped": [summary(value, variables) for value in stripped],
        "guard_only_minor_columns": [
            index for index, value in enumerate(stripped)
            if not sp.Poly(value, *variables, modulus=PRIME).is_zero
            and sp.Poly(value, *variables, modulus=PRIME).total_degree() == 0
        ],
    }
    if dump:
        output["stripped_expressions"] = [str(value) for value in stripped]
        output["stripped_ledgers"] = [ledger for _, ledger in stripped_records]
        output["kernel_cofactor_expressions"] = [
            str(sp.expand(value)) for value in kernel_cofactors
        ]
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cell", type=int, choices=range(15), required=True)
    parser.add_argument("--dump", action="store_true")
    arguments = parser.parse_args()
    print(json.dumps(compile_cell(arguments.cell, dump=arguments.dump),
                     sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
