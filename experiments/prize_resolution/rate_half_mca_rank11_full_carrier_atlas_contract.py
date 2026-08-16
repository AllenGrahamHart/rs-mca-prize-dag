#!/usr/bin/env python3
"""Shared validator for compact rank-eleven carrier-atlas row contracts."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import re
import sys
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve()
PROBE_NAME = "rate_half_mca_rank11_k72_two_step_probe.py"


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


def repository_root() -> Path:
    candidate = HERE.parents[2] if len(HERE.parents) > 2 else HERE.parent
    return candidate if (candidate / "background").is_dir() else HERE.parent


ROOT = repository_root()
repository_probe = ROOT / "experiments/prize_resolution" / PROBE_NAME
PROBE = load_module(
    "carrier_atlas_for_compact_contract",
    repository_probe if repository_probe.exists() else HERE.with_name(PROBE_NAME),
)
K71 = PROBE.K71


def active_conservative_caps(kprime: int, label: str):
    q = kprime - 10
    m = 67472 + kprime
    baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(q, m)
    _, front23, steps, carrier32, _ = PROBE.position23_group(kprime, baseline)
    defects = tuple(
        int(re.search(rf"s{support}=([0-9]+)", label).group(1))
        for support in range(2, 6)
    )
    s2, s3, s4, s5 = defects
    left_label = label.split("/s4=", 1)[0]
    if label.endswith("/ordinary"):
        left = next(vector for name, vector in front23 if name == left_label)
    elif label.endswith("/carrier32_plain"):
        left = next(
            vector for a, b, vector in carrier32 if (a, b) == (s2, s3)
        )
    else:
        match = re.search(r"/offset([1-6])_plain$", label)
        require(match is not None, "plain route label")
        left = next(
            vector
            for a, b, vector in steps[int(match.group(1))]
            if (a, b) == (s2, s3)
        )
    exact45, _, _ = K71.exact45_rows(kprime, baseline)
    middle = next(
        vector for a, b, vector in exact45 if (a, b) == (s4, s5)
    )
    high_match = re.search(r"(c6[TF]/c7[TF]/c8[TF]/c9[TF])", label)
    require(high_match is not None, "high label")
    _, high = K71.PARENT.high_group(kprime, baseline)
    right = next(
        vector for name, vector in high if name == high_match.group(1)
    )
    return K71.combine(left, middle, right)


def validate(data: object, root: Path = ROOT) -> dict[str, int]:
    require(isinstance(data, dict), "contract object")
    require("full-carrier-atlas-payment-v1" in data["schema"], "schema")
    for relative, digest in data["replay_sources"].items():
        require(
            hashlib.sha256((root / relative).read_bytes()).hexdigest() == digest,
            f"replay source {relative}",
        )
    p = data["parameters"]
    kprime = p["kprime"]
    require(
        (p["q"], p["m"], p["n"])
        == (kprime - 10, 67472 + kprime, 1048576 + kprime),
        "parameters",
    )
    require(
        p["new_closed_prefix"] == [10, kprime]
        and p["next_open_row"] == kprime + 1,
        "prefix",
    )

    plain = data["plain_frontier"]
    require(plain["evaluations"] > 0, "plain evaluations")
    require(plain["unsafe_distinct_defect_tuples"] > 0, "unsafe count")
    require(
        re.fullmatch(r"[0-9a-f]{64}", plain["unsafe_tuple_sha256"])
        is not None,
        "unsafe digest",
    )
    require(
        K71.premium(active_conservative_caps(kprime, plain["safe_maximum_label"]))
        == plain["safe_maximum"],
        "active premium",
    )

    row = data["row"]
    ceiling = row["safe_premium_ceiling"]
    require(plain["unsafe_minimum"] > ceiling, "unsafe threshold")
    require(plain["safe_maximum"] < ceiling, "safe threshold")
    reroute = data["reroute"]
    require(
        reroute["cells"] == plain["unsafe_distinct_defect_tuples"]
        and reroute["evaluations"] > 0
        and reroute["all_safe"],
        "reroute",
    )
    require(
        reroute["maximum"] + reroute["minimum_margin"] == ceiling,
        "reroute margin",
    )
    lanes = data["geometry_lanes"]
    require(
        {lane["lane"] for lane in lanes}
        == {
            "carrier32_geom", "one_geom", "two_geom", "three_geom",
            "four_geom", "five_geom", "six_geom",
        },
        "lane names",
    )
    require(
        sum(lane["evaluations"] for lane in lanes)
        == data["geometry_total_evaluations"],
        "lane evaluations",
    )
    require(
        max([reroute["maximum"]] + [lane["maximum"] for lane in lanes])
        < plain["safe_maximum"],
        "global maximum",
    )

    old = K71.LEDGER.row(kprime)
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
    return {
        "kprime": kprime,
        "unsafe_cells": reroute["cells"],
        "geometry_lanes": len(lanes),
    }


def tamper_selftest(data: dict, root: Path = ROOT) -> int:
    mutations = (
        lambda item: item["parameters"].__setitem__(
            "kprime", item["parameters"]["kprime"] + 1
        ),
        lambda item: item["replay_sources"].__setitem__(
            next(iter(item["replay_sources"])), "0" * 64
        ),
        lambda item: item["plain_frontier"].__setitem__(
            "unsafe_tuple_sha256", "0" * 63
        ),
        lambda item: item["plain_frontier"].__setitem__(
            "unsafe_distinct_defect_tuples", 0
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
            validate(trial, root)
        except (Reject, KeyError, TypeError, ValueError, StopIteration):
            rejected += 1
    require(rejected == len(mutations), "tamper rejection")
    return rejected


def run_primary(contract: Path, expected_sha256: str, root: Path = ROOT) -> int:
    raw = contract.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == expected_sha256, "contract hash")
    data = json.loads(raw)
    result = validate(data, root)
    result["contract_sha256"] = expected_sha256
    result["tamper_rejected"] = tamper_selftest(data, root)
    print(json.dumps(result, sort_keys=True))
    return 0


def compare_full_audit(data: dict, actual: dict) -> dict[str, int | str]:
    plain = actual["plain_frontier"]
    expected_plain = data["plain_frontier"]
    for key in (
        "evaluations", "unsafe_distinct_defect_tuples", "unsafe_tuple_sha256",
        "safe_maximum", "safe_maximum_label",
    ):
        require(plain[key] == expected_plain[key], f"audit plain {key}")
    reroute = actual["reroute"]
    expected_reroute = data["reroute"]
    for key in ("cells", "evaluations", "all_safe", "maximum", "minimum_margin"):
        require(reroute[key] == expected_reroute[key], f"audit reroute {key}")
    for key, value in actual["row"].items():
        require(value == data["row"][key], f"audit row {key}")
    return {
        "unsafe_tuple_sha256": plain["unsafe_tuple_sha256"],
        "rerouted_cells": reroute["cells"],
        "reroute_evaluations": reroute["evaluations"],
        "payment_gap": actual["row"]["gap"],
    }


def guarded_main(action) -> None:
    try:
        raise SystemExit(action())
    except Reject as exc:
        print(f"REJECT: {exc}", file=sys.stderr)
        raise SystemExit(1)
