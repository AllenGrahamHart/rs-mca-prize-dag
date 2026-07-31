#!/usr/bin/env python3
"""Screen every off-common projection cofactor in the moving-mixed cell.

The three star projections have respectively three, four, and one factors
after common-component and open-factor removal.  This script computes all
twelve exact endpoint intersections over the deployed prime.  A projection
intersection is only a necessary condition until its endpoint and trace
coordinates are replayed.
"""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path

import flint


DEPLOYED_PRIME = 2130706433
HERE = Path(__file__).resolve().parent
ROUTER = HERE / "kb_c2_112_aligned_positive_unramified_moving_router.py"
FACTOR_DIGESTS = (
    (
        "27dc2c568e0ef0ca4fc4b03d4d117cfd636cc7ed48f7c52053556f13c9ca3632",
        "ff63832304d9161ac8508901af890abf8bc2b7259e34cb941a4727ca7e1388c1",
        "4adfcfacbd60ef2f5afa6c86c29d14ac4ec10fc96cba5b176f9d2c72f0181766",
    ),
    (
        "106bae7e5d7ca5e88c4c39b7477e807ddcff8b0ac4eaffc1f990364c2168d132",
        "b02512c083274778475e6ccaeb49a80f2e7d85f940cf5aa7e61b63e01e57fbe7",
        "9d795b62514a2cd3afa8b81f15f62cc448b2ac1d55af3258f23132487ab15412",
        "332174450bb8b701dea1bfeeb7de3291e8b9a97251d7807aa23f295ec6a9a730",
    ),
    (
        "45b014b8997745ad8a460565f5ed988e715a74935d945bb4c57f33bfa034bd7b",
    ),
)
COMMON_OR_OPEN_DIGESTS = {
    "fb4eb943d5c1108596e2199a57fecaff32c3c94bb13305773054123f1b74d0a5",
    "9b318c946825ce375fc493b90aa2699b8aebf6868bf552e9a1e8419a66d134b5",
    "544274fb97120d080da62a45b251927b63f70bd19285d3b60ad8c17f8f861d35",
    "74192520e1f5f028cb2ff733e206f8084a5aa920ed5985ff94f44e8c33f02718",
    "d54e40904960bcd20c2da066128d71124ade633fe8e4ab65360cba361dbb7fcd",
    "108ffdd9fa92bdeaba39a5fb2560e9155ed60e7e040f89be4d94ec3a3dc5348e",
    "8cec5db42e9f38668aa4f9afe928bb9adf9610c3b59f1789f26f7759802ba26e",
    "f87faf4fa44b76fd9d8854ff630cfda98653a46e6d5fa69da86a7600c0e9e6ba",
    "e33a2320f3a6377c5e39cc0a8aa7b5dc151ef561324c66d2decf32b46935a909",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def load_router():
    spec = importlib.util.spec_from_file_location("moving_router", ROUTER)
    require(spec is not None and spec.loader is not None, "router loader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def select_factors(projection, digests, compiler):
    _, factors = projection.factor()
    by_digest = {
        compiler.polynomial_digest(factor): factor
        for factor, exponent in factors
    }
    require(all(digest in by_digest for digest in digests), "projection factors")
    require(
        set(by_digest) == set(digests) | COMMON_OR_OPEN_DIGESTS.intersection(by_digest),
        "unclassified projection factor",
    )
    return [by_digest[digest] for digest in digests]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--factor", action="store_true")
    parser.add_argument("--finite-replay", action="store_true")
    args = parser.parse_args()
    require(flint.__version__ == "0.9.0", "python-flint version")
    router = load_router()
    compiler = router.load_compiler()
    context = flint.nmod_mpoly_ctx.get(
        ("trace", "p", "t", "w"), DEPLOYED_PRIME, "lex"
    )
    residuals = router.load_residuals(compiler, context, "mixed")
    projections = [
        residuals[0].resultant(residuals[right], 3)
        for right in (1, 2, 3)
    ]
    factor_sets = [
        select_factors(projection, digests, compiler)
        for projection, digests in zip(projections, FACTOR_DIGESTS)
    ]
    conic = router.load_conic(compiler, context, "mixed")
    _, conic_factors = conic.factor()
    conic_residuals = [
        factor for factor, exponent in conic_factors
        if len(factor.to_dict()) > 100 and exponent == 1
    ]
    require(len(conic_residuals) == 1, "unique kernel-conic residual")
    conic_residual = conic_residuals[0]
    right = factor_sets[2][0]
    nonempty = 0
    endpoint_candidates = {}
    for left_index, left in enumerate(factor_sets[0]):
        left_right_norm = left.resultant(right, 1)
        require(not left_right_norm.is_zero(), "left/right resultant")
        for middle_index, middle in enumerate(factor_sets[1]):
            left_middle_norm = left.resultant(middle, 1)
            require(not left_middle_norm.is_zero(), "left/middle resultant")
            common_norm = left_right_norm.gcd(left_middle_norm)
            digest = compiler.polynomial_digest(common_norm)
            _, factors = common_norm.factor()
            degrees = tuple(factor.degrees()[2] for factor, _ in factors)
            if common_norm.total_degree() > 0:
                nonempty += 1
            print(
                f"off_common_pair={left_index}{middle_index} "
                f"terms={len(common_norm.to_dict())} "
                f"degrees={common_norm.degrees()} "
                f"factor_degrees={','.join(map(str, degrees)) or '-'} "
                f"digest={digest}",
                flush=True,
            )
            if args.factor:
                compiler.emit_factorization(
                    common_norm,
                    f"off_common_pair={left_index}{middle_index}",
                    context,
                )
            if args.finite_replay:
                for norm_factor, _ in factors:
                    modulus = router.univariate_modulus(norm_factor, 2)
                    field = flint.fq_default_ctx(
                        modulus=modulus, fq_type="FQ_NMOD"
                    )
                    t_value = field.gen()
                    polynomial_context = flint.fq_default_poly_ctx(field)
                    p_gcd = router.evaluate_as_p_polynomial(
                        left, t_value, polynomial_context
                    )
                    for polynomial in (middle, right):
                        p_gcd = p_gcd.gcd(router.evaluate_as_p_polynomial(
                            polynomial, t_value, polynomial_context
                        ))
                    _, p_factors = p_gcd.factor()
                    for p_factor, _ in p_factors:
                        require(p_factor.degree() == 1, "nonlinear p factor")
                        p_value = -p_factor[0] / p_factor[1]
                        key = (
                            tuple(int(value) for value in t_value.to_list()),
                            tuple(int(value) for value in p_value.to_list()),
                        )
                        endpoint_candidates[key] = (field, t_value, p_value)
    if args.finite_replay:
        boundary = 0
        empty = 0
        w_candidates = []
        for index, (_, (field, t_value, p_value)) in enumerate(
                sorted(endpoint_candidates.items())):
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
                status = "BASE_BOUNDARY"
            else:
                polynomial_context = flint.fq_default_poly_ctx(field)
                w_gcd = router.evaluate_ptw_polynomial(
                    residuals[0], p_value, t_value, polynomial_context
                )
                for polynomial in (*residuals[1:], conic_residual):
                    w_gcd = w_gcd.gcd(router.evaluate_ptw_polynomial(
                        polynomial, p_value, t_value, polynomial_context
                    ))
                if w_gcd.degree() == 0:
                    empty += 1
                    status = "MINOR_CONIC_EMPTY"
                else:
                    _, w_factors = w_gcd.factor()
                    require(
                        all(factor.degree() == 1 for factor, _ in w_factors),
                        "nonlinear w factor",
                    )
                    for w_factor, _ in w_factors:
                        w_value = -w_factor[0] / w_factor[1]
                        w_candidates.append((index, t_value, p_value, w_value))
                    status = f"W_CANDIDATES_{len(w_factors)}"
            print(
                f"endpoint_candidate={index} status={status}",
                flush=True,
            )
        require(not w_candidates, f"off-common w candidates: {w_candidates}")
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_MIXED_"
            "OFF_COMMON_FINITE_REPLAY_PASS "
            f"endpoints={len(endpoint_candidates)} boundary={boundary} "
            f"minor_conic_empty={empty}",
            flush=True,
        )
    print(
        "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_MIXED_"
        f"OFF_COMMON_SCREEN_PASS pairs=12 nonconstant_norms={nonempty}",
        flush=True,
    )


if __name__ == "__main__":
    main()
