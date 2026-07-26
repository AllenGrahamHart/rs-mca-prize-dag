#!/usr/bin/env python3
"""Classify the anti-reciprocal coefficient stratum of the WCL (4,9) Pell form."""

from __future__ import annotations

import hashlib
import json
import resource
import signal
import time

import modal


APP_NAME = "wcl49-inversion-symmetric-groebner"

app = modal.App(APP_NAME)
image = modal.Image.debian_slim(python_version="3.12").pip_install("sympy==1.14.0")


def equations(sp):
    y, c0, c1, c2, c3 = sp.symbols("y c0 c1 c2 c3")
    variables = (c3, c2, c1, c0)
    a = y**4 + c3 * y**3 + c2 * y**2 + c1 * y + c0
    p = sp.Poly(sp.expand(y * a**2 - 1), y)
    anti = [sp.expand(p.nth(index) + p.nth(9 - index)) for index in range(1, 5)]
    return variables, anti


@app.function(image=image, cpu=1, memory=1024, timeout=90, max_containers=1)
def classify() -> dict[str, object]:
    import sympy as sp

    started = time.monotonic()
    variables, anti = equations(sp)
    equation_text = [str(value) for value in anti]
    base = {
        "app": APP_NAME,
        "domain": "QQ",
        "order": "lex",
        "variables": [str(value) for value in variables],
        "equations": equation_text,
        "equations_sha256": hashlib.sha256("\n".join(equation_text).encode()).hexdigest(),
    }
    print("WCL49_INV_INPUT " + json.dumps(base, sort_keys=True), flush=True)

    def alarm_handler(_signum, _frame):
        raise TimeoutError("75-second symbolic classification alarm")

    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(75)
    try:
        basis = sp.groebner(anti, *variables, order="lex", domain=sp.QQ)
        basis_text = [str(poly.as_expr()) for poly in basis.polys]
        univariate_factors = {
            value: str(sp.factor(sp.sympify(value)))
            for value in basis_text
            if len(sp.sympify(value).free_symbols) == 1
        }
        result = {
            **base,
            "status": "COMPLETE",
            "seconds": round(time.monotonic() - started, 6),
            "peak_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024,
            "zero_dimensional": bool(basis.is_zero_dimensional),
            "basis_polynomials": basis_text,
            "basis_sha256": hashlib.sha256("\n".join(basis_text).encode()).hexdigest(),
            "univariate_factors": univariate_factors,
        }
    except TimeoutError as error:
        result = {
            **base,
            "status": "TIMEOUT",
            "seconds": round(time.monotonic() - started, 6),
            "peak_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024,
            "checkpoint": "equations_constructed",
            "error": str(error),
        }
    finally:
        signal.alarm(0)

    print("WCL49_INV_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    return result


@app.local_entrypoint()
def main() -> None:
    print(json.dumps(classify.remote(), indent=2, sort_keys=True))
