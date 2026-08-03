#!/usr/bin/env python3
"""Solve the finite outside fibers left by the cell-3 xi2/pairing0 cut."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
KERNEL = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_compact_kernel_result.json"
REPLAY = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_xi2_pairing0_six_basis_root_replay_census_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_xi2_pairing0_outside_solver_result.json"
REMOTE_KERNEL = "/root/kernel.json"
REMOTE_REPLAY = "/root/replay.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell3-xi2-pairing0-outside-solver")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0", "python-flint==0.8.0")
    .add_local_file(KERNEL, REMOTE_KERNEL)
    .add_local_file(REPLAY, REMOTE_REPLAY)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=90, max_containers=4)
def solve_sign(signs):
    import sympy as sp
    from flint import fmpz_mod_poly_ctx

    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    replay_payload = json.loads(Path(REMOTE_REPLAY).read_text())
    kernel_row = next(
        row for row in kernel_payload["rows"] if row["epsilon"] == list(signs)
    )
    replay_row = next(
        row for row in replay_payload["rows"] if row["epsilon"] == list(signs)
    )
    if replay_row["epsilon"] != list(signs) or replay_row["status"] != "COMPLETE":
        raise ValueError("root-replay/sign custody mismatch")
    u, v, f = sp.symbols("u v f")
    polynomial_context = fmpz_mod_poly_ctx(PRIME)

    def compile_expression(expression):
        return [
            (exponents, int(coefficient) % PRIME)
            for exponents, coefficient in sp.Poly(
                sp.sympify(expression), *sp.symbols("c b t r"), modulus=PRIME
            ).terms()
        ]

    kernel_terms = [
        compile_expression(value["expression"])
        for value in kernel_row["kernel"]
    ]

    def evaluate_kernel(compiled, c_value, b_value, t_value, r_value):
        values = (c_value, b_value, t_value, r_value)
        return sum(
            coefficient
            * sp.prod(pow(value, exponent, PRIME)
                      for value, exponent in zip(values, exponents))
            for exponents, coefficient in compiled
        ) % PRIME

    def paired(a_values, b_values, left, right):
        p0, p1, p2 = (
            b_values[index]-left*a_values[index] for index in range(3)
        )
        q0 = b_values[0]-right*a_values[0]
        q1 = -b_values[1]+right*a_values[1]
        q2 = b_values[2]-right*a_values[2]
        return sp.expand(
            (p2*q0-p0*q2)**2-(p2*q1-p1*q2)*(p1*q0-p0*q1)
        )

    def flint_polynomial(poly, variable, substitutions):
        source = sp.Poly(poly, variable, *substitutions, modulus=PRIME)
        output = {}
        for exponents, coefficient in source.terms():
            value = int(coefficient) % PRIME
            for point, exponent in zip(substitutions.values(), exponents[1:]):
                value = value*pow(point, exponent, PRIME) % PRIME
            output[exponents[0]] = (output.get(exponents[0], 0)+value) % PRIME
        maximum = max(output, default=0)
        return polynomial_context([
            output.get(exponent, 0) for exponent in range(maximum+1)
        ])

    variable_poly = polynomial_context([0, 1])

    def field_roots(polynomial):
        if polynomial.is_zero():
            return None
        if int(polynomial.degree()) == 0:
            return []
        root_polynomial = polynomial.gcd(
            pow(variable_poly, PRIME, polynomial)-variable_poly
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

    def target_guards(representatives):
        failures = []
        for index, value in enumerate(representatives):
            if value % PRIME == 0:
                failures.append(f"nonzero_{index}")
        for left in range(6):
            for right in range(left+1, 6):
                if (representatives[left]-representatives[right]) % PRIME == 0:
                    failures.append(f"difference_{left}_{right}")
                if (representatives[left]+representatives[right]) % PRIME == 0:
                    failures.append(f"sum_{left}_{right}")
        return failures

    def evaluate_target(poly, values):
        source = sp.Poly(poly, u, v, f, modulus=PRIME)
        return sum(
            int(coefficient)
            * pow(values[0], exponents[0], PRIME)
            * pow(values[1], exponents[1], PRIME)
            * pow(values[2], exponents[2], PRIME)
            for exponents, coefficient in source.terms()
        ) % PRIME

    rows = []
    witnesses = []
    boundary_solutions = []
    for point in replay_row["target_free_zero_points"]:
        r_value, t_value, b_value, c_value = point
        kernel_values = [
            evaluate_kernel(value, c_value, b_value, t_value, r_value)
            for value in kernel_terms
        ]
        a_values = kernel_values[:3]
        b_values = kernel_values[3:6]
        beta_0, beta_1 = kernel_values[6:]
        missing_label = -t_value*t_value % PRIME
        a_missing = (
            a_values[0]+a_values[1]*missing_label
            + a_values[2]*missing_label*missing_label
        ) % PRIME
        b_missing = (
            b_values[0]+b_values[1]*missing_label
            + b_values[2]*missing_label*missing_label
        ) % PRIME
        if a_missing == 0:
            raise ValueError("root replay admitted a missing-ratio boundary")
        source_missing_record = b_missing*pow(a_missing, -1, PRIME) % PRIME
        de_value = -source_missing_record % PRIME

        for sigma_c in (-1, 1):
            for sigma_o in (-1, 1):
                rank_equation = de_value*f*f-u*v
                target_free_equation = paired(
                    a_values, b_values, de_value, de_value
                )
                outside_pair_equation = paired(
                    a_values, b_values, u, sigma_o*v
                )
                colored_pair_equation = paired(
                    a_values, b_values, b_value*f, sigma_c*c_value*f
                )
                sum_equation = (
                    f*f*missing_label
                    * (beta_0+beta_1*missing_label)**2
                    - (u-v)**2*a_missing*a_missing
                )
                if int(target_free_equation) % PRIME != 0:
                    raise ValueError("target-free replay changed value")
                substitution = de_value*f*f/u
                outside_cleared = sp.together(
                    outside_pair_equation.subs(v, substitution)
                ).as_numer_denom()[0]
                sum_cleared = sp.together(
                    sum_equation.subs(v, substitution)
                ).as_numer_denom()[0]
                colored_f = flint_polynomial(
                    colored_pair_equation, f, {u: 0, v: 0}
                )
                f_roots = field_roots(colored_f)
                case_row = {
                    "point": point,
                    "sigma": [sigma_c, sigma_o],
                    "de": de_value,
                    "colored_degree": (
                        None if f_roots is None else int(colored_f.degree())
                    ),
                    "f_roots": f_roots,
                    "f_rows": [],
                }
                if f_roots is None:
                    case_row["status"] = "ZERO_COLORED_CUT"
                    rows.append(case_row)
                    continue
                for f_value in f_roots:
                    f_row = {"f": f_value}
                    if f_value == 0:
                        f_row["status"] = "TARGET_BOUNDARY"
                        f_row["failed_guards"] = ["nonzero_5"]
                        boundary_solutions.append({
                            "point": point, "sigma": [sigma_c, sigma_o],
                            **f_row,
                        })
                        case_row["f_rows"].append(f_row)
                        continue
                    outside_u = flint_polynomial(
                        outside_cleared, u, {v: 0, f: f_value}
                    )
                    sum_u = flint_polynomial(
                        sum_cleared, u, {v: 0, f: f_value}
                    )
                    if outside_u.is_zero() and sum_u.is_zero():
                        f_row["status"] = "ZERO_U_CUTS"
                        case_row["f_rows"].append(f_row)
                        continue
                    common_u = (
                        sum_u if outside_u.is_zero() else outside_u
                        if sum_u.is_zero() else outside_u.gcd(sum_u)
                    )
                    u_roots = field_roots(common_u)
                    f_row["u_gcd_degree"] = (
                        None if u_roots is None else int(common_u.degree())
                    )
                    f_row["u_roots"] = u_roots
                    f_row["u_rows"] = []
                    if u_roots is None:
                        f_row["status"] = "ZERO_U_GCD"
                        case_row["f_rows"].append(f_row)
                        continue
                    for u_value in u_roots:
                        u_row = {"u": u_value}
                        if u_value == 0:
                            u_row["status"] = "TARGET_BOUNDARY"
                            u_row["failed_guards"] = ["nonzero_d"]
                            f_row["u_rows"].append(u_row)
                            continue
                        v_value = de_value*f_value*f_value*pow(
                            u_value, -1, PRIME
                        ) % PRIME
                        d_value = u_value*pow(f_value, -1, PRIME) % PRIME
                        e_value = v_value*pow(f_value, -1, PRIME) % PRIME
                        representatives = (
                            1, b_value, c_value, d_value, e_value, f_value
                        )
                        failures = target_guards(representatives)
                        equation_values = [
                            evaluate_target(value, (u_value, v_value, f_value))
                            for value in (
                                rank_equation, target_free_equation,
                                outside_pair_equation, colored_pair_equation,
                                sum_equation,
                            )
                        ]
                        if any(equation_values):
                            raise ValueError("direct target-equation replay failed")
                        u_row.update({
                            "v": v_value,
                            "target_representatives": list(representatives),
                            "failed_guards": failures,
                            "equation_values": equation_values,
                            "status": "TARGET_BOUNDARY" if failures else "WITNESS",
                        })
                        record = {
                            "point": point, "sigma": [sigma_c, sigma_o],
                            **u_row,
                        }
                        (boundary_solutions if failures else witnesses).append(record)
                        f_row["u_rows"].append(u_row)
                    f_row["status"] = "CHECKED"
                    case_row["f_rows"].append(f_row)
                case_row["status"] = "CHECKED"
                rows.append(case_row)

    unresolved = [
        [row["point"], row["sigma"], row["status"]]
        for row in rows if row["status"] != "CHECKED"
    ]
    return {
        "epsilon": list(signs),
        "xi_index": 2,
        "pairing_index": 0,
        "status": "COMPLETE" if not unresolved else "INCOMPLETE",
        "case_count": len(rows),
        "rows": rows,
        "boundary_solutions": boundary_solutions,
        "witnesses": witnesses,
        "unresolved": unresolved,
        "case_excluded": not witnesses and not unresolved,
    }


@app.local_entrypoint()
def main(signs: str = "-1:-1", all_signs: bool = False):
    selected_signs = (
        ((-1, -1), (-1, 1), (1, -1), (1, 1))
        if all_signs else (tuple(int(value) for value in signs.split(":")),)
    )
    raw = list(solve_sign.map(
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
            "rate-half-kb-positive-433-1b-cell3-xi2-pairing0-outside-census-v1"
            if all_signs else
            "rate-half-kb-positive-433-1b-cell3-xi2-pairing0-outside-solver-v1"
        ),
        "scope": (
            "All four target sign lanes above the exact xi2/pairing0 common "
            "cut for one source-sign row."
        ),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "source_replay_sha256": hashlib.sha256(REPLAY.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [{
            "epsilon": row.get("epsilon"),
            "status": row.get("status"),
            "error": row.get("error"),
            "fiber_case_count": row.get("case_count"),
            "boundary_solution_count": len(row.get("boundary_solutions", [])),
            "witness_count": len(row.get("witnesses", [])),
            "unresolved": row.get("unresolved"),
            "case_excluded": row.get("case_excluded"),
        } for row in rows],
    }, sort_keys=True))
