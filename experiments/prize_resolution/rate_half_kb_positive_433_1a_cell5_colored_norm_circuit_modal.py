#!/usr/bin/env python3
"""Sparse norm-circuit attack on one deployed cell-5 colored family."""

import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
SPARSE = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
ATLAS = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json"
REMOTE_SPARSE = "/root/rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
REMOTE_ATLAS = "/root/rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json"

app = modal.App("rs-mca-positive-433-1a-cell5-colored-norm-circuit")
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

    r, c, b, t = sp.symbols("r c b t")
    parse = {"r": r, "c": c, "b": b, "t": t}
    c_leading = sp.sympify(chart["leading"], locals=parse)
    c_equation = sp.expand(
        c * c_leading + sp.sympify(chart["constant"], locals=parse)
    )
    r_equation = sp.expand(
        r * sp.sympify(data["r_chart"]["leading"], locals=parse)
        + sp.sympify(data["r_chart"]["constant"], locals=parse)
    )
    a0t = t**4 - 2 * iota * t**3 - 4 * iota * t**2 - 2 * iota * t - 1
    a1t = -8 * iota * (t**4 + 1)
    a2t = -2 * t**4 + 4 * iota * t**3 - 24 * iota * t**2 + 4 * iota * t + 2
    projection = sp.expand(
        a0t * (b**4 + 1) + a1t * (b**3 + b) + a2t * b**2
    )
    a2, a0, _, _, _ = sparse_product_kernel()
    variables = (r, c, b, t)

    def singular(expression):
        return str(sp.Poly(sp.expand(expression), *variables, modulus=prime)
                   .as_expr()).replace("**", "^")

    pair_declarations = [
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
        "poly n0=ncoef0+ncoef1*z0^2+ncoef2*z0^4;",
        "poly n1=ncoef0+ncoef1*z1^2+ncoef2*z1^4;",
        "poly q0=z0*beta*(z0^2-1);",
        "poly q1=z1*beta*(z1^2-1);",
        "poly hd0=dd0-d0;",
        "poly hd1=dd1-d1;",
        "poly hn0=nn0-n0;",
        "poly hn1=nn1-n1;",
        "poly hqsource0=qq0-q0;",
        "poly hqsource1=qq1-q1;",
        "poly g3=nn1*dd0+nn0*dd1;",
        "poly g4=qq0*dd1-qq1*dd0+2*e*delta*dd0*dd1;",
        "poly g5=delta*nn0+e*qq0+e^2*delta*dd0;",
        "poly hguard=s*cLeading-1;",
    ]
    norm_declarations = [
        "poly hA=aa-(ncoef2-b*e*dcoef2);",
        "poly hB=bb-(ncoef1-b*e*dcoef1);",
        "poly hC=cc-(ncoef0-b*e*dcoef0);",
        "poly sum2=(b+e)^2;",
        "poly hq0=v0+sum2*dcoef0^2;",
        "poly hq1=v1-(beta^2-2*sum2*dcoef0*dcoef1);",
        "poly hq2=v2-(-2*beta^2-sum2*(dcoef1^2+2*dcoef0*dcoef2));",
        "poly hq3=v3-(beta^2-2*sum2*dcoef1*dcoef2);",
        "poly hq4=v4+sum2*dcoef2^2;",
        "poly hr1=rr1-(v4*(-bb^3+2*aa*bb*cc)"
        "+v3*aa*(bb^2-aa*cc)-v2*aa^2*bb+v1*aa^3);",
        "poly hr0=rr0-(v4*(-bb^2*cc+aa*cc^2)"
        "+v3*aa*bb*cc-v2*aa^2*cc+v0*aa^3);",
        "poly hnorm=aa*rr0^2-bb*rr0*rr1+cc*rr1^2;",
    ]
    equations = (
        "f0", "f1", "f2", "hd0", "hd1", "hn0", "hn1", "hqsource0",
        "hqsource1", "g3", "g4", "g5", "hA", "hB", "hC", "hq0",
        "hq1", "hq2", "hq3", "hq4", "hr0", "hr1", "hnorm", "hguard",
    )
    pair_equations = (
        "f0", "f1", "f2", "hd0", "hd1", "hn0", "hn1", "hqsource0",
        "hqsource1", "g3", "g4", "g5", "hguard",
    )
    if stage == "pair-ledger":
        body = (
            'print("SIGNED_PAIR_CIRCUIT_LEDGER");',
            *(f"print(deg({name})); print(size({name}));"
              for name in pair_equations),
        )
        expected = "SIGNED_PAIR_CIRCUIT_LEDGER"
    elif stage in {"pair-basis", "pair-dp-basis"}:
        body = (
            f"ideal J={','.join(pair_equations)};",
            'print("SIGNED_PAIR_CIRCUIT_INPUT");',
            "print(dim(J)); print(size(J));",
            "ideal G=slimgb(J);",
            'print("SIGNED_PAIR_CIRCUIT_BASIS");',
            "print(dim(G)); print(size(G));",
            'if (reduce(1,G)==0) { print("UNIT"); } else { print("NONUNIT"); }',
        )
        expected = "SIGNED_PAIR_CIRCUIT_BASIS"
    elif stage == "ledger":
        body = (
            'print("COLORED_NORM_CIRCUIT_LEDGER");',
            *(f"print(deg({name})); print(size({name}));" for name in equations),
        )
        expected = "COLORED_NORM_CIRCUIT_LEDGER"
    elif stage == "basis":
        body = (
            f"ideal J={','.join(equations)};",
            'print("COLORED_NORM_CIRCUIT_INPUT");',
            "print(dim(J)); print(size(J));",
            "ideal G=slimgb(J);",
            'print("COLORED_NORM_CIRCUIT_BASIS");',
            "print(dim(G)); print(size(G));",
            'if (reduce(1,G)==0) { print("UNIT"); } else { print("NONUNIT"); }',
        )
        expected = "COLORED_NORM_CIRCUIT_BASIS"
    else:
        raise ValueError(
            "stage must be pair-ledger, pair-basis, pair-dp-basis, ledger, "
            "or basis"
        )

    if stage.startswith("pair-"):
        order = "dp" if stage == "pair-dp-basis" else "(dp(9),dp(5))"
        ring = (
            f"ring R={prime},"
            "(dd0,dd1,nn0,nn1,qq0,qq1,r,c,s,e,z0,z1,b,t),"
            f"{order};"
        )
        active_declarations = pair_declarations
    else:
        ring = (
            f"ring R={prime},"
            "(aa,bb,cc,v0,v1,v2,v3,v4,rr0,rr1,"
            "dd0,dd1,nn0,nn1,qq0,qq1,r,c,s,e,z0,z1,b,t),"
            "(dp(19),dp(5));"
        )
        active_declarations = [*pair_declarations, *norm_declarations]
    program = "\n".join((
        ring,
        "option(redSB);",
        *active_declarations,
        *body,
        "quit;",
    ))
    header = {
        "chart_index": chart_index,
        "stage": stage,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "scope": (
            "necessary deployed cell-5 DE+/DE-/BE relaxation using the "
            "proved compact squared-sum edge norm; unit proves chart "
            "emptiness, nonunit need not lift unsquared or pass guards"
        ),
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
def main(charts: str = "2", stage: str = "pair-ledger"):
    indices = [int(value) for value in charts.split(",")]
    if any(value not in {2, 3, 4, 5} for value in indices):
        raise ValueError("charts must be a comma-separated subset of 2,3,4,5")
    if stage not in {
        "pair-ledger", "pair-basis", "pair-dp-basis", "ledger", "basis",
    }:
        raise ValueError(
            "stage must be pair-ledger, pair-basis, pair-dp-basis, ledger, "
            "or basis"
        )
    for result in analyze.map(
        [f"{stage}:{index}" for index in indices], order_outputs=True
    ):
        print(json.dumps(result, sort_keys=True), flush=True)
