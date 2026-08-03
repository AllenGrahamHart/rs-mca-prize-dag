#!/usr/bin/env python3
"""Solve every cell-3 xi5 pairing on the exact compatible source points."""

import hashlib
import json
from pathlib import Path
import time

import modal


DIRECTORY = Path(__file__).parent
SOURCE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell3_xi5_xi6_"
    "endpoint_compatibility_census_result.json"
)
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell3_compact_kernel_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell3_xi5_"
    "finite_source_pairing_solver_pilot_result.json"
)
CENSUS_RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell3_xi5_"
    "finite_source_pairing_solver_census_result.json"
)
REMOTE_SOURCE = "/root/source.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell3-xi5-finite-source-pairing")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0", "python-flint==0.8.0")
    .add_local_file(SOURCE, REMOTE_SOURCE)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


def canonical_matchings(items):
    if not items:
        return ((),)
    output = []
    for index in range(1, len(items)):
        for tail in canonical_matchings(items[1:index]+items[index+1:]):
            output.append(((items[0], items[index]),)+tail)
    return tuple(output)


@app.function(image=image, cpu=2.0, memory=4096, timeout=600, max_containers=24)
def solve_source(case):
    import sympy as sp
    from flint import fmpz_mod_mpoly_ctx, fmpz_mod_poly_ctx

    started = time.perf_counter()
    epsilon_1, epsilon_2, point_index = case
    source_payload = json.loads(Path(REMOTE_SOURCE).read_text())
    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    source_row = next(
        row for row in source_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
        and row["xi_index"] == 5
    )
    compatible = source_row["direct_lift"]["compatible_source_points"]
    if point_index not in range(len(compatible)):
        raise ValueError("point index outside the compatible-source ledger")
    source = compatible[point_index]
    r_value, t_value, b_value, c_value = source["point"]
    m_value = source["source_missing"]
    s_value = source["source_sum"]
    f_value = source["signed_other"]
    if (
        b_value*f_value % PRIME != m_value
        or pow(b_value+f_value, 2, PRIME) != s_value
    ):
        raise ValueError("xi5 endpoint reconstruction failed")

    kernel_row = next(
        row for row in kernel_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    )
    c_symbol, b_symbol, t_symbol, r_symbol = sp.symbols("c b t r")

    def evaluate_expression(text):
        output = 0
        for exponents, coefficient in sp.Poly(
            sp.sympify(text), c_symbol, b_symbol, t_symbol, r_symbol,
            modulus=PRIME,
        ).terms():
            term = int(coefficient) % PRIME
            for value, exponent in zip(
                (c_value, b_value, t_value, r_value), exponents
            ):
                term = term*pow(value, exponent, PRIME) % PRIME
            output = (output+term) % PRIME
        return output

    kernel_values = [
        evaluate_expression(item["expression"])
        for item in kernel_row["kernel"]
    ]
    a_values = kernel_values[:3]
    b_values = kernel_values[3:6]

    context = fmpz_mod_mpoly_ctx.get(["u", "v"], PRIME)
    u_variable = context.from_dict({(1, 0): 1})
    v_variable = context.from_dict({(0, 1): 1})

    def constant(value):
        return context.from_dict({(0, 0): value % PRIME})

    def paired(left, right):
        p0, p1, p2 = (
            constant(b_coefficient)-left*a_coefficient
            for a_coefficient, b_coefficient in zip(a_values, b_values)
        )
        q0 = constant(b_values[0])-right*a_values[0]
        q1 = constant(-b_values[1])+right*a_values[1]
        q2 = constant(b_values[2])-right*a_values[2]
        return (p2*q0-p0*q2)**2-(p2*q1-p1*q2)*(p1*q0-p0*q1)

    polynomial_context = fmpz_mod_poly_ctx(PRIME)
    univariate_variable = polynomial_context([0, 1])

    def univariate(polynomial, free_index, assignments=None):
        assignments = assignments or {}
        coefficients = {}
        for exponents, coefficient in polynomial.to_dict().items():
            scalar = int(coefficient) % PRIME
            for index, value in assignments.items():
                scalar = scalar*pow(value, exponents[index], PRIME) % PRIME
            degree = exponents[free_index]
            if any(
                exponent and index != free_index and index not in assignments
                for index, exponent in enumerate(exponents)
            ):
                raise ValueError("incomplete polynomial specialization")
            coefficients[degree] = (
                coefficients.get(degree, 0)+scalar
            ) % PRIME
        return polynomial_context([
            coefficients.get(degree, 0)
            for degree in range(max(coefficients, default=0)+1)
        ])

    def field_roots(polynomial):
        if polynomial.is_zero():
            return None
        if polynomial.degree() == 0:
            return []
        field_part = polynomial.gcd(
            pow(univariate_variable, PRIME, polynomial)-univariate_variable
        )
        _, factors = field_part.factor()
        roots = []
        for factor, _ in factors:
            if factor.degree() != 1:
                raise ValueError("field-root gcd contains a nonlinear factor")
            roots.append(
                -int(factor[0])*pow(int(factor[1]), -1, PRIME) % PRIME
            )
        return sorted(roots)

    def profile(polynomial):
        if not polynomial:
            return {"zero": True, "terms": 0, "degrees": None, "sha256": None}
        text = polynomial.str()
        return {
            "zero": False,
            "terms": len(polynomial.to_dict()),
            "degrees": [int(value) for value in polynomial.degrees()],
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
        }

    def evaluate_polynomial(polynomial, u_value, v_value):
        return sum(
            int(coefficient)
            * pow(u_value, exponents[0], PRIME)
            * pow(v_value, exponents[1], PRIME)
            for exponents, coefficient in polynomial.to_dict().items()
        ) % PRIME

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

    inverse_f = pow(f_value, -1, PRIME)
    q_record = (inverse_f*inverse_f % PRIME)*u_variable*v_variable
    matchings = canonical_matchings(tuple(range(6)))
    if len(matchings) != 15:
        raise ValueError("canonical matching count")

    lane_rows = []
    witnesses = []
    boundaries = []
    unresolved = []
    total_u_roots = 0
    total_v_roots = 0
    for sigma_c in (-1, 1):
        for sigma_o in (-1, 1):
            records = (
                q_record, q_record, -q_record, u_variable,
                sigma_o*v_variable, constant(sigma_c*c_value*f_value),
            )
            pairing_rows = []
            for pairing_index, matching in enumerate(matchings):
                equations = [
                    paired(records[left], records[right])
                    for left, right in matching
                ]
                resultant_rows = []
                candidates = []
                for left in range(3):
                    for right in range(left+1, 3):
                        resultant = equations[left].resultant(
                            equations[right], "v"
                        )
                        current_profile = profile(resultant)
                        resultant_rows.append({
                            "equations": [left, right],
                            **current_profile,
                        })
                        if not resultant:
                            continue
                        if int(resultant.degrees()[1]) != 0:
                            raise ValueError("v survived resultant")
                        candidates.append((
                            int(resultant.degrees()[0]),
                            len(resultant.to_dict()), left, right, resultant,
                        ))
                pairing_row = {
                    "pairing_index": pairing_index,
                    "matching": [list(value) for value in matching],
                    "equation_profiles": [profile(value) for value in equations],
                    "resultant_profiles": resultant_rows,
                    "fiber_rows": [],
                }
                if not candidates:
                    pairing_row["status"] = "ZERO_PAIRWISE_RESULTANTS"
                    unresolved.append({
                        "sigma": [sigma_c, sigma_o],
                        "pairing_index": pairing_index,
                        "reason": pairing_row["status"],
                    })
                    pairing_rows.append(pairing_row)
                    continue
                _, _, selected_left, selected_right, selected = min(candidates)
                selected_univariate = univariate(selected, 0)
                u_roots = field_roots(selected_univariate)
                if u_roots is None:
                    raise ValueError("nonzero selected resultant became zero")
                total_u_roots += len(u_roots)
                pairing_row.update({
                    "selected_equations": [selected_left, selected_right],
                    "selected_resultant_degree": int(selected_univariate.degree()),
                    "u_roots": u_roots,
                })
                for u_value in u_roots:
                    specialized = [
                        univariate(value, 1, {0: u_value})
                        for value in equations
                    ]
                    nonzero = [value for value in specialized if not value.is_zero()]
                    fiber_row = {
                        "u": u_value,
                        "specialized_degrees": [
                            None if value.is_zero() else int(value.degree())
                            for value in specialized
                        ],
                        "solutions": [],
                    }
                    if not nonzero:
                        fiber_row["status"] = "FREE_V"
                        unresolved.append({
                            "sigma": [sigma_c, sigma_o],
                            "pairing_index": pairing_index,
                            "u": u_value,
                            "reason": "FREE_V",
                        })
                        pairing_row["fiber_rows"].append(fiber_row)
                        continue
                    common = nonzero[0]
                    for value in nonzero[1:]:
                        common = common.gcd(value)
                    v_roots = field_roots(common)
                    if v_roots is None:
                        raise ValueError("nonzero fiber gcd became zero")
                    total_v_roots += len(v_roots)
                    fiber_row.update({
                        "common_v_degree": int(common.degree()),
                        "v_roots": v_roots,
                    })
                    for v_value in v_roots:
                        equation_values = [
                            evaluate_polynomial(value, u_value, v_value)
                            for value in equations
                        ]
                        if any(equation_values):
                            raise ValueError("fiber root violates original equation")
                        d_value = u_value*inverse_f % PRIME
                        e_value = v_value*inverse_f % PRIME
                        representatives = (
                            1, b_value, c_value, d_value, e_value, f_value
                        )
                        failed_guards = target_guards(representatives)
                        solution = {
                            "u": u_value,
                            "v": v_value,
                            "d": d_value,
                            "e": e_value,
                            "equation_values": equation_values,
                            "target_representatives": list(representatives),
                            "failed_guards": failed_guards,
                            "status": "TARGET_BOUNDARY" if failed_guards else "WITNESS",
                        }
                        record = {
                            "sigma": [sigma_c, sigma_o],
                            "pairing_index": pairing_index,
                            **solution,
                        }
                        (boundaries if failed_guards else witnesses).append(record)
                        fiber_row["solutions"].append(solution)
                    fiber_row["status"] = "CHECKED"
                    pairing_row["fiber_rows"].append(fiber_row)
                pairing_row["status"] = "CHECKED"
                pairing_rows.append(pairing_row)
            lane_rows.append({
                "sigma": [sigma_c, sigma_o],
                "pairing_rows": pairing_rows,
            })

    output = {
        "epsilon": [epsilon_1, epsilon_2],
        "point_index": point_index,
        "source": source,
        "status": "COMPLETE",
        "lane_rows": lane_rows,
        "u_root_count": total_u_roots,
        "v_root_count": total_v_roots,
        "boundary_count": len(boundaries),
        "boundaries": boundaries,
        "witness_count": len(witnesses),
        "witnesses": witnesses,
        "unresolved_count": len(unresolved),
        "unresolved": unresolved,
        "source_excluded": not witnesses and not unresolved,
        "seconds": time.perf_counter()-started,
    }
    print(json.dumps({
        "epsilon": output["epsilon"],
        "point_index": point_index,
        "u_roots": total_u_roots,
        "v_roots": total_v_roots,
        "boundaries": len(boundaries),
        "witnesses": len(witnesses),
        "unresolved": len(unresolved),
        "source_excluded": output["source_excluded"],
        "seconds": output["seconds"],
    }), flush=True)
    return output


@app.local_entrypoint()
def main(
    signs: str = "-1:-1",
    point_index: int = 0,
    source_census: bool = False,
):
    sign_pairs = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    if source_census:
        cases = tuple(
            (*epsilon, selected_point)
            for epsilon in sign_pairs
            for selected_point in range(6)
        )
    else:
        epsilon = tuple(int(value) for value in signs.split(":"))
        cases = ((*epsilon, point_index),)
    raw = list(solve_source.map(
        cases, order_outputs=True, return_exceptions=True
    ))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]),
                "point_index": case[2],
                "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-cell3-xi5-finite-source-"
            "pairing-census-v1" if source_census else
            "rate-half-kb-positive-433-1b-cell3-xi5-finite-source-"
            "pairing-pilot-v1"
        ),
        "scope": (
            "Exact finite-source solver for every canonical matching and "
            "target lane at the printed xi=5 compatible sources; no claim "
            "beyond the printed source rows."
        ),
        "source_census_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "rows": rows,
    }
    output_path = CENSUS_RESULT if source_census else RESULT
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(output_path),
        "rows": [{
            "epsilon": row.get("epsilon"),
            "point_index": row.get("point_index"),
            "status": row.get("status"),
            "error": row.get("error"),
            "u_roots": row.get("u_root_count"),
            "v_roots": row.get("v_root_count"),
            "boundaries": row.get("boundary_count"),
            "witnesses": row.get("witness_count"),
            "unresolved": row.get("unresolved_count"),
            "source_excluded": row.get("source_excluded"),
            "seconds": row.get("seconds"),
        } for row in rows],
    }, sort_keys=True))
