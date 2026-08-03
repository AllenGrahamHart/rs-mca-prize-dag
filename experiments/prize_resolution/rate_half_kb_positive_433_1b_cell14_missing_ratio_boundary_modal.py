#!/usr/bin/env python3
"""Exclude the cell-14 boundary where the missing product ratio is undefined.

The target-projection compiler writes the product at the omitted source label
as B(xi)/A(xi).  This compiler keeps the original division-free condition and
checks F(r,b)=A(xi)=B(xi)=0 over the deployed field for every source-sign row.
"""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
CURVE = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_curve_kernel_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_missing_ratio_boundary_result.json"
REMOTE_CURVE = "/root/curve.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell14-missing-ratio-boundary")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0", "python-flint==0.8.0")
    .add_local_file(CURVE, REMOTE_CURVE)
)


@app.function(image=image, cpu=1.0, memory=1024, timeout=120, max_containers=4)
def decide_source_sign(epsilon):
    import sympy as sp
    from flint import fmpz_mod_poly_ctx

    payload = json.loads(Path(REMOTE_CURVE).read_text())
    source = next(row for row in payload["rows"] if row["epsilon"] == epsilon)
    r, b = sp.symbols("r b")

    def expression(summary):
        return sp.sympify(summary["expression"])

    def poly(value, *variables):
        return sp.Poly(sp.expand(value), *variables, modulus=PRIME)

    curve = poly(expression(source["relation_rb"]), b, r)
    t_numerator = expression(source["t_map"]["numerator"])
    t_denominator = expression(source["t_map"]["denominator"])
    kernel = [expression(value) for value in source["kernel"]]

    # xi=-t^2. Multiplication by t_denominator^4 clears A(xi), B(xi)
    # without changing their zero sets on the already-proved t-map chart.
    n2 = t_numerator**2
    d2 = t_denominator**2
    n4 = n2**2
    d4 = d2**2
    a_missing = poly(kernel[0]*d4-kernel[1]*n2*d2+kernel[2]*n4, b, r)
    b_missing = poly(kernel[3]*d4-kernel[4]*n2*d2+kernel[5]*n4, b, r)
    if a_missing.degree(b) > 1 or b_missing.degree(b) > 1:
        raise ValueError("missing-label coordinates are not linear in b")

    def b_coefficients(value):
        value_expression = value.as_expr()
        return (
            poly(value_expression.coeff(b, 1), r),
            poly(value_expression.subs(b, 0), r),
        )

    a_linear, a_constant = b_coefficients(a_missing)
    b_linear, b_constant = b_coefficients(b_missing)
    cross = poly(
        a_constant.as_expr()*b_linear.as_expr()
        - a_linear.as_expr()*b_constant.as_expr(),
        r,
    )

    curve_expression = curve.as_expr()
    curve_a = poly(curve_expression.coeff(b, 2), r)
    curve_b = poly(curve_expression.coeff(b, 1), r)
    curve_c = poly(curve_expression.subs(b, 0), r)
    a_norm = poly(
        curve_a.as_expr()*a_constant.as_expr()**2
        - curve_b.as_expr()*a_constant.as_expr()*a_linear.as_expr()
        + curve_c.as_expr()*a_linear.as_expr()**2,
        r,
    )
    necessary_gcd = sp.gcd(cross, a_norm).monic()

    context = fmpz_mod_poly_ctx(PRIME)

    def flint_univariate(value):
        coefficients = {
            exponent: int(coefficient) % PRIME
            for (exponent,), coefficient in value.terms()
        }
        return context([
            coefficients.get(index, 0)
            for index in range(max(coefficients, default=0)+1)
        ])

    gcd_flint = flint_univariate(necessary_gcd)
    variable = context([0, 1])
    field_gcd = gcd_flint.gcd(pow(variable, PRIME, gcd_flint)-variable)
    _, factors = field_gcd.factor()
    roots = []
    for factor, _ in factors:
        if int(factor.degree()) != 1:
            raise ValueError("field-root gcd contains a nonlinear factor")
        roots.append(-int(factor[0])*pow(int(factor[1]), -1, PRIME) % PRIME)

    curve_leading_flint = flint_univariate(curve_a)
    curve_leading_field_gcd = curve_leading_flint.gcd(
        pow(variable, PRIME, curve_leading_flint)-variable
    )
    _, curve_leading_factors = curve_leading_field_gcd.factor()
    curve_leading_roots = []
    for factor, _ in curve_leading_factors:
        if int(factor.degree()) != 1:
            raise ValueError("curve-leading field gcd contains a nonlinear factor")
        curve_leading_roots.append(
            -int(factor[0])*pow(int(factor[1]), -1, PRIME) % PRIME
        )

    route_expressions = {
        "r": r,
        "t": t_numerator,
        "r2_minus_1": r**2-1,
        "r2_plus_1": r**2+1,
        "t2_minus_1": n2-d2,
        "t2_plus_1": n2+d2,
        "t2_minus_r2": n2-r**2*d2,
        "t2_plus_r2": n2+r**2*d2,
        "t_denominator": t_denominator,
    }

    def evaluate(value, point):
        return int(poly(value, r).eval(point)) % PRIME

    root_rows = []
    unresolved = []
    curve_leading_root_rows = []
    for r_value in sorted(curve_leading_roots):
        zero_guards = sorted(
            name for name, value in route_expressions.items()
            if evaluate(value, r_value) == 0
        )
        row = {"r": r_value, "zero_guards": zero_guards}
        if zero_guards:
            row["status"] = "ROUTE_BOUNDARY"
        else:
            row["status"] = "UNRESOLVED"
            unresolved.append(r_value)
        curve_leading_root_rows.append(row)

    b_context = fmpz_mod_poly_ctx(PRIME)
    b_variable = b_context([0, 1])
    for r_value in sorted(roots):
        zero_guards = sorted(
            name for name, value in route_expressions.items()
            if evaluate(value, r_value) == 0
        )
        row = {"r": r_value, "zero_guards": zero_guards}
        if zero_guards:
            row["status"] = "ROUTE_BOUNDARY"
            root_rows.append(row)
            continue

        def specialize(value):
            degree = value.degree(b)
            value_expression = value.as_expr()
            return b_context([
                int(poly(value_expression.coeff(b, index), r).eval(r_value)) % PRIME
                for index in range(degree+1)
            ])

        common_b = specialize(curve)
        common_b = common_b.gcd(specialize(a_missing))
        common_b = common_b.gcd(specialize(b_missing))
        field_b = common_b.gcd(pow(b_variable, PRIME, common_b)-b_variable)
        _, b_factors = field_b.factor()
        b_roots = []
        for factor, _ in b_factors:
            if int(factor.degree()) != 1:
                raise ValueError("b field-root gcd contains a nonlinear factor")
            b_roots.append(
                -int(factor[0])*pow(int(factor[1]), -1, PRIME) % PRIME
            )
        row.update({
            "status": "CHECKED",
            "common_b_degree": int(common_b.degree()),
            "b_roots": sorted(b_roots),
        })
        if b_roots:
            unresolved.append(r_value)
        root_rows.append(row)

    def summary(value):
        text = str(value.as_expr())
        return {
            "degree": value.degree(),
            "terms": len(value.terms()),
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
            "expression": text,
        }

    return {
        "epsilon": epsilon,
        "status": "COMPLETE",
        "unit": not unresolved,
        "unresolved_roots": unresolved,
        "a_missing_degree": a_missing.total_degree(),
        "b_missing_degree": b_missing.total_degree(),
        "cross": summary(cross),
        "a_norm": summary(a_norm),
        "necessary_gcd": summary(necessary_gcd),
        "field_root_gcd_degree": int(field_gcd.degree()),
        "field_roots": sorted(roots),
        "field_root_rows": root_rows,
        "curve_leading_coefficient": summary(curve_a),
        "curve_leading_field_root_gcd_degree": int(curve_leading_field_gcd.degree()),
        "curve_leading_field_roots": sorted(curve_leading_roots),
        "curve_leading_field_root_rows": curve_leading_root_rows,
    }


@app.local_entrypoint()
def main():
    cases = [[x, y] for x in (-1, 1) for y in (-1, 1)]
    rows = list(decide_source_sign.map(cases, order_outputs=False))
    rows.sort(key=lambda row: row["epsilon"])
    payload = {
        "schema": "rate-half-kb-positive-433-1b-cell14-missing-ratio-boundary-v1",
        "scope": "Division-free A(xi)=B(xi)=0 boundary on the guarded cell-14 curve.",
        "field": PRIME,
        "source_curve_sha256": hashlib.sha256(CURVE.read_bytes()).hexdigest(),
        "source_script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "case_count": len(rows),
        "unit_count": sum(bool(row.get("unit")) for row in rows),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT),
        "case_count": payload["case_count"],
        "unit_count": payload["unit_count"],
        "failures": [row["epsilon"] for row in rows if not row.get("unit")],
    }, sort_keys=True))
