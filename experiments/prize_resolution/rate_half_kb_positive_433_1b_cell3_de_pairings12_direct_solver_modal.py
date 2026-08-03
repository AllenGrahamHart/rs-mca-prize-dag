#!/usr/bin/env python3
"""Solve cell-3 DE-missing pairings 1 and 2 from proved target-free ledgers."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
KERNEL = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_compact_kernel_result.json"
REPLAY0 = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_six_basis_cut_root_replay_census_result.json"
REPLAY2 = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_xi2_pairing0_six_basis_root_replay_census_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_de_pairings12_direct_solver_result.json"
REMOTE_KERNEL = "/root/kernel.json"
REMOTE_REPLAY0 = "/root/replay0.json"
REMOTE_REPLAY2 = "/root/replay2.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell3-de-pairings12-direct-solver")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0", "python-flint==0.8.0")
    .add_local_file(KERNEL, REMOTE_KERNEL)
    .add_local_file(REPLAY0, REMOTE_REPLAY0)
    .add_local_file(REPLAY2, REMOTE_REPLAY2)
)


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        second = values[index]
        rest = values[1:index]+values[index+1:]
        for tail in pairings(rest):
            yield ((first, second),)+tail


@app.function(image=image, cpu=1.0, memory=2048, timeout=90, max_containers=16)
def solve_case(case):
    import sympy as sp
    from flint import fmpz_mod_poly_ctx

    epsilon_1, epsilon_2, xi_index, pairing_index = case
    if xi_index not in (0, 2) or pairing_index not in (1, 2):
        raise ValueError("scope is xi in {0,2}, pairing in {1,2}")
    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    replay_payload = json.loads(Path(
        REMOTE_REPLAY0 if xi_index == 0 else REMOTE_REPLAY2
    ).read_text())
    signs = [epsilon_1, epsilon_2]
    kernel_row = next(row for row in kernel_payload["rows"]
                      if row["epsilon"] == signs)
    replay_row = next(row for row in replay_payload["rows"]
                      if row["epsilon"] == signs)
    if replay_row["status"] != "COMPLETE" or replay_row["xi_index"] != xi_index:
        raise ValueError("root-replay custody mismatch")

    c_symbol, b_symbol, t_symbol, r_symbol = sp.symbols("c b t r")
    f_symbol, d_symbol = sp.symbols("f d")
    polynomial_context = fmpz_mod_poly_ctx(PRIME)
    variable_poly = polynomial_context([0, 1])

    def compile_expression(expression):
        return [
            (exponents, int(coefficient) % PRIME)
            for exponents, coefficient in sp.Poly(
                sp.sympify(expression), c_symbol, b_symbol, t_symbol, r_symbol,
                modulus=PRIME,
            ).terms()
        ]

    kernel_terms = [
        compile_expression(value["expression"])
        for value in kernel_row["kernel"]
    ]

    def evaluate_kernel(compiled, c_value, b_value, t_value, r_value):
        values = (c_value, b_value, t_value, r_value)
        return sum(
            coefficient*sp.prod(
                pow(value, exponent, PRIME)
                for value, exponent in zip(values, exponents)
            )
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

    def flint_polynomial(expression, variable):
        source = sp.Poly(expression, variable, modulus=PRIME)
        coefficients = {}
        for (degree,), coefficient in source.terms():
            coefficients[degree] = int(coefficient) % PRIME
        maximum = max(coefficients, default=0)
        return polynomial_context([
            coefficients.get(degree, 0) for degree in range(maximum+1)
        ])

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

    matching = tuple(pairings(range(6)))[pairing_index]
    rows = []
    witnesses = []
    boundary_solutions = []
    unresolved = []
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
            raise ValueError("missing-ratio boundary in proved replay")
        source_missing = b_missing*pow(a_missing, -1, PRIME) % PRIME
        de_value = source_missing if xi_index == 0 else -source_missing % PRIME
        source_sum = (
            missing_label
            * pow((beta_0+beta_1*missing_label) % PRIME, 2, PRIME)
            * pow(a_missing, -2, PRIME)
        ) % PRIME
        sign = 1 if xi_index == 0 else -1
        d_equation = (
            (d_symbol*d_symbol+sign*de_value)**2
            - source_sum*d_symbol*d_symbol
        )
        d_polynomial = flint_polynomial(d_equation, d_symbol)
        d_roots = field_roots(d_polynomial)
        if d_roots is None:
            unresolved.append([point, "ZERO_D_EQUATION"])
            continue
        point_row = {
            "point": point,
            "source_missing": source_missing,
            "de": de_value,
            "source_sum": source_sum,
            "d_degree": int(d_polynomial.degree()),
            "d_roots": d_roots,
            "lanes": [],
        }
        for sigma_c in (-1, 1):
            for sigma_o in (-1, 1):
                lane_row = {"sigma": [sigma_c, sigma_o], "d_rows": []}
                for d_value in d_roots:
                    d_row = {"d": d_value, "f_rows": []}
                    if d_value == 0:
                        d_row["status"] = "TARGET_BOUNDARY"
                        d_row["failed_guards"] = ["nonzero_3"]
                        boundary_solutions.append({
                            "point": point, "sigma": [sigma_c, sigma_o],
                            **d_row,
                        })
                        lane_row["d_rows"].append(d_row)
                        continue
                    e_value = de_value*pow(d_value, -1, PRIME) % PRIME
                    records = (
                        de_value,
                        -de_value % PRIME if xi_index == 0 else de_value,
                        d_value*f_symbol,
                        sigma_o*e_value*f_symbol,
                        b_value*f_symbol,
                        sigma_c*c_value*f_symbol,
                    )
                    equations = [
                        paired(a_values, b_values,
                               records[left], records[right])
                        for left, right in matching
                    ]
                    first = flint_polynomial(equations[0], f_symbol)
                    if not first.is_zero():
                        raise ValueError("proved target-free pair changed")
                    cuts = [flint_polynomial(value, f_symbol)
                            for value in equations[1:]]
                    if cuts[0].is_zero() and cuts[1].is_zero():
                        d_row["status"] = "ZERO_F_CUTS"
                        unresolved.append([point, [sigma_c, sigma_o], d_value,
                                           "ZERO_F_CUTS"])
                        lane_row["d_rows"].append(d_row)
                        continue
                    common = (
                        cuts[1] if cuts[0].is_zero() else cuts[0]
                        if cuts[1].is_zero() else cuts[0].gcd(cuts[1])
                    )
                    f_roots = field_roots(common)
                    d_row["e"] = e_value
                    d_row["f_gcd_degree"] = (
                        None if f_roots is None else int(common.degree())
                    )
                    d_row["f_roots"] = f_roots
                    if f_roots is None:
                        d_row["status"] = "ZERO_F_GCD"
                        unresolved.append([point, [sigma_c, sigma_o], d_value,
                                           "ZERO_F_GCD"])
                        lane_row["d_rows"].append(d_row)
                        continue
                    for f_value in f_roots:
                        representatives = (
                            1, b_value, c_value, d_value, e_value, f_value
                        )
                        failures = target_guards(representatives)
                        full_records = (
                            de_value, de_value, -de_value % PRIME,
                            d_value*f_value, sigma_o*e_value*f_value,
                            b_value*f_value, sigma_c*c_value*f_value,
                        )
                        full_sums = (
                            (d_value+e_value)**2,
                            (d_value+e_value)**2,
                            (d_value-e_value)**2,
                            (d_value+f_value)**2,
                            (e_value+sigma_o*f_value)**2,
                            (b_value+f_value)**2,
                            (c_value+sigma_c*f_value)**2,
                        )
                        equation_values = [
                            (full_records[xi_index]-source_missing) % PRIME,
                            (full_sums[xi_index]-source_sum) % PRIME,
                            *(int(value.subs(f_symbol, f_value)) % PRIME
                              for value in equations),
                        ]
                        if any(equation_values):
                            raise ValueError("direct target-equation replay failed")
                        f_row = {
                            "f": f_value,
                            "target_representatives": list(representatives),
                            "failed_guards": failures,
                            "equation_values": equation_values,
                            "status": "TARGET_BOUNDARY" if failures else "WITNESS",
                        }
                        record = {
                            "point": point, "sigma": [sigma_c, sigma_o],
                            "d": d_value, "e": e_value, **f_row,
                        }
                        (boundary_solutions if failures else witnesses).append(record)
                        d_row["f_rows"].append(f_row)
                    d_row["status"] = "CHECKED"
                    lane_row["d_rows"].append(d_row)
                lane_row["status"] = "CHECKED"
                point_row["lanes"].append(lane_row)
        point_row["status"] = "CHECKED"
        rows.append(point_row)

    return {
        "epsilon": signs,
        "xi_index": xi_index,
        "pairing_index": pairing_index,
        "matching": [list(value) for value in matching],
        "status": "COMPLETE" if not unresolved else "INCOMPLETE",
        "point_count": len(rows),
        "rows": rows,
        "boundary_solutions": boundary_solutions,
        "witnesses": witnesses,
        "unresolved": unresolved,
        "case_excluded": not witnesses and not unresolved,
    }


@app.local_entrypoint()
def main(all_cases: bool = False):
    signs = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    cases = tuple((*epsilon, xi_index, pairing_index)
                  for epsilon in signs
                  for xi_index in (0, 2)
                  for pairing_index in (1, 2))
    if not all_cases:
        cases = (cases[0],)
    raw = list(solve_case.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        rows.append({
            "epsilon": list(case[:2]),
            "xi_index": case[2],
            "pairing_index": case[3],
            "status": "REMOTE_ERROR",
            "error": repr(row),
        } if isinstance(row, BaseException) else row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell3-de-pairings12-direct-solver-v1",
        "scope": (
            "Exact direct target solve for xi in {0,2}, pairings in {1,2}; "
            "xi=1 transport and all other cases are outside scope."
        ),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "source_replay0_sha256": hashlib.sha256(REPLAY0.read_bytes()).hexdigest(),
        "source_replay2_sha256": hashlib.sha256(REPLAY2.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [{
            "epsilon": row.get("epsilon"),
            "xi_index": row.get("xi_index"),
            "pairing_index": row.get("pairing_index"),
            "status": row.get("status"),
            "point_count": row.get("point_count"),
            "boundary_solution_count": len(row.get("boundary_solutions", [])),
            "witness_count": len(row.get("witnesses", [])),
            "unresolved": row.get("unresolved"),
            "case_excluded": row.get("case_excluded"),
            "error": row.get("error"),
        } for row in rows],
    }, sort_keys=True))
