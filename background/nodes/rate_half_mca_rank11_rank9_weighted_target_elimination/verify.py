#!/usr/bin/env python3
"""Verify the repaired rank-nine weighted target boundary."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "28cfa4f50ea4ffa9a61888148c3916b0638906117d6efdbd2a779d8f4a925d94"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def demand_fraction(p: dict[str, int], k: int) -> tuple[int, int]:
    n, m = p["n_offset"] + k, p["m_offset"] + k
    numerator = (
        p["lane_density_numerator"]
        * p["residual_record_floor"]
        * comb(m, 9)
        * comb(m - 9, 2)
    )
    denominator = p["lane_density_denominator"] * comb(n, 9)
    return numerator, denominator


def weighted_cap(p: dict[str, int], k: int) -> int:
    n, m = p["n_offset"] + k, p["m_offset"] + k
    return (p["support_complement"] + 1) * (m - 10) * n


def row(p: dict[str, int], k: int) -> tuple[int, int, bool]:
    numerator, denominator = demand_fraction(p, k)
    cap = weighted_cap(p, k)
    return ceil_div(numerator, denominator), cap, numerator > cap * denominator


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-rank11-rank9-weighted-target-elimination-v2",
        "schema",
    )
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_component_ninesubset_target_router",
        "rate_half_mca_rank11_component_ninesubset_weighted_concentrator",
        "rate_half_mca_rank11_rank9_weighted_component_cap",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p["n_offset"] - p["m_offset"] == p["support_complement"] == 981104, "complement")
    require(p["last_open_dimension"] + 1 == p["first_closed_dimension"] == 20618, "boundary")
    require(p["reopened_interval"] == [10, 20617], "reopened interval")
    require(p["deleted_core_size_formula"] == "1048576-K_prime", "deleted core")

    last = row(p, p["last_open_dimension"])
    first = row(p, p["first_closed_dimension"])
    require((p["last_open_n"], p["last_open_m"]) == (1069193, 88089), "last row dimensions")
    require((p["first_closed_n"], p["first_closed_m"]) == (1069194, 88090), "first row dimensions")
    require(last == (p["last_open_demand"], p["last_open_cap"], False), "last open row")
    require(first == (p["first_closed_demand"], p["first_closed_cap"], True), "first closed row")
    require(p["last_open_gap"] == last[1] - last[0] == 7221289203362, "last gap")
    require(p["first_closed_gap"] == first[0] - first[1] == 2403530864991, "first gap")

    n, m = p["first_closed_n"], p["first_closed_m"]
    for i in range(9):
        require((m + 1 - i) * (n - i) > (m - i) * (n + 1 - i), f"factor {i}")
    require((m - 8) * n > (m - 9) * (n + 1), "final factor")
    require(p["deployed_dimension_maximum"] == 1048576, "deployed maximum")
    require("remains open" in str(data.get("nonclaim")), "nonclaim")
    return {"last_gap": last[1] - last[0], "first_gap": first[0] - first[1]}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("last_open_dimension", 20616),
        lambda item: item["parameters"].__setitem__("first_closed_dimension", 20617),
        lambda item: item["parameters"].__setitem__("last_open_gap", 7221289203361),
        lambda item: item["parameters"].__setitem__("first_closed_gap", 2403530864990),
        lambda item: item["parameters"].__setitem__("reopened_interval", [10, 20616]),
        lambda item: item["parameters"].__setitem__("deleted_core_size_formula", "0"),
        lambda item: item["parameters"].__setitem__("lane_density_numerator", 495405466),
        lambda item: item.__setitem__("nonclaim", "all rows closed"),
    )
    caught = 0
    for mutation in mutations:
        changed = copy.deepcopy(data)
        mutation(changed)
        try:
            validate(changed)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "hostile mutations")
    print(
        "RATE_HALF_MCA_RANK11_RANK9_WEIGHTED_TARGET_ELIMINATION_PASS "
        f"last_gap={result['last_gap']} first_gap={result['first_gap']} "
        f"reopened=10..20617 controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
