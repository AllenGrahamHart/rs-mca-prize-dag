#!/usr/bin/env python3
"""Test source-only endpoint cuts on the cell-11 common curve."""

import hashlib
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
STRUCTURE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_complete_pivot_scout_result.json"
)
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_endpoint_compatibility_pilot_result.json"
)
REMOTE_STRUCTURE = "/root/structure.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell11-endpoint-pilot")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(STRUCTURE, REMOTE_STRUCTURE)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=300, max_containers=8)
def decide(case):
    import sympy as sp

    epsilon_1, epsilon_2, endpoint = case
    t, r, c, b = sp.symbols("t r c b")
    variables = (t, r, c, b)
    structure = json.loads(Path(REMOTE_STRUCTURE).read_text())
    structure_rows = [
        row for row in structure["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    ]
    signatures = {
        tuple(item["sha256"] for item in row["lex_basis"])
        for row in structure_rows
    }
    if len(structure_rows) != 6 or len(signatures) != 1:
        raise RuntimeError("structure chart mismatch")
    basis = [item["expression"] for item in structure_rows[0]["lex_basis"]]
    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    kernel_row = next(
        row for row in kernel_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    )
    kernel = [sp.sympify(item["expression"]) for item in kernel_row["kernel"]]
    a_coefficients = kernel[:3]
    b_coefficients = kernel[3:6]
    beta_0, beta_1 = kernel[6:]
    label = -t*t
    a_value = sp.expand(sum(value*label**index
                            for index, value in enumerate(a_coefficients)))
    b_value = sp.expand(sum(value*label**index
                            for index, value in enumerate(b_coefficients)))
    endpoint_value = b if endpoint == "b" else c
    cut = sp.expand(
        (endpoint_value**2*a_value + b_value)**2
        - label*(beta_0 + beta_1*label)**2*endpoint_value**2
    )

    def singular(expression):
        return str(sp.Poly(expression, *variables, modulus=PRIME).as_expr()).replace(
            "**", "^"
        )

    definitions = "\n".join(
        f"poly k{index}={expression};"
        for index, expression in enumerate(basis, start=1)
    )
    guard = (
        "r*t*b*c*(b-1)*(b+1)*(c-1)*(c+1)*(b-c)*(b+c)"
        "*(r^2-1)*(r^2+1)*(t^2-1)*(t^2+1)"
        "*(t^2-r^2)*(t^2+r^2)"
    )
    program = f"""
ring R={PRIME},(z,t,r,c,b),(dp(1),dp(4));
option(redSB);
{definitions}
poly cut={singular(cut)};
ideal G=k1,k2,k3,k4,k5,k6,k7,k8,z*({guard})-1,cut; G=slimgb(G);
print("BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); }}
ideal Er=eliminate(G,z*t*c*b); Er=slimgb(Er);
print("ERDIM="+string(dim(Er))); print("ERSIZE="+string(size(Er)));
print("ER_BEGIN"); Er; print("ER_END"); print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=240,
        )
    except subprocess.TimeoutExpired as error:
        return {
            "epsilon": [epsilon_1, epsilon_2], "endpoint": endpoint,
            "status": "TIMEOUT", "partial_stdout": (error.stdout or "")[-2000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }
    stdout = process.stdout

    def integer(label_name):
        match = re.search(rf"(?:^|\n){label_name}=(-?\d+)", stdout)
        return int(match.group(1)) if match else None

    elimination = re.search(r"ER_BEGIN\n(.*?)\nER_END", stdout, re.DOTALL)
    polynomial = sp.Poly(cut, *variables, modulus=PRIME)
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
    return {
        "epsilon": [epsilon_1, epsilon_2], "endpoint": endpoint,
        "status": "COMPLETE" if valid else "ERROR",
        "dimension": integer("DIM"), "basis_size": integer("SIZE"),
        "unit": "UNIT=1" in stdout,
        "r_elimination_dimension": integer("ERDIM"),
        "r_elimination_size": integer("ERSIZE"),
        "r_elimination": (
            "".join(elimination.group(1).split()) if elimination else None
        ),
        "cut_degree": int(polynomial.total_degree()),
        "cut_terms": len(polynomial.terms()),
        "cut_sha256": hashlib.sha256(str(polynomial.as_expr()).encode()).hexdigest(),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stdout_tail": stdout[-2000:], "stderr_tail": process.stderr[-1000:],
    }


@app.local_entrypoint()
def main():
    cases = tuple(
        (epsilon_1, epsilon_2, endpoint)
        for epsilon_1 in (-1, 1) for epsilon_2 in (-1, 1)
        for endpoint in ("b", "c")
    )
    raw = list(decide.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]), "endpoint": case[2],
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell11-endpoint-pilot-v1",
        "field": PRIME,
        "scope": (
            "Exact source-only endpoint compatibility ideals on cell 11; "
            "pilot evidence only until finite fibers are replayed."
        ),
        "source_structure_sha256": hashlib.sha256(STRUCTURE.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [{key: row.get(key) for key in (
            "epsilon", "endpoint", "status", "dimension", "basis_size",
            "unit", "r_elimination_dimension", "r_elimination_size",
            "cut_degree", "cut_terms",
        )} for row in rows],
    }, sort_keys=True))
