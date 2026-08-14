#!/usr/bin/env python3
"""Verify the rank-drop payment and full-rank relative-core router."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "db4235553ac01335be6bb2daa03e3299735e8c882e40fd8d855527eb0e9e1eee"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def falling(value: int, length: int) -> int:
    out = 1
    for offset in range(length):
        out *= value - offset
    return out


def rising(value: int, length: int) -> int:
    out = 1
    for offset in range(length):
        out *= value + offset
    return out


def transversality_cap(R: int, d: int, dimension: int, rank: int) -> int:
    n = R + dimension
    m = d + dimension
    first = Fraction(
        falling(n, rank + 1),
        m * rising(d + 1, rank - 1),
    )
    second = Fraction(
        falling(R + rank, rank + 1),
        rising(d + 1, rank),
    )
    value = max(first, second)
    return value.numerator // value.denominator


def margin_split(
    R: int,
    d: int,
    dimension: int,
    rank: int,
    threshold: int,
    near: int,
    field_size: int,
) -> dict[str, int | bool]:
    n = R + dimension
    m = d + dimension
    agreement = m - threshold + 1
    residual = agreement - dimension
    ordinary = comb(R + rank, rank) // comb(residual + rank, rank)
    caps = [n // threshold]
    for active_rank in range(1, rank + 1):
        first = Fraction(
            falling(n, active_rank + 1),
            m * threshold * rising(d + 1, active_rank - 1),
        )
        second = Fraction(
            falling(R + active_rank, active_rank + 1),
            threshold * rising(d + 1, active_rank),
        )
        value = max(first, second)
        caps.append(value.numerator // value.denominator)
    high = max(caps)
    low = (R - d + threshold - 1) * ordinary
    return {
        "ordinary": ordinary,
        "high": high,
        "low": low,
        "total": near + high + low,
        "subsqrt": ordinary * ordinary < field_size,
    }


def eval_poly(coefficients: list[int], value: int, field: int) -> int:
    out = 0
    for coefficient in reversed(coefficients):
        out = (out * value + coefficient) % field
    return out


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-global-core-rankdrop-highcomplexity-router-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == [
            "rate_half_mca_rank11_anchor_star_sae_router",
            "rate_half_mca_rank11_shortened_partial_relative_router",
            "rate_half_mca_support_local_transversality_compiler",
            "rate_half_mca_rank10_margin_interleaving_split_payment",
            "rate_half_mca_order32_partial_relative_harvest",
        ],
        "dependencies",
    )
    row = data.get("official")
    require(isinstance(row, dict), "official")
    require(
        tuple(row.get(key) for key in ("n", "K", "m", "R", "d"))
        == (2097152, 1048576, 1116048, 1048576, 67472),
        "row",
    )
    require(row["n"] == row["R"] + row["K"], "length identity")
    require(row["m"] == row["d"] + row["K"], "agreement identity")
    require(row.get("near_charge") == 2 * row["d"] == 134944, "near")
    require(row.get("complexity_threshold") == 3 * row["m"] - row["K"] + 3, "chi")

    rank_drop = data.get("rank_drop")
    require(isinstance(rank_drop, dict), "rank drop")
    entries = rank_drop.get("transversality")
    require(isinstance(entries, list) and len(entries) == 8, "rank entries")
    for rank, entry in enumerate(entries, 1):
        short = transversality_cap(row["R"], row["d"], rank, rank)
        deployed = transversality_cap(row["R"], row["d"], row["K"], rank)
        expected = {
            "rank": rank,
            "short_endpoint": short,
            "deployed_endpoint": deployed,
            "maximum": max(short, deployed),
        }
        require(entry == expected, f"rank endpoint {rank}")
    rank8_total = entries[-1]["maximum"] + row["near_charge"]
    require(rank8_total == rank_drop.get("rank8_total_with_near"), "rank8 total")
    require(rank8_total < row["budget"], "rank8 payment")

    rank9 = rank_drop.get("rank9")
    require(isinstance(rank9, dict) and rank9.get("threshold") == 667, "rank9")
    field_size = row["p"] ** row["extension_degree"]
    short9 = margin_split(
        row["R"], row["d"], 9, 9, 667, row["near_charge"], field_size
    )
    deployed9 = margin_split(
        row["R"], row["d"], row["K"], 9, 667, row["near_charge"], field_size
    )
    require(short9["subsqrt"] and deployed9["subsqrt"], "field guard")
    require(rank9.get("ordinary_list_cap") == deployed9["ordinary"] == short9["ordinary"], "M9")
    require(rank9.get("short_endpoint_total") == short9["total"], "short rank9")
    require(rank9.get("deployed_high") == deployed9["high"], "rank9 high")
    require(rank9.get("low") == deployed9["low"] == short9["low"], "rank9 low")
    require(rank9.get("deployed_total") == deployed9["total"], "rank9 total")
    require(rank9.get("slack") == row["budget"] - deployed9["total"] > 0, "rank9 slack")

    full = data.get("full_rank")
    require(isinstance(full, dict), "full rank")
    require(
        tuple(
            full.get(key)
            for key in (
                "rank",
                "residual_dimension_minimum",
                "dense_pair_owner_minimum",
                "dense_anchor_count",
                "basis_records",
                "fillers",
                "anchor_size",
                "tuple_size",
                "slope_degree_minimum",
                "slope_degree_maximum",
            )
        )
        == (10, 10, 220, 18, 10, 3, 31, 32, 18, 31),
        "anchor constants",
    )
    require(full["dense_anchor_count"] + full["basis_records"] + full["fillers"] == 31, "anchor slots")
    require(full.get("complexity_addback_per_core_coordinate") == 2, "chi addback")
    require(full.get("sunflower_addback_per_core_coordinate") == 1, "sunflower addback")

    toy = data.get("toy_lift")
    require(isinstance(toy, dict), "toy")
    core = toy["core_size"]
    require(
        (toy["residual_n"], toy["residual_K"], toy["residual_m"])
        == (row["n"] - core, row["K"] - core, row["m"] - core),
        "toy shortening",
    )
    residual_chi = 3 * toy["residual_m"] - toy["residual_K"] + 3
    require(toy["residual_complexity_threshold"] == residual_chi, "toy chi residual")
    require(residual_chi + 2 * core == row["complexity_threshold"], "toy chi lift")
    require(
        toy["residual_sunflower_core_31"] + core == row["near_sunflower_core_31"],
        "sunflower lift",
    )
    require(
        toy["residual_noncollision_31"] + core == row["near_sunflower_noncollision_31"],
        "noncollision lift",
    )
    denominator = toy["denominator"]
    p = toy["field"]
    require(all(eval_poly(denominator, x, p) for x in toy["residual_points"]), "residual root free")
    require(any(eval_poly(denominator, x, p) == 0 for x in toy["deleted_points"]), "deleted root")
    require(
        data.get("route_labels")
        == [
            "P:rank-drop-at-most-nine-paid",
            "H_C:full-rank-relative-high-complexity-core",
            "A:coherent-root-free-rational-atom-after-lift",
            "E:pure-locator-denominator-root-or-collision-exception",
        ],
        "routes",
    )
    require("not the deployed" in str(data.get("nonclaim")), "nonclaim")
    return {"rank8": rank8_total, "rank9": deployed9["total"], "core": core}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["rank_drop"]["transversality"][7].__setitem__("maximum", 1),
        lambda item: item["rank_drop"]["rank9"].__setitem__("deployed_total", 1),
        lambda item: item["full_rank"].__setitem__("fillers", 2),
        lambda item: item["full_rank"].__setitem__("rank", 9),
        lambda item: item["toy_lift"].__setitem__("residual_complexity_threshold", 1),
        lambda item: item["toy_lift"].__setitem__("denominator", [1]),
        lambda item: item["route_labels"].__setitem__(1, "S:deployed-spread"),
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
        "RATE_HALF_MCA_RANK11_GLOBAL_CORE_RANKDROP_HIGHCOMPLEXITY_ROUTER_PASS "
        f"r8={result['rank8']} r9={result['rank9']} core={result['core']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
