#!/usr/bin/env python3
"""Verify the 218-plane projective direction bank."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "7c94cac28f465b7f62128dc013b41851eb37c98605f53244244c724aaa0db8db"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-pair-pencil-plane218-projective-direction-bank-v1",
        "schema",
    )
    n, m, K, s = data.get("n"), data.get("m"), data.get("K"), data.get("pair_core_size")
    t, line = data.get("plane_occupancy"), data.get("line_cap")
    require((n, m, K, s, t, line) == (2097152, 1116048, 1048576, m - 2, 218, 15), "pins")
    cmin = ceil_div(t * s - line * n, t - line)
    require(data.get("plane_core_floor") == cmin == 1043551, "core floor")
    kmax = K - cmin
    require(data.get("shortened_K_ceiling") == kmax == 5025, "K ceiling")
    fconst = data.get("full_coordinate_floor_constant")
    fslope = data.get("full_coordinate_floor_slope")
    require((fconst, fslope) == (28396, 204), "full floor")
    lines = (t * ((t - 1) // (line - 1))) // line
    require(data.get("full_line_ceiling") == lines == 218, "line ceiling")
    kmin = ceil_div(fconst + lines, lines - fslope)
    require(data.get("shortened_K_floor") == kmin == 2044, "K floor")
    cmax = K - kmin
    require(data.get("plane_core_ceiling") == cmax == 1046532, "core ceiling")
    require(fconst + fslope * kmax > 209 * (kmax - 1), "210 directions")
    require(data.get("direction_floor") == 210, "direction floor")
    deficit = lines * (kmax - 1) - (fconst + fslope * kmax)
    require(data.get("aggregate_direction_deficit_ceiling") == deficit == 41736, "deficit")
    sat_num, sat_den = data.get("saturation_numerator"), data.get("saturation_denominator")
    g = math.gcd(fconst + fslope * kmax, lines * (kmax - 1))
    require((sat_num, sat_den) == ((fconst + fslope * kmax) // g, lines * (kmax - 1) // g) == (131687, 136904), "saturation")
    pairs = t * (t - 1) // 2 - 210 * line * (line - 1) // 2
    require(data.get("dual_rich_point_floor") == 210, "dual rich")
    require(data.get("dual_remaining_pair_ceiling") == pairs == 1603, "dual pairs")
    require("not excluded" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes.get("rate_half_mca_rank11_pair_pencil_affine_plane_cap_218_sharpening", {}).get("status") == "PROVED", "dependency")
    return {"kmin": kmin, "kmax": kmax, "directions": 210, "deficit": deficit}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("plane_occupancy", 217),
        lambda item: item.__setitem__("plane_core_floor", 1043550),
        lambda item: item.__setitem__("shortened_K_floor", 2043),
        lambda item: item.__setitem__("shortened_K_ceiling", 5024),
        lambda item: item.__setitem__("full_line_ceiling", 219),
        lambda item: item.__setitem__("direction_floor", 209),
        lambda item: item.__setitem__("aggregate_direction_deficit_ceiling", 41735),
        lambda item: item.__setitem__("dual_remaining_pair_ceiling", 1604),
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
        print(f"PAIR_PENCIL_PLANE218_BANK_TAMPER_PASS mutations={tamper_selftest(data)}/8")
        return
    print(
        "PAIR_PENCIL_PLANE218_BANK_PASS "
        f"K={checked['kmin']}..{checked['kmax']} "
        f"directions={checked['directions']} deficit={checked['deficit']}"
    )


if __name__ == "__main__":
    main()
