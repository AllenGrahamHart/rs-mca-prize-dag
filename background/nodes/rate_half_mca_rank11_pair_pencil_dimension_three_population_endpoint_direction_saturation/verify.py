#!/usr/bin/env python3
"""Verify the q=3170 aggregate direction-saturation bank."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from fractions import Fraction
from math import comb, gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "ffbc2eaed1d0d6d1a495ba685ed7bce7d0ad87e8de4864dfe31ff63aa99ec260"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") ==
            "rate-half-mca-rank11-dimension-three-population-endpoint-direction-saturation-v1",
            "schema")
    q = data.get("type_population")
    kmin = data.get("residual_dimension_floor")
    kmax = data.get("residual_dimension_ceiling")
    c0 = data.get("full_owner_floor_constant")
    c1 = data.get("full_owner_floor_slope")
    directions = data.get("directions_per_full_plane_floor")
    line = data.get("selected_line_size")
    require((q, kmin, kmax, c0, c1, directions, line,
             data.get("pairs_per_saturated_line")) ==
            (3170, 4960, 4982, -13661092, 2953, 210, 15, 105),
            "input pins")

    pair_currency = comb(q, 2)
    rmax = pair_currency // comb(line, 2)
    require(data["direction_population_ceiling"] == rmax == 47836,
            "direction ceiling")
    rows = []
    for kprime in range(kmin, kmax + 1):
        full = c0 + c1 * kprime
        root_incidence = directions * full
        rmin = ceil_div(root_incidence, kprime - 1)
        deficit = rmax * (kprime - 1) - root_incidence
        rows.append((rmin, deficit, root_incidence, rmax * (kprime - 1)))
    require(rows[0][0] == data["direction_population_floor"] == 41746,
            "direction floor")
    require(rows[-1][0] == data["direction_population_upper_row_floor"] == 44301,
            "direction upper-row floor")
    require(max(item[1] for item in rows) ==
            data["aggregate_degree_deficit_ceiling"] == 30203244,
            "aggregate deficit")
    require(rows[0] == (41746, 30203244, 207015480, 237218724),
            "first row")
    require(rows[-1] == (44301, 17612776, 220658340, 238271116),
            "last row")

    numerator, denominator = rows[0][2], rows[0][3]
    divisor = gcd(numerator, denominator)
    require((data["saturation_numerator"], data["saturation_denominator"]) ==
            (numerator // divisor, denominator // divisor) ==
            (5750430, 6589409), "saturation fraction")
    require(Fraction(numerator, denominator) > Fraction(8726, 10000),
            "saturation decimal")
    root_floor = kmin - 2609
    require(data["individual_direction_root_floor"] == root_floor == 2351,
            "individual root floor")
    require("not classified or paid" in str(data.get("nonclaim")).lower(),
            "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for parent in (
        "rate_half_mca_rank11_pair_pencil_dimension_three_population_endpoint_plane_line_design",
        "rate_half_mca_rank11_pair_pencil_plane218_projective_direction_bank",
    ):
        require(nodes.get(parent, {}).get("status") == "PROVED", f"dependency {parent}")
    return {"rmin": rows[0][0], "rmax": rmax, "root": root_floor,
            "deficit": max(item[1] for item in rows)}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("directions_per_full_plane_floor", 209),
        lambda item: item.__setitem__("pairs_per_saturated_line", 104),
        lambda item: item.__setitem__("direction_population_floor", 41745),
        lambda item: item.__setitem__("direction_population_ceiling", 47837),
        lambda item: item.__setitem__("individual_direction_root_floor", 2350),
        lambda item: item.__setitem__("aggregate_degree_deficit_ceiling", 30203243),
        lambda item: item.__setitem__("saturation_numerator", 5750429),
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
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256,
            "contract hash")
    data = json.loads(CONTRACT.read_text())
    checked = validate(data)
    if args.tamper_selftest:
        print(f"RANK11_D3_DIRECTION_SAT_TAMPER_PASS mutations={tamper_selftest(data)}/7")
        return
    print(
        "RANK11_D3_DIRECTION_SAT_PASS "
        f"directions={checked['rmin']}..{checked['rmax']} "
        f"root={checked['root']} deficit={checked['deficit']}"
    )


if __name__ == "__main__":
    main()
