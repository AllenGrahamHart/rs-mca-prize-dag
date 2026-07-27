#!/usr/bin/env python3
"""Bounded exact profile of the m=8 order-one reciprocal system.

This is a route-pricing worker.  It constructs the residual hypergeometric
curve, the degree-six reduced mth-power resultant, and the first three
reciprocal equations.  It then performs only sequential univariate
elimination (rho_star, then rho) and reports every completed stage.
"""

from __future__ import annotations

import hashlib
import json
import resource
import time

import modal


APP_NAME = "l1-mersenne-m8-order-one-reciprocal-profile"
H = 7
M = 8

app = modal.App(APP_NAME)
image = modal.Image.debian_slim(python_version="3.12").pip_install(
    "sympy==1.14.0"
)


def profile(poly, variables) -> dict[str, object]:
    import sympy as sp

    value = sp.Poly(poly, *variables, domain=sp.QQ)
    text = str(value.as_expr())
    return {
        "total_degree": value.total_degree(),
        "degrees": {str(variable): value.degree(variable) for variable in variables},
        "terms": len(value.terms()),
        "bytes": len(text.encode()),
        "sha256": hashlib.sha256(text.encode()).hexdigest(),
    }


@app.function(image=image, cpu=1, memory=2048, timeout=180, max_containers=1)
def run_profile() -> dict[str, object]:
    import sympy as sp

    rho, rho_star, c, zeta, w, z, y = sp.symbols(
        "rho rho_star c zeta w z y"
    )
    started = time.monotonic()
    stages: dict[str, object] = {}

    def emit(name: str, payload: object) -> None:
        stages[name] = payload
        print(
            "L1_M8_ORDER_ONE_PROFILE_STAGE "
            + json.dumps({"stage": name, "payload": payload}, sort_keys=True),
            flush=True,
        )

    def falling(value, degree):
        out = sp.Integer(1)
        for index in range(degree):
            out *= value - index
        return out / sp.factorial(degree)

    def rising(value, degree):
        out = sp.Integer(1)
        for index in range(degree):
            out *= value + index
        return out / sp.factorial(degree)

    def u_coefficient(degree, rho_value, c_value):
        return sp.expand(
            sum(
                (-1) ** index
                * falling(c_value * rho_value, index)
                * c_value ** (degree - index)
                * rising(rho_value, degree - index)
                for index in range(degree + 1)
            )
        )

    coefficients = [u_coefficient(index, rho, c) for index in range(H + 1)]
    phi = coefficients[H]
    d = c - 1
    psi = sp.cancel(sp.factorial(H) * phi / (6 * rho * c * d * (c + 1)))
    assert sp.denom(psi) == 1
    emit("psi", profile(psi, (rho, c)))

    g = sum(coefficients[index] * y ** (H - index) for index in range(H + 1))
    p_expr = sp.cancel(g.subs(y, 1 + d * w) / d**H)
    p_coefficients = [sp.cancel(value) for value in sp.Poly(p_expr, w).all_coeffs()]
    assert len(p_coefficients) == H + 1 and p_coefficients[0] == 1

    root = -1 / d
    quotient_coefficients = [sp.Integer(1)]
    for index in range(1, H):
        quotient_coefficients.append(
            sp.cancel(p_coefficients[index] + root * quotient_coefficients[-1])
        )
    remainder = sp.cancel(p_coefficients[-1] + root * quotient_coefficients[-1])
    assert sp.cancel(remainder - phi / d**H) == 0
    ell = sp.cancel(sum(
        quotient_coefficients[index] * w ** (H - 1 - index)
        for index in range(H)
    ))
    ell_numerator, ell_denominator = sp.together(ell).as_numer_denom()
    emit(
        "ell",
        {
            "numerator": profile(ell_numerator, (w, rho, c)),
            "denominator": str(sp.factor(ell_denominator)),
        },
    )

    q_tilde = sp.cancel(sp.resultant(ell, z - w**M, w))
    q_coefficients = [sp.cancel(value) for value in sp.Poly(q_tilde, z).all_coeffs()]
    assert len(q_coefficients) == H and q_coefficients[0] == 1
    emit(
        "q_tilde_coefficients",
        [
            {
                "index": index,
                "numerator": profile(sp.together(value).as_numer_denom()[0], (rho, c)),
                "denominator": str(sp.factor(sp.together(value).as_numer_denom()[1])),
            }
            for index, value in enumerate(q_coefficients)
        ],
    )

    c_star = 1 + zeta / d
    psi_star = sp.cancel(psi.subs({rho: rho_star, c: c_star}, simultaneous=True))
    psi_star_numerator = sp.Poly(
        sp.together(psi_star).as_numer_denom()[0], rho_star, c, zeta, domain=sp.QQ
    ).as_expr()
    emit("psi_star", profile(psi_star_numerator, (rho_star, c, zeta)))

    constant = q_coefficients[-1]
    equations = []
    for index in (1, 2, 3):
        starred = q_coefficients[index].subs(
            {rho: rho_star, c: c_star}, simultaneous=True
        )
        expression = sp.cancel(constant * starred - q_coefficients[H - 1 - index])
        numerator = sp.Poly(
            sp.together(expression).as_numer_denom()[0],
            rho_star,
            rho,
            c,
            zeta,
            domain=sp.QQ,
        ).as_expr()
        equations.append(numerator)
        emit(f"F{index}", profile(numerator, (rho_star, rho, c, zeta)))

    psi_poly = sp.Poly(psi, rho, c, domain=sp.QQ).as_expr()
    projections = []
    for index, equation in enumerate(equations, start=1):
        first = sp.resultant(psi_star_numerator, equation, rho_star)
        first = sp.Poly(first, rho, c, zeta, domain=sp.QQ).primitive()[1].as_expr()
        emit(f"E{index}_after_rho_star", profile(first, (rho, c, zeta)))
        second = sp.resultant(psi_poly, first, rho)
        second = sp.Poly(second, c, zeta, domain=sp.QQ).primitive()[1].as_expr()
        projections.append(second)
        emit(f"R{index}_after_rho", profile(second, (c, zeta)))

    cyclotomic = zeta**M - 1
    reduced = [sp.rem(value, cyclotomic, zeta) for value in projections]
    for index, value in enumerate(reduced, start=1):
        emit(f"R{index}_mod_zeta8", profile(value, (c, zeta)))

    basis = sp.groebner([cyclotomic, *reduced], zeta, c, order="lex", domain=sp.QQ)
    basis_rows = [profile(value, (zeta, c)) for value in basis.polys]
    emit(
        "projected_basis",
        {
            "unit": len(basis.polys) == 1 and basis.polys[0].as_expr() == 1,
            "size": len(basis.polys),
            "polynomials": basis_rows,
        },
    )

    result = {
        "app": APP_NAME,
        "status": "COMPLETE",
        "h": H,
        "m": M,
        "stages": stages,
        "seconds": round(time.monotonic() - started, 6),
        "peak_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024,
    }
    print("L1_M8_ORDER_ONE_PROFILE_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    return result


@app.local_entrypoint()
def main() -> None:
    print(json.dumps(run_profile.remote(), indent=2, sort_keys=True))
