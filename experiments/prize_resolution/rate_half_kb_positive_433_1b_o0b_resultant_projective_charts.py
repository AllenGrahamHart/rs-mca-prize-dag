#!/usr/bin/env python3
"""Verify the exact projective-chart split of the O0b matching resultants."""

import importlib.util
from itertools import product
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
COMPILER = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
EXPECTED_COMPILER_SHA256 = "048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def symbols_and_resultant():
    p0, p1, p2, q0, q1, q2, z, u = sp.symbols(
        "p0 p1 p2 q0 q1 q2 z u"
    )
    p = p0 + p1 * z + p2 * z**2
    q = q0 + q1 * z + q2 * z**2
    formula = (
        (p2 * q0 - p0 * q2) ** 2
        - (p2 * q1 - p1 * q2) * (p1 * q0 - p0 * q1)
    )
    return (p0, p1, p2, q0, q1, q2, z, u), p, q, formula


def verify_resultant_identity(sign=-1):
    symbols, p, q, formula = symbols_and_resultant()
    p0, p1, p2, q0, q1, q2, _, _ = symbols
    if sign != -1:
        formula = (
            (p2 * q0 - p0 * q2) ** 2
            + (p2 * q1 - p1 * q2) * (p1 * q0 - p0 * q1)
        )
    sylvester = sp.Matrix([
        [p2, p1, p0, 0],
        [0, p2, p1, p0],
        [q2, q1, q0, 0],
        [0, q2, q1, q0],
    ])
    require(sp.expand(sylvester.det() - formula) == 0,
            "Sylvester determinant identity")
    require(sp.expand(sp.resultant(p, q, symbols[6]) - formula) == 0,
            "quadratic resultant identity")
    return formula


def verify_chart_implications():
    symbols, _, _, formula = symbols_and_resultant()
    p0, p1, p2, q0, q1, q2, _, u = symbols
    finite_substitution = {
        p0: -p1 * u - p2 * u**2,
        q0: -q1 * u - q2 * u**2,
    }
    require(sp.expand(formula.subs(finite_substitution)) == 0,
            "finite common-root chart implies resultant zero")
    require(sp.expand(formula.subs({p2: 0, q2: 0})) == 0,
            "infinity chart implies resultant zero")
    return ("finite", "infinity")


def chart_masks():
    return tuple(product(("finite", "infinity"), repeat=3))


def verify_chart_cover(masks=None):
    masks = tuple(masks if masks is not None else chart_masks())
    require(len(masks) == 8 and len(set(masks)) == 8, "eight distinct charts")
    expected = set(product(("finite", "infinity"), repeat=3))
    require(set(masks) == expected, "complete distributive chart cover")
    return masks


def load_compiler():
    import hashlib

    require(hashlib.sha256(COMPILER.read_bytes()).hexdigest() ==
            EXPECTED_COMPILER_SHA256, "compiler custody")
    spec = importlib.util.spec_from_file_location("cached_outside_core", COMPILER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_compiler_resultants():
    compiler = load_compiler()
    packet = {
        "variables": ["t", "r", "c", "b"],
        "common_equations": ["t", "r", "c"],
        "kernel": ["1", "t", "r", "c", "b", "t+r", "t+c", "r+b"],
        "route_guards": [f"t+{index}" for index in range(16)],
        "rank_cofactors": [f"r+{index}" for index in range(6)],
    }
    compiled = compiler.compile_case((3, "S0", -1, -1, -1, 2, 0), packet)
    definitions = set(compiled["definitions"])
    for index in (4, 5, 6):
        prefix = f"m{index}"
        expected = (
            f"poly q{index}=({prefix}p2*{prefix}q0-{prefix}p0*{prefix}q2)^2"
            f"-({prefix}p2*{prefix}q1-{prefix}p1*{prefix}q2)"
            f"*({prefix}p1*{prefix}q0-{prefix}p0*{prefix}q1);"
        )
        require(expected in definitions, f"compiler q{index} resultant")
    require(compiled["equations"][3:] == ("q3", "q4", "q5", "q6", "q7"),
            "outside equation order")
    return 3


def main():
    verify_resultant_identity()
    verify_chart_implications()
    masks = verify_chart_cover()
    count = verify_compiler_resultants()
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_RESULTANT_PROJECTIVE_CHARTS_PASS "
          f"resultants={count} charts={len(masks)}")


if __name__ == "__main__":
    main()
