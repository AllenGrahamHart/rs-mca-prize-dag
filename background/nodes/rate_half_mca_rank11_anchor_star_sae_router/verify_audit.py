#!/usr/bin/env python3
"""Independent audit of the 31-anchor C/S/A/E router."""

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


def audit(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    row = data.get("official")
    schedule = data.get("anchor_schedule")
    require(isinstance(row, dict) and isinstance(schedule, list), "records")
    dense, size = row.get("dense_anchor_count"), row.get("anchor_size")
    singles_seen = []
    for entry in schedule:
        t = entry.get("basis_pairs")
        original_doubled = min(t, 14 - t)
        if dense + t + original_doubled < 32:
            doubled = original_doubled
            fillers = size - dense - t - doubled
        else:
            doubled = original_doubled - 1
            fillers = 0
        singles = t - doubled
        require(entry.get("doubled_pairs") == doubled, "doubled")
        require(entry.get("single_pairs") == singles, "singles")
        require(entry.get("fillers") == fillers, "fillers")
        require(dense + t + doubled + fillers == size == entry.get("used"), "used")
        singles_seen.append(singles)
    require(singles_seen == [0, 0, 0, 0, 0, 0, 1, 3, 5, 7], "single profile")
    require(row.get("theta_maximum") == 387, "theta")
    common = row.get("K") - 4923 + max(singles_seen) * row.get("theta_maximum")
    require(common == row.get("anchor_common_support_maximum") == row.get("K") - 2214, "core")
    require(row.get("K") - common == row.get("anchor_residual_dimension_minimum") == 2214, "residual")
    require(row.get("near_charge") == 2 * row.get("w"), "near")
    q, n, m = row.get("overlap_size"), row.get("n"), row.get("m")
    g, remainder = divmod(q * m - n, q - 1)
    g += bool(remainder)
    require(g == row.get("near_sunflower_core_31") == 1083345, "g31")
    require(g - (m - row.get("K")) == row.get("near_sunflower_noncollision_31"), "g31-d")
    routes = data.get("route_labels")
    require(isinstance(routes, list) and len(routes) == 4 and routes[0].startswith("C:"), "C route")

    toy = data.get("toy")
    require(isinstance(toy, dict) and toy.get("field") == 17, "toy")
    certificate = toy.get("certificate")
    scale = toy.get("projective_scale")
    require(certificate == {"Q": [2, 1], "A": [3, 4, 1], "B": [5, 0, 2], "c0": 6, "c1": 3}, "certificate")
    scaled_q = [(scale * x) % 17 for x in certificate["Q"]]
    ratio = scaled_q[0] * pow(certificate["Q"][0], -1, 17) % 17
    require(ratio == scale and ratio != 0, "projective ratio")
    for key in ("A", "B"):
        require([(ratio * x) % 17 for x in certificate[key]] == [(scale * x) % 17 for x in certificate[key]], key)
    require("not folded into E" in str(data.get("nonclaim")), "scope")
    return {"common": common, "g31": g, "routes": len(routes)}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = audit(data)
    controls = []
    for section, key, value in (
        ("official", "theta_maximum", 388),
        ("official", "anchor_residual_dimension_minimum", 2213),
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
    altered = copy.deepcopy(data)
    altered["route_labels"] = altered["route_labels"][1:]
    try:
        audit(altered)
    except Reject:
        controls.append(True)
    else:
        controls.append(False)
    require(all(controls), "audit controls")
    print(
        "RATE_HALF_MCA_RANK11_ANCHOR_STAR_CSAE_ROUTER_AUDIT_PASS "
        f"core={result['common']} g31={result['g31']} routes={result['routes']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
