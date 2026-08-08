#!/usr/bin/env python3
"""Independent norm-root and adapter audit for cell-12 reciprocal pairing 0."""

import ast
import hashlib
import json
import multiprocessing
from pathlib import Path
import warnings

import sympy as sp
from sympy.polys.domains import ZZ
from sympy.polys.galoistools import gf_gcd, gf_pow_mod, gf_sub
from sympy.utilities.exceptions import SymPyDeprecationWarning


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell12_xi3_pairing0_template_adapter_modal.py"
TEMPLATE = EXP / "rate_half_kb_positive_433_1b_cell4_xi3_pairing0_reciprocal_square_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell12_xi3_pairing0_template_adapter_result.json"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell12_four_basis_tower_result.json"
P = 2130706433
x = sp.symbols("x")
ROOT_CACHE = {}
warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def parse_flint(text):
    if text == "0":
        return {}
    coefficients = {}
    for term in text.split(" + "):
        if "*x^" in term:
            coefficient, degree = term.split("*x^")
            coefficient, degree = int(coefficient), int(degree)
        elif term.startswith("x^"):
            coefficient, degree = 1, int(term[2:])
        elif term.endswith("*x"):
            coefficient, degree = int(term[:-2]), 1
        elif term == "x":
            coefficient, degree = 1, 1
        else:
            coefficient, degree = int(term), 0
        require(degree not in coefficients, "duplicate polynomial degree")
        coefficients[degree] = coefficient % P
    return {degree: value for degree, value in coefficients.items() if value}


def compute_roots(profile):
    key = profile["sha256"]
    text = profile["expression"]
    require(hashlib.sha256(text.encode()).hexdigest() == key, "profile digest")
    coefficients = parse_flint(text)
    require((max(coefficients, default=-1), len(coefficients)) ==
            (profile["degree"], profile["terms"]), "profile shape")
    degree = max(coefficients, default=-1)
    require(degree >= 0, "nonzero polynomial")
    polynomial = [coefficients.get(power, 0) for power in range(degree, -1, -1)]
    if degree == 0:
        output = []
    else:
        frobenius = gf_pow_mod([1, 0], P, polynomial, P, ZZ)
        root_part = gf_gcd(
            polynomial, gf_sub(frobenius, [1, 0], P, ZZ), P, ZZ
        )
        root_degree = len(root_part)-1
        expression = sum(value*x**(root_degree-index)
                         for index, value in enumerate(root_part))
        _, factors = sp.factor_list(expression, modulus=P)
        output = []
        for factor, _ in factors:
            row = sp.Poly(factor, x, modulus=P)
            require(row.degree() == 1, "root part split")
            leading, constant = (int(value) % P for value in row.all_coeffs())
            output.append(-constant*pow(leading, -1, P) % P)
        output = sorted(set(output))
    return key, output


def roots(profile):
    key = profile["sha256"]
    if key not in ROOT_CACHE:
        _, ROOT_CACHE[key] = compute_roots(profile)
    return ROOT_CACHE[key]


def main():
    source = SCRIPT.read_text()
    tree = ast.parse(source)
    require("function.decorator_list = []" in source
            and 'node.name == "evaluate_case"' in source
            and 'compile(module, REMOTE_TEMPLATE, "exec")' in source,
            "AST adapter boundary")
    extracted = [node for node in ast.parse(TEMPLATE.read_text()).body
                 if isinstance(node, ast.FunctionDef)
                 and node.name == "evaluate_case"]
    require(len(extracted) == 1, "unique pinned template function")

    tower = json.loads(TOWER.read_text())
    leading = {
        tuple(row["epsilon"]): sp.sympify(row["b_leading"]["expression"])
        for row in tower["rows"] if row["c_row_index"] == 5
    }
    r, t = sp.symbols("r t")
    payload = json.loads(RESULT.read_text())
    profiles = {}
    for row in payload["rows"]:
        for value in [*row["inverse_guards"], row["target_norm"]]:
            for side in ("numerator", "denominator"):
                profile = value[side]
                profiles.setdefault(profile["sha256"], profile)
    with multiprocessing.get_context("fork").Pool(processes=2) as pool:
        ROOT_CACHE.update(pool.map(compute_roots, profiles.values()))
    polynomials = 0
    boundary_count = 0
    for row in payload["rows"]:
        candidates = row["candidate_roots"]
        target_roots = roots(row["target_norm"]["numerator"])
        require(target_roots == row["target_norm_roots"], "target-root replay")
        union = set(target_roots)
        polynomials += 1
        for value in [*row["inverse_guards"], row["target_norm"]]:
            for side in ("numerator", "denominator"):
                union.update(roots(value[side]))
                polynomials += 1
        require(sorted(union) == candidates, "complete candidate-root union")
        covered = {
            item["r"] for field in ("boundary_rows", "no_lift_rows", "finite_rows")
            for item in row[field]
        }
        require(covered == set(candidates), "direct candidate coverage")
        for item in row["boundary_rows"]:
            if item["stage"] != "CELL12_B_LEADING":
                continue
            expression = leading[tuple(row["epsilon"])]
            require(int(expression.subs({r: item["r"], t: item["t"]})) % P == 0,
                    "cell-12 leading-boundary routing")
            boundary_count += 1
    require(boundary_count == 24, "24 leading-boundary terminals")
    require(len(ROOT_CACHE) == 89, "unique polynomial audit count")
    print(f"PASS reciprocal adapter audit: profiles={polynomials} unique=89 boundary=24")


if __name__ == "__main__":
    main()
