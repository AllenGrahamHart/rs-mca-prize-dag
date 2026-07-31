#!/usr/bin/env python3
"""Project moving-moving trace-minor caches onto the endpoint plane.

Proof status: EXPERIMENTAL component router.  Projection support is only a
necessary condition; no cell is deleted until components and finite
intersections are replayed in the four trace quadratics and open set.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import flint
import sympy as sp
from sympy.polys.agca.extensions import FiniteExtension


DEPLOYED_PRIME = 2130706433
HERE = Path(__file__).resolve().parent
COMPILER = HERE / "kb_c2_112_aligned_positive_unramified_flint.py"
COMPILER_SHA256 = "988e60a010ea2793049505b5e9b0ff6d5c28b300e4a00a4b8a3724849ede09f0"
CONFIGS = {
    "same": {
        "cache": HERE / "kb_c2_112_aligned_positive_unramified_moving_same_minors.json",
        "conic_cache": HERE / "kb_c2_112_aligned_positive_unramified_moving_same_conic.json",
        "cache_sha256": "f5c8285e2d93064f509ecb3ecfad98bb49eb1357777e39e968d06ce769eaba97",
        "conic_cache_sha256": "e754fecd9711b5119e4603d45848d601cb894c1c2b357b696c243b8e4439ca72",
        "residual_digests": (
            "623d1c4c5024360fe8c4f46c07b8fc735e904e3df7a9e5d527c58235e29ef04b",
            "c1b7ed943dcc506ec1f5ac5a945a3c49d737ba5eda3eaed3e9f230c780b7def9",
            "5053d388c9fd2374f9c2f88c0a856c6af6a3074fa8a892353f5f54913f520262",
            "387dfb97236370156a6206b386279185a476f77906ebac04e9bb2414b4a28303",
        ),
    },
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def load_compiler():
    require(
        hashlib.sha256(COMPILER.read_bytes()).hexdigest() == COMPILER_SHA256,
        "compiler hash",
    )
    spec = importlib.util.spec_from_file_location("unramified_flint", COMPILER)
    require(spec is not None and spec.loader is not None, "compiler loader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_residuals(compiler, context, allocation: str):
    config = CONFIGS[allocation]
    cache = config["cache"]
    require(
        hashlib.sha256(cache.read_bytes()).hexdigest()
        == config["cache_sha256"],
        "cache hash",
    )
    payload = json.loads(cache.read_text(encoding="ascii"))
    require(
        payload["schema"]
        == "kb-c2-112-aligned-positive-minor-residuals-v1",
        "cache schema",
    )
    require(payload["prime"] == DEPLOYED_PRIME, "cache prime")
    require(payload["template"] == "moving-moving", "cache template")
    require(payload["allocation"] == allocation, "cache allocation")
    expected = config["residual_digests"]
    require(tuple(payload["digests"]) == expected, "cache digests")
    residuals = []
    for encoded, digest in zip(payload["polynomials"], expected):
        polynomial = context.from_dict({
            tuple(monomial): coefficient for monomial, coefficient in encoded
        })
        require(
            compiler.polynomial_digest(polynomial) == digest,
            "decoded residual digest",
        )
        residuals.append(polynomial)
    return residuals


def load_conic(compiler, context, allocation: str):
    config = CONFIGS[allocation]
    cache = config["conic_cache"]
    require(
        hashlib.sha256(cache.read_bytes()).hexdigest()
        == config["conic_cache_sha256"],
        "conic cache hash",
    )
    payload = json.loads(cache.read_text(encoding="ascii"))
    require(
        payload["schema"] == "kb-c2-112-aligned-positive-kernel-conic-v1",
        "conic schema",
    )
    require(payload["template"] == "moving-moving", "conic template")
    require(payload["allocation"] == allocation, "conic allocation")
    polynomial = context.from_dict({
        tuple(monomial): coefficient
        for monomial, coefficient in payload["polynomial"]
    })
    require(
        compiler.polynomial_digest(polynomial) == payload["digest"],
        "decoded conic digest",
    )
    return polynomial


def evaluate_extension_polynomial(coefficients, point, extension):
    value = extension.zero
    for coefficient in reversed(coefficients):
        value = value * point + coefficient
    return value


def extension_value_numerator(value, p):
    coefficients = list(reversed(value.rep.to_list()))
    denominators = [coefficient.denom.as_expr() for coefficient in coefficients]
    denominator_product = sp.prod(denominators)
    numerator = sp.Integer(0)
    for index, coefficient in enumerate(coefficients):
        numerator += (
            coefficient.numer.as_expr()
            * sp.prod(denominators[:index] + denominators[index + 1:])
            * p**index
        )
    return sp.expand(numerator), sp.expand(denominator_product)


def same_cubic(p, t):
    return (
        8 * p**3 + 37 * p**2 * t + 27 * p**2
        + 52 * p * t**2 + 89 * p * t + 27 * p
        + 20 * t**3 + 52 * t**2 + 37 * t + 8
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allocation", choices=tuple(CONFIGS), required=True)
    parser.add_argument("--pair", choices=("01", "02", "03", "all"), default="all")
    parser.add_argument("--factor", action="store_true")
    parser.add_argument("--linear-component", action="store_true")
    parser.add_argument("--cubic-component", action="store_true")
    args = parser.parse_args()

    require(flint.__version__ == "0.9.0", "python-flint version")
    compiler = load_compiler()
    context = flint.nmod_mpoly_ctx.get(
        ("trace", "p", "t", "w"), DEPLOYED_PRIME, "lex"
    )
    residuals = load_residuals(compiler, context, args.allocation)
    if args.linear_component:
        trace, _, t, w = context.gens()
        inverse_four = pow(4, -1, DEPLOYED_PRIME)
        p_value = -(5 * t + 4) * inverse_four
        specialized = [
            polynomial.compose(trace, p_value, t, w)
            for polynomial in residuals
        ]
        common_minor = specialized[0]
        for polynomial in specialized[1:]:
            common_minor = common_minor.gcd(polynomial)
        require(not common_minor.is_zero(), "zero linear-component minor gcd")
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_LINEAR_MINOR_GCD_PASS "
            f"allocation={args.allocation} terms={len(common_minor.to_dict())} "
            f"degrees={common_minor.degrees()} "
            f"digest={compiler.polynomial_digest(common_minor)}",
            flush=True,
        )
        compiler.emit_factorization(common_minor, "linear_minor_gcd", context)
        conic = load_conic(compiler, context, args.allocation)
        specialized_conic = conic.compose(trace, p_value, t, w)
        admissible_support = common_minor.gcd(specialized_conic)
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_LINEAR_CONIC_GCD_PASS "
            f"allocation={args.allocation} terms={len(admissible_support.to_dict())} "
            f"degrees={admissible_support.degrees()} "
            f"digest={compiler.polynomial_digest(admissible_support)}",
            flush=True,
        )
        compiler.emit_factorization(
            admissible_support, "linear_minor_conic_gcd", context
        )
        expected = t**3 * (t + 1) * (t + 4) * (w - 1)
        compiler.require_associate(
            admissible_support, expected, "moving linear exclusion support"
        )
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_LINEAR_EXCLUSION_PASS "
            "allocation=same component=4*p+5*t+4 "
            "support=w-1,discriminant,q(1)",
            flush=True,
        )
        return
    if args.cubic_component:
        trace_symbol, p_symbol, t_symbol, w_symbol = sp.symbols(
            "trace p t w"
        )
        component_expression = same_cubic(p_symbol, t_symbol)
        component = compiler.sympy_to_flint(
            sp.Poly(
                component_expression,
                trace_symbol,
                p_symbol,
                t_symbol,
                w_symbol,
            ),
            context,
        )
        for right in (1, 2, 3):
            projection = residuals[0].resultant(residuals[right], 3)
            quotient, remainder = divmod(projection, component)
            require(remainder.is_zero(), "missing cubic projection factor")
            require(not (quotient % component).is_zero(), "cubic multiplicity")
        extension = FiniteExtension(
            sp.Poly(
                component_expression,
                p_symbol,
                domain=sp.GF(DEPLOYED_PRIME).frac_field(t_symbol),
            ).monic()
        )
        extension_residuals = [
            compiler.flint_to_extension_w_coefficients(
                polynomial, p_symbol, t_symbol, extension
            )
            for polynomial in residuals
        ]
        common = compiler.extension_gcd(
            extension_residuals[0], extension_residuals[1], extension
        )
        for right in (2, 3):
            common = compiler.extension_gcd(
                common,
                compiler.extension_gcd(
                    extension_residuals[0],
                    extension_residuals[right],
                    extension,
                ),
                extension,
            )
        require(len(common) == 2, "cubic common root is not linear")
        root = -common[0]
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_CUBIC_ROOT_PASS "
            f"allocation=same degree=1 "
            f"digest={compiler.extension_polynomial_digest(common)}",
            flush=True,
        )

        conic = load_conic(compiler, context, args.allocation)
        _, conic_factors = conic.factor()
        conic_residuals = [
            factor for factor, exponent in conic_factors
            if len(factor.to_dict()) > 100 and exponent == 1
        ]
        require(len(conic_residuals) == 1, "unique kernel-conic residual")
        conic_residual = conic_residuals[0]
        conic_extension = compiler.flint_to_extension_w_coefficients(
            conic_residual, p_symbol, t_symbol, extension
        )
        conic_value = evaluate_extension_polynomial(
            conic_extension, root, extension
        )
        require(conic_value != extension.zero, "cubic lies on kernel conic")
        numerator, denominator = extension_value_numerator(
            conic_value, p_symbol
        )
        numerator_flint = compiler.sympy_to_flint(
            sp.Poly(
                numerator,
                trace_symbol,
                p_symbol,
                t_symbol,
                w_symbol,
            ),
            context,
        )
        norm = component.resultant(numerator_flint, 1)
        require(not norm.is_zero(), "zero cubic kernel-conic norm")
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_CUBIC_CONIC_PASS "
            "generic_conic_root=false "
            f"norm_terms={len(norm.to_dict())} degrees={norm.degrees()} "
            f"digest={compiler.polynomial_digest(norm)}",
            flush=True,
        )
        compiler.emit_factorization(norm, "cubic_conic_norm", context)
        denominator_flint = compiler.sympy_to_flint(
            sp.Poly(
                denominator,
                trace_symbol,
                p_symbol,
                t_symbol,
                w_symbol,
            ),
            context,
        )
        compiler.emit_factorization(
            denominator_flint, "cubic_conic_denominator", context
        )
        return
    pairs = ("01", "02", "03") if args.pair == "all" else (args.pair,)
    projections = []
    for pair in pairs:
        left, right = map(int, pair)
        resultant = residuals[left].resultant(residuals[right], 3)
        require(not resultant.is_zero(), "zero projection")
        projections.append(resultant)
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_PROJECTION_PASS "
            f"allocation={args.allocation} pair={pair} "
            f"terms={len(resultant.to_dict())} degrees={resultant.degrees()} "
            f"digest={compiler.polynomial_digest(resultant)}",
            flush=True,
        )
        if args.factor:
            compiler.emit_factorization(resultant, f"projection={pair}", context)

    if len(projections) > 1:
        common = projections[0]
        for projection in projections[1:]:
            common = common.gcd(projection)
        require(not common.is_zero(), "zero projection gcd")
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_GCD_PASS "
            f"allocation={args.allocation} terms={len(common.to_dict())} "
            f"degrees={common.degrees()} "
            f"digest={compiler.polynomial_digest(common)}",
            flush=True,
        )
        compiler.emit_factorization(common, "projection_gcd", context)


if __name__ == "__main__":
    main()
