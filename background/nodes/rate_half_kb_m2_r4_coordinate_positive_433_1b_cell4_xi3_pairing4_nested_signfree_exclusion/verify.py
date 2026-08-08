#!/usr/bin/env python3
"""Independently verify the cell-4 xi3 pairing-4 exclusion."""

import ast
import collections
import hashlib
import itertools
import json
from pathlib import Path
import re
import warnings

import sympy as sp
from sympy.polys.domains import ZZ
from sympy.polys.galoistools import gf_gcd, gf_pow_mod, gf_sub
from sympy.utilities.exceptions import SymPyDeprecationWarning


warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)

NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairing4_"
    "nested_signfree_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairing4_"
    "nested_signfree_result.json"
)
STRUCTURE = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_remaining_compact_pivot_scout_result.json"
)
KERNEL = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_compact_kernel_result.json"
)
PINNED = {
    SCRIPT: "0992beedc8d85e1d7e510d40dadccd72d01e8b38325d9e6fe56c741ab50711fd",
    RESULT: "6f6a94918baa77a0a9913b5d542cdbcc1b76902ba70516ff429c37a1c1e984da",
    STRUCTURE: "53e7e23afe164a94a677d2f3be044b1e25542d9c3d0ab6850efd1f0029002a33",
    KERNEL: "52d40fe51d713eeb6c92217d4bd0024dfd9fa29118c44cfa64592c0da350fdab",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_four_basis_tower_kernel",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
)
PRIME = 2130706433
SIGNS = set(itertools.product((-1, 1), repeat=2))
t, r, c, b = sp.symbols("t r c b")
VARIABLES = (t, r, c, b)
x = sp.symbols("x")
ROOT_CACHE = {}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_flint_polynomial(text):
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
        require(degree not in coefficients, "unique FLINT polynomial degree")
        coefficients[degree] = coefficient % PRIME
    return {
        degree: coefficient
        for degree, coefficient in coefficients.items()
        if coefficient
    }


def verify_profile(profile, label):
    require(
        set(profile) == {"degree", "terms", "sha256", "expression"},
        f"{label} keys",
    )
    text = profile["expression"]
    require(
        hashlib.sha256(text.encode()).hexdigest() == profile["sha256"],
        f"{label} digest",
    )
    coefficients = parse_flint_polynomial(text)
    require(
        (max(coefficients, default=-1), len(coefficients))
        == (profile["degree"], profile["terms"]),
        f"{label} shape",
    )
    return coefficients


def verify_compact_profile(profile, label):
    require(
        set(profile) == {"degree", "terms", "sha256"},
        f"{label} keys",
    )
    require(
        profile["degree"] >= -1
        and profile["terms"] >= 0
        and ((profile["degree"] == -1) == (profile["terms"] == 0))
        and len(profile["sha256"]) == 64,
        f"{label} shape",
    )


def trim(polynomial):
    output = [coefficient % PRIME for coefficient in polynomial]
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def field_roots(coefficients):
    maximum = max(coefficients, default=-1)
    require(maximum >= 0, "nonzero root polynomial")
    leading_inverse = pow(coefficients[maximum], -1, PRIME)
    coefficients = {
        degree: coefficient*leading_inverse % PRIME
        for degree, coefficient in coefficients.items()
        if coefficient % PRIME
    }
    key = tuple(sorted(coefficients.items()))
    if key in ROOT_CACHE:
        return ROOT_CACHE[key]
    reflected_key = tuple(sorted(
        (degree, coefficient if degree % 2 == 0 else -coefficient % PRIME)
        for degree, coefficient in coefficients.items()
    ))
    if reflected_key in ROOT_CACHE:
        output = sorted({-root % PRIME for root in ROOT_CACHE[reflected_key]})
        ROOT_CACHE[key] = output
        return output
    polynomial = [
        coefficients.get(degree, 0)
        for degree in range(maximum, -1, -1)
    ]
    if maximum == 0:
        return []
    frobenius = gf_pow_mod([1, 0], PRIME, polynomial, PRIME, ZZ)
    root_part = gf_gcd(
        polynomial,
        gf_sub(frobenius, [1, 0], PRIME, ZZ),
        PRIME,
        ZZ,
    )
    root_degree = len(root_part) - 1
    expression = sum(
        coefficient * x**(root_degree-index)
        for index, coefficient in enumerate(root_part)
    )
    _, factors = sp.factor_list(expression, modulus=PRIME)
    roots = []
    for factor, multiplicity in factors:
        polynomial_factor = sp.Poly(factor, x, modulus=PRIME)
        require(polynomial_factor.degree() == 1, "field-root part splits")
        leading, constant = (
            int(coefficient) % PRIME
            for coefficient in polynomial_factor.all_coeffs()
        )
        root = -constant * pow(leading, -1, PRIME) % PRIME
        roots.extend([root] * int(multiplicity))
    output = sorted(set(roots))
    ROOT_CACHE[key] = output
    return output


def parse_singular(text, ordered_variables):
    symbols = {"t": t, "r": r, "c": c, "b": b}
    expression = 0
    for term in re.findall(r"[+-]?[^+-]+", text):
        sign = -1 if term.startswith("-") else 1
        unsigned = term.lstrip("+-")
        digits = re.match(r"\d*", unsigned).group()
        monomial = sp.Integer(sign * int(digits or "1"))
        for variable, exponent in re.findall(
            r"([trcb])(\d*)", unsigned[len(digits):]
        ):
            monomial *= symbols[variable] ** int(exponent or "1")
        expression += monomial
    return sp.Poly(
        expression, *ordered_variables, modulus=PRIME
    ).as_expr()


def value(expression, point):
    substitutions = {
        t: point.get("t", 0),
        r: point.get("r", 0),
        c: point.get("c", 0),
        b: point.get("b", 0),
    }
    return int(sp.sympify(expression).subs(substitutions)) % PRIME


def roots_from_coefficients(coefficients):
    coefficients = trim(coefficients or [0])
    if coefficients == [0]:
        return None
    degree = len(coefficients) - 1
    if degree == 0:
        return []
    if degree == 1:
        return [
            -coefficients[0] * pow(coefficients[1], -1, PRIME) % PRIME
        ]
    if degree > 2:
        return field_roots({
            index: coefficient
            for index, coefficient in enumerate(coefficients)
            if coefficient
        })
    constant, linear, leading = coefficients
    discriminant = (linear * linear - 4 * leading * constant) % PRIME
    inverse = pow(2 * leading, -1, PRIME)
    return sorted({
        (-linear + square_root) * inverse % PRIME
        for square_root in sp.sqrt_mod(discriminant, PRIME, all_roots=True)
    })


def relation_roots(expression, variable, point):
    polynomial = sp.Poly(expression, variable)
    coefficients = [
        value(polynomial.coeff_monomial(variable**degree), point)
        for degree in range(polynomial.degree() + 1)
    ]
    return roots_from_coefficients(coefficients)


def paired(a_values, b_values, left, right):
    p0, p1, p2 = (
        (b_value-left*a_value) % PRIME
        for a_value, b_value in zip(a_values, b_values)
    )
    q0 = (b_values[0]-right*a_values[0]) % PRIME
    q1 = (-b_values[1]+right*a_values[1]) % PRIME
    q2 = (b_values[2]-right*a_values[2]) % PRIME
    return (
        pow((p2*q0-p0*q2) % PRIME, 2, PRIME)
        - ((p2*q1-p1*q2) % PRIME)*((p1*q0-p0*q1) % PRIME)
    ) % PRIME


def polynomial_add(left, right):
    size = max(len(left), len(right))
    return trim([
        ((left[index] if index < len(left) else 0)
         + (right[index] if index < len(right) else 0)) % PRIME
        for index in range(size)
    ])


def polynomial_subtract(left, right):
    return polynomial_add(left, [(-value) % PRIME for value in right])


def polynomial_multiply(left, right):
    output = [0] * (len(left)+len(right)-1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            output[left_index+right_index] = (
                output[left_index+right_index] + left_value*right_value
            ) % PRIME
    return trim(output)


def paired_both_coefficients(a_values, b_values, left_scale, right_scale):
    p0, p1, p2 = (
        [b_value, -left_scale*a_value % PRIME]
        for a_value, b_value in zip(a_values, b_values)
    )
    q0 = [b_values[0], -right_scale*a_values[0] % PRIME]
    q1 = [-b_values[1] % PRIME, right_scale*a_values[1] % PRIME]
    q2 = [b_values[2], -right_scale*a_values[2] % PRIME]
    first = polynomial_subtract(
        polynomial_multiply(p2, q0), polynomial_multiply(p0, q2)
    )
    second = polynomial_subtract(
        polynomial_multiply(p2, q1), polynomial_multiply(p1, q2)
    )
    third = polynomial_subtract(
        polynomial_multiply(p1, q0), polynomial_multiply(p0, q1)
    )
    return polynomial_subtract(
        polynomial_multiply(first, first),
        polynomial_multiply(second, third),
    )


def paired_left_coefficients(a_values, b_values, right):
    p0, p1, p2 = (
        [b_value, -a_value % PRIME]
        for a_value, b_value in zip(a_values, b_values)
    )
    q0 = [(b_values[0]-right*a_values[0]) % PRIME]
    q1 = [(-b_values[1]+right*a_values[1]) % PRIME]
    q2 = [(b_values[2]-right*a_values[2]) % PRIME]
    first = polynomial_subtract(
        polynomial_multiply(p2, q0), polynomial_multiply(p0, q2)
    )
    second = polynomial_subtract(
        polynomial_multiply(p2, q1), polynomial_multiply(p1, q2)
    )
    third = polynomial_subtract(
        polynomial_multiply(p1, q0), polynomial_multiply(p0, q1)
    )
    return polynomial_subtract(
        polynomial_multiply(first, first),
        polynomial_multiply(second, third),
    )


def target_guards(representatives):
    failures = []
    for index, representative in enumerate(representatives):
        if representative % PRIME == 0:
            failures.append(f"nonzero_{index}")
    for left in range(6):
        for right in range(left+1, 6):
            if (representatives[left]-representatives[right]) % PRIME == 0:
                failures.append(f"difference_{left}_{right}")
            if (representatives[left]+representatives[right]) % PRIME == 0:
                failures.append(f"sum_{left}_{right}")
    return failures


def reconstruct_row(row, base_expression, b_expression, c_expression, kernel):
    route_guards = (
        b, c, r, t, b-1, b+1, c-1, c+1, b-c, b+c,
        r*r-1, r*r+1, t*t-1, t*t+1,
        t*t-r*r, t*t+r*r,
    )
    boundary_rows = []
    target_boundary_rows = []
    no_lift_rows = []
    finite_rows = []
    z_candidates = []
    q_candidates = []
    final_pair_solutions = []
    witnesses = []
    unresolved = []
    source_point_count = 0
    route_point_count = 0

    for r_value in row["candidate_roots"]:
        base_point = {"r": r_value}
        if any(value(guard, base_point) == 0 for guard in (
            r, r*r-1, r*r+1,
        )):
            boundary_rows.append({**base_point, "stage": "R_GUARD"})
            continue
        t_roots = relation_roots(base_expression, t, base_point)
        require(t_roots is not None, "base relation not free")
        if not t_roots:
            no_lift_rows.append({**base_point, "stage": "NO_T_ROOT"})
            continue
        for t_value in t_roots:
            bt_point = {"r": r_value, "t": t_value}
            if any(value(guard, bt_point) == 0 for guard in (
                t, t*t-1, t*t+1, t*t-r*r, t*t+r*r,
            )):
                boundary_rows.append({**bt_point, "stage": "T_GUARD"})
                continue
            b_roots = relation_roots(b_expression, b, bt_point)
            require(b_roots is not None, "b relation not free")
            if not b_roots:
                no_lift_rows.append({**bt_point, "stage": "NO_B_ROOT"})
                continue
            for b_value in b_roots:
                c_point = {**bt_point, "b": b_value}
                if any(value(guard, c_point) == 0 for guard in (
                    b, b-1, b+1,
                )):
                    boundary_rows.append({**c_point, "stage": "B_GUARD"})
                    continue
                c_roots = relation_roots(c_expression, c, c_point)
                require(c_roots is not None, "c relation not free")
                if not c_roots:
                    no_lift_rows.append({**c_point, "stage": "NO_C_ROOT"})
                    continue
                require(len(c_roots) == 1, "linear c recovery")
                point = {**c_point, "c": c_roots[0]}
                source_point_count += 1
                if any(value(guard, point) == 0 for guard in route_guards):
                    boundary_rows.append({**point, "stage": "FULL_GUARD"})
                    continue
                route_point_count += 1
                values = [value(expression, point) for expression in kernel]
                a_values, b_values = values[:3], values[3:6]
                beta_0, beta_1 = values[6:]
                label = -point["t"]*point["t"] % PRIME
                a_missing = sum(
                    coefficient*pow(label, index, PRIME)
                    for index, coefficient in enumerate(a_values)
                ) % PRIME
                b_missing = sum(
                    coefficient*pow(label, index, PRIME)
                    for index, coefficient in enumerate(b_values)
                ) % PRIME
                if a_missing == 0:
                    status = "MISSING_IMPOSSIBLE" if b_missing else "MISSING_FREE"
                    if status == "MISSING_FREE":
                        unresolved.append({**point, "reason": status})
                    finite_rows.append({**point, "status": status})
                    continue
                missing = b_missing*pow(a_missing, -1, PRIME) % PRIME
                source_sum = (
                    label*pow((beta_0+beta_1*label) % PRIME, 2, PRIME)
                    * pow(a_missing, -2, PRIME)
                ) % PRIME
                branch_row = {
                    **point,
                    "missing": missing,
                    "source_sum": source_sum,
                    "z_rows": [],
                }
                if missing == 0:
                    branch_row["status"] = "TARGET_PRODUCT_BOUNDARY"
                    target_boundary_rows.append(branch_row)
                    finite_rows.append(branch_row)
                    continue
                missing_z_roots = roots_from_coefficients([
                    1, 0, (2*missing-source_sum) % PRIME, 0,
                    missing*missing % PRIME,
                ])
                require(missing_z_roots is not None, "monic missing cut")
                antipodal_q_roots = roots_from_coefficients(
                    paired_both_coefficients(a_values, b_values, 1, -1)
                )
                branch_row.update({
                    "missing_z_roots": missing_z_roots,
                    "antipodal_q_roots": antipodal_q_roots,
                })
                for z_value in missing_z_roots:
                    y_value = z_value*z_value % PRIME
                    require(z_value != 0, "reciprocal root nonzero")
                    require(
                        (1+(2*missing-source_sum)*y_value
                         + missing*missing*y_value*y_value) % PRIME == 0,
                        "missing cut replay",
                    )
                    d_value = pow(z_value, -1, PRIME)
                    f_value = missing*z_value % PRIME
                    second_q_roots = roots_from_coefficients(
                        paired_left_coefficients(
                            a_values, b_values,
                            point["b"]*f_value % PRIME,
                        )
                    )
                    if antipodal_q_roots is None:
                        q_roots = second_q_roots
                    elif second_q_roots is None:
                        q_roots = antipodal_q_roots
                    else:
                        q_roots = sorted(
                            set(antipodal_q_roots) & set(second_q_roots)
                        )
                    if q_roots is None:
                        unresolved.append({
                            **point,
                            "z": z_value,
                            "reason": "FREE_Q",
                        })
                        q_roots = []
                    z_row = {
                        "z": z_value,
                        "y": y_value,
                        "d": d_value,
                        "f": f_value,
                        "second_q_roots": second_q_roots,
                        "common_q_roots": q_roots,
                        "q_rows": [],
                    }
                    if q_roots:
                        z_candidates.append({
                            **point,
                            "z": z_value,
                            "y": y_value,
                            "q_count": len(q_roots),
                        })
                    for q_value in q_roots:
                        e_value = q_value*z_value % PRIME
                        candidate = {
                            **point,
                            "q": q_value,
                            "z": z_value,
                            "y": y_value,
                            "d": d_value,
                            "e": e_value,
                            "f": f_value,
                        }
                        q_candidates.append(candidate)
                        antipodal_pair = paired(
                            a_values, b_values, q_value, -q_value % PRIME
                        )
                        second_pair = paired(
                            a_values, b_values, q_value,
                            point["b"]*f_value % PRIME,
                        )
                        require(not antipodal_pair and not second_pair,
                                "common q-root replay")
                        q_row = {
                            "q": q_value,
                            "e": e_value,
                            "antipodal_pair_cut": antipodal_pair,
                            "second_pair_cut": second_pair,
                            "lanes": [],
                        }
                        for sigma_c in (-1, 1):
                            for sigma_o in (-1, 1):
                                final_pair = paired(
                                    a_values, b_values,
                                    sigma_o*e_value*f_value % PRIME,
                                    sigma_c*point["c"]*f_value % PRIME,
                                )
                                lane_row = {
                                    "sigma": [sigma_c, sigma_o],
                                    "final_pair_cut": final_pair,
                                }
                                if final_pair:
                                    lane_row["status"] = "THIRD_PAIR_NONZERO"
                                    q_row["lanes"].append(lane_row)
                                    continue
                                representatives = (
                                    1, point["b"], point["c"],
                                    d_value, e_value, f_value,
                                )
                                failed_guards = target_guards(representatives)
                                equation_values = [
                                    (d_value*e_value-q_value) % PRIME,
                                    (d_value*f_value-missing) % PRIME,
                                    (pow(d_value+f_value, 2, PRIME)-source_sum) % PRIME,
                                    antipodal_pair,
                                    second_pair,
                                    final_pair,
                                ]
                                require(not any(equation_values), "target replay")
                                lane_row.update({
                                    "target_representatives": list(representatives),
                                    "failed_guards": failed_guards,
                                    "equation_values": equation_values,
                                    "status": (
                                        "TARGET_BOUNDARY" if failed_guards else "WITNESS"
                                    ),
                                })
                                solution = {**candidate, **lane_row}
                                final_pair_solutions.append(solution)
                                (target_boundary_rows if failed_guards else witnesses).append(
                                    solution
                                )
                                q_row["lanes"].append(lane_row)
                        z_row["q_rows"].append(q_row)
                    branch_row["z_rows"].append(z_row)
                branch_row["status"] = "CHECKED"
                finite_rows.append(branch_row)

    replay = {
        "source_point_count": source_point_count,
        "route_point_count": route_point_count,
        "boundary_rows": boundary_rows,
        "target_boundary_rows": target_boundary_rows,
        "no_lift_rows": no_lift_rows,
        "finite_rows": finite_rows,
        "z_candidate_count": len(z_candidates),
        "z_candidates": z_candidates,
        "q_candidate_count": len(q_candidates),
        "q_candidates": q_candidates,
        "final_pair_solution_count": len(final_pair_solutions),
        "final_pair_solutions": final_pair_solutions,
        "witness_count": len(witnesses),
        "witnesses": witnesses,
        "unresolved": unresolved,
        "target_excluded": not witnesses and not unresolved,
    }
    for key, expected in replay.items():
        require(row[key] == expected, f"independent finite replay {key}")


def formal_sign_free_identity():
    z_symbol, y_symbol = sp.symbols("z_symbol y_symbol")
    h0, h1, h2, h3, h4 = sp.symbols("h0 h1 h2 h3 h4")
    polynomial = h0+h1*z_symbol+h2*z_symbol**2+h3*z_symbol**3+h4*z_symbol**4
    even = h0+h2*y_symbol+h4*y_symbol**2
    odd = h1+h3*y_symbol
    require(
        sp.expand(
            polynomial*polynomial.subs(z_symbol, -z_symbol)
            - (even**2-y_symbol*odd**2).subs(y_symbol, z_symbol**2)
        ) == 0,
        "formal sign-free quartic identity",
    )


def verify_payload(payload):
    require(
        payload["schema"] ==
        "rate-half-kb-positive-433-1b-cell4-xi3-pairing4-"
        "nested-signfree-v1",
        "schema",
    )
    require(
        payload["field"] == PRIME
        and payload["source_structure_sha256"] == digest(STRUCTURE)
        and payload["source_kernel_sha256"] == digest(KERNEL),
        "source custody",
    )
    structure = json.loads(STRUCTURE.read_text())
    kernel_payload = json.loads(KERNEL.read_text())
    expected = SIGNS
    actual = set()
    profiles = collections.Counter()
    final_lane_count = 0

    for row_index, row in enumerate(payload["rows"]):
        key = tuple(row["epsilon"])
        require(key in expected and key not in actual, "sign Cartesian row")
        actual.add(key)
        epsilon = key
        require(
            row["xi_index"] == 3
            and row["pairing_index"] == 4
            and row["status"] == "COMPLETE"
            and row["target_excluded"]
            and row["unresolved"] == []
            and row["witnesses"] == [],
            "complete scoped exclusion",
        )
        require(
            (row["missing_cut_degree"], row["antipodal_u_degree"],
             row["second_target_z_degree"], row["remainder_u_z_degrees"],
             row["remainder_z_degree"], row["z_sign_free_degree"],
             row["remainder_degree"])
            == (2, 2, 8, [4, 4], 3, 3, 1),
            "nested q/z sign-free degree ledger",
        )
        for label, profiles_list in (
            ("target", row["target_free_profiles"]),
        ):
            expected_length = 4
            require(len(profiles_list) == expected_length, f"{label} basis")
            for profile_index, profile in enumerate(profiles_list):
                for part in ("numerator", "denominator"):
                    verify_compact_profile(
                        profile[part],
                        f"row {row_index} {label} {profile_index} {part}",
                    )
        for label, coefficient_count in (
            ("missing_cut_profiles", 3),
            ("antipodal_u_profiles", 3),
            ("second_target_z_profiles", 9),
        ):
            require(len(row[label]) == coefficient_count,
                    f"{label} coefficient count")
            for coefficient_index, coefficient in enumerate(row[label]):
                require(len(coefficient) == 4, f"{label} tower basis")
                for profile_index, profile in enumerate(coefficient):
                    for part in ("numerator", "denominator"):
                        verify_compact_profile(
                            profile[part],
                            f"row {row_index} {label} {coefficient_index} "
                            f"{profile_index} {part}",
                        )

        norm = row["target_norm"]
        numerator = verify_profile(norm["numerator"], f"row {row_index} norm n")
        denominator = verify_profile(norm["denominator"], f"row {row_index} norm d")
        target_roots = field_roots(numerator)
        require(
            row["target_norm_roots"] == target_roots
            and row["target_norm_root_count"] == len(target_roots),
            "complete target norm roots",
        )
        candidate_roots = set(target_roots)
        require(len(row["inverse_guards"]) == 7, "inverse guard count")
        for guard_index, guard in enumerate(row["inverse_guards"]):
            for part in ("numerator", "denominator"):
                coefficients = verify_profile(
                    guard[part],
                    f"row {row_index} guard {guard_index} {part}",
                )
                candidate_roots.update(field_roots(coefficients))
        candidate_roots.update(field_roots(denominator))
        require(
            row["candidate_roots"] == sorted(candidate_roots)
            and row["candidate_root_count"] == len(candidate_roots),
            "complete candidate-root union",
        )

        structure_row = next(
            item for item in structure["rows"]
            if item["epsilon"] == list(epsilon) and item["chart"] == 0
        )
        expected_relations = (
            parse_singular(structure_row["lex_basis"][0]["expression"], (t, r)),
            parse_singular(structure_row["lex_basis"][1]["expression"], (b, t, r)),
            parse_singular(structure_row["lex_basis"][5]["expression"], (c, b, t, r)),
        )
        printed_relations = tuple(
            sp.sympify(row[label])
            for label in ("base_relation", "b_relation", "c_relation")
        )
        for expected_relation, printed_relation in zip(
            expected_relations, printed_relations
        ):
            require(
                sp.Poly(
                    expected_relation-printed_relation,
                    *VARIABLES,
                    modulus=PRIME,
                ).is_zero,
                "printed source relation custody",
            )
        kernel_row = next(
            item for item in kernel_payload["rows"]
            if item["epsilon"] == list(epsilon)
        )
        kernel = tuple(
            sp.sympify(item["expression"]) for item in kernel_row["kernel"]
        )
        reconstruct_row(row, *expected_relations, kernel)
        lane_count = sum(
            len(q_row["lanes"])
            for finite in row["finite_rows"]
            for z_row in finite.get("z_rows", [])
            for q_row in z_row.get("q_rows", [])
        )
        final_lane_count += lane_count
        profiles[(
            row["target_norm_root_count"],
            row["candidate_root_count"],
            row["source_point_count"],
            row["route_point_count"],
            row["z_candidate_count"],
            row["q_candidate_count"],
        )] += 1

    require(actual == expected and len(actual) == 4, "4 exact sign rows")
    expected_profiles = collections.Counter({
        (9, 14, 14, 14, 8, 8): 4,
    })
    require(profiles == expected_profiles, "exact sign-profile multiset")
    require(
        sum(row["candidate_root_count"] for row in payload["rows"]) == 56
        and sum(row["source_point_count"] for row in payload["rows"]) == 56
        and sum(row["z_candidate_count"] for row in payload["rows"]) == 32
        and sum(row["q_candidate_count"] for row in payload["rows"]) == 32
        and final_lane_count == 128,
        "aggregate finite census",
    )
    return 4, 16, final_lane_count


def verify_source():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "class RationalFunction:",
        "common = numer.gcd(denom)",
        "2*missing_record - source_sum_record",
        "def polynomial_remainder(dividend, divisor):",
        "class PairBivariate:",
        "def nested_remainder(dividend, divisor):",
        "p_antipodal_q = paired_polynomial(q_polynomial, -q_polynomial)",
        "p_second_sign_free = p_second_qz*p_second_qz.negate_q()",
        "remainder_u = nested_remainder",
        "remainder_z = polynomial_remainder",
        "p_z_even**2-variable_polynomial*p_z_odd**2",
        "paired_polynomial(",
        "target_free = (",
        "target_norm = target_free.norm()",
        "candidate_roots.update(roots)",
        "for epsilon_1 in (-1, 1)",
    ):
        require(snippet in source, f"source construction {snippet}")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED", "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"parent edge {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer edge")


def main():
    formal_sign_free_identity()
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    verify_source()
    rows, raw_cases, lane_checks = verify_payload(json.loads(RESULT.read_text()))
    require((rows, raw_cases, lane_checks) == (4, 16, 128), "scope accounting")
    verify_dag()
    print(
        "cell=4 xi=3 pairing=4 raw_cases=16 sign_rows=4 candidate_r=56 "
        "source_points=56 z=32 q=32 lane_checks=128 witnesses=0"
    )


if __name__ == "__main__":
    main()
