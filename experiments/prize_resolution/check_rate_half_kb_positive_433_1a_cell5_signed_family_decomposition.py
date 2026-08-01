#!/usr/bin/env python3
"""Audit the scoped cell-5 finite-algebra telemetry."""

import json
from pathlib import Path

import sympy as sp


DIRECTORY = Path(__file__).parent
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_signed_family_decomposition_result.json"
)
LAUNCHER = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_signed_family_decomposition_modal.py"
)
COMMON = DIRECTORY / "rate_half_kb_positive_433_1a_common_vieta_compiler.py"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    payload = json.loads(RESULT.read_text())
    field = payload["probe_field"]
    prime = field["prime"]
    iota = field["iota"]
    require((iota * iota + 1) % prime == 0, "probe iota")

    component = payload["generic_component"]
    require(component["dimension"] == 0, "generic dimension")
    require(component["basis_size"] == 6, "generic basis")
    require(component["vector_dimension"] == 4, "generic degree")
    require(component["component_count"] == 1, "component count")

    algebra = payload["lex_finite_algebra"]
    require(algebra["basis_size"] == 3, "lex basis")
    require(algebra["primitive_degree"] == 4, "primitive degree")
    require(algebra["reciprocal_check"], "reciprocal check")
    require(algebra["quadratic_trace_lift_check"], "trace lift")

    pair = payload["finite_pair"]
    require(
        pair["cut_degree_terms"] == [[9, 24], [8, 32], [9, 24], [8, 32]],
        "finite-pair cuts",
    )
    require(pair["status"] == "TIMEOUT", "finite-pair status")
    require(pair["timeout_seconds"] == 240, "finite-pair cap")

    boundary = payload["deployed_backend_boundary"]
    require(boundary["affine_basis_size"] == 12, "deployed affine basis")
    require("2^29" in boundary["reason"], "backend fence")

    deployed = payload["deployed_trace_quadratic"]
    p = 2130706433
    i = 16711679
    b, t = sp.symbols("b t")
    a0 = t**4 - 2*i*t**3 - 4*i*t**2 - 2*i*t - 1
    a1 = -8*i*(t**4 + 1)
    a2 = -2*t**4 + 4*i*t**3 - 24*i*t**2 + 4*i*t + 2
    polynomial = sp.Poly(
        a0*(b**4 + 1) + a1*(b**3 + b) + a2*b**2,
        b, t, modulus=p,
    )
    require(polynomial.total_degree() == 8, "deployed total degree")
    require(len(polynomial.terms()) == 19, "deployed terms")
    require(deployed["elimination_generator_count"] == 1, "elimination count")
    require(deployed["reciprocal_check"], "deployed reciprocal")
    require(deployed["quadratic_trace_lift_check"], "deployed trace lift")

    u = sp.symbols("u")
    trace_quadratic = a0*u**2 + a1*u + (a2 - 2*a0)
    lifted = sp.together(b**2 * trace_quadratic.subs(u, b + 1/b))
    require(
        sp.Poly(lifted - polynomial.as_expr(), b, t, modulus=p).is_zero,
        "fraction-free trace lift",
    )
    discriminant = sp.expand(a1**2 - 4*a0*(a2 - 2*a0))
    expected_discriminant = sp.expand(
        -48*(t-i)**2*(t+i)**4*(t**2 - 2*i*pow(3, -1, p)*t - 1)
    )
    require(
        sp.Poly(
            discriminant - expected_discriminant, t, modulus=p
        ).is_zero,
        "deployed discriminant",
    )

    launcher = LAUNCHER.read_text()
    common = COMMON.read_text()
    for token in (
        "prime=characteristic",
        "iota=iota",
        "reciprocal4-bpoly==0",
        "quadratic_lift-bpoly==0",
        "DEPLOYED_BPOLY",
        'timeout = 240 if method == "finite-pair" else 120',
    ):
        require(token in launcher, f"launcher token: {token}")
    require("prime=PRIME" in common and "iota=IOTA" in common, "compiler API")

    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_FINITE_ALGEBRA_PASS "
        "deployed_trace=quadratic probe=65521 degree=4 components=1 "
        "cuts=24/32"
    )


if __name__ == "__main__":
    main()
