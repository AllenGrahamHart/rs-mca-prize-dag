#!/usr/bin/env python3
"""Verify the dihedral exception-SPI route fence."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "3daaf19044cb9003355121fa416fa45354415c6ff1a4ac669cba7251c01c15c1"


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
        == "rate-half-mca-rank11-exception-spi-dihedral-quotient-fence-v1",
        "schema",
    )
    order = data.get("official_domain_order")
    exponent = data.get("official_domain_exponent")
    ds = data.get("quotient_degrees")
    degrees = data.get("pencil_degrees")
    require(order == 2**exponent == 2097152 and exponent == 21, "official domain")
    require(ds == [1, 2, 4] and degrees == [2, 4, 8], "degrees")
    require([2 * d for d in ds] == degrees, "degree relation")
    counts = [order // (2 * d) for d in ds]
    require(counts == data.get("fiber_counts") == [1048576, 524288, 262144], "counts")
    require(min(counts) == data.get("minimum_constructed_fibers") == 262144, "minimum")
    require(min(counts) > data.get("minimum_required_fibers") == 20, "threshold")

    toy = data.get("toy")
    require(isinstance(toy, dict), "toy")
    p = toy.get("field")
    n = toy.get("domain_order")
    primitive = toy.get("primitive_field_generator")
    d = toy.get("quotient_degree")
    require((p, n, primitive, d) == (97, 32, 5, 4), "toy pins")
    require(multiplicative_order(primitive, p) == p - 1, "primitive generator")
    h = pow(primitive, (p - 1) // n, p)
    require(multiplicative_order(h, p) == n, "domain generator")
    domain = {pow(h, i, p) for i in range(n)}
    quotient = {pow(x, d, p) for x in domain}
    require(len(quotient) == toy.get("expected_quotient_order") == 8, "quotient")
    a = pow(h, d, p)
    require(a in quotient and pow(a, len(quotient) // 2, p) == p - 1, "nonsquare")

    seen_z: set[int] = set()
    slopes: set[int] = set()
    fibers: list[set[int]] = []
    for z in quotient:
        if z in seen_z:
            continue
        mate = a * pow(z, p - 2, p) % p
        require(mate != z and mate in quotient, "fixed-point-free involution")
        seen_z.update((z, mate))
        gamma = -(z + mate) % p
        require(gamma not in slopes, "slope injectivity")
        slopes.add(gamma)
        fiber = {
            x
            for x in domain
            if (pow(x, 2 * d, p) + gamma * pow(x, d, p) + a) % p == 0
        }
        require(len(fiber) == toy.get("expected_fiber_size") == 8, "fiber size")
        require(all(not (fiber & prior) for prior in fibers), "fiber disjointness")
        fibers.append(fiber)

    require(seen_z == quotient, "orbit coverage")
    require(len(fibers) == toy.get("expected_fiber_count") == 4, "fiber count")
    require(set().union(*fibers) == domain, "domain partition")
    require("not an mca counterexample" in str(data.get("nonclaim")).lower(), "nonclaim")
    return {"minimum": min(counts), "toy_fibers": len(fibers), "toy_points": len(domain)}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("official_domain_exponent", 20),
        lambda item: item.__setitem__("quotient_degrees", [1, 2, 3]),
        lambda item: item.__setitem__("pencil_degrees", [2, 4, 6]),
        lambda item: item.__setitem__("fiber_counts", [1048576, 524288, 262143]),
        lambda item: item.__setitem__("minimum_constructed_fibers", 262143),
        lambda item: item.__setitem__("minimum_required_fibers", 262144),
        lambda item: item["toy"].__setitem__("primitive_field_generator", 4),
        lambda item: item["toy"].__setitem__("expected_fiber_size", 7),
        lambda item: item["toy"].__setitem__("expected_fiber_count", 3),
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
        print(f"RANK11_EXCEPTION_SPI_DIHEDRAL_FENCE_TAMPER_PASS mutations={caught}/9")
        return
    print(
        "RANK11_EXCEPTION_SPI_DIHEDRAL_FENCE_PASS "
        f"official_min={result['minimum']} toy_fibers={result['toy_fibers']} "
        f"toy_points={result['toy_points']}"
    )


if __name__ == "__main__":
    main()
