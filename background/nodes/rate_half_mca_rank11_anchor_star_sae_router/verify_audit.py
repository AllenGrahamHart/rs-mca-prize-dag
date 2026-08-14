#!/usr/bin/env python3
"""Independent audit of the line-global-core C/S/A/E router."""

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


def audit(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    row = data.get("official")
    schedule = data.get("anchor_schedule")
    require(isinstance(row, dict) and isinstance(schedule, list), "records")
    require(row.get("global_common_support_maximum") == row.get("K") - 1, "global core")
    require(row.get("zero_core_anchor_intersection") == 0, "zero core")
    require(
        (row.get("deviation_dimension_minimum"), row.get("deviation_dimension_maximum")) == (1, 10),
        "deviation dimensions",
    )
    filler_profile = []
    for entry in schedule:
        r = entry.get("deviation_dimension")
        require(entry.get("basis_records") == r, "basis records")
        fillers = row.get("anchor_size") - row.get("dense_anchor_count") - r
        require(entry.get("fillers") == fillers, "fillers")
        require(row.get("dense_anchor_count") + r + fillers == entry.get("used") == 31, "used")
        filler_profile.append(fillers)
    require(filler_profile == list(range(12, 2, -1)), "filler profile")
    require(row.get("near_charge") == 2 * row.get("w"), "near")
    q, n, m = row.get("overlap_size"), row.get("n"), row.get("m")
    quotient, remainder = divmod(q * m - n, q - 1)
    g = quotient + bool(remainder)
    require(g == row.get("near_sunflower_core_31") == 1083345, "g31")
    require(g - (m - row.get("K")) == row.get("near_sunflower_noncollision_31"), "g31-d")
    routes = data.get("route_labels")
    require(
        isinstance(routes, list)
        and len(routes) == 4
        and routes[0].startswith("C:line-global")
        and all("zero-global-core" in route for route in routes[1:]),
        "route scopes",
    )

    toy = data.get("toy")
    require(isinstance(toy, dict) and toy.get("field") == 17, "toy")
    certificate = toy.get("certificate")
    scale = toy.get("projective_scale")
    require(certificate == {"Q": [2, 1], "A": [3, 4, 1], "B": [5, 0, 2], "c0": 6, "c1": 3}, "certificate")
    require(scale == 7, "scale pin")
    scaled_q = [(scale * x) % 17 for x in certificate["Q"]]
    ratio = scaled_q[0] * pow(certificate["Q"][0], -1, 17) % 17
    require(ratio == scale and ratio != 0, "projective ratio")
    require("remain unpaid" in str(data.get("nonclaim")), "scope")
    return {"basis": len(schedule), "g31": g, "routes": len(routes)}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = audit(data)
    controls = []
    for section, key, value in (
        ("official", "global_common_support_maximum", 1048576),
        ("official", "zero_core_anchor_intersection", 1),
        ("official", "deviation_dimension_minimum", 0),
        ("official", "overlap_size", 30),
        ("toy", "projective_scale", 0),
    ):
        altered = copy.deepcopy(data)
        altered[section][key] = value
        try:
            audit(altered)
        except (Reject, TypeError, ValueError):
            controls.append(True)
        else:
            controls.append(False)
    require(all(controls), "audit controls")
    print(
        "RATE_HALF_MCA_RANK11_ANCHOR_STAR_CSAE_ROUTER_AUDIT_PASS "
        f"basis={result['basis']} g31={result['g31']} routes={result['routes']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
