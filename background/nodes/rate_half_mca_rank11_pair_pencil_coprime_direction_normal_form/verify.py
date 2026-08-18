#!/usr/bin/env python3
"""Verify the pair-pencil coprime-direction normal form contract."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "d55f5f730f7a5352b9f2bc33794dc789b6b9beb41c0533760df5a8066721dac6"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-rank11-pair-pencil-coprime-direction-normal-form-v1",
        "schema",
    )
    n, m, K = data.get("n"), data.get("m"), data.get("K")
    q = data.get("quotient_type_floor")
    core = data.get("pair_core_size")
    dim = data.get("correction_space_dimension_cap")
    intersection = data.get("pair_core_intersection_floor")
    direction = data.get("primitive_direction_degree_cap")
    require((n, m, K) == (2097152, 1116048, 1048576), "official row")
    require(q == 520 and core == m - 2, "population/core")
    require(dim == 4, "base-field dimension")
    require(intersection == 2 * core - n == 134940, "intersection floor")
    require(direction == K - 1 - intersection == 913635, "direction degree")
    require("gcd(U,V)=1" in str(data.get("normal_form")), "coprime form")
    root_inclusion = str(data.get("root_inclusion"))
    require("subset" in root_inclusion and "R_p-R_q" in root_inclusion, "root inclusion")
    require("not proved" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for dependency in (
        "rate_half_mca_rank11_quadratic_quotient_large_owner_or_pair_pencil_router",
        "rate_half_mca_rank11_heavy_ruling_triple_owner_pole_simple_router",
    ):
        require(nodes.get(dependency, {}).get("status") == "PROVED", f"dependency {dependency}")
    return {"types": q, "dimension": dim, "roots": intersection, "direction": direction}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("n", 2097151),
        lambda item: item.__setitem__("quotient_type_floor", 519),
        lambda item: item.__setitem__("pair_core_size", 1116045),
        lambda item: item.__setitem__("correction_space_dimension_cap", 5),
        lambda item: item.__setitem__("pair_core_intersection_floor", 134939),
        lambda item: item.__setitem__("primitive_direction_degree_cap", 913636),
        lambda item: item.__setitem__("normal_form", "rational direction"),
        lambda item: item.__setitem__("root_inclusion", "unrelated roots"),
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
        print(f"PAIR_PENCIL_COPRIME_DIRECTION_TAMPER_PASS mutations={tamper_selftest(data)}/8")
        return
    print(
        "PAIR_PENCIL_COPRIME_DIRECTION_PASS "
        f"types={checked['types']} dim={checked['dimension']} roots={checked['roots']} "
        f"direction={checked['direction']}"
    )


if __name__ == "__main__":
    main()
