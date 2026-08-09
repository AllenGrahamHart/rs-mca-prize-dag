#!/usr/bin/env python3
"""Independently audit the cell-9 first-pair residual systems."""

import hashlib
import itertools
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
REPLAY = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_parallel_de_four_basis_replay_result.json"
)
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_compact_kernel_result.json"
)
PRIMARY = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_parallel_de_first_pair_residual_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_parallel_de_first_pair_audit_result.json"
)
REMOTE_REPLAY = "/root/replay.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433
MATCHINGS = (
    ((0, 1), (2, 3), (4, 5)),
    ((0, 1), (2, 4), (3, 5)),
    ((0, 1), (2, 5), (3, 4)),
)

app = modal.App("rs-mca-positive-433-1b-cell9-parallel-de-audit")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(REPLAY, REMOTE_REPLAY)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=300, max_containers=16)
def audit(case):
    import sympy as sp

    epsilon_1, epsilon_2, sigma_c, sigma_o, cut_kind = case
    z, d, e, f = sp.symbols("z d e f")
    replay = json.loads(Path(REMOTE_REPLAY).read_text())
    source_row = next(
        row for row in replay["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
        and row["cut_kind"] == cut_kind
    )
    points = source_row["witnesses"]
    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    kernel_row = next(
        row for row in kernel_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    )
    kernel_expressions = [
        sp.sympify(item["expression"]) for item in kernel_row["kernel"]
    ]
    t, r, c, b = sp.symbols("t r c b")

    def roots(polynomial, variable):
        polynomial = sp.Poly(polynomial, variable, modulus=PRIME)
        if polynomial.is_zero:
            return None
        _, factors = sp.factor_list(polynomial.as_expr(), variable, modulus=PRIME)
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

    systems = 0
    unit_systems = 0
    finite_systems = 0
    no_deployed_root = 0
    witnesses = []
    unresolved = []
    for point_index, point in enumerate(points):
        substitutions = {
            t: point["t"], r: point["r"], b: point["b"], c: point["c"],
        }
        kernel = [int(value.subs(substitutions)) % PRIME
                  for value in kernel_expressions]
        a_coefficients, b_coefficients = kernel[:3], kernel[3:6]
        beta_0, beta_1 = kernel[6:]
        missing = point["missing"]
        label = -point["t"]*point["t"] % PRIME
        a_missing = sum(value*pow(label, index, PRIME)
                        for index, value in enumerate(a_coefficients)) % PRIME
        source_sum = (
            label*pow((beta_0+beta_1*label) % PRIME, 2, PRIME)
            * pow(a_missing, -2, PRIME)
        ) % PRIME

        def paired(left, right):
            p0, p1, p2 = (
                b_value-left*a_value
                for a_value, b_value in zip(a_coefficients, b_coefficients)
            )
            q0 = b_coefficients[0]-right*a_coefficients[0]
            q1 = -b_coefficients[1]+right*a_coefficients[1]
            q2 = b_coefficients[2]-right*a_coefficients[2]
            return sp.expand(
                (p2*q0-p0*q2)**2-(p2*q1-p1*q2)*(p1*q0-p0*q1)
            )

        records = (
            d*e, -d*e, d*f, sigma_o*e*f,
            point["b"]*f, sigma_c*point["c"]*f,
        )
        representatives = (1, point["b"], point["c"], d, e, f)
        guard = sp.Integer(1)
        for value in representatives:
            guard *= value
        for left, right in itertools.combinations(representatives, 2):
            guard *= (left-right)*(left+right)
        eta = 1 if cut_kind == "positive" else -1
        de_value = missing if cut_kind == "positive" else -missing % PRIME

        for pairing_index, matching in enumerate(MATCHINGS):
            systems += 1
            substitution = {e: sp.Rational(de_value, 1)/d}
            equations = []
            sum_numerator, _ = sp.fraction(sp.cancel(
                ((d+eta*e)**2-source_sum).subs(substitution)
            ))
            equations.append(sp.Poly(sum_numerator, d, f, modulus=PRIME))
            for left, right in matching[1:]:
                numerator, _ = sp.fraction(sp.cancel(
                    paired(records[left], records[right]).subs(substitution)
                ))
                equations.append(sp.Poly(numerator, d, f, modulus=PRIME))
            guard_numerator, _ = sp.fraction(sp.cancel(guard.subs(substitution)))
            guard_polynomial = sp.Poly(guard_numerator, d, f, modulus=PRIME)
            basis = sp.groebner(
                [item.as_expr() for item in equations]
                + [z*d*guard_polynomial.as_expr()-1],
                z, d, f, modulus=PRIME, order="lex",
            )
            if len(basis.polys) == 1 and basis.polys[0].is_one:
                unit_systems += 1
                continue
            eliminants = [
                sp.Poly(item.as_expr(), f, modulus=PRIME)
                for item in basis.polys
                if item.degree(z) == 0 and item.degree(d) == 0
            ]
            if not eliminants:
                unresolved.append({
                    "point_index": point_index,
                    "pairing_index": pairing_index,
                    "reason": "NO_F_ELIMINANT",
                })
                continue
            finite_systems += 1
            eliminant = eliminants[0]
            for item in eliminants[1:]:
                eliminant = sp.gcd(eliminant, item)
            deployed = 0
            for f_value in roots(eliminant.as_expr(), f) or []:
                d_polynomials = [
                    sp.Poly(item.as_expr().subs(f, f_value), d, modulus=PRIME)
                    for item in equations
                    if not sp.Poly(
                        item.as_expr().subs(f, f_value), d, modulus=PRIME
                    ).is_zero
                ]
                if not d_polynomials:
                    unresolved.append({
                        "point_index": point_index,
                        "pairing_index": pairing_index,
                        "reason": "FREE_D", "f": f_value,
                    })
                    continue
                d_polynomial = d_polynomials[0]
                for item in d_polynomials[1:]:
                    d_polynomial = sp.gcd(d_polynomial, item)
                for d_value in roots(d_polynomial.as_expr(), d) or []:
                    if d_value == 0:
                        continue
                    e_value = de_value*pow(d_value, -1, PRIME) % PRIME
                    if any(int(item.as_expr().subs({d: d_value, f: f_value}))
                           % PRIME for item in equations):
                        continue
                    if int(guard.subs({
                        d: d_value, e: e_value, f: f_value,
                    })) % PRIME == 0:
                        continue
                    deployed += 1
                    witnesses.append({
                        "point_index": point_index,
                        "pairing_index": pairing_index,
                        "d": d_value, "e": e_value, "f": f_value,
                    })
            if deployed == 0:
                no_deployed_root += 1

    return {
        "epsilon": [epsilon_1, epsilon_2],
        "sigma": [sigma_c, sigma_o], "cut_kind": cut_kind,
        "status": "COMPLETE" if not unresolved else "INCOMPLETE",
        "source_points": len(points), "systems": systems,
        "unit_systems": unit_systems, "finite_systems": finite_systems,
        "no_deployed_root": no_deployed_root,
        "witnesses": witnesses, "unresolved": unresolved,
    }


@app.local_entrypoint()
def main(limit: int = 0):
    cases = tuple(
        (*epsilon, sigma_c, sigma_o, cut_kind)
        for epsilon in itertools.product((-1, 1), repeat=2)
        for sigma_c in (-1, 1) for sigma_o in (-1, 1)
        for cut_kind in ("positive", "negative")
    )
    if limit:
        cases = cases[:limit]
    raw = list(audit.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]), "sigma": list(case[2:4]),
                "cut_kind": case[4], "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
    primary = json.loads(PRIMARY.read_text())
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell9-parallel-de-audit-v1",
        "field": PRIME,
        "scope": (
            "Independent two-variable lex and deployed-root audit for the "
            "cell-9 positive/negative DE first-pair residual systems."
        ),
        "source_replay_sha256": hashlib.sha256(REPLAY.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "source_primary_sha256": hashlib.sha256(PRIMARY.read_bytes()).hexdigest(),
        "primary_complete": all(
            row["status"] == "COMPLETE" for row in primary["rows"]
        ),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT), "cases": len(rows),
        "complete": sum(row.get("status") == "COMPLETE" for row in rows),
        "systems": sum(row.get("systems", 0) for row in rows),
        "unit_systems": sum(row.get("unit_systems", 0) for row in rows),
        "finite_systems": sum(row.get("finite_systems", 0) for row in rows),
        "no_deployed_root": sum(row.get("no_deployed_root", 0) for row in rows),
        "witnesses": sum(len(row.get("witnesses", [])) for row in rows),
        "unresolved": sum(len(row.get("unresolved", [])) for row in rows),
    }, sort_keys=True))
