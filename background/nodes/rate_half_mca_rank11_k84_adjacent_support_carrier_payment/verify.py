#!/usr/bin/env python3
"""Verify the compact K'=84 adjacent-support payment contract."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "6cdb8f6495f90001bafe26e656566f6483d8505f565a69ebe57d2a6717d07cd3"
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
        == "rate-half-mca-rank11-k84-adjacent-support-carrier-payment-v1"
    )

    for relative, expected in data["sources"].items():
        actual = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
        assert actual == expected, relative

    node = json.loads((HERE / "node.json").read_text())
    assert node["node"]["status"] == "PROVED"
    dependencies = [row["from"] for row in node["requires"]]
    assert dependencies == data["dependencies"]

    coverage = data["coverage"]
    assert coverage["lanes"] == 1 + 73
    assert coverage["jobs"] == 2 * coverage["lanes"]
    offset_units = sum((74 - offset) * 5625 for offset in range(1, 74))
    assert coverage["source_units"] == coverage["ordinary_units"] + offset_units
    assert coverage["raw_rows"] == 7 * coverage["source_units"]
    assert coverage["ordinary_raw_rows"] == 7 * coverage["ordinary_units"]
    assert coverage["primary_geometry_rows"] > 0
    assert coverage["audit_geometry_rows"] >= coverage["primary_geometry_rows"]

    ledger = load_module("k84_payment_ledger", K71_VERIFY).LEDGER
    p = data["parameters"]
    row = data["row"]
    frontier = data["frontier"]
    old = ledger.row(p["kprime"])
    assert int(old["marks"]) == row["rank_nine_marks"]
    assert int(old["kernel"]) == row["kernel_capacity"]
    assert ledger.RECORD_FLOOR == row["record_floor"]
    ceiling = (
        ledger.RECORD_FLOOR * 55 * comb(p["m"], 11)
        - 55 * comb(p["n"], 11)
        - 55 * row["kernel_capacity"]
        - row["rank_nine_marks"]
        - 1
    ) // ledger.RECORD_FLOOR
    assert ceiling == frontier["safe_premium_ceiling"]
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
    assert p["new_closed_prefix"] == [10, 84] and p["next_open_row"] == 85
    assert [item["role"] for item in data["captures"]] == [
        "primary_wave",
        "audit_wave",
        "compact_merger",
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
