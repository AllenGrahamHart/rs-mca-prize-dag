#!/usr/bin/env python3
"""Lift the cell-3 six-basis target-free norm roots over the deployed field."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
QUOTIENT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_birational_profile_result.json"
KERNEL = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_compact_kernel_result.json"
PRODUCT = DIRECTORY / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
PILOT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_six_basis_cut_census_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_six_basis_cut_root_replay_result.json"
CENSUS_RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_six_basis_cut_root_replay_census_result.json"
REMOTE_QUOTIENT = "/root/quotient.json"
REMOTE_KERNEL = "/root/kernel.json"
REMOTE_PRODUCT = "/root/product.json"
REMOTE_PILOT = "/root/pilot.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell3-six-basis-cut-root-replay")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0", "python-flint==0.8.0")
    .add_local_file(QUOTIENT, REMOTE_QUOTIENT)
    .add_local_file(KERNEL, REMOTE_KERNEL)
    .add_local_file(PRODUCT, REMOTE_PRODUCT)
    .add_local_file(PILOT, REMOTE_PILOT)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=90, max_containers=4)
def replay(signs):
    import sympy as sp
    from flint import fmpz_mod_poly_ctx

    epsilon_1, epsilon_2 = signs
    quotient = json.loads(Path(REMOTE_QUOTIENT).read_text())
    kernel = json.loads(Path(REMOTE_KERNEL).read_text())
    product = json.loads(Path(REMOTE_PRODUCT).read_text())
    pilot = json.loads(Path(REMOTE_PILOT).read_text())
    source = next(
        row for row in quotient["rows"]
        if row["epsilon"] == list(signs) and row["chart"] == 0
    )
    kernel_row = next(
        row for row in kernel["rows"] if row["epsilon"] == list(signs)
    )
    product_row = next(row for row in product["rows"] if row["cell"] == 3)
    pilot_row = next(
        row for row in pilot["rows"] if row["epsilon"] == list(signs)
    )
    if pilot_row["epsilon"] != list(signs) or pilot_row["status"] != "COMPLETE":
        raise ValueError("pilot/sign custody mismatch")

    t, r, c, b = sp.symbols("t r c b")
    interface = source["quotient_interface"]
    polynomial_context = fmpz_mod_poly_ctx(PRIME)

    def terms(expression, variables):
        return [
            (exponents, int(coefficient) % PRIME)
            for exponents, coefficient in sp.Poly(
                sp.sympify(expression), *variables, modulus=PRIME
            ).terms()
        ]

    base_terms = terms(interface["base_relation"]["expression"], (t, r))
    b_terms = terms(interface["b_relation"]["expression"], (b, t, r))
    c_constant_terms = terms(interface["c_constant"]["expression"], (b, t, r))
    c_denominator_terms = terms(
        interface["c_denominator"]["expression"], (t, r)
    )
    kernel_terms = [
        terms(value["expression"], (c, b, t, r))
        for value in kernel_row["kernel"]
    ]
    cofactor_terms = [
        terms(value, (t, r, c, b))
        for value in product_row["stripped_expressions"]
    ]

    def evaluate(compiled, values):
        return sum(
            coefficient
            * sp.prod(pow(value, exponent, PRIME)
                      for value, exponent in zip(values, exponents))
            for exponents, coefficient in compiled
        ) % PRIME

    def specialized_coefficients(compiled, variable_position, values):
        maximum = max(exponents[variable_position] for exponents, _ in compiled)
        coefficients = [0]*(maximum+1)
        for exponents, coefficient in compiled:
            value = coefficient
            for position, point in enumerate(values):
                if position == variable_position:
                    continue
                value = value*pow(point, exponents[position], PRIME) % PRIME
            degree = exponents[variable_position]
            coefficients[degree] = (coefficients[degree]+value) % PRIME
        return coefficients

    def field_roots(coefficients):
        polynomial = polynomial_context(coefficients)
        if polynomial.is_zero():
            return None
        if int(polynomial.degree()) == 0:
            return []
        variable = polynomial_context([0, 1])
        root_polynomial = polynomial.gcd(
            pow(variable, PRIME, polynomial)-variable
        )
        _, factors = root_polynomial.factor()
        roots = []
        for factor, _ in factors:
            if int(factor.degree()) != 1:
                raise ValueError("field-root gcd has nonlinear factor")
            roots.append(
                -int(factor[0])*pow(int(factor[1]), -1, PRIME) % PRIME
            )
        return sorted(roots)

    def r_guards(r_value):
        values = {
            "r": r_value,
            "r2_minus_1": r_value*r_value-1,
            "r2_plus_1": r_value*r_value+1,
        }
        return [name for name, value in values.items() if value % PRIME == 0]

    def tr_guards(t_value, r_value):
        values = {
            "t": t_value,
            "t2_minus_1": t_value*t_value-1,
            "t2_plus_1": t_value*t_value+1,
            "t2_minus_r2": t_value*t_value-r_value*r_value,
            "t2_plus_r2": t_value*t_value+r_value*r_value,
        }
        return [name for name, value in values.items() if value % PRIME == 0]

    def bc_guards(b_value, c_value):
        values = {
            "b": b_value, "c": c_value,
            "b_minus_1": b_value-1, "b_plus_1": b_value+1,
            "c_minus_1": c_value-1, "c_plus_1": c_value+1,
            "b_minus_c": b_value-c_value, "b_plus_c": b_value+c_value,
        }
        return [name for name, value in values.items() if value % PRIME == 0]

    root_rows = []
    guarded_common_points = []
    target_free_zero_points = []
    for r_value in pilot_row["field_roots"]:
        row = {"r": r_value, "r_zero_guards": r_guards(r_value), "t_rows": []}
        if row["r_zero_guards"]:
            row["status"] = "ROUTE_BOUNDARY"
            root_rows.append(row)
            continue
        t_coefficients = specialized_coefficients(base_terms, 0, (0, r_value))
        t_roots = field_roots(t_coefficients)
        row["t_roots"] = t_roots
        if t_roots is None:
            row["status"] = "ZERO_BASE_POLYNOMIAL"
            root_rows.append(row)
            continue
        for t_value in t_roots:
            t_row = {
                "t": t_value,
                "tr_zero_guards": tr_guards(t_value, r_value),
                "b_rows": [],
            }
            if t_row["tr_zero_guards"]:
                t_row["status"] = "ROUTE_BOUNDARY"
                row["t_rows"].append(t_row)
                continue
            b_coefficients = specialized_coefficients(
                b_terms, 0, (0, t_value, r_value)
            )
            b_roots = field_roots(b_coefficients)
            t_row["b_roots"] = b_roots
            if b_roots is None:
                t_row["status"] = "ZERO_B_POLYNOMIAL"
                row["t_rows"].append(t_row)
                continue
            for b_value in b_roots:
                c_denominator = evaluate(
                    c_denominator_terms, (t_value, r_value)
                )
                b_row = {"b": b_value, "c_denominator": c_denominator}
                if c_denominator == 0:
                    b_row["status"] = "C_DENOMINATOR_BOUNDARY"
                    t_row["b_rows"].append(b_row)
                    continue
                c_constant = evaluate(
                    c_constant_terms, (b_value, t_value, r_value)
                )
                c_value = -c_constant*pow(c_denominator, -1, PRIME) % PRIME
                b_row["c"] = c_value
                b_row["bc_zero_guards"] = bc_guards(b_value, c_value)
                cofactors = [
                    evaluate(value, (t_value, r_value, c_value, b_value))
                    for value in cofactor_terms
                ]
                b_row["nonzero_cofactor_indices"] = [
                    index for index, value in enumerate(cofactors) if value
                ]
                if b_row["bc_zero_guards"]:
                    b_row["status"] = "ROUTE_BOUNDARY"
                    t_row["b_rows"].append(b_row)
                    continue
                if not b_row["nonzero_cofactor_indices"]:
                    b_row["status"] = "PRODUCT_RANK_DROP"
                    t_row["b_rows"].append(b_row)
                    continue
                kernel_values = [
                    evaluate(value, (c_value, b_value, t_value, r_value))
                    for value in kernel_terms
                ]
                a_values = kernel_values[:3]
                b_values = kernel_values[3:6]
                missing_label = -t_value*t_value % PRIME
                a_missing = (
                    a_values[0]+a_values[1]*missing_label
                    + a_values[2]*missing_label*missing_label
                ) % PRIME
                b_missing = (
                    b_values[0]+b_values[1]*missing_label
                    + b_values[2]*missing_label*missing_label
                ) % PRIME
                b_row["a_missing"] = a_missing
                b_row["b_missing"] = b_missing
                if a_missing == 0:
                    b_row["status"] = (
                        "MISSING_RATIO_FREE" if b_missing == 0
                        else "MISSING_RATIO_INCONSISTENT"
                    )
                    t_row["b_rows"].append(b_row)
                    continue
                missing_record = b_missing*pow(a_missing, -1, PRIME) % PRIME
                left, right = missing_record, -missing_record % PRIME
                p0, p1, p2 = (
                    (b_values[index]-left*a_values[index]) % PRIME
                    for index in range(3)
                )
                q0 = (b_values[0]-right*a_values[0]) % PRIME
                q1 = (-b_values[1]+right*a_values[1]) % PRIME
                q2 = (b_values[2]-right*a_values[2]) % PRIME
                target_free = (
                    (p2*q0-p0*q2)**2
                    - (p2*q1-p1*q2)*(p1*q0-p0*q1)
                ) % PRIME
                b_row["missing_record"] = missing_record
                b_row["target_free_value"] = target_free
                b_row["status"] = (
                    "TARGET_FREE_ZERO" if target_free == 0
                    else "TARGET_FREE_NONZERO"
                )
                point = [r_value, t_value, b_value, c_value]
                guarded_common_points.append(point)
                if target_free == 0:
                    target_free_zero_points.append(point)
                t_row["b_rows"].append(b_row)
            t_row["status"] = "CHECKED"
            row["t_rows"].append(t_row)
        row["status"] = "CHECKED"
        root_rows.append(row)

    return {
        "epsilon": list(signs),
        "xi_index": 0,
        "pairing_index": 0,
        "target_lanes_covered": [[x, y] for x in (-1, 1) for y in (-1, 1)],
        "status": "COMPLETE",
        "norm_root_count": len(pilot_row["field_roots"]),
        "root_rows": root_rows,
        "guarded_common_points": guarded_common_points,
        "target_free_zero_points": target_free_zero_points,
        "case_excluded": not target_free_zero_points,
    }


@app.local_entrypoint()
def main(signs: str = "-1:-1", all_signs: bool = False):
    selected_signs = (
        ((-1, -1), (-1, 1), (1, -1), (1, 1))
        if all_signs else (tuple(int(value) for value in signs.split(":")),)
    )
    raw = list(replay.map(
        selected_signs, order_outputs=True, return_exceptions=True
    ))
    rows = []
    for epsilon, row in zip(selected_signs, raw):
        rows.append(
            {"epsilon": list(epsilon), "status": "REMOTE_ERROR", "error": repr(row)}
            if isinstance(row, BaseException) else row
        )
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-cell3-six-basis-cut-root-replay-census-v1"
            if all_signs else
            "rate-half-kb-positive-433-1b-cell3-six-basis-cut-root-replay-v1"
        ),
        "scope": (
            "Exact deployed-field lift of one target-free norm root ledger; "
            "no claim outside the printed sign/missing/matching scope."
        ),
        "source_quotient_sha256": hashlib.sha256(QUOTIENT.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "source_product_sha256": hashlib.sha256(PRODUCT.read_bytes()).hexdigest(),
        "source_pilot_sha256": hashlib.sha256(PILOT.read_bytes()).hexdigest(),
        "rows": rows,
    }
    output_path = CENSUS_RESULT if all_signs else RESULT
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(output_path),
        "rows": [{
            "epsilon": row.get("epsilon"),
            "status": row.get("status"),
            "error": row.get("error"),
            "norm_root_count": row.get("norm_root_count"),
            "guarded_common_point_count": len(row.get("guarded_common_points", [])),
            "target_free_zero_point_count": len(row.get("target_free_zero_points", [])),
        } for row in rows],
    }, sort_keys=True))
