#!/usr/bin/env python3
"""Capped route pilot for the WCL (ell,w)=(1,5) unit ideal.

Decision
--------
Measure the exact three-variable remainder growth and test whether a modular
Groebner basis can certify the unit ideal inside one 60-second container.

PASS: all eight quotient squarings finish and a modular basis is `[1]`.
This authorizes a separate, costed multi-prime rational-reconstruction job;
it is not a characteristic-zero or integer Nullstellensatz certificate.

FAIL: a nonunit modular basis is a candidate bad characteristic and must be
checked for an actual divisor point. Timeout or memory failure only route the
certificate to a stronger CAS. Checkpoint lines preserve completed squarings
and coefficient statistics.

Resources: one CPU, 2 GiB, one container, hard timeout 60 seconds. Expected
cost is well below $0.10. No larger WCL ideal is attempted.

Run `ap-gWA4UOyBSv4c8C4tqDVd84` established the exact-expansion route fence:
it reached exponent 64, with up to 3,212 terms in one coefficient, and timed
out while forming exponent 128. The default entrypoint therefore runs the
modular-coefficient variant below. The exact function remains for replay.
"""

from __future__ import annotations

import json
import time

import modal


APP_NAME = "dli-wcl-15-unit-ideal-pilot"
MODULUS = 65537

app = modal.App(APP_NAME)
image = modal.Image.debian_slim(python_version="3.12").pip_install(
    "sympy==1.13.3"
)


@app.function(
    image=image,
    cpu=1,
    memory=2048,
    timeout=60,
    max_containers=1,
)
def pilot() -> dict[str, object]:
    import sympy as sp

    began = time.monotonic()
    y, c0, c1, b = sp.symbols("y c0 c1 b")
    domain = sp.ZZ.poly_ring(c0, c1, b)
    A = y**2 + c1 * y + c0
    G = sp.Poly(sp.expand(y * A**2 - (b * y + 1) ** 2), y, domain=domain)
    value = sp.Poly(y, y, domain=domain)
    checkpoints: list[dict[str, object]] = []

    for index in range(1, 9):
        value = (value * value).rem(G)
        coefficient_stats = []
        for coefficient in value.all_coeffs():
            poly = sp.Poly(coefficient, c0, c1, b, domain=sp.ZZ)
            coefficient_stats.append(
                {
                    "terms": len(poly.terms()),
                    "degree": poly.total_degree(),
                    "max_coeff_bits": max(
                        (abs(int(item)).bit_length() for item in poly.coeffs()),
                        default=0,
                    ),
                }
            )
        checkpoint = {
            "squaring": index,
            "exponent": 1 << index,
            "degree_y": value.degree(),
            "coefficient_stats": coefficient_stats,
            "seconds": time.monotonic() - began,
        }
        checkpoints.append(checkpoint)
        print("WCL15_CHECKPOINT " + json.dumps(checkpoint, sort_keys=True), flush=True)
        if index < 8 and max(item["terms"] for item in coefficient_stats) > 2500:
            return {
                "app": APP_NAME,
                "decision": "wcl_15_modular_unit_ideal_route",
                "representation": "ZZ[c0,c1,b][y]/(G)",
                "complete": False,
                "route_fence": "coefficient_term_wall_before_exponent_256",
                "squarings_complete": index,
                "checkpoints": checkpoints,
                "unit_ideal_mod_p": None,
                "seconds": time.monotonic() - began,
            }

    remainder = value - sp.Poly(1, y, domain=domain)
    coefficients = [sp.expand(remainder.nth(index).as_expr()) for index in range(5)]
    summary = {
        "remainder_terms": [
            len(sp.Poly(item, c0, c1, b, domain=sp.ZZ).terms())
            for item in coefficients
        ],
        "remainder_degrees": [
            sp.Poly(item, c0, c1, b, domain=sp.ZZ).total_degree()
            for item in coefficients
        ],
        "seconds": time.monotonic() - began,
    }
    print("WCL15_REMAINDER " + json.dumps(summary, sort_keys=True), flush=True)

    groebner_began = time.monotonic()
    basis = sp.groebner(
        coefficients,
        c0,
        c1,
        b,
        modulus=MODULUS,
        order="grevlex",
        method="f5b",
    )
    is_unit = len(basis.polys) == 1 and basis.polys[0].as_expr() == 1
    result = {
        "app": APP_NAME,
        "decision": "wcl_15_modular_unit_ideal_route",
        "modulus": MODULUS,
        "squarings_complete": len(checkpoints),
        "checkpoints": checkpoints,
        "remainder": summary,
        "basis_size": len(basis.polys),
        "basis_degrees": [poly.total_degree() for poly in basis.polys[:32]],
        "unit_ideal_mod_p": is_unit,
        "groebner_seconds": time.monotonic() - groebner_began,
        "seconds": time.monotonic() - began,
    }
    print("WCL15_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    return result


@app.function(
    image=image,
    cpu=1,
    memory=2048,
    timeout=60,
    max_containers=1,
)
def pilot_modular() -> dict[str, object]:
    import sympy as sp
    from sympy.polys.domains import GF
    from sympy.polys.rings import ring

    began = time.monotonic()
    coefficient_ring, c0, c1, b = ring("c0,c1,b", GF(MODULUS))
    c0_symbol, c1_symbol, b_symbol = sp.symbols("c0 c1 b")
    zero = coefficient_ring.zero
    one = coefficient_ring.one

    # G=Y*A^2-(bY+1)^2, low coefficients through Y^4. The Y^5
    # coefficient is one, so quotient reduction needs no division.
    g_low = [
        -one,
        c0**2 - 2 * b,
        2 * c0 * c1 - b**2,
        c1**2 + 2 * c0,
        2 * c1,
    ]

    def multiply_reduce(left, right):
        raw = [zero] * (len(left) + len(right) - 1)
        for i, left_coefficient in enumerate(left):
            if not left_coefficient:
                continue
            for j, right_coefficient in enumerate(right):
                if right_coefficient:
                    raw[i + j] += left_coefficient * right_coefficient
        for degree in range(len(raw) - 1, 4, -1):
            leading = raw[degree]
            if not leading:
                continue
            shift = degree - 5
            for j, coefficient in enumerate(g_low):
                raw[shift + j] -= leading * coefficient
            raw[degree] = zero
        return raw[:5]

    def total_degree(poly):
        return max((sum(monomial) for monomial, _ in poly.iterterms()), default=0)

    value = [zero, one]
    checkpoints: list[dict[str, object]] = []

    for index in range(1, 9):
        value = multiply_reduce(value, value)
        coefficient_stats = []
        for coefficient in value:
            coefficient_stats.append(
                {"terms": len(coefficient), "degree": total_degree(coefficient)}
            )
        checkpoint = {
            "squaring": index,
            "exponent": 1 << index,
            "degree_y": max(
                (j for j, coefficient in enumerate(value) if coefficient),
                default=-1,
            ),
            "coefficient_stats": coefficient_stats,
            "seconds": time.monotonic() - began,
        }
        checkpoints.append(checkpoint)
        print(
            "WCL15_MOD_CHECKPOINT " + json.dumps(checkpoint, sort_keys=True),
            flush=True,
        )
        if index < 8 and max(item["terms"] for item in coefficient_stats) > 2500:
            return {
                "app": APP_NAME,
                "decision": "wcl_15_modular_unit_ideal_route",
                "representation": "GF(p)[c0,c1,b][y]/(G)",
                "modulus": MODULUS,
                "complete": False,
                "route_fence": "coefficient_term_wall_before_exponent_256",
                "squarings_complete": index,
                "checkpoints": checkpoints,
                "unit_ideal_mod_p": None,
                "seconds": time.monotonic() - began,
            }

    value[0] -= one
    coefficients = [coefficient.as_expr() for coefficient in value]
    summary = {
        "remainder_terms": [len(item) for item in value],
        "remainder_degrees": [total_degree(item) for item in value],
        "seconds": time.monotonic() - began,
    }
    print("WCL15_MOD_REMAINDER " + json.dumps(summary, sort_keys=True), flush=True)

    groebner_began = time.monotonic()
    basis = sp.groebner(
        coefficients,
        c0_symbol,
        c1_symbol,
        b_symbol,
        modulus=MODULUS,
        order="grevlex",
        method="f5b",
    )
    is_unit = len(basis.polys) == 1 and basis.polys[0].as_expr() == 1
    result = {
        "app": APP_NAME,
        "decision": "wcl_15_modular_unit_ideal_route",
        "representation": "GF(p)[c0,c1,b][y]/(G)",
        "modulus": MODULUS,
        "squarings_complete": len(checkpoints),
        "checkpoints": checkpoints,
        "remainder": summary,
        "basis_size": len(basis.polys),
        "basis_degrees": [poly.total_degree() for poly in basis.polys[:32]],
        "unit_ideal_mod_p": is_unit,
        "groebner_seconds": time.monotonic() - groebner_began,
        "seconds": time.monotonic() - began,
    }
    print("WCL15_MOD_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    return result


@app.local_entrypoint()
def main() -> None:
    result = pilot_modular.remote()
    print(json.dumps(result, indent=2, sort_keys=True))
    print(
        "DLI_WCL_15_UNIT_IDEAL_PILOT "
        f"squarings={result['squarings_complete']} "
        f"unit_mod_p={result['unit_ideal_mod_p']} "
        f"seconds={result['seconds']:.3f}"
    )
