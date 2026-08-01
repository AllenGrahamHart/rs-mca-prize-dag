#!/usr/bin/env python3
"""Exact q-only router for one-loop 433 common cells 1 and 2."""

import importlib.util
import itertools
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
ATLAS_PATH = ROOT / (
    "experiments/prize_resolution/rate_half_kb_one_loop_433_common_atlas.py"
)
SPEC = importlib.util.spec_from_file_location("atlas", ATLAS_PATH)
ATLAS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ATLAS)
P = ATLAS.PRIME


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_branch(cell, epsilon_1, epsilon_2):
    variables, equations, _ = ATLAS.compile_cell(cell, epsilon_1, epsilon_2)
    t, r, c, b = variables
    guard_factors = (
        b, c, r,
        b-1, b+1, c-1, c+1, b-c, b+c,
        b*c-1, b*c+1,
        r-1, r+1, r**2-1, r**2+1,
    )
    q_values = tuple(
        ATLAS.BASE.strip_factors(value, guard_factors, variables)
        for value in equations[2:]
    )
    require(
        all(sp.Poly(value, r, b, c, modulus=P).degree(r) == 1
            for value in q_values),
        "q row not linear in r",
    )
    resultant = sp.Poly(
        sp.resultant(q_values[0], q_values[1], r), b, c, modulus=P
    ).monic()
    expected = b*(c**2-1) if epsilon_1 == epsilon_2 else c*(b**2-1)
    require(
        resultant == sp.Poly(expected, b, c, modulus=P).monic(),
        "guard resultant",
    )


def verify():
    for cell, epsilon_1, epsilon_2 in itertools.product(
        (1, 2), (1, -1), (1, -1)
    ):
        verify_branch(cell, epsilon_1, epsilon_2)


def main():
    verify()
    print(
        "RATE_HALF_KB_ONE_LOOP_433_CELL12_Q_PASS "
        "cells=1,2 sign_rows=8 resultants=target_guards"
    )


if __name__ == "__main__":
    main()
