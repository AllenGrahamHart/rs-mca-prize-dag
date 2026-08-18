#!/usr/bin/env python3
"""Verify the quadratic quotient-survivor identification."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "bf16d15b78bf1527448e471563569952e1b1dd63d4fbd01da62a3b35d957db5a"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def toy_orbit_checks() -> int:
    prime = 97
    order = 16
    generator = pow(5, (prime - 1) // order, prime)
    group = {pow(generator, exponent, prime) for exponent in range(order)}
    squares = {x * x % prime for x in group}
    require(len(group) == order and len(squares) == order // 2, "toy subgroup")

    antipodal = {frozenset((x, -x % prime)) for x in group}
    require(len(antipodal) == order // 2, "antipodal count")
    require({next(iter(pair)) ** 2 % prime for pair in antipodal} == squares, "cyclic fibers")

    checks = 0
    for kappa in group:
        fixed = {x for x in group if x * x % prime == kappa}
        orbits = {
            frozenset((x, kappa * pow(x, prime - 2, prime) % prime))
            for x in group
            if x * x % prime != kappa
        }
        expected_fixed = 2 if kappa in squares else 0
        require(len(fixed) == expected_fixed, "constant-product fixed points")
        require(len(orbits) == (order - expected_fixed) // 2, "constant-product orbit count")
        slopes = set()
        for orbit in orbits:
            require(len(orbit) == 2, "nonfixed orbit")
            x, y = tuple(orbit)
            require(x * y % prime == kappa, "constant product")
            slopes.add((x + y) % prime)
        require(len(slopes) == len(orbits), "slope injectivity")
        checks += 1
    return checks


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-quadratic-quotient-survivor-identification-v1",
        "schema",
    )
    n = data.get("official_domain_order")
    demand = data.get("required_survivor_fibers")
    require((n, demand) == (2**21, 4370), "official pins")
    require(data.get("antipodal_fixed_points") == 0, "antipodal fixed points")
    require(data.get("antipodal_fibers") == n // 2 == 1048576, "antipodal fibers")
    require(data.get("constant_product_nonsquare_fixed_points") == 0, "nonsquare fixed points")
    require(data.get("constant_product_nonsquare_fibers") == n // 2, "nonsquare fibers")
    require(data.get("constant_product_square_fixed_points") == 2, "square fixed points")
    require(data.get("constant_product_square_fibers") == (n - 2) // 2, "square fibers")
    minimum = min(
        data.get("antipodal_fibers"),
        data.get("constant_product_nonsquare_fibers"),
        data.get("constant_product_square_fibers"),
    )
    require(data.get("minimum_quotient_fibers") == minimum == 1048575, "minimum")
    require(data.get("minimum_excess_over_survivor") == minimum - demand == 1044205, "excess")
    require(data.get("remaining_shifted_parameter") == "lambda!=0,1", "shifted frontier")
    require("does not pay" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for dependency in (
        "rate_half_mca_rank11_quadratic_survivor_mobius_router",
        "rate_half_mca_rank11_exception_spi_quotient_periodic_fence",
        "rate_half_mca_rank11_exception_spi_dihedral_quotient_fence",
        "rate_half_mca_rank11_shifted_inversion_reciprocal_affine_elimination",
    ):
        require(nodes.get(dependency, {}).get("status") == "PROVED", f"dependency {dependency}")
    return {"toy_checks": toy_orbit_checks(), "minimum": minimum}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("official_domain_order", 2**21 - 1),
        lambda item: item.__setitem__("required_survivor_fibers", 4369),
        lambda item: item.__setitem__("antipodal_fixed_points", 2),
        lambda item: item.__setitem__("antipodal_fibers", 1048575),
        lambda item: item.__setitem__("constant_product_nonsquare_fibers", 1048575),
        lambda item: item.__setitem__("constant_product_square_fixed_points", 0),
        lambda item: item.__setitem__("constant_product_square_fibers", 1048576),
        lambda item: item.__setitem__("minimum_excess_over_survivor", 1044204),
        lambda item: item.__setitem__("remaining_shifted_parameter", "lambda!=0"),
    )
    caught = 0
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutations")
    return caught


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    checked = validate(data)
    if args.tamper_selftest:
        print(f"QUADRATIC_QUOTIENT_IDENTIFICATION_TAMPER_PASS mutations={tamper_selftest(data)}/9")
        return
    print(
        "QUADRATIC_QUOTIENT_IDENTIFICATION_PASS "
        f"minimum={checked['minimum']} toy_checks={checked['toy_checks']}"
    )


if __name__ == "__main__":
    main()
