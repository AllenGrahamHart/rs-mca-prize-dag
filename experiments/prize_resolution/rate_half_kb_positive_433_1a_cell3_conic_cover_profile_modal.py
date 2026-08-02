#!/usr/bin/env python3
"""Profile the second quadratic cover after parametrizing cell 3's conic."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
PROFILE = DIRECTORY / "rate_half_kb_positive_433_1a_cell3_palindromic_profile_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell3_conic_cover_profile_result.json"
REMOTE_PROFILE = "/root/cell3_palindromic_profile.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell3-conic-cover-profile")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(PROFILE, REMOTE_PROFILE)
)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


@app.function(image=image, cpu=2.0, memory=2048, timeout=180)
def profile_cover():
    import sympy as sp

    payload = json.loads(Path(REMOTE_PROFILE).read_text())["result"]
    t, x, s = sp.symbols("t x s")
    quotient = sp.Poly(sp.sympify(payload["quotient"]), x, t,
                       modulus=PRIME)
    q_expr = quotient.as_expr()
    a0 = sp.Poly(q_expr.coeff(x, 2), t, modulus=PRIME)
    a1 = sp.Poly(q_expr.coeff(x, 1), t, modulus=PRIME)
    a2 = sp.Poly(q_expr.coeff(x, 0), t, modulus=PRIME)
    discriminant = sp.Poly(a1.as_expr()**2 - 4*a0.as_expr()*a2.as_expr(),
                           t, modulus=PRIME)

    root_1 = (-510119941) % PRIME
    root_2 = (-899209895) % PRIME
    square_part = sp.Poly(
        (t + 16711679) * (t - 16711679)**2, t, modulus=PRIME,
    )
    square_free = sp.Poly(48*(t-root_1)*(t-root_2), t, modulus=PRIME)
    expected_discriminant = sp.Poly(
        square_part.as_expr()**2 * square_free.as_expr(),
        t, modulus=PRIME,
    )
    if expected_discriminant != discriminant:
        raise RuntimeError("discriminant decomposition mismatch")

    base_point = None
    for candidate_t in range(1024):
        candidate_square = (
            48*(candidate_t-root_1)*(candidate_t-root_2)
        ) % PRIME
        roots = sp.sqrt_mod(candidate_square, PRIME, all_roots=True)
        if roots:
            base_point = (candidate_t, min(int(root) % PRIME for root in roots))
            break
    if base_point is None:
        raise RuntimeError("no small deployed-field conic point")
    base_t, base_y = base_point
    denominator_t = s**2 - 48
    numerator_t = (
        base_t*(s**2 + 48) - 2*s*base_y
        - 48*(root_1 + root_2)
    )
    t_of_s = sp.cancel(numerator_t / denominator_t, modulus=PRIME)
    conic_y = sp.cancel(base_y + s*(t_of_s-base_t), modulus=PRIME)
    conic_check = sp.cancel(
        conic_y**2 - 48*(t_of_s-root_1)*(t_of_s-root_2),
        modulus=PRIME,
    )
    if conic_check != 0:
        raise RuntimeError("conic parametrization mismatch")

    y_discriminant = sp.cancel(
        square_part.as_expr().subs(t, t_of_s) * conic_y,
        modulus=PRIME,
    )
    x_of_s = sp.cancel(
        (-a1.as_expr().subs(t, t_of_s) + y_discriminant)
        / (2*a0.as_expr().subs(t, t_of_s)),
        modulus=PRIME,
    )
    quotient_check = sp.cancel(
        q_expr.subs({t: t_of_s, x: x_of_s}), modulus=PRIME,
    )
    if quotient_check != 0:
        raise RuntimeError("quotient lift mismatch")

    second_discriminant = sp.cancel(x_of_s**2 - 4, modulus=PRIME)
    numerator, denominator = sp.fraction(second_discriminant)
    numerator_poly = sp.Poly(numerator, s, modulus=PRIME)
    denominator_poly = sp.Poly(denominator, s, modulus=PRIME)
    num_content, num_factors = sp.factor_list(numerator_poly, modulus=PRIME)
    den_content, den_factors = sp.factor_list(denominator_poly, modulus=PRIME)

    def factor_payload(content, factors):
        return {
            "content": int(content) % PRIME,
            "factors": [
                {
                    "polynomial": str(factor.as_expr()),
                    "degree": factor.degree(),
                    "multiplicity": multiplicity,
                }
                for factor, multiplicity in factors
            ],
        }

    return {
        "status": "COMPLETE",
        "field": PRIME,
        "source_profile_sha256": hashlib.sha256(
            Path(REMOTE_PROFILE).read_bytes()
        ).hexdigest(),
        "conic_base_point": [base_t, base_y],
        "conic_roots": [root_1, root_2],
        "t_of_s": str(t_of_s),
        "conic_y_of_s": str(conic_y),
        "x_of_s": str(x_of_s),
        "second_discriminant": str(second_discriminant),
        "numerator_shape": {
            "degree": numerator_poly.degree(),
            "terms": len(numerator_poly.terms()),
        },
        "denominator_shape": {
            "degree": denominator_poly.degree(),
            "terms": len(denominator_poly.terms()),
        },
        "numerator_factorization": factor_payload(num_content, num_factors),
        "denominator_factorization": factor_payload(den_content, den_factors),
        "parametrization_sha256": digest(
            str(t_of_s) + "\n" + str(conic_y) + "\n" + str(x_of_s)
        ),
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell3-conic-cover-profile-v1",
        "scope": (
            "Exact deployed-field profile of the remaining b-cover after "
            "parametrizing the cell-3 quotient conic; no outside, route, "
            "K3, or Prize claim."
        ),
        "result": profile_cover.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "status": output["result"].get("status"),
        "numerator_factorization": output["result"].get(
            "numerator_factorization"
        ),
        "denominator_factorization": output["result"].get(
            "denominator_factorization"
        ),
    }, sort_keys=True))
