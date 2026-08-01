#!/usr/bin/env python3
"""Large-prime function-field attack on the reconstructed cell-5 pair."""

import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
SPARSE = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
ATLAS = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json"
REMOTE_SPARSE = "/root/rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
REMOTE_ATLAS = "/root/rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json"

app = modal.App("rs-mca-positive-433-1a-cell5-pair-function-field")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(SPARSE, REMOTE_SPARSE)
    .add_local_file(ATLAS, REMOTE_ATLAS)
)


@app.function(image=image, cpu=1.0, memory=4096, timeout=300)
def analyze(payload):
    import hashlib
    import json
    import sys

    import sympy as sp

    stage, chart_text = payload.split(":", 1)
    chart_index = int(chart_text)
    sys.path.insert(0, "/root")
    from rate_half_kb_positive_433_1a_cell5_sparse_edge_probe import (
        sparse_product_kernel,
    )

    data = json.loads(Path(REMOTE_ATLAS).read_text())
    prime = data["characteristic"]
    iota = data["iota"]
    charts = {item["basis_index"]: item for item in data["c_charts"]}
    chart = charts[chart_index]

    e, z1, z0, b, t, r, c = sp.symbols("e z1 z0 b t r c")
    field = sp.GF(prime).frac_field(t)
    parse = {"r": r, "c": c, "b": b, "t": t}

    a0t = t**4 - 2 * iota * t**3 - 4 * iota * t**2 - 2 * iota * t - 1
    a1t = -8 * iota * (t**4 + 1)
    a2t = -2 * t**4 + 4 * iota * t**3 - 24 * iota * t**2 + 4 * iota * t + 2
    primitive = sp.Poly(
        a0t * (b**4 + 1) + a1t * (b**3 + b) + a2t * b**2,
        b, domain=field,
    ).monic()

    def bpoly(expression):
        return sp.Poly(sp.cancel(expression), b, domain=field)

    r_leading = bpoly(sp.sympify(data["r_chart"]["leading"], locals=parse))
    r_constant = bpoly(sp.sympify(data["r_chart"]["constant"], locals=parse))
    c_leading = bpoly(sp.sympify(chart["leading"], locals=parse))
    c_constant = bpoly(sp.sympify(chart["constant"], locals=parse))
    def inverse_mod(value):
        coefficient, _, gcd = sp.gcdex(value, primitive)
        if gcd.degree() != 0:
            raise RuntimeError("noninvertible lift denominator over GF(p)(t)")
        return bpoly(coefficient.as_expr() / gcd.LC()).rem(primitive)

    r_inverse = inverse_mod(r_leading)
    c_inverse = inverse_mod(c_leading)
    r_value = (-r_constant * r_inverse).rem(primitive)
    c_value = (-c_constant * c_inverse).rem(primitive)

    zero = sp.Poly(0, b, domain=field)
    one = sp.Poly(1, b, domain=field)

    def multiply(left, right):
        return (left * right).rem(primitive)

    def power(value, exponent):
        output = one
        base = value
        while exponent:
            if exponent & 1:
                output = multiply(output, base)
            base = multiply(base, base)
            exponent >>= 1
        return output

    def quotient(expression):
        source = sp.Poly(expression, r, c, b, domain=field)
        output = zero
        for (r_degree, c_degree, b_degree), coefficient in source.terms():
            term = bpoly(field.to_sympy(coefficient) * b**b_degree)
            term = multiply(term, power(r_value, r_degree))
            term = multiply(term, power(c_value, c_degree))
            output = output + term
        return output.rem(primitive)

    a2_source, a0_source, _, _, _ = sparse_product_kernel()
    a2 = [quotient(value) for value in a2_source]
    a0 = [quotient(value) for value in a0_source]

    def evaluate(coefficients, value):
        return sum(item.as_expr() * value**index
                   for index, item in enumerate(coefficients))

    delta = t**2 * (t**2 - 1)
    beta = -t * (1 + b) * evaluate(a2, t**2)
    d0 = evaluate(a2, z0**2)
    d1 = evaluate(a2, z1**2)
    n0 = evaluate(a0, z0**2)
    n1 = evaluate(a0, z1**2)
    q0 = z0 * beta * (z0**2 - 1)
    q1 = z1 * beta * (z1**2 - 1)
    pair = (
        n1 * d0 + n0 * d1,
        q0 * d1 - q1 * d0 + 2 * e * delta * d0 * d1,
        delta * n0 + e * q0 + e**2 * delta * d0,
    )
    generators = (e, z1, z0, b)
    polynomials = [
        sp.Poly(primitive.as_expr(), *generators, domain=field),
        *(sp.Poly(value, *generators, domain=field) for value in pair),
    ]
    ledger = [
        {"degree": value.total_degree(), "terms": len(value.terms())}
        for value in polynomials
    ]
    header = {
        "chart_index": chart_index,
        "field": f"GF({prime})(t)",
        "ledger": ledger,
        "primitive_degree": primitive.degree(),
        "r_degree": r_value.degree(),
        "c_degree": c_value.degree(),
        "scope": (
            "generic-t reconstructed DE+/DE- pair over the selected c chart; "
            "no exceptional t specialization, colored edge, source guards, "
            "route, row, or Prize conclusion"
        ),
    }
    serialized = "\n".join(str(value.as_expr()) for value in polynomials)
    header["input_sha256"] = hashlib.sha256(serialized.encode()).hexdigest()
    if stage == "ledger":
        return {**header, "status": "COMPLETE"}
    if stage != "groebner":
        raise ValueError("stage must be ledger or groebner")

    basis = sp.groebner(
        [value.as_expr() for value in polynomials],
        *generators, order="grevlex", domain=field, method="f5b",
    )
    basis_ledger = [
        {"degree": value.total_degree(), "terms": len(value.terms())}
        for value in basis.polys
    ]
    basis_text = "\n".join(str(value.as_expr()) for value in basis.polys)
    return {
        **header,
        "status": "COMPLETE",
        "basis_size": len(basis.polys),
        "basis_ledger": basis_ledger,
        "basis_sha256": hashlib.sha256(basis_text.encode()).hexdigest(),
        "unit": bool(len(basis.polys) == 1 and basis.polys[0].total_degree() == 0),
    }


@app.local_entrypoint()
def main(charts: str = "2", stage: str = "ledger"):
    indices = [int(value) for value in charts.split(",")]
    if any(value not in {2, 3, 4, 5} for value in indices):
        raise ValueError("charts must be a comma-separated subset of 2,3,4,5")
    if stage not in {"ledger", "groebner"}:
        raise ValueError("stage must be ledger or groebner")
    for result in analyze.map(
        [f"{stage}:{index}" for index in indices], order_outputs=True
    ):
        print(json.dumps(result, sort_keys=True), flush=True)
