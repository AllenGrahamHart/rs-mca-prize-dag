#!/usr/bin/env python3
"""Certify the guarded factorization of the cell-3 signed-pair resultant."""

import hashlib
import json
from pathlib import Path
import re

import modal


DIRECTORY = Path(__file__).parent
PLANE = DIRECTORY / "rate_half_kb_positive_433_1a_cell3_plane_kernel_flint_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell3_signed_pair_guard_factorization_result.json"
REMOTE_PLANE = "/root/plane.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell3-signed-pair-guard-factorization")
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


@app.function(image=image, cpu=4.0, memory=32768, timeout=600)
def certify():
    from flint import fmpz_mod_mpoly_ctx, fmpz_mod_poly_ctx

    context = fmpz_mod_mpoly_ctx.get(["w1", "w0", "b", "t"], PRIME)
    w1, w0, b, t = context.gens()

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
        return context.from_dict({
            key: coefficient for key, coefficient in output.items() if coefficient
        })

    payload = json.loads(Path(REMOTE_PLANE).read_text())["result"]
    plane = parse(payload["plane_polynomial"])
    plane_leading = parse(payload["plane_leading_coefficient"])
    normalized = {
        name: parse(row["polynomial"])
        for name, row in payload["normalized_coefficients"].items()
    }
    rn = parse(payload["r_numerator"])
    rd = parse(payload["r_denominator"])

    def evaluate_form(prefix, variable):
        return sum(
            normalized[f"{prefix}{index}"]*variable**index
            for index in range(3)
        )

    d0, d1 = evaluate_form("a2", w0), evaluate_form("a2", w1)
    n0, n1 = evaluate_form("a0", w0), evaluate_form("a0", w1)
    k = normalized["b10"]
    raw_product = n1*d0+n0*d1
    raw_square = (
        k*k*w0*(1-w0)*(1-w0)*d1*d1
        -k*k*w1*(1-w1)*(1-w1)*d0*d0
        -4*n0*d0*d1*d1
    )

    def coefficient_at_degree(polynomial, variable_index, degree):
        return context.from_dict({
            tuple(0 if index == variable_index else monomial[index]
                  for index in range(4)): int(coefficient)
            for monomial, coefficient in polynomial.to_dict().items()
            if monomial[variable_index] == degree
        })

    def reduce_by_plane(polynomial):
        reduced = polynomial
        steps = 0
        while int(reduced.degrees()[2]) >= 4:
            old_degree = int(reduced.degrees()[2])
            coefficient = coefficient_at_degree(reduced, 2, old_degree)
            reduced = (
                plane_leading*reduced
                -coefficient*b**(old_degree-4)*plane
            )
            if int(reduced.degrees()[2]) >= old_degree:
                raise RuntimeError("plane pseudo-division did not lower b degree")
            steps += 1
        return reduced, steps

    product, product_steps = reduce_by_plane(raw_product)
    square, square_steps = reduce_by_plane(raw_square)
    resultant = product.resultant(square, "w1")
    if int(resultant.degrees()[0]) != 0:
        raise RuntimeError("signed-pair resultant retained w1")
    projected, projected_steps = reduce_by_plane(resultant)
    projected_degree = int(projected.degrees()[1])
    if projected_degree != 16:
        raise RuntimeError(f"unexpected projected degree {projected_degree}")

    reductions = []
    d0_fifth = d0
    for exponent in range(2, 6):
        d0_fifth, steps = reduce_by_plane(d0_fifth*d0)
        reductions.append({
            "operation": f"d0_power_{exponent}", "steps": steps,
            "shape": shape(d0_fifth),
        })
    r_guard, steps = reduce_by_plane(rd*rd*w0-rn*rn)
    reductions.append({
        "operation": "r_guard", "steps": steps, "shape": shape(r_guard),
    })
    r_guard_squared, steps = reduce_by_plane(r_guard*r_guard)
    reductions.append({
        "operation": "r_guard_squared", "steps": steps,
        "shape": shape(r_guard_squared),
    })
    candidate, steps = reduce_by_plane(n0*d0_fifth)
    reductions.append({
        "operation": "n0_times_d0_fifth", "steps": steps,
        "shape": shape(candidate),
    })
    candidate = candidate*(w0+1)*(w0-t*t)
    candidate, steps = reduce_by_plane(candidate*r_guard_squared)
    reductions.append({
        "operation": "times_label_guards", "steps": steps,
        "shape": shape(candidate),
    })
    candidate_degree = int(candidate.degrees()[1])
    if candidate_degree != projected_degree:
        raise RuntimeError("candidate and projected degrees differ")

    projected_leading = coefficient_at_degree(
        projected, 1, projected_degree
    )
    candidate_leading = coefficient_at_degree(
        candidate, 1, candidate_degree
    )
    cross = candidate_leading*projected-projected_leading*candidate
    cross, cross_steps = reduce_by_plane(cross)
    if not cross.is_zero():
        raise RuntimeError(f"quotient-ring cross identity failed: {shape(cross)}")

    leading_norm = plane.resultant(projected_leading, "b")
    if any(value != 0 for value in leading_norm.degrees()[:3]):
        raise RuntimeError("leading norm is not univariate in t")
    scalar, factors = leading_norm.factor()
    reconstruction = context.constant(int(scalar))
    factor_rows = []
    for factor, multiplicity in factors:
        reconstruction *= factor**multiplicity
        factor_rows.append({
            "multiplicity": int(multiplicity),
            "shape": shape(factor),
            "sha256": hashlib.sha256(factor.str().encode()).hexdigest(),
            "text": factor.str(),
        })
    if reconstruction != leading_norm:
        raise RuntimeError("leading norm factor reconstruction failed")

    univariate = fmpz_mod_poly_ctx(PRIME)

    def specialize_univariate(polynomial, variable_index, values):
        coefficients = {}
        for monomial, source_coefficient in polynomial.to_dict().items():
            value = int(source_coefficient)
            for index, point in values.items():
                value = value*pow(point, monomial[index], PRIME) % PRIME
            degree = monomial[variable_index]
            coefficients[degree] = (coefficients.get(degree, 0)+value) % PRIME
        maximum = max(coefficients, default=0)
        return univariate([
            coefficients.get(degree, 0) for degree in range(maximum+1)
        ])

    def linear_root(polynomial):
        if int(polynomial.degree()) != 1:
            raise RuntimeError("requested root of nonlinear polynomial")
        return (-int(polynomial[0])*pow(int(polynomial[1]), -1, PRIME)) % PRIME

    def evaluate_univariate(polynomial, value):
        return sum(
            int(polynomial[index])*pow(value, index, PRIME)
            for index in range(int(polynomial.degree())+1)
        ) % PRIME

    norm_roots = []
    for factor, _ in factors:
        if int(factor.degrees()[3]) == 1:
            coefficients = {
                monomial[3]: int(coefficient)
                for monomial, coefficient in factor.to_dict().items()
            }
            norm_roots.append(
                (-coefficients.get(0, 0)*pow(coefficients[1], -1, PRIME))
                % PRIME
            )
    norm_roots = sorted(set(norm_roots))
    scale_roots = {0, 1, PRIME-1, 16711679, PRIME-16711679, 1288361599}
    exception_rows = []
    all_exception_roots_guarded = True
    for t_value in norm_roots:
        if t_value in scale_roots:
            exception_rows.append({
                "t": t_value, "covered_by_exceptional_scale": True,
            })
            continue
        plane_b = specialize_univariate(plane, 2, {3: t_value})
        leading_b = specialize_univariate(projected_leading, 2, {3: t_value})
        common_b = plane_b.gcd(leading_b)
        _, b_factors = common_b.factor()
        b_roots = sorted({
            linear_root(factor) for factor, _ in b_factors
            if int(factor.degree()) == 1
        })
        row = {
            "t": t_value,
            "covered_by_exceptional_scale": False,
            "common_b_degree": int(common_b.degree()),
            "deployed_b_roots": b_roots,
            "b_rows": [],
        }
        for b_value in b_roots:
            values = {2: b_value, 3: t_value}
            projected_w0 = specialize_univariate(projected, 1, values)
            if projected_w0.is_zero():
                common_guards = []
                if b_value == 0:
                    common_guards.append("b")
                if b_value == 1:
                    common_guards.append("b-1")
                if b_value == PRIME-1:
                    common_guards.append("b+1")
                row["b_rows"].append({
                    "b": b_value, "zero_projected_polynomial": True,
                    "common_guards": common_guards,
                    "all_deployed_roots_guarded": bool(common_guards),
                })
                if not common_guards:
                    all_exception_roots_guarded = False
                continue
            known = {
                "N0": specialize_univariate(n0, 1, values),
                "D0": specialize_univariate(d0, 1, values),
                "w0+1": univariate([1, 1]),
                "w0-t^2": univariate([-(t_value*t_value) % PRIME, 1]),
                "w0-r^2": specialize_univariate(
                    rd*rd*w0-rn*rn, 1, values
                ),
            }
            _, w0_factors = projected_w0.factor()
            deployed_rows = []
            nonlinear = []
            for factor, multiplicity in w0_factors:
                degree = int(factor.degree())
                if degree != 1:
                    nonlinear.append({
                        "degree": degree, "multiplicity": int(multiplicity),
                    })
                    continue
                root = linear_root(factor)
                guards = [
                    name for name, polynomial in known.items()
                    if evaluate_univariate(polynomial, root) == 0
                ]
                if not guards:
                    all_exception_roots_guarded = False
                deployed_rows.append({
                    "w0": root,
                    "multiplicity": int(multiplicity),
                    "guards": guards,
                })
            row["b_rows"].append({
                "b": b_value,
                "zero_projected_polynomial": False,
                "projected_degree": int(projected_w0.degree()),
                "deployed_w0_roots": deployed_rows,
                "nonlinear_factors": nonlinear,
                "all_deployed_roots_guarded": all(
                    item["guards"] for item in deployed_rows
                ),
            })
        exception_rows.append(row)

    return {
        "status": "COMPLETE",
        "field": PRIME,
        "plane_shape": shape(plane),
        "plane_leading": plane_leading.str(),
        "raw_product_shape": shape(raw_product),
        "raw_square_shape": shape(raw_square),
        "product_shape": shape(product),
        "square_shape": shape(square),
        "product_steps": product_steps,
        "square_steps": square_steps,
        "raw_resultant_shape": shape(resultant),
        "projected_steps": projected_steps,
        "projected_shape": shape(projected),
        "projected_sha256": hashlib.sha256(projected.str().encode()).hexdigest(),
        "guard_identity": (
            "plane-reduced(N0*D0^5*(w0+1)*(w0-t^2)*"
            "(rd^2*w0-rn^2)^2) is proportional to pair resultant"
        ),
        "guard_reductions": reductions,
        "guard_plane_leading_exponent": sum(
            row["steps"] for row in reductions
        ),
        "candidate_shape": shape(candidate),
        "candidate_sha256": hashlib.sha256(candidate.str().encode()).hexdigest(),
        "quotient_ring_cross_identity": {
            "verified": True,
            "plane_steps": cross_steps,
            "remainder_zero": True,
            "projected_leading_shape": shape(projected_leading),
            "projected_leading_sha256": hashlib.sha256(
                projected_leading.str().encode()
            ).hexdigest(),
            "candidate_leading_shape": shape(candidate_leading),
            "candidate_leading_sha256": hashlib.sha256(
                candidate_leading.str().encode()
            ).hexdigest(),
        },
        "projected_leading_norm": {
            "content": int(scalar),
            "shape": shape(leading_norm),
            "sha256": hashlib.sha256(leading_norm.str().encode()).hexdigest(),
            "factors": factor_rows,
        },
        "leading_exception_atlas": {
            "base_field_norm_roots": norm_roots,
            "exceptional_scale_roots": sorted(scale_roots),
            "rows": exception_rows,
            "all_uncovered_deployed_roots_guarded": all_exception_roots_guarded,
        },
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell3-signed-pair-guard-factorization-v1",
        "scope": (
            "Exact compact-plane quotient factorization of the complete "
            "necessary cell-3 signed-pair resultant into original product, "
            "denominator, and source-label guards. Exceptional leading/norm "
            "fibers, symmetry transport, route, and Prize consequences remain "
            "separate."
        ),
        "source_plane_sha256": hashlib.sha256(PLANE.read_bytes()).hexdigest(),
        "result": certify.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    result = output["result"]
    print(json.dumps({
        "result": str(RESULT), "status": result["status"],
        "projected_shape": result["projected_shape"],
        "candidate_shape": result["candidate_shape"],
        "cross": result["quotient_ring_cross_identity"],
        "leading_norm": result["projected_leading_norm"],
        "leading_exception_atlas": result["leading_exception_atlas"],
    }, sort_keys=True))
