#!/usr/bin/env python3
"""Verify the two R20 K10-zero linear-source saturation certificates."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
UNIT_SHA256 = "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"
CASES = (
    (
        "F04-R20",
        "modal_degree12_r20_k10_zero_linear_source_f04_output.json",
        "4cf2851432cf1327b61e4a553652d6fffd44706ca186f27b12b9f938ac5de5a4",
        82,
        "4350f3ec96c5202955ac20f15b9b9286051364c4a6c419e599f6d8ed5b851d63",
        ("e3cd67a1a71031826c536c35e234e6c32cfa0ba8e6d9854e981184138877b61a",
         "aa25bbc2ce1a21c942c4b7e86e3805abe2a6c88e64ba879ecf848707a0c5aee3"),
    ),
    (
        "F06-R20",
        "modal_degree12_r20_k10_zero_linear_source_f06_output.json",
        "f280f54b362182ff75d63ab369e1ac7fe766c784b5fe520df92446739bc1d91f",
        80,
        "660526bb69ed2d8ee9fc8b43722003d318e4c342851c9294b3ff09d92aa5292a",
        ("7f447947215825fbd8bcbbdab8a63a765e31d4c772dfe115b591df1a5554a5d9",
         "4012e3248795af3d0eee69e12ff53f011261bb576585fd924241e1f241dd2a34"),
    ),
)


def phase(records: list[dict[str, object]], name: str) -> dict[str, object]:
    return next(record for record in records if record.get("phase") == name)


def main() -> None:
    for cell, filename, payload_sha256, basis_size, basis_sha256, core_hashes in CASES:
        raw = (HERE / filename).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == payload_sha256
        payload = json.loads(raw)
        assert payload["counts"] == {
            "FAIL": 0,
            "PASS": 1,
            "REMOTE_ERROR": 0,
            "TIMEOUT": 0,
        }
        row = payload["results"][0]
        assert row["cell"] == cell and row["status"] == "PASS"
        assert row["linear_source"] is True

        begin = phase(row["records"], "GROEBNER_BEGIN")
        assert begin["linear_drop_reduced"]["terms"] == 0
        source = begin["linear_source"]
        for name, terms, expected_hash in zip(
            ("A1", "B1"), (5431, 5293), core_hashes
        ):
            assert source[name]["degree_w"] == 4
            assert source[name]["core"]["degree"] == 58
            assert source[name]["core"]["terms"] == terms
            assert source[name]["core"]["sha256"] == expected_hash
            assert source[name]["removed_units"] == []

        groebner = phase(row["records"], "GROEBNER_DONE")
        assert groebner["dimension"] == 1
        assert groebner["basis_size"] == basis_size
        assert groebner["basis_sha256"] == basis_sha256
        assert not groebner["unit_ideal"]

        saturation = phase(row["records"], "SATURATION_DONE")
        assert saturation == {
            "phase": "SATURATION_DONE",
            "unit_ideal": True,
            "basis_size": 1,
            "basis_sha256": UNIT_SHA256,
            "dimension": -1,
        }
        done = phase(row["records"], "DONE")
        assert done["terminal"] == "K10_ZERO_BRANCH_EMPTY"
        assert done["saturation_unit_ideal"]
        assert [step["label"] for step in done["localizer_steps"][:2]] == [
            "prior_s",
            "prior_L6",
        ]
        assert len(done["localizer_steps"]) == 26

    print(
        "KB_C2_112_R20_K10_ZERO_LINEAR_SOURCE_PASS "
        "representatives=2 transported_cells=4 source_rows=4"
    )


if __name__ == "__main__":
    main()
