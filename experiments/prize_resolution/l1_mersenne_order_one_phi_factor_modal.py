#!/usr/bin/env python3
"""Cheap exact factorization probe for the order-one HNF curve.

The worker constructs h! times

    Phi_h(rho,c) = [t^h] (1-t)^(c rho) (1-ct)^(-rho)

over ZZ and factors it over QQ.  The h=7 result is printed before h=15 is
started, so a worker timeout still leaves the smallest official chamber.
"""

from __future__ import annotations

import hashlib
import json
import resource
import time

import modal


APP_NAME = "l1-mersenne-order-one-phi-factor"

app = modal.App(APP_NAME)
image = modal.Image.debian_slim(python_version="3.12").pip_install(
    "sympy==1.14.0"
)


@app.function(image=image, cpu=1, memory=1024, timeout=180, max_containers=1)
def factor_curves() -> dict[str, object]:
    import sympy as sp

    rho, c = sp.symbols("rho c")
    started = time.monotonic()
    rows: list[dict[str, object]] = []

    for h in (7, 15):
        coefficients_left = [sp.Integer(1)]
        coefficients_right = [sp.Integer(1)]
        falling = sp.Integer(1)
        rising = sp.Integer(1)
        for degree in range(1, h + 1):
            falling *= c * rho - (degree - 1)
            rising *= rho + (degree - 1)
            coefficients_left.append((-1) ** degree * falling / sp.factorial(degree))
            coefficients_right.append(c**degree * rising / sp.factorial(degree))

        phi = sum(
            coefficients_left[index] * coefficients_right[h - index]
            for index in range(h + 1)
        )
        integral = sp.Poly(sp.expand(sp.factorial(h) * phi), rho, c, domain=sp.ZZ)
        content, factors = sp.factor_list(integral.as_expr(), rho, c)
        factor_rows = []
        reconstructed = sp.Integer(content)
        for factor, multiplicity in factors:
            factor_poly = sp.Poly(factor, rho, c, domain=sp.ZZ)
            text = str(factor_poly.as_expr())
            factor_rows.append(
                {
                    "multiplicity": multiplicity,
                    "total_degree": factor_poly.total_degree(),
                    "rho_degree": factor_poly.degree(rho),
                    "c_degree": factor_poly.degree(c),
                    "terms": len(factor_poly.terms()),
                    "sha256": hashlib.sha256(text.encode()).hexdigest(),
                    "text": text,
                }
            )
            reconstructed *= factor**multiplicity

        assert sp.Poly(sp.expand(reconstructed), rho, c, domain=sp.ZZ) == integral
        row = {
            "h": h,
            "content": int(content),
            "total_degree": integral.total_degree(),
            "rho_degree": integral.degree(rho),
            "c_degree": integral.degree(c),
            "terms": len(integral.terms()),
            "factors": factor_rows,
            "seconds_cumulative": round(time.monotonic() - started, 6),
        }
        rows.append(row)
        print("L1_ORDER_ONE_PHI_STAGE " + json.dumps(row, sort_keys=True), flush=True)

    result = {
        "app": APP_NAME,
        "status": "COMPLETE",
        "rows": rows,
        "seconds": round(time.monotonic() - started, 6),
        "peak_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024,
    }
    print("L1_ORDER_ONE_PHI_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    return result


@app.local_entrypoint()
def main() -> None:
    print(json.dumps(factor_curves.remote(), indent=2, sort_keys=True))
