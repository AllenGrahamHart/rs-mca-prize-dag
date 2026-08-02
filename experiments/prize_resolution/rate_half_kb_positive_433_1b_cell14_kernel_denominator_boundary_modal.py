#!/usr/bin/env python3
"""Exclude the normalized-kernel denominator boundary on cell 14."""

import hashlib
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
CURVE = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_curve_kernel_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_kernel_denominator_boundary_result.json"
REMOTE_CURVE = "/root/curve.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell14-kernel-denominator-boundary")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(CURVE, REMOTE_CURVE)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=120, max_containers=4)
def decide(signs):
    import sympy as sp

    epsilon_1, epsilon_2 = signs
    payload = json.loads(Path(REMOTE_CURVE).read_text())
    row = next(value for value in payload["rows"]
               if value["epsilon"] == [epsilon_1, epsilon_2])
    t, c, r, b = sp.symbols("t c r b")
    variables = (t, c, r, b)

    def expression(summary):
        return sp.sympify(summary["expression"])

    t_numerator = expression(row["t_map"]["numerator"])
    t_denominator = expression(row["t_map"]["denominator"])
    c_numerator = expression(row["c_map"]["numerator"])
    c_denominator = expression(row["c_map"]["denominator"])
    relation = expression(row["relation_rb"])
    kernel_denominator = expression(row["kernel_common_denominator"])
    equations = (
        t*t_denominator-t_numerator,
        c*c_denominator-c_numerator,
        relation,
        kernel_denominator,
    )
    guards = (
        b, c, r, t,
        b-1, b+1, c-1, c+1, b-c, b+c,
        r*r-1, r*r+1, t*t-1, t*t+1,
        t*t-r*r, t*t+r*r,
        t_denominator, c_denominator,
    )

    def polynomial(value):
        return sp.Poly(value, *variables, modulus=PRIME).as_expr()

    def singular(value):
        return str(polynomial(value)).replace("**", "^")

    equation_definitions = "\n".join(
        f"poly q{index}={singular(value)};"
        for index, value in enumerate(equations)
    )
    guard_definitions = "\n".join(
        f"poly h{index}={singular(value)};"
        for index, value in enumerate(guards)
    )
    saturation = "\n".join(
        f"ideal H{index}=h{index}; list L{index}=sat(G,H{index}); "
        f"G=L{index}[1]; G=slimgb(G); "
        f'print("SAT={index},DIM="+string(dim(G))+",SIZE="+string(size(G)));'
        for index in range(len(guards))
    )
    program = f"""
LIB "elim.lib";
ring R={PRIME},(t,c,r,b),dp;
option(redSB);
{equation_definitions}
{guard_definitions}
ideal G=q0,q1,q2,q3; G=slimgb(G);
print("INITIAL_DIM="+string(dim(G))+",INITIAL_SIZE="+string(size(G)));
{saturation}
print("BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); G; }}
print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=100,
        )
    except subprocess.TimeoutExpired as error:
        partial_stdout = error.stdout or ""
        partial_stderr = error.stderr or ""
        if isinstance(partial_stdout, bytes):
            partial_stdout = partial_stdout.decode(errors="replace")
        if isinstance(partial_stderr, bytes):
            partial_stderr = partial_stderr.decode(errors="replace")
        return {"epsilon": list(signs), "status": "TIMEOUT",
                "partial_stdout": partial_stdout[-4000:],
                "partial_stderr": partial_stderr[-1000:]}
    stdout = process.stdout
    dimensions = re.findall(r"DIM=(-?\d+)", stdout)
    sizes = re.findall(r"SIZE=(\d+)", stdout)
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
    return {
        "epsilon": list(signs),
        "status": "COMPLETE" if valid else "ERROR",
        "unit": bool(re.search(r"(?:^|\n)UNIT=1(?:\n|$)", stdout)),
        "dimension": int(dimensions[-1]) if dimensions else None,
        "basis_size": int(sizes[-1]) if sizes else None,
        "stdout": stdout[-12000:], "stderr": process.stderr[-1000:],
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "kernel_denominator": singular(kernel_denominator),
    }


@app.local_entrypoint()
def main():
    signs = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    raw = list(decide.map(signs, order_outputs=True, return_exceptions=True))
    rows = []
    for sign, row in zip(signs, raw):
        if isinstance(row, BaseException):
            rows.append({"epsilon": list(sign), "status": "REMOTE_ERROR",
                         "error": repr(row)})
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell14-kernel-denominator-boundary-v1",
        "field": PRIME,
        "scope": "Exact guarded exclusion of the normalized-kernel denominator boundary.",
        "source_curve_sha256": hashlib.sha256(CURVE.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"result": str(RESULT),
                      "rows": [{key: row.get(key) for key in
                                ("epsilon", "status", "unit", "dimension",
                                 "basis_size")} for row in rows]},
                     sort_keys=True))
