#!/usr/bin/env python3
"""Verify cross-type scalar-pair rigidity arithmetic and dependencies."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "5fc6a6faee611491cd10bdfb698ebe5d4def70ec9d2e9e49b68a05d2841779d1"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_div(numerator: int, denominator: int) -> int:
    return -(-numerator // denominator)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-cross-type-scalar-pair-rigidity-v1",
        "schema",
    )
    n = data.get("domain_size")
    m = data.get("support_size")
    dimension = data.get("code_dimension")
    shared = data.get("shared_records")
    per_type = data.get("records_per_pair_type")
    require((n, m, dimension) == (2097152, 1116048, 1048576), "row pins")
    require((shared, per_type) == (28, 14), "deck pins")
    require(2 * per_type == shared, "balanced deck")
    require(data.get("pole_incidence_cap") == 1, "pole incidence")

    forced = ceil_div(shared * m - n, shared - 1)
    pair_cap = dimension - 1
    margin = forced - pair_cap
    require(data.get("forced_g_minus_h_before_shortening") == forced == 1079711, "forced floor")
    require(data.get("distinct_pair_core_cap_before_shortening") == pair_cap == 1048575, "pair cap")
    require(data.get("contradiction_margin") == margin == 31136, "margin")
    for shortening in (0, 1, 67471, 67472, 1048573):
        shortened_forced = ceil_div(shared * (m - shortening) - (n - shortening), shared - 1)
        require(shortened_forced == forced - shortening, "shortening floor")
        require(shortened_forced - (dimension - shortening - 1) == margin, "shortening margin")

    require(data.get("survivor_relation") == "proportional scalar coefficient pairs", "survivor")
    require(data.get("degree_two_interpretation") == "same projective value at infinity", "interpretation")
    require("does not prove" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for dependency in (
        "rate_half_mca_rank11_heavy_ruling_triple_owner_pole_simple_router",
        "rate_half_mca_rank11_cross_type_one_swap_synchronization_wall",
        "rate_half_mca_rank11_quadratic_quotient_factor_through_interface",
    ):
        require(nodes.get(dependency, {}).get("status") == "PROVED", f"dependency {dependency}")
    return {"forced": forced, "pair_cap": pair_cap, "margin": margin}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("domain_size", 2097151),
        lambda item: item.__setitem__("support_size", 1116047),
        lambda item: item.__setitem__("code_dimension", 1048575),
        lambda item: item.__setitem__("shared_records", 27),
        lambda item: item.__setitem__("records_per_pair_type", 13),
        lambda item: item.__setitem__("pole_incidence_cap", 2),
        lambda item: item.__setitem__("forced_g_minus_h_before_shortening", 1079710),
        lambda item: item.__setitem__("contradiction_margin", 31135),
        lambda item: item.__setitem__("survivor_relation", "independent scalar coefficient pairs"),
        lambda item: item.__setitem__("degree_two_interpretation", "same finite fibers"),
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
        print(f"CROSS_TYPE_SCALAR_PAIR_RIGIDITY_TAMPER_PASS mutations={tamper_selftest(data)}/10")
        return
    print(
        "CROSS_TYPE_SCALAR_PAIR_RIGIDITY_PASS "
        f"forced={checked['forced']} pair_cap={checked['pair_cap']} margin={checked['margin']}"
    )


if __name__ == "__main__":
    main()
