#!/usr/bin/env python3
"""Independent deployed-field audit of the cell-12 endpoint systems."""

import hashlib
import itertools
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
REPLAY = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_endpoint_compatibility_replay_result.json"
)
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_compact_kernel_result.json"
)
PRIMARY = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_endpoint_residual_census_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_endpoint_residual_audit_result.json"
)
REMOTE_REPLAY = "/root/replay.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell12-endpoint-residual-audit")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(REPLAY, REMOTE_REPLAY)
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
def audit(case):
    import sympy as sp

    epsilon_1, epsilon_2, endpoint, sigma_c, sigma_o = case
    d, e = sp.symbols("d e")

    def roots(expression, variable):
        polynomial = sp.Poly(expression, variable, modulus=PRIME)
        if polynomial.is_zero:
            return None
        _, factors = sp.factor_list(
            polynomial.as_expr(), variable, modulus=PRIME
        )
        output = []
        for factor, _ in factors:
            row = sp.Poly(factor, variable, modulus=PRIME)
            if row.degree() != 1:
                continue
            leading, constant = (
                int(coefficient) % PRIME for coefficient in row.all_coeffs()
            )
            output.append(-constant*pow(leading, -1, PRIME) % PRIME)
        return sorted(set(output))

    replay = json.loads(Path(REMOTE_REPLAY).read_text())
    source_row = next(row for row in replay["rows"]
                      if row["epsilon"] == [epsilon_1, epsilon_2]
                      and row["endpoint"] == endpoint)
    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    kernel_expressions = [
        sp.sympify(item["expression"])
        for item in kernel_payload["rows"][0]["kernel"]
    ]
    t, r, c, b = sp.symbols("t r c b")
    xi_index = 5 if endpoint == "b" else 6
    systems = 0
    unit_unrestricted = 0
    finite_unrestricted = 0
    no_deployed_root = 0
    target_boundary = 0
    witnesses = []
    unresolved = []
    for point_index, point in enumerate(source_row["generic_points"]):
        substitutions = {t: point["t"], r: point["r"],
                         b: point["b"], c: point["c"]}
        kernel = [int(value.subs(substitutions)) % PRIME
                  for value in kernel_expressions]
        a_coefficients = kernel[:3]
        b_coefficients = kernel[3:6]
        missing = point["missing"]
        f_value = (
            missing*pow(point["b"], -1, PRIME) % PRIME
            if endpoint == "b"
            else sigma_c*missing*pow(point["c"], -1, PRIME) % PRIME
        )

        def paired(left, right):
            p0, p1, p2 = (
                b_value-left*a_value
                for a_value, b_value in zip(a_coefficients, b_coefficients)
            )
            q0 = b_coefficients[0]-right*a_coefficients[0]
            q1 = -b_coefficients[1]+right*a_coefficients[1]
            q2 = b_coefficients[2]-right*a_coefficients[2]
            return sp.Poly(
                (p2*q0-p0*q2)**2-(p2*q1-p1*q2)*(p1*q0-p0*q1),
                d, e, modulus=PRIME,
            )

        records = (
            d*e, d*e, -d*e, d*f_value, sigma_o*e*f_value,
            point["b"]*f_value, sigma_c*point["c"]*f_value,
        )
        residual = tuple(records[index] for index in range(7)
                         if index != xi_index)
        for pairing_index, matching in enumerate(MATCHINGS):
            systems += 1
            equations = [
                paired(residual[left], residual[right])
                for left, right in matching
            ]
            basis = sp.groebner(
                [value.as_expr() for value in equations], d, e,
                modulus=PRIME, order="lex",
            )
            if len(basis.polys) == 1 and basis.polys[0].is_one:
                unit_unrestricted += 1
                continue
            univariate = [
                sp.Poly(value.as_expr(), e, modulus=PRIME)
                for value in basis.polys if value.degree(d) == 0
            ]
            if not univariate:
                unresolved.append({
                    "point_index": point_index,
                    "pairing_index": pairing_index,
                    "reason": "NO_E_ELIMINANT",
                })
                continue
            finite_unrestricted += 1
            e_polynomial = univariate[0]
            for value in univariate[1:]:
                e_polynomial = sp.gcd(e_polynomial, value)
            e_roots = roots(e_polynomial.as_expr(), e)
            deployed = 0
            for e_value in e_roots or []:
                d_polynomials = [
                    sp.Poly(value.as_expr().subs(e, e_value), d, modulus=PRIME)
                    for value in equations
                    if not sp.Poly(value.as_expr().subs(e, e_value), d,
                                   modulus=PRIME).is_zero
                ]
                if not d_polynomials:
                    unresolved.append({
                        "point_index": point_index,
                        "pairing_index": pairing_index,
                        "reason": "FREE_D", "e": e_value,
                    })
                    continue
                d_polynomial = d_polynomials[0]
                for value in d_polynomials[1:]:
                    d_polynomial = sp.gcd(d_polynomial, value)
                for d_value in roots(d_polynomial.as_expr(), d) or []:
                    if any(int(value.as_expr().subs({d: d_value, e: e_value}))
                           % PRIME for value in equations):
                        continue
                    deployed += 1
                    representatives = (
                        1, point["b"], point["c"], d_value, e_value, f_value,
                    )
                    failures = []
                    for index, value in enumerate(representatives):
                        if value % PRIME == 0:
                            failures.append(f"nonzero_{index}")
                    for left, right in itertools.combinations(range(6), 2):
                        if (representatives[left]-representatives[right]) % PRIME == 0:
                            failures.append(f"difference_{left}_{right}")
                        if (representatives[left]+representatives[right]) % PRIME == 0:
                            failures.append(f"sum_{left}_{right}")
                    if failures:
                        target_boundary += 1
                    else:
                        witnesses.append({
                            "point_index": point_index,
                            "pairing_index": pairing_index,
                            "d": d_value, "e": e_value, "f": f_value,
                        })
            if deployed == 0:
                no_deployed_root += 1

    return {
        "epsilon": [epsilon_1, epsilon_2], "endpoint": endpoint,
        "sigma": [sigma_c, sigma_o],
        "status": "COMPLETE" if not unresolved else "INCOMPLETE",
        "source_points": len(source_row["generic_points"]),
        "systems": systems, "unit_unrestricted": unit_unrestricted,
        "finite_unrestricted": finite_unrestricted,
        "no_deployed_root": no_deployed_root,
        "target_boundary": target_boundary,
        "witnesses": witnesses, "unresolved": unresolved,
    }


@app.local_entrypoint()
def main(limit: int = 0):
    cases = tuple(
        (epsilon_1, epsilon_2, endpoint, sigma_c, sigma_o)
        for epsilon_1 in (-1, 1) for epsilon_2 in (-1, 1)
        for endpoint in ("b", "c")
        for sigma_c in (-1, 1) for sigma_o in (-1, 1)
    )
    if limit:
        cases = cases[:limit]
    raw = list(audit.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]), "endpoint": case[2],
                "sigma": list(case[3:]), "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
    primary = json.loads(PRIMARY.read_text())
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell12-endpoint-residual-audit-v1",
        "field": PRIME,
        "scope": (
            "Independent SymPy lex/root audit of every finite cell-12 "
            "endpoint residual system."
        ),
        "source_replay_sha256": hashlib.sha256(REPLAY.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "source_primary_sha256": hashlib.sha256(PRIMARY.read_bytes()).hexdigest(),
        "primary_complete": all(row["status"] == "COMPLETE"
                                for row in primary["rows"]),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT), "cases": len(rows),
        "complete": sum(row.get("status") == "COMPLETE" for row in rows),
        "systems": sum(row.get("systems", 0) for row in rows),
        "unit_unrestricted": sum(row.get("unit_unrestricted", 0) for row in rows),
        "finite_unrestricted": sum(row.get("finite_unrestricted", 0) for row in rows),
        "no_deployed_root": sum(row.get("no_deployed_root", 0) for row in rows),
        "target_boundary": sum(row.get("target_boundary", 0) for row in rows),
        "witnesses": sum(len(row.get("witnesses", [])) for row in rows),
        "unresolved": sum(len(row.get("unresolved", [])) for row in rows),
    }, sort_keys=True))
