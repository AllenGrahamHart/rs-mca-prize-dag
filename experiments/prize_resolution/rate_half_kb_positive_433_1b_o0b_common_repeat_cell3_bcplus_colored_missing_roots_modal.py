#!/usr/bin/env python3
"""Lift deployed-field roots of the cell-3 BC+ BE/CF missing cuts."""

from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import time

import modal


DIRECTORY = Path(__file__).parent
TORUS = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcplus_monomial_probe_result.json"
)
CUT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcplus_colored_missing_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcplus_colored_missing_roots_result.json"
)
REMOTE_TORUS = "/root/torus.json"
REMOTE_CUT = "/root/cut.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-o0b-cell3-bcplus-colored-roots")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0", "python-flint==0.8.0")
    .add_local_file(TORUS, REMOTE_TORUS)
    .add_local_file(CUT, REMOTE_CUT)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=180, max_containers=8)
def lift(case):
    import sympy as sp
    from flint import fmpz_mod_poly_ctx

    started = time.perf_counter()
    epsilon_1, epsilon_2, missing_record = case
    torus_payload = json.loads(Path(REMOTE_TORUS).read_text())
    cut_payload = json.loads(Path(REMOTE_CUT).read_text())
    torus_row = next(
        row for row in torus_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    )
    cut_row = next(
        row for row in cut_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
        and row["missing_record"] == missing_record
    )
    if cut_row["status"] != "COMPLETE" or cut_row["unit"]:
        raise ValueError("cut custody")

    b, r, u = sp.symbols("b r u")
    labels = (1, r**4, -1, r**2, -r**2)
    products = (-1, b, u, b*u, b*u)
    matrix = sp.Matrix([
        [-product, -product*label, -product*label**2,
         1, label, label**2]
        for product, label in zip(products, labels)
    ])
    cofactors = []
    for column in range(6):
        columns = [index for index in range(6) if index != column]
        value = (-1)**column*matrix[:, columns].det(method="berkowitz")
        cofactors.append(
            sp.Poly(sp.expand(value), b, r, u, modulus=PRIME).as_expr()
        )
    scale = r**4*(1-r**4)
    kernel = [scale*value for value in cofactors]
    a_values = kernel[:3]
    b_values = kernel[3:6]
    a_pivot = sum(value*r**(4*index)
                  for index, value in enumerate(cofactors[:3]))
    beta_0 = -epsilon_1*epsilon_2*r**2*(1+b)*a_pivot
    beta_1 = -beta_0
    missing_label = -r**4
    a_missing = sum(value*missing_label**index
                    for index, value in enumerate(a_values))
    b_missing = sum(value*missing_label**index
                    for index, value in enumerate(b_values))
    beta_missing = beta_0+beta_1*missing_label
    known = b if missing_record == "BE" else u
    cut = r**4*known**2*beta_missing**2+(known**2*a_missing+b_missing)**2
    substitution = {b: -u**-3}

    def numerator(expression):
        value, _ = sp.fraction(sp.cancel(expression.subs(substitution)))
        polynomial = sp.Poly(sp.expand(value), r, u, modulus=PRIME)
        return polynomial.monic().as_expr()

    cut_ru = numerator(cut)
    core_ru = sp.Poly(
        sp.sympify(torus_row["torus_core"]["expression"]),
        r, u, modulus=PRIME,
    ).monic().as_expr()
    resultant = sp.Poly(cut_ru, r, u, modulus=PRIME).resultant(
        sp.Poly(core_ru, r, u, modulus=PRIME)
    )
    if resultant.is_zero:
        return {
            "epsilon": [epsilon_1, epsilon_2],
            "missing_record": missing_record,
            "status": "ZERO_RESULTANT",
            "seconds": time.perf_counter()-started,
        }

    context = fmpz_mod_poly_ctx(PRIME)
    variable = context([0, 1])

    def to_flint(poly, variable_symbol):
        source = sp.Poly(poly, variable_symbol, modulus=PRIME)
        coefficients = {
            exponents[0]: int(coefficient) % PRIME
            for exponents, coefficient in source.terms()
        }
        return context([
            coefficients.get(index, 0)
            for index in range(max(coefficients, default=0)+1)
        ])

    def field_roots(polynomial):
        if polynomial.is_zero():
            return None
        if int(polynomial.degree()) == 0:
            return []
        split = polynomial.gcd(pow(variable, PRIME, polynomial)-variable)
        _, factors = split.factor()
        roots = []
        for factor, multiplicity in factors:
            if int(factor.degree()) != 1:
                raise ValueError("field-root gcd has nonlinear factor")
            root = -int(factor[0])*pow(int(factor[1]), -1, PRIME) % PRIME
            roots.extend([root]*int(multiplicity))
        return sorted(set(roots))

    resultant_u = to_flint(resultant.as_expr(), u)
    u_roots = field_roots(resultant_u)
    if u_roots is None:
        raise ValueError("zero resultant polynomial")

    def specialize_r(expression, u_value):
        source = sp.Poly(expression, r, u, modulus=PRIME)
        coefficients = {}
        for exponents, coefficient in source.terms():
            value = int(coefficient)*pow(u_value, exponents[1], PRIME) % PRIME
            coefficients[exponents[0]] = (
                coefficients.get(exponents[0], 0)+value
            ) % PRIME
        return context([
            coefficients.get(index, 0)
            for index in range(max(coefficients, default=0)+1)
        ])

    def evaluate(expression, values):
        source = sp.Poly(expression, b, r, u, modulus=PRIME)
        output = 0
        for exponents, coefficient in source.terms():
            term = int(coefficient) % PRIME
            for value, exponent in zip(values, exponents):
                term = term*pow(value, exponent, PRIME) % PRIME
            output = (output+term) % PRIME
        return output

    guard_ru = sp.Poly(
        sp.sympify(torus_row["transformed_guard"]["expression"]),
        r, u, modulus=PRIME,
    ).as_expr()
    points = []
    unresolved = []
    u_rows = []
    for u_value in u_roots:
        if u_value == 0:
            u_rows.append({"u": u_value, "status": "U_BOUNDARY"})
            continue
        h_r = specialize_r(core_ru, u_value)
        e_r = specialize_r(cut_ru, u_value)
        common = h_r.gcd(e_r)
        r_roots = field_roots(common)
        u_row = {
            "u": u_value,
            "gcd_degree": int(common.degree()),
            "r_roots": r_roots,
            "root_rows": [],
        }
        if r_roots is None:
            unresolved.append([u_value, "ZERO_R_GCD"])
            u_row["status"] = "ZERO_R_GCD"
            u_rows.append(u_row)
            continue
        for r_value in r_roots:
            core_value = int(h_r(r_value)) % PRIME
            cut_value = int(e_r(r_value)) % PRIME
            if core_value or cut_value:
                raise ValueError("specialized gcd root replay")
            guard_value = 0
            guard_poly = sp.Poly(guard_ru, r, u, modulus=PRIME)
            for exponents, coefficient in guard_poly.terms():
                guard_value = (
                    guard_value+int(coefficient)
                    * pow(r_value, exponents[0], PRIME)
                    * pow(u_value, exponents[1], PRIME)
                ) % PRIME
            root_row = {
                "r": r_value,
                "core_value": core_value,
                "cut_value": cut_value,
                "guard_value": guard_value,
            }
            if guard_value == 0:
                root_row["status"] = "GUARD_BOUNDARY"
                u_row["root_rows"].append(root_row)
                continue
            b_value = -pow(u_value, -3, PRIME) % PRIME
            values = (b_value, r_value, u_value)
            am = evaluate(a_missing, values)
            bm = evaluate(b_missing, values)
            betam = evaluate(beta_missing, values)
            point = {
                "b": b_value, "r": r_value, "u": u_value,
                "a_missing": am, "b_missing": bm,
                "beta_missing": betam,
            }
            if am == 0:
                point["status"] = "MISSING_RATIO_BOUNDARY"
            else:
                source_product = bm*pow(am, -1, PRIME) % PRIME
                known_value = b_value if missing_record == "BE" else u_value
                target_value = source_product*pow(known_value, -1, PRIME) % PRIME
                source_sum = (
                    (-pow(r_value, 4, PRIME))*betam*betam*pow(am, -2, PRIME)
                ) % PRIME
                direct_sum = pow(known_value+target_value, 2, PRIME)
                if direct_sum != source_sum:
                    raise ValueError("missing sum lift")
                point.update({
                    "source_product": source_product,
                    "source_squared_sum": source_sum,
                    "missing_target_coordinate": target_value,
                    "status": "LIFTED",
                })
            points.append(point)
            root_row["status"] = point["status"]
            root_row["point_index"] = len(points)-1
            u_row["root_rows"].append(root_row)
        u_row["status"] = "CHECKED"
        u_rows.append(u_row)

    resultant_text = str(resultant.as_expr())
    return {
        "epsilon": [epsilon_1, epsilon_2],
        "missing_record": missing_record,
        "status": "COMPLETE" if not unresolved else "INCOMPLETE",
        "resultant_degree": int(resultant_u.degree()),
        "resultant_terms": len(resultant.coeffs()),
        "resultant_sha256": hashlib.sha256(resultant_text.encode()).hexdigest(),
        "u_roots": u_roots,
        "u_rows": u_rows,
        "raw_r_root_count": sum(
            len(row.get("r_roots") or []) for row in u_rows
        ),
        "guard_boundary_count": sum(
            root["status"] == "GUARD_BOUNDARY"
            for row in u_rows for root in row.get("root_rows", [])
        ),
        "point_count": len(points),
        "boundary_count": sum(
            point["status"] == "MISSING_RATIO_BOUNDARY" for point in points
        ),
        "points": points,
        "unresolved": unresolved,
        "seconds": time.perf_counter()-started,
    }


@app.local_entrypoint()
def main():
    cases = tuple(itertools.product((-1, 1), (-1, 1), ("BE", "CF")))
    raw = list(lift.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]), "missing_record": case[2],
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            rows.append(row)
    status_counts = dict(sorted(Counter(row["status"] for row in rows).items()))
    output = {
        "schema": "rate-half-kb-positive-433-1b-o0b-cell3-bcplus-colored-roots-v1",
        "scope": (
            "Exact deployed-field roots of the BE/CF common-only missing cuts; "
            "no residual matching or outside exclusion claim."
        ),
        "source_torus_sha256": hashlib.sha256(TORUS.read_bytes()).hexdigest(),
        "source_cut_sha256": hashlib.sha256(CUT.read_bytes()).hexdigest(),
        "case_count": len(rows),
        "status_counts": status_counts,
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT),
        "status_counts": status_counts,
        "maximum_seconds": max((row.get("seconds", 0) for row in rows), default=0),
        "rows": [[row.get("epsilon"), row.get("missing_record"),
                  row.get("status"), row.get("resultant_degree"),
                  len(row.get("u_roots", [])), row.get("point_count"),
                  row.get("raw_r_root_count"), row.get("guard_boundary_count"),
                  row.get("boundary_count"), len(row.get("unresolved", []))]
                 for row in rows],
    }, sort_keys=True))
