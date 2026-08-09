#!/usr/bin/env python3
"""Independently substitute the cell-5 source-census survivors."""

import ast
import copy
import json
from pathlib import Path
import re

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
REPLAY = EXP / "rate_half_kb_positive_433_1b_cell5_parallel_de_four_basis_replay_result.json"
STRUCTURE = EXP / "rate_half_kb_positive_433_1b_cell5_complete_pivot_scout_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell5_compact_kernel_result.json"
P = 2130706433
t, r, c, b = sp.symbols("t r c b")
SYMBOLS = {"t": t, "r": r, "c": c, "b": b}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def parse_singular(text):
    expression = 0
    for term in re.findall(r"[+-]?[^+-]+", text):
        sign = -1 if term.startswith("-") else 1
        unsigned = term.lstrip("+-")
        digits = re.match(r"\d*", unsigned).group()
        value = sp.Integer(sign * int(digits or "1"))
        for variable, exponent in re.findall(
            r"([cbtr])(\d*)", unsigned[len(digits):]
        ):
            value *= SYMBOLS[variable] ** int(exponent or "1")
        expression += value
    return expression


def value(expression, point):
    return int(expression.subs({symbol: point[str(symbol)]
                                for symbol in (t, r, c, b)})) % P


def paired(a_values, b_values, left, right):
    p0, p1, p2 = ((bv-left*av) % P
                  for av, bv in zip(a_values, b_values))
    q0 = (b_values[0]-right*a_values[0]) % P
    q1 = (-b_values[1]+right*a_values[1]) % P
    q2 = (b_values[2]-right*a_values[2]) % P
    return (pow((p2*q0-p0*q2) % P, 2, P)
            - (p2*q1-p1*q2)*(p1*q0-p0*q1)) % P


def check(replay):
    structure = json.loads(STRUCTURE.read_text())
    kernels = json.loads(KERNEL.read_text())
    for row in replay["rows"]:
        epsilon = row["epsilon"]
        basis_row = next(item for item in structure["rows"]
                         if item["epsilon"] == epsilon)
        basis = [parse_singular(item["expression"])
                 for item in basis_row["lex_basis"]]
        kernel_row = next(item for item in kernels["rows"]
                          if item["epsilon"] == epsilon)
        kernel = [sp.sympify(item["expression"])
                  for item in kernel_row["kernel"]]
        for point in row["witnesses"]:
            require(all(value(item, point) == 0 for item in basis),
                    "common-equation substitution")
            values = [value(item, point) for item in kernel]
            a_values, b_values = values[:3], values[3:6]
            label = -point["t"]*point["t"] % P
            av = sum(item*pow(label, index, P)
                     for index, item in enumerate(a_values)) % P
            bv = sum(item*pow(label, index, P)
                     for index, item in enumerate(b_values)) % P
            require(av and point["missing"] == bv*pow(av, -1, P) % P,
                    "missing-value reconstruction")
            m = point["missing"]
            cut = (paired(a_values, b_values, m, -m % P)
                   if row["cut_kind"] == "opposite"
                   else paired(a_values, b_values, -m % P, -m % P))
            require(cut == point["cut"] == 0, "source-cut substitution")


def main():
    ast.parse((NODE / "verify.py").read_text())
    replay = json.loads(REPLAY.read_text())
    check(replay)
    hostile = copy.deepcopy(replay)
    witness_row = next(row for row in hostile["rows"] if row["witnesses"])
    witness_row["witnesses"][0]["cut"] = 1
    try:
        check(hostile)
    except RuntimeError:
        pass
    else:
        raise RuntimeError("hostile cut mutation survived")
    print("PASS cell-5 source audit: ordinary=8 hostile=detected")


if __name__ == "__main__":
    main()
