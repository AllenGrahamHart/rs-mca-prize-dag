#!/usr/bin/env python3
"""Verify the shifted-inversion product-energy ledger."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "cd621dd58a4a513c06e1cfb1e470a9321863f0e51765386cba3b8a4631a998da"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def counts(group: set[int], tau: int, prime: int) -> tuple[Counter[int], Counter[int]]:
    representations: Counter[int] = Counter()
    fixed: Counter[int] = Counter()
    for x in group:
        if (x + tau) % prime == 0:
            continue
        fixed[(x + tau) ** 2 % prime] += 1
        for y in group:
            product = (x + tau) * (y + tau) % prime
            if product:
                representations[product] += 1
    return representations, fixed


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-shifted-inversion-product-energy-ledger-v1",
        "schema",
    )
    p, n, index = (
        data.get("official_base_prime"),
        data.get("official_domain_order"),
        data.get("cyclotomic_index"),
    )
    require((p, n, index) == (2130706433, 2**21, 1016), "pins")
    require(p - 1 == index * n, "index")
    numerator = data.get("shift_outside_subgroup_nonfixed_mean_numerator")
    denominator = data.get("shift_outside_subgroup_nonfixed_mean_denominator")
    quotient, remainder = divmod(numerator, denominator)
    require(numerator == n - 1 and denominator == index, "mean fraction")
    require(
        (quotient, remainder)
        == (
            data.get("shift_outside_subgroup_nonfixed_mean_integer_part"),
            data.get("shift_outside_subgroup_nonfixed_mean_remainder"),
        )
        == (2064, 127),
        "mean division",
    )
    require(data.get("forced_nonfixed_points") == 8740, "threshold")
    require(data.get("scaling_invariant") == "kappa/tau^2", "scaling invariant")
    require(data.get("reciprocal_exception") == "kappa=tau^2", "exception")
    require(data.get("reciprocal_affine_constant") == "-1/tau", "affine constant")

    toy_p = 97
    toy_n = 16
    generator = pow(5, (toy_p - 1) // toy_n, toy_p)
    group = {pow(generator, exponent, toy_p) for exponent in range(toy_n)}
    require(len(group) == toy_n and -1 % toy_p in group, "toy subgroup")
    checks = 0
    for tau in (1, 2, 5, 11):
        representations, fixed = counts(group, tau, toy_p)
        z = int((-tau) % toy_p in group)
        require(sum(representations.values()) == (toy_n - z) ** 2, "R first moment")
        require(sum(fixed.values()) == toy_n - z, "F first moment")
        nonfixed = {
            kappa: representations[kappa] - fixed[kappa]
            for kappa in range(1, toy_p)
        }
        require(sum(nonfixed.values()) == (toy_n - z) * (toy_n - z - 1), "I first moment")
        require(all(value % 2 == 0 for value in nonfixed.values()), "orbit parity")
        energy = sum(value * value for value in representations.values())
        shifted = [(x + tau) % toy_p for x in group if (x + tau) % toy_p]
        products = Counter(a * b % toy_p for a in shifted for b in shifted)
        require(energy == sum(value * value for value in products.values()), "energy")

        h = generator
        scaled_r, scaled_f = counts(group, h * tau % toy_p, toy_p)
        for kappa in range(1, toy_p):
            require(
                scaled_r[h * h * kappa % toy_p] == representations[kappa],
                "R scaling",
            )
            require(scaled_f[h * h * kappa % toy_p] == fixed[kappa], "F scaling")

        for kappa in (3, 7, 13, 29):
            a_value = (tau * tau - kappa) % toy_p
            if a_value == 0:
                continue
            inverse = pow(a_value, toy_p - 2, toy_p)
            new_tau = tau * inverse % toy_p
            new_kappa = kappa * inverse * inverse % toy_p
            reciprocal_r, reciprocal_f = counts(group, new_tau, toy_p)
            require(reciprocal_r[new_kappa] == representations[kappa], "R reciprocal")
            require(reciprocal_f[new_kappa] == fixed[kappa], "F reciprocal")
            require(
                new_kappa * pow(new_tau, toy_p - 3, toy_p) % toy_p
                == kappa * pow(tau, toy_p - 3, toy_p) % toy_p,
                "lambda reciprocal",
            )
            checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(
        nodes.get("rate_half_mca_rank11_quadratic_survivor_mobius_router", {}).get("status")
        == "PROVED",
        "dependency",
    )
    require("does not imply" in str(data.get("nonclaim")).lower(), "nonclaim")
    return {"mean_integer": quotient, "mean_remainder": remainder, "toy_checks": checks}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("official_base_prime", 2130706431),
        lambda item: item.__setitem__("official_domain_order", 2**21 - 1),
        lambda item: item.__setitem__("cyclotomic_index", 1015),
        lambda item: item.__setitem__("forced_nonfixed_points", 8738),
        lambda item: item.__setitem__("shift_outside_subgroup_nonfixed_mean_numerator", 2097152),
        lambda item: item.__setitem__("shift_outside_subgroup_nonfixed_mean_remainder", 128),
        lambda item: item.__setitem__("scaling_invariant", "kappa/tau"),
        lambda item: item.__setitem__("reciprocal_exception", "kappa=0"),
        lambda item: item.__setitem__("nonclaim", "pointwise cap follows"),
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
        print(f"SHIFTED_PRODUCT_ENERGY_LEDGER_TAMPER_PASS mutations={tamper_selftest(data)}/9")
        return
    print(
        "SHIFTED_PRODUCT_ENERGY_LEDGER_PASS "
        f"mean={checked['mean_integer']}+{checked['mean_remainder']}/1016 "
        f"toy_checks={checked['toy_checks']}"
    )


if __name__ == "__main__":
    main()
