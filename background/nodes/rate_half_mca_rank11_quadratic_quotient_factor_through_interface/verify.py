#!/usr/bin/env python3
"""Verify the quadratic quotient factor-through interface."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "d01ae3d6be9e1cbb150d8b9c9bbf4187d78a286ecbd525e923bb9a9b5b34d903"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def projectively_equal(left: tuple[int, int], right: tuple[int, int], prime: int) -> bool:
    return (left[0] * right[1] - right[0] * left[1]) % prime == 0


def mobius_pair(q_num: int, q_den: int, matrix: tuple[int, int, int, int], prime: int) -> tuple[int, int]:
    a, b, c, d = matrix
    return ((a * q_num + b * q_den) % prime, (c * q_num + d * q_den) % prime)


def toy_factor_checks() -> int:
    prime = 97
    order = 16
    generator = pow(5, (prime - 1) // order, prime)
    group = {pow(generator, exponent, prime) for exponent in range(order)}
    matrices = ((1, 2, 3, 5), (2, 7, 1, 4), (3, 1, 5, 9))
    require(all((a * d - b * c) % prime for a, b, c, d in matrices), "invertible matrices")

    checks = 0
    for matrix in matrices:
        for x in group:
            cyclic_x = mobius_pair(x * x % prime, 1, matrix, prime)
            cyclic_neg = mobius_pair((-x % prime) ** 2 % prime, 1, matrix, prime)
            require(projectively_equal(cyclic_x, cyclic_neg, prime), "cyclic invariance")
            checks += 1

        for kappa in (1, generator, generator * generator % prime):
            for x in group:
                partner = kappa * pow(x, prime - 2, prime) % prime
                q_x = ((x * x + kappa) % prime, x)
                q_partner = ((partner * partner + kappa) % prime, partner)
                left = mobius_pair(*q_x, matrix, prime)
                right = mobius_pair(*q_partner, matrix, prime)
                require(projectively_equal(left, right, prime), "dihedral invariance")
                checks += 1
    return checks


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-quadratic-quotient-factor-through-interface-v1",
        "schema",
    )
    require(data.get("minimum_distinct_fibers") == 4370, "fiber pin")
    require(data.get("rational_slope_map") == "-u/v", "slope map")
    require(data.get("cyclic_locator_basis") == ["X^2", "1"], "cyclic basis")
    require(data.get("cyclic_quotient") == "X^2", "cyclic quotient")
    require(data.get("dihedral_locator_basis") == ["X^2+kappa", "X"], "dihedral basis")
    require(data.get("dihedral_quotient") == "X+kappa/X", "dihedral quotient")
    require(data.get("postcomposition") == "PGL_2(F)", "postcomposition")
    require("does not pay" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for dependency in (
        "rate_half_mca_rank11_heavy_ruling_exception_split_pencil_normal_form",
        "rate_half_mca_rank11_quadratic_quotient_survivor_identification",
    ):
        require(nodes.get(dependency, {}).get("status") == "PROVED", f"dependency {dependency}")
    return {"toy_checks": toy_factor_checks()}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("minimum_distinct_fibers", 1),
        lambda item: item.__setitem__("rational_slope_map", "u/v"),
        lambda item: item.__setitem__("cyclic_locator_basis", ["X", "1"]),
        lambda item: item.__setitem__("cyclic_quotient", "X"),
        lambda item: item.__setitem__("dihedral_locator_basis", ["X^2", "X"]),
        lambda item: item.__setitem__("dihedral_quotient", "X-kappa/X"),
        lambda item: item.__setitem__("postcomposition", "PGL_3(F)"),
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item.__setitem__("nonclaim", "records paid"),
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
        print(f"QUADRATIC_QUOTIENT_FACTOR_TAMPER_PASS mutations={tamper_selftest(data)}/9")
        return
    print(f"QUADRATIC_QUOTIENT_FACTOR_PASS toy_checks={checked['toy_checks']}")


if __name__ == "__main__":
    main()
