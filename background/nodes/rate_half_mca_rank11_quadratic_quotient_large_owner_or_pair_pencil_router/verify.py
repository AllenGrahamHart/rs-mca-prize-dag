#!/usr/bin/env python3
"""Verify the quadratic quotient large-owner/pair-pencil router."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "2ebb18038873432107abdbd56f789a5b40d508e69afc0f9001250653507dffd9"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-quadratic-quotient-large-owner-or-pair-pencil-router-v1",
        "schema",
    )
    mass = data.get("residual_mass")
    types = data.get("quotient_type_floor")
    large_floor = data.get("large_type_record_floor")
    small_cap = data.get("small_owner_record_cap")
    small_owner = data.get("small_owner_max")
    first_large = data.get("first_large_owner")
    require((mass, types, large_floor) == (255011043, 520, 29), "population pins")
    require(data.get("high_complexity_floor") == 2299571, "complexity")
    require(small_cap == 2097152 and mass > small_cap, "owner cap contradiction")
    require((small_owner, first_large) == (1183520, 1183521), "owner threshold")
    require(data.get("generic_output") == "one record-covering pole-simple atom with a large owner", "generic")
    require(data.get("degenerate_output") == "pair-type rank at most two over F(X)", "degenerate")
    require("neither" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for dependency in (
        "rate_half_mca_rank11_quadratic_quotient_population_router",
        "rate_half_mca_rank11_cross_type_atom_weld_gauge_dichotomy",
        "rate_half_mca_rank11_cross_type_global_atom_record_extension",
        "rate_half_mca_rank11_pole_simple_small_owner_atom_payment_import",
    ):
        require(nodes.get(dependency, {}).get("status") == "PROVED", f"dependency {dependency}")
    return {"mass": mass, "types": types, "first_large": first_large}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("residual_mass", 255011042),
        lambda item: item.__setitem__("quotient_type_floor", 519),
        lambda item: item.__setitem__("large_type_record_floor", 28),
        lambda item: item.__setitem__("small_owner_record_cap", 255011043),
        lambda item: item.__setitem__("small_owner_max", 1183519),
        lambda item: item.__setitem__("first_large_owner", 1183520),
        lambda item: item.__setitem__("generic_output", "one atom"),
        lambda item: item.__setitem__("degenerate_output", "pair-type rank at most three over F(X)"),
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
        print(f"QUOTIENT_LARGE_OWNER_OR_PAIR_PENCIL_TAMPER_PASS mutations={tamper_selftest(data)}/8")
        return
    print(
        "QUOTIENT_LARGE_OWNER_OR_PAIR_PENCIL_PASS "
        f"mass={checked['mass']} types={checked['types']} owner={checked['first_large']}"
    )


if __name__ == "__main__":
    main()
