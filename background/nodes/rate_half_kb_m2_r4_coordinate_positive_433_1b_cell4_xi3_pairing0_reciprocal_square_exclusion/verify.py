#!/usr/bin/env python3
"""Independently verify the cell-4 xi3/pairing-0 exclusion."""

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
    "rate_half_kb_positive_433_1b_cell4_xi3_pairing0_"
    "reciprocal_square_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairing0_"
    "reciprocal_square_result.json"
)
STRUCTURE = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_remaining_compact_pivot_scout_result.json"
)
KERNEL = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_compact_kernel_result.json"
)
PINNED = {
    SCRIPT: "be6e74f8713af6f26fe183a00e5bc50d0a89aa1fdd53c1c636525165a2f5ae68",
    RESULT: "41ec67dd29fa9c3e3d6b640e0a8ea997f9c921d6322f4d638a967878de9f4d8f",
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
    return sorted(set(roots))


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
    require(degree == 2, "finite replay polynomial is at most quadratic")
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


def paired_coefficients(a_values, b_values, left, right_scale):
    samples = [
        paired(a_values, b_values, left, right_scale*y_value % PRIME)
        for y_value in (0, 1, 2)
    ]
    inverse_two = pow(2, -1, PRIME)
    quadratic = (samples[2]-2*samples[1]+samples[0])*inverse_two % PRIME
    linear = (samples[1]-samples[0]-quadratic) % PRIME
    return trim([samples[0], linear, quadratic])


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
    branch_index = row["branch_index"]
    sigma_o = row["sigma_o"]
    candidate_roots = row["candidate_roots"]
    route_guards = (
        b, c, r, t, b-1, b+1, c-1, c+1, b-c, b+c,
        r*r-1, r*r+1, t*t-1, t*t+1,
        t*t-r*r, t*t+r*r,
    )
    boundary_rows = []
    target_boundary_rows = []
    no_lift_rows = []
    finite_rows = []
    yd_candidates = []
    final_pair_solutions = []
    witnesses = []
    unresolved = []
    source_point_count = 0
    route_point_count = 0

    for r_value in candidate_roots:
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
                    "branch_index": branch_index,
                    "sigma_o": sigma_o,
                    "yd_rows": [],
                }
                if missing == 0:
                    branch_row["status"] = "TARGET_PRODUCT_BOUNDARY"
                    target_boundary_rows.append(branch_row)
                    finite_rows.append(branch_row)
                    continue
                a_branch = a_values[branch_index]
                b_branch = b_values[branch_index]
                branch_row.update({"a_branch": a_branch, "b_branch": b_branch})
                if a_branch == 0:
                    branch_row["status"] = (
                        "FREE_Q_BRANCH" if b_branch == 0 else "EMPTY_Q_BRANCH"
                    )
                    if b_branch == 0:
                        unresolved.append({
                            **point,
                            "branch_index": branch_index,
                            "reason": "FREE_Q_BRANCH",
                        })
                    finite_rows.append(branch_row)
                    continue
                q_value = b_branch*pow(a_branch, -1, PRIME) % PRIME
                same_pair = paired(a_values, b_values, q_value, q_value)
                require(same_pair == 0, "q branch satisfies paired(q,q)")
                missing_y_roots = roots_from_coefficients([
                    1,
                    (2*missing-source_sum) % PRIME,
                    missing*missing % PRIME,
                ])
                outside_y_roots = roots_from_coefficients(paired_coefficients(
                    a_values,
                    b_values,
                    -q_value % PRIME,
                    sigma_o*q_value*missing % PRIME,
                ))
                require(missing_y_roots is not None, "monic missing cut")
                y_roots = (
                    missing_y_roots if outside_y_roots is None
                    else sorted(set(missing_y_roots) & set(outside_y_roots))
                )
                branch_row.update({
                    "q": q_value,
                    "same_pair_cut": same_pair,
                    "missing_y_roots": missing_y_roots,
                    "outside_y_roots": outside_y_roots,
                    "common_y_roots": y_roots,
                })
                for y_value in y_roots:
                    require(y_value != 0, "reciprocal-square root nonzero")
                    require(
                        (1+(2*missing-source_sum)*y_value
                         + missing*missing*y_value*y_value) % PRIME == 0,
                        "missing cut replay",
                    )
                    d_squared = pow(y_value, -1, PRIME)
                    d_roots = roots_from_coefficients([
                        -d_squared % PRIME, 0, 1,
                    ])
                    require(d_roots is not None, "monic square lift")
                    y_row = {
                        "y": y_value,
                        "d_squared": d_squared,
                        "d_roots": d_roots,
                        "d_rows": [],
                    }
                    for d_value in d_roots:
                        inverse_d = pow(d_value, -1, PRIME)
                        e_value = q_value*inverse_d % PRIME
                        f_value = missing*inverse_d % PRIME
                        candidate = {
                            "r": point["r"],
                            "t": point["t"],
                            "b": point["b"],
                            "c": point["c"],
                            "branch_index": branch_index,
                            "sigma_o": sigma_o,
                            "q": q_value,
                            "y": y_value,
                            "d": d_value,
                            "e": e_value,
                            "f": f_value,
                        }
                        yd_candidates.append(candidate)
                        outside_pair = paired(
                            a_values,
                            b_values,
                            -q_value % PRIME,
                            sigma_o*e_value*f_value % PRIME,
                        )
                        require(outside_pair == 0, "outside pair replay")
                        d_row = {
                            "d": d_value,
                            "e": e_value,
                            "f": f_value,
                            "outside_pair_cut": outside_pair,
                            "lanes": [],
                        }
                        for sigma_c in (-1, 1):
                            final_pair = paired(
                                a_values,
                                b_values,
                                point["b"]*f_value % PRIME,
                                sigma_c*point["c"]*f_value % PRIME,
                            )
                            lane_row = {
                                "sigma": [sigma_c, sigma_o],
                                "final_pair_cut": final_pair,
                            }
                            if final_pair:
                                lane_row["status"] = "THIRD_PAIR_NONZERO"
                                d_row["lanes"].append(lane_row)
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
                                same_pair,
                                outside_pair,
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
                            d_row["lanes"].append(lane_row)
                        y_row["d_rows"].append(d_row)
                    branch_row["yd_rows"].append(y_row)
                branch_row["status"] = "CHECKED"
                finite_rows.append(branch_row)

    replay = {
        "source_point_count": source_point_count,
        "route_point_count": route_point_count,
        "boundary_rows": boundary_rows,
        "target_boundary_rows": target_boundary_rows,
        "no_lift_rows": no_lift_rows,
        "finite_rows": finite_rows,
        "yd_candidate_count": len(yd_candidates),
        "yd_candidates": yd_candidates,
        "final_pair_solution_count": len(final_pair_solutions),
        "final_pair_solutions": final_pair_solutions,
        "witness_count": len(witnesses),
        "witnesses": witnesses,
        "unresolved": unresolved,
        "target_excluded": not witnesses and not unresolved,
    }
    for key, expected in replay.items():
        require(row[key] == expected, f"independent finite replay {key}")


def formal_same_pair_identity():
    a0, a1, a2, b0, b1, b2, q = sp.symbols("a0 a1 a2 b0 b1 b2 q")
    linear = [b0-q*a0, b1-q*a1, b2-q*a2]
    p0, p1, p2 = linear
    q0, q1, q2 = p0, -p1, p2
    paired_expression = (
        (p2*q0-p0*q2)**2-(p2*q1-p1*q2)*(p1*q0-p0*q1)
    )
    require(
        sp.expand(paired_expression-4*p0*p1*p1*p2) == 0,
        "formal paired(q,q) factorization",
    )


def verify_payload(payload):
    require(
        payload["schema"] ==
        "rate-half-kb-positive-433-1b-cell4-xi3-pairing0-"
        "reciprocal-square-v1",
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
    expected = {
        (epsilon, branch, sigma_o)
        for epsilon in SIGNS
        for branch in (0, 1, 2)
        for sigma_o in (-1, 1)
    }
    actual = set()
    profiles = collections.Counter()
    final_lane_count = 0

    for row_index, row in enumerate(payload["rows"]):
        key = (tuple(row["epsilon"]), row["branch_index"], row["sigma_o"])
        require(key in expected and key not in actual, "branch Cartesian row")
        actual.add(key)
        epsilon, branch_index, sigma_o = key
        require(
            row["xi_index"] == 3
            and row["pairing_index"] == 0
            and row["status"] == "COMPLETE"
            and row["target_excluded"]
            and row["unresolved"] == []
            and row["witnesses"] == [],
            "complete scoped exclusion",
        )
        require(
            (row["missing_cut_degree"], row["outside_cut_degree"]) == (2, 2),
            "quadratic reciprocal-square cuts",
        )
        for label, profiles_list, expected_length in (
            ("q", row["q_branch_profiles"], 4),
            ("target", row["target_free_profiles"], 4),
        ):
            require(len(profiles_list) == expected_length, f"{label} basis")
            for profile_index, profile in enumerate(profiles_list):
                for part in ("numerator", "denominator"):
                    verify_compact_profile(
                        profile[part],
                        f"row {row_index} {label} {profile_index} {part}",
                    )
        for label in ("missing_cut_profiles", "outside_cut_profiles"):
            require(len(row[label]) == 3, f"{label} coefficient count")
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
        require(len(row["inverse_guards"]) == 6, "inverse guard count")
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
            len(d_row["lanes"])
            for finite in row["finite_rows"]
            for y_row in finite.get("yd_rows", [])
            for d_row in y_row.get("d_rows", [])
        )
        final_lane_count += lane_count
        profiles[(
            branch_index,
            sigma_o,
            row["target_norm_root_count"],
            row["candidate_root_count"],
            row["source_point_count"],
            row["yd_candidate_count"],
        )] += 1

    require(actual == expected and len(actual) == 24, "24 exact branch rows")
    expected_profiles = collections.Counter({
        (1, -1, 5, 9, 6, 8): 4,
        (1, 1, 6, 10, 8, 8): 4,
        (0, -1, 5, 8, 2, 0): 2,
        (0, 1, 5, 8, 2, 0): 2,
        (2, -1, 6, 8, 0, 0): 2,
        (2, 1, 5, 7, 0, 0): 2,
        (0, -1, 6, 8, 0, 0): 2,
        (0, 1, 5, 7, 0, 0): 2,
        (2, -1, 5, 8, 2, 0): 2,
        (2, 1, 5, 8, 2, 0): 2,
    })
    require(profiles == expected_profiles, "exact branch-profile multiset")
    require(
        sum(row["candidate_root_count"] for row in payload["rows"]) == 200
        and sum(row["source_point_count"] for row in payload["rows"]) == 72
        and sum(row["yd_candidate_count"] for row in payload["rows"]) == 64
        and final_lane_count == 128,
        "aggregate finite census",
    )
    return 24, 16, final_lane_count


def verify_source():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "class RationalFunction:",
        "common = numer.gcd(denom)",
        "q_record = b_coefficients[branch_index] / a_coefficients[branch_index]",
        "2*missing_record - source_sum_record",
        "paired_polynomial(",
        "target_free = (",
        "target_norm = target_free.norm()",
        "candidate_roots.update(roots)",
        "for branch_index in (0, 1, 2)",
        "for sigma_o in (-1, 1)",
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
    formal_same_pair_identity()
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    verify_source()
    rows, raw_cases, lane_checks = verify_payload(json.loads(RESULT.read_text()))
    require((rows, raw_cases, lane_checks) == (24, 16, 128), "scope accounting")
    verify_dag()
    print(
        "cell=4 xi=3 pairing=0 raw_cases=16 branch_rows=24 "
        "candidate_r=200 source_points=72 yd=64 lane_checks=128 witnesses=0"
    )


if __name__ == "__main__":
    main()
