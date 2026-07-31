#!/usr/bin/env python3
"""Route off-common projection support in fixed-moving cells."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
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
SAME_FACTOR_DIGESTS = (
    (
        "8c19a2dad39ed04e922c228dc27f04b1b38eeabf322318808ed58ec64203fd11",
        "05f4944632d0476e98503db02c330908b655aa06de83ffbdd2b7de469b26a091",
    ),
    ("fa454e06ad0f8e2573abf334570ad180a0fb446c0cfdc389e582cba6246a97ec",),
    ("9adb4280d9cad8c53a64a751820b394e21de5e9a632ad47ce78e96961d2edbd8",),
)
SAME_COMMON_OR_OPEN_DIGESTS = {
    "d54e40904960bcd20c2da066128d71124ade633fe8e4ab65360cba361dbb7fcd",
    "ce7c2e06c6d7e3e6bfe2ea4722eb2795300c229d50ca5712870f20b8cc736da8",
    "544274fb97120d080da62a45b251927b63f70bd19285d3b60ad8c17f8f861d35",
    "74192520e1f5f028cb2ff733e206f8084a5aa920ed5985ff94f44e8c33f02718",
    "108ffdd9fa92bdeaba39a5fb2560e9155ed60e7e040f89be4d94ec3a3dc5348e",
    "8cec5db42e9f38668aa4f9afe928bb9adf9610c3b59f1789f26f7759802ba26e",
    "e33a2320f3a6377c5e39cc0a8aa7b5dc151ef561324c66d2decf32b46935a909",
    "f87faf4fa44b76fd9d8854ff630cfda98653a46e6d5fa69da86a7600c0e9e6ba",
}
SWAP_FACTOR_DIGESTS = (
    (
        "078c1dc07f88af11758d4dd78d6e9f06c393f97255719b8800bfc9a10fd0b32b",
        "ade45d1739e1b5181393246dbb5abb9865229b3dcb8e51c78422c4ad60d85aef",
    ),
    ("12bcb389853295f9a1a5db28626ed1078c24b331588d12dc6f895ae404e69cc8",),
    ("1d336ad19fd079bce56500b6c78b5d7b91ebe0a7a902e6dceb3c212b22979780",),
)
SWAP_COMMON_OR_OPEN_DIGESTS = SAME_COMMON_OR_OPEN_DIGESTS | {
    "ec6358a79eddf8196b83a23ef63dbc172af0d11544c2e5bfa90e220c30ac346e",
}
OFF_COMMON_CONFIGS = {
    "same": (SAME_FACTOR_DIGESTS, SAME_COMMON_OR_OPEN_DIGESTS),
    "swap": (SWAP_FACTOR_DIGESTS, SWAP_COMMON_OR_OPEN_DIGESTS),
}
MIXED_FACTOR_DIGESTS = (
    (
        "27dc2c568e0ef0ca4fc4b03d4d117cfd636cc7ed48f7c52053556f13c9ca3632",
        "ff63832304d9161ac8508901af890abf8bc2b7259e34cb941a4727ca7e1388c1",
        "0fd5b3c3ae63816fc90416a9d403b03abca94a138aaa547fc972b36e2dc3c6ce",
        "60be59c7b280160d57e3df7cb5b1ec6bd6bd40f2ca1f73ccbc0b4cfeeccf3626",
        "22e9eb93d67950eb03bbd5e60061598618dad415462c07e3738d7cef260ecc23",
    ),
    (
        "b02512c083274778475e6ccaeb49a80f2e7d85f940cf5aa7e61b63e01e57fbe7",
        "332174450bb8b701dea1bfeeb7de3291e8b9a97251d7807aa23f295ec6a9a730",
        "8f8e77a6ed34abccd39ec13efdfffd4e34afef8bc07900630a743ffc0468873b",
        "106bae7e5d7ca5e88c4c39b7477e807ddcff8b0ac4eaffc1f990364c2168d132",
    ),
    ("700d00d959e88a9639cc878b78de4261502dd5dd4c9f02de1754916a7cd77348",),
)
MIXED_COMMON_OR_OPEN_DIGESTS = {
    "fb4eb943d5c1108596e2199a57fecaff32c3c94bb13305773054123f1b74d0a5",
    "3f902abdd53c17c8139ff2b0606f8e79ec9c5686b9c673fa145f83cb673f6d52",
    "de39723065f2a73569050f7290d326610ebfc5f4d9e4f6db969be30d5c414de9",
    "544274fb97120d080da62a45b251927b63f70bd19285d3b60ad8c17f8f861d35",
    "74192520e1f5f028cb2ff733e206f8084a5aa920ed5985ff94f44e8c33f02718",
    "108ffdd9fa92bdeaba39a5fb2560e9155ed60e7e040f89be4d94ec3a3dc5348e",
    "e33a2320f3a6377c5e39cc0a8aa7b5dc151ef561324c66d2decf32b46935a909",
    "8cec5db42e9f38668aa4f9afe928bb9adf9610c3b59f1789f26f7759802ba26e",
    "d54e40904960bcd20c2da066128d71124ade633fe8e4ab65360cba361dbb7fcd",
    "f87faf4fa44b76fd9d8854ff630cfda98653a46e6d5fa69da86a7600c0e9e6ba",
}
OFF_COMMON_CONFIGS["mixed"] = (
    MIXED_FACTOR_DIGESTS,
    MIXED_COMMON_OR_OPEN_DIGESTS,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def load_router():
    spec = importlib.util.spec_from_file_location("quartic_router", QUARTIC_ROUTER)
    require(spec is not None and spec.loader is not None, "router loader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_moving_router():
    spec = importlib.util.spec_from_file_location("moving_router", MOVING_ROUTER)
    require(spec is not None and spec.loader is not None, "moving router loader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def select_factors(projection, digests, common_or_open, compiler):
    _, factors = projection.factor()
    by_digest = {
        compiler.polynomial_digest(factor): factor for factor, _ in factors
    }
    require(all(digest in by_digest for digest in digests), "residual factors")
    require(
        set(by_digest) == set(digests) | common_or_open.intersection(by_digest),
        "unclassified projection factor",
    )
    return [by_digest[digest] for digest in digests]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allocation", choices=("same", "swap", "mixed"), default="same")
    parser.add_argument("--factor", action="store_true")
    parser.add_argument("--finite-replay", action="store_true")
    args = parser.parse_args()
    require(flint.__version__ == "0.9.0", "python-flint version")
    router = load_router()
    compiler = router.load_compiler()
    context = flint.nmod_mpoly_ctx.get(
        ("b", "p", "t", "w"), DEPLOYED_PRIME, "lex"
    )
    config = router.CONFIGS[args.allocation]
    residuals = router.load_cache(compiler, context, args.allocation, config)
    projections = []
    for pair, right in zip(("01", "02", "03"), (1, 2, 3)):
        projection = residuals[0].resultant(residuals[right], 3)
        require(not projection.is_zero(), "zero projection")
        projections.append(projection)
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_"
            f"PROJECTION_PASS allocation={args.allocation} pair={pair} "
            f"terms={len(projection.to_dict())} degrees={projection.degrees()} "
            f"digest={compiler.polynomial_digest(projection)}",
            flush=True,
        )
        if args.factor:
            compiler.emit_factorization(projection, f"projection={pair}", context)
    common = projections[0]
    for projection in projections[1:]:
        common = common.gcd(projection)
    print(
        "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_"
        f"PROJECTION_GCD_PASS allocation={args.allocation} "
        f"terms={len(common.to_dict())} degrees={common.degrees()} "
        f"digest={compiler.polynomial_digest(common)}",
        flush=True,
    )
    if args.factor:
        compiler.emit_factorization(common, "projection_gcd", context)
    if args.allocation not in OFF_COMMON_CONFIGS:
        require(not args.finite_replay, "finite replay not configured")
        return

    factor_digests, common_or_open_digests = OFF_COMMON_CONFIGS[args.allocation]
    factor_sets = [
        select_factors(
            projection,
            digests,
            common_or_open_digests,
            compiler,
        )
        for projection, digests in zip(projections, factor_digests)
    ]
    endpoint_candidates = {}
    for branch_index, (left, middle, right) in enumerate(
            itertools.product(*factor_sets)):
        left_middle_norm = left.resultant(middle, 1)
        left_right_norm = left.resultant(right, 1)
        require(
            not left_middle_norm.is_zero() and not left_right_norm.is_zero(),
            "zero off-common resultant",
        )
        common_norm = left_middle_norm.gcd(left_right_norm)
        _, norm_factors = common_norm.factor()
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_"
            f"OFF_COMMON_SCREEN_PASS allocation={args.allocation} "
            f"branch={branch_index} "
            f"terms={len(common_norm.to_dict())} degrees={common_norm.degrees()} "
            f"factor_degrees="
            f"{','.join(str(item.degrees()[2]) for item, _ in norm_factors) or '-'} "
            f"digest={compiler.polynomial_digest(common_norm)}",
            flush=True,
        )
        if not args.finite_replay:
            continue
        moving_router = load_moving_router()
        for norm_factor, _ in norm_factors:
            modulus = moving_router.univariate_modulus(norm_factor, 2)
            t_degree = modulus.degree()
            if 6 % t_degree:
                continue
            field = flint.fq_default_ctx(modulus=modulus, fq_type="FQ_NMOD")
            t_value = field.gen()
            polynomial_context = flint.fq_default_poly_ctx(field)
            p_gcd = moving_router.evaluate_as_p_polynomial(
                left, t_value, polynomial_context
            )
            for polynomial in (middle, right):
                p_gcd = p_gcd.gcd(moving_router.evaluate_as_p_polynomial(
                    polynomial, t_value, polynomial_context
                ))
            _, p_factors = p_gcd.factor()
            for p_factor, _ in p_factors:
                p_degree = p_factor.degree()
                if (6 // t_degree) % p_degree:
                    continue
                require(p_degree == 1, "unrouted deployed p extension")
                p_value = -p_factor[0] / p_factor[1]
                key = (
                    tuple(int(value) for value in modulus),
                    tuple(int(value) for value in t_value.to_list()),
                    tuple(int(value) for value in p_value.to_list()),
                )
                endpoint_candidates[key] = (field, t_value, p_value, t_degree)
    if not args.finite_replay:
        return

    moving_router = load_moving_router()
    conic = router.load_conic_cache(compiler, context, config)
    boundary = 0
    empty = 0
    w_candidates = []
    for index, (_, (field, t_value, p_value, t_degree)) in enumerate(
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
            w_gcd = moving_router.evaluate_ptw_polynomial(
                residuals[0], p_value, t_value, polynomial_context
            )
            for polynomial in (*residuals[1:], conic):
                w_gcd = w_gcd.gcd(moving_router.evaluate_ptw_polynomial(
                    polynomial, p_value, t_value, polynomial_context
                ))
            if w_gcd.degree() == 0:
                empty += 1
                status = "MINOR_CONIC_EMPTY"
            else:
                _, w_factors = w_gcd.factor()
                for w_factor, _ in w_factors:
                    w_degree = w_factor.degree()
                    if (6 // t_degree) % w_degree:
                        continue
                    require(w_degree == 1, "unrouted deployed w extension")
                    w_candidates.append((index, t_value, p_value, w_factor))
                status = f"W_CANDIDATES_{len(w_factors)}"
        print(f"endpoint_candidate={index} status={status}", flush=True)
    print(
        "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_"
        f"OFF_COMMON_FINITE_REPLAY_PASS allocation={args.allocation} "
        f"endpoints={len(endpoint_candidates)} boundary={boundary} "
        f"minor_conic_empty={empty} w_candidates={len(w_candidates)}",
        flush=True,
    )
    require(
        not w_candidates,
        f"fixed-{args.allocation} off-common w candidates: {w_candidates}",
    )


if __name__ == "__main__":
    main()
