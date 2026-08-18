#!/usr/bin/env python3
"""Verify the official-field affine-reflection exception-SPI fence."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "373f3d0292a9d6dc0d0ad10cf7deef900e23a606cb77b9cd16fcd98a7500c12b"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return value == divisor
        divisor = 3 if divisor == 2 else divisor + 2
    return True


def multiplicative_order(value: int, p: int) -> int:
    current = 1
    for order in range(1, p):
        current = current * value % p
        if current == 1:
            return order
    raise Reject("order")


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-exception-spi-affine-reflection-fence-v1",
        "schema",
    )
    p = data.get("official_base_prime")
    n = data.get("official_domain_order")
    exponent = data.get("official_domain_exponent")
    require(p == 2130706433 and is_prime(p), "official prime")
    require(n == 2**exponent == 2097152 and exponent == 21, "official domain")
    require((p - 1) == 1016 * n, "domain divisibility")
    numerator = n * n - n
    quotient, remainder = divmod(numerator, p - 1)
    require((quotient, remainder) == (2064, 266338304), "average division")
    forced_points = quotient + (1 if remainder else 0)
    forced_fibers = (forced_points - 1) // 2
    require(quotient == data.get("nonzero_reflection_average_floor"), "average floor")
    require(forced_points == data.get("forced_reflection_points") == 2065, "points")
    require(forced_fibers == data.get("forced_quadratic_fibers") == 1032, "fibers")
    require(forced_fibers > data.get("minimum_required_fibers") == 20, "threshold")

    toy = data.get("toy")
    require(isinstance(toy, dict), "toy")
    tp, order, primitive, c = (
        toy.get("field"),
        toy.get("domain_order"),
        toy.get("primitive_field_generator"),
        toy.get("reflection_constant"),
    )
    require((tp, order, primitive, c) == (97, 32, 5, 96), "toy pins")
    require(multiplicative_order(primitive, tp) == tp - 1, "toy primitive")
    h = pow(primitive, (tp - 1) // order, tp)
    domain = {pow(h, i, tp) for i in range(order)}
    reflected = {x for x in domain if (c - x) % tp in domain}
    require(len(reflected) == toy.get("reflection_points") == 12, "toy points")
    pairs = {
        tuple(sorted((x, (c - x) % tp)))
        for x in reflected
        if x != (c - x) % tp
    }
    require(len(pairs) == toy.get("quadratic_fibers") == 6, "toy pairs")
    slopes: set[int] = set()
    union: set[int] = set()
    for left, right in pairs:
        require(not ({left, right} & union), "toy disjointness")
        union.update((left, right))
        gamma = left * right % tp
        require(gamma not in slopes, "toy slope injectivity")
        slopes.add(gamma)
        require((left + right) % tp == c, "toy sum")
        require(all((x * x - c * x + gamma) % tp == 0 for x in (left, right)), "toy roots")
    require(union == reflected, "toy coverage")
    require("not an unsafe mca line" in str(data.get("nonclaim")).lower(), "nonclaim")
    return {"points": forced_points, "fibers": forced_fibers, "toy_fibers": len(pairs)}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("official_base_prime", 2130706431),
        lambda item: item.__setitem__("official_domain_exponent", 20),
        lambda item: item.__setitem__("nonzero_reflection_average_floor", 2063),
        lambda item: item.__setitem__("forced_reflection_points", 2064),
        lambda item: item.__setitem__("forced_quadratic_fibers", 1031),
        lambda item: item.__setitem__("minimum_required_fibers", 1032),
        lambda item: item["toy"].__setitem__("reflection_constant", 0),
        lambda item: item["toy"].__setitem__("reflection_points", 11),
        lambda item: item["toy"].__setitem__("quadratic_fibers", 5),
    )
    caught = 0
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    return caught


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    if args.tamper_selftest:
        caught = tamper_selftest(data)
        print(f"RANK11_EXCEPTION_SPI_AFFINE_REFLECTION_TAMPER_PASS mutations={caught}/9")
        return
    print(
        "RANK11_EXCEPTION_SPI_AFFINE_REFLECTION_PASS "
        f"official_points={result['points']} official_fibers={result['fibers']} "
        f"toy_fibers={result['toy_fibers']}"
    )


if __name__ == "__main__":
    main()
