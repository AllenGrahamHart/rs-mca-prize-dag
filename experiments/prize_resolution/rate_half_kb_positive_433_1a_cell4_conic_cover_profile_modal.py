#!/usr/bin/env python3
"""Profile the second quadratic cover for positive common cell 4."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
PROFILE = DIRECTORY / "rate_half_kb_positive_433_1a_remaining_palindromic_profile_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_conic_cover_profile_result.json"
REMOTE_PROFILE = "/root/remaining_palindromic_profile.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell4-conic-cover-profile")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(PROFILE, REMOTE_PROFILE)
)


@app.function(image=image, cpu=2.0, memory=2048, timeout=120)
def profile_cover():
    import sympy as sp

    source_bytes = Path(REMOTE_PROFILE).read_bytes()
    source = json.loads(source_bytes)
    payload = next(row for row in source["rows"] if row["cell"] == 4)
    t, x, s = sp.symbols("t x s")
    quotient = sp.Poly(sp.sympify(payload["quotient"]), x, t, modulus=PRIME)
    q_expr = quotient.as_expr()
    a0 = sp.Poly(q_expr.coeff(x, 2), t, modulus=PRIME)
    a1 = sp.Poly(q_expr.coeff(x, 1), t, modulus=PRIME)
    a2 = sp.Poly(q_expr.coeff(x, 0), t, modulus=PRIME)
    discriminant = sp.Poly(a1.as_expr()**2-4*a0.as_expr()*a2.as_expr(),
                           t, modulus=PRIME)

    factorization = payload["discriminant_factorization"]
    square_part = sp.Poly(1, t, modulus=PRIME)
    square_free = sp.Poly(factorization["content"], t, modulus=PRIME)
    for row in factorization["factors"]:
        factor = sp.Poly(sp.sympify(row["polynomial"]), t, modulus=PRIME)
        square_part *= factor**(row["multiplicity"]//2)
        if row["multiplicity"] % 2:
            square_free *= factor
    if sp.Poly(square_part.as_expr()**2*square_free.as_expr(), t,
               modulus=PRIME) != discriminant:
        raise RuntimeError("discriminant decomposition mismatch")

    base_point = None
    for candidate_t in range(1024):
        candidate_square = int(square_free.eval(candidate_t)) % PRIME
        roots = sp.sqrt_mod(candidate_square, PRIME, all_roots=True)
        if roots:
            base_point = (candidate_t, min(int(root) % PRIME for root in roots))
            break
    if base_point is None:
        raise RuntimeError("no small conic point")
    base_t, base_y = base_point
    conic_expression = square_free.as_expr()
    conic_coefficients = square_free.all_coeffs()
    if square_free.degree() != 2:
        raise RuntimeError("square-free quotient is not a conic")
    leading = int(conic_coefficients[0]) % PRIME
    linear = int(conic_coefficients[1]) % PRIME
    # The sum of the two t-intersections of y=y0+s(t-t0) with
    # y^2=leading*t^2+linear*t+constant is rational in s.
    intersection_linear = 2*s*(base_y-s*base_t)-linear
    second_t = sp.cancel(
        -intersection_linear/(s**2-leading)-base_t, modulus=PRIME
    )
    conic_y = sp.cancel(base_y+s*(second_t-base_t), modulus=PRIME)
    if sp.cancel(conic_y**2-conic_expression.subs(t, second_t),
                 modulus=PRIME) != 0:
        raise RuntimeError("conic parametrization mismatch")

    y_discriminant = sp.cancel(
        square_part.as_expr().subs(t, second_t)*conic_y, modulus=PRIME
    )
    x_of_s = sp.cancel(
        (-a1.as_expr().subs(t, second_t)+y_discriminant)
        /(2*a0.as_expr().subs(t, second_t)), modulus=PRIME
    )
    if sp.cancel(q_expr.subs({t: second_t, x: x_of_s}), modulus=PRIME) != 0:
        raise RuntimeError("quotient lift mismatch")

    second_discriminant = sp.cancel(x_of_s**2-4, modulus=PRIME)
    numerator, denominator = sp.fraction(second_discriminant)
    numerator_poly = sp.Poly(numerator, s, modulus=PRIME)
    denominator_poly = sp.Poly(denominator, s, modulus=PRIME)
    num_content, num_factors = sp.factor_list(numerator_poly, modulus=PRIME)
    den_content, den_factors = sp.factor_list(denominator_poly, modulus=PRIME)

    def factor_payload(content, factors):
        return {
            "content": int(content) % PRIME,
            "factors": [
                {"polynomial": str(factor.as_expr()),
                 "degree": factor.degree(), "multiplicity": multiplicity}
                for factor, multiplicity in factors
            ],
        }

    return {
        "status": "COMPLETE",
        "field": PRIME,
        "source_profile_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "conic_base_point": [base_t, base_y],
        "t_of_s": str(second_t),
        "conic_y_of_s": str(conic_y),
        "x_of_s": str(x_of_s),
        "second_discriminant": str(second_discriminant),
        "numerator_shape": {"degree": numerator_poly.degree(),
                            "terms": len(numerator_poly.terms())},
        "denominator_shape": {"degree": denominator_poly.degree(),
                              "terms": len(denominator_poly.terms())},
        "numerator_factorization": factor_payload(num_content, num_factors),
        "denominator_factorization": factor_payload(den_content, den_factors),
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell4-conic-cover-profile-v1",
        "scope": (
            "Exact deployed-field profile of the remaining b-cover for cell "
            "4; no outside, route, K3, or Prize claim."
        ),
        "result": profile_cover.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "status": output["result"].get("status"),
        "base_point": output["result"].get("conic_base_point"),
        "numerator_shape": output["result"].get("numerator_shape"),
        "numerator_factorization": output["result"].get("numerator_factorization"),
        "denominator_factorization": output["result"].get("denominator_factorization"),
    }, sort_keys=True))
