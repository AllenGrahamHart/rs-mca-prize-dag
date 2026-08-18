#!/usr/bin/env python3
"""Verify the quadratic quotient population router."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "ec7a5f0f4d30192ffd155c02c644d28c74c7e902c9eff425ff457e6976ca09e5"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-quadratic-quotient-population-router-v1",
        "schema",
    )
    n = data.get("official_domain_order")
    m = data.get("official_agreement")
    degree = data.get("exception_degree")
    residual = data.get("synchronized_residual_records")
    types = data.get("maximum_pair_types")
    cap = data.get("quotient_type_cap")
    require((n, m, degree, residual, types) == (2097152, 1116048, 2, 255011043, 58361), "pins")
    require(cap == (n - (m - degree)) // degree == 490553, "per-type cap")
    floor = ceil_div(residual, cap)
    require(data.get("quotient_only_type_floor") == floor == 520, "population floor")
    require(data.get("floor_predecessor_capacity") == (floor - 1) * cap == 254597007, "predecessor")
    require(data.get("floor_capacity") == floor * cap == 255087560, "capacity")

    qs = data.get("tradeoff_q")
    masses = data.get("tradeoff_other_mass")
    one_type = data.get("tradeoff_one_type_floor")
    require(isinstance(qs, list) and isinstance(masses, list) and isinstance(one_type, list), "tables")
    require(len(qs) == len(masses) == len(one_type) == 9, "table lengths")
    for q, mass, forced in zip(qs, masses, one_type):
        expected_mass = max(0, residual - q * cap)
        require(mass == expected_mass, f"mass q={q}")
        require(forced == ceil_div(expected_mass, types - q), f"one type q={q}")
    require("not an aggregate" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for dependency in (
        "rate_half_mca_rank11_nonzero_affine_reflection_mass_router",
        "rate_half_mca_rank11_quadratic_quotient_survivor_identification",
        "rate_half_mca_rank11_quadratic_quotient_factor_through_interface",
    ):
        require(nodes.get(dependency, {}).get("status") == "PROVED", f"dependency {dependency}")
    return {"cap": cap, "floor": floor, "rows": len(qs)}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("official_agreement", 1116047),
        lambda item: item.__setitem__("exception_degree", 3),
        lambda item: item.__setitem__("synchronized_residual_records", 255011042),
        lambda item: item.__setitem__("maximum_pair_types", 58360),
        lambda item: item.__setitem__("quotient_type_cap", 490552),
        lambda item: item.__setitem__("quotient_only_type_floor", 519),
        lambda item: item.__setitem__("floor_predecessor_capacity", 254597008),
        lambda item: item["tradeoff_other_mass"].__setitem__(4, 58789842),
        lambda item: item["tradeoff_one_type_floor"].__setitem__(7, 15),
    )
    caught = 0
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError, ZeroDivisionError):
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
        print(f"QUADRATIC_QUOTIENT_POPULATION_TAMPER_PASS mutations={tamper_selftest(data)}/9")
        return
    print(
        "QUADRATIC_QUOTIENT_POPULATION_PASS "
        f"cap={checked['cap']} floor={checked['floor']} rows={checked['rows']}"
    )


if __name__ == "__main__":
    main()
