#!/usr/bin/env python3
"""Eliminate w1 from the cell-4 signed DE+/DE- pair."""

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
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_w1_resultant_result.json"
POLYNOMIAL = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_w1_resultant_polynomial.txt"
REMOTE_PLANE = "/root/cell4_plane_kernel_flint.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell4-pair-w1-resultant")
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


def compile_pair(include_objects=False):
    from flint import fmpz_mod_mpoly_ctx

    payload = json.loads(Path(REMOTE_PLANE).read_text())["result"]
    context = fmpz_mod_mpoly_ctx.get(["w1", "w0", "b", "t"], PRIME)
    w1, w0, b, _ = context.gens()

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
            exponents = {name: 0 for name in ("w1", "w0", "b", "t")}
            for factor in term.split("*"):
                if factor.isdigit():
                    coefficient = coefficient*int(factor) % PRIME
                    continue
                match = re.fullmatch(r"(w1|w0|b|t)(?:\^(\d+))?", factor)
                if match is None:
                    raise RuntimeError(f"cannot parse factor {factor!r}")
                variable, exponent = match.groups()
                exponents[variable] += int(exponent) if exponent else 1
            key = tuple(exponents[name] for name in ("w1", "w0", "b", "t"))
            output[key] = (output.get(key, 0)+sign*coefficient) % PRIME
        return context.from_dict({key: coefficient for key, coefficient in
                                  output.items() if coefficient})

    coefficients = {
        name: parse_polynomial(row["polynomial"])
        for name, row in payload["normalized_coefficients"].items()
    }
    if not (coefficients["b10"]+coefficients["b11"]).is_zero():
        raise RuntimeError("B1 opposition failed")

    def evaluate(prefix, w_value):
        return coefficients[f"{prefix}0"]+coefficients[f"{prefix}1"]*w_value \
            + coefficients[f"{prefix}2"]*w_value**2

    d0, d1 = evaluate("a2", w0), evaluate("a2", w1)
    n0, n1 = evaluate("a0", w0), evaluate("a0", w1)
    k = coefficients["b10"]
    raw_product = n1*d0+n0*d1
    raw_sum = (
        k*k*w0*(1-w0)*(1-w0)*d1*d1
        -k*k*w1*(1-w1)*(1-w1)*d0*d0
        -4*n0*d0*d1*d1
    )
    plane = parse_polynomial(payload["plane_polynomial"])
    plane_leading = parse_polynomial(payload["plane_leading_coefficient"])

    def coefficient_at_b_degree(polynomial, degree):
        return context.from_dict({
            (monomial[0], monomial[1], 0, monomial[3]): int(coefficient)
            for monomial, coefficient in polynomial.to_dict().items()
            if monomial[2] == degree
        })

    def pseudo_remainder(polynomial):
        remainder = polynomial
        steps = 0
        while int(remainder.degrees()[2]) >= 4:
            old_degree = int(remainder.degrees()[2])
            leading = coefficient_at_b_degree(remainder, old_degree)
            remainder = plane_leading*remainder-leading*b**(old_degree-4)*plane
            if int(remainder.degrees()[2]) >= old_degree:
                raise RuntimeError("plane pseudo-division did not lower b degree")
            steps += 1
        return remainder, steps

    product, product_steps = pseudo_remainder(raw_product)
    sum_cut, sum_steps = pseudo_remainder(raw_sum)
    summary = {
        "raw_shapes": [shape(raw_product), shape(raw_sum)],
        "reduced_shapes": [shape(product), shape(sum_cut)],
        "pseudo_steps": [product_steps, sum_steps],
        "product_sha256": hashlib.sha256(product.str().encode()).hexdigest(),
        "sum_sha256": hashlib.sha256(sum_cut.str().encode()).hexdigest(),
    }
    if include_objects:
        return summary, context, product, sum_cut, plane, plane_leading
    return summary


@app.function(image=image, cpu=2.0, memory=4096, timeout=120)
def summarize_pair():
    return compile_pair(include_objects=False)


@app.function(image=image, cpu=4.0, memory=8192, timeout=300)
def eliminate_w1():
    summary, context, product, sum_cut, plane, plane_leading = compile_pair(
        include_objects=True
    )
    _, _, b, _ = context.gens()
    resultant = product.resultant(sum_cut, "w1")
    if int(resultant.degrees()[0]) != 0:
        raise RuntimeError("w1 was not eliminated")

    def coefficient_at_b_degree(polynomial, degree):
        return context.from_dict({
            (monomial[0], monomial[1], 0, monomial[3]): int(coefficient)
            for monomial, coefficient in polynomial.to_dict().items()
            if monomial[2] == degree
        })

    reduced = resultant
    steps = 0
    while int(reduced.degrees()[2]) >= 4:
        old_degree = int(reduced.degrees()[2])
        leading = coefficient_at_b_degree(reduced, old_degree)
        reduced = plane_leading*reduced-leading*b**(old_degree-4)*plane
        if int(reduced.degrees()[2]) >= old_degree:
            raise RuntimeError("resultant pseudo-division did not lower b degree")
        steps += 1

    coefficient_groups = {}
    for monomial, coefficient in reduced.to_dict().items():
        key = monomial[:3]
        coefficient_groups.setdefault(key, {})[(0, 0, 0, monomial[3])] = int(coefficient)
    coefficient_polynomials = [context.from_dict(value)
                               for value in coefficient_groups.values()]
    content = functools.reduce(lambda left, right: left.gcd(right),
                               coefficient_polynomials)
    primitive, remainder = divmod(reduced, content)
    if not remainder.is_zero():
        raise RuntimeError("nonexact resultant content division")
    text = primitive.str()
    compressed = base64.b64encode(zlib.compress(text.encode(), level=9)).decode()
    return {
        **summary, "status": "COMPLETE",
        "resultant_shape": shape(resultant),
        "projected_shape": shape(reduced),
        "projected_pseudo_steps": steps,
        "content": content.str(), "content_shape": shape(content),
        "primitive_shape": shape(primitive),
        "primitive_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "primitive_zlib_base64": compressed,
        "primitive_chars": len(text), "compressed_chars": len(compressed),
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell4-pair-w1-resultant-v1",
        "scope": (
            "Necessary squared-label DE+/DE- pair projection on the main "
            "cell-4 chart; no unit, orbit, route, K3, or Prize claim."
        ),
        "source_plane_sha256": hashlib.sha256(PLANE.read_bytes()).hexdigest(),
        "status": "CHECKPOINT", "pair_summary": summarize_pair.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    try:
        result = eliminate_w1.remote()
        compressed = base64.b64decode(result.pop("primitive_zlib_base64"))
        polynomial = zlib.decompress(compressed).decode()
        POLYNOMIAL.write_text(polynomial+"\n")
        result["polynomial_file"] = POLYNOMIAL.name
        result["polynomial_file_sha256"] = hashlib.sha256(
            POLYNOMIAL.read_bytes()).hexdigest()
        output["status"] = "COMPLETE"
        output["result"] = result
    except Exception as error:
        output["status"] = "TIMEOUT" if "Timeout" in type(error).__name__ else "REMOTE_ERROR"
        output["error"] = repr(error)
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT), "status": output["status"],
        "pair_summary": output["pair_summary"],
        "result_summary": output.get("result", {}), "error": output.get("error"),
    }, sort_keys=True))
