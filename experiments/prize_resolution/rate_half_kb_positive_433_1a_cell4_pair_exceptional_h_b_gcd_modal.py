#!/usr/bin/env python3
"""Recover the common b divisor over the exceptional H curve."""

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
LIVE = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_resultant_factor_2.txt"
LINEAR = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_w1_reconstruction_linear_factor_0.txt"
CONSTANT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_w1_reconstruction_constant_factor_1.txt"
HFACTOR = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_common_factor_6.txt"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_b_gcd_result.json"
BGCD = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_b_gcd_polynomial.txt"
REMOTE = {
    PLANE: "/root/plane.json",
    LIVE: "/root/live.txt",
    LINEAR: "/root/linear.txt",
    CONSTANT: "/root/constant.txt",
    HFACTOR: "/root/hfactor.txt",
}
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell4-exceptional-h-b-gcd")
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
def compute_common_divisor():
    from flint import fmpz_mod_mpoly_ctx

    context = fmpz_mod_mpoly_ctx.get(["w0", "b", "t"], PRIME)
    _, b, _ = context.gens()

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
            key = tuple(exponents[name] for name in ("w0", "b", "t"))
            output[key] = (output.get(key, 0)+sign*coefficient) % PRIME
        return context.from_dict({key: coefficient for key, coefficient in
                                  output.items() if coefficient})

    plane_payload = json.loads(Path(REMOTE[PLANE]).read_text())["result"]
    polynomials = {
        "plane": parse_polynomial(plane_payload["plane_polynomial"]),
        "linear": parse_polynomial(Path(REMOTE[LINEAR]).read_text().strip()),
        "constant": parse_polynomial(Path(REMOTE[CONSTANT]).read_text().strip()),
        "live": parse_polynomial(Path(REMOTE[LIVE]).read_text().strip()),
    }
    hfactor = parse_polynomial(Path(REMOTE[HFACTOR]).read_text().strip())

    def coefficient_at_b_degree(polynomial, degree):
        return context.from_dict({
            (monomial[0], 0, monomial[2]): int(coefficient)
            for monomial, coefficient in polynomial.to_dict().items()
            if monomial[1] == degree
        })

    h_degree = int(hfactor.degrees()[0])

    def coefficient_at_w0_degree(polynomial, degree):
        return context.from_dict({
            (0, monomial[1], monomial[2]): int(coefficient)
            for monomial, coefficient in polynomial.to_dict().items()
            if monomial[0] == degree
        })

    h_leading = coefficient_at_w0_degree(hfactor, h_degree)

    def reduce_by_h(polynomial):
        reduced = polynomial
        reduction_steps = 0
        while int(reduced.degrees()[0]) >= h_degree:
            old_degree = int(reduced.degrees()[0])
            coefficient = coefficient_at_w0_degree(reduced, old_degree)
            reduced = (
                h_leading*reduced
                -coefficient*context.gens()[0]**(old_degree-h_degree)*hfactor
            )
            if int(reduced.degrees()[0]) >= old_degree:
                raise RuntimeError("H pseudo-division did not lower w0 degree")
            reduction_steps += 1
        return reduced, reduction_steps

    def pseudo_remainder(dividend, divisor):
        divisor_degree = int(divisor.degrees()[1])
        leading = coefficient_at_b_degree(divisor, divisor_degree)
        remainder = dividend
        steps = 0
        h_steps = 0
        while int(remainder.degrees()[1]) >= divisor_degree:
            old_degree = int(remainder.degrees()[1])
            coefficient = coefficient_at_b_degree(remainder, old_degree)
            remainder = (
                leading*remainder
                -coefficient*b**(old_degree-divisor_degree)*divisor
            )
            remainder, new_h_steps = reduce_by_h(remainder)
            h_steps += new_h_steps
            if int(remainder.degrees()[1]) >= old_degree:
                raise RuntimeError("b pseudo-division did not lower degree")
            steps += 1
        return remainder, steps, h_steps, leading

    reduced_polynomials = {}
    source_h_steps = {}
    for name, polynomial in polynomials.items():
        reduced_polynomials[name], source_h_steps[name] = reduce_by_h(polynomial)

    quadratic, quadratic_steps, quadratic_h_steps, linear_leading = pseudo_remainder(
        reduced_polynomials["plane"], reduced_polynomials["linear"]
    )
    if int(quadratic.degrees()[1]) != 2:
        raise RuntimeError("candidate common divisor is not quadratic")
    quadratic_coefficients = [
        coefficient_at_b_degree(quadratic, degree) for degree in range(3)
    ]
    quadratic_content = functools.reduce(
        lambda left, right: left.gcd(right), quadratic_coefficients
    )
    quadratic, quadratic_content_remainder = divmod(
        quadratic, quadratic_content
    )
    if not quadratic_content_remainder.is_zero():
        raise RuntimeError("quadratic content division failed")

    candidate, linear_steps, linear_h_steps, quadratic_leading = pseudo_remainder(
        reduced_polynomials["linear"], quadratic
    )
    if int(candidate.degrees()[1]) != 1:
        raise RuntimeError("candidate common divisor is not linear")
    candidate_coefficients = [
        coefficient_at_b_degree(candidate, degree) for degree in range(2)
    ]
    candidate_content = functools.reduce(
        lambda left, right: left.gcd(right), candidate_coefficients
    )
    candidate, candidate_content_remainder = divmod(candidate, candidate_content)
    if not candidate_content_remainder.is_zero():
        raise RuntimeError("linear content division failed")

    content_scalar, content_factors = candidate_content.factor()
    content_reconstruction = context.constant(int(content_scalar))
    content_rows = []
    for factor, multiplicity in content_factors:
        content_reconstruction *= factor**multiplicity
        content_rows.append({
            "shape": shape(factor), "multiplicity": int(multiplicity),
            "sha256": hashlib.sha256(factor.str().encode()).hexdigest(),
            "text": factor.str(),
        })
    if content_reconstruction != candidate_content:
        raise RuntimeError("candidate content reconstruction failed")

    divisibility = {}
    for name in ("plane", "linear", "constant", "live"):
        remainder, steps, remainder_h_steps, leading = pseudo_remainder(
            reduced_polynomials[name], candidate
        )
        coefficient_rows = []
        for degree in range(max(0, int(remainder.degrees()[1]))+1):
            coefficient = coefficient_at_b_degree(remainder, degree)
            coefficient_rows.append({
                "degree": degree, "shape": shape(coefficient),
                "sha256": hashlib.sha256(coefficient.str().encode()).hexdigest(),
                "zero_mod_h": coefficient.is_zero(),
            })
        divisibility[name] = {
            "steps": steps, "h_steps": remainder_h_steps,
            "leading_shape": shape(leading),
            "remainder_shape": shape(remainder),
            "coefficients": coefficient_rows,
        }

    candidate_text = candidate.str()
    return {
        "status": "COMPLETE", "field": PRIME,
        "h_shape": shape(hfactor),
        "h_leading_shape": shape(h_leading),
        "source_h_steps": source_h_steps,
        "quadratic": {
            "shape": shape(quadratic),
            "steps": quadratic_steps,
            "h_steps": quadratic_h_steps,
            "content_shape": shape(quadratic_content),
        },
        "candidate_steps": linear_steps,
        "candidate_h_steps": linear_h_steps,
        "linear_leading_shape": shape(linear_leading),
        "quadratic_leading_shape": shape(quadratic_leading),
        "candidate_content": {
            "shape": shape(candidate_content),
            "sha256": hashlib.sha256(candidate_content.str().encode()).hexdigest(),
            "content": int(content_scalar), "factors": content_rows,
        },
        "candidate_shape": shape(candidate),
        "candidate_sha256": hashlib.sha256(candidate_text.encode()).hexdigest(),
        "candidate_zlib_base64": base64.b64encode(
            zlib.compress(candidate_text.encode(), level=9)
        ).decode(),
        "divisibility": divisibility,
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell4-pair-exceptional-h-b-gcd-v3",
        "scope": (
            "Exact linear b-subresultant over the exceptional H projection "
            "and coefficientwise H-divisibility tests for plane,L,M,F. "
            "Leading/content exceptional loci and deployed points remain "
            "separate; no colored, orbit, or Prize claim."
        ),
        "artifact_sha256": {
            path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in REMOTE
        },
        "result": compute_common_divisor.remote(),
    }
    result = output["result"]
    text = zlib.decompress(
        base64.b64decode(result.pop("candidate_zlib_base64"))
    ).decode()
    BGCD.write_text(text+"\n")
    result["candidate_file"] = BGCD.name
    result["candidate_file_sha256"] = hashlib.sha256(BGCD.read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT), "status": result["status"],
        "h_shape": result["h_shape"],
        "candidate_shape": result["candidate_shape"],
        "candidate_content": result["candidate_content"],
        "divisibility": result["divisibility"],
    }, sort_keys=True))
