#!/usr/bin/env python3
"""Verify the dimension-three projective-image degree router."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "7db36df8a696c4ad7a415b2c9e0933e395d6fe44845ee0c3bc2f2116dc6b0c03"


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
            "rate-half-mca-rank11-dimension-three-projective-image-degree-router-v1",
            "schema")
    kmin = data.get("residual_dimension_floor")
    kmax = data.get("residual_dimension_ceiling")
    c0 = data.get("full_owner_floor_constant")
    c1 = data.get("full_owner_floor_slope")
    owner_cap = data.get("owner_multiplicity_ceiling")
    delta0 = data.get("occupancy_deficit_constant")
    delta1 = data.get("occupancy_deficit_slope")
    require((kmin, kmax, c0, c1, owner_cap, delta0, delta1) ==
            (4960, 4982, -13661092, 2953, 218, 14709668, -2952),
            "input pins")
    require(data.get("projective_image_degree_floor") == 2, "image floor")
    require(data.get("higher_image_degree_floor") == 3, "higher image floor")

    conic_rows = []
    higher_rows = []
    gcd_rows = []
    for kprime in range(kmin, kmax + 1):
        full = c0 + c1 * kprime
        deficit = delta0 + delta1 * kprime
        gcd_roots = deficit // owner_cap
        raw_roots = kprime - 2609
        primitive_roots = raw_roots - gcd_roots
        conic_e = (kprime - 1) // 2
        higher_e = (kprime - 1) // 3
        conic_rows.append((kprime, conic_e, ceil_div(full, conic_e)))
        higher_rows.append((kprime, higher_e, ceil_div(full, higher_e)))
        gcd_rows.append((kprime, deficit, gcd_roots, raw_roots,
                         primitive_roots, ceil_div(primitive_roots, 2)))

    require(gcd_rows[0] == (4960, 67748, 310, 2351, 2041, 1021),
            "gcd first row")
    require(gcd_rows[-1] == (4982, 2804, 12, 2373, 2361, 1181),
            "gcd last row")
    require(data.get("raw_direction_root_floor_first_row") == 2351,
            "raw root first")
    require(data.get("raw_direction_root_floor_last_row") == 2373,
            "raw root last")
    require(data.get("common_gcd_domain_root_ceiling_first_row") == 310,
            "gcd root first")
    require(data.get("common_gcd_domain_root_ceiling_last_row") == 12,
            "gcd root last")
    require(data.get("primitive_direction_root_floor_first_row") == 2041,
            "primitive root first")
    require(data.get("primitive_direction_root_floor_last_row") == 2361,
            "primitive root last")
    require(min(row[5] for row in gcd_rows) ==
            data.get("conic_map_degree_floor") == 1021,
            "conic degree floor")
    require(conic_rows[-1][1] ==
            data.get("conic_map_degree_ceiling") == 2490,
            "conic degree ceiling")
    require(conic_rows[0] == (4960, 2479, 398), "conic first row")
    require(conic_rows[-1] == (4982, 2490, 422), "conic last row")
    require(data.get("conic_normal_floor_first_row") == 398,
            "conic first normal")
    require(data.get("conic_normal_floor_last_row") == 422,
            "conic last normal")

    require(max(row[1] for row in higher_rows) ==
            data.get("higher_image_map_degree_ceiling") == 1660,
            "higher map ceiling")
    require(higher_rows[0] == (4960, 1653, 597), "higher first row")
    require(higher_rows[-1] == (4982, 1660, 633), "higher last row")
    require(data.get("higher_image_normal_floor_first_row") == 597,
            "higher first normal")
    require(data.get("higher_image_normal_floor_last_row") == 633,
            "higher last normal")
    require(all(conic_rows[i][2] <= conic_rows[i + 1][2]
                for i in range(len(conic_rows) - 1)), "conic monotonicity")
    require(all(higher_rows[i][2] <= higher_rows[i + 1][2]
                for i in range(len(higher_rows) - 1)), "higher monotonicity")
    require("not" in str(data.get("nonclaim")).lower() or
            "neither" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for parent in (
        "rate_half_mca_rank11_pair_pencil_coprime_direction_normal_form",
        "rate_half_mca_rank11_pair_pencil_dimension_three_common_core_shortening",
        "rate_half_mca_rank11_pair_pencil_dimension_three_type_population_ceiling",
        "rate_half_mca_rank11_pair_pencil_dimension_three_population_endpoint_direction_saturation",
    ):
        require(nodes.get(parent, {}).get("status") == "PROVED", f"dependency {parent}")
    return {
        "conic_first": conic_rows[0][2],
        "conic_last": conic_rows[-1][2],
        "higher_first": higher_rows[0][2],
        "higher_last": higher_rows[-1][2],
        "gcd": gcd_rows[0][2],
        "primitive": gcd_rows[0][4],
    }


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("owner_multiplicity_ceiling", 217),
        lambda item: item.__setitem__("occupancy_deficit_constant", 14709667),
        lambda item: item.__setitem__("common_gcd_domain_root_ceiling_first_row", 309),
        lambda item: item.__setitem__("primitive_direction_root_floor_first_row", 2040),
        lambda item: item.__setitem__("projective_image_degree_floor", 1),
        lambda item: item.__setitem__("conic_map_degree_floor", 1020),
        lambda item: item.__setitem__("conic_map_degree_ceiling", 2491),
        lambda item: item.__setitem__("conic_normal_floor_first_row", 397),
        lambda item: item.__setitem__("conic_normal_floor_last_row", 421),
        lambda item: item.__setitem__("higher_image_degree_floor", 4),
        lambda item: item.__setitem__("higher_image_map_degree_ceiling", 1661),
        lambda item: item.__setitem__("higher_image_normal_floor_first_row", 596),
        lambda item: item.__setitem__("higher_image_normal_floor_last_row", 632),
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
        print(f"RANK11_D3_IMAGE_DEGREE_TAMPER_PASS mutations={tamper_selftest(data)}/13")
        return
    print(
        "RANK11_D3_IMAGE_DEGREE_PASS "
        f"conic_normals={checked['conic_first']}..{checked['conic_last']} "
        f"higher_normals={checked['higher_first']}..{checked['higher_last']} "
        f"gcd_roots<={checked['gcd']} primitive_roots>={checked['primitive']}"
    )


if __name__ == "__main__":
    main()
