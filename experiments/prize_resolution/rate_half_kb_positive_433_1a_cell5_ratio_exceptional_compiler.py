#!/usr/bin/env python3
"""Compile the deployed cell-5 ratio exceptional branch for Singular."""

import hashlib
import importlib.util
from pathlib import Path

import sympy as sp


DIRECTORY = Path(__file__).resolve().parent
COMMON = DIRECTORY / "rate_half_kb_positive_433_1a_common_vieta_compiler.py"
PRIME = 2130706433
IOTA = 16711679


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_common():
    specification = importlib.util.spec_from_file_location("common", COMMON)
    common = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(common)
    return common


def compile_program():
    common = load_common()
    variables, equations, _ = common.compile_cell(5, -1, -1, strip_fast=True)
    t, r, c, b = variables
    x = sp.symbols("x")
    atom_guards = (
        t-1, t+1, r-1, r+1, r-IOTA, r+IOTA,
        t-r, t+r, t-IOTA*r, t+IOTA*r, t-IOTA, t+IOTA,
        r, t, b, c, b-1, b+1, c-1, c+1, c-b, b+c,
    )
    localized = []
    for equation in equations[:3]:
        polynomial = sp.Poly(equation, *variables, modulus=PRIME).monic()
        for guard in atom_guards:
            divisor = sp.Poly(guard, *variables, modulus=PRIME).monic()
            while True:
                quotient, remainder = polynomial.div(divisor)
                if not remainder.is_zero:
                    break
                polynomial = quotient.monic()
        localized.append(polynomial.as_expr())

    quotient_polynomials = []
    for equation in localized:
        substituted = sp.Poly(
            sp.expand(equation.subs(c, b*x)), b, t, r, x, modulus=PRIME
        )
        minimum_b_degree = min(
            monomial[0] for monomial, _ in substituted.terms()
        )
        require(minimum_b_degree == 2, "ratio b valuation")
        quotient_polynomials.append(sp.Poly(
            sp.expand(substituted.as_expr() / b**2), b, domain="EX"
        ))
    require([value.degree() for value in quotient_polynomials] == [1, 2, 2],
            "ratio degree ledger")
    linear = quotient_polynomials[0]
    a0, a1 = linear.nth(0), linear.nth(1)
    l1, l2 = (value.as_expr() for value in quotient_polynomials[1:])

    ratio_guards = (
        t-1, t+1, r-1, r+1, r-IOTA, r+IOTA,
        t-r, t+r, t-IOTA*r, t+IOTA*r, t-IOTA, t+IOTA,
        r, t, b, x, b-1, b+1, b*x-1, b*x+1, x-1, x+1,
    )
    guard = sp.prod(ratio_guards)
    singular_variables = (b, x, r, t)

    def singular(expression):
        return str(sp.Poly(
            expression, *singular_variables, modulus=PRIME
        ).as_expr()).replace("**", "^")

    equation_text = [singular(value) for value in (a0, a1, l1, l2)]
    guard_text = singular(guard)
    program = f"""
ring R={PRIME},(b,x,r,t,z),dp;
option(redSB);
poly a0={equation_text[0]};
poly a1={equation_text[1]};
poly l1={equation_text[2]};
poly l2={equation_text[3]};
poly guard={guard_text};
ideal I=a0,a1,l1,l2,z*guard-1;
ideal G=std(I);
print(\"EXCEPTIONAL\"); print(dim(G)); print(size(G)); print(vdim(G));
print(\"BEGIN_BASIS\"); G; print(\"END_BASIS\");
quit;
"""
    return {
        "field": PRIME,
        "iota": IOTA,
        "cell": 5,
        "epsilon": [-1, -1],
        "branch": "a0=a1=L1=L2=0",
        "equation_shapes": [
            {
                "degree": sp.Poly(value, *singular_variables,
                                  modulus=PRIME).total_degree(),
                "terms": len(sp.Poly(value, *singular_variables,
                                     modulus=PRIME).terms()),
            }
            for value in (a0, a1, l1, l2)
        ],
        "guard_count": len(ratio_guards),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "program": program,
    }
