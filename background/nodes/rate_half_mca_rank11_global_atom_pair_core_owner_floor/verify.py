#!/usr/bin/env python3
"""Verify the global-atom pair-core owner floor."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "deaebba8de032ae673d53863d29d5b57610dc35c09a6098c1fa6b28f31f58e20"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_fraction(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-rank11-global-atom-pair-core-owner-floor-v1",
        "schema",
    )
    n, m, K = data.get("n"), data.get("m"), data.get("K")
    q = data.get("quotient_type_floor")
    anchors = data.get("anchor_supports")
    s = data.get("pair_core_size")
    c = data.get("pair_intersection_cap")
    require((n, m, K) == (2097152, 1116048, 1048576), "official row")
    require((q, anchors, s, c) == (520, 18, m - 2, K - 1), "core pins")
    require(anchors >= 2, "pole exclusion multiplicity")
    bound = Fraction(q * s * s, s + (q - 1) * c)
    require(data.get("union_numerator") == bound.numerator, "numerator")
    require(data.get("union_denominator") == bound.denominator, "denominator")
    owner = ceil_fraction(bound)
    generic = 2 * m - K + 1
    require(data.get("owner_floor") == owner == 1187712, "owner floor")
    require(data.get("generic_large_owner_floor") == generic == 1183521, "generic floor")
    require(data.get("improvement") == owner - generic == 4191, "improvement")
    require("not proved" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for dependency in (
        "rate_half_mca_rank11_quadratic_quotient_population_router",
        "rate_half_mca_rank11_cross_type_degree18_atom_weld_compiler",
        "rate_half_mca_rank11_cross_type_global_atom_record_extension",
    ):
        require(nodes.get(dependency, {}).get("status") == "PROVED", f"dependency {dependency}")
    return {"types": q, "owner": owner, "improvement": owner - generic}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("n", 2097151),
        lambda item: item.__setitem__("quotient_type_floor", 519),
        lambda item: item.__setitem__("anchor_supports", 1),
        lambda item: item.__setitem__("pair_core_size", 1116045),
        lambda item: item.__setitem__("pair_intersection_cap", 1048576),
        lambda item: item.__setitem__("union_numerator", 647690510540319),
        lambda item: item.__setitem__("owner_floor", 1187711),
        lambda item: item.__setitem__("improvement", 4190),
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
        print(f"GLOBAL_ATOM_PAIR_CORE_OWNER_FLOOR_TAMPER_PASS mutations={tamper_selftest(data)}/8")
        return
    print(
        "GLOBAL_ATOM_PAIR_CORE_OWNER_FLOOR_PASS "
        f"types={checked['types']} owner={checked['owner']} improvement={checked['improvement']}"
    )


if __name__ == "__main__":
    main()
