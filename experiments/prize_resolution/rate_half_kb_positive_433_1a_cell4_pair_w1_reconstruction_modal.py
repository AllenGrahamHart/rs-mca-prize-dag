#!/usr/bin/env python3
"""Compute a linear w1 reconstruction for the cell-4 signed pair."""

import base64
import functools
import hashlib
import importlib.util
import json
from pathlib import Path
import zlib

import modal


DIRECTORY = Path(__file__).parent
PAIR_SOURCE = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_w1_resultant_modal.py"
PLANE = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_plane_kernel_flint_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_w1_reconstruction_result.json"
REMOTE_PAIR_SOURCE = "/root/cell4_pair_w1_resultant.py"
REMOTE_PLANE = "/root/cell4_plane_kernel_flint.json"

app = modal.App("rs-mca-positive-433-1a-cell4-pair-w1-reconstruction")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
    .add_local_file(PAIR_SOURCE, REMOTE_PAIR_SOURCE)
    .add_local_file(PLANE, REMOTE_PLANE)
)


def shape(polynomial):
    return {
        "degrees": [int(value) for value in polynomial.degrees()],
        "total_degree": int(polynomial.total_degree()),
        "terms": len(list(polynomial.terms())),
    }


def compressed_row(polynomial, multiplicity=None):
    text = polynomial.str()
    row = {
        **shape(polynomial),
        "sha256": hashlib.sha256(text.encode()).hexdigest(),
        "zlib_base64": base64.b64encode(
            zlib.compress(text.encode(), level=9)
        ).decode(),
    }
    if multiplicity is not None:
        row["multiplicity"] = int(multiplicity)
    return row


@app.function(image=image, cpu=4.0, memory=8192, timeout=300)
def reconstruct_w1():
    spec = importlib.util.spec_from_file_location("cell4_pair", REMOTE_PAIR_SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    summary, context, product, sum_cut, plane, plane_leading = module.compile_pair(
        include_objects=True
    )
    w1, _, b, _ = context.gens()

    def coefficient_at_w1_degree(polynomial, degree):
        return context.from_dict({
            (0, monomial[1], monomial[2], monomial[3]): int(coefficient)
            for monomial, coefficient in polynomial.to_dict().items()
            if monomial[0] == degree
        })

    divisor_degree = int(product.degrees()[0])
    if divisor_degree != 2 or int(sum_cut.degrees()[0]) != 4:
        raise RuntimeError("unexpected signed-pair degrees")
    leading = coefficient_at_w1_degree(product, divisor_degree)
    remainder = sum_cut
    steps = 0
    quotient_terms = []
    while int(remainder.degrees()[0]) >= divisor_degree:
        old_degree = int(remainder.degrees()[0])
        coefficient = coefficient_at_w1_degree(remainder, old_degree)
        shift = old_degree-divisor_degree
        remainder = leading*remainder-coefficient*w1**shift*product
        quotient_terms.append((steps, shift, compressed_row(coefficient)))
        if int(remainder.degrees()[0]) >= old_degree:
            raise RuntimeError("w1 pseudo-division did not lower degree")
        steps += 1
    if int(remainder.degrees()[0]) != 1:
        raise RuntimeError("signed-pair remainder is not linear")

    original_resultant = product.resultant(sum_cut, "w1")
    remainder_resultant = product.resultant(remainder, "w1")
    resultant_leading_exponent = (
        int(remainder.degrees()[0])+steps*divisor_degree
        -int(sum_cut.degrees()[0])
    )
    expected = leading**resultant_leading_exponent*original_resultant
    if remainder_resultant != expected:
        raise RuntimeError("pseudo-remainder resultant identity failed")

    constant = coefficient_at_w1_degree(remainder, 0)
    linear = coefficient_at_w1_degree(remainder, 1)

    def coefficient_at_b_degree(polynomial, degree):
        return context.from_dict({
            (monomial[0], monomial[1], 0, monomial[3]): int(coefficient)
            for monomial, coefficient in polynomial.to_dict().items()
            if monomial[2] == degree
        })

    def reduce_by_plane(polynomial):
        reduced = polynomial
        reduction_steps = 0
        while int(reduced.degrees()[2]) >= 4:
            old_degree = int(reduced.degrees()[2])
            coefficient = coefficient_at_b_degree(reduced, old_degree)
            reduced = (
                plane_leading*reduced
                -coefficient*b**(old_degree-4)*plane
            )
            if int(reduced.degrees()[2]) >= old_degree:
                raise RuntimeError("plane pseudo-division did not lower b degree")
            reduction_steps += 1
        return reduced, reduction_steps

    compact_linear, linear_plane_steps = reduce_by_plane(linear)
    compact_constant, constant_plane_steps = reduce_by_plane(constant)
    if linear_plane_steps != constant_plane_steps:
        raise RuntimeError("reconstruction coefficients have unequal plane scales")

    content_coefficients = []
    for polynomial in (compact_linear, compact_constant):
        groups = {}
        for monomial, coefficient in polynomial.to_dict().items():
            key = monomial[:3]
            groups.setdefault(key, {})[(0, 0, 0, monomial[3])] = int(coefficient)
        content_coefficients.extend(
            context.from_dict(value) for value in groups.values()
        )
    common_content = functools.reduce(
        lambda left, right: left.gcd(right), content_coefficients
    )
    compact_linear, linear_content_remainder = divmod(
        compact_linear, common_content
    )
    compact_constant, constant_content_remainder = divmod(
        compact_constant, common_content
    )
    if not linear_content_remainder.is_zero() or not constant_content_remainder.is_zero():
        raise RuntimeError("reconstruction content division was not exact")
    common_polynomial = compact_linear.gcd(compact_constant)
    compact_linear, linear_gcd_remainder = divmod(
        compact_linear, common_polynomial
    )
    compact_constant, constant_gcd_remainder = divmod(
        compact_constant, common_polynomial
    )
    if not linear_gcd_remainder.is_zero() or not constant_gcd_remainder.is_zero():
        raise RuntimeError("reconstruction polynomial gcd division was not exact")

    discarded_factors = {}
    for name, polynomial in (("plane_content", common_content),
                             ("polynomial_gcd", common_polynomial)):
        content, factors = polynomial.factor()
        reconstruction = context.constant(int(content))
        rows = []
        for factor, multiplicity in factors:
            reconstruction *= factor**multiplicity
            rows.append(compressed_row(factor, multiplicity))
        if reconstruction != polynomial:
            raise RuntimeError(f"{name} factor reconstruction failed")
        discarded_factors[name] = {
            "content": int(content),
            "shape": shape(polynomial),
            "sha256": hashlib.sha256(polynomial.str().encode()).hexdigest(),
            "factors": rows,
        }

    factor_rows = {}
    for name, polynomial in (("leading", leading),
                             ("linear", compact_linear),
                             ("constant", compact_constant)):
        content, factors = polynomial.factor()
        reconstruction = context.constant(int(content))
        rows = []
        for factor, multiplicity in factors:
            reconstruction *= factor**multiplicity
            rows.append(compressed_row(factor, multiplicity))
        if reconstruction != polynomial:
            raise RuntimeError(f"{name} factor reconstruction failed")
        factor_rows[name] = {
            "content": int(content),
            "shape": shape(polynomial),
            "sha256": hashlib.sha256(polynomial.str().encode()).hexdigest(),
            "factors": rows,
        }

    return {
        "status": "COMPLETE",
        "pair_summary": summary,
        "product_shape": shape(product),
        "sum_shape": shape(sum_cut),
        "pseudo_steps": steps,
        "remainder_shape": shape(remainder),
        "remainder_sha256": hashlib.sha256(
            remainder.str().encode()
        ).hexdigest(),
        "resultant_identity": {
            "verified": True,
            "leading_exponent": resultant_leading_exponent,
            "original_shape": shape(original_resultant),
            "remainder_shape": shape(remainder_resultant),
            "original_sha256": hashlib.sha256(
                original_resultant.str().encode()
            ).hexdigest(),
            "remainder_sha256": hashlib.sha256(
                remainder_resultant.str().encode()
            ).hexdigest(),
        },
        "coefficients": factor_rows,
        "raw_coefficients": {
            "linear": {
                "shape": shape(linear),
                "sha256": hashlib.sha256(linear.str().encode()).hexdigest(),
            },
            "constant": {
                "shape": shape(constant),
                "sha256": hashlib.sha256(constant.str().encode()).hexdigest(),
            },
        },
        "plane_reduction": {
            "steps": linear_plane_steps,
            "discarded_factors": discarded_factors,
            "compact_remainder_shape": shape(
                compact_linear*w1+compact_constant
            ),
        },
        "quotient_step_coefficients": quotient_terms,
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell4-pair-w1-reconstruction-v3",
        "scope": (
            "Exact pseudo-remainder reconstruction for w1 in the necessary "
            "signed-pair ideal; no exceptional-coefficient, colored, orbit, "
            "or Prize claim."
        ),
        "source_pair_sha256": hashlib.sha256(PAIR_SOURCE.read_bytes()).hexdigest(),
        "source_plane_sha256": hashlib.sha256(PLANE.read_bytes()).hexdigest(),
        "result": reconstruct_w1.remote(),
    }
    for pattern in (
        "rate_half_kb_positive_433_1a_cell4_pair_w1_reconstruction_"
        "leading_factor_*.txt",
        "rate_half_kb_positive_433_1a_cell4_pair_w1_reconstruction_"
        "linear_factor_*.txt",
        "rate_half_kb_positive_433_1a_cell4_pair_w1_reconstruction_"
        "constant_factor_*.txt",
        "rate_half_kb_positive_433_1a_cell4_pair_w1_reconstruction_"
        "discarded_*_factor_*.txt",
        "rate_half_kb_positive_433_1a_cell4_pair_w1_reconstruction_content.txt",
    ):
        for path in DIRECTORY.glob(pattern):
            path.unlink()

    def materialize_factor_rows(prefix, rows):
        for index, row in enumerate(rows):
            text = zlib.decompress(base64.b64decode(row.pop("zlib_base64"))).decode()
            filename = (
                "rate_half_kb_positive_433_1a_cell4_pair_w1_reconstruction_"
                f"{prefix}_factor_{index}.txt"
            )
            path = DIRECTORY / filename
            path.write_text(text+"\n")
            row["file"] = filename
            row["file_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()

    for coefficient_name, coefficient in output["result"]["coefficients"].items():
        materialize_factor_rows(coefficient_name, coefficient["factors"])
    discarded = output["result"]["plane_reduction"]["discarded_factors"]
    for name, row in discarded.items():
        materialize_factor_rows(f"discarded_{name}", row["factors"])
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT),
        "status": output["result"]["status"],
        "pseudo_steps": output["result"]["pseudo_steps"],
        "remainder_shape": output["result"]["remainder_shape"],
        "resultant_identity": output["result"]["resultant_identity"],
        "coefficients": output["result"]["coefficients"],
    }, sort_keys=True))
