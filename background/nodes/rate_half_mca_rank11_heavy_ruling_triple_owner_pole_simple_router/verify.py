#!/usr/bin/env python3
"""Verify the triple-owner pole-simple router."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "ce7ac51d33075bca9d5913e1b127a8ed598cd2a6b30bd50894fd2b8b975ae1f5"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-heavy-ruling-triple-owner-pole-simple-router-v1",
        "schema",
    )
    mass = data.get("orientation_mass")
    q4 = data.get("pair_type_cap")
    low_max = data.get("low_multiplicity_maximum")
    require((mass, q4, low_max) == (322476359, 58361, 2), "source pins")
    low_cap = low_max * q4
    triple_mass = mass - low_cap
    require(low_cap == data.get("low_multiplicity_record_cap") == 116722, "low cap")
    require(triple_mass == data.get("triple_owner_mass") == 322359637, "triple mass")

    q2 = data.get("rank_two_pair_type_cap")
    multiplicity = data.get("fixed_pair_multiplicity")
    triple_capacity = q2 * multiplicity
    total_capacity = triple_capacity + low_cap
    gap = mass - total_capacity
    require((q2, multiplicity) == (241, 981115), "dimension-two pins")
    require(triple_capacity == data.get("large_core_triple_capacity") == 236448715, "triple capacity")
    require(total_capacity == data.get("large_core_total_capacity") == 236565437, "total capacity")
    require(gap == data.get("large_core_gap") == 85910922 > 0, "capacity gap")
    dense = ceil_div(triple_mass, q4)
    require(dense == data.get("dense_triple_owner_minimum") == 5524, "dense pair")

    component_dimension = data.get("component_dimension")
    additional = data.get("maximum_additional_pair_types")
    per_pair = data.get("records_per_additional_pair")
    seed = data.get("seed_size")
    anchor = seed - per_pair * additional
    require((component_dimension, additional, per_pair, seed) == (4, 4, 3, 32), "selection")
    require(anchor == data.get("minimum_anchor_records") == 20, "anchor")
    require(dense >= anchor, "anchor supply")
    require(data.get("minimum_selected_pair_types") == 2, "pair floor")
    require(data.get("common_support_dimension_gap") == 3, "dimension gap")

    margin = data.get("pair_core_margin")
    excess = data.get("agreement_excess")
    root_surplus = excess - (2 * margin - 1)
    require((margin, excess) == (11, 67472), "core pins")
    require(root_surplus == data.get("two_core_root_surplus") == 67451, "root surplus")
    require(
        (data.get("minimum_slope_degree"), data.get("maximum_slope_degree"))
        == (anchor, seed - 1)
        == (20, 31),
        "degree pin",
    )
    denominator = data.get("denominator_degree_maximum")
    require(denominator == excess == 67472, "denominator")
    require(data.get("maximum_common_poles") == 0, "common poles")
    support_per_root = data.get("maximum_supports_per_denominator_root")
    incidences = denominator * support_per_root
    require(support_per_root == 1, "root support multiplicity")
    require(
        incidences == data.get("maximum_denominator_root_support_incidences") == 67472,
        "root incidences",
    )
    require(data.get("complexity_threshold") == 2299571, "complexity")

    selected_pair_types = additional + 1
    scalar_zero_allowance = 1
    forced_supports = selected_pair_types * per_pair - scalar_zero_allowance
    require(per_pair - scalar_zero_allowance >= 2, "two forced supports in exceptional pair")
    require(forced_supports == 14, "forced support toy")
    require("remain unpaid" in str(data.get("nonclaim")), "nonclaim")
    return {
        "triple_mass": triple_mass,
        "gap": gap,
        "dense": dense,
        "anchor": anchor,
        "pole_incidences": incidences,
    }


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("low_multiplicity_record_cap", 116721),
        lambda item: item.__setitem__("triple_owner_mass", 322359636),
        lambda item: item.__setitem__("large_core_total_capacity", 236565436),
        lambda item: item.__setitem__("large_core_gap", 85910921),
        lambda item: item.__setitem__("dense_triple_owner_minimum", 5523),
        lambda item: item.__setitem__("records_per_additional_pair", 2),
        lambda item: item.__setitem__("minimum_anchor_records", 19),
        lambda item: item.__setitem__("two_core_root_surplus", 67450),
        lambda item: item.__setitem__("maximum_common_poles", 1),
        lambda item: item.__setitem__("maximum_supports_per_denominator_root", 2),
        lambda item: item.__setitem__("maximum_denominator_root_support_incidences", 67471),
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
        print(f"RANK11_TRIPLE_OWNER_POLE_SIMPLE_TAMPER_PASS mutations={caught}/11")
        return
    print(
        "RANK11_TRIPLE_OWNER_POLE_SIMPLE_PASS "
        f"mass={result['triple_mass']} gap={result['gap']} dense={result['dense']} "
        f"anchor={result['anchor']} poles={result['pole_incidences']}"
    )


if __name__ == "__main__":
    main()
