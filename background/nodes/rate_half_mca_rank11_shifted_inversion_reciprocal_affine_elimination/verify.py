#!/usr/bin/env python3
"""Verify the reciprocal-affine shifted-inversion elimination."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "8ff563e2379abb76d88d3bb4bdb1d81ab654d7d1a8155f774c513fe3b60114ea"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def toy_reciprocal_checks() -> int:
    prime = 97
    order = 16
    generator = pow(5, (prime - 1) // order, prime)
    group = {pow(generator, exponent, prime) for exponent in range(order)}
    require(len(group) == order, "toy subgroup")

    checks = 0
    for tau in (1, 2, 5, 11, 29):
        kappa = tau * tau % prime
        constant = -pow(tau, prime - 2, prime) % prime
        original = {
            (x, y)
            for x in group
            for y in group
            if (x + tau) * (y + tau) % prime == kappa
        }
        reflected = {
            (u, v)
            for u in group
            for v in group
            if (u + v) % prime == constant
        }
        image = {
            (pow(x, prime - 2, prime), pow(y, prime - 2, prime))
            for x, y in original
        }
        require(image == reflected, "reciprocal graph bijection")
        require(
            sum(x != y for x, y in original)
            == sum(u != v for u, v in reflected),
            "nonfixed graph preservation",
        )
        checks += 1
    return checks


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-shifted-inversion-reciprocal-affine-elimination-v1",
        "schema",
    )
    fibers = data.get("minimum_survivor_fibers")
    points = data.get("minimum_survivor_nonfixed_points")
    cap_points = data.get("maximum_affine_reflection_points")
    cap_fibers = data.get("maximum_affine_reflection_fibers")
    require((fibers, points, cap_points, cap_fibers) == (4370, 8740, 2308, 1154), "pins")
    require(points == 2 * fibers and cap_points == 2 * cap_fibers, "point/fiber conversion")
    require(data.get("fiber_contradiction_margin") == fibers - cap_fibers == 3216, "fiber margin")
    require(data.get("point_contradiction_margin") == points - cap_points == 6432, "point margin")
    require(data.get("normalized_parameter") == "kappa/tau^2", "parameter")
    require(data.get("excluded_parameter") == 1, "excluded parameter")
    require(data.get("transformed_reflection_constant") == "-1/tau", "reflection constant")
    require(data.get("high_complexity_threshold") == 2299571, "complexity threshold")
    require("only" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for dependency in (
        "rate_half_mca_rank11_shifted_inversion_product_energy_ledger",
        "rate_half_mca_rank11_exception_spi_affine_reflection_fixed_pencil_cap",
    ):
        require(nodes.get(dependency, {}).get("status") == "PROVED", f"dependency {dependency}")

    return {"toy_checks": toy_reciprocal_checks(), "fiber_margin": fibers - cap_fibers}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("minimum_survivor_fibers", 4369),
        lambda item: item.__setitem__("minimum_survivor_nonfixed_points", 8738),
        lambda item: item.__setitem__("maximum_affine_reflection_points", 2310),
        lambda item: item.__setitem__("maximum_affine_reflection_fibers", 1155),
        lambda item: item.__setitem__("fiber_contradiction_margin", 3215),
        lambda item: item.__setitem__("point_contradiction_margin", 6431),
        lambda item: item.__setitem__("normalized_parameter", "kappa/tau"),
        lambda item: item.__setitem__("excluded_parameter", 0),
        lambda item: item.__setitem__("transformed_reflection_constant", "-tau"),
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
        print(f"RECIPROCAL_AFFINE_ELIMINATION_TAMPER_PASS mutations={tamper_selftest(data)}/9")
        return
    print(
        "RECIPROCAL_AFFINE_ELIMINATION_PASS "
        f"toy_checks={checked['toy_checks']} fiber_margin={checked['fiber_margin']}"
    )


if __name__ == "__main__":
    main()
