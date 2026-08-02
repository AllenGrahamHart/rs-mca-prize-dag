#!/usr/bin/env python3
"""Eliminate the colored source square w2 on the cell-3 main plane chart."""

import base64
import hashlib
import json
from pathlib import Path
import re
import zlib

import modal


DIRECTORY = Path(__file__).parent
PLANE = DIRECTORY / "rate_half_kb_positive_433_1a_cell3_plane_kernel_flint_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell3_w2_resultant_result.json"
POLYNOMIAL = DIRECTORY / "rate_half_kb_positive_433_1a_cell3_w2_resultant_polynomial.txt"
REMOTE_PLANE = "/root/cell3_plane_kernel_flint.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell3-w2-resultant")
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


def compile_cuts(include_text=False):
    from flint import fmpz_mod_mpoly_ctx

    payload = json.loads(Path(REMOTE_PLANE).read_text())["result"]
    context = fmpz_mod_mpoly_ctx.get(["w", "z0", "z1", "b", "t"], PRIME)
    w, z0, z1, b, _ = context.gens()

    def parse_polynomial(value):
        output = {}
        compact = value.replace(" ", "")
        for raw_term in re.findall(r"[+-]?[^+-]+", compact):
            sign = 1
            term = raw_term
            if term.startswith("+"):
                term = term[1:]
            elif term.startswith("-"):
                sign = -1
                term = term[1:]
            coefficient = 1
            exponents = {name: 0 for name in ("w", "z0", "z1", "b", "t")}
            for factor in term.split("*"):
                if factor.isdigit():
                    coefficient = coefficient*int(factor) % PRIME
                    continue
                match = re.fullmatch(r"(w|z0|z1|b|t)(?:\^(\d+))?", factor)
                if match is None:
                    raise RuntimeError(f"cannot parse factor {factor!r}")
                variable, exponent = match.groups()
                exponents[variable] += int(exponent) if exponent else 1
            key = tuple(exponents[name] for name in ("w", "z0", "z1", "b", "t"))
            output[key] = (output.get(key, 0) + sign*coefficient) % PRIME
        return context.from_dict({key: coefficient for key, coefficient in output.items()
                                  if coefficient})

    coefficients = {
        name: parse_polynomial(row["polynomial"])
        for name, row in payload["normalized_coefficients"].items()
    }
    if not (coefficients["b10"] + coefficients["b11"]).is_zero():
        raise RuntimeError("B1 opposition failed")

    def evaluate(prefix, root_square):
        return (
            coefficients[f"{prefix}0"]
            + coefficients[f"{prefix}1"]*root_square
            + coefficients[f"{prefix}2"]*root_square**2
        )

    w0 = z0*z0
    w1 = z1*z1
    d0, d1 = evaluate("a2", w0), evaluate("a2", w1)
    n0, n1 = evaluate("a0", w0), evaluate("a0", w1)
    k = coefficients["b10"]
    q0 = k*z0*(1-w0)
    q1 = k*z1*(1-w1)
    d2 = evaluate("a2", w)
    n2 = evaluate("a0", w)
    a_value = 2*d0*d1
    cross = q1*d0-q0*d1

    # These are necessary and sufficient for some z2 with z2^2=w before
    # source guards: the second equation is the square of the unsquared row.
    product_cut = a_value*n2-b*cross*d2
    sum_cut = (
        a_value*a_value*k*k*w*(1-w)*(1-w)
        -(a_value*b+cross)*(a_value*b+cross)*d2*d2
    )

    plane = parse_polynomial(payload["plane_polynomial"])
    plane_leading = parse_polynomial(payload["plane_leading_coefficient"])

    def coefficient_at_b_degree(polynomial, degree):
        return context.from_dict({
            (monomial[0], monomial[1], monomial[2], 0, monomial[4]):
                int(coefficient)
            for monomial, coefficient in polynomial.to_dict().items()
            if monomial[3] == degree
        })

    def pseudo_remainder(polynomial):
        remainder = polynomial
        steps = 0
        while int(remainder.degrees()[3]) >= 4:
            old_degree = int(remainder.degrees()[3])
            leading = coefficient_at_b_degree(remainder, old_degree)
            remainder = plane_leading*remainder-leading*b**(old_degree-4)*plane
            if int(remainder.degrees()[3]) >= old_degree:
                raise RuntimeError("plane pseudo-division did not lower b degree")
            steps += 1
        return remainder, steps

    product_reduced, product_steps = pseudo_remainder(product_cut)
    sum_reduced, sum_steps = pseudo_remainder(sum_cut)
    output = {
        "raw_shapes": [shape(product_cut), shape(sum_cut)],
        "reduced_shapes": [shape(product_reduced), shape(sum_reduced)],
        "pseudo_steps": [product_steps, sum_steps],
        "product_sha256": hashlib.sha256(product_reduced.str().encode()).hexdigest(),
        "sum_sha256": hashlib.sha256(sum_reduced.str().encode()).hexdigest(),
    }
    if include_text:
        output["product"] = product_reduced.str()
        output["sum"] = sum_reduced.str()
        output["plane"] = plane.str()
        output["plane_leading"] = plane_leading.str()
    return output


@app.function(image=image, cpu=2.0, memory=4096, timeout=120)
def summarize_cuts():
    return compile_cuts(include_text=False)


@app.function(image=image, cpu=4.0, memory=8192, timeout=300)
def eliminate_w():
    import functools

    compiled = compile_cuts(include_text=True)
    from flint import fmpz_mod_mpoly_ctx
    context = fmpz_mod_mpoly_ctx.get(["w", "z0", "z1", "b", "t"], PRIME)
    w, _, _, b, _ = context.gens()

    def parse_flint(value):
        # FLINT parses its own canonical string through the context call.
        return context(value)

    product = parse_flint(compiled.pop("product"))
    sum_cut = parse_flint(compiled.pop("sum"))
    plane = parse_flint(compiled.pop("plane"))
    plane_leading = parse_flint(compiled.pop("plane_leading"))
    resultant = product.resultant(sum_cut, "w")
    if not resultant.degrees()[0] == 0:
        raise RuntimeError("w was not eliminated")

    def coefficient_at_b_degree(polynomial, degree):
        return context.from_dict({
            (monomial[0], monomial[1], monomial[2], 0, monomial[4]):
                int(coefficient)
            for monomial, coefficient in polynomial.to_dict().items()
            if monomial[3] == degree
        })

    reduced = resultant
    steps = 0
    while int(reduced.degrees()[3]) >= 4:
        old_degree = int(reduced.degrees()[3])
        leading = coefficient_at_b_degree(reduced, old_degree)
        reduced = plane_leading*reduced-leading*b**(old_degree-4)*plane
        if int(reduced.degrees()[3]) >= old_degree:
            raise RuntimeError("resultant pseudo-division did not lower b degree")
        steps += 1

    coefficient_groups = {}
    for monomial, coefficient in reduced.to_dict().items():
        key = monomial[:4]
        coefficient_groups.setdefault(key, {})[(0, 0, 0, 0, monomial[4])] = int(coefficient)
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
        **compiled,
        "status": "COMPLETE",
        "resultant_shape": shape(resultant),
        "projected_shape": shape(reduced),
        "projected_pseudo_steps": steps,
        "content": content.str(),
        "content_shape": shape(content),
        "primitive_shape": shape(primitive),
        "primitive_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "primitive_zlib_base64": compressed,
        "primitive_chars": len(text),
        "compressed_chars": len(compressed),
    }


@app.local_entrypoint()
def main():
    source_hash = hashlib.sha256(PLANE.read_bytes()).hexdigest()
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell3-w2-resultant-v1",
        "scope": (
            "Necessary colored-source-square elimination on the main cell-3 "
            "plane chart; no unit, orbit, route, K3, or Prize claim."
        ),
        "source_plane_sha256": source_hash,
        "status": "CHECKPOINT",
        "cut_summary": summarize_cuts.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    try:
        result = eliminate_w.remote()
        compressed = base64.b64decode(result.pop("primitive_zlib_base64"))
        polynomial = zlib.decompress(compressed).decode()
        POLYNOMIAL.write_text(polynomial + "\n")
        result["polynomial_file"] = POLYNOMIAL.name
        result["polynomial_file_sha256"] = hashlib.sha256(
            POLYNOMIAL.read_bytes()
        ).hexdigest()
        output["status"] = "COMPLETE"
        output["result"] = result
    except Exception as error:
        output["status"] = "REMOTE_ERROR"
        output["error"] = repr(error)
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "status": output["status"],
        "cut_summary": output["cut_summary"],
        "result_summary": {
            key: value for key, value in output.get("result", {}).items()
            if key not in ("product", "sum")
        },
        "error": output.get("error"),
    }, sort_keys=True))
