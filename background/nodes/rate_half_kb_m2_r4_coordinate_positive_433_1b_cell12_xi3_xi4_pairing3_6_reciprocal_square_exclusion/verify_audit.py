#!/usr/bin/env python3
"""Independent root and final-gcd audit for cell-12 pairing 3/6."""

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
SCRIPT = EXP / (
    "rate_half_kb_positive_433_1b_cell12_xi3_pairing3_"
    "template_adapter_modal.py"
)
TEMPLATE = EXP / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairing3_"
    "reciprocal_square_modal.py"
)
RESULT = EXP / (
    "rate_half_kb_positive_433_1b_cell12_xi3_pairing3_"
    "template_adapter_result.json"
)
TOWER = EXP / "rate_half_kb_positive_433_1b_cell12_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell12_compact_kernel_result.json"
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
    require(
        (max(coefficients, default=-1), len(coefficients))
        == (profile["degree"], profile["terms"]),
        "profile shape",
    )
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
        root_degree = len(root_part) - 1
        expression = sum(
            value * x ** (root_degree - index)
            for index, value in enumerate(root_part)
        )
        _, factors = sp.factor_list(expression, modulus=P)
        output = []
        for factor, _ in factors:
            row = sp.Poly(factor, x, modulus=P)
            require(row.degree() == 1, "root part split")
            leading, constant = (int(value) % P for value in row.all_coeffs())
            output.append(-constant * pow(leading, -1, P) % P)
        output = sorted(set(output))
    return key, output


def roots(profile):
    return ROOT_CACHE[profile["sha256"]]


def paired_polynomial(a_values, b_values, left_scale, right_scale):
    p0, p1, p2 = (
        b_value - left_scale * x * a_value
        for a_value, b_value in zip(a_values, b_values)
    )
    q0 = b_values[0] - right_scale * x * a_values[0]
    q1 = -b_values[1] + right_scale * x * a_values[1]
    q2 = b_values[2] - right_scale * x * a_values[2]
    return sp.Poly(
        (p2 * q0 - p0 * q2) ** 2
        - (p2 * q1 - p1 * q2) * (p1 * q0 - p0 * q1),
        x,
        modulus=P,
    )


def paired_scalar(a_values, b_values, left, right):
    p0, p1, p2 = (
        (b_value - left * a_value) % P
        for a_value, b_value in zip(a_values, b_values)
    )
    q0 = (b_values[0] - right * a_values[0]) % P
    q1 = (-b_values[1] + right * a_values[1]) % P
    q2 = (b_values[2] - right * a_values[2]) % P
    return (
        pow((p2 * q0 - p0 * q2) % P, 2, P)
        - ((p2 * q1 - p1 * q2) % P) * ((p1 * q0 - p0 * q1) % P)
    ) % P


def main():
    source = SCRIPT.read_text()
    ast.parse(source)
    require(
        "function.decorator_list = []" in source
        and 'node.name == "evaluate_case"' in source
        and 'compile(module, REMOTE_TEMPLATE, "exec")' in source,
        "AST adapter boundary",
    )
    extracted = [
        node for node in ast.parse(TEMPLATE.read_text()).body
        if isinstance(node, ast.FunctionDef) and node.name == "evaluate_case"
    ]
    require(len(extracted) == 1, "unique pinned template function")

    tower = json.loads(TOWER.read_text())
    leading = {
        tuple(row["epsilon"]): sp.sympify(row["b_leading"]["expression"])
        for row in tower["rows"] if row["c_row_index"] == 5
    }
    kernel_payload = json.loads(KERNEL.read_text())
    kernels = {
        tuple(row["epsilon"]): tuple(
            sp.sympify(value["expression"]) for value in row["kernel"]
        )
        for row in kernel_payload["rows"]
    }
    r, t, b, c = sp.symbols("r t b c")
    payload = json.loads(RESULT.read_text())
    profiles = {}
    for row in payload["rows"]:
        for value in [*row["inverse_guards"], row["target_norm"]]:
            for side in ("numerator", "denominator"):
                profile = value[side]
                profiles.setdefault(profile["sha256"], profile)
    require(len(profiles) == 45, "unique polynomial census")
    with multiprocessing.get_context("fork").Pool(processes=2) as pool:
        ROOT_CACHE.update(pool.map(compute_roots, profiles.values()))

    profile_visits = 0
    boundary_count = 0
    gcd_count = 0
    for row in payload["rows"]:
        target_roots = roots(row["target_norm"]["numerator"])
        require(target_roots == row["target_norm_roots"], "target-root replay")
        union = set(target_roots)
        for value in [*row["inverse_guards"], row["target_norm"]]:
            for side in ("numerator", "denominator"):
                union.update(roots(value[side]))
                profile_visits += 1
        require(sorted(union) == row["candidate_roots"], "candidate-root union")
        covered = {
            item["r"]
            for field in ("boundary_rows", "no_lift_rows", "finite_rows")
            for item in row[field]
        }
        require(covered == set(row["candidate_roots"]), "direct candidate coverage")
        for item in row["boundary_rows"]:
            if item["stage"] != "CELL12_B_LEADING":
                continue
            expression = leading[tuple(row["epsilon"])]
            require(
                int(expression.subs({r: item["r"], t: item["t"]})) % P == 0,
                "cell-12 leading-boundary routing",
            )
            boundary_count += 1

        kernel = kernels[tuple(row["epsilon"])]
        for finite in row["finite_rows"]:
            for z_row in finite.get("z_rows", []):
                point = {r: finite["r"], t: finite["t"],
                         b: finite["b"], c: finite["c"]}
                values = [int(value.subs(point)) % P for value in kernel]
                a_values, b_values = values[:3], values[3:6]
                missing = finite["missing"]
                source_sum = finite["source_sum"]
                z_value = z_row["z"]
                y_value = z_value * z_value % P
                require(
                    (1 + (2 * missing - source_sum) * y_value
                     + missing * missing * y_value * y_value) % P == 0,
                    "missing reciprocal relation",
                )
                colored = paired_scalar(
                    a_values, b_values,
                    finite["b"] * missing * z_value % P,
                    row["sigma_c"] * finite["c"] * missing * z_value % P,
                )
                require(colored == 0, "colored-pair direct replay")
                antipodal = paired_polynomial(a_values, b_values, 1, -1)
                for d_row in z_row["d_rows"]:
                    for lane in d_row["lanes"]:
                        sigma_o = lane["sigma"][1]
                        outside = paired_polynomial(
                            a_values, b_values,
                            1, sigma_o * missing * y_value % P,
                        )
                        require(
                            sp.gcd(antipodal, outside).degree() == 0,
                            "nonconstant final q gcd",
                        )
                        require(
                            lane["common_q_roots"] == [] and lane["q_rows"] == [],
                            "stored final lane",
                        )
                        gcd_count += 1
    require(profile_visits == 112, "profile replay count")
    require(boundary_count == 8, "eight leading-boundary terminals")
    require(gcd_count == 80, "80 final q gcds")
    print(
        "PASS pairing-3 adapter audit: "
        "profiles=112 unique=45 boundary=8 q_gcds=80"
    )


if __name__ == "__main__":
    main()
