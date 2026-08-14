#!/usr/bin/env python3
"""Verify the fixed rank-nine split-pencil cell ledger."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "150863c70ede9590605eaa93eb97a16da4edb6883d6ede80c60c1c12d9795cf3"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_ratio(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-rank9-split-pencil-cell-ledger-v1", "schema")
    require(data.get("dependencies") == ["rate_half_mca_rank11_component_star_owner_pencil_router"], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["cell_size"], p["cell_rank"], p["kernel_dimension"]) == (10, 9, 1), "cell")
    require(p["n_minus_k"] - p["m_minus_k"] == p["n_minus_m"] == 981104, "invariants")
    require(p["fixed_owner_slope_cap"] == p["n_minus_m"] + 1 == 981105, "owner cap")
    weighted = p["fixed_owner_slope_cap"] * (p["n_max"] - p["common_root_core_floor"])
    require(weighted == p["weighted_petal_incidence_cap"] == 2057516501910, "weighted cap")
    cell = ceil_ratio(weighted, p["extension_floor"])
    require(cell == p["fixed_cell_record_cap"] == 45567659, "cell cap")
    require(
        data.get("identities")
        == [
            "record_lines_have_distinct_slope_directions",
            "sum_choose_t_p_2_equals_choose_g_2",
            "owner_core_equals_common_root_core_disjoint_union_unique_petal",
            "sum_extension_incidences_at_most_sum_t_p_times_petal_size",
        ],
        "identities",
    )
    upstream = data.get("upstream_alignment")
    require(isinstance(upstream, dict) and upstream.get("acceptance_pr") == 1169, "upstream")
    require("cross-cell chronology" in str(data.get("nonclaim")), "nonclaim")
    return {"weighted": weighted, "cell": cell}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("cell_rank", 8),
        lambda item: item["parameters"].__setitem__("extension_floor", 45152),
        lambda item: item["parameters"].__setitem__("common_root_core_floor", 9),
        lambda item: item["parameters"].__setitem__("fixed_owner_slope_cap", 981104),
        lambda item: item["parameters"].__setitem__("fixed_cell_record_cap", 45567658),
        lambda item: item["identities"].pop(),
        lambda item: item["upstream_alignment"].__setitem__("acceptance_pr", 1168),
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
        "RATE_HALF_MCA_RANK11_RANK9_SPLIT_PENCIL_CELL_LEDGER_PASS "
        f"weighted={result['weighted']} cell={result['cell']} controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
