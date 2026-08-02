#!/usr/bin/env python3
"""Classify every pseudo-subresultant scale used on the H component."""

import functools
import hashlib
import json
from pathlib import Path
import re

import modal


DIRECTORY = Path(__file__).parent
PLANE = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_plane_kernel_flint_result.json"
HFACTOR = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_common_factor_6.txt"
LIVE = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_resultant_factor_2.txt"
LINEAR = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_w1_reconstruction_linear_factor_0.txt"
CONSTANT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_w1_reconstruction_constant_factor_1.txt"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_subresultant_scale_atlas_result.json"
REMOTE = {
    PLANE: "/root/plane.json",
    HFACTOR: "/root/hfactor.txt",
    LIVE: "/root/live.txt",
    LINEAR: "/root/linear.txt",
    CONSTANT: "/root/constant.txt",
}
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell4-h-subresultant-scales")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
)
for local_path, remote_path in REMOTE.items():
    image = image.add_local_file(local_path, remote_path)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


def shape(polynomial):
    return {
        "degrees": [int(value) for value in polynomial.degrees()],
        "total_degree": int(polynomial.total_degree()),
        "terms": len(list(polynomial.terms())),
    }


@app.function(image=image, cpu=4.0, memory=16384, timeout=600)
def classify_scales():
    from flint import fmpz_mod_mpoly_ctx, fmpz_mod_poly_ctx

    context = fmpz_mod_mpoly_ctx.get(["w0", "b", "t"], PRIME)
    w0, b, _ = context.gens()
    univariate_context = fmpz_mod_poly_ctx(PRIME)

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

    def coefficient_at_degree(polynomial, variable_index, degree):
        return context.from_dict({
            tuple(0 if index == variable_index else monomial[index]
                  for index in range(3)): int(coefficient)
            for monomial, coefficient in polynomial.to_dict().items()
            if monomial[variable_index] == degree
        })

    payload = json.loads(Path(REMOTE[PLANE]).read_text())["result"]
    polynomials = {
        "plane": parse(payload["plane_polynomial"]),
        "linear": parse(Path(REMOTE[LINEAR]).read_text().strip()),
        "constant": parse(Path(REMOTE[CONSTANT]).read_text().strip()),
        "live": parse(Path(REMOTE[LIVE]).read_text().strip()),
    }
    h = parse(Path(REMOTE[HFACTOR]).read_text().strip())
    h_degree = int(h.degrees()[0])
    h_leading = coefficient_at_degree(h, 0, h_degree)

    def reduce_by_h(polynomial):
        reduced = polynomial
        while int(reduced.degrees()[0]) >= h_degree:
            old_degree = int(reduced.degrees()[0])
            coefficient = coefficient_at_degree(reduced, 0, old_degree)
            reduced = (
                h_leading*reduced
                -coefficient*w0**(old_degree-h_degree)*h
            )
            if int(reduced.degrees()[0]) >= old_degree:
                raise RuntimeError("H pseudo-division did not lower degree")
        return reduced

    def pseudo_remainder(dividend, divisor):
        divisor_degree = int(divisor.degrees()[1])
        leading = coefficient_at_degree(divisor, 1, divisor_degree)
        remainder = dividend
        while int(remainder.degrees()[1]) >= divisor_degree:
            old_degree = int(remainder.degrees()[1])
            coefficient = coefficient_at_degree(remainder, 1, old_degree)
            remainder = (
                leading*remainder
                -coefficient*b**(old_degree-divisor_degree)*divisor
            )
            remainder = reduce_by_h(remainder)
            if int(remainder.degrees()[1]) >= old_degree:
                raise RuntimeError("b pseudo-division did not lower degree")
        return remainder, leading

    reduced = {name: reduce_by_h(value) for name, value in polynomials.items()}
    quadratic, linear_leading = pseudo_remainder(
        reduced["plane"], reduced["linear"]
    )
    quadratic_coefficients = [
        coefficient_at_degree(quadratic, 1, degree) for degree in range(3)
    ]
    quadratic_content = functools.reduce(
        lambda left, right: left.gcd(right), quadratic_coefficients
    )
    quadratic, remainder = divmod(quadratic, quadratic_content)
    if not remainder.is_zero():
        raise RuntimeError("quadratic content division failed")
    candidate, quadratic_leading = pseudo_remainder(
        reduced["linear"], quadratic
    )
    candidate_coefficients = [
        coefficient_at_degree(candidate, 1, degree) for degree in range(2)
    ]
    candidate_content = candidate_coefficients[0].gcd(candidate_coefficients[1])
    candidate, remainder = divmod(candidate, candidate_content)
    if not remainder.is_zero():
        raise RuntimeError("candidate content division failed")
    candidate_leading = coefficient_at_degree(candidate, 1, 1)

    scales = {
        "h_leading": h_leading,
        "linear_leading": linear_leading,
        "quadratic_content": quadratic_content,
        "quadratic_leading": quadratic_leading,
        "candidate_content": candidate_content,
        "candidate_leading_A": candidate_leading,
    }
    if any(int(scale.degrees()[1]) > 0 for scale in scales.values()):
        raise RuntimeError("a scale unexpectedly depends on b")

    def to_univariate_t(polynomial):
        entries = polynomial.to_dict()
        degree = max(int(monomial[2]) for monomial in entries)
        coefficients = [0]*(degree+1)
        for monomial, value in entries.items():
            if monomial[:2] != (0, 0):
                raise RuntimeError("polynomial is not univariate in t")
            coefficients[int(monomial[2])] = int(value)
        return univariate_context(coefficients)

    def specialize(polynomial, variable_index, values):
        coefficients = {}
        for monomial, source_coefficient in polynomial.to_dict().items():
            value = int(source_coefficient)
            for index, point in values.items():
                value = value*pow(point, monomial[index], PRIME) % PRIME
            degree = monomial[variable_index]
            coefficients[degree] = (coefficients.get(degree, 0)+value) % PRIME
        maximum = max(coefficients, default=0)
        return univariate_context([
            coefficients.get(degree, 0) for degree in range(maximum+1)
        ])

    def evaluate(polynomial, values):
        total = 0
        for monomial, source_coefficient in polynomial.to_dict().items():
            value = int(source_coefficient)
            for index, point in values.items():
                value = value*pow(point, monomial[index], PRIME) % PRIME
            total = (total+value) % PRIME
        return total

    def linear_roots(polynomial):
        _, factors = polynomial.factor()
        roots = []
        factor_rows = []
        for factor, multiplicity in factors:
            degree = int(factor.degree())
            row = {
                "degree": degree,
                "multiplicity": int(multiplicity),
                "sha256": digest(str(factor)),
            }
            if degree == 1:
                root = (-int(factor[0])*pow(int(factor[1]), -1, PRIME)) % PRIME
                roots.append(root)
                row["root"] = root
            factor_rows.append(row)
        return sorted(set(roots)), factor_rows

    scale_rows = []
    exceptional_points = set()
    tpoly = univariate_context([0, 1])
    for name, scale in scales.items():
        resultant = h.resultant(scale, "w0")
        if resultant.is_zero() or int(resultant.degrees()[0]) != 0:
            raise RuntimeError(f"{name} resultant is zero or retains w0")
        resultant_t = to_univariate_t(resultant)
        frobenius = pow(tpoly, PRIME, resultant_t)
        root_gcd = resultant_t.gcd(frobenius-tpoly)
        t_roots, root_factors = linear_roots(root_gcd)
        point_rows = []
        for t_value in t_roots:
            h_t = specialize(h, 0, {2: t_value})
            scale_t = specialize(scale, 0, {2: t_value})
            common = h_t.gcd(scale_t)
            w0_roots, common_factors = linear_roots(common)
            for w0_value in w0_roots:
                exceptional_points.add((t_value, w0_value))
            point_rows.append({
                "t": t_value,
                "t_guard": t_value == 0 or pow(t_value, 2, PRIME) in (1, PRIME-1),
                "common_degree": int(common.degree()),
                "common_sha256": digest(str(common)),
                "common_factors": common_factors,
            })
        scale_rows.append({
            "name": name,
            "shape": shape(scale),
            "sha256": digest(scale.str()),
            "resultant_degree": int(resultant_t.degree()),
            "base_field_t_degree": int(root_gcd.degree()),
            "base_field_t_factors": root_factors,
            "point_rows": point_rows,
        })

    normalized = {
        name: parse(row["polynomial"])
        for name, row in payload["normalized_coefficients"].items()
    }
    rn = parse(payload["r_numerator"])
    rd = parse(payload["r_denominator"])
    replay_rows = []
    for t_value, w0_value in sorted(exceptional_points):
        b_polynomials = {
            name: specialize(polynomial, 1, {0: w0_value, 2: t_value})
            for name, polynomial in polynomials.items()
        }
        common_b = b_polynomials["plane"]
        for name in ("linear", "constant", "live"):
            common_b = common_b.gcd(b_polynomials[name])
        b_roots, b_factors = linear_roots(common_b)
        replay = {
            "t": t_value,
            "w0": w0_value,
            "t_guard": t_value == 0 or pow(t_value, 2, PRIME) in (1, PRIME-1),
            "common_b_degree": int(common_b.degree()),
            "common_b_sha256": digest(str(common_b)),
            "common_b_factors": b_factors,
            "b_rows": [],
        }
        for b_value in b_roots:
            bt = {1: b_value, 2: t_value}
            coefficient_values = {
                name: evaluate(polynomial, bt)
                for name, polynomial in normalized.items()
            }

            def coefficient_polynomial(prefix):
                return univariate_context([
                    coefficient_values[f"{prefix}{index}"]
                    for index in range(3)
                ])

            a2 = coefficient_polynomial("a2")
            a0 = coefficient_polynomial("a0")
            k = coefficient_values["b10"]
            w = univariate_context([0, 1])
            d0 = int(a2(w0_value))
            n0 = int(a0(w0_value))
            product = a0*d0+n0*a2
            sum_cut = (
                k*k*w0_value*(1-w0_value)*(1-w0_value)*a2*a2
                -k*k*w*(1-w)*(1-w)*d0*d0
                -4*n0*d0*a2*a2
            )
            pair_gcd = product.gcd(sum_cut)
            w1_roots, pair_factors = linear_roots(pair_gcd)
            rd_value = evaluate(rd, bt)
            rn_value = evaluate(rn, bt)
            r_guard_values = set()
            if rd_value != 0:
                r2 = rn_value*rn_value*pow(
                    rd_value*rd_value % PRIME, -1, PRIME
                ) % PRIME
                r_guard_values = {r2, (-r2) % PRIME}
            fixed_guards = {
                0, 1, PRIME-1, pow(t_value, 2, PRIME)
            } | r_guard_values
            b_row = {
                "b": b_value,
                "d0_zero": d0 == 0,
                "n0_zero": n0 == 0,
                "k_zero": k == 0,
                "r_denominator_zero": rd_value == 0,
                "w0_source_guard": w0_value in fixed_guards,
                "pair_gcd_degree": int(pair_gcd.degree()),
                "pair_gcd_sha256": digest(str(pair_gcd)),
                "pair_factors": pair_factors,
                "w1_rows": [],
            }
            for w1_value in w1_roots:
                b_row["w1_rows"].append({
                    "w1": w1_value,
                    "w1_source_guard": w1_value in fixed_guards,
                    "d1_zero": int(a2(w1_value)) == 0,
                    "n1_zero": int(a0(w1_value)) == 0,
                })
            replay["b_rows"].append(b_row)
        replay_rows.append(replay)

    return {
        "status": "COMPLETE",
        "field": PRIME,
        "h_shape": shape(h),
        "scale_rows": scale_rows,
        "exceptional_point_count": len(exceptional_points),
        "replay_rows": replay_rows,
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell4-pair-exceptional-h-subresultant-scale-atlas-v1",
        "scope": (
            "Exact deployed-field atlas of every leading coefficient and "
            "content scale used in the H-component pseudo-subresultant chain, "
            "with direct original P,L,M,F and squared-pair replay at every "
            "base-field scale-zero point. Unsquared colored equations, other "
            "charts, orbit, and Prize claims remain separate."
        ),
        "artifact_sha256": {
            path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in REMOTE
        },
        "result": classify_scales.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    result = output["result"]
    print(json.dumps({
        "result": str(RESULT),
        "status": result["status"],
        "exceptional_point_count": result["exceptional_point_count"],
        "scales": [{
            "name": row["name"],
            "shape": row["shape"],
            "resultant_degree": row["resultant_degree"],
            "base_field_t_degree": row["base_field_t_degree"],
        } for row in result["scale_rows"]],
        "replay": [{
            "t": row["t"],
            "w0": row["w0"],
            "t_guard": row["t_guard"],
            "b_count": len(row["b_rows"]),
            "w1_count": sum(len(item["w1_rows"]) for item in row["b_rows"]),
        } for row in result["replay_rows"]],
    }, sort_keys=True))
