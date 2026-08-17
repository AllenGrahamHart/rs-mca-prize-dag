#!/usr/bin/env python3
"""Verify the compact K'=87 raw-clipped adjacent payment contract."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "fc0699db0b33a5ff6a6fe04b918e5cbd5eefe3e9b29b9acd7816880b31cf7c88"
K71_VERIFY = (
    ROOT
    / "background/nodes/"
    "rate_half_mca_rank11_k71_carrier_trichotomy_payment/verify.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    assert data["schema"] == "rate-half-mca-rank11-k87-raw-clipped-adjacent-payment-v1"

    for relative, expected in data["sources"].items():
        actual = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
        assert actual == expected, relative

    node = json.loads((HERE / "node.json").read_text())
    assert node["node"]["status"] == "PROVED"
    dependencies = [row["from"] for row in node["requires"]]
    assert dependencies == data["dependencies"]

    coverage = data["coverage"]
    ordinary = coverage["ordinary"]
    raw = coverage["raw_offsets"]
    clipped = coverage["clipped_residual"]
    assert ordinary["jobs"] == 2
    assert ordinary["raw_rows"] == 7 * ordinary["source_units"]
    assert ordinary["audit_geometry_rows"] == ordinary["primary_geometry_rows"]
    assert raw["lanes"] == 76 and raw["jobs"] == 152
    offset_units = sum((77 - offset) * 6084 for offset in range(1, 77))
    assert raw["source_units_per_implementation"] == offset_units
    assert raw["raw_rows_per_implementation"] == 7 * offset_units
    assert (
        raw["raw_safe_units_per_implementation"]
        + raw["raw_unsafe_units_per_implementation"]
        == offset_units
    )
    assert raw["unsafe_offsets"] == [1, 43]
    assert raw["fully_safe_offsets"] == [44, 76]
    assert clipped["lanes"] == 43 and clipped["jobs"] == 86
    clipped_sources = sum((77 - offset) * 6084 for offset in range(1, 44))
    assert clipped["source_units_per_implementation"] == clipped_sources
    assert (
        clipped["unsafe_units_per_implementation"]
        == raw["raw_unsafe_units_per_implementation"]
    )
    assert clipped["profiles_per_implementation"] > 0

    ranges = data["clipped_ranges"]
    assert ranges[0]["offsets"][0] == 1 and ranges[-1]["offsets"][1] == 43
    assert all(
        left["offsets"][1] + 1 == right["offsets"][0]
        for left, right in zip(ranges, ranges[1:])
    )
    assert all(len(row["sha256"]) == 64 for row in ranges)
    assert len(data["clipped_merged_sha256"]) == 64

    ledger = load_module("k87_payment_ledger", K71_VERIFY).LEDGER
    p = data["parameters"]
    row = data["row"]
    frontier = data["frontier"]
    old = ledger.row(p["kprime"])
    assert int(old["marks"]) == row["rank_nine_marks"]
    assert int(old["kernel"]) == row["kernel_capacity"]
    assert ledger.RECORD_FLOOR == row["record_floor"]
    ceiling_numerator = (
        ledger.RECORD_FLOOR * 55 * comb(p["m"], 11)
        - 55 * comb(p["n"], 11)
        - 55 * row["kernel_capacity"]
        - row["rank_nine_marks"]
        - 1
    )
    ceiling, remainder = divmod(ceiling_numerator, ledger.RECORD_FLOOR)
    assert ceiling == frontier["safe_premium_ceiling"]
    assert remainder == row["ceiling_remainder"]
    assert ordinary["premium"] < frontier["completion_premium"]
    assert (
        ceiling - frontier["completion_premium"]
        == frontier["premium_ceiling_margin"]
        > 0
    )
    full = (
        row["rank_nine_marks"]
        + ledger.RECORD_FLOOR * frontier["completion_premium"]
    ) // 55
    required = ledger.RECORD_FLOOR * comb(p["m"], 11) - comb(p["n"], 11)
    assert full == row["full_rank_capacity"]
    assert full + row["kernel_capacity"] == row["total_capacity"]
    assert required == row["required_component_incidence"]
    assert required - row["total_capacity"] == row["gap"] > 0
    assert p["new_closed_prefix"] == [10, 87] and p["next_open_row"] == 88
    assert [item["role"] for item in data["captures"]] == [
        "ordinary",
        "raw_threshold_wave",
        "component_payment",
    ]
    assert len({item["app_id"] for item in data["captures"] + ranges}) == 9
    print(json.dumps({
        "status": "PASS",
        "premium": frontier["completion_premium"],
        "margin": frontier["premium_ceiling_margin"],
        "gap": row["gap"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
