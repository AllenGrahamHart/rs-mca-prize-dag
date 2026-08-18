#!/usr/bin/env python3
"""Verify the quotient-periodic exception-SPI route fence."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "01c960dee395b776edef296f31b799234b4c480f478a7cbb2adb4b8e6711218e"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


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
        == "rate-half-mca-rank11-exception-spi-quotient-periodic-fence-v1",
        "schema",
    )
    domain_order = data.get("official_domain_order")
    exponent = data.get("official_domain_exponent")
    degrees = data.get("supported_degrees")
    require(domain_order == 2**exponent == 2097152 and exponent == 21, "official domain")
    require(degrees == [1, 2, 4, 8], "degrees")
    counts = [domain_order // degree for degree in degrees]
    require(counts == data.get("fiber_counts") == [2097152, 1048576, 524288, 262144], "counts")
    minimum = min(counts)
    require(minimum == data.get("minimum_constructed_fibers") == 262144, "minimum")
    require(minimum > data.get("minimum_required_fibers") == 20, "twenty-fiber fence")
    require(all(domain_order % degree == 0 and degree <= 11 for degree in degrees), "degree scope")

    toy = data.get("toy")
    require(isinstance(toy, dict), "toy")
    p, order, generator, degree = (
        toy.get("field"),
        toy.get("domain_order"),
        toy.get("primitive_field_generator"),
        toy.get("degree"),
    )
    require((p, order, generator, degree) == (97, 32, 5, 4), "toy pins")
    require(multiplicative_order(generator, p) == p - 1, "primitive generator")
    domain_generator = pow(generator, (p - 1) // order, p)
    require(multiplicative_order(domain_generator, p) == order, "domain generator")
    domain = {pow(domain_generator, i, p) for i in range(order)}
    fibers: dict[int, set[int]] = {}
    for x in domain:
        fibers.setdefault(pow(x, degree, p), set()).add(x)
    require(len(fibers) == toy.get("expected_image_order") == toy.get("expected_fiber_count") == 8, "toy image")
    require(all(len(fiber) == toy.get("expected_fiber_size") == 4 for fiber in fibers.values()), "toy fibers")
    union: set[int] = set()
    for y, fiber in fibers.items():
        require(not (union & fiber), "toy disjointness")
        union.update(fiber)
        require(all((pow(x, degree, p) - y) % p == 0 for x in fiber), "toy roots")
        require(pow(y, order // degree, p) == 1, "toy image group")
    require(union == domain, "toy partition")
    require("not an mca counterexample" in str(data.get("nonclaim")).lower(), "nonclaim")
    return {"minimum": minimum, "toy_fibers": len(fibers), "toy_points": len(union)}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("official_domain_exponent", 20),
        lambda item: item.__setitem__("supported_degrees", [1, 2, 4, 6]),
        lambda item: item.__setitem__("fiber_counts", [2097152, 1048576, 524288, 262143]),
        lambda item: item.__setitem__("minimum_constructed_fibers", 262143),
        lambda item: item.__setitem__("minimum_required_fibers", 262144),
        lambda item: item["toy"].__setitem__("primitive_field_generator", 4),
        lambda item: item["toy"].__setitem__("expected_fiber_size", 3),
        lambda item: item["toy"].__setitem__("expected_fiber_count", 7),
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
        print(f"RANK11_EXCEPTION_SPI_PERIODIC_FENCE_TAMPER_PASS mutations={caught}/8")
        return
    print(
        "RANK11_EXCEPTION_SPI_PERIODIC_FENCE_PASS "
        f"official_min={result['minimum']} toy_fibers={result['toy_fibers']} "
        f"toy_points={result['toy_points']}"
    )


if __name__ == "__main__":
    main()
