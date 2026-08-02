#!/usr/bin/env python3
"""Profile reciprocal quotient geometry of the remaining positive curves."""

import hashlib
import json
from pathlib import Path
import re

import modal


DIRECTORY = Path(__file__).parent
SCOUT = DIRECTORY / "rate_half_kb_positive_433_1a_remaining_lex_scout_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_remaining_palindromic_profile_result.json"
REMOTE_SCOUT = "/root/remaining_lex_scout.json"
PRIME = 2130706433
CELLS = (4, 9, 11, 12, 14)

app = modal.App("rs-mca-positive-433-1a-remaining-palindromic-profile")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(SCOUT, REMOTE_SCOUT)
)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


@app.function(image=image, cpu=1.0, memory=1536, timeout=90, max_containers=5)
def profile(cell):
    import sympy as sp

    payload = json.loads(Path(REMOTE_SCOUT).read_text())
    row = next(item for item in payload["rows"]
               if item.get("cell") == cell
               and item.get("order") == ["c", "r", "b", "t"])
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
        return converted.lstrip("*").replace("+*", "+").replace("-*", "-")

    b, t, x = sp.symbols("b t x")
    polynomial = sp.Poly(sp.sympify(sympy_text(singular_text)), b, t,
                         modulus=PRIME)
    degree_b = polynomial.degree(b)
    coefficients = [
        sp.Poly(polynomial.as_expr().coeff(b, degree), t, modulus=PRIME)
        for degree in range(degree_b+1)
    ]
    palindromic = all(coefficients[degree] == coefficients[degree_b-degree]
                      for degree in range(degree_b+1))
    output = {
        "cell": cell,
        "status": "COMPLETE",
        "field": PRIME,
        "source_program_sha256": row["program_sha256"],
        "source_eliminant_sha256": digest(singular_text),
        "palindromic": palindromic,
        "eliminant_shape": {
            "total_degree": polynomial.total_degree(),
            "terms": len(polynomial.terms()),
            "degree_b": degree_b,
            "degree_t": polynomial.degree(t),
        },
    }
    if degree_b != 4 or not palindromic:
        return output
    a0 = coefficients[4]
    a1 = coefficients[3]
    a2 = coefficients[2]-2*a0
    quotient = sp.Poly(a0.as_expr()*x**2+a1.as_expr()*x+a2.as_expr(),
                       x, t, modulus=PRIME)
    reconstructed = sp.Poly(
        b**2*quotient.as_expr().subs(x, b+b**-1), b, t, modulus=PRIME
    )
    discriminant = sp.Poly(a1.as_expr()**2-4*a0.as_expr()*a2.as_expr(),
                           t, modulus=PRIME)
    content, factors = sp.factor_list(discriminant, modulus=PRIME)
    output.update({
        "reconstruction_equal": reconstructed == polynomial,
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
            "content": int(content) % PRIME,
            "factors": [
                {"polynomial": str(factor.as_expr()),
                 "degree": factor.degree(), "multiplicity": multiplicity}
                for factor, multiplicity in factors
            ],
        },
    })
    return output


@app.local_entrypoint()
def main():
    rows = list(profile.map(CELLS, order_outputs=True, return_exceptions=True))
    normalized = []
    for cell, row in zip(CELLS, rows):
        if isinstance(row, BaseException):
            normalized.append({"cell": cell, "status": "REMOTE_ERROR",
                               "error": repr(row)})
        else:
            normalized.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1a-remaining-palindromic-profile-v1",
        "scope": (
            "Exact reciprocal-quotient profiles of the five remaining "
            "positive common curves; no outside, route, K3, or Prize claim."
        ),
        "source_scout_sha256": hashlib.sha256(SCOUT.read_bytes()).hexdigest(),
        "rows": normalized,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {"cell": row.get("cell"), "status": row.get("status"),
             "palindromic": row.get("palindromic"),
             "eliminant_shape": row.get("eliminant_shape"),
             "discriminant_factorization": row.get("discriminant_factorization")}
            for row in normalized
        ],
    }, sort_keys=True))
