#!/usr/bin/env python3
"""Verify the complete fixed-literal inversion transport certificate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "modal_literal_fixed_inversion_transport_output.json"
OUTPUT_SHA256 = "6c199c50063abca20981f71133c71e3d5e8a68b52800e9666067dcffe4fed9b3"
PAIRS = {"F04-F05": ("F04", "F05"), "F06-F07": ("F06", "F07")}


def assert_named_support(record: dict[str, object]) -> None:
    assert record["all_factors_named_units"]
    assert all(factor["named_unit"] for factor in record["factors"])


def main() -> None:
    raw = OUTPUT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == OUTPUT_SHA256
    payload = json.loads(raw)
    assert payload["upstream_commit"] == "55ac3e07477bd7a768190a3e755f22b0d44354b0"
    assert payload["counts"] == {
        "FAIL": 0,
        "PASS": 2,
        "REMOTE_ERROR": 0,
        "TIMEOUT": 0,
    }
    assert {row["pair"] for row in payload["results"]} == set(PAIRS)
    for row in payload["results"]:
        assert row["status"] == "PASS" and row["returncode"] == 0
        assert len(row["records"]) == 1
        packet = row["records"][0]
        assert packet["schema"] == "kb-c2-112-fixed-literal-companion-inversion-transport-v1"
        result = packet["result"]
        source, target = PAIRS[row["pair"]]
        assert result["source_assignment"] == source
        assert result["target_assignment"] == target
        assert result["map"] == "b -> b^-1"
        assert all(result["source_coefficients_exact"].values())
        assert all(result["label_factor_multisets_exact"].values())
        named = result["named_open_transport"]
        assert named == {
            "b_chart_invariant": True,
            "nonmonomial_factor_multiset_exact": True,
            "source_factor_count": 30,
            "target_factor_count": 30,
        }
        full = result["full_identity_transport"]
        assert full["G_exact"] and full["J_G_factor_multiset_exact"]
        assert full["I_G_factor_multiset_exact"]
        assert full["full_J_exact"] and full["full_I_exact"]
        assert all(full["locator_checks"].values())
        checks = result["qslice_checks"]
        assert [check["source_cell"] for check in checks] == [
            f"{source}-R02",
            f"{source}-R11",
            f"{source}-R20",
        ]
        assert [check["target_cell"] for check in checks] == [
            f"{target}-R02",
            f"{target}-R11",
            f"{target}-R20",
        ]
        for check in checks:
            assert check["row_count"] == 4 and check["all_rows_exact"]
            for qslice_row in check["rows"]:
                assert qslice_row["cleared_numerator_up_to_sign"]
                for name in (
                    "source_denominator",
                    "target_denominator",
                    "ratio_numerator",
                    "ratio_denominator",
                ):
                    assert_named_support(qslice_row[name])
    print("KB_C2_112_FIXED_LITERAL_COMPANION_INVERSION_TRANSPORT_PASS pairs=2 targets=3 rows=24")


if __name__ == "__main__":
    main()
