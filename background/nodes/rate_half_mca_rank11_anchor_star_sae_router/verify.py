#!/usr/bin/env python3
"""Verify the line-global-core plus fixed-anchor C/S/A/E router."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "57b1bee830274e9b76ed7a0372446d82d237752d1c6904b5c67195cefe971fa8"


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
    require(data.get("schema") == "rate-half-mca-rank11-anchor-star-sae-router-v2", "schema")
    require(
        data.get("dependencies")
        == [
            "rate_half_mca_rank11_dense_pair_degree18_seed_compiler",
            "rate_half_mca_rank11_shortened_partial_relative_router",
            "rate_half_mca_whole_line_global_core_router",
            "rate_half_mca_order32_partial_relative_harvest",
            "rate_half_mca_pole_tolerant_scalar_locator_harvest",
        ],
        "dependencies",
    )
    row = data.get("official")
    require(isinstance(row, dict), "official")
    n, dimension, agreement, w = (row.get(k) for k in ("n", "K", "m", "w"))
    require((n, dimension, agreement, w) == (2097152, 1048576, 1116048, 67472), "row")
    require(row.get("near_charge") == 2 * w == 134944, "near charge")
    require(
        (
            row.get("dense_pair_owner_minimum"),
            row.get("dense_anchor_count"),
            row.get("anchor_size"),
            row.get("tuple_size"),
            row.get("overlap_size"),
        )
        == (220, 18, 31, 32, 31),
        "anchor constants",
    )
    require(
        (
            row.get("deviation_dimension_minimum"),
            row.get("deviation_dimension_maximum"),
            row.get("global_common_support_maximum"),
            row.get("zero_core_anchor_intersection"),
        )
        == (1, 10, dimension - 1, 0),
        "global core and deviation range",
    )
    schedule = data.get("anchor_schedule")
    require(isinstance(schedule, list) and len(schedule) == 10, "schedule")
    for r, entry in enumerate(schedule, 1):
        fillers = 31 - 18 - r
        require(
            entry
            == {
                "deviation_dimension": r,
                "basis_records": r,
                "fillers": fillers,
                "used": 31,
            },
            f"schedule {r}",
        )
        require(18 + r + fillers == row.get("anchor_size"), "slot identity")
    require(
        (row.get("slope_degree_minimum"), row.get("slope_degree_maximum")) == (18, 31),
        "degree range",
    )
    q = row.get("overlap_size")
    sunflower = (q * agreement - n + q - 2) // (q - 1)
    require(sunflower == row.get("near_sunflower_core_31") == 1083345, "sunflower")
    require(
        sunflower - (agreement - dimension)
        == row.get("near_sunflower_noncollision_31")
        == 1015873,
        "noncollision core",
    )
    require(
        data.get("route_labels")
        == [
            "C:line-global-common-core-shortened-residual",
            "S:zero-global-core-primitive-spread",
            "A:zero-global-core-coherent-rational-atom-owner",
            "E:zero-global-core-pure-locator-or-named-exception",
        ],
        "route labels",
    )
    toy_degree = validate_toy(data.get("toy"))
    require("line-global C residual" in str(data.get("nonclaim")), "nonclaim")
    return {"basis": len(schedule), "sunflower": sunflower, "toy": toy_degree}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["official"].__setitem__("global_common_support_maximum", 1048576),
        lambda item: item["official"].__setitem__("zero_core_anchor_intersection", 1),
        lambda item: item["official"].__setitem__("deviation_dimension_maximum", 11),
        lambda item: item["anchor_schedule"][9].__setitem__("fillers", 2),
        lambda item: item["official"].__setitem__("near_sunflower_core_31", 1083344),
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
        f"basis={result['basis']} anchor=31 g31={result['sunflower']} "
        f"toyQ={result['toy']} controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
