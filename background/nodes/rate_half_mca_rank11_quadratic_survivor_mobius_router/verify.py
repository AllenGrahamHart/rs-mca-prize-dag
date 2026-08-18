#!/usr/bin/env python3
"""Verify the quadratic synchronized-survivor Mobius router."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "9f3f2ec95488d364e8961e1a468c09f907d24f11caa75974d526c5ef82dde175"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def inverse(value: int, prime: int) -> int:
    require(value % prime != 0, "inverse")
    return pow(value, prime - 2, prime)


def classify(a: int, b: int, c: int, prime: int) -> tuple[str, int, int]:
    delta = (a * a + b * c) % prime
    require(delta != 0, "determinant")
    if b % prime == 0:
        return ("affine", c * inverse(a, prime) % prime, 0)
    tau = a * inverse(b, prime) % prime
    kappa = delta * inverse(b * b % prime, prime) % prime
    return ("constant-product" if tau == 0 else "shifted-inversion", tau, kappa)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-quadratic-survivor-mobius-router-v1",
        "schema",
    )
    prime = data.get("official_base_prime")
    order = data.get("official_domain_order")
    fibers = data.get("minimum_synchronized_fibers")
    points = data.get("minimum_nonfixed_graph_points")
    require((prime, order, fibers, points) == (2130706433, 2**21, 4370, 8740), "pins")
    require(points == 2 * fibers, "graph-point count")
    require((prime - 1) % order == 0, "official subgroup")
    degrees = data.get("allowed_exception_degrees")
    retained = data.get("retained_nonquadratic_degrees")
    require(degrees == list(range(1, 12)), "degrees")
    require(retained == [degree for degree in degrees if degree != 2], "degree split")
    require(
        (
            data.get("quadratic_coefficient_relation"),
            data.get("mobius_formula"),
            data.get("determinant_formula"),
            data.get("shift_formula"),
        )
        == (
            "b*x*y+a*(x+y)=c",
            "(c-a*x)/(a+b*x)",
            "a^2+b*c",
            "phi(x)+tau=kappa/(x+tau)",
        ),
        "formulas",
    )
    require(
        data.get("quadratic_classes")
        == ["antipodal", "constant-product", "shifted-inversion"],
        "classes",
    )
    require(data.get("high_complexity_threshold") == 2299571, "chi")

    samples = (
        (7, 0, 0),
        (7, 0, 13),
        (0, 5, 17),
        (11, 5, 17),
        (19, 23, 29),
    )
    checked = 0
    for a, b, c in samples:
        delta = (a * a + b * c) % prime
        require(delta != 0, "sample determinant")
        kind, tau_or_shift, kappa = classify(a, b, c, prime)
        if b == 0:
            require(kind == "affine" and tau_or_shift == c * inverse(a, prime) % prime, "affine")
        else:
            tau = tau_or_shift
            require(kappa != 0, "kappa")
            require((b * tau - a) % prime == 0, "tau")
            require((b * b * kappa - delta) % prime == 0, "kappa formula")
            require((kind == "constant-product") == (a == 0), "fractional split")
            for x in (1, 2, 3, 31, 127):
                denominator = (a + b * x) % prime
                if denominator == 0:
                    continue
                image = (c - a * x) * inverse(denominator, prime) % prime
                require((x + tau) % prime != 0, "shifted pole")
                normalized = kappa * inverse((x + tau) % prime, prime) - tau
                require(image == normalized % prime, "normalization identity")
                second_denominator = (a + b * image) % prime
                require(second_denominator != 0, "second denominator")
                second = (c - a * image) * inverse(second_denominator, prime) % prime
                require(second == x, "involution")
                checked += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    dependencies = (
        "rate_half_mca_rank11_nonzero_affine_reflection_mass_router",
        "rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_pair_locator_mobius_dichotomy",
    )
    require(all(nodes.get(dep, {}).get("status") == "PROVED" for dep in dependencies), "dependencies")
    require("does not pay" in str(data.get("nonclaim")).lower(), "nonclaim")
    return {"fibers": fibers, "points": points, "identity_checks": checked}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("official_base_prime", 2130706431),
        lambda item: item.__setitem__("minimum_synchronized_fibers", 4369),
        lambda item: item.__setitem__("minimum_nonfixed_graph_points", 8739),
        lambda item: item.__setitem__("allowed_exception_degrees", list(range(1, 11))),
        lambda item: item.__setitem__("retained_nonquadratic_degrees", [1, 3, 4]),
        lambda item: item.__setitem__("quadratic_classes", ["antipodal", "shifted-inversion"]),
        lambda item: item.__setitem__("determinant_formula", "a^2-b*c"),
        lambda item: item.__setitem__("high_complexity_threshold", 2299570),
        lambda item: item.__setitem__("nonclaim", "pays every survivor"),
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
        print(f"RANK11_QUADRATIC_MOBIUS_ROUTER_TAMPER_PASS mutations={tamper_selftest(data)}/9")
        return
    print(
        "RANK11_QUADRATIC_MOBIUS_ROUTER_PASS "
        f"fibers={checked['fibers']} graph_points={checked['points']} "
        f"identity_checks={checked['identity_checks']}"
    )


if __name__ == "__main__":
    main()
