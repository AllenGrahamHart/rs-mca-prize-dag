#!/usr/bin/env python3
"""Price and extract the symmetric WCL weight-six sign product."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import modal


OUTPUT = Path(__file__).with_name("dli_wcl_ell1_weight6_psi6_formula_result.json")

PROGRAM = r'''
import hashlib
import json
import time
import sympy as sp

started = time.monotonic()
r = sp.symbols("r1:7")
y = sp.symbols("y1:7")
value = sum(r)
stages = []

def emit(stage, polynomial, variables):
    row = {
        "stage": stage,
        "terms": len(sp.Poly(polynomial, *variables).terms()),
        "seconds": round(time.monotonic() - started, 6),
    }
    stages.append(row)
    print("STAGE " + json.dumps(row, sort_keys=True), flush=True)

for index in range(5, 0, -1):
    paired = sp.expand(value * value.xreplace({r[index]: -r[index]}))
    univariate = sp.Poly(paired, r[index])
    if any((degree[0] & 1) for degree, coefficient in univariate.terms() if coefficient):
        raise AssertionError("odd eliminated exponent")
    value = sp.expand(sum(
        coefficient * y[index] ** (degree[0] // 2)
        for degree, coefficient in univariate.terms()
    ))
    emit(f"eliminate_r{index+1}", value, (*r[:index], *y[index:]))

univariate = sp.Poly(value, r[0])
if any((degree[0] & 1) for degree, coefficient in univariate.terms() if coefficient):
    raise AssertionError("odd r1 exponent")
psi = sp.expand(sum(
    coefficient * y[0] ** (degree[0] // 2)
    for degree, coefficient in univariate.terms()
))
emit("psi_y", psi, y)

symmetric, remainder, mapping = sp.symmetrize(psi, y, formal=True)
if remainder != 0:
    raise AssertionError("nonzero symmetric remainder")
s_symbols = [pair[0] for pair in mapping]
s_poly = sp.Poly(symmetric, *s_symbols)
emit("psi_elementary", symmetric, s_symbols)

for roots in ((1,2,3,4,5,6), (1,-2,4,-5,7,9), (2,3,5,7,11,13)):
    direct = 1
    for mask in range(32):
        term = roots[0]
        for index in range(1, 6):
            term += (-1 if (mask >> (index-1)) & 1 else 1) * roots[index]
        direct *= term
    squared = [root*root for root in roots]
    elementary = []
    for degree in range(1, 7):
        elementary.append(sum(
            sp.prod(squared[index] for index in subset)
            for subset in __import__("itertools").combinations(range(6), degree)
        ))
    evaluated = int(symmetric.subs(dict(zip(s_symbols, elementary))))
    if evaluated != direct:
        raise AssertionError((roots, evaluated, direct))

formula = str(sp.expand(symmetric))
result = {
    "schema": "dli-wcl-ell1-weight6-psi6-formula-v1",
    "status": "COMPLETE",
    "formula": formula,
    "formula_sha256": hashlib.sha256((formula + "\n").encode()).hexdigest(),
    "elementary_terms": len(s_poly.terms()),
    "elementary_total_degree": s_poly.total_degree(),
    "elementary_weighted_degree": max(
        sum((index+1)*power for index,power in enumerate(monomial))
        for monomial, coefficient in s_poly.terms()
    ),
    "coefficient_max_bits": max(abs(int(coefficient)).bit_length() for monomial, coefficient in s_poly.terms()),
    "stages": stages,
    "evaluation_controls": 3,
    "seconds": round(time.monotonic() - started, 6),
}
print("RESULT " + json.dumps(result, sort_keys=True), flush=True)
'''

app = modal.App("rs-mca-wcl16-psi6-formula")
image = modal.Image.debian_slim().pip_install("sympy==1.14.0")


@app.function(image=image, cpu=2, memory=4096, timeout=65, max_containers=1)
def compute() -> dict[str, object]:
    try:
        process = subprocess.run(
            [sys.executable, "-c", PROGRAM],
            capture_output=True,
            text=True,
            timeout=55,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        return {
            "schema": "dli-wcl-ell1-weight6-psi6-formula-v1",
            "status": "TIMEOUT",
            "stage_lines": [line for line in stdout.splitlines() if line.startswith("STAGE ")],
        }
    if process.returncode:
        return {
            "schema": "dli-wcl-ell1-weight6-psi6-formula-v1",
            "status": "ERROR",
            "returncode": process.returncode,
            "stdout_tail": process.stdout[-4000:],
            "stderr_tail": process.stderr[-4000:],
        }
    rows = [line[7:] for line in process.stdout.splitlines() if line.startswith("RESULT ")]
    if len(rows) != 1:
        raise AssertionError(process.stdout[-4000:])
    return json.loads(rows[0])


@app.local_entrypoint()
def main() -> None:
    result = compute.remote()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "DLI_WCL_ELL1_WEIGHT6_PSI6_FORMULA "
        f"status={result['status']} terms={result.get('elementary_terms')} "
        f"seconds={result.get('seconds')}"
    )
