#!/usr/bin/env python3
"""Route fixed-moving determinant components from pinned caches.

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
COMPILER_SHA256 = "988e60a010ea2793049505b5e9b0ff6d5c28b300e4a00a4b8a3724849ede09f0"
CONFIGS = {
    "same": {
        "cache": HERE / "kb_c2_112_aligned_positive_unramified_fixed_same_minors.json",
        "conic_cache": HERE / "kb_c2_112_aligned_positive_unramified_fixed_same_conic.json",
        "cache_sha256": "f9767957f0946595c9e3618a469cdc69ecde3809b7726e1ef5f9061054a6ad2f",
        "conic_cache_sha256": "0ba5df80a91444b44c5e8e8e2b5124e68ea7cfd891fca8a448730b973b9e4c00",
        "pair_hashes": {
            "01": "c0071e721158855c5eb40fa1ce3dd002cba12173644a4ce3d54aa6444eead989",
        },
        "residual_digests": (
            "3c633aade4b55213e462267e8fb43d2974a9d2a250e81944dba6b913daaf1b84",
            "0cd1323bd11dda676a1a23c807bc920fe71f31f551191a3886b38d5906ce1bc9",
            "0ed1f3e13918f34f06070ce7a7ef8c4d9d167d2c0d8ddf5ea0b157780e4a78d3",
            "1485da9048037830c82b2ef1e08559a04d5eb365174322e509def8c748744af7",
        ),
    },
    "swap": {
        "cache": HERE / "kb_c2_112_aligned_positive_unramified_fixed_swap_minors.json",
        "conic_cache": HERE / "kb_c2_112_aligned_positive_unramified_fixed_swap_conic.json",
        "cache_sha256": "c231e80bb7a0ce77412e63c196261c0c2c561e358dcc719b98db3b5f01f4db30",
        "conic_cache_sha256": "bb53aa14bcfd96b890bb5ba895d2b8bfbfc1e46d4d7ba394a4ad156e3293faba",
        "pair_hashes": {
            "01": "afc54d37e1313b96c4cc7cf52ebfac282ae6a3ca6f3da7b12d66f3073b0f8a05",
        },
        "residual_digests": (
            "3163fdef00392b7b6d511709c585cbe51e9e967a6f683d1a9966320dd1fdd142",
            "81ad740cb98a6de014fed0b080e0f4f93820cfba3bd7e304d996e0b6bfb1a32d",
            "90603b49ca00a24281d4445396688050281ddbda585c78740fdc7c6f87b1682a",
            "f94c87026f6e5d9af79891247a80f65c0e2d6976fb220f7aa6bf0bd9cbaf85cd",
        ),
    },
    "mixed": {
        "cache": HERE / "kb_c2_112_aligned_positive_unramified_fixed_mixed_minors.json",
        "conic_cache": HERE / "kb_c2_112_aligned_positive_unramified_fixed_mixed_conic.json",
        "cache_sha256": "b44414abc54949c3a111e15a012bd6e96e060f1c9a3b81172ab05ffe7d2dcfb2",
        "conic_cache_sha256": "4f091eee7d93b05939cb15303befc75f0b37628112496ac8b5c703f9b2acafd5",
        "pair_hashes": {
            "23": "8510195c58cedb3b1759bf182113be5f820ed5157a5d0c20b11fa63ef2ada08e",
        },
        "component_digest": "de39723065f2a73569050f7290d326610ebfc5f4d9e4f6db969be30d5c414de9",
        "residual_digests": (
            "d1caffe0616ccf3911a87f67a9bb56b25317faba548dd502f1d9795e61a78126",
            "0c87ff003bf234a6aa4d034c45da0d83869f465cb178454f41f3f711905377e8",
            "3a414834a49a9334fd5dcf859fd8ba111f0b0fe081112d149f4d98c33bdf82f5",
            "59b6ff99837c08d51bb05785843e7b82fca64a59e3033231666cfdee65abc0dc",
        ),
    },
}


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


def load_cache(compiler, context, allocation, config):
    cache = config["cache"]
    require(hashlib.sha256(cache.read_bytes()).hexdigest()
            == config["cache_sha256"],
            "cache hash")
    payload = json.loads(cache.read_text(encoding="ascii"))
    require(payload["schema"] ==
            "kb-c2-112-aligned-positive-minor-residuals-v1", "cache schema")
    require(payload["prime"] == DEPLOYED_PRIME, "cache prime")
    require(payload["template"] == "fixed-moving", "cache template")
    require(payload["allocation"] == allocation, "cache allocation")
    residual_digests = config["residual_digests"]
    require(tuple(payload["digests"]) == residual_digests, "cache digests")
    polynomials = []
    for encoded, expected_digest in zip(
            payload["polynomials"], residual_digests):
        polynomial = context.from_dict({
            tuple(monomial): coefficient for monomial, coefficient in encoded
        })
        require(compiler.polynomial_digest(polynomial) == expected_digest,
                "decoded residual digest")
        polynomials.append(polynomial)
    return polynomials


def load_conic_cache(compiler, context, config):
    conic_cache = config["conic_cache"]
    require(
        hashlib.sha256(conic_cache.read_bytes()).hexdigest()
        == config["conic_cache_sha256"],
        "conic cache hash",
    )
    payload = json.loads(conic_cache.read_text(encoding="ascii"))
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


def component_expression(allocation, p, t):
    if allocation == "same":
        return (
            16 * p**4 + 220 * p**3 * t - 20 * p**3
            + 579 * p**2 * t**2 + 684 * p**2 * t - 72 * p**2
            + 503 * p * t**3 + 1218 * p * t**2
            + 684 * p * t - 20 * p
            + 140 * t**4 + 503 * t**3 + 579 * t**2 + 220 * t + 16
        )
    if allocation == "swap":
        return (
            16 * p**3 + 204 * p**2 * t + 804 * p**2
            + 165 * p * t**2 + 948 * p * t + 804 * p
            + 20 * t**3 + 165 * t**2 + 204 * t + 16
        )
    require(allocation == "mixed", "component allocation")
    return None


def flint_component_expression(polynomial, p, t):
    expression = sp.Integer(0)
    for monomial, coefficient in polynomial.to_dict().items():
        require(monomial[0] == 0 and monomial[3] == 0,
                "component variable support")
        expression += int(coefficient) * p**monomial[1] * t**monomial[2]
    return expression


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allocation", choices=tuple(CONFIGS), default="same")
    parser.add_argument("--pair",
                        choices=("01", "02", "03", "12", "13", "23", "all"),
                        default="all")
    parser.add_argument("--dump-gcd", type=Path)
    parser.add_argument("--test-pair-cache", type=Path)
    args = parser.parse_args()
    require(args.dump_gcd is None or args.pair != "all",
            "--dump-gcd requires one pair")
    require(args.test_pair_cache is None or args.dump_gcd is None,
            "pair-cache test and dump are exclusive")
    require(flint.__version__ == "0.9.0", "python-flint version")
    config = CONFIGS[args.allocation]
    compiler = load_compiler()
    b, p, t, w = sp.symbols("b p t w")
    context = flint.nmod_mpoly_ctx.get(
        ("b", "p", "t", "w"), DEPLOYED_PRIME, "lex"
    )
    residuals = load_cache(compiler, context, args.allocation, config)
    component_expression_value = component_expression(args.allocation, p, t)
    if component_expression_value is None:
        first_projection = residuals[0].resultant(residuals[1], 3)
        _, first_factors = first_projection.factor()
        candidates = [
            factor for factor, exponent in first_factors
            if exponent == 1
            and compiler.polynomial_digest(factor)
            == config["component_digest"]
        ]
        require(len(candidates) == 1, "unique configured component")
        component = candidates[0]
        component_expression_value = flint_component_expression(
            component, p, t
        )
    else:
        component = compiler.sympy_to_flint(
            sp.Poly(component_expression_value, b, p, t, w), context
        )
    pairs = ("01", "02", "03") if args.pair == "all" else (args.pair,)
    for pair in pairs:
        left, right = map(int, pair)
        projection = residuals[left].resultant(residuals[right], 3)
        multiplicity = 0
        quotient = projection
        while (quotient % component).is_zero():
            quotient //= component
            multiplicity += 1
        require(multiplicity >= 1, "missing component factor")
        print(f"component_pair={pair} multiplicity={multiplicity}", flush=True)
    print(
        f"component_projection_factor=PASS allocation={args.allocation}",
        flush=True,
    )

    extension = FiniteExtension(
        sp.Poly(
            component_expression_value, p,
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
        pair_payload = json.loads(
            args.test_pair_cache.read_text(encoding="ascii")
        )
        pair_name = pair_payload["pair"]
        require(pair_name in config["pair_hashes"],
                "pair cache hash not configured")
        require(
            hashlib.sha256(args.test_pair_cache.read_bytes()).hexdigest()
            == config["pair_hashes"][pair_name],
            "pair cache hash",
        )
        require(pair_payload.get("allocation", "same") == args.allocation,
                "pair cache allocation")
        pair_gcd = decode_extension_polynomial(
            pair_payload["coefficients"], extension, p, t
        )
        require(len(pair_gcd) == 2 and pair_gcd[1] == extension.one,
                "pair cache monic linear")
        root = -pair_gcd[0]
        norms = []
        denominators = []
        pair_indices = set(map(int, pair_name))
        for index in sorted(set(range(4)) - pair_indices):
            value = evaluate_extension_polynomial(
                extension_residuals[index], root, extension
            )
            if value == extension.zero:
                print(
                    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_COMPONENT_"
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
            norm = component.resultant(numerator_flint, 1)
            require(not norm.is_zero(), "zero extension-value norm")
            norms.append(norm)
            denominators.append(denominator_flint)
            print(
                "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_COMPONENT_"
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
                "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_COMPONENT_"
                "ROOT_NORM_GCD_PASS "
                f"terms={len(common_norm.to_dict())} "
                f"degrees={common_norm.degrees()} "
                f"digest={compiler.polynomial_digest(common_norm)}",
                flush=True,
            )
            compiler.emit_factorization(
                common_norm, "component_root_norm_gcd", context
            )
            common_denominator = denominators[0]
            for denominator in denominators[1:]:
                common_denominator *= denominator
            compiler.emit_factorization(
                common_denominator, "component_root_denominators", context
            )

        conic = load_conic_cache(compiler, context, config)
        _, conic_factors = conic.factor()
        conic_residuals = [
            factor for factor, exponent in conic_factors
            if len(factor.to_dict()) > 100 and exponent == 1
        ]
        require(len(conic_residuals) == 1, "unique kernel-conic residual")
        conic_residual = conic_residuals[0]
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_COMPONENT_"
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
                "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_COMPONENT_"
                "CONIC_TEST_PASS generic_conic_root=true",
                flush=True,
            )
            return
        numerator, denominator = extension_value_numerator(conic_value, p)
        numerator_flint = compiler.sympy_to_flint(
            sp.Poly(numerator, b, p, t, w), context
        )
        norm = component.resultant(numerator_flint, 1)
        require(not norm.is_zero(), "zero kernel-conic norm")
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_COMPONENT_"
            "CONIC_TEST_PASS generic_conic_root=false "
            f"norm_terms={len(norm.to_dict())} "
            f"norm_degrees={norm.degrees()} "
            f"norm_digest={compiler.polynomial_digest(norm)}",
            flush=True,
        )
        compiler.emit_factorization(norm, "component_conic_norm", context)
        denominator_flint = compiler.sympy_to_flint(
            sp.Poly(denominator, b, p, t, w), context
        )
        compiler.emit_factorization(
            denominator_flint, "component_conic_denominator", context
        )
        return
    pair_gcds = []
    for pair in pairs:
        left, right = map(int, pair)
        started = time.monotonic()
        pair_gcd = compiler.extension_gcd(
            extension_residuals[left], extension_residuals[right], extension
        )
        pair_gcds.append(pair_gcd)
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_COMPONENT_PAIR_GCD_PASS "
            f"pair={pair} degree={len(pair_gcd) - 1} "
            f"digest={compiler.extension_polynomial_digest(pair_gcd)} "
            f"elapsed={time.monotonic() - started:.3f}",
            flush=True,
        )
        if args.dump_gcd:
            payload = {
                "schema": "kb-c2-112-aligned-positive-quartic-pair-gcd-v1",
                "prime": DEPLOYED_PRIME,
                "cache_sha256": config["cache_sha256"],
                "allocation": args.allocation,
                "pair": pair,
                "degree": len(pair_gcd) - 1,
                "digest": compiler.extension_polynomial_digest(pair_gcd),
                "coefficients": encode_extension_polynomial(pair_gcd),
            }
            encoded = json.dumps(
                payload, sort_keys=True, separators=(",", ":")
            ) + "\n"
            args.dump_gcd.write_text(encoded, encoding="ascii")
            print(
                f"component_pair_cache={args.dump_gcd} "
                f"sha256={hashlib.sha256(encoded.encode('ascii')).hexdigest()}",
                flush=True,
            )
    if args.pair != "all":
        return
    common = pair_gcds[0]
    for pair_gcd in pair_gcds[1:]:
        common = compiler.extension_gcd(common, pair_gcd, extension)
    print(
        "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_COMPONENT_GENERIC_GCD_PASS "
        f"degree={len(common) - 1} "
        f"digest={compiler.extension_polynomial_digest(common)}",
        flush=True,
    )


if __name__ == "__main__":
    main()
