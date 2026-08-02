#!/usr/bin/env python3
"""Clear the cell-4 plane-chart kernel denominators with FLINT."""

import hashlib
import json
from pathlib import Path
import re

import modal


DIRECTORY = Path(__file__).parent
SCOUT = DIRECTORY / "rate_half_kb_positive_433_1a_remaining_lex_scout_result.json"
KERNEL = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_kernel_reduction_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_plane_kernel_flint_result.json"
REMOTE_SCOUT = "/root/remaining_lex_scout.json"
REMOTE_KERNEL = "/root/cell4_kernel_reduction.json"
PRIME = 2130706433
NAMES = ("a20", "a21", "a22", "a00", "a01", "a02", "b10", "b11")

app = modal.App("rs-mca-positive-433-1a-cell4-plane-kernel-flint")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
    .add_local_file(SCOUT, REMOTE_SCOUT)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


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
            match = re.match(r"\d+", term)
            coefficient = int(match.group(0)) if match else 1
            term = term[match.end():] if match else term
            exponents = {name: 0 for name in "crbt"}
            while term:
                match = re.match(r"([crbt])(\d*)", term)
                if match is None:
                    raise RuntimeError(f"cannot parse monomial tail {term!r}")
                variable, exponent = match.groups()
                exponents[variable] += int(exponent) if exponent else 1
                term = term[match.end():]
            key = tuple(exponents[name] for name in "crbt")
            output[key] = (output.get(key, 0)+sign*coefficient) % PRIME
        return {key: coefficient for key, coefficient in output.items()
                if coefficient}

    scout_bytes = Path(REMOTE_SCOUT).read_bytes()
    kernel_bytes = Path(REMOTE_KERNEL).read_bytes()
    scout = json.loads(scout_bytes)
    row = next(item for item in scout["rows"]
               if item.get("cell") == 4
               and item.get("order") == ["c", "r", "b", "t"])
    basis = re.findall(r"^GP\[\d+\]=(.*)$", row["stdout"], re.MULTILINE)
    kernel = json.loads(kernel_bytes)["result"]
    if len(basis) != 7:
        raise RuntimeError("unexpected cell-4 lex basis")

    context = fmpz_mod_mpoly_ctx.get(["b", "t"], PRIME)
    b, t = context.gens()

    def from_terms(terms, predicate, transform, scalar=1):
        payload = {}
        for exponents, coefficient in terms.items():
            if predicate(exponents):
                key = transform(exponents)
                payload[key] = (payload.get(key, 0)+scalar*coefficient) % PRIME
        return context.from_dict({key: coefficient for key, coefficient in
                                  payload.items() if coefficient})

    r_terms = parse_polynomial(basis[1])
    r_denominator = from_terms(
        r_terms, lambda e: e[0] == 0 and e[1] == 1,
        lambda e: (e[2], e[3]),
    )
    r_numerator = from_terms(
        r_terms, lambda e: e[0] == 0 and e[1] == 0,
        lambda e: (e[2], e[3]), scalar=-1,
    )
    if any(e[0] or e[1] > 1 for e in r_terms):
        raise RuntimeError("r equation is not linear")

    c_terms = parse_polynomial(basis[4])
    c_denominator_0 = from_terms(
        c_terms, lambda e: e[0] == 1, lambda e: (e[2], e[3]),
    )
    c_r_part = from_terms(
        c_terms, lambda e: e[0] == 0 and e[1] == 1,
        lambda e: (e[2], e[3]),
    )
    c_base_part = from_terms(
        c_terms, lambda e: e[0] == 0 and e[1] == 0,
        lambda e: (e[2], e[3]),
    )
    if any(e[0] > 1 or e[1] > 1 for e in c_terms):
        raise RuntimeError("c equation is not bilinear")
    c_numerator = -(c_r_part*r_numerator+c_base_part*r_denominator)
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
                * powers_c_num[ec]*powers_c_den[3-ec]
                * powers_r_num[er]*powers_r_den[6-er]
                * b**eb*t**et
            )
        return output

    cleared = {name: substitute_cleared(kernel["reduced_coefficients"][name])
               for name in NAMES}
    common_gcd = functools.reduce(lambda left, right: left.gcd(right),
                                  cleared.values())
    preprojection = {}
    for name, polynomial in cleared.items():
        quotient, remainder = divmod(polynomial, common_gcd)
        if not remainder.is_zero():
            raise RuntimeError(f"nonexact common division: {name}")
        preprojection[name] = quotient
    if not (preprojection["b10"]+preprojection["b11"]).is_zero():
        raise RuntimeError("B1 opposition lost before projection")

    plane_terms = parse_polynomial(basis[0])
    plane = context.from_dict({(e[2], e[3]): coefficient
                               for e, coefficient in plane_terms.items()})
    plane_leading = context.from_dict({
        (0, e[3]): coefficient for e, coefficient in plane_terms.items()
        if e[2] == 4
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
            remainder = plane_leading*remainder-leading*b**(old_degree-4)*plane
            if int(remainder.degrees()[0]) >= old_degree:
                raise RuntimeError("pseudo-division did not lower b degree")
            steps += 1
        return remainder, steps

    projected_rows = {name: pseudo_remainder(polynomial)
                      for name, polynomial in preprojection.items()}
    pseudo_scale_power = max(steps for _, steps in projected_rows.values())
    aligned = {
        name: polynomial*plane_leading**(pseudo_scale_power-steps)
        for name, (polynomial, steps) in projected_rows.items()
    }
    projected_gcd = functools.reduce(lambda left, right: left.gcd(right),
                                     aligned.values())
    normalized = {}
    normalized_polynomials = {}
    for name, polynomial in aligned.items():
        quotient, remainder = divmod(polynomial, projected_gcd)
        if not remainder.is_zero():
            raise RuntimeError(f"nonexact projected division: {name}")
        normalized_polynomials[name] = quotient
        normalized[name] = {
            "polynomial": quotient.str(),
            "degrees": [int(value) for value in quotient.degrees()],
            "total_degree": int(quotient.total_degree()),
            "terms": len(list(quotient.terms())),
        }
    if not (normalized_polynomials["b10"]
            + normalized_polynomials["b11"]).is_zero():
        raise RuntimeError("B1 opposition lost after projection")

    def shape(polynomial):
        return {
            "degrees": [int(value) for value in polynomial.degrees()],
            "total_degree": int(polynomial.total_degree()),
            "terms": len(list(polynomial.terms())),
        }

    denominator_scale = powers_c_den[3]*powers_r_den[6]
    return {
        "status": "COMPLETE",
        "field": PRIME,
        "cell": 4,
        "epsilon": [-1, -1],
        "source_scout_sha256": hashlib.sha256(scout_bytes).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(kernel_bytes).hexdigest(),
        "plane_polynomial": plane.str(),
        "plane_shape": shape(plane),
        "r_numerator": r_numerator.str(),
        "r_denominator": r_denominator.str(),
        "c_numerator": c_numerator.str(),
        "c_denominator": c_denominator.str(),
        "denominator_scale": denominator_scale.str(),
        "denominator_scale_shape": shape(denominator_scale),
        "common_projective_scale": common_gcd.str(),
        "common_projective_scale_shape": shape(common_gcd),
        "preprojection_shapes": {name: shape(polynomial)
                                 for name, polynomial in preprojection.items()},
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
        "schema": "rate-half-kb-positive-433-1a-cell4-plane-kernel-flint-v1",
        "scope": (
            "Exact denominator clearing and common-scale removal on the "
            "cell-4 plane chart; no outside, route, K3, or Prize claim."
        ),
        "result": clear_denominators.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    result = output["result"]
    print(json.dumps({
        "result": str(RESULT), "status": result.get("status"),
        "plane_shape": result.get("plane_shape"),
        "denominator_scale_shape": result.get("denominator_scale_shape"),
        "common_projective_scale_shape": result.get("common_projective_scale_shape"),
        "projected_common_scale_shape": result.get("projected_common_scale_shape"),
        "pseudo_scale_power": result.get("pseudo_scale_power"),
        "coefficient_shapes": {
            name: {key: row[key] for key in ("degrees", "total_degree", "terms")}
            for name, row in result.get("normalized_coefficients", {}).items()
        },
    }, sort_keys=True))
