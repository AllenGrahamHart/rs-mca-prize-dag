#!/usr/bin/env python3
"""Factor the t eliminant of the 470-point primitive residual."""

import base64
import hashlib
import json
from pathlib import Path
import re
import zlib

import modal


DIRECTORY = Path(__file__).parent
SOURCE = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_primitive_tpoly.txt"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_primitive_tpoly_factor_result.json"
REMOTE_SOURCE = "/root/primitive_tpoly.txt"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell4-exceptional-primitive-t-factor")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
    .add_local_file(SOURCE, REMOTE_SOURCE)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=120)
def factor_t_polynomial():
    from flint import fmpz_mod_mpoly_ctx

    context = fmpz_mod_mpoly_ctx.get(["t"], PRIME)
    value = Path(REMOTE_SOURCE).read_text().strip()
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
        exponent = 0
        for factor in term.split("*"):
            if factor.isdigit():
                coefficient = coefficient*int(factor) % PRIME
                continue
            match = re.fullmatch(r"t(?:\^(\d+))?", factor)
            if match is None:
                raise RuntimeError(f"cannot parse factor {factor!r}")
            exponent += int(match.group(1)) if match.group(1) else 1
        output[(exponent,)] = (
            output.get((exponent,), 0)+sign*coefficient
        ) % PRIME
    polynomial = context.from_dict({key: coefficient for key, coefficient in
                                    output.items() if coefficient})
    content, factors = polynomial.factor()
    reconstruction = context.constant(int(content))
    rows = []
    for factor, multiplicity in factors:
        reconstruction *= factor**multiplicity
        text = factor.str()
        row = {
            "degree": int(factor.degrees()[0]),
            "terms": len(list(factor.terms())),
            "multiplicity": int(multiplicity),
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
            "zlib_base64": base64.b64encode(
                zlib.compress(text.encode(), level=9)
            ).decode(),
        }
        if int(factor.degrees()[0]) == 1:
            coefficients = factor.to_dict()
            leading = int(coefficients[(1,)])
            constant = int(coefficients.get((0,), 0))
            row["root"] = -constant*pow(leading, -1, PRIME) % PRIME
        rows.append(row)
    if reconstruction != polynomial:
        raise RuntimeError("t factor reconstruction failed")
    return {
        "status": "COMPLETE", "field": PRIME,
        "source_degree": int(polynomial.degrees()[0]),
        "source_terms": len(list(polynomial.terms())),
        "content": int(content), "factors": rows,
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell4-pair-exceptional-b-resultant-primitive-tpoly-factor-v1",
        "scope": (
            "Exact deployed-field factorization of the primitive residual t "
            "eliminant; absence of non-guard linear factors excludes deployed "
            "residual points, but makes no common-curve, colored, orbit, or "
            "Prize claim."
        ),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "result": factor_t_polynomial.remote(),
    }
    for index, row in enumerate(output["result"]["factors"]):
        text = zlib.decompress(base64.b64decode(row.pop("zlib_base64"))).decode()
        filename = (
            "rate_half_kb_positive_433_1a_cell4_pair_exceptional_"
            f"b_resultant_primitive_tpoly_factor_{index}.txt"
        )
        path = DIRECTORY / filename
        path.write_text(text+"\n")
        row["file"] = filename
        row["file_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT), "status": output["result"]["status"],
        "source_degree": output["result"]["source_degree"],
        "factors": output["result"]["factors"],
    }, sort_keys=True))
