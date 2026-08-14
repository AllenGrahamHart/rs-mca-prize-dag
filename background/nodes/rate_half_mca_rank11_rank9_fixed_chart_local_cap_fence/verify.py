#!/usr/bin/env python3
"""Verify the fixed rank-nine chart local-cap fence."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "1cb156081477cb7438193899419d8c537054a9ee4570d5f6fdb5ec03868cdeca"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-rank9-fixed-chart-local-cap-fence-v1",
        "schema",
    )
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_component_ninesubset_target_router",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    n, k, m, w = p["n"], p["K"], p["m"], p["w"]
    require((n, k, m, w) == (2097152, 1048576, 1116048, 67472), "row")
    require(n - k == 1048576 and m - k == w, "row identities")
    require((p["correction_dimension"], p["fixed_selector_size"]) == (10, 9), "dimensions")
    require(p["evaluation_rank_on_selector"] == 9, "selector rank")
    require(p["component_tuple_size"] == 11, "tuple size")
    j = k - 1
    outside = n - j
    support = m - j
    require(p["common_core_size"] == j, "common core")
    require(p["outside_coordinate_weight"] == outside == 1048577, "outside")
    require(p["outside_support_weight"] == support == 67473, "support")
    owners = p["heavy_owner_count"]
    heavy = support - 1
    light = outside - owners * heavy
    slopes = owners * light
    require((owners, heavy, light) == (8, 67472, 508801), "owner weights")
    require(p["heavy_owner_weight"] == heavy, "heavy weight")
    require(p["unit_owner_count"] == light, "light owners")
    require(p["rich_slope_count"] == slopes == 4070408, "slope count")
    require(j + heavy + 1 == m, "exact support")
    require(j + heavy == m - 1, "pair noncontainment")
    require(m - 1 > k - 1, "pair noncontainment root bound")
    require(slopes > p["fixed_selector_population_floor"] == 2578110, "fence")
    require(p["base_prime"] > slopes, "distinct differences")
    require(p["base_prime"] > p["forbidden_slope_count"] * slopes, "avoidance translate")
    require(p["error_affine_rank_ceiling"] == 2, "error rank")
    require("not a realization of the dense-anchor ancestors" in str(data.get("nonclaim")), "nonclaim")
    return {"slopes": slopes, "excess": slopes - p["fixed_selector_population_floor"]}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("common_core_size", 1048574),
        lambda item: item["parameters"].__setitem__("heavy_owner_count", 7),
        lambda item: item["parameters"].__setitem__("unit_owner_count", 508800),
        lambda item: item["parameters"].__setitem__("rich_slope_count", 2578110),
        lambda item: item["parameters"].__setitem__("evaluation_rank_on_selector", 8),
        lambda item: item["parameters"].__setitem__("error_affine_rank_ceiling", 3),
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
        "RATE_HALF_MCA_RANK11_RANK9_FIXED_CHART_LOCAL_CAP_FENCE_PASS "
        f"slopes={result['slopes']} excess={result['excess']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
