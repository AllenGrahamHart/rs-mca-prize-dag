#!/usr/bin/env python3
"""Verify the exact K'=41 sharp-isolated payment."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "0b926a50e1d5ab12e56bdb1db2cdd143e7de60bf371862501d3853beb86ded69"
PARENT_VERIFY = (
    ROOT
    / "background/nodes/rate_half_mca_rank11_k24_k40_full_deficit_shadow_payment/verify.py"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_parent():
    spec = importlib.util.spec_from_file_location("full_deficit_parent", PARENT_VERIFY)
    require(spec is not None and spec.loader is not None, "parent module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PARENT = load_parent()


def expected(kprime: int) -> dict[str, int]:
    row = PARENT.row(kprime)
    n = 1048576 + kprime
    m = 67472 + kprime
    records = PARENT.RECORD_FLOOR
    demand = records * comb(m, 11) - comb(n, 11)
    coefficient = 55 * comb(m, 11) - int(row["premium"])
    raw = (
        records * coefficient
        - 55 * comb(n, 11)
        - 55 * int(row["kernel"])
        - int(row["marks"])
    )
    return {
        "n": n,
        "m": m,
        "q": kprime - 10,
        "isolated_global_cap": comb(n, 11),
        "max_core": int(row["max_core"]),
        "chart": int(row["chart"]),
        "kernel_capacity": int(row["kernel"]),
        "rank_nine_marks": int(row["marks"]),
        "completion_premium": int(row["premium"]),
        "full_rank_capacity": int(row["full_rank"]),
        "total_capacity": int(row["total"]),
        "required_component_incidence": demand,
        "gap": demand - int(row["total"]),
        "record_coefficient_cross": coefficient,
        "floor_record_raw_cross": raw,
    }


def validate(data: object) -> None:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-rank11-k41-sharp-isolated-payment-v1",
        "schema",
    )
    require(len(data.get("dependencies", [])) == 2, "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p.get("closed_row") == 41, "closed row")
    require(p.get("new_closed_prefix") == [10, 41], "prefix")
    require(p.get("first_method_wall") == 42, "wall")
    require(p.get("isolated_cap_per_eleven_set") == 1, "isolated cap")
    row41 = expected(41)
    for key, value in row41.items():
        require(p.get(key) == value, key)
    row42 = expected(42)
    require(row41["gap"] > 0, "K41 gap")
    require(row41["record_coefficient_cross"] > 0, "K41 coefficient")
    require(row41["floor_record_raw_cross"] > 0, "K41 raw")
    require(row42["gap"] < 0, "K42 wall sign")
    require(p.get("K42_capacity_excess") == -row42["gap"], "K42 excess")
    require(p.get("remaining_rank9_interval") == [42, 15528], "remaining")
    require("fails at K'=42" in str(data.get("nonclaim")), "nonclaim")


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item["parameters"].__setitem__("closed_row", 40),
        lambda item: item["parameters"].__setitem__("isolated_cap_per_eleven_set", 198),
        lambda item: item["parameters"].__setitem__("max_core", 39),
        lambda item: item["parameters"].__setitem__("completion_premium", 0),
        lambda item: item["parameters"].__setitem__("gap", 0),
        lambda item: item["parameters"].__setitem__("K42_capacity_excess", 0),
        lambda item: item.__setitem__("nonclaim", "K'=42 closed"),
    )
    rejected = 0
    for mutation in mutations:
        hostile = copy.deepcopy(data)
        mutation(hostile)
        try:
            validate(hostile)
        except (AssertionError, KeyError, TypeError):
            rejected += 1
    require(rejected == len(mutations), "tamper controls")
    return rejected


def main() -> None:
    raw = CONTRACT.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(raw)
    validate(data)
    controls = tamper_selftest(data)
    p = data["parameters"]
    print(
        "RATE_HALF_MCA_RANK11_K41_SHARP_ISOLATED_PAYMENT_PASS "
        f"gap={p['gap']} wall={p['K42_capacity_excess']} controls={controls}"
    )


if __name__ == "__main__":
    main()
