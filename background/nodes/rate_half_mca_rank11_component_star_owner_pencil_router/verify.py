#!/usr/bin/env python3
"""Verify component-star owner-pencil endpoint arithmetic."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "23894520514168a69e1de5e638705c2036c6303e678bd295c124fe4278a917f7"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_ratio(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def extension_count(K: int, d: int = 67472) -> int:
    return ceil_ratio(98 * (d + K - 10), 100)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-component-star-owner-pencil-router-v1", "schema")
    require(data.get("dependencies") == ["rate_half_mca_rank11_dense_locator_component_incidence_dichotomy"], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p["component_incidence_ppb"] == 990810934, "component density")
    require(p["record_threshold_percent"] == 98, "threshold")
    fraction_ppb = (p["component_incidence_ppb"] - 980000000) * 50
    require(fraction_ppb == p["record_fraction_ppb"] == 540546700, "record fraction")
    absolute = ceil_ratio(p["non_dense_record_floor"] * fraction_ppb, 10**9)
    require(absolute == p["threshold_record_floor"] == 148639925144138894, "record floor")
    require((p["space_dimension"], p["tuple_size"]) == (10, 11), "dimensions")
    K_max = p["K_max"]
    m_max = p["d"] + K_max
    deficiency = (2 * (m_max - 10)) // 100
    require(deficiency == p["full_rank_owner_deficiency_ceiling"] == 22320, "deficiency")
    pencil = extension_count(K_max, p["d"]) - (K_max - 11)
    require(pencil == p["rank9_pencil_extension_floor"] == 45153, "pencil floor")
    for K in (10, 11, 12, 4923, K_max):
        require(extension_count(K, p["d"]) - max(0, K - 11) >= pencil, f"pencil sample {K}")
    require(p["low_rank_kernel_dimension_floor"] == 2, "kernel")
    require(data.get("routes") == ["LARGE_AFFINE_OWNER", "RANK9_OWNER_PENCIL", "KERNEL_PLANE"], "routes")
    require(len(data.get("logical_pins", [])) == 5, "logical pins")
    upstream = data.get("upstream_reconciliation")
    require(isinstance(upstream, dict) and upstream.get("open_pr") == 1169, "upstream")
    require("not aggregated" in str(data.get("nonclaim")), "nonclaim")
    return {"records": absolute, "pencil": pencil}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("record_fraction_ppb", 540546701),
        lambda item: item["parameters"].__setitem__("threshold_record_floor", 148639925144138893),
        lambda item: item["parameters"].__setitem__("full_rank_owner_deficiency_ceiling", 22319),
        lambda item: item["parameters"].__setitem__("rank9_pencil_extension_floor", 45152),
        lambda item: item["parameters"].__setitem__("low_rank_kernel_dimension_floor", 1),
        lambda item: item["routes"].pop(),
        lambda item: item["upstream_reconciliation"].__setitem__("open_pr", 1168),
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
        "RATE_HALF_MCA_RANK11_COMPONENT_STAR_OWNER_PENCIL_ROUTER_PASS "
        f"records={result['records']} pencil={result['pencil']} controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
