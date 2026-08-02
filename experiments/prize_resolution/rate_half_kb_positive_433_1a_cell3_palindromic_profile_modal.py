#!/usr/bin/env python3
"""Factor the palindromic cell-3 eliminant and its quotient discriminant."""

import hashlib
import json
from pathlib import Path
import re

import modal


DIRECTORY = Path(__file__).parent
SCOUT = DIRECTORY / "rate_half_kb_positive_433_1a_cell3_common_triangle_scout_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell3_palindromic_profile_result.json"
REMOTE_SCOUT = "/root/cell3_triangle_scout.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell3-palindromic-profile")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(SCOUT, REMOTE_SCOUT)
)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


@app.function(image=image, cpu=2.0, memory=2048, timeout=180)
def profile():
    import sympy as sp

    payload = json.loads(Path(REMOTE_SCOUT).read_text())
    row = next(item for item in payload["rows"]
               if item.get("order") == ["c", "r", "b", "t"])
    match = re.search(r"^GP\[1\]=(.*)$", row["stdout"], re.MULTILINE)
    if match is None:
        raise RuntimeError("missing first lex polynomial")
    singular_text = match.group(1)

    def sympy_text(value):
        converted = re.sub(
            r"([brct])(\d*)",
            lambda found: "*" + found.group(1)
            + ("**" + found.group(2) if found.group(2) else ""),
            value,
        )
        return (
            converted.lstrip("*")
            .replace("+*", "+")
            .replace("-*", "-")
        )

    b, t, x = sp.symbols("b t x")
    polynomial = sp.Poly(sp.sympify(sympy_text(singular_text)), b, t,
                         modulus=PRIME)
    polynomial_expression = polynomial.as_expr()
    coefficients = {
        degree: sp.Poly(polynomial_expression.coeff(b, degree), t,
                        modulus=PRIME)
        for degree in range(5)
    }
    palindromic = (
        coefficients[4] == coefficients[0]
        and coefficients[3] == coefficients[1]
    )
    if not palindromic:
        raise RuntimeError("eliminant is not palindromic")
    a0 = coefficients[4]
    a1 = coefficients[3]
    a2 = coefficients[2] - 2 * a0
    quotient = sp.Poly(
        a0.as_expr() * x**2 + a1.as_expr() * x + a2.as_expr(),
        x, t, modulus=PRIME,
    )
    reconstructed = sp.Poly(
        b**2 * quotient.as_expr().subs(x, b + b**-1),
        b, t, modulus=PRIME,
    )
    discriminant = sp.Poly(
        a1.as_expr()**2 - 4 * a0.as_expr() * a2.as_expr(),
        t, modulus=PRIME,
    )
    disc_content, disc_factors = sp.factor_list(discriminant, modulus=PRIME)
    return {
        "status": "COMPLETE",
        "field": PRIME,
        "source_program_sha256": row["program_sha256"],
        "source_eliminant_sha256": digest(singular_text),
        "palindromic": palindromic,
        "reconstruction_equal": reconstructed == polynomial,
        "eliminant_shape": {
            "total_degree": polynomial.total_degree(),
            "terms": len(polynomial.terms()),
            "degree_b": polynomial.degree(b),
            "degree_t": polynomial.degree(t),
        },
        "quotient": str(quotient.as_expr()),
        "quotient_shape": {
            "total_degree": quotient.total_degree(),
            "terms": len(quotient.terms()),
        },
        "discriminant": str(discriminant.as_expr()),
        "discriminant_shape": {
            "degree": discriminant.degree(),
            "terms": len(discriminant.terms()),
        },
        "discriminant_factorization": {
            "content": int(disc_content) % PRIME,
            "factors": [
                {"polynomial": str(factor.as_expr()),
                 "degree": factor.degree(),
                 "multiplicity": multiplicity}
                for factor, multiplicity in disc_factors
            ],
        },
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell3-palindromic-profile-v1",
        "scope": (
            "Exact factor profile of the cell-3 palindromic common-curve "
            "eliminant; no outside, route, K3, or Prize claim."
        ),
        "result": profile.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "status": output["result"].get("status"),
        "discriminant_factorization": output["result"].get(
            "discriminant_factorization"
        ),
    }, sort_keys=True))
