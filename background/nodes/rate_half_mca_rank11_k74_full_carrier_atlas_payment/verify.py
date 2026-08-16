#!/usr/bin/env python3
"""Verify the compact K'=74 full-carrier-atlas payment contract."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "8162044ad85a08b7dbed81a06f707e799c4be5ae837fd855be8aaa3c2d285b4d"
PROBE_PATH = (
    ROOT
    / "experiments/prize_resolution/"
    "rate_half_mca_rank11_k72_two_step_probe.py"
)


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"module {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PROBE = load_module("carrier_atlas_for_k74_contract", PROBE_PATH)
K71 = PROBE.K71


def active_conservative_caps():
    baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(64, 67546)
    _, _, steps, _, _ = PROBE.position23_group(74, baseline)
    left = next(
        vector for s2, s3, vector in steps[1] if (s2, s3) == (32, 31)
    )
    exact45, _, _ = K71.exact45_rows(74, baseline)
    middle = next(
        vector for s4, s5, vector in exact45 if (s4, s5) == (32, 30)
    )
    _, high = K71.PARENT.high_group(74, baseline)
    right = next(
        vector for label, vector in high if label == "c6F/c7F/c8F/c9F"
    )
    return K71.combine(left, middle, right)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract object")
    require(data["schema"].endswith("k74-full-carrier-atlas-payment-v1"), "schema")
    for relative, digest in data["replay_sources"].items():
        require(
            hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == digest,
            f"replay source {relative}",
        )
    p = data["parameters"]
    require(
        (p["kprime"], p["q"], p["m"], p["n"])
        == (74, 64, 67546, 1048650),
        "parameters",
    )
    require(
        p["new_closed_prefix"] == [10, 74] and p["next_open_row"] == 75,
        "prefix",
    )

    plain = data["plain_frontier"]
    require(plain["evaluations"] == 8869588, "plain evaluations")
    require(plain["unsafe_distinct_defect_tuples"] == 729, "unsafe count")
    require(
        plain["unsafe_tuple_sha256"]
        == "e036791483f8f10702731c02172071ce6106a1587f1996439640f08122162cf4",
        "unsafe digest",
    )
    require(
        K71.premium(active_conservative_caps()) == plain["safe_maximum"],
        "active premium",
    )
    require(
        plain["safe_maximum_label"]
        == "s2=32/s3=31/s4=32/s5=30/c6F/c7F/c8F/c9F/offset1_plain",
        "active label",
    )

    row = data["row"]
    ceiling = row["safe_premium_ceiling"]
    require(plain["unsafe_minimum"] > ceiling, "unsafe threshold")
    require(plain["safe_maximum"] < ceiling, "safe threshold")
    reroute = data["reroute"]
    require(
        reroute["cells"] == 729
        and reroute["evaluations"] == 338149
        and reroute["all_safe"],
        "reroute",
    )
    require(not reroute["maximizer_unique"], "tie convention")
    require(
        reroute["maximum"] + reroute["minimum_margin"] == ceiling,
        "reroute margin",
    )
    lanes = data["geometry_lanes"]
    require(len(lanes) == 7, "lane count")
    require(
        sum(lane["evaluations"] for lane in lanes)
        == data["geometry_total_evaluations"]
        == 124851888,
        "lane evaluations",
    )
    require(
        max([reroute["maximum"]] + [lane["maximum"] for lane in lanes])
        < plain["safe_maximum"],
        "global maximum",
    )

    old = K71.LEDGER.row(74)
    require(row["rank_nine_marks"] == int(old["marks"]), "marks")
    require(row["kernel_capacity"] == int(old["kernel"]), "kernel")
    require(row["record_floor"] == K71.LEDGER.RECORD_FLOOR, "record floor")
    require(row["completion_premium"] == plain["safe_maximum"], "premium")
    full = (
        row["rank_nine_marks"]
        + row["record_floor"] * row["completion_premium"]
    ) // 55
    demand = row["record_floor"] * comb(p["m"], 11) - comb(p["n"], 11)
    recomputed_ceiling = (
        row["record_floor"] * 55 * comb(p["m"], 11)
        - 55 * comb(p["n"], 11)
        - 55 * row["kernel_capacity"]
        - row["rank_nine_marks"]
        - 1
    ) // row["record_floor"]
    coefficient = 55 * comb(p["m"], 11) - row["completion_premium"]
    raw = (
        row["record_floor"] * coefficient
        - 55 * comb(p["n"], 11)
        - 55 * row["kernel_capacity"]
        - row["rank_nine_marks"]
    )
    require(full == row["full_rank_capacity"], "full capacity")
    require(full + row["kernel_capacity"] == row["total_capacity"], "total")
    require(demand == row["required_component_incidence"], "demand")
    require(demand - row["total_capacity"] == row["gap"] > 0, "positive gap")
    require(recomputed_ceiling == ceiling, "ceiling")
    require(
        ceiling - row["completion_premium"]
        == row["premium_ceiling_margin"]
        > 0,
        "premium margin",
    )
    require(coefficient == row["record_coefficient_cross"], "coefficient")
    require(raw == row["floor_record_raw_cross"] > 0, "raw cross")
    return {"unsafe_cells": 729, "geometry_lanes": 7}


def tamper_selftest(data: dict) -> int:
    mutations = (
        lambda item: item["parameters"].__setitem__("kprime", 75),
        lambda item: item["replay_sources"].__setitem__(
            next(iter(item["replay_sources"])), "0" * 64
        ),
        lambda item: item["plain_frontier"].__setitem__(
            "unsafe_tuple_sha256", "0" * 64
        ),
        lambda item: item["plain_frontier"].__setitem__(
            "unsafe_distinct_defect_tuples", 728
        ),
        lambda item: item["reroute"].__setitem__("all_safe", False),
        lambda item: item["geometry_lanes"][0].__setitem__(
            "maximum", item["row"]["safe_premium_ceiling"]
        ),
        lambda item: item["row"].__setitem__(
            "completion_premium", item["row"]["completion_premium"] + 1
        ),
        lambda item: item["row"].__setitem__("gap", -1),
    )
    rejected = 0
    for mutate in mutations:
        trial = copy.deepcopy(data)
        mutate(trial)
        try:
            validate(trial)
        except (Reject, KeyError, TypeError, ValueError, StopIteration):
            rejected += 1
    require(rejected == len(mutations), "tamper rejection")
    return rejected


def main() -> int:
    raw = CONTRACT.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(raw)
    result = validate(data)
    result["contract_sha256"] = CONTRACT_SHA256
    result["tamper_rejected"] = tamper_selftest(data)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Reject as exc:
        print(f"REJECT: {exc}", file=sys.stderr)
        raise SystemExit(1)
