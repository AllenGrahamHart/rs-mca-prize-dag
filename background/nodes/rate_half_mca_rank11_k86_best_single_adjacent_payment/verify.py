#!/usr/bin/env python3
"""Verify the compact K'=86 best-single adjacent payment contract."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "b318de9938264a3306372b473513b1975e6941204a39c03d07a5ff16b62e896f"
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
    assert (
        data["schema"]
        == "rate-half-mca-rank11-k86-best-single-adjacent-payment-v1"
    )

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
    residual = coverage["best_single_residual"]
    assert ordinary["jobs"] == 2
    assert ordinary["raw_rows"] == 7 * ordinary["source_units"]
    assert ordinary["audit_geometry_rows"] >= ordinary["primary_geometry_rows"]
    assert raw["lanes"] == 75 and raw["jobs"] == 150
    offset_units = sum((76 - offset) * 5929 for offset in range(1, 76))
    assert raw["source_units_per_implementation"] == offset_units
    assert raw["raw_rows_per_implementation"] == 7 * offset_units
    assert (
        raw["raw_safe_units_per_implementation"]
        + raw["raw_unsafe_units_per_implementation"]
        == offset_units
    )
    assert raw["unsafe_offsets"] == [1, 42]
    assert raw["fully_safe_offsets"] == [43, 75]
    assert residual["lanes"] == 42 and residual["jobs"] == 84
    residual_sources = sum((76 - offset) * 5929 for offset in range(1, 43))
    assert residual["source_units_per_implementation"] == residual_sources
    assert (
        residual["unsafe_units_per_implementation"]
        == raw["raw_unsafe_units_per_implementation"]
    )
    assert residual["profiles_per_implementation"] > 0

    ledger = load_module("k86_payment_ledger", K71_VERIFY).LEDGER
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
    assert p["new_closed_prefix"] == [10, 86] and p["next_open_row"] == 87
    assert [item["role"] for item in data["captures"]] == [
        "ordinary_slice",
        "raw_threshold_wave",
        "best_single_wave",
        "component_payment",
    ]
    assert len({item["app_id"] for item in data["captures"]}) == 4
    print(json.dumps({
        "status": "PASS",
        "premium": frontier["completion_premium"],
        "margin": frontier["premium_ceiling_margin"],
        "gap": row["gap"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
