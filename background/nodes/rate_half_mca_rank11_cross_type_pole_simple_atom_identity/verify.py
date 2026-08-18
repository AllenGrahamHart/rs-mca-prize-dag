#!/usr/bin/env python3
"""Verify the official cross-type pole-simple atom-identity threshold."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "ade6ad1a3aeb7899cbeec67bb06dc9568d93c63e9ad5490902ed4b3fc96ee684"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_div(numerator: int, denominator: int) -> int:
    return -(-numerator // denominator)


def margin(n: int, m: int, dimension: int, shared: int) -> int:
    return ceil_div(shared * m - n, shared - 1) - (dimension - 1)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-cross-type-pole-simple-atom-identity-v1",
        "schema",
    )
    n = data.get("domain_size")
    m = data.get("support_size")
    dimension = data.get("code_dimension")
    minimum = data.get("minimum_shared_records")
    predecessor = data.get("threshold_predecessor")
    require((n, m, dimension) == (2097152, 1116048, 1048576), "row pins")
    require((minimum, predecessor) == (16, 15), "threshold pins")
    require(data.get("minimum_records_per_distinguished_type") == 3, "type multiplicity")
    predecessor_margin = margin(n, m, dimension, predecessor)
    require(predecessor_margin == -data.get("threshold_predecessor_deficit") == -2605, "predecessor")
    require(margin(n, m, dimension, minimum) == 2067 > 0, "first positive")
    require(all(margin(n, m, dimension, r) <= 0 for r in range(2, minimum)), "minimal threshold")
    require(all(margin(n, m, dimension, r) > 0 for r in range(minimum, 33)), "monotonic range")

    expected = {str(r): margin(n, m, dimension, r) for r in (16, 19, 22, 25, 28)}
    require(data.get("margins") == expected, "margins")
    for shortening in (0, 1, 67472, 524288, 1048573):
        for r, expected_margin in ((int(key), value) for key, value in expected.items()):
            actual = margin(n - shortening, m - shortening, dimension - shortening, r)
            require(actual == expected_margin, "shortening invariance")

    require(data.get("conclusion") == "projectively identical scalar-locator certificates", "conclusion")
    require("does not construct" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for dependency in (
        "rate_half_mca_rank11_heavy_ruling_triple_owner_pole_simple_router",
        "rate_half_mca_rank11_cross_type_scalar_pair_rigidity",
        "rate_half_mca_rank11_cross_type_one_swap_synchronization_wall",
    ):
        require(nodes.get(dependency, {}).get("status") == "PROVED", f"dependency {dependency}")
    return {"threshold": minimum, "margin": expected["16"]}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("minimum_shared_records", 15),
        lambda item: item.__setitem__("minimum_records_per_distinguished_type", 2),
        lambda item: item.__setitem__("threshold_predecessor", 14),
        lambda item: item.__setitem__("threshold_predecessor_deficit", 2604),
        lambda item: item["margins"].__setitem__("16", 2066),
        lambda item: item["margins"].__setitem__("19", 12967),
        lambda item: item["margins"].__setitem__("22", 20753),
        lambda item: item["margins"].__setitem__("25", 26593),
        lambda item: item["margins"].__setitem__("28", 31135),
        lambda item: item.__setitem__("conclusion", "proportional scalar pairs only"),
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
        print(f"CROSS_TYPE_POLE_SIMPLE_ATOM_IDENTITY_TAMPER_PASS mutations={tamper_selftest(data)}/10")
        return
    print(
        "CROSS_TYPE_POLE_SIMPLE_ATOM_IDENTITY_PASS "
        f"threshold={checked['threshold']} margin={checked['margin']}"
    )


if __name__ == "__main__":
    main()
