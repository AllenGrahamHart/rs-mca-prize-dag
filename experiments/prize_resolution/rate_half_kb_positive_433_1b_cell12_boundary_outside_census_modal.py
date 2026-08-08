#!/usr/bin/env python3
"""Census all outside systems on the eight rational cell-12 boundary points."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_compact_kernel_result.json"
)
BOUNDARY = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_tower_boundary_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_boundary_outside_census_result.json"
)
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell12-boundary-outside-census")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        second = values[index]
        rest = values[1:index] + values[index + 1:]
        for tail in pairings(rest):
            yield ((first, second),) + tail


MATCHINGS = tuple(pairings(range(6)))


@app.function(image=image, cpu=2.0, memory=4096, timeout=300, max_containers=32)
def census(case):
    import sympy as sp

    point_index, signs, point, sigma_c, sigma_o = case
    y = sp.symbols("y")
    inverse_two = pow(2, -1, PRIME)
    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    kernel_expressions = [
        sp.sympify(item["expression"])
        for item in kernel_payload["rows"][0]["kernel"]
    ]
    t, r, c, b = sp.symbols("t r c b")
    values = {t: point["t"], r: point["r"],
              c: point["c"], b: point["b"]}
    kernel = [int(expression.subs(values)) % PRIME
              for expression in kernel_expressions]
    a_coefficients = kernel[:3]
    b_coefficients = kernel[3:6]
    beta_0, beta_1 = kernel[6:]
    missing_label = -point["t"] * point["t"] % PRIME

    def evaluate(coefficients, value):
        return sum(coefficient * pow(value, index, PRIME)
                   for index, coefficient in enumerate(coefficients)) % PRIME

    a_missing = evaluate(a_coefficients, missing_label)
    b_missing = evaluate(b_coefficients, missing_label)
    if a_missing == 0:
        return {
            "point_index": point_index, "epsilon": list(signs),
            "sigma": [sigma_c, sigma_o], "status": "INCOMPLETE",
            "reason": "ZERO_MISSING_DENOMINATOR",
        }
    missing = b_missing * pow(a_missing, -1, PRIME) % PRIME
    source_sum = (
        missing_label
        * pow((beta_0 + beta_1 * missing_label) % PRIME, 2, PRIME)
        * pow(a_missing, -2, PRIME)
    ) % PRIME

    def paired(left, right):
        p0, p1, p2 = (
            sp.expand(b_value - left * a_value)
            for a_value, b_value in zip(a_coefficients, b_coefficients)
        )
        q0 = sp.expand(b_coefficients[0] - right * a_coefficients[0])
        q1 = sp.expand(-b_coefficients[1] + right * a_coefficients[1])
        q2 = sp.expand(b_coefficients[2] - right * a_coefficients[2])
        return sp.Poly(
            (p2*q0 - p0*q2)**2
            - (p2*q1 - p1*q2)*(p1*q0 - p0*q1),
            y, modulus=PRIME,
        )

    def roots(polynomial):
        if polynomial.is_zero:
            return None
        _, factors = sp.factor_list(
            polynomial.as_expr(), y, modulus=PRIME
        )
        output = []
        for factor, _ in factors:
            value = sp.Poly(factor, y, modulus=PRIME)
            if value.degree() != 1:
                continue
            leading, constant = (
                int(coefficient) % PRIME for coefficient in value.all_coeffs()
            )
            output.append(-constant * pow(leading, -1, PRIME) % PRIME)
        return sorted(set(output))

    square_roots = sorted(sp.sqrt_mod(source_sum, PRIME, all_roots=True))
    discriminant_roots = sorted(sp.sqrt_mod(
        (source_sum - 4*missing) % PRIME, PRIME, all_roots=True
    ))

    def missing_lifts(xi_index):
        lifts = []
        if xi_index in (0, 1):
            for sum_root in square_roots:
                for delta in discriminant_roots:
                    d_value = (sum_root + delta) * inverse_two % PRIME
                    e_value = (sum_root - delta) * inverse_two % PRIME
                    lifts.append((d_value, e_value, y))
        elif xi_index == 2:
            for difference_root in square_roots:
                for delta in discriminant_roots:
                    e_value = (-difference_root + delta) * inverse_two % PRIME
                    d_value = e_value + difference_root
                    lifts.append((d_value % PRIME, e_value, y))
        elif xi_index == 3:
            for sum_root in square_roots:
                for delta in discriminant_roots:
                    d_value = (sum_root + delta) * inverse_two % PRIME
                    f_value = (sum_root - delta) * inverse_two % PRIME
                    lifts.append((d_value, y, f_value))
        elif xi_index == 4:
            for sum_root in square_roots:
                for delta in discriminant_roots:
                    e_value = (sum_root + delta) * inverse_two % PRIME
                    signed_f = (sum_root - delta) * inverse_two % PRIME
                    lifts.append((y, e_value, sigma_o * signed_f % PRIME))
        elif xi_index == 5:
            endpoint = point["b"]
            compatibility = (
                pow((endpoint*endpoint + missing) % PRIME, 2, PRIME)
                - source_sum*endpoint*endpoint
            ) % PRIME
            if compatibility == 0:
                return None
        elif xi_index == 6:
            endpoint = point["c"]
            compatibility = (
                pow((endpoint*endpoint + missing) % PRIME, 2, PRIME)
                - source_sum*endpoint*endpoint
            ) % PRIME
            if compatibility == 0:
                return None
        return sorted(set(lifts), key=str)

    def outside_records(d_value, e_value, f_value):
        return (
            d_value*e_value,
            d_value*e_value,
            -d_value*e_value,
            d_value*f_value,
            sigma_o*e_value*f_value,
            point["b"]*f_value,
            sigma_c*point["c"]*f_value,
        )

    def target_guard_failures(d_value, e_value, f_value):
        representatives = (
            1, point["b"], point["c"],
            d_value, e_value, f_value,
        )
        failures = []
        for index, value in enumerate(representatives):
            if value % PRIME == 0:
                failures.append(f"nonzero_{index}")
        for left in range(6):
            for right in range(left + 1, 6):
                if (representatives[left] - representatives[right]) % PRIME == 0:
                    failures.append(f"difference_{left}_{right}")
                if (representatives[left] + representatives[right]) % PRIME == 0:
                    failures.append(f"sum_{left}_{right}")
        return failures

    rows = []
    witnesses = []
    unresolved = []
    for xi_index in range(7):
        residual_indices = tuple(index for index in range(7) if index != xi_index)
        lifts = missing_lifts(xi_index)
        for pairing_index, matching in enumerate(MATCHINGS):
            row = {
                "xi_index": xi_index,
                "pairing_index": pairing_index,
                "missing_lifts": None if lifts is None else len(lifts),
                "free_root_candidates": 0,
                "target_boundaries": 0,
                "witnesses": 0,
                "unresolved": False,
            }
            if lifts is None:
                row["unresolved"] = True
                unresolved.append({
                    "xi_index": xi_index,
                    "pairing_index": pairing_index,
                    "reason": "TWO_FREE_MISSING_ENDPOINT",
                })
                rows.append(row)
                continue
            for d_value, e_value, f_value in lifts:
                records = outside_records(d_value, e_value, f_value)
                residual = tuple(records[index] for index in residual_indices)
                equations = [
                    paired(residual[left], residual[right])
                    for left, right in matching
                ]
                nonzero = next((value for value in equations
                                if not value.is_zero), None)
                if nonzero is None:
                    row["unresolved"] = True
                    unresolved.append({
                        "xi_index": xi_index,
                        "pairing_index": pairing_index,
                        "reason": "FREE_TARGET_PARAMETER",
                        "lift": [str(d_value), str(e_value), str(f_value)],
                    })
                    continue
                candidates = roots(nonzero)
                row["free_root_candidates"] += len(candidates)
                for free_value in candidates:
                    substitutions = {y: free_value}
                    if any(int(value.as_expr().subs(substitutions)) % PRIME
                           for value in equations):
                        continue
                    target_values = tuple(
                        int(value.subs(substitutions)) % PRIME
                        if isinstance(value, sp.Basic) else int(value) % PRIME
                        for value in (d_value, e_value, f_value)
                    )
                    failures = target_guard_failures(*target_values)
                    if failures:
                        row["target_boundaries"] += 1
                        continue
                    row["witnesses"] += 1
                    witness = {
                        "xi_index": xi_index,
                        "pairing_index": pairing_index,
                        "d": target_values[0], "e": target_values[1],
                        "f": target_values[2],
                    }
                    witnesses.append(witness)
            rows.append(row)

    valid = len(rows) == 105
    return {
        "point_index": point_index,
        "epsilon": list(signs),
        "point": {key: point[key] for key in ("r", "t", "b", "c")},
        "sigma": [sigma_c, sigma_o],
        "status": "COMPLETE" if valid and not unresolved else "INCOMPLETE",
        "missing": missing,
        "source_sum": source_sum,
        "square_root_count": len(square_roots),
        "discriminant_root_count": len(discriminant_roots),
        "rows": rows,
        "witnesses": witnesses,
        "unresolved": unresolved,
    }


@app.local_entrypoint()
def main():
    boundary = json.loads(BOUNDARY.read_text())
    points = []
    for row in boundary["rows"]:
        for point in row["rational_points"]:
            points.append((tuple(row["epsilon"]), point))
    cases = tuple(
        (point_index, signs, point, sigma_c, sigma_o)
        for point_index, (signs, point) in enumerate(points)
        for sigma_c in (-1, 1) for sigma_o in (-1, 1)
    )
    raw = list(census.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "point_index": case[0], "epsilon": list(case[1]),
                "sigma": list(case[3:]), "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell12-boundary-outside-census-v1",
        "field": PRIME,
        "scope": (
            "Exact all-label outside census on the eight rational leading-"
            "boundary points of cell 12; no generic-curve or cell claim."
        ),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "source_boundary_sha256": hashlib.sha256(BOUNDARY.read_bytes()).hexdigest(),
        "expected_cases": len(cases),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "cases": len(rows),
        "complete": sum(row.get("status") == "COMPLETE" for row in rows),
        "labels": sum(len(row.get("rows", [])) for row in rows),
        "witnesses": sum(len(row.get("witnesses", [])) for row in rows),
        "unresolved": sum(len(row.get("unresolved", [])) for row in rows),
    }, sort_keys=True))
