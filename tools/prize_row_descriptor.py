#!/usr/bin/env python3
"""Build exact row-derived constants for an admissible prize row."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


INPUT_SCHEMA = "prize-row-input-v1"
OUTPUT_SCHEMA = "prize-row-descriptor-v1"
EPSILON_BITS = 128
FIELD_CAP = 1 << 256
K_CAP = 1 << 40
SUPPORTED_RATES = {
    Fraction(1, 2),
    Fraction(1, 4),
    Fraction(1, 8),
    Fraction(1, 16),
}


def exact_int(value: Any, label: str) -> int:
    if isinstance(value, bool):
        raise ValueError(f"{label} must be an integer")
    if isinstance(value, int):
        result = value
    elif isinstance(value, str) and value and value.isdigit():
        result = int(value)
    else:
        raise ValueError(f"{label} must be a nonnegative decimal integer")
    if result < 0:
        raise ValueError(f"{label} must be nonnegative")
    return result


def exact_rate(value: Any) -> Fraction:
    if not isinstance(value, str):
        raise ValueError("rate must be an exact fraction string")
    try:
        rate = Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError("rate must be an exact fraction string") from exc
    if rate not in SUPPORTED_RATES:
        allowed = ", ".join(str(item) for item in sorted(SUPPORTED_RATES))
        raise ValueError(f"rate must be one of {allowed}")
    return rate


def describe_row(source: dict[str, Any]) -> dict[str, Any]:
    if source.get("schema") != INPUT_SCHEMA:
        raise ValueError(f"schema must be {INPUT_SCHEMA}")
    p = exact_int(source.get("p"), "p")
    extension_degree = exact_int(source.get("extension_degree"), "extension_degree")
    subgroup_log2 = exact_int(source.get("subgroup_log2"), "subgroup_log2")
    rate = exact_rate(source.get("rate"))
    if p < 2:
        raise ValueError("p must be at least 2")
    if extension_degree == 0:
        raise ValueError("extension_degree must be positive")
    if (p.bit_length() - 1) * extension_degree >= 256:
        raise ValueError("official rows require q < 2^256")
    if subgroup_log2 >= 256:
        raise ValueError("evaluation subgroup order must be below 2^256")

    q = p**extension_degree
    n = 1 << subgroup_log2
    scaled_k = n * rate.numerator
    if scaled_k % rate.denominator:
        raise ValueError("rate does not give an integral dimension")
    k = scaled_k // rate.denominator

    if q >= FIELD_CAP:
        raise ValueError("official rows require q < 2^256")
    if k > K_CAP:
        raise ValueError("official rows require k <= 2^40")
    if (q - 1) % n:
        raise ValueError("evaluation subgroup order n must divide q-1")
    if not 0 < k < n:
        raise ValueError("need 0 < k < n")

    core = {
        "p": str(p),
        "extension_degree": extension_degree,
        "subgroup_log2": subgroup_log2,
        "rate": f"{rate.numerator}/{rate.denominator}",
    }
    fingerprint = hashlib.sha256(
        json.dumps(core, separators=(",", ":"), sort_keys=True).encode()
    ).hexdigest()
    return {
        "schema": OUTPUT_SCHEMA,
        "row_fingerprint_sha256": fingerprint,
        "input": core,
        "field": {
            "characteristic_decimal": str(p),
            "extension_degree": extension_degree,
            "order_decimal": str(q),
            "order_bit_length": q.bit_length(),
            "under_2^256": True,
        },
        "evaluation_domain": {
            "order_decimal": str(n),
            "order_log2": subgroup_log2,
            "subgroup_cofactor_decimal": str((q - 1) // n),
            "divides_field_units": True,
        },
        "code": {
            "dimension_decimal": str(k),
            "dimension_at_most_2^40": True,
            "rate": f"{rate.numerator}/{rate.denominator}",
        },
        "target": {
            "epsilon_bits": EPSILON_BITS,
            "denominator_decimal": str(q),
            "B_star_decimal": str(q // (1 << EPSILON_BITS)),
        },
        "endpoint_contract": {
            "agreement_symbol": "a",
            "largest_safe_closed_radius": "(n-a)/n",
            "adjacent_unsafe_agreement": "a-1",
            "boundary_supremum": "(n-a+1)/n, not attained",
        },
        "external_preconditions": [
            "p is prime",
            "the supplied code uses the order-n multiplicative subgroup or a proved equivalent coset",
        ],
        "nonclaims": [
            "no primality certificate is generated",
            "no upper or lower theorem-packet count is generated",
            "no safe or unsafe agreement is inferred",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    result = describe_row(json.loads(args.input.read_text()))
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
