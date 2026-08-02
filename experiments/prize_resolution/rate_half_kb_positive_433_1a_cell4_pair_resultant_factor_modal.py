#!/usr/bin/env python3
"""Factor the primitive cell-4 signed-pair projection."""

import base64
import hashlib
import json
from pathlib import Path
import re
import zlib

import modal


DIRECTORY = Path(__file__).parent
POLYNOMIAL = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_w1_resultant_polynomial.txt"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_resultant_factor_result.json"
REMOTE_POLYNOMIAL = "/root/cell4_pair_w1_resultant.txt"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell4-pair-resultant-factor")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
    .add_local_file(POLYNOMIAL, REMOTE_POLYNOMIAL)
)


@app.function(image=image, cpu=4.0, memory=8192, timeout=300)
def factor_projection():
    from flint import fmpz_mod_mpoly_ctx

    source_bytes = Path(REMOTE_POLYNOMIAL).read_bytes()
    text = source_bytes.decode().strip()
    context = fmpz_mod_mpoly_ctx.get(["w0", "b", "t"], PRIME)

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
            exponents = {"w0": 0, "b": 0, "t": 0}
            for factor in term.split("*"):
                if factor.isdigit():
                    coefficient = coefficient*int(factor) % PRIME
                    continue
                match = re.fullmatch(r"(w0|b|t)(?:\^(\d+))?", factor)
                if match is None:
                    raise RuntimeError(f"cannot parse factor {factor!r}")
                variable, exponent = match.groups()
                exponents[variable] += int(exponent) if exponent else 1
            key = (exponents["w0"], exponents["b"], exponents["t"])
            output[key] = (output.get(key, 0)+sign*coefficient) % PRIME
        return context.from_dict({key: coefficient for key, coefficient in
                                  output.items() if coefficient})

    polynomial = parse_polynomial(text)
    content, factors = polynomial.factor()
    reconstruction = context.constant(int(content))
    rows = []
    for factor, multiplicity in factors:
        reconstruction *= factor**multiplicity
        factor_text = factor.str()
        rows.append({
            "multiplicity": int(multiplicity),
            "degrees": [int(value) for value in factor.degrees()],
            "total_degree": int(factor.total_degree()),
            "terms": len(list(factor.terms())),
            "sha256": hashlib.sha256(factor_text.encode()).hexdigest(),
            "zlib_base64": base64.b64encode(
                zlib.compress(factor_text.encode(), level=9)
            ).decode(),
        })
    if reconstruction != polynomial:
        raise RuntimeError("factor reconstruction failed")
    return {
        "status": "COMPLETE", "field": PRIME,
        "source_polynomial_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "source_shape": {
            "degrees": [int(value) for value in polynomial.degrees()],
            "total_degree": int(polynomial.total_degree()),
            "terms": len(list(polynomial.terms())),
        },
        "content": int(content) % PRIME,
        "factors": rows,
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell4-pair-resultant-factor-v1",
        "scope": (
            "Exact factorization of the primitive necessary signed-pair "
            "projection; no component realizability, orbit, or Prize claim."
        ),
        "result": factor_projection.remote(),
    }
    for index, row in enumerate(output["result"].get("factors", [])):
        text = zlib.decompress(base64.b64decode(row.pop("zlib_base64"))).decode()
        filename = (
            "rate_half_kb_positive_433_1a_cell4_pair_resultant_factor_"
            f"{index}.txt"
        )
        path = DIRECTORY / filename
        path.write_text(text+"\n")
        row["file"] = filename
        row["file_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    result = output["result"]
    print(json.dumps({
        "result": str(RESULT), "status": result.get("status"),
        "source_shape": result.get("source_shape"),
        "content": result.get("content"),
        "factors": result.get("factors"),
    }, sort_keys=True))
