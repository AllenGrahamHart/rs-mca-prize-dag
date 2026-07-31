#!/usr/bin/env python3
"""Finite replay for the fixed-mixed common linear rank curve."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import flint


DEPLOYED_PRIME = 2130706433
HERE = Path(__file__).resolve().parent
DIRECT = HERE / "kb_c2_112_aligned_positive_unramified_fixed_direct_router.py"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def load_direct():
    spec = importlib.util.spec_from_file_location("fixed_direct", DIRECT)
    require(spec is not None and spec.loader is not None, "direct router loader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--factor", action="store_true")
    parser.add_argument("--finite-replay", action="store_true")
    parser.add_argument("--dump-survivors", type=Path)
    args = parser.parse_args()
    require(flint.__version__ == "0.9.0", "python-flint version")

    direct = load_direct()
    router = direct.load_quartic_router()
    compiler = router.load_compiler()
    moving = direct.load_moving_router()
    context = flint.nmod_mpoly_ctx.get(
        ("b", "p", "t", "w"), DEPLOYED_PRIME, "lex"
    )
    config = router.CONFIGS["mixed"]
    residuals = router.load_cache(compiler, context, "mixed", config)
    conic = router.load_conic_cache(compiler, context, config)

    b_generator, _, t_generator, w_generator = context.gens()
    inverse_four = pow(4, -1, DEPLOYED_PRIME)
    p_value = -(5 * t_generator + 4) * inverse_four
    specialized = [
        polynomial.compose(
            b_generator, p_value, t_generator, w_generator
        )
        for polynomial in (*residuals, conic)
    ]
    curve = (
        4 * t_generator**3 * w_generator**2
        + 22 * t_generator**3 * w_generator
        + 99 * t_generator**3
        + 124 * t_generator**2 * w_generator**2
        + 200 * t_generator**2 * w_generator
        + 76 * t_generator**2
        + 320 * t_generator * w_generator**2
        + 160 * t_generator * w_generator
        - 160 * t_generator
        + 128 * w_generator**2 - 128
    )
    require(
        all((polynomial % curve).is_zero() for polynomial in specialized[:4]),
        "rank curve missing from residual minor",
    )
    norm = curve.resultant(specialized[4], 3)
    require(not norm.is_zero(), "zero linear rank-curve norm")
    _, norm_factors = norm.factor()
    print(
        "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_MIXED_"
        "LINEAR_NORM_PASS "
        f"terms={len(norm.to_dict())} degrees={norm.degrees()} "
        f"digest={compiler.polynomial_digest(norm)}",
        flush=True,
    )
    if args.factor:
        compiler.emit_factorization(norm, "fixed_mixed_linear_norm", context)
    if not args.finite_replay:
        return

    _, exact_equations = compiler.build_cell("fixed-moving", "mixed")
    flint_equations = [
        compiler.sympy_to_flint(equation, context)
        for equation in exact_equations
    ]
    skipped_degree = 0
    endpoint_candidates = 0
    boundary = 0
    empty = 0
    survivors = []
    survivor_records = []
    for index, (factor, _) in enumerate(norm_factors):
        modulus = moving.univariate_modulus(factor, 2)
        t_degree = modulus.degree()
        if 6 % t_degree:
            skipped_degree += 1
            print(
                f"linear_factor={index} t_degree={t_degree} "
                "status=NO_F_P6_ROOT",
                flush=True,
            )
            continue
        field = flint.fq_default_ctx(modulus=modulus, fq_type="FQ_NMOD")
        t_value = field.gen()
        p_fixed = -(5 * t_value + 4) / field(4)
        endpoint_candidates += 1
        base_forbidden = (
            p_fixed * (p_fixed - 1)
            * (p_fixed - t_value + 1) * (p_fixed + t_value + 1)
            * (p_fixed + 2 * t_value + 4)
            * (4 * p_fixed + 2 * t_value + 1)
            * (5 * p_fixed + 4 * t_value + 5)
            * (t_value**2 - 4 * p_fixed)
        )
        if base_forbidden == field.zero():
            boundary += 1
            print(
                f"linear_factor={index} t_degree={t_degree} "
                "status=BASE_BOUNDARY",
                flush=True,
            )
            continue
        polynomial_context = flint.fq_default_poly_ctx(field)
        w_gcd = moving.evaluate_ptw_polynomial(
            residuals[0], p_fixed, t_value, polynomial_context
        )
        for polynomial in (*residuals[1:], conic):
            w_gcd = w_gcd.gcd(moving.evaluate_ptw_polynomial(
                polynomial, p_fixed, t_value, polynomial_context
            ))
        if w_gcd.degree() == 0:
            empty += 1
            print(
                f"linear_factor={index} t_degree={t_degree} "
                "status=MINOR_CONIC_EMPTY",
                flush=True,
            )
            continue
        statuses = []
        _, w_factors = w_gcd.factor()
        for w_factor, _ in w_factors:
            w_degree = w_factor.degree()
            if (6 // t_degree) % w_degree:
                statuses.append(f"W{w_degree}_NO_F_P6_ROOT")
                continue
            require(w_degree == 1, "unrouted deployed w extension")
            w_value = -w_factor[0] / w_factor[1]
            scale_denominator = (
                p_fixed * w_value - 4 * p_fixed
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
            b_gcd = moving.evaluate_trace_polynomial(
                flint_equations[0],
                p_fixed,
                t_value,
                w_value,
                polynomial_context,
            )
            for equation in flint_equations[1:]:
                b_gcd = b_gcd.gcd(moving.evaluate_trace_polynomial(
                    equation,
                    p_fixed,
                    t_value,
                    w_value,
                    polynomial_context,
                ))
            if b_gcd.degree() == 0:
                empty += 1
                statuses.append("ORIGINAL_EQUATIONS_EMPTY")
                continue
            b_variable = polynomial_context.gen()
            b_forbidden = (
                b_variable * (b_variable - 2) * (2 * b_variable - 1)
                * (b_variable - 1) * (b_variable + 1)
                * (b_variable**2 + t_value * b_variable + p_fixed)
                * (1 + t_value * b_variable + p_fixed * b_variable**2)
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
                require(b_degree == 1, "unrouted deployed b extension")
                b_value = -b_factor[0] / b_factor[1]
                equation_values = [
                    moving.evaluate_trace_polynomial(
                        equation,
                        p_fixed,
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
                survivors.append((index, t_degree, w_degree, b_degree))
                survivor_records.append({
                    "factor_index": index,
                    "modulus": [int(value) for value in modulus],
                    "t": [int(value) for value in t_value.to_list()],
                    "p": [int(value) for value in p_fixed.to_list()],
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
                statuses.append("SURVIVOR_B1")
        print(
            f"linear_factor={index} t_degree={t_degree} "
            f"w_gcd_degree={w_gcd.degree()} "
            f"status={','.join(statuses) or 'EMPTY'}",
            flush=True,
        )

    print(
        "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_MIXED_"
        "LINEAR_FINITE_REPLAY_PASS "
        f"norm_factors={len(norm_factors)} skipped_degree={skipped_degree} "
        f"deployed_endpoints={endpoint_candidates} boundary={boundary} "
        f"empty={empty} survivors={len(survivors)}",
        flush=True,
    )
    if survivors and args.dump_survivors:
        payload = {
            "schema": "kb-c2-112-aligned-positive-fixed-mixed-linear-v1",
            "prime": DEPLOYED_PRIME,
            "allocation": "mixed",
            "minor_cache_sha256": config["cache_sha256"],
            "conic_cache_sha256": config["conic_cache_sha256"],
            "linear_norm_digest": compiler.polynomial_digest(norm),
            "survivors": survivor_records,
        }
        encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"
        args.dump_survivors.write_text(encoded, encoding="ascii")
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_MIXED_"
            f"LINEAR_SURVIVOR_CERTIFICATE_PASS count={len(survivors)} "
            f"path={args.dump_survivors} "
            f"sha256={hashlib.sha256(encoded.encode('ascii')).hexdigest()}",
            flush=True,
        )
        return
    require(not survivors, f"fixed-mixed linear survivors: {survivors}")


if __name__ == "__main__":
    main()
