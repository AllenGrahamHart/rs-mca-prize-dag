#!/usr/bin/env python3
"""Dense small-order reference for the C36 Taylor cutoff ladder.

This is a correctness oracle, not an official-scale implementation. It
intentionally refuses exponents above four (n > 16).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import signal
import tempfile
import time
from pathlib import Path
from typing import Any

from sympy import Poly, QQ, expand, resultant, symbols


Z, T, X = symbols("Z T X")
SCHEMA = "c36-taylor-cutoff-reference-v1"
MAX_EXPONENT = 4


class ReferenceTimeout(RuntimeError):
    pass


def valuation_two(value: int) -> int:
    result = 0
    while value % 2 == 0:
        result += 1
        value //= 2
    return result


def canonical_block_specs(exponent: int) -> list[tuple[int, str, int]]:
    specs: list[tuple[int, str, int]] = []
    for degree_exponent in range(1, exponent):
        conductor = 2 ** (degree_exponent + 1)
        specs.extend((degree_exponent, "+", parameter) for parameter in range(2, conductor))
        specs.extend(
            (degree_exponent, "-", parameter)
            for parameter in range(2, conductor, 2)
        )
    return specs


def geometric_sum(parameter: int):
    return sum(Z**power for power in range(parameter))


def orbit_polynomial(spec: tuple[int, str, int]) -> Poly:
    degree_exponent, sign, parameter = spec
    degree = 2**degree_exponent
    cyclotomic = Z**degree + 1
    series = geometric_sum(parameter)
    if sign == "+":
        expression = resultant(cyclotomic, T - series, Z)
    else:
        if parameter % 2:
            raise ValueError("minus blocks require an even parameter")
        norm = 2 ** (2 ** valuation_two(parameter) - 1)
        expression = resultant(cyclotomic, series * T - 1, Z) / norm
    polynomial = Poly(expression, T, domain=QQ)
    if polynomial.LC() != 1 or polynomial.degree() != degree:
        raise AssertionError(f"bad orbit polynomial for {spec}")
    return polynomial


def shifted_product_polynomial(exponent: int) -> Poly:
    order = 2**exponent
    degree = order - 1
    shifted_root = Poly(expand(((1 - Z) ** order - 1) / Z), Z)
    second_factor = expand(Z**degree * shifted_root.as_expr().subs(Z, T / Z))
    polynomial = Poly(resultant(shifted_root.as_expr(), second_factor, Z), T)
    if polynomial.degree() != degree**2 or polynomial.LC() != 1:
        raise AssertionError("shifted-product resultant mismatch")
    return polynomial


def hasse_remainders(product: Poly, block: Poly, max_cutoff: int) -> list[Poly]:
    derivatives: list[Poly] = [Poly(product, T, domain=QQ)]
    for order in range(1, max_cutoff + 1):
        # Recompute from the original polynomial: differentiating a remainder
        # does not commute with reduction modulo q_O.
        expression = product.as_expr().diff(T, order) / math.factorial(order)
        derivatives.append(Poly(expression, T, domain=QQ))
    return [derivative.rem(block) for derivative in derivatives]


def odd_content(polynomial: Poly) -> int:
    content = 0
    for coefficient in polynomial.all_coeffs():
        numerator, denominator = map(int, coefficient.as_numer_denom())
        if denominator <= 0 or denominator & (denominator - 1):
            raise AssertionError("non-dyadic coefficient denominator")
        content = math.gcd(content, abs(numerator))
    while content and content % 2 == 0:
        content //= 2
    return content


def coefficient_hash(polynomial: Poly) -> str:
    payload = ",".join(str(value) for value in polynomial.all_coeffs()).encode()
    return hashlib.sha256(payload).hexdigest()


def taylor_content(remainders: list[Poly], block: Poly, cutoff: int) -> tuple[int, int, str]:
    packet = sum(remainders[index].as_expr() * X**index for index in range(cutoff + 1))
    certificate = Poly(resultant(block.as_expr(), packet, T), X, domain=QQ)
    return odd_content(certificate), certificate.degree(), coefficient_hash(certificate)


def atomic_write(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", dir=path.parent, delete=False) as handle:
        handle.write(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        temporary = Path(handle.name)
    temporary.replace(path)


def run_reference(
    exponent: int,
    cutoffs: list[int],
    output: Path,
    timeout_seconds: float,
    max_blocks: int | None = None,
) -> dict[str, Any]:
    if not 2 <= exponent <= MAX_EXPONENT:
        raise ValueError(f"exponent must be in [2,{MAX_EXPONENT}]")
    order = 2**exponent
    if not cutoffs or any(cutoff < 2 or cutoff >= order - 1 for cutoff in cutoffs):
        raise ValueError("every cutoff must satisfy 2 <= cutoff < n-1")
    cutoffs = sorted(set(cutoffs))
    specs = canonical_block_specs(exponent)
    selected = specs if max_blocks is None else specs[: max(0, max_blocks)]
    start = time.monotonic()
    payload: dict[str, Any] = {
        "schema": SCHEMA,
        "complete": False,
        "stage": "initializing",
        "exponent": exponent,
        "order": order,
        "cutoffs": cutoffs,
        "expected_blocks": len(specs),
        "selected_blocks": len(selected),
        "blocks": [],
        "elapsed_seconds": 0.0,
        "error": None,
    }
    atomic_write(output, payload)

    def timeout_handler(_signum, _frame):
        raise ReferenceTimeout(f"timeout after {timeout_seconds} seconds")

    old_handler = signal.signal(signal.SIGALRM, timeout_handler)
    if timeout_seconds > 0:
        signal.setitimer(signal.ITIMER_REAL, timeout_seconds)
    try:
        payload["stage"] = "building_shifted_product"
        atomic_write(output, payload)
        product = shifted_product_polynomial(exponent)
        payload["product_degree"] = product.degree()
        payload["product_hash"] = coefficient_hash(product)
        payload["stage"] = "blocks"
        atomic_write(output, payload)

        for spec in selected:
            block_start = time.monotonic()
            block = orbit_polynomial(spec)
            remainders = hasse_remainders(product, block, max(cutoffs))
            results: dict[str, Any] = {}
            for cutoff in cutoffs:
                content, x_degree, digest = taylor_content(remainders, block, cutoff)
                results[str(cutoff)] = {
                    "odd_content": str(content),
                    "x_degree": x_degree,
                    "certificate_sha256": digest,
                }
            payload["blocks"].append(
                {
                    "id": f"{spec[0]}{spec[1]}{spec[2]}",
                    "j": spec[0],
                    "sign": spec[1],
                    "w": spec[2],
                    "degree": block.degree(),
                    "orbit_polynomial_sha256": coefficient_hash(block),
                    "cutoffs": results,
                    "seconds": round(time.monotonic() - block_start, 6),
                }
            )
            payload["elapsed_seconds"] = round(time.monotonic() - start, 6)
            atomic_write(output, payload)

        payload["complete"] = len(selected) == len(specs)
        payload["stage"] = "complete" if payload["complete"] else "partial_selection"
    except ReferenceTimeout as exc:
        payload["stage"] = "timeout"
        payload["error"] = str(exc)
    except Exception as exc:
        payload["stage"] = "error"
        payload["error"] = f"{type(exc).__name__}: {exc}"
        raise
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, old_handler)
        payload["elapsed_seconds"] = round(time.monotonic() - start, 6)
        atomic_write(output, payload)
    return payload


def parse_cutoffs(raw: str) -> list[int]:
    return [int(value) for value in raw.split(",") if value.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--exponent", type=int, required=True)
    parser.add_argument("--cutoffs", default="2")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument("--max-blocks", type=int)
    args = parser.parse_args()
    try:
        payload = run_reference(
            args.exponent,
            parse_cutoffs(args.cutoffs),
            args.output,
            args.timeout,
            args.max_blocks,
        )
    except (ValueError, AssertionError) as exc:
        print(f"C36_TAYLOR_REFERENCE_FAIL {exc}")
        return 2
    print(
        "C36_TAYLOR_REFERENCE_"
        f"{'PASS' if payload['complete'] else 'PARTIAL'} "
        f"n={payload['order']} blocks={len(payload['blocks'])}/{payload['selected_blocks']} "
        f"stage={payload['stage']} seconds={payload['elapsed_seconds']}"
    )
    return 0 if payload["complete"] else 3


if __name__ == "__main__":
    raise SystemExit(main())
