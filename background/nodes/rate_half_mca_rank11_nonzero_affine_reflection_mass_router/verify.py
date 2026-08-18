#!/usr/bin/env python3
"""Verify the nonzero affine-reflection mass router."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "d85fb9f733083381b0e8137972dfd8562fcc1646c80abae355fa27f9bd1593a8"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-nonzero-affine-reflection-mass-router-v1",
        "schema",
    )
    mass, types, threshold, small, cap = (
        data.get("triple_owner_mass"),
        data.get("maximum_pair_types"),
        data.get("synchronization_threshold"),
        data.get("maximum_small_type_records"),
        data.get("nonzero_affine_fixed_pencil_cap"),
    )
    require((mass, types, threshold, small, cap) == (322359637, 58361, 29, 28, 1154), "pins")
    charge = max(small, cap)
    require(charge == data.get("uniform_pair_type_charge") == 1154, "uniform charge")
    total_charge = types * charge
    residual = mass - total_charge
    require(total_charge == data.get("total_affine_or_small_charge") == 67348594, "total charge")
    require(residual == data.get("nonaffine_residual_mass") == 255011043, "residual")
    quotient, remainder = divmod(residual, types)
    require(
        (quotient, remainder)
        == (data.get("residual_division_quotient"), data.get("residual_division_remainder"))
        == (4369, 31834),
        "division",
    )
    forced = quotient + int(remainder > 0)
    require(forced == data.get("forced_residual_pair_records") == 4370, "pigeonhole")
    require(forced >= threshold, "residual synchronization")
    require(data.get("high_complexity_threshold") == 2299571, "chi")
    require(len(data.get("remaining_classes", [])) == 5, "remaining classes")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    dependencies = (
        "rate_half_mca_rank11_multi_anchor_exchange_split_pencil_synchronization",
        "rate_half_mca_rank11_exception_spi_affine_reflection_fixed_pencil_cap",
        "rate_half_mca_rank11_heavy_ruling_triple_owner_pole_simple_router",
    )
    require(all(nodes.get(dep, {}).get("status") == "PROVED" for dep in dependencies), "dependencies")
    require("does not pay" in str(data.get("nonclaim")).lower(), "nonclaim")
    return {"charge": total_charge, "residual": residual, "forced": forced}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("triple_owner_mass", 322359636),
        lambda item: item.__setitem__("maximum_pair_types", 58362),
        lambda item: item.__setitem__("synchronization_threshold", 28),
        lambda item: item.__setitem__("maximum_small_type_records", 29),
        lambda item: item.__setitem__("nonzero_affine_fixed_pencil_cap", 1155),
        lambda item: item.__setitem__("total_affine_or_small_charge", 67348593),
        lambda item: item.__setitem__("nonaffine_residual_mass", 255011042),
        lambda item: item.__setitem__("forced_residual_pair_records", 4369),
        lambda item: item.__setitem__("nonclaim", "pays the residual"),
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
        print(f"RANK11_AFFINE_MASS_ROUTER_TAMPER_PASS mutations={tamper_selftest(data)}/9")
        return
    print(
        "RANK11_AFFINE_MASS_ROUTER_PASS "
        f"charge={checked['charge']} residual={checked['residual']} forced={checked['forced']}"
    )


if __name__ == "__main__":
    main()
