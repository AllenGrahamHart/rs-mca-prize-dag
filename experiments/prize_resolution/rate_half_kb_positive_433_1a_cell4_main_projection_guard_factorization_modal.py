#!/usr/bin/env python3
"""Certify the guarded factorization of the cell-4 main projection."""

import hashlib
import json
from pathlib import Path
import re

import modal


DIRECTORY = Path(__file__).parent
PLANE = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_plane_kernel_flint_result.json"
FPROJECTION = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_resultant_factor_2.txt"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_main_projection_guard_factorization_result.json"
REMOTE = {
    PLANE: "/root/plane.json",
    FPROJECTION: "/root/fprojection.txt",
}
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell4-main-guard-factorization")
image = modal.Image.debian_slim(python_version="3.12").pip_install(
    "python-flint==0.8.0"
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
def certify_factorization():
    from flint import fmpz_mod_mpoly_ctx

    context = fmpz_mod_mpoly_ctx.get(["w0", "b", "t"], PRIME)
    w0, b, _ = context.gens()

    def parse(value):
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
            exponents = {name: 0 for name in ("w0", "b", "t")}
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
        return context.from_dict({
            key: coefficient for key, coefficient in output.items() if coefficient
        })

    payload = json.loads(Path(REMOTE[PLANE]).read_text())["result"]
    plane = parse(payload["plane_polynomial"])
    plane_leading = parse(payload["plane_leading_coefficient"])
    fprojection = parse(Path(REMOTE[FPROJECTION]).read_text().strip())
    normalized = {
        name: parse(row["polynomial"])
        for name, row in payload["normalized_coefficients"].items()
    }
    rn = parse(payload["r_numerator"])
    rd = parse(payload["r_denominator"])

    n0 = normalized["a00"]+normalized["a01"]*w0+normalized["a02"]*w0*w0
    d0 = normalized["a20"]+normalized["a21"]*w0+normalized["a22"]*w0*w0
    source_guard = rd*rd*w0-rn*rn

    def coefficient_at_b_degree(polynomial, degree):
        return context.from_dict({
            (monomial[0], 0, monomial[2]): int(coefficient)
            for monomial, coefficient in polynomial.to_dict().items()
            if monomial[1] == degree
        })

    def reduce_by_plane(polynomial):
        reduced = polynomial
        steps = 0
        while int(reduced.degrees()[1]) >= 4:
            old_degree = int(reduced.degrees()[1])
            coefficient = coefficient_at_b_degree(reduced, old_degree)
            reduced = (
                plane_leading*reduced
                -coefficient*b**(old_degree-4)*plane
            )
            if int(reduced.degrees()[1]) >= old_degree:
                raise RuntimeError("plane pseudo-division did not lower b degree")
            steps += 1
        return reduced, steps

    reductions = []
    d0_fifth = d0
    for exponent in range(2, 6):
        d0_fifth, steps = reduce_by_plane(d0_fifth*d0)
        reductions.append({
            "operation": f"d0_power_{exponent}",
            "steps": steps,
            "shape": shape(d0_fifth),
        })
    source_guard, steps = reduce_by_plane(source_guard)
    reductions.append({
        "operation": "source_guard", "steps": steps,
        "shape": shape(source_guard),
    })
    candidate, steps = reduce_by_plane(n0*d0_fifth)
    reductions.append({
        "operation": "n0_times_d0_fifth", "steps": steps,
        "shape": shape(candidate),
    })
    candidate, steps = reduce_by_plane(candidate*source_guard)
    reductions.append({
        "operation": "times_source_guard", "steps": steps,
        "shape": shape(candidate),
    })
    plane_leading_exponent = sum(row["steps"] for row in reductions)

    quotient, remainder = divmod(candidate, fprojection)

    def coefficient_at_w0_degree(polynomial, degree):
        return context.from_dict({
            (0, monomial[1], monomial[2]): int(coefficient)
            for monomial, coefficient in polynomial.to_dict().items()
            if monomial[0] == degree
        })

    f_degree = int(fprojection.degrees()[0])
    candidate_degree = int(candidate.degrees()[0])
    if f_degree != 13 or candidate_degree != f_degree:
        raise RuntimeError("unexpected projection or candidate degree")
    f_leading = coefficient_at_w0_degree(fprojection, f_degree)
    candidate_leading = coefficient_at_w0_degree(candidate, candidate_degree)
    cross = candidate_leading*fprojection-f_leading*candidate
    cross, cross_steps = reduce_by_plane(cross)
    if not cross.is_zero():
        raise RuntimeError(f"quotient-ring cross identity failed: {shape(cross)}")

    leading_norm = plane.resultant(f_leading, "b")
    if any(value != 0 for value in leading_norm.degrees()[:2]):
        raise RuntimeError("leading norm is not univariate in t")

    def factor_rows(polynomial):
        scalar, factors = polynomial.factor()
        reconstruction = context.constant(int(scalar))
        rows = []
        for factor, multiplicity in factors:
            reconstruction *= factor**multiplicity
            rows.append({
                "multiplicity": int(multiplicity),
                "shape": shape(factor),
                "sha256": hashlib.sha256(factor.str().encode()).hexdigest(),
                "text": factor.str(),
            })
        if reconstruction != polynomial:
            raise RuntimeError("factor reconstruction failed")
        return int(scalar), rows

    norm_scalar, norm_factors = factor_rows(leading_norm)

    return {
        "status": "COMPLETE",
        "field": PRIME,
        "identity": "plane-reduced(N0*D0^5*(rd^2*w0-rn^2))=Q(t)*F",
        "plane_shape": shape(plane),
        "plane_leading": plane_leading.str(),
        "f_shape": shape(fprojection),
        "n0_shape": shape(n0),
        "d0_shape": shape(d0),
        "source_guard_shape": shape(source_guard),
        "reductions": reductions,
        "plane_leading_exponent": plane_leading_exponent,
        "candidate_shape": shape(candidate),
        "candidate_sha256": hashlib.sha256(candidate.str().encode()).hexdigest(),
        "ambient_division_diagnostic": {
            "quotient_shape": shape(quotient),
            "remainder_zero": remainder.is_zero(),
            "remainder_shape": shape(remainder),
        },
        "quotient_ring_cross_identity": {
            "verified": True,
            "plane_steps": cross_steps,
            "remainder_zero": True,
            "f_leading_shape": shape(f_leading),
            "f_leading_sha256": hashlib.sha256(
                f_leading.str().encode()
            ).hexdigest(),
            "candidate_leading_shape": shape(candidate_leading),
            "candidate_leading_sha256": hashlib.sha256(
                candidate_leading.str().encode()
            ).hexdigest(),
        },
        "f_leading_norm": {
            "content": norm_scalar,
            "shape": shape(leading_norm),
            "sha256": hashlib.sha256(leading_norm.str().encode()).hexdigest(),
            "factors": norm_factors,
        },
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell4-main-guard-factorization-v1",
        "scope": (
            "Exact plane-quotient factorization of the necessary degree-13 "
            "signed-pair projection into N0, D0^5, and the squared source-"
            "label guard. Guard invertibility, exceptional plane-leading "
            "fibers, orbit transport, and Prize consequences remain separate."
        ),
        "artifact_sha256": {
            path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in REMOTE
        },
        "result": certify_factorization.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    result = output["result"]
    print(json.dumps({
        "result": str(RESULT),
        "status": result["status"],
        "candidate_shape": result["candidate_shape"],
        "ambient_division_diagnostic": result["ambient_division_diagnostic"],
        "quotient_ring_cross_identity": result["quotient_ring_cross_identity"],
        "f_leading_norm": result["f_leading_norm"],
    }, sort_keys=True))
