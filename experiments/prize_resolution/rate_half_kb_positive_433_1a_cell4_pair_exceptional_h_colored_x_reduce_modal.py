#!/usr/bin/env python3
"""Reduce the colored x projection by the H curve and linear b lift."""

import base64
import functools
import hashlib
import json
from pathlib import Path
import re
import zlib

import modal


DIRECTORY = Path(__file__).parent
SOURCE = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_colored_x_w2_resultant_polynomial.txt"
HFACTOR = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_common_factor_6.txt"
BLIFT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_b_gcd_polynomial.txt"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_colored_x_reduce_result.json"
POLYNOMIAL = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_colored_x_reduce_polynomial.txt"
REMOTE = {
    SOURCE: "/root/colored_x.txt",
    HFACTOR: "/root/hfactor.txt",
    BLIFT: "/root/blift.txt",
}
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell4-exceptional-h-colored-x-reduce")
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


@app.function(image=image, cpu=4.0, memory=16384, timeout=300)
def reduce_colored_projection():
    from flint import fmpz_mod_mpoly_ctx

    context = fmpz_mod_mpoly_ctx.get(["x", "w1", "w0", "b", "t"], PRIME)
    _, _, w0, b, _ = context.gens()

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
            exponents = {name: 0 for name in ("x", "w1", "w0", "b", "t")}
            for factor in term.split("*"):
                if factor.isdigit():
                    coefficient = coefficient*int(factor) % PRIME
                    continue
                match = re.fullmatch(r"(x|w1|w0|b|t)(?:\^(\d+))?", factor)
                if match is None:
                    raise RuntimeError(f"cannot parse factor {factor!r}")
                variable, exponent = match.groups()
                exponents[variable] += int(exponent) if exponent else 1
            key = tuple(exponents[name] for name in ("x", "w1", "w0", "b", "t"))
            output[key] = (output.get(key, 0)+sign*coefficient) % PRIME
        return context.from_dict({key: coefficient for key, coefficient in
                                  output.items() if coefficient})

    source = parse_polynomial(Path(REMOTE[SOURCE]).read_text().strip())
    hfactor = parse_polynomial(Path(REMOTE[HFACTOR]).read_text().strip())
    blift = parse_polynomial(Path(REMOTE[BLIFT]).read_text().strip())

    def coefficient_at_degree(polynomial, variable_index, degree):
        return context.from_dict({
            tuple(0 if index == variable_index else monomial[index]
                  for index in range(5)): int(coefficient)
            for monomial, coefficient in polynomial.to_dict().items()
            if monomial[variable_index] == degree
        })

    h_degree = int(hfactor.degrees()[2])
    h_leading = coefficient_at_degree(hfactor, 2, h_degree)

    def reduce_by_h(polynomial):
        reduced = polynomial
        steps = 0
        while int(reduced.degrees()[2]) >= h_degree:
            old_degree = int(reduced.degrees()[2])
            coefficient = coefficient_at_degree(reduced, 2, old_degree)
            reduced = (
                h_leading*reduced
                -coefficient*w0**(old_degree-h_degree)*hfactor
            )
            if int(reduced.degrees()[2]) >= old_degree:
                raise RuntimeError("H pseudo-division did not lower degree")
            steps += 1
        return reduced, steps

    blift, blift_h_steps = reduce_by_h(blift)
    if int(blift.degrees()[3]) != 1:
        raise RuntimeError("b lift is not linear")
    b_leading = coefficient_at_degree(blift, 3, 1)
    reduced, h_steps = reduce_by_h(source)
    b_steps = 0
    while int(reduced.degrees()[3]) >= 1:
        old_degree = int(reduced.degrees()[3])
        coefficient = coefficient_at_degree(reduced, 3, old_degree)
        reduced = (
            b_leading*reduced
            -coefficient*b**(old_degree-1)*blift
        )
        reduced, new_h_steps = reduce_by_h(reduced)
        h_steps += new_h_steps
        if int(reduced.degrees()[3]) >= old_degree:
            raise RuntimeError("b pseudo-division did not lower degree")
        b_steps += 1

    groups = {}
    for monomial, coefficient in reduced.to_dict().items():
        key = monomial[:4]
        groups.setdefault(key, {})[(0, 0, 0, 0, monomial[4])] = int(coefficient)
    coefficient_polynomials = [context.from_dict(value) for value in groups.values()]
    content = functools.reduce(lambda left, right: left.gcd(right),
                               coefficient_polynomials)
    primitive, remainder = divmod(reduced, content)
    if not remainder.is_zero():
        raise RuntimeError("colored projection content division failed")
    content_scalar, content_factors = content.factor()
    content_reconstruction = context.constant(int(content_scalar))
    factor_rows = []
    for factor, multiplicity in content_factors:
        content_reconstruction *= factor**multiplicity
        factor_rows.append({
            "shape": shape(factor), "multiplicity": int(multiplicity),
            "sha256": hashlib.sha256(factor.str().encode()).hexdigest(),
            "text": factor.str(),
        })
    if content_reconstruction != content:
        raise RuntimeError("colored content reconstruction failed")
    text = primitive.str()
    return {
        "status": "COMPLETE", "field": PRIME,
        "source_shape": shape(source),
        "h_shape": shape(hfactor), "h_leading_shape": shape(h_leading),
        "blift_shape": shape(blift), "blift_h_steps": blift_h_steps,
        "blift_leading_shape": shape(b_leading),
        "h_steps": h_steps, "b_steps": b_steps,
        "reduced_shape": shape(reduced),
        "content": {
            "shape": shape(content),
            "sha256": hashlib.sha256(content.str().encode()).hexdigest(),
            "content": int(content_scalar), "factors": factor_rows,
        },
        "primitive_shape": shape(primitive),
        "primitive_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "primitive_zlib_base64": base64.b64encode(
            zlib.compress(text.encode(), level=9)
        ).decode(),
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell4-pair-exceptional-h-colored-x-reduce-v1",
        "scope": (
            "Exact generic reduction of the necessary colored x projection "
            "by the linear b lift and H, followed by univariate content "
            "removal. Leading exceptions, sign realizability, pair, orbit, "
            "and Prize claims remain separate."
        ),
        "artifact_sha256": {
            path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in REMOTE
        },
        "result": reduce_colored_projection.remote(),
    }
    result = output["result"]
    text = zlib.decompress(
        base64.b64decode(result.pop("primitive_zlib_base64"))
    ).decode()
    POLYNOMIAL.write_text(text+"\n")
    result["polynomial_file"] = POLYNOMIAL.name
    result["polynomial_file_sha256"] = hashlib.sha256(
        POLYNOMIAL.read_bytes()
    ).hexdigest()
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT), "status": result["status"],
        "h_steps": result["h_steps"], "b_steps": result["b_steps"],
        "content": result["content"],
        "primitive_shape": result["primitive_shape"],
    }, sort_keys=True))
