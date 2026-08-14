#!/usr/bin/env python3
"""Verify the fixed 31-anchor C/S/A/E router ledger."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "628ddcd210398c51695f6181677b43100ec58793d896f77bc3eb502d2366d1b8"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate_toy(toy: object) -> int:
    require(isinstance(toy, dict), "toy")
    p = toy.get("field")
    certificate = toy.get("certificate")
    scale = toy.get("projective_scale")
    require(
        (p, certificate, scale)
        == (
            17,
            {"Q": [2, 1], "A": [3, 4, 1], "B": [5, 0, 2], "c0": 6, "c1": 3},
            7,
        ),
        "toy pins",
    )
    scaled = {
        key: ([(scale * value) % p for value in item] if isinstance(item, list) else scale * item % p)
        for key, item in certificate.items()
    }
    inverse = pow(scale, -1, p)
    normalized = {
        key: ([(inverse * value) % p for value in item] if isinstance(item, list) else inverse * item % p)
        for key, item in scaled.items()
    }
    require(normalized == certificate, "projective normalization")
    return len(certificate["Q"]) - 1


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-anchor-star-sae-router-v1", "schema")
    row = data.get("official")
    require(isinstance(row, dict), "official")
    n, dimension, agreement, w = (row.get(k) for k in ("n", "K", "m", "w"))
    require((n, dimension, agreement, w) == (2097152, 1048576, 1116048, 67472), "row")
    require(row.get("near_charge") == 2 * w == 134944, "near charge")
    require(
        (
            row.get("dense_pair_owner_minimum"),
            row.get("dense_anchor_count"),
            row.get("off_line_anchor_count"),
            row.get("anchor_size"),
            row.get("tuple_size"),
            row.get("overlap_size"),
        )
        == (220, 18, 1, 31, 32, 31),
        "anchor constants",
    )
    schedule = data.get("anchor_schedule")
    require(isinstance(schedule, list) and len(schedule) == 10, "schedule")
    max_singles = 0
    for t, entry in enumerate(schedule, 1):
        if t <= 6:
            doubled = t
            singles = 0
            fillers = 31 - (18 + t + doubled)
        else:
            doubled = min(t, 14 - t) - 1
            singles = t - doubled
            fillers = 0
        used = 18 + t + doubled + fillers
        require(
            entry
            == {
                "basis_pairs": t,
                "doubled_pairs": doubled,
                "single_pairs": singles,
                "fillers": fillers,
                "used": used,
            },
            f"schedule {t}",
        )
        require(used == row.get("anchor_size"), f"anchor size {t}")
        max_singles = max(max_singles, singles)
    require(max_singles == row.get("single_basis_core_maximum") == 7, "single maximum")
    require(row.get("basis_pair_maximum") == 10, "basis maximum")
    common = row.get("heavy_core_intersection_maximum") + max_singles * row.get("theta_maximum")
    residual = dimension - common
    require(
        (common, residual)
        == (row.get("anchor_common_support_maximum"), row.get("anchor_residual_dimension_minimum"))
        == (1046362, 2214),
        "common core",
    )
    require(common < dimension, "strict cancellation")
    degree = (row.get("slope_degree_minimum"), row.get("slope_degree_maximum"))
    require(degree == (18, 31), "degree range")
    q = row.get("overlap_size")
    sunflower = (q * agreement - n + q - 2) // (q - 1)
    require(sunflower == row.get("near_sunflower_core_31") == 1083345, "sunflower core")
    require(
        sunflower - (agreement - dimension)
        == row.get("near_sunflower_noncollision_31")
        == 1015873,
        "sunflower noncollision",
    )
    require(
        data.get("route_labels")
        == [
            "C:local-maximal-common-support-residual",
            "S:primitive-spread-core",
            "A:coherent-rational-atom-owner",
            "E:pure-locator-or-named-exception",
        ],
        "route labels",
    )
    toy_degree = validate_toy(data.get("toy"))
    require("C is not folded into E" in str(data.get("nonclaim")), "nonclaim")
    return {"common": common, "singles": max_singles, "sunflower": sunflower, "toy": toy_degree}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["official"].__setitem__("anchor_size", 30),
        lambda item: item["official"].__setitem__("single_basis_core_maximum", 6),
        lambda item: item["official"].__setitem__("anchor_common_support_maximum", 1046363),
        lambda item: item["official"].__setitem__("near_sunflower_core_31", 1083344),
        lambda item: item["anchor_schedule"][9].__setitem__("doubled_pairs", 4),
        lambda item: item["route_labels"].pop(0),
        lambda item: item["toy"].__setitem__("projective_scale", 0),
    )
    controls = []
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            controls.append(True)
        else:
            controls.append(False)
    require(all(controls), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_ANCHOR_STAR_CSAE_ROUTER_PASS "
        f"core={result['common']} singles={result['singles']} "
        f"g31={result['sunflower']} toyQ={result['toy']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
