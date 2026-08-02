#!/usr/bin/env python3
"""Test the H-component colored coefficient for deployed-field roots."""

import base64
import hashlib
import json
from pathlib import Path
import re
import zlib

import modal


DIRECTORY = Path(__file__).parent
COLORED = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_colored_x_reduce_polynomial.txt"
HFACTOR = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_common_factor_6.txt"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_colored_coefficient_frobenius_result.json"
ELIMINANT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_colored_coefficient_t_eliminant.txt"
REMOTE = {
    COLORED: "/root/colored.txt",
    HFACTOR: "/root/hfactor.txt",
}
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell4-h-colored-coefficient-frobenius")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
)
for local_path, remote_path in REMOTE.items():
    image = image.add_local_file(local_path, remote_path)


def shape(polynomial):
    return {
        "degrees": [int(value) for value in polynomial.degrees()],
        "total_degree": int(polynomial.total_degree()),
        "terms": len(list(polynomial.terms())),
    }


@app.function(image=image, cpu=4.0, memory=16384, timeout=600)
def compute_eliminant():
    from flint import fmpz_mod_mpoly_ctx, fmpz_mod_poly_ctx

    context = fmpz_mod_mpoly_ctx.get(["x", "w0", "t"], PRIME)

    def parse_polynomial(value):
        output = {}
        for raw_term in re.findall(r"[+-]?[^+-]+", value.replace(" ", "")):
            sign = 1
            term = raw_term
            if term.startswith("+"):
                term = term[1:]
            elif term.startswith("-"):
                sign = -1
                term = term[1:]
            coefficient = 1
            exponents = {name: 0 for name in ("x", "w0", "t")}
            for factor in term.split("*"):
                if factor.isdigit():
                    coefficient = coefficient*int(factor) % PRIME
                    continue
                match = re.fullmatch(r"(x|w0|t)(?:\^(\d+))?", factor)
                if match is None:
                    raise RuntimeError(f"cannot parse factor {factor!r}")
                variable, exponent = match.groups()
                exponents[variable] += int(exponent) if exponent else 1
            key = tuple(exponents[name] for name in ("x", "w0", "t"))
            output[key] = (output.get(key, 0)+sign*coefficient) % PRIME
        return context.from_dict({key: coefficient for key, coefficient in
                                  output.items() if coefficient})

    colored = parse_polynomial(Path(REMOTE[COLORED]).read_text().strip())
    colored_dict = colored.to_dict()
    x_degrees = sorted({int(monomial[0]) for monomial in colored_dict})
    if x_degrees != [4]:
        raise RuntimeError(f"colored projection is not x^4 times a coefficient: {x_degrees}")
    coefficient = context.from_dict({
        (0, monomial[1], monomial[2]): int(value)
        for monomial, value in colored_dict.items()
    })
    hfactor = parse_polynomial(Path(REMOTE[HFACTOR]).read_text().strip())
    if int(hfactor.degrees()[0]) != 0:
        raise RuntimeError("H unexpectedly depends on x")

    eliminant = hfactor.resultant(coefficient, "w0")
    if eliminant.is_zero() or int(eliminant.degrees()[1]) != 0:
        raise RuntimeError("colored H resultant is zero or retains w0")

    eliminant_dict = eliminant.to_dict()
    degree = max(int(monomial[2]) for monomial in eliminant_dict)
    coefficients = [0]*(degree+1)
    for monomial, value in eliminant_dict.items():
        if monomial[:2] != (0, 0):
            raise RuntimeError("eliminant is not univariate in t")
        coefficients[int(monomial[2])] = int(value)

    univariate_context = fmpz_mod_poly_ctx(PRIME)
    univariate = univariate_context(coefficients)
    tpoly = univariate_context([0, 1])
    frobenius = pow(tpoly, PRIME, univariate)
    root_gcd = univariate.gcd(frobenius-tpoly)
    root_content, root_factors = root_gcd.factor()
    factor_rows = []
    reconstruction = univariate_context([int(root_content)])
    for factor, multiplicity in root_factors:
        reconstruction *= factor**multiplicity
        factor_rows.append({
            "degree": int(factor.degree()),
            "multiplicity": int(multiplicity),
            "sha256": hashlib.sha256(str(factor).encode()).hexdigest(),
            "text": str(factor),
        })
    if reconstruction != root_gcd:
        raise RuntimeError("Frobenius gcd factor reconstruction failed")

    text = eliminant.str()
    return {
        "status": "COMPLETE",
        "field": PRIME,
        "colored_shape": shape(colored),
        "x_degrees": x_degrees,
        "coefficient_shape": shape(coefficient),
        "coefficient_sha256": hashlib.sha256(coefficient.str().encode()).hexdigest(),
        "h_shape": shape(hfactor),
        "eliminant_shape": shape(eliminant),
        "eliminant_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "eliminant_zlib_base64": base64.b64encode(
            zlib.compress(text.encode(), level=9)
        ).decode(),
        "frobenius_remainder_degree": int(frobenius.degree()),
        "base_field_root_gcd": {
            "content": int(root_content),
            "degree": int(root_gcd.degree()),
            "sha256": hashlib.sha256(str(root_gcd).encode()).hexdigest(),
            "factors": factor_rows,
        },
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell4-pair-exceptional-h-colored-coefficient-frobenius-v1",
        "scope": (
            "Exact deployed-field root test for the coefficient C in the "
            "generic necessary colored projection x^4 C(w0,t), restricted "
            "to H. The nonzero-x deduction, discarded content fibers, "
            "pseudo-division leading charts, lifts, orbit, and Prize claims "
            "remain separate."
        ),
        "artifact_sha256": {
            path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in REMOTE
        },
        "result": compute_eliminant.remote(),
    }
    result = output["result"]
    text = zlib.decompress(
        base64.b64decode(result.pop("eliminant_zlib_base64"))
    ).decode()
    ELIMINANT.write_text(text+"\n")
    result["eliminant_file"] = ELIMINANT.name
    result["eliminant_file_sha256"] = hashlib.sha256(
        ELIMINANT.read_bytes()
    ).hexdigest()
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT),
        "status": result["status"],
        "x_degrees": result["x_degrees"],
        "coefficient_shape": result["coefficient_shape"],
        "eliminant_shape": result["eliminant_shape"],
        "base_field_root_gcd": result["base_field_root_gcd"],
    }, sort_keys=True))
