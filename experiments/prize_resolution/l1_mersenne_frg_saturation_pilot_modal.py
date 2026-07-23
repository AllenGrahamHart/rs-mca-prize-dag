#!/usr/bin/env python3
"""Bounded Modal benchmark for the HNF Frobenius reciprocal saturation."""

import json
import time

import modal


app = modal.App("l1-mersenne-frg-saturation-pilot")
image = modal.Image.debian_slim().pip_install("sympy")


def reduced(expression, generators, p):
    import sympy as sp

    return sp.Poly(expression, *generators, modulus=p).as_expr()


@app.function(image=image, cpu=1.0, memory=2048, timeout=120)
def run_pilot(p: int = 31, m: int = 8):
    import resource
    import sympy as sp

    started = time.monotonic()
    h = m - 1
    s, t, z, w, v = sp.symbols("s t z w v")

    rising = 1
    P = 0
    for r in range(h + 1):
        if r:
            rising = sp.expand(rising * (s + r - 1) * pow(r, -1, p))
        P += rising * w ** (h - r)
    P = reduced(P, (w, s), p)
    print(f"FRG_STAGE polynomial seconds={time.monotonic() - started:.6f}", flush=True)

    Q = sp.resultant(P, z - w ** m, w)
    Q = reduced(Q, (z, s), p)
    q = []
    q_as_z = sp.Poly(Q, z)
    for j in range(h + 1):
        q.append(reduced(q_as_z.coeff_monomial(z ** (h - j)), (s,), p))
    print(f"FRG_STAGE resultant seconds={time.monotonic() - started:.6f}", flush=True)

    C = q[h]
    equations = []
    for j in range(h + 1):
        equation = reduced(C * q[j].subs(s, t) - q[h - j], (s, t), p)
        if equation != 0:
            equations.append(equation)
    saturation_equation = reduced(v * (t - s) - 1, (v, t, s), p)
    equation_degrees = [sp.Poly(eq, s, t, modulus=p).total_degree() for eq in equations]
    print(
        f"FRG_STAGE equations count={len(equations)} max_degree={max(equation_degrees)} "
        f"seconds={time.monotonic() - started:.6f}",
        flush=True,
    )

    basis = sp.groebner(
        equations + [saturation_equation],
        v,
        t,
        s,
        modulus=p,
        order="grevlex",
    )
    basis_expressions = [poly.as_expr() for poly in basis.polys]
    unit = any(expression == 1 for expression in basis_expressions)
    elapsed = time.monotonic() - started
    peak_mb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024
    return {
        "p": p,
        "m": m,
        "h": h,
        "equation_count": len(equations),
        "equation_degrees": equation_degrees,
        "basis_count": len(basis_expressions),
        "basis_degrees": [sp.Poly(expr, v, t, s, modulus=p).total_degree()
                          for expr in basis_expressions],
        "unit_saturation": unit,
        "worker_seconds": round(elapsed, 6),
        "peak_mb": peak_mb,
    }


@app.local_entrypoint()
def main():
    print(json.dumps(run_pilot.remote(), sort_keys=True, separators=(",", ":")))
