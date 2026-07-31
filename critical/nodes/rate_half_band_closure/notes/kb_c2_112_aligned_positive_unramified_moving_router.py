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
        "off_common_digests": (
            "a3882e8bb2c445e70b9f594d4ddf2beadd2e2ffd64bf973e682f35908b0018f5",
            "123228f02b6bf1687d4c37f3bc2fa36418ec860bb38d65a3bbc565b729050802",
            "3991528db1a1f476582e3d5814df421f8fb968410f0a8994d786c54334bf5fca",
        ),
    },
    "swap": {
        "cache": HERE / "kb_c2_112_aligned_positive_unramified_moving_swap_minors.json",
        "conic_cache": HERE / "kb_c2_112_aligned_positive_unramified_moving_swap_conic.json",
        "cache_sha256": "cafb0e48b2be45a98e72dbe5a1689f3ffe9a6bda64e685ea152873af48ab3d86",
        "conic_cache_sha256": "aacf8976e2fe3933055fb8e7d1a90d2b176dad8699ce37cbf2c0f7f3d6fd521e",
        "residual_digests": (
            "26452db131405a042769b8ec06338d97184fb3b5cb2b3a3b9916d5075d93fe42",
            "2b35a062187051891c9208b055a11af76df40c473cde2375ef5afcbe2b6a426c",
            "77a57e7fe1829d13e7a80e27abb651c1db28ac7887d29dbe26a3a86d277873a3",
            "15f984e753ce2f35ef8effee17f7fbbff340fd1bd3883249cb424f12178669ed",
        ),
        "off_common_digests": (
            "bd7f29ac722c6a42084e9a65f6c687daf9cef0d13d121ce129e7ce606fd28d92",
            "8abd5c5c46bd6380dce7581bf0b2c681ab58d48a664693ee9055ea97fe0c3fce",
            "e5d10f1a8637f850e6dacf0a94de67047ec5330cdbd80a475dbdc586a50665cd",
        ),
    },
    "mixed": {
        "cache": HERE / "kb_c2_112_aligned_positive_unramified_moving_mixed_minors.json",
        "conic_cache": HERE / "kb_c2_112_aligned_positive_unramified_moving_mixed_conic.json",
        "cache_sha256": "799e8feb8f89fee7bf7dab30c3e1e4522380bb490f350a5c93f48f6ff19d3565",
        "conic_cache_sha256": "639a9eeacf175fbfa2e427ca8ad6c3dae1110f658bf4edbe7e3136f2c1748880",
        "component_digest": "9b318c946825ce375fc493b90aa2699b8aebf6868bf552e9a1e8419a66d134b5",
        "residual_digests": (
            "19368af4bc1c045ef91c8246c0dab28af41c94e2b8942f9c1818ffe1a7255773",
            "d1cef76a2057ab469fc5541ba04f361acb9c726e117475f6beb0fa6b82a2f87e",
            "2f1944962810dfd8588bb030d7e0bd565fa0abced32efc9fc9447bd97aa2ecce",
            "40050000690c16beb7de39ee38803e9055eaf645d6d1d79d306fbc6a1a6e80a4",
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


def flint_component_expression(polynomial, p, t):
    expression = sp.Integer(0)
    for monomial, coefficient in polynomial.to_dict().items():
        require(
            monomial[0] == 0 and monomial[3] == 0,
            "component variable support",
        )
        expression += int(coefficient) * p**monomial[1] * t**monomial[2]
    return expression


def univariate_modulus(polynomial, variable_index: int):
    degree = polynomial.degrees()[variable_index]
    coefficients = [0 for _ in range(degree + 1)]
    for monomial, coefficient in polynomial.to_dict().items():
        require(
            all(
                exponent == 0
                for index, exponent in enumerate(monomial)
                if index != variable_index
            ),
            "non-univariate norm factor",
        )
        coefficients[monomial[variable_index]] = int(coefficient)
    return flint.fmpz_mod_poly_ctx(DEPLOYED_PRIME)(coefficients)


def evaluate_ptw_polynomial(polynomial, p_value, t_value, polynomial_context):
    coefficients = [
        p_value * 0
        for _ in range(polynomial.degrees()[3] + 1)
    ]
    for monomial, coefficient in polynomial.to_dict().items():
        require(monomial[0] == 0, "unexpected trace term in determinant cache")
        coefficients[monomial[3]] += (
            int(coefficient)
            * p_value**monomial[1]
            * t_value**monomial[2]
        )
    return polynomial_context(coefficients)


def evaluate_trace_polynomial(
        polynomial, p_value, t_value, w_value, polynomial_context):
    coefficients = [
        p_value * 0
        for _ in range(polynomial.degrees()[0] + 1)
    ]
    for monomial, coefficient in polynomial.to_dict().items():
        coefficients[monomial[0]] += (
            int(coefficient)
            * p_value**monomial[1]
            * t_value**monomial[2]
            * w_value**monomial[3]
        )
    return polynomial_context(coefficients)


def evaluate_as_p_polynomial(polynomial, t_value, polynomial_context):
    coefficients = [
        t_value * 0
        for _ in range(polynomial.degrees()[1] + 1)
    ]
    for monomial, coefficient in polynomial.to_dict().items():
        require(
            monomial[0] == 0 and monomial[3] == 0,
            "unexpected variable in endpoint projection",
        )
        coefficients[monomial[1]] += (
            int(coefficient) * t_value**monomial[2]
        )
    return polynomial_context(coefficients)


def finite_swap_replay(
        compiler, residuals, conic, equations, norm_factors):
    empty = 0
    boundary = 0
    rank_candidates = 0
    survivors = []
    for index, (factor, _) in enumerate(norm_factors):
        modulus = univariate_modulus(factor, 2)
        field = flint.fq_default_ctx(
            modulus=modulus, fq_type="FQ_NMOD"
        )
        t_value = field.gen()
        denominator = t_value + 5
        if denominator == field.zero():
            # On t=-5 the component p(t+5)+t equals -5, so it is empty.
            boundary += 1
            print(
                "finite_factor=" f"{index} degree={modulus.degree()} "
                "status=COMPONENT_DENOMINATOR_EMPTY",
                flush=True,
            )
            continue
        p_value = -t_value / denominator
        base_forbidden = (
            p_value * (p_value - 1)
            * (p_value - t_value + 1) * (p_value + t_value + 1)
            * (p_value + 2 * t_value + 4)
            * (4 * p_value + 2 * t_value + 1)
            * (5 * p_value + 4 * t_value + 5)
            * (t_value**2 - 4 * p_value)
        )
        if base_forbidden == field.zero():
            boundary += 1
            print(
                f"finite_factor={index} degree={modulus.degree()} "
                "status=BASE_BOUNDARY",
                flush=True,
            )
            continue
        polynomial_context = flint.fq_default_poly_ctx(field)
        common = evaluate_ptw_polynomial(
            residuals[0], p_value, t_value, polynomial_context
        )
        for polynomial in (*residuals[1:], conic):
            common = common.gcd(evaluate_ptw_polynomial(
                polynomial, p_value, t_value, polynomial_context
            ))
        if common.degree() == 0:
            empty += 1
            status = "EMPTY"
        else:
            rank_candidates += 1
            require(common.degree() == 1, "nonlinear finite w candidate")
            w_value = -common[0] / common[1]
            scale_denominator = (
                p_value * w_value - 4 * p_value
                + 2 * t_value * w_value - 2 * t_value
                + 4 * w_value - 1
            )
            w_forbidden = (
                w_value * (w_value - 1) * (w_value + 1)
                * scale_denominator
            )
            if w_forbidden == field.zero():
                boundary += 1
                status = "W_BOUNDARY"
            else:
                trace_gcd = evaluate_trace_polynomial(
                    equations[0],
                    p_value,
                    t_value,
                    w_value,
                    polynomial_context,
                )
                for equation in equations[1:]:
                    trace_gcd = trace_gcd.gcd(evaluate_trace_polynomial(
                        equation,
                        p_value,
                        t_value,
                        w_value,
                        polynomial_context,
                    ))
                if trace_gcd.degree() == 0:
                    empty += 1
                    status = "ORIGINAL_EQUATIONS_EMPTY"
                else:
                    trace = polynomial_context.gen()
                    endpoint_orbit_collision = (
                        p_value * (trace**2 - 2)
                        + t_value * (1 + p_value) * trace
                        + 1 + t_value**2 + p_value**2
                    )
                    trace_forbidden = (
                        (trace - 2) * (trace + 2) * (2 * trace - 5)
                        * endpoint_orbit_collision
                    )
                    forbidden_gcd = trace_gcd.gcd(trace_forbidden)
                    if forbidden_gcd.degree() == trace_gcd.degree():
                        boundary += 1
                        status = "TRACE_BOUNDARY"
                    else:
                        survivors.append((
                            index,
                            modulus.degree(),
                            common.degree(),
                            trace_gcd.degree(),
                        ))
                        status = (
                            "SURVIVOR_W_TRACE_DEGREES_"
                            f"{common.degree()}_{trace_gcd.degree()}"
                        )
        print(
            f"finite_factor={index} degree={modulus.degree()} status={status}",
            flush=True,
        )
    require(not survivors, f"finite swap survivors: {survivors}")
    print(
        "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_"
        "SWAP_FINITE_COMPONENT_REPLAY_PASS "
        f"factors={len(norm_factors)} rank_candidates={rank_candidates} "
        f"empty={empty} boundary={boundary}",
        flush=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allocation", choices=tuple(CONFIGS), required=True)
    parser.add_argument("--pair", choices=("01", "02", "03", "all"), default="all")
    parser.add_argument("--factor", action="store_true")
    parser.add_argument("--linear-component", action="store_true")
    parser.add_argument("--component", action="store_true")
    parser.add_argument(
        "--cubic-component", action="store_true", help=argparse.SUPPRESS
    )
    parser.add_argument("--component-resultant-screen", action="store_true")
    parser.add_argument("--finite-replay", action="store_true")
    parser.add_argument("--off-common-screen", action="store_true")
    parser.add_argument("--dump-survivors", type=Path)
    args = parser.parse_args()

    require(flint.__version__ == "0.9.0", "python-flint version")
    compiler = load_compiler()
    context = flint.nmod_mpoly_ctx.get(
        ("trace", "p", "t", "w"), DEPLOYED_PRIME, "lex"
    )
    residuals = load_residuals(compiler, context, args.allocation)
    if args.off_common_screen:
        require(
            "off_common_digests" in CONFIGS[args.allocation],
            "off-common screen allocation",
        )
        configured = CONFIGS[args.allocation]["off_common_digests"]
        off_common = []
        for right, digest in zip((1, 2, 3), configured):
            projection = residuals[0].resultant(residuals[right], 3)
            _, factors = projection.factor()
            candidates = [
                factor for factor, exponent in factors
                if exponent == 1
                and compiler.polynomial_digest(factor) == digest
            ]
            require(len(candidates) == 1, "unique off-common cofactor")
            off_common.append(candidates[0])
        first_norm = off_common[0].resultant(off_common[1], 1)
        second_norm = off_common[0].resultant(off_common[2], 1)
        require(
            not first_norm.is_zero() and not second_norm.is_zero(),
            "zero off-common projection resultant",
        )
        common_norm = first_norm.gcd(second_norm)
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_"
            f"OFF_COMMON_SCREEN_PASS allocation={args.allocation} "
            f"terms={len(common_norm.to_dict())} "
            f"degrees={common_norm.degrees()} "
            f"digest={compiler.polynomial_digest(common_norm)}",
            flush=True,
        )
        norm_factors = compiler.emit_factorization(
            common_norm, "off_common_norm_gcd", context
        )
        if args.finite_replay:
            p_candidates = 0
            boundary_candidates = 0
            unresolved_candidates = []
            conic = load_conic(compiler, context, args.allocation)
            _, conic_factors = conic.factor()
            conic_residuals = [
                factor for factor, exponent in conic_factors
                if len(factor.to_dict()) > 100 and exponent == 1
            ]
            require(len(conic_residuals) == 1, "unique kernel-conic residual")
            conic_residual = conic_residuals[0]
            for index, (factor, _) in enumerate(norm_factors):
                modulus = univariate_modulus(factor, 2)
                field = flint.fq_default_ctx(
                    modulus=modulus, fq_type="FQ_NMOD"
                )
                t_value = field.gen()
                polynomial_context = flint.fq_default_poly_ctx(field)
                p_gcd = evaluate_as_p_polynomial(
                    off_common[0], t_value, polynomial_context
                )
                for polynomial in off_common[1:]:
                    p_gcd = p_gcd.gcd(evaluate_as_p_polynomial(
                        polynomial, t_value, polynomial_context
                    ))
                _, p_factors = p_gcd.factor()
                print(
                    f"off_common_factor={index} t_degree={modulus.degree()} "
                    f"p_gcd_degree={p_gcd.degree()} "
                    f"p_factor_degrees="
                    f"{','.join(str(item.degree()) for item, _ in p_factors) or '-'}",
                    flush=True,
                )
                for p_index, (p_factor, _) in enumerate(p_factors):
                    p_candidates += 1
                    if p_factor.degree() != 1:
                        unresolved_candidates.append((
                            index, p_index, p_factor.degree(), "p"
                        ))
                        print(
                            f"off_common_factor={index} p_factor={p_index} "
                            f"status=UNROUTED_P_DEGREE_{p_factor.degree()}",
                            flush=True,
                        )
                        continue
                    p_value = -p_factor[0] / p_factor[1]
                    base_forbidden = (
                        p_value * (p_value - 1)
                        * (p_value - t_value + 1)
                        * (p_value + t_value + 1)
                        * (p_value + 2 * t_value + 4)
                        * (4 * p_value + 2 * t_value + 1)
                        * (5 * p_value + 4 * t_value + 5)
                        * (t_value**2 - 4 * p_value)
                    )
                    if base_forbidden == field.zero():
                        boundary_candidates += 1
                        status = "BASE_BOUNDARY"
                    else:
                        w_gcd = evaluate_ptw_polynomial(
                            residuals[0],
                            p_value,
                            t_value,
                            polynomial_context,
                        )
                        for polynomial in (*residuals[1:], conic_residual):
                            w_gcd = w_gcd.gcd(evaluate_ptw_polynomial(
                                polynomial,
                                p_value,
                                t_value,
                                polynomial_context,
                            ))
                        _, w_factors = w_gcd.factor()
                        status = (
                            f"W_GCD_{w_gcd.degree()}_FACTOR_DEGREES_"
                            f"{','.join(str(item.degree()) for item, _ in w_factors) or '-'}"
                        )
                        if w_gcd.degree() > 0:
                            unresolved_candidates.append((
                                index, p_index, w_gcd.degree(), "w"
                            ))
                    print(
                        f"off_common_factor={index} p_factor={p_index} "
                        f"status={status}",
                        flush=True,
                    )
            if args.allocation == "swap":
                require(
                    not unresolved_candidates,
                    f"off-common survivors: {unresolved_candidates}",
                )
                require(
                    p_candidates == boundary_candidates,
                    "off-common candidate accounting",
                )
                print(
                    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_"
                    "SWAP_OFF_COMMON_FINITE_REPLAY_PASS "
                    f"t_factors={len(norm_factors)} "
                    f"p_candidates={p_candidates} "
                    f"boundary={boundary_candidates}",
                    flush=True,
                )
            else:
                require(
                    not unresolved_candidates,
                    f"off-common survivors: {unresolved_candidates}",
                )
                require(
                    p_candidates == boundary_candidates,
                    "off-common candidate accounting",
                )
                print(
                    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_"
                    "OFF_COMMON_FINITE_REPLAY_PASS "
                    f"allocation={args.allocation} "
                    f"t_factors={len(norm_factors)} "
                    f"p_candidates={p_candidates} "
                    f"boundary={boundary_candidates}",
                    flush=True,
                )
        return
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
        if args.allocation in ("same", "swap", "mixed"):
            t_power = {"same": 3, "swap": 2, "mixed": 4}[args.allocation]
            expected = t**t_power * (t + 1) * (t + 4) * (w - 1)
            compiler.require_associate(
                admissible_support,
                expected,
                "moving linear exclusion support",
            )
            print(
                "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_"
                f"LINEAR_EXCLUSION_PASS allocation={args.allocation} "
                "component=4*p+5*t+4 "
                "support=w-1,discriminant,q(1)",
                flush=True,
            )
        return
    if args.component_resultant_screen:
        trace_symbol, p_symbol, t_symbol, w_symbol = sp.symbols(
            "trace p t w"
        )
        if args.allocation == "same":
            component = compiler.sympy_to_flint(
                sp.Poly(
                    same_cubic(p_symbol, t_symbol),
                    trace_symbol,
                    p_symbol,
                    t_symbol,
                    w_symbol,
                ),
                context,
            )
        elif args.allocation == "swap":
            component = compiler.sympy_to_flint(
                sp.Poly(
                    p_symbol * t_symbol + 5 * p_symbol + t_symbol,
                    trace_symbol,
                    p_symbol,
                    t_symbol,
                    w_symbol,
                ),
                context,
            )
        else:
            require(args.allocation == "mixed", "component screen allocation")
            first_projection = residuals[0].resultant(residuals[1], 3)
            _, factors = first_projection.factor()
            candidates = [
                factor for factor, exponent in factors
                if exponent == 1
                and compiler.polynomial_digest(factor)
                == CONFIGS[args.allocation]["component_digest"]
            ]
            require(len(candidates) == 1, "unique configured component")
            component = candidates[0]
        conic = load_conic(compiler, context, args.allocation)
        _, conic_factors = conic.factor()
        conic_residuals = [
            factor for factor, exponent in conic_factors
            if len(factor.to_dict()) > 100 and exponent == 1
        ]
        require(len(conic_residuals) == 1, "unique kernel-conic residual")
        conic_residual = conic_residuals[0]
        print(
            f"component_resultant=START allocation={args.allocation} "
            f"minor_terms={len(residuals[0].to_dict())} "
            f"conic_terms={len(conic_residual.to_dict())} "
            f"conic_degrees={conic_residual.degrees()}",
            flush=True,
        )
        resultant = residuals[0].resultant(conic_residual, 3)
        require(not resultant.is_zero(), "zero minor-conic resultant")
        _, remainder = divmod(resultant, component)
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_"
            f"COMPONENT_RESULTANT_SCREEN_PASS allocation={args.allocation} "
            f"component_divides={str(remainder.is_zero()).lower()} "
            f"terms={len(resultant.to_dict())} degrees={resultant.degrees()} "
            f"digest={compiler.polynomial_digest(resultant)}",
            flush=True,
        )
        if not remainder.is_zero():
            norm = component.resultant(resultant, 1)
            require(not norm.is_zero(), "zero component-conic norm")
            print(
                "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_"
                f"COMPONENT_RESULTANT_NORM_PASS allocation={args.allocation} "
                f"terms={len(norm.to_dict())} degrees={norm.degrees()} "
                f"digest={compiler.polynomial_digest(norm)}",
                flush=True,
            )
            norm_factors = compiler.emit_factorization(
                norm, "component_direct_conic_norm", context
            )
            if args.finite_replay:
                _, exact_equations = compiler.build_cell(
                    "moving-moving", args.allocation
                )
                exact_context = flint.nmod_mpoly_ctx.get(
                    ("trace", "p", "t", "w"),
                    DEPLOYED_PRIME,
                    "lex",
                )
                flint_equations = [
                    compiler.sympy_to_flint(equation, exact_context)
                    for equation in exact_equations
                ]
                empty_count = 0
                boundary_count = 0
                rank_candidates = 0
                survivors = []
                survivor_records = []
                for index, (factor, _) in enumerate(norm_factors):
                    modulus = univariate_modulus(factor, 2)
                    field = flint.fq_default_ctx(
                        modulus=modulus, fq_type="FQ_NMOD"
                    )
                    t_value = field.gen()
                    polynomial_context = flint.fq_default_poly_ctx(field)
                    p_gcd = evaluate_as_p_polynomial(
                        component, t_value, polynomial_context
                    ).gcd(evaluate_as_p_polynomial(
                        resultant, t_value, polynomial_context
                    ))
                    _, p_factors = p_gcd.factor()
                    statuses = []
                    for p_factor, _ in p_factors:
                        if p_factor.degree() != 1:
                            survivors.append((
                                index, p_factor.degree(), -1, -1
                            ))
                            statuses.append(f"P{p_factor.degree()}")
                            continue
                        p_value = -p_factor[0] / p_factor[1]
                        base_forbidden = (
                            p_value * (p_value - 1)
                            * (p_value - t_value + 1)
                            * (p_value + t_value + 1)
                            * (p_value + 2 * t_value + 4)
                            * (4 * p_value + 2 * t_value + 1)
                            * (5 * p_value + 4 * t_value + 5)
                            * (t_value**2 - 4 * p_value)
                        )
                        if base_forbidden == field.zero():
                            statuses.append("BOUNDARY")
                            boundary_count += 1
                            continue
                        w_gcd = evaluate_ptw_polynomial(
                            residuals[0],
                            p_value,
                            t_value,
                            polynomial_context,
                        )
                        for polynomial in (*residuals[1:], conic_residual):
                            w_gcd = w_gcd.gcd(evaluate_ptw_polynomial(
                                polynomial,
                                p_value,
                                t_value,
                                polynomial_context,
                            ))
                        _, w_factors = w_gcd.factor()
                        if w_gcd.degree() == 0:
                            empty_count += 1
                            statuses.append("EMPTY")
                            continue
                        rank_candidates += 1
                        if w_gcd.degree() != 1:
                            survivors.append((
                                index, p_factor.degree(), w_gcd.degree(), -1
                            ))
                            statuses.append(f"UNROUTED_W{w_gcd.degree()}")
                            continue
                        w_value = -w_gcd[0] / w_gcd[1]
                        scale_denominator = (
                            p_value * w_value - 4 * p_value
                            + 2 * t_value * w_value - 2 * t_value
                            + 4 * w_value - 1
                        )
                        if (
                            w_value * (w_value - 1) * (w_value + 1)
                            * scale_denominator
                        ) == field.zero():
                            boundary_count += 1
                            statuses.append("W_BOUNDARY")
                            continue
                        trace_gcd = evaluate_trace_polynomial(
                            flint_equations[0],
                            p_value,
                            t_value,
                            w_value,
                            polynomial_context,
                        )
                        for equation in flint_equations[1:]:
                            trace_gcd = trace_gcd.gcd(
                                evaluate_trace_polynomial(
                                    equation,
                                    p_value,
                                    t_value,
                                    w_value,
                                    polynomial_context,
                                )
                            )
                        if trace_gcd.degree() == 0:
                            empty_count += 1
                            statuses.append("ORIGINAL_EQUATIONS_EMPTY")
                            continue
                        trace = polynomial_context.gen()
                        endpoint_orbit_collision = (
                            p_value * (trace**2 - 2)
                            + t_value * (1 + p_value) * trace
                            + 1 + t_value**2 + p_value**2
                        )
                        trace_forbidden = (
                            (trace - 2) * (trace + 2) * (2 * trace - 5)
                            * endpoint_orbit_collision
                        )
                        forbidden_gcd = trace_gcd.gcd(trace_forbidden)
                        if forbidden_gcd.degree() == trace_gcd.degree():
                            boundary_count += 1
                            statuses.append("TRACE_BOUNDARY")
                        else:
                            trace_value = -trace_gcd[0] / trace_gcd[1]
                            equation_values = [
                                evaluate_trace_polynomial(
                                    equation,
                                    p_value,
                                    t_value,
                                    w_value,
                                    polynomial_context,
                                )(trace_value)
                                for equation in flint_equations
                            ]
                            require(
                                all(value == field.zero()
                                    for value in equation_values),
                                "survivor equation replay",
                            )
                            survivors.append((
                                index,
                                p_factor.degree(),
                                w_gcd.degree(),
                                trace_gcd.degree(),
                            ))
                            survivor_records.append({
                                "factor_index": index,
                                "modulus": [int(value) for value in modulus],
                                "t": [int(value) for value in t_value.to_list()],
                                "p": [int(value) for value in p_value.to_list()],
                                "w": [int(value) for value in w_value.to_list()],
                                "trace": [
                                    int(value) for value in trace_value.to_list()
                                ],
                                "base_forbidden": [
                                    int(value)
                                    for value in base_forbidden.to_list()
                                ],
                                "scale_denominator": [
                                    int(value)
                                    for value in scale_denominator.to_list()
                                ],
                                "trace_forbidden": [
                                    int(value)
                                    for value in trace_forbidden(trace_value).to_list()
                                ],
                            })
                            statuses.append(
                                f"SURVIVOR_TRACE{trace_gcd.degree()}"
                            )
                    print(
                        f"component_finite_factor={index} "
                        f"t_degree={modulus.degree()} "
                        f"p_gcd_degree={p_gcd.degree()} "
                        f"status={','.join(statuses) or 'EMPTY'}",
                        flush=True,
                    )
                if survivors and args.dump_survivors:
                    payload = {
                        "schema": "kb-c2-112-aligned-positive-moving-survivors-v1",
                        "prime": DEPLOYED_PRIME,
                        "allocation": args.allocation,
                        "cache_sha256": CONFIGS[args.allocation]["cache_sha256"],
                        "conic_cache_sha256": CONFIGS[args.allocation][
                            "conic_cache_sha256"
                        ],
                        "direct_norm_digest": compiler.polynomial_digest(norm),
                        "survivors": survivor_records,
                    }
                    encoded = json.dumps(
                        payload, sort_keys=True, separators=(",", ":")
                    ) + "\n"
                    args.dump_survivors.write_text(encoded, encoding="ascii")
                    print(
                        "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_"
                        "DIRECT_COMPONENT_SURVIVORS_PASS "
                        f"allocation={args.allocation} count={len(survivors)} "
                        f"path={args.dump_survivors} "
                        f"sha256={hashlib.sha256(encoded.encode('ascii')).hexdigest()}",
                        flush=True,
                    )
                    return
                require(not survivors,
                        f"direct component survivors: {survivors}")
                print(
                    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_"
                    "DIRECT_FINITE_COMPONENT_REPLAY_PASS "
                    f"allocation={args.allocation} "
                    f"factors={len(norm_factors)} "
                    f"rank_candidates={rank_candidates} "
                    f"empty={empty_count} boundary={boundary_count}",
                    flush=True,
                )
        return
    if args.component or args.cubic_component:
        trace_symbol, p_symbol, t_symbol, w_symbol = sp.symbols(
            "trace p t w"
        )
        if args.allocation == "same":
            component_expression = same_cubic(p_symbol, t_symbol)
            component_name = "reciprocal-cubic"
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
        elif args.allocation == "swap":
            component_expression = p_symbol * t_symbol + 5 * p_symbol + t_symbol
            component_name = "bilinear"
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
        else:
            require(args.allocation == "mixed", "component router allocation")
            first_projection = residuals[0].resultant(residuals[1], 3)
            _, factors = first_projection.factor()
            candidates = [
                factor for factor, exponent in factors
                if exponent == 1
                and compiler.polynomial_digest(factor)
                == CONFIGS[args.allocation]["component_digest"]
            ]
            require(len(candidates) == 1, "unique configured component")
            component = candidates[0]
            component_expression = flint_component_expression(
                component, p_symbol, t_symbol
            )
            component_name = "degree-twelve"
        for right in (1, 2, 3):
            projection = residuals[0].resultant(residuals[right], 3)
            quotient, remainder = divmod(projection, component)
            require(remainder.is_zero(), "missing configured projection factor")
            require(
                not (quotient % component).is_zero(),
                "configured component multiplicity",
            )
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
        require(len(common) == 2, "component common root is not linear")
        root = -common[0]
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_COMPONENT_ROOT_PASS "
            f"allocation={args.allocation} component={component_name} degree=1 "
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
        require(conic_value != extension.zero, "component lies on kernel conic")
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
        require(not norm.is_zero(), "zero component kernel-conic norm")
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_COMPONENT_CONIC_PASS "
            f"allocation={args.allocation} component={component_name} "
            "generic_conic_root=false "
            f"norm_terms={len(norm.to_dict())} degrees={norm.degrees()} "
            f"digest={compiler.polynomial_digest(norm)}",
            flush=True,
        )
        norm_factors = compiler.emit_factorization(
            norm, "component_conic_norm", context
        )
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
            denominator_flint, "component_conic_denominator", context
        )
        if args.finite_replay:
            require(args.allocation == "swap", "finite replay is pinned to swap")
            _, exact_equations = compiler.build_cell(
                "moving-moving", args.allocation
            )
            exact_context = flint.nmod_mpoly_ctx.get(
                ("trace", "p", "t", "w"), DEPLOYED_PRIME, "lex"
            )
            flint_equations = [
                compiler.sympy_to_flint(equation, exact_context)
                for equation in exact_equations
            ]
            finite_swap_replay(
                compiler,
                residuals,
                conic_residual,
                flint_equations,
                norm_factors,
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
