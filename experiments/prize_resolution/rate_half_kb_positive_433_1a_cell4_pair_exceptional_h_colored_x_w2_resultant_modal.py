#!/usr/bin/env python3
"""Eliminate w2 while retaining the DE cross value x."""

import base64
import functools
import hashlib
import json
from pathlib import Path
import re
import zlib

import modal


DIRECTORY = Path(__file__).parent
PLANE = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_plane_kernel_flint_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_colored_x_w2_resultant_result.json"
POLYNOMIAL = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_colored_x_w2_resultant_polynomial.txt"
REMOTE_PLANE = "/root/plane.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell4-exceptional-h-colored-x-w2")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
    .add_local_file(PLANE, REMOTE_PLANE)
)


def shape(polynomial):
    return {
        "degrees": [int(value) for value in polynomial.degrees()],
        "total_degree": int(polynomial.total_degree()),
        "terms": len(list(polynomial.terms())),
    }


def compile_equations(include_objects=False):
    from flint import fmpz_mod_mpoly_ctx

    payload = json.loads(Path(REMOTE_PLANE).read_text())["result"]
    context = fmpz_mod_mpoly_ctx.get(
        ["x", "w2", "w1", "w0", "b", "t"], PRIME
    )
    x, w2, w1, w0, b, _ = context.gens()

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
            exponents = {name: 0 for name in
                         ("x", "w2", "w1", "w0", "b", "t")}
            for factor in term.split("*"):
                if factor.isdigit():
                    coefficient = coefficient*int(factor) % PRIME
                    continue
                match = re.fullmatch(
                    r"(x|w2|w1|w0|b|t)(?:\^(\d+))?", factor
                )
                if match is None:
                    raise RuntimeError(f"cannot parse factor {factor!r}")
                variable, exponent = match.groups()
                exponents[variable] += int(exponent) if exponent else 1
            key = tuple(exponents[name] for name in
                        ("x", "w2", "w1", "w0", "b", "t"))
            output[key] = (output.get(key, 0)+sign*coefficient) % PRIME
        return context.from_dict({key: coefficient for key, coefficient in
                                  output.items() if coefficient})

    coefficients = {
        name: parse_polynomial(row["polynomial"])
        for name, row in payload["normalized_coefficients"].items()
    }

    def evaluate(prefix, w):
        return (coefficients[f"{prefix}0"]+coefficients[f"{prefix}1"]*w
                +coefficients[f"{prefix}2"]*w*w)

    d0, d1, d2 = [evaluate("a2", w) for w in (w0, w1, w2)]
    n0, n1, n2 = [evaluate("a0", w) for w in (w0, w1, w2)]
    k = coefficients["b10"]
    k2 = k*(1-w2)
    first_color = 2*n2*d0*d1-b*d2*x
    second_color = (b*b*d2+n2)**2-b*b*w2*k2*k2
    plane = parse_polynomial(payload["plane_polynomial"])
    plane_leading = parse_polynomial(payload["plane_leading_coefficient"])

    def coefficient_at_b_degree(polynomial, degree):
        return context.from_dict({
            (monomial[0], monomial[1], monomial[2], monomial[3], 0,
             monomial[5]): int(coefficient)
            for monomial, coefficient in polynomial.to_dict().items()
            if monomial[4] == degree
        })

    def reduce_by_plane(polynomial):
        reduced = polynomial
        steps = 0
        while int(reduced.degrees()[4]) >= 4:
            old_degree = int(reduced.degrees()[4])
            coefficient = coefficient_at_b_degree(reduced, old_degree)
            reduced = (
                plane_leading*reduced
                -coefficient*b**(old_degree-4)*plane
            )
            if int(reduced.degrees()[4]) >= old_degree:
                raise RuntimeError("plane pseudo-division did not lower b degree")
            steps += 1
        return reduced, steps

    first = reduce_by_plane(first_color)
    second = reduce_by_plane(second_color)
    summary = {
        "first_color": {"shape": shape(first[0]), "pseudo_steps": first[1],
                        "sha256": hashlib.sha256(first[0].str().encode()).hexdigest()},
        "second_color": {"shape": shape(second[0]), "pseudo_steps": second[1],
                         "sha256": hashlib.sha256(second[0].str().encode()).hexdigest()},
    }
    if include_objects:
        return summary, context, first[0], second[0], plane, plane_leading
    return summary


@app.function(image=image, cpu=2.0, memory=8192, timeout=120)
def summarize():
    return compile_equations(include_objects=False)


@app.function(image=image, cpu=4.0, memory=16384, timeout=300)
def eliminate_w2():
    summary, context, first, second, plane, plane_leading = compile_equations(
        include_objects=True
    )
    _, _, _, _, b, _ = context.gens()
    resultant = first.resultant(second, "w2")
    if int(resultant.degrees()[1]) != 0:
        raise RuntimeError("w2 was not eliminated")

    def coefficient_at_b_degree(polynomial, degree):
        return context.from_dict({
            (monomial[0], monomial[1], monomial[2], monomial[3], 0,
             monomial[5]): int(coefficient)
            for monomial, coefficient in polynomial.to_dict().items()
            if monomial[4] == degree
        })

    projected = resultant
    steps = 0
    while int(projected.degrees()[4]) >= 4:
        old_degree = int(projected.degrees()[4])
        coefficient = coefficient_at_b_degree(projected, old_degree)
        projected = (
            plane_leading*projected
            -coefficient*b**(old_degree-4)*plane
        )
        if int(projected.degrees()[4]) >= old_degree:
            raise RuntimeError("resultant plane reduction did not lower degree")
        steps += 1

    groups = {}
    for monomial, coefficient in projected.to_dict().items():
        key = monomial[:5]
        groups.setdefault(key, {})[(0, 0, 0, 0, 0, monomial[5])] = int(coefficient)
    content_polynomials = [context.from_dict(value) for value in groups.values()]
    content = functools.reduce(lambda left, right: left.gcd(right),
                               content_polynomials)
    primitive, remainder = divmod(projected, content)
    if not remainder.is_zero():
        raise RuntimeError("w2 resultant content division failed")
    text = primitive.str()
    return {
        "status": "COMPLETE", "equations": summary,
        "resultant_shape": shape(resultant),
        "projected_shape": shape(projected),
        "projected_pseudo_steps": steps,
        "content_shape": shape(content),
        "content_sha256": hashlib.sha256(content.str().encode()).hexdigest(),
        "primitive_shape": shape(primitive),
        "primitive_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "primitive_zlib_base64": base64.b64encode(
            zlib.compress(text.encode(), level=9)
        ).decode(),
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell4-pair-exceptional-h-colored-x-w2-resultant-v1",
        "scope": (
            "Necessary colored elimination retaining x=q1D0-q0D1: one "
            "quadratic and one quartic equation in w2. Squaring and projection "
            "may add solutions; no H-component, point, orbit, or Prize claim."
        ),
        "source_plane_sha256": hashlib.sha256(PLANE.read_bytes()).hexdigest(),
        "equation_summary": summarize.remote(),
    }
    try:
        result = eliminate_w2.remote()
        text = zlib.decompress(
            base64.b64decode(result.pop("primitive_zlib_base64"))
        ).decode()
        POLYNOMIAL.write_text(text+"\n")
        result["polynomial_file"] = POLYNOMIAL.name
        result["polynomial_file_sha256"] = hashlib.sha256(
            POLYNOMIAL.read_bytes()
        ).hexdigest()
        output["status"] = "COMPLETE"
        output["result"] = result
    except Exception as error:
        output["status"] = (
            "TIMEOUT" if "Timeout" in type(error).__name__ else "REMOTE_ERROR"
        )
        output["error"] = repr(error)
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT), "status": output["status"],
        "equation_summary": output["equation_summary"],
        "result_summary": output.get("result", {}),
        "error": output.get("error"),
    }, sort_keys=True))
