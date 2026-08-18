#!/usr/bin/env python3
"""Verify the dimension-three quotient-type population ceiling."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "780248e2f3b8498f7ccc9e5dccf23f88e4dc7d154453c3df6adb5c844cf26373"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def terms(q: int, n0: int, s0: int, cap: int) -> tuple[int, int, int]:
    pair_cap = comb(cap, 2)
    p = comb(q, 2) - (cap - 1) * q + pair_cap
    b = (cap - 1) * q * s0 - pair_cap * n0 + comb(q, 2)
    a = cap * n0 - q * s0
    return p, b, a


def cross_twice(q: int, n0: int, s0: int, cap: int) -> int:
    p, b, a = terms(q, n0, s0, cap)
    return 2 * (p * a - b * (q - cap))


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") ==
            "rate-half-mca-rank11-dimension-three-type-population-ceiling-v1",
            "schema")
    mass = data.get("retained_record_mass")
    qmin = data.get("population_floor")
    cap = data.get("plane_occupancy_cap")
    n0 = data.get("residual_length_offset")
    s0 = data.get("residual_core_offset")
    require((mass, qmin, cap, n0, s0, data.get("pair_overlap_offset")) ==
            (255011043, 520, 218, 1048576, 67470, 1), "input pins")

    qmax = data.get("population_ceiling")
    require(qmax == 3170, "population ceiling")
    factor = lambda q: -data["factor_constant"] * q * (q - cap) * (
        data["factor_slope"] * q - data["factor_intercept"])
    require((data["factor_constant"], data["factor_slope"],
             data["factor_intercept"]) == (109, 619, 1962831), "factor pins")
    for q in (qmin, 3000, qmax, qmax + 1, 3387):
        require(cross_twice(q, n0, s0, cap) == factor(q), f"factor {q}")
    last_cross = cross_twice(qmax, n0, s0, cap)
    first_cross = cross_twice(qmax + 1, n0, s0, cap)
    require(last_cross == data["last_feasible_cross_product_twice"] ==
            613022740560, "last cross")
    require(first_cross == -data["first_excluded_cross_product_deficit_twice"] ==
            -18372095406, "first cross")
    require(619 * qmax - 1962831 == -601, "last sign")
    require(619 * (qmax + 1) - 1962831 == 18, "first sign")

    p, b, a = terms(qmax, n0, s0, cap)
    low_q, low_r = divmod(b, p)
    high_q, high_r = divmod(a, qmax - cap)
    require((p, low_q, low_r) == (4358628, 4959, 556785), "lower endpoint")
    require((high_q, high_r) == (4982, 2804), "upper endpoint")
    require(data["endpoint_residual_dimension_floor"] == low_q + 1 == 4960,
            "endpoint floor")
    require(data["endpoint_residual_dimension_ceiling"] == high_q == 4982,
            "endpoint ceiling")
    require(data["endpoint_pair_lower_remainder"] == low_r, "lower remainder")
    require(data["endpoint_plane_upper_remainder"] == high_r, "upper remainder")
    full_floor = n0 + (low_q + 1) - (a - (qmax - cap) * (low_q + 1))
    full_upper = n0 + high_q - (a - (qmax - cap) * high_q)
    require(data["endpoint_full_owner_coordinate_floor"] == full_floor == 985788,
            "full-owner floor")
    require(data["endpoint_upper_row_full_owner_coordinate_floor"] ==
            full_upper == 1050754, "full-owner upper row")
    dense = (mass + qmax - 1) // qmax
    require(data["dense_type_record_floor"] == dense == 80446, "dense owner")
    require("no dense type" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for parent in (
        "rate_half_mca_rank11_quadratic_quotient_population_router",
        "rate_half_mca_rank11_pair_pencil_affine_plane_cap_218_sharpening",
        "rate_half_mca_rank11_pair_pencil_dimension_three_pair_overlap_moment_floor",
    ):
        require(nodes.get(parent, {}).get("status") == "PROVED", f"dependency {parent}")
    return {"qmax": qmax, "dense": dense, "low": low_q + 1,
            "high": high_q, "full": full_floor, "deficit": -first_cross}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("retained_record_mass", 255011042),
        lambda item: item.__setitem__("plane_occupancy_cap", 217),
        lambda item: item.__setitem__("population_ceiling", 3171),
        lambda item: item.__setitem__("dense_type_record_floor", 80445),
        lambda item: item.__setitem__("endpoint_residual_dimension_floor", 4959),
        lambda item: item.__setitem__("endpoint_residual_dimension_ceiling", 4983),
        lambda item: item.__setitem__("endpoint_full_owner_coordinate_floor", 985787),
        lambda item: item.__setitem__("first_excluded_cross_product_deficit_twice", 18372095405),
        lambda item: item.__setitem__("factor_slope", 618),
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
        print(f"RANK11_D3_TYPE_POP_TAMPER_PASS mutations={tamper_selftest(data)}/9")
        return
    print(
        "RANK11_D3_TYPE_POP_PASS "
        f"qmax={checked['qmax']} dense={checked['dense']} "
        f"K={checked['low']}..{checked['high']} full={checked['full']} "
        f"deficit={checked['deficit']}"
    )


if __name__ == "__main__":
    main()
