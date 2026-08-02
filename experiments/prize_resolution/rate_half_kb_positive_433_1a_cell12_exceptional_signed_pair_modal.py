#!/usr/bin/env python3
"""Replay the raw cell-12 signed pair on the proper exceptional common fiber."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
CHARTS = DIRECTORY / "rate_half_kb_positive_433_1a_cell12_exceptional_common_charts_result.json"
PROBE = DIRECTORY / "rate_half_kb_positive_433_1a_outside_edge_specialization_probe.py"
BASE = DIRECTORY / "rate_half_kb_positive_433_1a_product_base_rank_compiler.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell12_exceptional_signed_pair_result.json"
REMOTE_CHARTS = "/root/cell12_exceptional_common_charts.json"
REMOTE_PROBE = "/root/rate_half_kb_positive_433_1a_outside_edge_specialization_probe.py"
REMOTE_BASE = "/root/rate_half_kb_positive_433_1a_product_base_rank_compiler.py"
PRIME = 2130706433
T_VALUE = 1117681606

app = modal.App("rs-mca-positive-433-1a-cell12-exceptional-signed-pair")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0", "python-flint==0.8.0")
    .add_local_file(CHARTS, REMOTE_CHARTS)
    .add_local_file(PROBE, REMOTE_PROBE)
    .add_local_file(BASE, REMOTE_BASE)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=180)
def replay():
    import sys

    from flint import fmpz_mod_mpoly_ctx, fmpz_mod_poly_ctx
    import sympy as sp

    sys.path.insert(0, "/root")
    from rate_half_kb_positive_433_1a_outside_edge_specialization_probe import (
        common_kernel,
    )

    chart_bytes = Path(REMOTE_CHARTS).read_bytes()
    chart_payload = json.loads(chart_bytes)
    chart = next(row for row in chart_payload["rows"] if row["t"] == T_VALUE)
    expected_basis = (
        "G[1]=t+1013024827\n"
        "G[2]=r-558459069\n"
        "G[3]=c+40350282b-460157884\n"
        "G[4]=b2-9674473b+1\n"
        "G[5]=u-804018985b+98948155"
    )
    if chart["unit"] or expected_basis not in chart["stdout"]:
        raise RuntimeError("unexpected exceptional common chart")

    scalar_context = fmpz_mod_poly_ctx(PRIME)
    b_polynomial = scalar_context([1, -9674473, 1])
    content, b_factors = b_polynomial.factor()
    reconstruction = scalar_context([int(content)])
    b_roots = []
    for factor, multiplicity in b_factors:
        reconstruction *= factor**multiplicity
        if int(factor.degree()) == 1:
            b_roots.append(
                (-int(factor[0]) * pow(int(factor[1]), -1, PRIME)) % PRIME
            )
    if reconstruction != b_polynomial or len(b_roots) != 2:
        raise RuntimeError("exceptional b factorization")
    b_roots.sort()

    a2, a0, b1, _, _ = common_kernel(12, -1, -1)
    b, c, r, t = sp.symbols("b c r t")
    pair_context = fmpz_mod_mpoly_ctx.get(["w1", "w0"], PRIME)
    w1, w0 = pair_context.gens()

    def evaluate(expression, values):
        value = sp.Poly(expression.subs(values), b, c, r, t,
                        modulus=PRIME).as_expr()
        if value.free_symbols:
            raise RuntimeError(f"nonconstant specialization: {value}")
        return int(value) % PRIME

    def shape(polynomial):
        return {
            "degrees": [int(value) for value in polynomial.degrees()],
            "total_degree": int(polynomial.total_degree()),
            "terms": len(list(polynomial.terms())),
        }

    rows = []
    all_guarded = True
    for b_value in b_roots:
        r_value = 558459069
        c_value = (460157884 - 40350282 * b_value) % PRIME
        values = {b: b_value, c: c_value, r: r_value, t: T_VALUE}
        a2_values = [evaluate(expression, values) for expression in a2]
        a0_values = [evaluate(expression, values) for expression in a0]
        b1_values = [evaluate(expression, values) for expression in b1]
        if not any(a2_values + a0_values + b1_values):
            raise RuntimeError("zero common kernel")
        if (b1_values[0] + b1_values[1]) % PRIME:
            raise RuntimeError("B1 opposition failed")

        def form(values, variable):
            return sum(values[index] * variable**index for index in range(3))

        d0, d1 = form(a2_values, w0), form(a2_values, w1)
        n0, n1 = form(a0_values, w0), form(a0_values, w1)
        k = b1_values[0]
        product = n1 * d0 + n0 * d1
        square = (
            k * k * w0 * (1 - w0) * (1 - w0) * d1 * d1
            - k * k * w1 * (1 - w1) * (1 - w1) * d0 * d0
            - 4 * n0 * d0 * d1 * d1
        )
        resultant = product.resultant(square, "w1")
        if resultant.is_zero():
            raise RuntimeError("raw signed-pair resultant is zero")
        known = {
            "N0": n0,
            "D0": d0,
            "w0+1": w0 + 1,
            "w0-r^2": w0 - r_value * r_value,
            "w0+r^2": w0 + r_value * r_value,
            "w0-t^2": w0 - T_VALUE * T_VALUE,
            "w0+t^2": w0 + T_VALUE * T_VALUE,
        }
        factor_content, factors = resultant.factor()
        reconstruction = pair_context.constant(int(factor_content))
        factor_rows = []
        for factor, multiplicity in factors:
            reconstruction *= factor**multiplicity
            owners = []
            for name, polynomial in known.items():
                _, remainder = divmod(polynomial, factor)
                if remainder.is_zero():
                    owners.append(name)
            degree = int(factor.degrees()[1])
            if degree == 1 and not owners:
                all_guarded = False
            factor_rows.append({
                "degree": degree,
                "multiplicity": int(multiplicity),
                "owners": owners,
                "polynomial": factor.str(),
            })
        if reconstruction != resultant:
            raise RuntimeError("raw resultant reconstruction")
        rows.append({
            "b": b_value, "c": c_value, "r": r_value,
            "kernel": {
                "a2": a2_values, "a0": a0_values, "b1": b1_values,
            },
            "product_shape": shape(product),
            "square_shape": shape(square),
            "resultant_shape": shape(resultant),
            "resultant_sha256": hashlib.sha256(
                resultant.str().encode()
            ).hexdigest(),
            "factors": factor_rows,
            "all_deployed_roots_guarded": all(
                row["degree"] != 1 or row["owners"] for row in factor_rows
            ),
        })
    return {
        "status": "COMPLETE", "field": PRIME, "t": T_VALUE,
        "source_charts_sha256": hashlib.sha256(chart_bytes).hexdigest(),
        "b_polynomial": b_polynomial.str(), "b_roots": b_roots,
        "rows": rows, "all_deployed_roots_guarded": all_guarded,
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell12-exceptional-signed-pair-v1",
        "scope": (
            "Exact unnormalized common-kernel and complete signed-pair "
            "resultant replay at every deployed point of the sole proper "
            "cell-12 exceptional scale fiber; no orbit or Prize claim."
        ),
        "result": replay.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    result = output["result"]
    print(json.dumps({
        "result": str(RESULT), "status": result["status"],
        "t": result["t"], "b_roots": result["b_roots"],
        "all_deployed_roots_guarded": result["all_deployed_roots_guarded"],
        "rows": [
            {
                "b": row["b"], "c": row["c"],
                "resultant_shape": row["resultant_shape"],
                "factors": row["factors"],
                "all_deployed_roots_guarded": row["all_deployed_roots_guarded"],
            }
            for row in result["rows"]
        ],
    }, sort_keys=True))
