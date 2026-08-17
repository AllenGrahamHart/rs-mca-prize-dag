#!/usr/bin/env python3
"""Factor the guarded b-eliminant of the O0b collapsed common scheme."""

import json
from pathlib import Path
import re

import sympy as sp


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "rate_half_kb_positive_433_1b_o0b_collapsed_common_fglm_result.json"
PRIME = 2130706433
EXPECTED_FACTORS = (
    ("b", 3),
    ("b - 1", 4),
    ("b + 1", 5),
    ("b + 8244070", 1),
    ("b + 25179288", 1),
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def parse_univariate(expression):
    b = sp.symbols("b")
    expression = re.sub(r"b(\d+)", r"b**\1", expression)
    expression = re.sub(r"(?<=\d)b", "*b", expression)
    parsed = sp.Poly(sp.sympify(expression, locals={"b": b}), b, modulus=PRIME)
    return b, parsed


def verify_factorization():
    payload = json.loads(SOURCE.read_text())
    row = payload["row"]
    require(row["status"] == "COMPLETE" and row["lex_vdim"] == 65,
            "complete FGLM source")
    b, eliminant = parse_univariate(row["lex_basis"][0])
    coefficient, factors = sp.factor_list(eliminant, modulus=PRIME)
    require(int(coefficient) % PRIME == 1, "monic eliminant")
    actual = {
        (str(factor.as_expr()), multiplicity)
        for factor, multiplicity in factors
    }
    require(actual == set(EXPECTED_FACTORS), "exact factorization")
    guarded = tuple(
        (-constant) % PRIME for constant in (8244070, 25179288)
    )
    require(all(value not in {0, 1, PRIME - 1} for value in guarded),
            "surviving b fibers")
    product = sp.Poly(1, b, modulus=PRIME)
    for factor, multiplicity in factors:
        product *= factor ** multiplicity
    require(product.monic() == eliminant.monic(), "factor reconstruction")
    return eliminant.degree(), guarded


if __name__ == "__main__":
    degree, guarded = verify_factorization()
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_COLLAPSED_COMMON_ELIMINANT_FACTOR_PASS "
          f"degree={degree} guarded_fibers={len(guarded)} values={guarded}")
