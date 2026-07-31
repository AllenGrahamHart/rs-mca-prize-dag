#!/usr/bin/env python3
"""Direct finite router for aligned-positive unramified fixed-moving cells.

This starts from the pinned residual-minor and kernel-conic caches.  It uses
an affine minor-conic resultant, so function-field root denominators are
retained automatically.  Projection support is only necessary until every
finite point is replayed in the original four quadratic equations.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import flint


DEPLOYED_PRIME = 2130706433
HERE = Path(__file__).resolve().parent
QUARTIC_ROUTER = (
    HERE / "kb_c2_112_aligned_positive_unramified_quartic_router.py"
)
MOVING_ROUTER = (
    HERE / "kb_c2_112_aligned_positive_unramified_moving_router.py"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def load_quartic_router():
    spec = importlib.util.spec_from_file_location("quartic_router", QUARTIC_ROUTER)
    require(spec is not None and spec.loader is not None, "quartic router loader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_moving_router():
    spec = importlib.util.spec_from_file_location("moving_router", MOVING_ROUTER)
    require(spec is not None and spec.loader is not None, "moving router loader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--allocation", choices=("same", "swap", "mixed"), default="same"
    )
    parser.add_argument("--factor", action="store_true")
    parser.add_argument("--finite-replay", action="store_true")
    parser.add_argument("--dump-survivors", type=Path)
    args = parser.parse_args()
    require(flint.__version__ == "0.9.0", "python-flint version")

    router = load_quartic_router()
    compiler = router.load_compiler()
    context = flint.nmod_mpoly_ctx.get(
        ("b", "p", "t", "w"), DEPLOYED_PRIME, "lex"
    )
    config = router.CONFIGS[args.allocation]
    residuals = router.load_cache(
        compiler, context, args.allocation, config
    )
    conic = router.load_conic_cache(compiler, context, config)
    _, conic_factors = conic.factor()
    conic_residuals = [
        factor for factor, exponent in conic_factors
        if len(factor.to_dict()) > 100 and exponent == 1
    ]
    require(len(conic_residuals) == 1, "unique kernel-conic residual")
    conic_residual = conic_residuals[0]

    b_symbol, p_symbol, t_symbol, w_symbol = router.sp.symbols("b p t w")
    component_expression = router.component_expression(
        args.allocation, p_symbol, t_symbol
    )
    if component_expression is None:
        projection = residuals[0].resultant(residuals[1], 3)
        _, projection_factors = projection.factor()
        candidates = [
            factor for factor, exponent in projection_factors
            if exponent == 1
            and compiler.polynomial_digest(factor) == config["component_digest"]
        ]
        require(len(candidates) == 1, "unique configured component")
        component = candidates[0]
    else:
        component = compiler.sympy_to_flint(
            router.sp.Poly(
                component_expression,
                b_symbol,
                p_symbol,
                t_symbol,
                w_symbol,
            ),
            context,
        )
    resultant = residuals[0].resultant(conic_residual, 3)
    require(not resultant.is_zero(), "zero minor-conic resultant")
    _, remainder = divmod(resultant, component)
    print(
        "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_"
        f"DIRECT_RESULTANT_SCREEN_PASS allocation={args.allocation} "
        f"component_divides={str(remainder.is_zero()).lower()} "
        f"terms={len(resultant.to_dict())} degrees={resultant.degrees()} "
        f"digest={compiler.polynomial_digest(resultant)}",
        flush=True,
    )
    require(not remainder.is_zero(), "component lies on conic resultant")
    norm = component.resultant(resultant, 1)
    require(not norm.is_zero(), "zero direct component norm")
    print(
        "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_"
        f"DIRECT_NORM_PASS allocation={args.allocation} "
        f"terms={len(norm.to_dict())} degrees={norm.degrees()} "
        f"digest={compiler.polynomial_digest(norm)}",
        flush=True,
    )
    norm_factors = norm.factor()[1]
    if args.factor:
        compiler.emit_factorization(norm, "fixed_direct_norm", context)
    if not args.finite_replay:
        return

    moving_router = load_moving_router()
    _, exact_equations = compiler.build_cell("fixed-moving", args.allocation)
    exact_context = flint.nmod_mpoly_ctx.get(
        ("b", "p", "t", "w"), DEPLOYED_PRIME, "lex"
    )
    flint_equations = [
        compiler.sympy_to_flint(equation, exact_context)
        for equation in exact_equations
    ]
    skipped_degree = 0
    boundary = 0
    empty = 0
    deployed_endpoint_candidates = 0
    survivors = []
    survivor_records = []
    for index, (factor, _) in enumerate(norm_factors):
        modulus = moving_router.univariate_modulus(factor, 2)
        t_degree = modulus.degree()
        if 6 % t_degree:
            skipped_degree += 1
            print(
                f"finite_factor={index} t_degree={t_degree} "
                "status=NO_F_P6_ROOT",
                flush=True,
            )
            continue
        field = flint.fq_default_ctx(modulus=modulus, fq_type="FQ_NMOD")
        t_value = field.gen()
        polynomial_context = flint.fq_default_poly_ctx(field)
        p_gcd = moving_router.evaluate_as_p_polynomial(
            component, t_value, polynomial_context
        ).gcd(moving_router.evaluate_as_p_polynomial(
            resultant, t_value, polynomial_context
        ))
        require(p_gcd.degree() >= 0, "zero p gcd")
        _, p_factors = p_gcd.factor()
        statuses = []
        for p_factor, _ in p_factors:
            p_degree = p_factor.degree()
            if (6 // t_degree) % p_degree:
                statuses.append(f"P{p_degree}_NO_F_P6_ROOT")
                continue
            require(p_degree == 1, "unrouted deployed p extension")
            p_value = -p_factor[0] / p_factor[1]
            deployed_endpoint_candidates += 1
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
                statuses.append("BASE_BOUNDARY")
                continue
            w_gcd = moving_router.evaluate_ptw_polynomial(
                residuals[0], p_value, t_value, polynomial_context
            )
            for polynomial in (*residuals[1:], conic_residual):
                w_gcd = w_gcd.gcd(moving_router.evaluate_ptw_polynomial(
                    polynomial, p_value, t_value, polynomial_context
                ))
            if w_gcd.degree() == 0:
                empty += 1
                statuses.append("MINOR_CONIC_EMPTY")
                continue
            _, w_factors = w_gcd.factor()
            for w_factor, _ in w_factors:
                w_degree = w_factor.degree()
                if (6 // t_degree) % w_degree:
                    statuses.append(f"W{w_degree}_NO_F_P6_ROOT")
                    continue
                require(w_degree == 1, "unrouted deployed w extension")
                w_value = -w_factor[0] / w_factor[1]
                scale_denominator = (
                    p_value * w_value - 4 * p_value
                    + 2 * t_value * w_value - 2 * t_value
                    + 4 * w_value - 1
                )
                if (
                    w_value * (w_value - 1) * (w_value + 1)
                    * scale_denominator
                ) == field.zero():
                    boundary += 1
                    statuses.append("W_BOUNDARY")
                    continue
                b_gcd = moving_router.evaluate_trace_polynomial(
                    flint_equations[0],
                    p_value,
                    t_value,
                    w_value,
                    polynomial_context,
                )
                for equation in flint_equations[1:]:
                    b_gcd = b_gcd.gcd(
                        moving_router.evaluate_trace_polynomial(
                            equation,
                            p_value,
                            t_value,
                            w_value,
                            polynomial_context,
                        )
                    )
                if b_gcd.degree() == 0:
                    empty += 1
                    statuses.append("ORIGINAL_EQUATIONS_EMPTY")
                    continue
                b_variable = polynomial_context.gen()
                b_forbidden = (
                    b_variable * (b_variable - 2) * (2 * b_variable - 1)
                    * (b_variable - 1) * (b_variable + 1)
                    * (b_variable**2 + t_value * b_variable + p_value)
                    * (1 + t_value * b_variable + p_value * b_variable**2)
                )
                _, b_factors = b_gcd.factor()
                for b_factor, _ in b_factors:
                    b_degree = b_factor.degree()
                    if (6 // t_degree) % b_degree:
                        statuses.append(f"B{b_degree}_NO_F_P6_ROOT")
                        continue
                    if b_factor.gcd(b_forbidden).degree() == b_degree:
                        boundary += 1
                        statuses.append("B_BOUNDARY")
                        continue
                    survivors.append((index, t_degree, p_degree, w_degree, b_degree))
                    require(b_degree == 1, "nonlinear survivor b factor")
                    b_value = -b_factor[0] / b_factor[1]
                    equation_values = [
                        moving_router.evaluate_trace_polynomial(
                            equation,
                            p_value,
                            t_value,
                            w_value,
                            polynomial_context,
                        )(b_value)
                        for equation in flint_equations
                    ]
                    require(
                        all(value == field.zero() for value in equation_values),
                        "survivor equation replay",
                    )
                    b_forbidden_value = b_forbidden(b_value)
                    require(b_forbidden_value != field.zero(), "survivor b guard")
                    survivor_records.append({
                        "factor_index": index,
                        "modulus": [int(value) for value in modulus],
                        "t": [int(value) for value in t_value.to_list()],
                        "p": [int(value) for value in p_value.to_list()],
                        "w": [int(value) for value in w_value.to_list()],
                        "b": [int(value) for value in b_value.to_list()],
                        "base_forbidden": [
                            int(value) for value in base_forbidden.to_list()
                        ],
                        "scale_denominator": [
                            int(value) for value in scale_denominator.to_list()
                        ],
                        "b_forbidden": [
                            int(value) for value in b_forbidden_value.to_list()
                        ],
                    })
                    statuses.append(f"SURVIVOR_B{b_degree}")
        print(
            f"finite_factor={index} t_degree={t_degree} "
            f"p_gcd_degree={p_gcd.degree()} "
            f"status={','.join(statuses) or 'EMPTY'}",
            flush=True,
        )
    print(
        "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_"
        f"FINITE_REPLAY_PASS allocation={args.allocation} "
        f"norm_factors={len(norm_factors)} skipped_degree={skipped_degree} "
        f"deployed_endpoints={deployed_endpoint_candidates} "
        f"boundary={boundary} empty={empty} survivors={len(survivors)}",
        flush=True,
    )
    if survivors and args.dump_survivors:
        payload = {
            "schema": "kb-c2-112-aligned-positive-fixed-survivors-v1",
            "prime": DEPLOYED_PRIME,
            "allocation": args.allocation,
            "cache_sha256": config["cache_sha256"],
            "conic_cache_sha256": config["conic_cache_sha256"],
            "direct_norm_digest": compiler.polynomial_digest(norm),
            "survivors": survivor_records,
        }
        encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"
        args.dump_survivors.write_text(encoded, encoding="ascii")
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_"
            f"SURVIVOR_CERTIFICATE_PASS allocation={args.allocation} "
            f"count={len(survivors)} path={args.dump_survivors} "
            f"sha256={hashlib.sha256(encoded.encode('ascii')).hexdigest()}",
            flush=True,
        )
        return
    require(not survivors, f"fixed direct survivors: {survivors}")


if __name__ == "__main__":
    main()
