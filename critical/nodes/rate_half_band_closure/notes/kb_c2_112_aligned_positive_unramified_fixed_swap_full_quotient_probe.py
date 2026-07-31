#!/usr/bin/env python3
"""Test the fixed-swap q-slice survivor against both full quotient norms."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import flint


DEPLOYED_PRIME = 2130706433
HERE = Path(__file__).resolve().parent
BASE = (
    HERE / "kb_c2_112_aligned_positive_unramified_fixed_same_full_quotient_probe.py"
)
BASE_SHA256 = "bd1a945e6b09578278d3bfee6b9d7307c2abd365941a8ce143bb4ae390fc40e0"
SURVIVORS = (
    HERE / "kb_c2_112_aligned_positive_unramified_fixed_swap_survivors.json"
)
SURVIVORS_SHA256 = "30519893654add8a06c5bc56413363eb48aeed9b457ca0eb1797a2119f40843f"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def load_module(path: Path, digest: str, name: str):
    require(hashlib.sha256(path.read_bytes()).hexdigest() == digest, f"{name} hash")
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"{name} loader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_record(base, source, helpers, record):
    modulus = flint.fmpz_mod_poly_ctx(DEPLOYED_PRIME)(record["modulus"])
    require(modulus.degree() == 2, "fixed-swap survivor field degree")
    field = flint.fq_default_ctx(modulus=modulus, fq_type="FQ_NMOD")
    t_value = field(record["t"])
    p_value = field(record["p"])
    w_value = field(record["w"])
    b_value = field(record["b"])
    algebra = base.ScalarAlgebra(field, b_value)
    p, t, w = p_value, t_value, w_value
    one = algebra.one
    inverse_two = field(2) ** -1
    p_inverse = p ** -1
    w_inverse = w ** -1
    g_coefficients = base.build_g(
        source, helpers, p, t, b_value, w, algebra
    )

    fixed = (-field(5) * inverse_two, one)
    moving = (-b_value - b_value**-1, one)
    crossing = (t, p)
    resultant_j = [one]
    for a, c in (fixed, moving, crossing):
        resultant_j = helpers.poly_mul(
            resultant_j,
            helpers.quadratic_resultant(g_coefficients, a, c, algebra),
            algebra,
        )

    alpha = p + 2 * t + 4
    beta = 1 + 2 * t + 4 * p
    z = (w * beta - alpha) / (beta - w * alpha)
    z_inverse = z ** -1
    forced = (-w - w_inverse, one)
    internal = (-z - z_inverse, one)
    reciprocal_crossing = (t * p_inverse, p_inverse)
    resultant_i = [one]
    for a, c in (forced, internal, reciprocal_crossing):
        resultant_i = helpers.poly_mul(
            resultant_i,
            helpers.quadratic_resultant(g_coefficients, a, c, algebra),
            algebra,
        )

    q = helpers.quadratic(t, p, algebra)
    reciprocal_crossing_poly = helpers.quadratic(
        reciprocal_crossing[0], reciprocal_crossing[1], algebra
    )
    q_slice = helpers.quadratic_resultant(g_coefficients, t, p, algebra)
    q_slice_target = helpers.poly_mul(
        helpers.poly_pow(helpers.linear(w, algebra), 4, algebra),
        helpers.poly_pow(reciprocal_crossing_poly, 2, algebra),
        algebra,
    )
    helpers.require_associate(q_slice, q_slice_target, algebra, "q-slice control")

    fixed_poly = helpers.quadratic(fixed[0], fixed[1], algebra)
    moving_poly = helpers.quadratic(moving[0], moving[1], algebra)
    internal_poly = helpers.poly_mul(
        helpers.linear(z, algebra), helpers.linear(z_inverse, algebra), algebra
    )
    k5 = helpers.poly_mul(
        helpers.linear(w, algebra),
        helpers.poly_mul(internal_poly, reciprocal_crossing_poly, algebra),
        algebra,
    )
    p_j = helpers.poly_mul(
        q, helpers.poly_mul(fixed_poly, moving_poly, algebra), algebra
    )
    r7 = helpers.poly_mul(p_j, helpers.linear(w_inverse, algebra), algebra)
    first_target = helpers.poly_mul(
        helpers.poly_pow(k5, 4, algebra), helpers.poly_pow(q, 2, algebra), algebra
    )
    second_left = helpers.poly_mul(
        helpers.poly_pow(q, 2, algebra), resultant_i, algebra
    )
    second_target = helpers.poly_pow(r7, 4, algebra)

    first_pass = True
    second_pass = True
    try:
        helpers.require_associate(
            resultant_j, first_target, algebra, "first quotient norm"
        )
    except RuntimeError:
        first_pass = False
    try:
        helpers.require_associate(
            second_left, second_target, algebra, "second quotient norm"
        )
    except RuntimeError:
        second_pass = False
    require(not (first_pass and second_pass), "fixed-swap full quotient survivor")
    print(
        f"fixed_swap_survivor={record['factor_index']} q_slice=PASS "
        f"first_quotient_norm={str(first_pass).upper()} "
        f"second_quotient_norm={str(second_pass).upper()}",
        flush=True,
    )
    return first_pass, second_pass


def main() -> None:
    require(flint.__version__ == "0.9.0", "python-flint version")
    require(
        hashlib.sha256(SURVIVORS.read_bytes()).hexdigest() == SURVIVORS_SHA256,
        "survivor hash",
    )
    base = load_module(BASE, BASE_SHA256, "fixed_same_full_quotient")
    source = base.load_module(base.SOURCE, base.SOURCE_SHA256, "positive_qslice")
    helpers = base.load_module(
        base.HELPERS, base.HELPERS_SHA256, "full_quotient_helpers"
    )
    payload = json.loads(SURVIVORS.read_text(encoding="ascii"))
    require(payload["allocation"] == "swap", "allocation")
    require(len(payload["survivors"]) == 1, "survivor count")
    outcomes = [
        run_record(base, source, helpers, record)
        for record in payload["survivors"]
    ]
    rejected = sum(not (first and second) for first, second in outcomes)
    print(
        "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_SWAP_"
        f"FULL_QUOTIENT_PROBE_PASS tested=1 rejected={rejected} "
        f"survived={len(outcomes) - rejected}",
        flush=True,
    )


if __name__ == "__main__":
    main()
