#!/usr/bin/env python3
"""Verify both exact branches of the K8-zero cover."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "modal_degree12_k8_branch_output.json"
OUTPUT_SHA256 = "73c954a980bb6ece9a3690a69ead5221a8d8d03ea585bfd4cdd58aedd6e05838"


def main() -> None:
    raw = OUTPUT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == OUTPUT_SHA256
    payload = json.loads(raw)
    assert payload["counts"] == {
        "FAIL": 0,
        "PASS": 2,
        "REMOTE_ERROR": 0,
        "TIMEOUT": 0,
    }
    rows = {row["mode"]: row for row in payload["results"]}
    assert set(rows) == {"a0_k10_nonzero", "k8_k10_zero"}
    source = next(
        record
        for record in rows["a0_k10_nonzero"]["records"]
        if record["phase"] == "SOURCE_COMPILED"
    )
    assert (source["K8"]["degree"], source["K8"]["terms"], source["K8"]["sha256"]) == (
        8,
        72,
        "68a4b4515142e10e3ea36478ecb3126e60724a47511f61b85ff683c5b52fe33f",
    )
    assert (source["K10"]["degree"], source["K10"]["terms"], source["K10"]["sha256"]) == (
        10,
        130,
        "70c3b9e8ac39dc5fc64d873d3f78f44e2f4af47e95cfea0f4ff71419eb7c62ed",
    )
    assert {
        name: (record["degree"], record["terms"], record["sha256"])
        for name, record in source["cores"].items()
    } == {
        "A1": (37, 4124, "b3dd925bfeb1af9bed7691bec6ae50cfa1c6fe897eeba47bd650b5ee769abd0d"),
        "B1": (37, 3813, "aaaa336395cce7de3d265752464c12913ea570fdd921d73613efe08f18dbc61a"),
    }
    expected = {
        "a0_k10_nonzero": (
            62,
            "2d3e257ff476511a872c916f01d3845677a68bed8d25ebf084f1569be8e7462c",
            17,
        ),
        "k8_k10_zero": (
            27,
            "bba361cee0aeda5efd2d1c8a6aa534a41ed7954970cc2ea80af9f1cef5190464",
            16,
        ),
    }
    for mode, row in rows.items():
        assert row["status"] == "PASS"
        done = next(record for record in row["records"] if record["phase"] == "DONE")
        basis_size, basis_hash, final_index = expected[mode]
        assert (done["basis_size"], done["basis_sha256"], done["dimension"]) == (
            basis_size,
            basis_hash,
            1,
        )
        assert not done["unit_ideal"]
        assert done["terminal"] == "K8_BRANCH_EMPTY"
        assert done["saturation_unit_ideal"]
        assert done["saturation_basis_size"] == 1
        assert done["localizer_steps"][-1]["index"] == final_index
        assert done["localizer_steps"][-1]["label"] == "unit_14"
        assert done["localizer_steps"][-1]["zero"]
        assert all(not step["zero"] for step in done["localizer_steps"][:-1])
    print("KB_C2_112_DEGREE12_K8_BRANCH_COVER_PASS branches=2 bases=62,27")


if __name__ == "__main__":
    main()
