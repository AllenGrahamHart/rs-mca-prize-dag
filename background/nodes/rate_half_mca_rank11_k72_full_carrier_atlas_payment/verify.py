#!/usr/bin/env python3
"""Verify the exact K'=72 full-carrier-atlas payment contract."""

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
CONTRACT_SHA256 = "3f3d1903b9ba5063f370ce8acad984d0d740a722b3c17ead912c6faa7c98a258"
PARENT_VERIFY = ROOT / "background/nodes/rate_half_mca_rank11_k71_carrier_trichotomy_payment/verify.py"


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


PARENT = load_module("k71_for_k72_full_atlas", PARENT_VERIFY)


def active_conservative_caps():
    kprime = 72
    q = 62
    m = 67544
    baseline = PARENT.PARENT.PARENT.PARENT.CAPS.baseline_caps(q, m)
    left = PARENT.base23_vector(kprime, baseline, 35, 32)
    exact45, _, _ = PARENT.exact45_rows(kprime, baseline)
    middle = next(vector for s4, s5, vector in exact45 if (s4, s5) == (33, 31))
    _, high = PARENT.PARENT.high_group(kprime, baseline)
    right = next(vector for label, vector in high if label == "c6F/c7F/c8F/c9F")
    return PARENT.combine(left, middle, right)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract object")
    require(data["schema"].endswith("k72-full-carrier-atlas-payment-v1"), "schema")
    for relative, digest in data["replay_sources"].items():
        require(hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == digest, f"replay source {relative}")
    p = data["parameters"]
    require((p["kprime"], p["q"], p["m"], p["n"]) == (72, 62, 67544, 1048648), "parameters")
    require(p["new_closed_prefix"] == [10, 72] and p["next_open_row"] == 73, "prefix")

    plain = data["plain_frontier"]
    tuples = [tuple(row) for row in data["unsafe_defect_tuples"]]
    require(plain["unsafe_distinct_defect_tuples"] == len(tuples) == 36, "unsafe count")
    require(len(set(tuples)) == 36, "unsafe uniqueness")
    require(all(len(row) == 4 and all(0 <= value <= 62 for value in row) for row in tuples), "unsafe range")
    require(all(62 - row[1] > 62 - row[0] > 0 for row in tuples), "reroute full position")

    caps = active_conservative_caps()
    require(list(caps) == plain["safe_maximum_caps"], "active caps")
    require(PARENT.premium(caps) == plain["safe_maximum"], "active premium")

    reroute = data["reroute"]
    require(reroute["cells"] == 36 and reroute["all_safe"], "reroute")
    require(reroute["maximum"] + reroute["premium_margin"] == data["row"]["safe_premium_ceiling"], "reroute margin")
    lanes = data["geometry_lanes"]
    require(len(lanes) == 7, "lane count")
    require(sum(row["evaluations"] for row in lanes) == data["geometry_total_evaluations"], "lane evaluations")
    require(all(row["maximum"] < data["row"]["safe_premium_ceiling"] for row in lanes), "lane safety")
    require(max([reroute["maximum"]] + [row["maximum"] for row in lanes]) < plain["safe_maximum"], "global maximum")

    row = data["row"]
    old = PARENT.LEDGER.row(72)
    require(row["rank_nine_marks"] == int(old["marks"]), "marks")
    require(row["kernel_capacity"] == int(old["kernel"]), "kernel")
    require(row["record_floor"] == PARENT.LEDGER.RECORD_FLOOR, "record floor")
    require(row["completion_premium"] == plain["safe_maximum"], "premium")
    full = (row["rank_nine_marks"] + row["record_floor"] * row["completion_premium"]) // 55
    demand = row["record_floor"] * comb(p["m"], 11) - comb(p["n"], 11)
    ceiling = (
        row["record_floor"] * 55 * comb(p["m"], 11)
        - 55 * comb(p["n"], 11)
        - 55 * row["kernel_capacity"]
        - row["rank_nine_marks"] - 1
    ) // row["record_floor"]
    require(full == row["full_rank_capacity"], "full capacity")
    require(full + row["kernel_capacity"] == row["total_capacity"], "total capacity")
    require(demand == row["required_component_incidence"], "demand")
    require(demand - row["total_capacity"] == row["gap"] > 0, "positive gap")
    require(ceiling == row["safe_premium_ceiling"], "ceiling")
    require(ceiling - row["completion_premium"] == row["premium_ceiling_margin"] > 0, "premium margin")
    return {"unsafe_cells": len(tuples), "geometry_lanes": len(lanes)}


def tamper_selftest(data: dict) -> int:
    mutations = (
        lambda item: item["parameters"].__setitem__("kprime", 73),
        lambda item: item["replay_sources"].__setitem__(next(iter(item["replay_sources"])), "0" * 64),
        lambda item: item["unsafe_defect_tuples"].pop(),
        lambda item: item["reroute"].__setitem__("all_safe", False),
        lambda item: item["geometry_lanes"][0].__setitem__("maximum", item["row"]["safe_premium_ceiling"]),
        lambda item: item["row"].__setitem__("completion_premium", item["row"]["completion_premium"] + 1),
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
