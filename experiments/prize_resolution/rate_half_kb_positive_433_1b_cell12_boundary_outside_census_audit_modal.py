#!/usr/bin/env python3
"""Independent gcd/Frobenius audit of the cell-12 boundary census."""

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
PRIMARY = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_boundary_outside_census_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_boundary_outside_census_audit_result.json"
)
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell12-boundary-outside-audit")
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


@app.function(image=image, cpu=1.0, memory=2048, timeout=180, max_containers=16)
def audit(case):
    import sympy as sp

    point_index, signs, point, sigma_c, sigma_o = case
    y = sp.symbols("y")
    t, r, c, b = sp.symbols("t r c b")
    inverse_two = pow(2, -1, PRIME)

    def modular_square_roots(value):
        value %= PRIME
        if value == 0:
            return [0]
        if pow(value, (PRIME - 1) // 2, PRIME) != 1:
            return []
        q = PRIME - 1
        s = 0
        while q % 2 == 0:
            s += 1
            q //= 2
        if s == 1:
            root = pow(value, (PRIME + 1) // 4, PRIME)
            return sorted({root, -root % PRIME})
        nonresidue = 2
        while pow(nonresidue, (PRIME - 1) // 2, PRIME) != PRIME - 1:
            nonresidue += 1
        c_value = pow(nonresidue, q, PRIME)
        x_value = pow(value, (q + 1) // 2, PRIME)
        t_value = pow(value, q, PRIME)
        m_value = s
        while t_value != 1:
            index = 1
            square = t_value * t_value % PRIME
            while square != 1:
                square = square * square % PRIME
                index += 1
            factor = pow(c_value, 1 << (m_value - index - 1), PRIME)
            x_value = x_value * factor % PRIME
            c_value = factor * factor % PRIME
            t_value = t_value * c_value % PRIME
            m_value = index
        return sorted({x_value, -x_value % PRIME})

    def polynomial(expression):
        return sp.Poly(expression, y, modulus=PRIME)

    def power_mod(base, exponent, modulus):
        value = polynomial(1)
        base = sp.rem(base, modulus)
        while exponent:
            if exponent & 1:
                value = sp.rem(value * base, modulus)
            exponent >>= 1
            if exponent:
                base = sp.rem(base * base, modulus)
        return value

    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    expressions = [
        sp.sympify(item["expression"])
        for item in kernel_payload["rows"][0]["kernel"]
    ]
    substitutions = {t: point["t"], r: point["r"],
                     c: point["c"], b: point["b"]}
    kernel = [int(expression.subs(substitutions)) % PRIME
              for expression in expressions]
    a_coefficients = kernel[:3]
    b_coefficients = kernel[3:6]
    beta_0, beta_1 = kernel[6:]
    label = -point["t"] * point["t"] % PRIME

    def evaluate(coefficients, value):
        return sum(coefficient * pow(value, index, PRIME)
                   for index, coefficient in enumerate(coefficients)) % PRIME

    a_value = evaluate(a_coefficients, label)
    if a_value == 0:
        return {"point_index": point_index, "sigma": [sigma_c, sigma_o],
                "status": "INCOMPLETE", "reason": "ZERO_DENOMINATOR"}
    missing = evaluate(b_coefficients, label) * pow(a_value, -1, PRIME) % PRIME
    source_sum = (
        label * pow((beta_0 + beta_1*label) % PRIME, 2, PRIME)
        * pow(a_value, -2, PRIME)
    ) % PRIME

    sum_roots = modular_square_roots(source_sum)
    delta_roots = modular_square_roots(source_sum - 4*missing)

    def paired(left, right):
        p0, p1, p2 = (
            b_value - left*a_coefficient
            for a_coefficient, b_value in zip(a_coefficients, b_coefficients)
        )
        q0 = b_coefficients[0] - right*a_coefficients[0]
        q1 = -b_coefficients[1] + right*a_coefficients[1]
        q2 = b_coefficients[2] - right*a_coefficients[2]
        return polynomial(
            (p2*q0 - p0*q2)**2
            - (p2*q1 - p1*q2)*(p1*q0 - p0*q1)
        )

    def lifts(xi_index):
        output = []
        if xi_index in (0, 1):
            for total in sum_roots:
                for delta in delta_roots:
                    output.append(((total+delta)*inverse_two % PRIME,
                                   (total-delta)*inverse_two % PRIME, y))
        elif xi_index == 2:
            for difference in sum_roots:
                for delta in delta_roots:
                    e_value = (-difference+delta)*inverse_two % PRIME
                    output.append(((e_value+difference) % PRIME, e_value, y))
        elif xi_index == 3:
            for total in sum_roots:
                for delta in delta_roots:
                    output.append(((total+delta)*inverse_two % PRIME, y,
                                   (total-delta)*inverse_two % PRIME))
        elif xi_index == 4:
            for total in sum_roots:
                for delta in delta_roots:
                    output.append((y, (total+delta)*inverse_two % PRIME,
                                   sigma_o*(total-delta)*inverse_two % PRIME))
        return sorted(set(output), key=str)

    def records(d_value, e_value, f_value):
        return (
            d_value*e_value, d_value*e_value, -d_value*e_value,
            d_value*f_value, sigma_o*e_value*f_value,
            point["b"]*f_value, sigma_c*point["c"]*f_value,
        )

    def sums(d_value, e_value, f_value):
        return (
            (d_value+e_value)**2, (d_value+e_value)**2,
            (d_value-e_value)**2, (d_value+f_value)**2,
            (e_value+sigma_o*f_value)**2, (point["b"]+f_value)**2,
            (point["c"]+sigma_c*f_value)**2,
        )

    def target_guard(d_value, e_value, f_value):
        representatives = (1, point["b"], point["c"],
                           d_value, e_value, f_value)
        guard = polynomial(1)
        for value in representatives:
            guard *= polynomial(value)
        for left in range(6):
            for right in range(left + 1, 6):
                guard *= polynomial(representatives[left]-representatives[right])
                guard *= polynomial(representatives[left]+representatives[right])
        return guard

    rows = []
    free_branches = []
    for xi_index in range(7):
        residual_indices = tuple(index for index in range(7) if index != xi_index)
        if xi_index in (5, 6):
            endpoint = point["b"] if xi_index == 5 else point["c"]
            compatibility = (
                pow((endpoint*endpoint + missing) % PRIME, 2, PRIME)
                - source_sum*endpoint*endpoint
            ) % PRIME
            if compatibility == 0:
                free_branches.append({"xi_index": xi_index,
                                      "reason": "ENDPOINT_COMPATIBLE"})
            for pairing_index in range(15):
                rows.append({"xi_index": xi_index,
                             "pairing_index": pairing_index,
                             "guarded_root_degree": (
                                 None if compatibility == 0 else 0
                             )})
            continue
        for pairing_index, matching in enumerate(MATCHINGS):
            guarded_degree = 0
            for d_value, e_value, f_value in lifts(xi_index):
                full_records = records(d_value, e_value, f_value)
                full_sums = sums(d_value, e_value, f_value)
                require_product = polynomial(full_records[xi_index] - missing)
                require_sum = polynomial(full_sums[xi_index] - source_sum)
                if not require_product.is_zero or not require_sum.is_zero:
                    raise RuntimeError("missing lift replay")
                residual = tuple(full_records[index] for index in residual_indices)
                equations = [
                    paired(residual[left], residual[right])
                    for left, right in matching
                ]
                nonzero = [value for value in equations if not value.is_zero]
                if not nonzero:
                    free_branches.append({
                        "xi_index": xi_index, "pairing_index": pairing_index,
                        "reason": "ZERO_EQUATION_GCD",
                    })
                    continue
                common = nonzero[0]
                for equation in nonzero[1:]:
                    common = sp.gcd(common, equation)
                common = common.monic()
                if common.degree() == 0:
                    continue
                frobenius = power_mod(polynomial(y), PRIME, common)
                deployed = sp.gcd(common, frobenius - polynomial(y)).monic()
                if deployed.degree() == 0:
                    continue
                guard = target_guard(d_value, e_value, f_value)
                boundary_part = sp.gcd(deployed, guard)
                guarded, remainder = sp.div(deployed, boundary_part)
                if not remainder.is_zero:
                    raise RuntimeError("target guard division")
                guarded_degree += max(0, guarded.degree())
            rows.append({
                "xi_index": xi_index,
                "pairing_index": pairing_index,
                "guarded_root_degree": guarded_degree,
            })

    return {
        "point_index": point_index, "epsilon": list(signs),
        "sigma": [sigma_c, sigma_o],
        "status": "COMPLETE" if not free_branches else "INCOMPLETE",
        "missing": missing, "source_sum": source_sum,
        "sum_roots": sum_roots, "delta_roots": delta_roots,
        "rows": rows, "free_branches": free_branches,
    }


@app.local_entrypoint()
def main():
    boundary = json.loads(BOUNDARY.read_text())
    primary = json.loads(PRIMARY.read_text())
    points = []
    for row in boundary["rows"]:
        for point in row["rational_points"]:
            points.append((tuple(row["epsilon"]), point))
    cases = tuple(
        (point_index, signs, point, sigma_c, sigma_o)
        for point_index, (signs, point) in enumerate(points)
        for sigma_c in (-1, 1) for sigma_o in (-1, 1)
    )
    raw = list(audit.map(cases, order_outputs=True, return_exceptions=True))
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
    primary_keys = {
        (row["point_index"], *row["sigma"])
        for row in primary["rows"] if row["status"] == "COMPLETE"
    }
    audit_keys = {
        (row["point_index"], *row["sigma"])
        for row in rows if row["status"] == "COMPLETE"
    }
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell12-boundary-outside-audit-v1",
        "field": PRIME,
        "scope": (
            "Independent Frobenius-gcd and target-guard audit of every "
            "deployed root in the cell-12 rational-boundary census."
        ),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "source_boundary_sha256": hashlib.sha256(BOUNDARY.read_bytes()).hexdigest(),
        "source_primary_sha256": hashlib.sha256(PRIMARY.read_bytes()).hexdigest(),
        "coverage_agrees": primary_keys == audit_keys == {
            (case[0], case[3], case[4]) for case in cases
        },
        "expected_cases": len(cases),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT), "cases": len(rows),
        "complete": sum(row.get("status") == "COMPLETE" for row in rows),
        "labels": sum(len(row.get("rows", [])) for row in rows),
        "guarded_root_degree": sum(
            item.get("guarded_root_degree") or 0
            for row in rows for item in row.get("rows", [])
        ),
        "free_branches": sum(len(row.get("free_branches", [])) for row in rows),
        "coverage_agrees": output["coverage_agrees"],
    }, sort_keys=True))
