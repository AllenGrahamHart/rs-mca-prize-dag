#!/usr/bin/env python3
"""Verify the fixed rank-eight chart local-cap fence."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "553bbf5c9ba10d97f220480d50aea1dd7017407ddd833459f513992b97667093"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-rank8-fixed-chart-local-cap-fence-v1",
        "schema",
    )
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_component_ninesubset_target_router",
        "rate_half_mca_rank11_component_ninesubset_weighted_concentrator",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")

    n, k, m, w = p["n"], p["K"], p["m"], p["w"]
    require((n, k, m, w) == (2097152, 1048576, 1116048, 67472), "row")
    require(n - k == 1048576 and m - k == w, "row identities")
    kr = p["residual_K"]
    deleted = k - kr
    nr, mr = n - deleted, m - deleted
    require(kr == 11, "residual dimension")
    require(p["deleted_common_core"] == deleted == 1048565, "deleted core")
    require((p["residual_n"], p["residual_m"]) == (nr, mr) == (1048587, 67483), "residual row")

    require(p["correction_dimension"] == 10, "correction dimension")
    require(p["fixed_selector_size"] == 9, "selector size")
    require(p["evaluation_rank_on_selector"] == 8, "selector rank")
    require(p["kernel_dimension"] == 2, "kernel dimension")
    require(p["component_tuple_size"] == 11, "component tuple")
    require(8 + p["kernel_dimension"] == p["correction_dimension"], "rank-nullity")

    owners = p["owner_count"]
    petal = mr - 1 - p["fixed_selector_size"]
    remainder = nr - p["fixed_selector_size"] - owners * petal
    slopes = owners * remainder
    require((owners, petal, remainder) == (8, 67473, 508794), "partition")
    require(p["petal_size"] == petal, "petal")
    require(p["remainder_size"] == remainder, "remainder")
    require(p["rich_slope_count"] == slopes == 4070352, "slopes")
    require(p["fixed_selector_size"] + owners * petal + remainder == nr, "partition sum")
    require(p["fixed_selector_size"] + petal + 1 == mr, "exact support")
    require(slopes > p["fixed_selector_population_floor"] == 2578110, "distinct fence")

    extensions = comb(petal, 2)
    marked = slopes * extensions
    require(p["component_extensions_per_record"] == extensions == 2276269128, "extensions")
    require(p["marked_component_weight"] == marked == 9265216597693056, "marked weight")
    numerator = 55 * 495405467 * 274980728111260126 * comb(mr, 11)
    denominator = 10**9 * comb(nr, 9)
    demand = (numerator + denominator - 1) // denominator
    require(p["weighted_selector_demand"] == demand == 5869376383979174, "weighted demand")
    require(marked > demand, "weighted fence")

    forbidden = 64 * (remainder - 1) + owners * p["forbidden_slope_count"]
    require(p["maximum_greedy_forbidden_values"] == forbidden == 32562896, "greedy count")
    require(p["base_prime"] == 2130706433 and p["field_degree"] == 6, "field")
    require(p["base_prime"] > forbidden, "greedy field budget")

    residual_core = p["fixed_selector_size"] + petal
    require(p["residual_owner_core_size"] == residual_core == mr - 1, "residual core")
    require(residual_core > kr - 1, "residual root bound")
    lifted_core = deleted + residual_core
    require(p["lifted_owner_core_size"] == lifted_core == m - 1, "lifted core")
    require(deleted + mr == m and deleted + nr == n, "lift identities")
    require(p["error_affine_rank_ceiling"] == 2 < 3, "error rank")
    require("not a realization of the dense-anchor ancestors" in str(data.get("nonclaim")), "nonclaim")

    return {
        "slopes": slopes,
        "distinct_excess": slopes - p["fixed_selector_population_floor"],
        "marked": marked,
        "weighted_excess": marked - demand,
    }


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("residual_K", 10),
        lambda item: item["parameters"].__setitem__("evaluation_rank_on_selector", 9),
        lambda item: item["parameters"].__setitem__("owner_count", 7),
        lambda item: item["parameters"].__setitem__("remainder_size", 508793),
        lambda item: item["parameters"].__setitem__("rich_slope_count", 2578110),
        lambda item: item["parameters"].__setitem__("component_extensions_per_record", 2276269127),
        lambda item: item["parameters"].__setitem__("marked_component_weight", 5869376383979174),
        lambda item: item["parameters"].__setitem__("weighted_selector_demand", 5869376383979175),
        lambda item: item["parameters"].__setitem__("maximum_greedy_forbidden_values", 2130706433),
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
        "RATE_HALF_MCA_RANK11_RANK8_FIXED_CHART_LOCAL_CAP_FENCE_PASS "
        f"slopes={result['slopes']} distinct_excess={result['distinct_excess']} "
        f"marked={result['marked']} weighted_excess={result['weighted_excess']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
