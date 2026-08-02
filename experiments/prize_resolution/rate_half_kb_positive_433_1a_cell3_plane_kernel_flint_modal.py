#!/usr/bin/env python3
"""Clear the cell-3 plane-chart kernel denominators with FLINT."""

import hashlib
import json
from pathlib import Path
import re

import modal


DIRECTORY = Path(__file__).parent
SCOUT = DIRECTORY / "rate_half_kb_positive_433_1a_cell3_common_triangle_scout_result.json"
KERNEL = DIRECTORY / "rate_half_kb_positive_433_1a_cell3_kernel_reduction_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell3_plane_kernel_flint_result.json"
REMOTE_SCOUT = "/root/cell3_triangle_scout.json"
REMOTE_KERNEL = "/root/cell3_kernel_reduction.json"
PRIME = 2130706433
NAMES = ("a20", "a21", "a22", "a00", "a01", "a02", "b10", "b11")

app = modal.App("rs-mca-positive-433-1a-cell3-plane-kernel-flint")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
    .add_local_file(SCOUT, REMOTE_SCOUT)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


@app.function(image=image, cpu=2.0, memory=8192, timeout=240)
def clear_denominators():
    import functools

    from flint import fmpz_mod_mpoly_ctx

    def parse_polynomial(value):
        output = {}
        for raw_term in re.findall(r"[+-]?[^+-]+", value):
            sign = 1
            term = raw_term
            if term.startswith("+"):
                term = term[1:]
            elif term.startswith("-"):
                sign = -1
                term = term[1:]
            coefficient_match = re.match(r"\d+", term)
            if coefficient_match:
                coefficient = int(coefficient_match.group(0))
                term = term[coefficient_match.end():]
            else:
                coefficient = 1
            exponents = {name: 0 for name in "crbt"}
            while term:
                variable_match = re.match(r"([crbt])(\d*)", term)
                if variable_match is None:
                    raise RuntimeError(f"cannot parse monomial tail {term!r}")
                variable, exponent = variable_match.groups()
                exponents[variable] += int(exponent) if exponent else 1
                term = term[variable_match.end():]
            key = tuple(exponents[name] for name in "crbt")
            output[key] = (output.get(key, 0) + sign*coefficient) % PRIME
        return {key: value for key, value in output.items() if value}

    scout = json.loads(Path(REMOTE_SCOUT).read_text())
    scout_row = next(item for item in scout["rows"]
                     if item.get("order") == ["c", "r", "b", "t"])
    basis_text = re.findall(
        r"^GP\[\d+\]=(.*)$", scout_row["stdout"], re.MULTILINE,
    )
    kernel = json.loads(Path(REMOTE_KERNEL).read_text())["result"]
    if len(basis_text) != 7:
        raise RuntimeError("unexpected cell-3 lex basis")

    context = fmpz_mod_mpoly_ctx.get(["b", "t"], PRIME)
    b, t = context.gens()

    def from_terms(terms, predicate, transform, scalar=1):
        payload = {}
        for exponents, coefficient in terms.items():
            if predicate(exponents):
                key = transform(exponents)
                payload[key] = (
                    payload.get(key, 0) + scalar*coefficient
                ) % PRIME
        return context.from_dict({key: value for key, value in payload.items()
                                  if value})

    r_terms = parse_polynomial(basis_text[1])
    r_denominator = from_terms(
        r_terms,
        lambda exponents: exponents[0] == 0 and exponents[1] == 1,
        lambda exponents: (exponents[2], exponents[3]),
    )
    r_numerator = from_terms(
        r_terms,
        lambda exponents: exponents[0] == 0 and exponents[1] == 0,
        lambda exponents: (exponents[2], exponents[3]),
        scalar=-1,
    )
    if any(exponents[0] or exponents[1] > 1 for exponents in r_terms):
        raise RuntimeError("r equation is not linear")

    c_terms = parse_polynomial(basis_text[4])
    c_denominator_0 = from_terms(
        c_terms,
        lambda exponents: exponents[0] == 1,
        lambda exponents: (exponents[2], exponents[3]),
    )
    c_r_part = from_terms(
        c_terms,
        lambda exponents: exponents[0] == 0 and exponents[1] == 1,
        lambda exponents: (exponents[2], exponents[3]),
    )
    c_base_part = from_terms(
        c_terms,
        lambda exponents: exponents[0] == 0 and exponents[1] == 0,
        lambda exponents: (exponents[2], exponents[3]),
    )
    if any(exponents[0] > 1 or exponents[1] > 1 for exponents in c_terms):
        raise RuntimeError("c equation is not bilinear")
    c_numerator = -(c_r_part*r_numerator + c_base_part*r_denominator)
    c_denominator = c_denominator_0*r_denominator

    powers_c_num = [context.constant(1)]
    powers_c_den = [context.constant(1)]
    powers_r_num = [context.constant(1)]
    powers_r_den = [context.constant(1)]
    for _ in range(3):
        powers_c_num.append(powers_c_num[-1]*c_numerator)
        powers_c_den.append(powers_c_den[-1]*c_denominator)
    for _ in range(6):
        powers_r_num.append(powers_r_num[-1]*r_numerator)
        powers_r_den.append(powers_r_den[-1]*r_denominator)

    def substitute_cleared(value):
        output = context.constant(0)
        for (ec, er, eb, et), coefficient in parse_polynomial(value).items():
            output += (
                coefficient
                * powers_c_num[ec] * powers_c_den[3-ec]
                * powers_r_num[er] * powers_r_den[6-er]
                * b**eb * t**et
            )
        return output

    cleared = {
        name: substitute_cleared(kernel["reduced_coefficients"][name])
        for name in NAMES
    }
    common_gcd = functools.reduce(lambda left, right: left.gcd(right),
                                  cleared.values())
    preprojection_polynomials = {}
    for name, polynomial in cleared.items():
        quotient, remainder = divmod(polynomial, common_gcd)
        if not remainder.is_zero():
            raise RuntimeError(f"nonexact common scale division: {name}")
        preprojection_polynomials[name] = quotient
    if not (preprojection_polynomials["b10"]
            + preprojection_polynomials["b11"]).is_zero():
        raise RuntimeError("B1 factor did not survive denominator clearing")

    plane_terms = parse_polynomial(basis_text[0])
    plane = context.from_dict({
        (exponents[2], exponents[3]): coefficient
        for exponents, coefficient in plane_terms.items()
    })
    plane_leading = context.from_dict({
        (0, exponents[3]): coefficient
        for exponents, coefficient in plane_terms.items()
        if exponents[2] == 4
    })
    if plane_leading.is_zero():
        raise RuntimeError("missing plane leading coefficient")

    def coefficient_at_b_degree(polynomial, degree):
        return context.from_dict({
            (0, monomial[1]): int(coefficient)
            for monomial, coefficient in polynomial.to_dict().items()
            if monomial[0] == degree
        })

    def pseudo_remainder(polynomial):
        remainder = polynomial
        steps = 0
        while int(remainder.degrees()[0]) >= 4:
            old_degree = int(remainder.degrees()[0])
            leading = coefficient_at_b_degree(remainder, old_degree)
            remainder = (
                plane_leading*remainder
                - leading*b**(old_degree-4)*plane
            )
            new_degree = int(remainder.degrees()[0])
            if new_degree >= old_degree:
                raise RuntimeError("pseudo-division did not lower b degree")
            steps += 1
        return remainder, steps

    projected_rows = {
        name: pseudo_remainder(polynomial)
        for name, polynomial in preprojection_polynomials.items()
    }
    pseudo_scale_power = max(steps for _, steps in projected_rows.values())
    projected_aligned = {
        name: polynomial*plane_leading**(pseudo_scale_power-steps)
        for name, (polynomial, steps) in projected_rows.items()
    }
    projected_gcd = functools.reduce(
        lambda left, right: left.gcd(right), projected_aligned.values()
    )
    normalized = {}
    normalized_polynomials = {}
    for name, polynomial in projected_aligned.items():
        quotient, remainder = divmod(polynomial, projected_gcd)
        if not remainder.is_zero():
            raise RuntimeError(f"nonexact projected scale division: {name}")
        normalized_polynomials[name] = quotient
        normalized[name] = {
            "polynomial": quotient.str(),
            "degrees": [int(value) for value in quotient.degrees()],
            "total_degree": int(quotient.total_degree()),
            "terms": len(list(quotient.terms())),
        }
    if not (normalized_polynomials["b10"]
            + normalized_polynomials["b11"]).is_zero():
        raise RuntimeError("B1 factor did not survive plane projection")

    def shape(polynomial):
        return {
            "degrees": [int(value) for value in polynomial.degrees()],
            "total_degree": int(polynomial.total_degree()),
            "terms": len(list(polynomial.terms())),
        }

    denominator_scale = powers_c_den[3] * powers_r_den[6]
    return {
        "status": "COMPLETE",
        "field": PRIME,
        "cell": 3,
        "epsilon": [-1, -1],
        "source_scout_sha256": hashlib.sha256(
            Path(REMOTE_SCOUT).read_bytes()
        ).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(
            Path(REMOTE_KERNEL).read_bytes()
        ).hexdigest(),
        "plane_polynomial": plane.str(),
        "plane_shape": {
            "degrees": [int(value) for value in plane.degrees()],
            "total_degree": int(plane.total_degree()),
            "terms": len(list(plane.terms())),
        },
        "r_numerator": r_numerator.str(),
        "r_denominator": r_denominator.str(),
        "c_numerator": c_numerator.str(),
        "c_denominator": c_denominator.str(),
        "denominator_scale": denominator_scale.str(),
        "denominator_scale_shape": {
            "degrees": [int(value) for value in denominator_scale.degrees()],
            "total_degree": int(denominator_scale.total_degree()),
            "terms": len(list(denominator_scale.terms())),
        },
        "common_projective_scale": common_gcd.str(),
        "common_projective_scale_shape": {
            "degrees": [int(value) for value in common_gcd.degrees()],
            "total_degree": int(common_gcd.total_degree()),
            "terms": len(list(common_gcd.terms())),
        },
        "preprojection_shapes": {
            name: shape(polynomial)
            for name, polynomial in preprojection_polynomials.items()
        },
        "plane_leading_coefficient": plane_leading.str(),
        "plane_leading_shape": shape(plane_leading),
        "pseudo_scale_power": pseudo_scale_power,
        "projected_common_scale": projected_gcd.str(),
        "projected_common_scale_shape": shape(projected_gcd),
        "normalized_coefficients": normalized,
        "b1_opposite": True,
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell3-plane-kernel-flint-v1",
        "scope": (
            "Exact large-prime denominator clearing and common-scale removal "
            "on the cell-3 plane chart; denominator and common-scale zero "
            "strata remain separate and no outside, route, K3, or Prize claim."
        ),
        "result": clear_denominators.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "status": output["result"].get("status"),
        "plane_shape": output["result"].get("plane_shape"),
        "denominator_scale_shape": output["result"].get(
            "denominator_scale_shape"
        ),
        "common_projective_scale_shape": output["result"].get(
            "common_projective_scale_shape"
        ),
        "coefficient_shapes": {
            name: {
                key: value[key]
                for key in ("degrees", "total_degree", "terms")
            }
            for name, value in output["result"].get(
                "normalized_coefficients", {}
            ).items()
        },
    }, sort_keys=True))
