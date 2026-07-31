#!/usr/bin/env python3
"""Independently replay the exact moving-mixed q-slice survivors.

This verifier deliberately does not import the component router that found
the witnesses.  It rebuilds the four trace equations from the pinned source
compiler and evaluates the printed coordinates in their exact finite fields.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import flint


DEPLOYED_PRIME = 2130706433
DEPLOYED_EXTENSION_DEGREE = 6
HERE = Path(__file__).resolve().parent
COMPILER = HERE / "kb_c2_112_aligned_positive_unramified_flint.py"
COMPILER_SHA256 = "988e60a010ea2793049505b5e9b0ff6d5c28b300e4a00a4b8a3724849ede09f0"
MINOR_CACHE = (
    HERE / "kb_c2_112_aligned_positive_unramified_moving_mixed_minors.json"
)
MINOR_CACHE_SHA256 = (
    "799e8feb8f89fee7bf7dab30c3e1e4522380bb490f350a5c93f48f6ff19d3565"
)
CONIC_CACHE = (
    HERE / "kb_c2_112_aligned_positive_unramified_moving_mixed_conic.json"
)
CONIC_CACHE_SHA256 = (
    "639a9eeacf175fbfa2e427ca8ad6c3dae1110f658bf4edbe7e3136f2c1748880"
)
SURVIVORS = (
    HERE / "kb_c2_112_aligned_positive_unramified_moving_mixed_survivors.json"
)
SURVIVORS_SHA256 = (
    "c02e649960b35e3d264472c3c1aa69cfd71d48930df8844c281b901b3e5a5f36"
)
DIRECT_NORM_DIGEST = (
    "13a295c5219450a00c588cc9661863022d03ddca67429eb9626d398fe4515dae"
)
EXPECTED_FACTORS = (3, 5, 10, 12)
EXPECTED_DEGREES = (3, 3, 7, 7)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_compiler():
    require(file_sha256(COMPILER) == COMPILER_SHA256, "compiler hash")
    spec = importlib.util.spec_from_file_location("unramified_flint", COMPILER)
    require(spec is not None and spec.loader is not None, "compiler loader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def evaluate(polynomial, trace, p, t, w, field):
    value = field.zero()
    points = (trace, p, t, w)
    for monomial, coefficient in polynomial.to_dict().items():
        term = field(int(coefficient))
        for point, exponent in zip(points, monomial):
            term *= point**exponent
        value += term
    return value


def decode(record):
    polynomial_context = flint.fmpz_mod_poly_ctx(DEPLOYED_PRIME)
    modulus = polynomial_context(record["modulus"])
    require(modulus.is_monic(), "nonmonic survivor modulus")
    require(modulus.is_irreducible(), "reducible survivor modulus")
    field = flint.fq_default_ctx(modulus=modulus, fq_type="FQ_NMOD")
    values = tuple(field(record[name]) for name in ("trace", "p", "t", "w"))
    require(values[2] == field.gen(), "printed t is not the field generator")
    return modulus, field, values


def main() -> None:
    require(flint.__version__ == "0.9.0", "python-flint version")
    require(file_sha256(MINOR_CACHE) == MINOR_CACHE_SHA256, "minor cache hash")
    require(file_sha256(CONIC_CACHE) == CONIC_CACHE_SHA256, "conic cache hash")
    require(file_sha256(SURVIVORS) == SURVIVORS_SHA256, "survivor hash")

    payload = json.loads(SURVIVORS.read_text(encoding="ascii"))
    require(
        payload["schema"]
        == "kb-c2-112-aligned-positive-moving-survivors-v1",
        "survivor schema",
    )
    require(payload["prime"] == DEPLOYED_PRIME, "survivor prime")
    require(payload["allocation"] == "mixed", "survivor allocation")
    require(payload["cache_sha256"] == MINOR_CACHE_SHA256, "payload cache hash")
    require(
        payload["conic_cache_sha256"] == CONIC_CACHE_SHA256,
        "payload conic cache hash",
    )
    require(
        payload["direct_norm_digest"] == DIRECT_NORM_DIGEST,
        "direct norm digest",
    )
    require(
        tuple(item["factor_index"] for item in payload["survivors"])
        == EXPECTED_FACTORS,
        "survivor factor indices",
    )

    compiler = load_compiler()
    variables, equations = compiler.build_cell("moving-moving", "mixed")
    require(tuple(map(str, variables)) == ("trace", "p", "t", "w"), "variables")
    context = flint.nmod_mpoly_ctx.get(
        ("trace", "p", "t", "w"), DEPLOYED_PRIME, "lex"
    )
    flint_equations = [compiler.sympy_to_flint(item, context) for item in equations]

    deployed = []
    algebraic_closure_only = []
    for record, expected_degree in zip(payload["survivors"], EXPECTED_DEGREES):
        modulus, field, (trace, p, t, w) = decode(record)
        require(modulus.degree() == expected_degree, "survivor field degree")
        require(
            all(evaluate(equation, trace, p, t, w, field) == field.zero()
                for equation in flint_equations),
            "trace equation replay",
        )

        base_forbidden = (
            p * (p - 1) * (p - t + 1) * (p + t + 1)
            * (p + 2 * t + 4) * (4 * p + 2 * t + 1)
            * (5 * p + 4 * t + 5) * (t**2 - 4 * p)
        )
        scale_denominator = p * w - 4 * p + 2 * t * w - 2 * t + 4 * w - 1
        endpoint_orbit_collision = (
            p * (trace**2 - 2) + t * (1 + p) * trace
            + 1 + t**2 + p**2
        )
        trace_forbidden = (
            (trace - 2) * (trace + 2) * (2 * trace - 5)
            * endpoint_orbit_collision
        )
        require(base_forbidden != field.zero(), "base forbidden factor")
        require(
            w * (w - 1) * (w + 1) * scale_denominator != field.zero(),
            "w or scale forbidden factor",
        )
        require(trace_forbidden != field.zero(), "trace forbidden factor")
        require(field(record["base_forbidden"]) == base_forbidden,
                "printed base forbidden value")
        require(field(record["scale_denominator"]) == scale_denominator,
                "printed scale denominator")
        require(field(record["trace_forbidden"]) == trace_forbidden,
                "printed trace forbidden value")

        factor_index = record["factor_index"]
        if DEPLOYED_EXTENSION_DEGREE % modulus.degree() == 0:
            deployed.append(factor_index)
        else:
            algebraic_closure_only.append(factor_index)
        print(
            "mixed_survivor="
            f"{factor_index} degree={modulus.degree()} equations=PASS "
            "open_set=PASS "
            f"embeds_in_f_p6={str(DEPLOYED_EXTENSION_DEGREE % modulus.degree() == 0).lower()}",
            flush=True,
        )

    require(tuple(deployed) == (3, 5), "deployed-field survivor indices")
    require(
        tuple(algebraic_closure_only) == (10, 12),
        "algebraic-closure-only survivor indices",
    )
    print(
        "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_MIXED_"
        "SURVIVOR_VERIFY_PASS total=4 deployed_field=2 "
        "algebraic_closure_only=2",
        flush=True,
    )


if __name__ == "__main__":
    main()
