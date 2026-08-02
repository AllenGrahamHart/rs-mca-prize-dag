#!/usr/bin/env python3
"""Bounded deployed-field chart attack on the cell-5 DE+/DE-/BE family."""

import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
SPARSE = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
ATLAS = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json"
REMOTE_SPARSE = "/root/rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
REMOTE_ATLAS = "/root/rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json"

app = modal.App("rs-mca-positive-433-1a-cell5-colored-charts")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(SPARSE, REMOTE_SPARSE)
    .add_local_file(ATLAS, REMOTE_ATLAS)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=300)
def analyze(payload):
    import hashlib
    import json
    import subprocess
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from rate_half_kb_positive_433_1a_cell5_sparse_edge_probe import (
        sparse_product_kernel,
    )

    stage, chart_text = payload.split(":", 1)
    chart_index = int(chart_text)
    data = json.loads(Path(REMOTE_ATLAS).read_text())
    prime = data["characteristic"]
    iota = data["iota"]
    charts = {item["basis_index"]: item for item in data["c_charts"]}
    if chart_index not in charts:
        raise ValueError(f"unknown c chart {chart_index}")

    z0, z1, z2, d, e, s, r, c, b, t = sp.symbols(
        "z0 z1 z2 d e s r c b t"
    )
    variables = (r, c, s, z2, d, e, z0, z1, b, t)
    parse = {"r": r, "c": c, "b": b, "t": t}
    chart = charts[chart_index]
    c_leading = sp.sympify(chart["leading"], locals=parse)
    c_constant = sp.sympify(chart["constant"], locals=parse)
    r_leading = sp.sympify(data["r_chart"]["leading"], locals=parse)
    r_constant = sp.sympify(data["r_chart"]["constant"], locals=parse)

    a2, a0, _, _, _ = sparse_product_kernel()

    a0t = t**4 - 2 * iota * t**3 - 4 * iota * t**2 - 2 * iota * t - 1
    a1t = -8 * iota * (t**4 + 1)
    a2t = -2 * t**4 + 4 * iota * t**3 - 24 * iota * t**2 + 4 * iota * t + 2
    projection = sp.expand(
        a0t * (b**4 + 1) + a1t * (b**3 + b) + a2t * b**2
    )
    r_equation = sp.expand(r * r_leading + r_constant)
    c_equation = sp.expand(c * c_leading + c_constant)
    d2_expression = sp.expand(sum(
        a2[index] * z2**(2 * index) for index in range(3)
    ))
    n2_expression = sp.expand(sum(
        a0[index] * z2**(2 * index) for index in range(3)
    ))
    beta_expression = sp.expand(
        -t * (1 + b) * sum(a2[index] * t**(2 * index)
                           for index in range(3))
    )
    endpoint_expression = sp.expand(
        t**2 * (t**2 - 1) * (b**2 * d2_expression + n2_expression)
        + b * z2 * beta_expression * (z2**2 - 1)
    )
    endpoint_poly = sp.Poly(endpoint_expression, z2, r, c, b, t,
                            modulus=prime)
    residual_endpoint, endpoint_remainder = sp.div(
        endpoint_poly,
        sp.Poly(2 * b * t * (t**2 - 1) * (z2 - t),
                z2, r, c, b, t, modulus=prime),
    )
    if not endpoint_remainder.is_zero:
        raise RuntimeError("nonexact BE endpoint division")

    def singular(expression):
        return str(sp.Poly(sp.expand(expression), *variables, modulus=prime)
                   .as_expr()).replace("**", "^")

    declarations = [
        f"poly f0={singular(projection)};",
        f"poly f1={singular(r_equation)};",
        f"poly f2={singular(c_equation)};",
        f"poly cLeading={singular(c_leading)};",
        *(f"poly dcoef{index}={singular(value)};"
          for index, value in enumerate(a2)),
        *(f"poly ncoef{index}={singular(value)};"
          for index, value in enumerate(a0)),
        "poly delta=t^2*(t^2-1);",
        "poly beta=-t*(1+b)*(dcoef0+dcoef1*t^2+dcoef2*t^4);",
        "poly d0=dcoef0+dcoef1*z0^2+dcoef2*z0^4;",
        "poly d1=dcoef0+dcoef1*z1^2+dcoef2*z1^4;",
        "poly d2=dcoef0+dcoef1*z2^2+dcoef2*z2^4;",
        "poly n0=ncoef0+ncoef1*z0^2+ncoef2*z0^4;",
        "poly n1=ncoef0+ncoef1*z1^2+ncoef2*z1^4;",
        "poly n2=ncoef0+ncoef1*z2^2+ncoef2*z2^4;",
        "poly q0=z0*beta*(z0^2-1);",
        "poly q1=z1*beta*(z1^2-1);",
        "poly q2=z2*beta*(z2^2-1);",
        f"poly residualEndpoint={singular(residual_endpoint.as_expr())};",
    ]
    if stage.startswith(("direct-", "reconstructed-")):
        declarations.extend((
            "poly f3=n0-d*e*d0;",
            "poly f4=q0+(d+e)*delta*d0;",
            "poly f5=n1+d*e*d1;",
            "poly f6=q1+(d-e)*delta*d1;",
            "poly f7=residualEndpoint;",
            "poly f8=q2+(b+e)*delta*d2;",
            "poly f9=s*cLeading-1;",
        ))
    else:
        declarations.extend((
            "poly f3=n1*d0+n0*d1;",
            "poly f4=q0^2*d1^2-q1^2*d0^2-4*n0*delta^2*d0*d1^2;",
            "poly f5=residualEndpoint;",
            "poly f6=-2*q2*d0*d1-2*b*delta*d0*d1*d2"
            "-d2*(q1*d0-q0*d1);",
            "poly f7=s*cLeading*delta*d0*d1*d2-1;",
            "poly f8=s*cLeading*delta*d0*d1-1;",
        ))
    header = {
        "chart_index": chart_index,
        "stage": stage,
        "scope": (
            "necessary guarded superset for deployed cell-5 DE+/DE-/BE; "
            "unit proves chart emptiness, nonunit may contain projection "
            "or omitted-distinctness artifacts"
        ),
    }
    if stage == "direct-ledger":
        body = (
            'print("COLORED_DIRECT_LEDGER");',
            *(f"print(deg(f{index})); print(size(f{index}));"
              for index in range(10)),
        )
        expected = "COLORED_DIRECT_LEDGER"
    elif stage == "direct-basis":
        body = (
            "ideal J=f0,f1,f2,f3,f4,f5,f6,f7,f8,f9;",
            'print("COLORED_DIRECT_INPUT");',
            "print(dim(J)); print(size(J));",
            "ideal G=slimgb(J);",
            'print("COLORED_DIRECT_BASIS");',
            "print(dim(G)); print(size(G));",
            'if (reduce(1,G)==0) { print("UNIT"); } else { print("NONUNIT"); }',
            "if (dim(G)==0) { print(vdim(G)); }",
        )
        expected = "COLORED_DIRECT_BASIS"
    elif stage == "reconstructed-ledger":
        body = (
            "poly g3=n1*d0+n0*d1;",
            "poly g4=q0*d1-q1*d0+2*e*delta*d0*d1;",
            "poly g5=delta*n0+e*q0+e^2*delta*d0;",
            "poly g6=resultant(f7,f8,z2);",
            "poly g7=s*cLeading-1;",
            'print("COLORED_RECONSTRUCTED_LEDGER");',
            *(f"print(deg(g{index})); print(size(g{index}));"
              for index in range(3, 8)),
        )
        expected = "COLORED_RECONSTRUCTED_LEDGER"
    elif stage == "reconstructed-basis":
        body = (
            "poly g3=n1*d0+n0*d1;",
            "poly g4=q0*d1-q1*d0+2*e*delta*d0*d1;",
            "poly g5=delta*n0+e*q0+e^2*delta*d0;",
            "poly g6=resultant(f7,f8,z2);",
            "poly g7=s*cLeading-1;",
            "ideal J=f0,f1,f2,g3,g4,g5,g6,g7;",
            'print("COLORED_RECONSTRUCTED_INPUT");',
            "print(dim(J)); print(size(J));",
            "ideal G=slimgb(J);",
            'print("COLORED_RECONSTRUCTED_BASIS");',
            "print(dim(G)); print(size(G));",
            'if (reduce(1,G)==0) { print("UNIT"); } else { print("NONUNIT"); }',
        )
        expected = "COLORED_RECONSTRUCTED_BASIS"
    elif stage == "ledger":
        body = (
            'print("COLORED_CHART_LEDGER");',
            *(f"print(deg(f{index})); print(size(f{index}));"
              for index in range(9)),
        )
        expected = "COLORED_CHART_LEDGER"
    elif stage == "basis":
        body = (
            "ideal J=f0,f1,f2,f3,f4,f5,f6,f7;",
            'print("COLORED_CHART_INPUT");',
            "print(dim(J)); print(size(J));",
            "ideal G=slimgb(J);",
            'print("COLORED_CHART_BASIS");',
            "print(dim(G)); print(size(G));",
            'if (reduce(1,G)==0) { print("UNIT"); } else { print("NONUNIT"); }',
            "if (dim(G)==0) { print(vdim(G)); }",
        )
        expected = "COLORED_CHART_BASIS"
    elif stage == "z2-basis":
        body = (
            "poly z2cut=resultant(f5,f6,z2);",
            'print("COLORED_Z2_RESULTANT");',
            "print(deg(z2cut)); print(size(z2cut));",
            "ideal J=f0,f1,f2,f3,f4,z2cut,f8;",
            'print("COLORED_Z2_INPUT");',
            "print(dim(J)); print(size(J));",
            "ideal G=slimgb(J);",
            'print("COLORED_Z2_BASIS");',
            "print(dim(G)); print(size(G));",
            'if (reduce(1,G)==0) { print("UNIT"); } else { print("NONUNIT"); }',
            "if (dim(G)==1) { print(vdim(G)); }",
        )
        expected = "COLORED_Z2_BASIS"
    else:
        raise ValueError(
            "stage must be direct-ledger, direct-basis, ledger, basis, or "
            "z2-basis, reconstructed-ledger, or reconstructed-basis"
        )
    program = "\n".join((
        f"ring R={prime},(r,c,s,z2,d,e,z0,z1,b,t),(dp(6),dp(4));",
        "option(redSB);",
        *declarations,
        *body,
        "quit;",
    ))
    header = {
        **header,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
    }
    try:
        process = subprocess.run(
            ["Singular", "-q"], input=program, capture_output=True,
            text=True, timeout=240,
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""

        return {
            **header,
            "status": "TIMEOUT",
            "stdout": decoded(error.stdout)[-8000:],
            "stderr": decoded(error.stderr)[-4000:],
        }
    valid = (
        process.returncode == 0
        and "?" not in process.stdout
        and expected in process.stdout
    )
    return {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "returncode": process.returncode,
        "stdout": process.stdout[-8000:],
        "stderr": process.stderr[-4000:],
    }


@app.local_entrypoint()
def main(charts: str = "2,3,4,5", stage: str = "direct-ledger"):
    indices = [int(value) for value in charts.split(",")]
    if any(value not in {2, 3, 4, 5} for value in indices):
        raise ValueError("charts must be a comma-separated subset of 2,3,4,5")
    stages = {
        "direct-ledger", "direct-basis", "reconstructed-ledger",
        "reconstructed-basis", "ledger", "basis", "z2-basis",
    }
    if stage not in stages:
        raise ValueError(f"stage must be one of {sorted(stages)}")
    payloads = [f"{stage}:{index}" for index in indices]
    for result in analyze.map(payloads, order_outputs=True):
        print(json.dumps(result, sort_keys=True), flush=True)
