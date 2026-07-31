#!/usr/bin/env python3
"""Route the fixed-moving/same determinant quartic from a pinned cache.

Proof status: EXPERIMENTAL component router.  The cache is independently
reconstructed by kb_c2_112_aligned_positive_unramified_flint.py.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import time
from pathlib import Path

import flint
import sympy as sp
from sympy.polys.agca.extensions import FiniteExtension


DEPLOYED_PRIME = 2130706433
HERE = Path(__file__).resolve().parent
COMPILER = HERE / "kb_c2_112_aligned_positive_unramified_flint.py"
CACHE = HERE / "kb_c2_112_aligned_positive_unramified_fixed_same_minors.json"
CONIC_CACHE = HERE / "kb_c2_112_aligned_positive_unramified_fixed_same_conic.json"
COMPILER_SHA256 = "6bea33f870adeedd0b6d3e107b4c444704053fae0612d9927300d25ebf3271ed"
CACHE_SHA256 = "f9767957f0946595c9e3618a469cdc69ecde3809b7726e1ef5f9061054a6ad2f"
CONIC_CACHE_SHA256 = "0ba5df80a91444b44c5e8e8e2b5124e68ea7cfd891fca8a448730b973b9e4c00"
PAIR01_SHA256 = "c0071e721158855c5eb40fa1ce3dd002cba12173644a4ce3d54aa6444eead989"
RESIDUAL_DIGESTS = (
    "3c633aade4b55213e462267e8fb43d2974a9d2a250e81944dba6b913daaf1b84",
    "0cd1323bd11dda676a1a23c807bc920fe71f31f551191a3886b38d5906ce1bc9",
    "0ed1f3e13918f34f06070ce7a7ef8c4d9d167d2c0d8ddf5ea0b157780e4a78d3",
    "1485da9048037830c82b2ef1e08559a04d5eb365174322e509def8c748744af7",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def load_compiler():
    require(hashlib.sha256(COMPILER.read_bytes()).hexdigest() == COMPILER_SHA256,
            "compiler hash")
    spec = importlib.util.spec_from_file_location("unramified_flint", COMPILER)
    require(spec is not None and spec.loader is not None, "compiler loader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_cache(compiler, context):
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache hash")
    payload = json.loads(CACHE.read_text(encoding="ascii"))
    require(payload["schema"] ==
            "kb-c2-112-aligned-positive-minor-residuals-v1", "cache schema")
    require(payload["prime"] == DEPLOYED_PRIME, "cache prime")
    require(payload["template"] == "fixed-moving", "cache template")
    require(payload["allocation"] == "same", "cache allocation")
    require(tuple(payload["digests"]) == RESIDUAL_DIGESTS, "cache digests")
    polynomials = []
    for encoded, expected_digest in zip(
            payload["polynomials"], RESIDUAL_DIGESTS):
        polynomial = context.from_dict({
            tuple(monomial): coefficient for monomial, coefficient in encoded
        })
        require(compiler.polynomial_digest(polynomial) == expected_digest,
                "decoded residual digest")
        polynomials.append(polynomial)
    return polynomials


def load_conic_cache(compiler, context):
    require(
        hashlib.sha256(CONIC_CACHE.read_bytes()).hexdigest()
        == CONIC_CACHE_SHA256,
        "conic cache hash",
    )
    payload = json.loads(CONIC_CACHE.read_text(encoding="ascii"))
    require(payload["schema"] ==
            "kb-c2-112-aligned-positive-kernel-conic-v1", "conic schema")
    polynomial = context.from_dict({
        tuple(monomial): coefficient
        for monomial, coefficient in payload["polynomial"]
    })
    require(compiler.polynomial_digest(polynomial) == payload["digest"],
            "conic decoded digest")
    return polynomial


def encode_ring_polynomial(polynomial):
    return [
        [[int(exponent) for exponent in monomial], int(coefficient)]
        for monomial, coefficient in sorted(polynomial.to_dict().items())
    ]


def encode_extension_polynomial(coefficients):
    encoded = []
    for coefficient in coefficients:
        p_coefficients = []
        for fraction in reversed(coefficient.rep.to_list()):
            p_coefficients.append({
                "numerator": encode_ring_polynomial(fraction.numer),
                "denominator": encode_ring_polynomial(fraction.denom),
            })
        encoded.append(p_coefficients)
    return encoded


def decode_ring_polynomial(encoded, variable):
    return sum(
        coefficient * variable**monomial[0]
        for monomial, coefficient in encoded
    )


def decode_extension_polynomial(encoded, extension, p, t):
    coefficients = []
    for encoded_coefficient in encoded:
        expression = sp.Integer(0)
        for p_exponent, fraction in enumerate(encoded_coefficient):
            numerator = decode_ring_polynomial(fraction["numerator"], t)
            denominator = decode_ring_polynomial(fraction["denominator"], t)
            expression += numerator * p**p_exponent / denominator
        coefficients.append(extension(expression))
    return coefficients


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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pair", choices=("01", "02", "03", "all"),
                        default="all")
    parser.add_argument("--dump-gcd", type=Path)
    parser.add_argument("--test-pair-cache", type=Path)
    args = parser.parse_args()
    require(args.dump_gcd is None or args.pair != "all",
            "--dump-gcd requires one pair")
    require(args.test_pair_cache is None or args.dump_gcd is None,
            "pair-cache test and dump are exclusive")
    require(flint.__version__ == "0.9.0", "python-flint version")
    compiler = load_compiler()
    b, p, t, w = sp.symbols("b p t w")
    context = flint.nmod_mpoly_ctx.get(
        ("b", "p", "t", "w"), DEPLOYED_PRIME, "lex"
    )
    residuals = load_cache(compiler, context)
    quartic_expression = (
        16 * p**4 + 220 * p**3 * t - 20 * p**3
        + 579 * p**2 * t**2 + 684 * p**2 * t - 72 * p**2
        + 503 * p * t**3 + 1218 * p * t**2 + 684 * p * t - 20 * p
        + 140 * t**4 + 503 * t**3 + 579 * t**2 + 220 * t + 16
    )
    quartic = compiler.sympy_to_flint(
        sp.Poly(quartic_expression, b, p, t, w), context
    )
    indices = (1, 2, 3) if args.pair == "all" else (int(args.pair[1]),)
    for index in indices:
        projection = residuals[0].resultant(residuals[index], 3)
        quotient, remainder = divmod(projection, quartic)
        require(remainder.is_zero(), "missing quartic factor")
        require(not (quotient % quartic).is_zero(), "quartic multiplicity")
    print("quartic_projection_factor=PASS", flush=True)

    extension = FiniteExtension(
        sp.Poly(
            quartic_expression, p,
            domain=sp.GF(DEPLOYED_PRIME).frac_field(t),
        ).monic()
    )
    extension_residuals = [
        compiler.flint_to_extension_w_coefficients(
            polynomial, p, t, extension
        )
        for polynomial in residuals
    ]
    if args.test_pair_cache:
        require(
            hashlib.sha256(args.test_pair_cache.read_bytes()).hexdigest()
            == PAIR01_SHA256,
            "pair cache hash",
        )
        pair_payload = json.loads(
            args.test_pair_cache.read_text(encoding="ascii")
        )
        require(pair_payload["pair"] == "01", "pair cache identity")
        pair_gcd = decode_extension_polynomial(
            pair_payload["coefficients"], extension, p, t
        )
        require(len(pair_gcd) == 2 and pair_gcd[1] == extension.one,
                "pair cache monic linear")
        root = -pair_gcd[0]
        norms = []
        denominators = []
        for index in (2, 3):
            value = evaluate_extension_polynomial(
                extension_residuals[index], root, extension
            )
            if value == extension.zero:
                print(
                    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_QUARTIC_"
                    "ROOT_TEST_PASS "
                    f"residual={index} generic_common_root=true",
                    flush=True,
                )
                continue
            numerator, denominator = extension_value_numerator(value, p)
            numerator_flint = compiler.sympy_to_flint(
                sp.Poly(numerator, b, p, t, w), context
            )
            denominator_flint = compiler.sympy_to_flint(
                sp.Poly(denominator, b, p, t, w), context
            )
            norm = quartic.resultant(numerator_flint, 1)
            require(not norm.is_zero(), "zero extension-value norm")
            norms.append(norm)
            denominators.append(denominator_flint)
            print(
                "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_QUARTIC_"
                "ROOT_TEST_PASS "
                f"residual={index} norm_terms={len(norm.to_dict())} "
                f"norm_degrees={norm.degrees()} "
                f"norm_digest={compiler.polynomial_digest(norm)} "
                f"denominator_digest="
                f"{compiler.polynomial_digest(denominator_flint)}",
                flush=True,
            )
        if norms:
            common_norm = norms[0]
            for norm in norms[1:]:
                common_norm = common_norm.gcd(norm)
            print(
                "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_QUARTIC_"
                "ROOT_NORM_GCD_PASS "
                f"terms={len(common_norm.to_dict())} "
                f"degrees={common_norm.degrees()} "
                f"digest={compiler.polynomial_digest(common_norm)}",
                flush=True,
            )
            compiler.emit_factorization(
                common_norm, "quartic_root_norm_gcd", context
            )
            common_denominator = denominators[0]
            for denominator in denominators[1:]:
                common_denominator *= denominator
            compiler.emit_factorization(
                common_denominator, "quartic_root_denominators", context
            )

        conic = load_conic_cache(compiler, context)
        _, conic_factors = conic.factor()
        conic_residuals = [
            factor for factor, exponent in conic_factors
            if len(factor.to_dict()) > 100 and exponent == 1
        ]
        require(len(conic_residuals) == 1, "unique kernel-conic residual")
        conic_residual = conic_residuals[0]
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_QUARTIC_"
            "CONIC_FACTOR_PASS "
            f"terms={len(conic_residual.to_dict())} "
            f"degrees={conic_residual.degrees()} "
            f"digest={compiler.polynomial_digest(conic_residual)}",
            flush=True,
        )
        conic_extension = compiler.flint_to_extension_w_coefficients(
            conic_residual, p, t, extension
        )
        conic_value = evaluate_extension_polynomial(
            conic_extension, root, extension
        )
        if conic_value == extension.zero:
            print(
                "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_QUARTIC_"
                "CONIC_TEST_PASS generic_conic_root=true",
                flush=True,
            )
            return
        numerator, denominator = extension_value_numerator(conic_value, p)
        numerator_flint = compiler.sympy_to_flint(
            sp.Poly(numerator, b, p, t, w), context
        )
        norm = quartic.resultant(numerator_flint, 1)
        require(not norm.is_zero(), "zero kernel-conic norm")
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_QUARTIC_"
            "CONIC_TEST_PASS generic_conic_root=false "
            f"norm_terms={len(norm.to_dict())} "
            f"norm_degrees={norm.degrees()} "
            f"norm_digest={compiler.polynomial_digest(norm)}",
            flush=True,
        )
        compiler.emit_factorization(norm, "quartic_conic_norm", context)
        denominator_flint = compiler.sympy_to_flint(
            sp.Poly(denominator, b, p, t, w), context
        )
        compiler.emit_factorization(
            denominator_flint, "quartic_conic_denominator", context
        )
        return
    pair_gcds = []
    for index in indices:
        started = time.monotonic()
        pair_gcd = compiler.extension_gcd(
            extension_residuals[0], extension_residuals[index], extension
        )
        pair_gcds.append(pair_gcd)
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_QUARTIC_PAIR_GCD_PASS "
            f"pair=0{index} degree={len(pair_gcd) - 1} "
            f"digest={compiler.extension_polynomial_digest(pair_gcd)} "
            f"elapsed={time.monotonic() - started:.3f}",
            flush=True,
        )
        if args.dump_gcd:
            payload = {
                "schema": "kb-c2-112-aligned-positive-quartic-pair-gcd-v1",
                "prime": DEPLOYED_PRIME,
                "cache_sha256": CACHE_SHA256,
                "pair": f"0{index}",
                "degree": len(pair_gcd) - 1,
                "digest": compiler.extension_polynomial_digest(pair_gcd),
                "coefficients": encode_extension_polynomial(pair_gcd),
            }
            encoded = json.dumps(
                payload, sort_keys=True, separators=(",", ":")
            ) + "\n"
            args.dump_gcd.write_text(encoded, encoding="ascii")
            print(
                f"quartic_pair_cache={args.dump_gcd} "
                f"sha256={hashlib.sha256(encoded.encode('ascii')).hexdigest()}",
                flush=True,
            )
    if args.pair != "all":
        return
    common = pair_gcds[0]
    for pair_gcd in pair_gcds[1:]:
        common = compiler.extension_gcd(common, pair_gcd, extension)
    print(
        "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_QUARTIC_GENERIC_GCD_PASS "
        f"degree={len(common) - 1} "
        f"digest={compiler.extension_polynomial_digest(common)}",
        flush=True,
    )


if __name__ == "__main__":
    main()
