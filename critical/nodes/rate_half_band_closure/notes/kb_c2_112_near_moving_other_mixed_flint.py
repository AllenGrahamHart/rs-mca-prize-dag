#!/usr/bin/env python3
"""Bounded FLINT projections for the mixed reciprocal-quartic branch."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path

import flint


PRIME = 2130706433
INPUTS = {
    "sums": "kb_c2_112_other_mixed_quartic_equations.json",
    "product": "kb_c2_112_other_mixed_quartic_product_equations.json",
    "product-d": "kb_c2_112_other_mixed_quartic_product_d_equations.json",
    "cross": "kb_c2_112_other_mixed_quartic_product_c_d_equations.json",
}


def signed(value: int) -> int:
    value %= PRIME
    return value if value <= PRIME // 2 else value - PRIME


def load_equations(path: Path, context):
    payload = json.loads(path.read_text())
    if payload["allocation"] != "mixed":
        raise RuntimeError("equation cache scope")
    equations = []
    for record in payload["equations"]:
        terms = {}
        for monomial, coefficient in record["terms"]:
            value = Fraction(coefficient)
            terms[tuple(monomial)] = (
                value.numerator * pow(value.denominator, -1, PRIME)
            ) % PRIME
        equations.append(context.from_dict(terms))
    return equations


def polynomial_record(value):
    return [
        [[int(value) for value in monomial], str(signed(int(coefficient)))]
        for monomial, coefficient in value.to_dict().items()
    ]


def load_polynomial(path: Path, context):
    payload = json.loads(path.read_text())
    if payload["prime"] != PRIME:
        raise RuntimeError("projection prime")
    return context.from_dict({
        tuple(monomial): int(coefficient) % PRIME
        for monomial, coefficient in payload["terms"]
    })


def factor_summary(value):
    _, factors = value.factor()
    return [
        {
            "degree": int(factor.degrees()[1]),
            "exponent": int(exponent),
            "terms": sum(1 for _ in factor.terms()),
            "polynomial": (
                polynomial_record(factor)
                if factor.degrees()[1] <= 12 else None
            ),
        }
        for factor, exponent in factors
    ]


def monic(value):
    return value / value.leading_coefficient()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mode",
        choices=(
            "project-sums", "project-product", "project-product-d",
            "project-cross",
            "gcd", "gcd-all", "gcd-affine", "fibers-affine",
            "boundary-project", "boundary-fibers",
        ),
    )
    parser.add_argument("--cache-dir", type=Path, default=Path("/tmp"))
    args = parser.parse_args()
    context = flint.fmpz_mod_mpoly_ctx.get(["c", "d"], PRIME)

    if args.mode == "boundary-project":
        payload = json.loads((
            args.cache_dir
            / "kb_c2_112_other_mixed_quartic_boundary_equations.json"
        ).read_text())

        def boundary_equation(name):
            record = payload["equations"][name]
            return context.from_dict({
                tuple(monomial): (
                    Fraction(coefficient).numerator
                    * pow(Fraction(coefficient).denominator, -1, PRIME)
                ) % PRIME
                for monomial, coefficient in record["terms"]
            })

        q = boundary_equation("q")
        projections = []
        for name in ("det_c", "compat_c", "det_d", "compat_d"):
            projection = monic(q.resultant(boundary_equation(name), 0))
            projections.append(projection)
            print(
                f"stage=boundary_projection name={name} "
                f"degree={projection.degrees()[1]} "
                f"factors={len(projection.factor()[1])}",
                flush=True,
            )
        common = projections[0]
        for value in projections[1:]:
            common = monic(common.gcd(value))
        summary = factor_summary(common)
        path = (
            args.cache_dir
            / "kb_c2_112_other_mixed_quartic_boundary_mod_gcd.json"
        )
        path.write_text(json.dumps({
            "allocation": "mixed",
            "prime": PRIME,
            "terms": polynomial_record(common),
            "factors": summary,
        }, sort_keys=True))
        print(
            f"stage=boundary_gcd degree={common.degrees()[1]} "
            f"factor_count={len(summary)} factors={summary} path={path}",
            flush=True,
        )
        return

    if args.mode == "boundary-fibers":
        common = load_polynomial(
            args.cache_dir
            / "kb_c2_112_other_mixed_quartic_boundary_mod_gcd.json",
            context,
        )
        _, factors = common.factor()
        boundary_payload = json.loads((
            args.cache_dir
            / "kb_c2_112_other_mixed_quartic_boundary_equations.json"
        ).read_text())
        equation_records = [
            boundary_payload["equations"][name]["terms"]
            for name in ("q", "det_c", "compat_c", "det_d", "compat_d")
        ]
        source_records = []
        for root in ("c", "d"):
            payload = json.loads(
                (args.cache_dir / f"kb_c2_112_other_mixed_{root}_cores.json")
                .read_text()
            )
            source_records.extend(
                payload["polynomials"][kind]
                for kind in ("product", "sum")
            )
        ratio_payload = json.loads(
            (args.cache_dir / "kb_c2_112_other_mixed_ratio_gates.json")
            .read_text()
        )
        source_records.append(ratio_payload["polynomials"]["1"])
        polynomial_context = flint.fmpz_mod_poly_ctx(PRIME)
        fiber_records = []
        for index, (factor, _) in enumerate(factors):
            degree = int(factor.degrees()[1])
            modulus_coefficients = [0] * (degree + 1)
            for (_, power), coefficient in factor.to_dict().items():
                modulus_coefficients[int(power)] = int(coefficient)
            field = flint.fq_default_ctx(
                modulus=polynomial_context(modulus_coefficients),
                fq_type="FQ_NMOD",
            )
            d_value = field.gen()
            d_forbidden = (
                d_value == 0 or d_value == 1 or d_value == -1
                or d_value == 2 or 2 * d_value == 1
            )
            if d_forbidden:
                fiber_records.append({
                    "index": index,
                    "d_factor": polynomial_record(factor),
                    "d_degree": degree,
                    "d_forbidden": True,
                    "saturated_unit": True,
                })
                print(
                    f"stage=boundary_fiber index={index} d_degree={degree} "
                    "d_forbidden=True saturated_unit=True",
                    flush=True,
                )
                continue
            c_ring = flint.fq_default_poly_ctx(field)
            common_c = None
            for record in equation_records:
                max_c = max(monomial[0] for monomial, _ in record)
                coefficients = [field.zero()] * (max_c + 1)
                for (power_c, power_d), coefficient in record:
                    value = Fraction(coefficient)
                    scalar = (
                        value.numerator
                        * pow(value.denominator, -1, PRIME)
                    ) % PRIME
                    coefficients[power_c] += field(scalar) * d_value**power_d
                value_c = c_ring(coefficients)
                common_c = (
                    value_c if common_c is None
                    else common_c.gcd(value_c)
                )
            if common_c.degree() != 1:
                raise RuntimeError(
                    f"boundary c fiber degree {common_c.degree()}"
                )
            c_value = -common_c[0] / common_c[1]
            b_ring = flint.fq_default_poly_ctx(field)
            b_value = b_ring.gen()
            common_b = None
            for record in source_records:
                max_b = max(monomial[0] for monomial, _ in record)
                coefficients = [field.zero()] * (max_b + 1)
                for (power_b, power_c, power_d), coefficient in record:
                    value = Fraction(coefficient)
                    scalar = (
                        value.numerator
                        * pow(value.denominator, -1, PRIME)
                    ) % PRIME
                    coefficients[power_b] += (
                        field(scalar) * c_value**power_c * d_value**power_d
                    )
                value_b = b_ring(coefficients)
                common_b = (
                    value_b if common_b is None
                    else common_b.gcd(value_b)
                )
            forbidden_b = (
                b_value * c_value * d_value
                * (b_value - 2) * (2 * b_value - 1)
                * (b_value - 1) * (b_value + 1)
                * (c_value - 2) * (2 * c_value - 1)
                * (c_value - 1) * (c_value + 1)
                * (d_value - 2) * (2 * d_value - 1)
                * (d_value - 1) * (d_value + 1)
                * (b_value - c_value) * (b_value * c_value - 1)
                * (b_value - d_value) * (b_value * d_value - 1)
                * (c_value - d_value) * (c_value * d_value - 1)
                * (5 * c_value * d_value - 4 * c_value - 4 * d_value + 5)
                * (
                    4 * c_value**2 * d_value - 2 * c_value**2
                    - 3 * c_value * d_value + 3 * c_value
                    + 2 * d_value - 4
                )
            )
            admissible = common_b / common_b.gcd(forbidden_b)
            fiber_records.append({
                "index": index,
                "d_factor": polynomial_record(factor),
                "d_degree": degree,
                "d_forbidden": False,
                "c_degree": common_c.degree(),
                "b_degree": common_b.degree(),
                "admissible_degree": admissible.degree(),
                "saturated_unit": admissible.degree() == 0,
            })
            print(
                f"stage=boundary_fiber index={index} d_degree={degree} "
                f"c_degree={common_c.degree()} b_degree={common_b.degree()} "
                f"admissible_degree={admissible.degree()} "
                f"saturated_unit={admissible.degree() == 0}",
                flush=True,
            )
        fiber_path = (
            args.cache_dir
            / "kb_c2_112_other_mixed_quartic_boundary_fibers.json"
        )
        fiber_path.write_text(json.dumps({
            "allocation": "mixed",
            "prime": PRIME,
            "fibers": fiber_records,
        }, sort_keys=True))
        print(
            f"stage=boundary_fibers_cache path={fiber_path} "
            f"bytes={fiber_path.stat().st_size}",
            flush=True,
        )
        return

    if args.mode.startswith("project-"):
        kind = args.mode.removeprefix("project-")
        equations = load_equations(args.cache_dir / INPUTS[kind], context)
        print(
            f"stage=load kind={kind} degrees={[value.degrees() for value in equations]}",
            flush=True,
        )
        projection = monic(equations[0].resultant(equations[1], 0))
        path = args.cache_dir / f"kb_c2_112_other_mixed_quartic_{kind}_mod_projection.json"
        payload = {
            "allocation": "mixed",
            "kind": kind,
            "prime": PRIME,
            "terms": polynomial_record(projection),
            "factors": factor_summary(projection),
        }
        path.write_text(json.dumps(payload, sort_keys=True))
        print(
            f"stage=projection kind={kind} degree={projection.degrees()[1]} "
            f"terms={sum(1 for _ in projection.terms())} "
            f"factor_count={len(payload['factors'])} path={path} "
            f"bytes={path.stat().st_size}",
            flush=True,
        )
        return

    if args.mode == "fibers-affine":
        common = load_polynomial(
            args.cache_dir
            / "kb_c2_112_other_mixed_quartic_affine_mod_gcd.json",
            context,
        )
        _, factors = common.factor()
        equation_payloads = [
            json.loads((args.cache_dir / INPUTS[kind]).read_text())
            for kind in ("sums", "product", "product-d", "cross")
        ]
        source_records = []
        for root in ("c", "d"):
            payload = json.loads(
                (args.cache_dir / f"kb_c2_112_other_mixed_{root}_cores.json")
                .read_text()
            )
            source_records.extend(
                payload["polynomials"][kind]
                for kind in ("product", "sum")
            )
        ratio_payload = json.loads(
            (args.cache_dir / "kb_c2_112_other_mixed_ratio_gates.json")
            .read_text()
        )
        source_records.append(ratio_payload["polynomials"]["1"])
        polynomial_context = flint.fmpz_mod_poly_ctx(PRIME)
        fiber_records = []
        for index, (factor, _) in enumerate(factors):
            factor_terms = factor.to_dict()
            degree = int(factor.degrees()[1])
            modulus_coefficients = [0] * (degree + 1)
            for (_, power), coefficient in factor_terms.items():
                modulus_coefficients[int(power)] = int(coefficient)
            modulus = polynomial_context(modulus_coefficients)
            field = flint.fq_default_ctx(
                modulus=modulus, fq_type="FQ_NMOD"
            )
            alpha = field.gen()
            ring = flint.fq_default_poly_ctx(field)
            common_c = None
            for payload in equation_payloads:
                for record in payload["equations"]:
                    max_c = max(monomial[0] for monomial, _ in record["terms"])
                    coefficients = [field.zero()] * (max_c + 1)
                    for (power_c, power_d), coefficient in record["terms"]:
                        value = Fraction(coefficient)
                        scalar = (
                            value.numerator
                            * pow(value.denominator, -1, PRIME)
                        ) % PRIME
                        coefficients[power_c] += field(scalar) * alpha**power_d
                    value_c = ring(coefficients)
                    common_c = (
                        value_c if common_c is None
                        else common_c.gcd(value_c)
                    )
            c_degree = common_c.degree()
            if c_degree == 1:
                fiber_values = [(
                    field, -common_c[0] / common_c[1], alpha
                )]
            elif c_degree == 2 and degree == 1:
                _, c_factors = common_c.factor()
                if all(factor.degree() == 1 for factor, _ in c_factors):
                    fiber_values = [
                        (field, -factor[0] / factor[1], alpha)
                        for factor, _ in c_factors
                    ]
                else:
                    c_modulus = polynomial_context([
                        int(common_c[index])
                        for index in range(c_degree + 1)
                    ])
                    full_field = flint.fq_default_ctx(
                        modulus=c_modulus, fq_type="FQ_NMOD"
                    )
                    fiber_values = [(
                        full_field, full_field.gen(), full_field(int(alpha))
                    )]
            else:
                raise RuntimeError(
                    f"unsupported full fiber degrees d={degree} c={c_degree}"
                )
            b_degrees = []
            admissible_degrees = []
            for full_field, c_value, d_value in fiber_values:
                b_ring = flint.fq_default_poly_ctx(full_field)
                b_value = b_ring.gen()
                common_b = None
                for record in source_records:
                    max_b = max(monomial[0] for monomial, _ in record)
                    coefficients = [full_field.zero()] * (max_b + 1)
                    for (power_b, power_c, power_d), coefficient in record:
                        value = Fraction(coefficient)
                        scalar = (
                            value.numerator
                            * pow(value.denominator, -1, PRIME)
                        ) % PRIME
                        coefficients[power_b] += (
                            full_field(scalar)
                            * c_value**power_c * d_value**power_d
                        )
                    value_b = b_ring(coefficients)
                    common_b = (
                        value_b if common_b is None
                        else common_b.gcd(value_b)
                    )
                b_degrees.append(common_b.degree())
                forbidden_b = (
                    b_value * c_value * d_value
                    * (b_value - 2) * (2 * b_value - 1)
                    * (b_value - 1) * (b_value + 1)
                    * (c_value - 2) * (2 * c_value - 1)
                    * (c_value - 1) * (c_value + 1)
                    * (d_value - 2) * (2 * d_value - 1)
                    * (d_value - 1) * (d_value + 1)
                    * (b_value - c_value) * (b_value * c_value - 1)
                    * (b_value - d_value) * (b_value * d_value - 1)
                    * (c_value - d_value) * (c_value * d_value - 1)
                    * (5 * c_value * d_value - 4 * c_value - 4 * d_value + 5)
                    * (
                        4 * c_value**2 * d_value - 2 * c_value**2
                        - 3 * c_value * d_value + 3 * c_value
                        + 2 * d_value - 4
                    )
                )
                forbidden_part = common_b.gcd(forbidden_b)
                admissible_degrees.append(
                    (common_b / forbidden_part).degree()
                )
            fiber_records.append({
                "index": index,
                "d_factor": polynomial_record(factor),
                "d_degree": degree,
                "c_gcd_degree": c_degree,
                "b_gcd_degrees": b_degrees,
                "admissible_degrees": admissible_degrees,
                "saturated_unit": all(
                    value == 0 for value in admissible_degrees
                ),
            })
            print(
                f"stage=fiber index={index} d_degree={degree} "
                f"c_gcd_degree={c_degree} "
                f"b_gcd_degrees={b_degrees} "
                f"admissible_degrees={admissible_degrees} "
                f"saturated_unit={all(value == 0 for value in admissible_degrees)}",
                flush=True,
            )
        fiber_path = (
            args.cache_dir
            / "kb_c2_112_other_mixed_quartic_affine_fibers.json"
        )
        fiber_path.write_text(json.dumps({
            "allocation": "mixed",
            "prime": PRIME,
            "fibers": fiber_records,
        }, sort_keys=True))
        print(
            f"stage=affine_fibers_cache path={fiber_path} "
            f"bytes={fiber_path.stat().st_size}",
            flush=True,
        )
        return

    def projected(kind):
        return load_polynomial(
            args.cache_dir
            / f"kb_c2_112_other_mixed_quartic_{kind}_mod_projection.json",
            context,
        )

    left = projected("sums")
    right = projected("product")
    if args.mode == "gcd-affine":
        cleaned = []
        for kind in ("sums", "product", "product-d", "cross"):
            equations = load_equations(args.cache_dir / INPUTS[kind], context)
            leading = []
            for equation in equations:
                terms = equation.to_dict()
                degree_c = max(monomial[0] for monomial in terms)
                leading.append(context.from_dict({
                    monomial: coefficient
                    for monomial, coefficient in terms.items()
                    if monomial[0] == degree_c
                }))
            boundary = monic(leading[0].gcd(leading[1]))
            value = projected(kind)
            while True:
                common_boundary = value.gcd(boundary)
                if sum(1 for _ in common_boundary.terms()) == 1:
                    break
                value = value / common_boundary
            cleaned.append(monic(value))
            print(
                f"stage=affine kind={kind} boundary={factor_summary(boundary)} "
                f"clean_degree={cleaned[-1].degrees()[1]}",
                flush=True,
            )
        common = cleaned[0]
        for value in cleaned[1:]:
            common = monic(common.gcd(value))
        summary = factor_summary(common)
        path = (
            args.cache_dir
            / "kb_c2_112_other_mixed_quartic_affine_mod_gcd.json"
        )
        path.write_text(json.dumps({
            "allocation": "mixed",
            "prime": PRIME,
            "terms": polynomial_record(common),
            "factors": summary,
        }, sort_keys=True))
        print(
            f"stage=affine_gcd degree={common.degrees()[1]} "
            f"terms={sum(1 for _ in common.terms())} "
            f"factor_count={len(summary)} factors={summary} path={path}",
            flush=True,
        )
        return
    common = monic(left.gcd(right))
    if args.mode == "gcd-all":
        third = load_polynomial(
            args.cache_dir
            / "kb_c2_112_other_mixed_quartic_product-d_mod_projection.json",
            context,
        )
        common = monic(common.gcd(third))
    summary = factor_summary(common)
    print(
        f"stage=gcd degree={common.degrees()[1]} "
        f"terms={sum(1 for _ in common.terms())} "
        f"factor_count={len(summary)} factors={summary}",
        flush=True,
    )


if __name__ == "__main__":
    main()
