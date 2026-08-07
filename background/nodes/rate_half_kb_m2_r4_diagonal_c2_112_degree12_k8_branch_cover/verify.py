#!/usr/bin/env python3
"""Verify both exact K8-zero branches in all four R02 cells."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTPUTS = {
    "modal_degree12_k8_branch_output.json":
        "73c954a980bb6ece9a3690a69ead5221a8d8d03ea585bfd4cdd58aedd6e05838",
    "modal_degree12_k8_branch_all_r02_output.json":
        "f6fd14988f383e28e8821ee1e0a1655ca31e8c1ac7c3ae575f6f64c4bf6a5d36",
}


def load(name: str) -> dict[str, object]:
    raw = (HERE / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == OUTPUTS[name]
    return json.loads(raw)


def record(row: dict[str, object], phase: str) -> dict[str, object]:
    return next(value for value in row["records"] if value["phase"] == phase)


def main() -> None:
    payload = load("modal_degree12_k8_branch_all_r02_output.json")
    assert payload["counts"] == {
        "FAIL": 0,
        "PASS": 8,
        "REMOTE_ERROR": 0,
        "TIMEOUT": 0,
    }
    rows = {(row["cell"], row["mode"]): row for row in payload["results"]}
    cells = tuple(f"F{index:02d}-R02" for index in range(4, 8))
    modes = ("a0_k10_nonzero", "k8_k10_zero")
    assert set(rows) == {(cell, mode) for cell in cells for mode in modes}

    source_expected = {
        "F04-R02": {
            "K8": (8, 72, "68a4b4515142e10e3ea36478ecb3126e60724a47511f61b85ff683c5b52fe33f"),
            "K10": (10, 130, "70c3b9e8ac39dc5fc64d873d3f78f44e2f4af47e95cfea0f4ff71419eb7c62ed"),
            "A1": (37, 4124, "b3dd925bfeb1af9bed7691bec6ae50cfa1c6fe897eeba47bd650b5ee769abd0d"),
            "B1": (37, 3813, "aaaa336395cce7de3d265752464c12913ea570fdd921d73613efe08f18dbc61a"),
        },
        "F05-R02": {
            "K8": (8, 72, "f6afdd660950dbf340dd7d51d54709cb48a75b7f128efad398284778b64657db"),
            "K10": (10, 130, "67bf9e8a751e32c04f2231fda2e35db6b9759c6b9fb0fc4366ae9bdac8fe0e70"),
            "A1": (38, 4124, "0c2744d903c66a415f4451ba3c4d368b6c3ac9ae81092d6baf1532a833785066"),
            "B1": (37, 3813, "a7fd1d67309f7acea89453442f5e007062ee485eb708b6e101e23285ec3ef5e9"),
        },
        "F06-R02": {
            "K8": (8, 72, "f6afdd660950dbf340dd7d51d54709cb48a75b7f128efad398284778b64657db"),
            "K10": (10, 130, "67bf9e8a751e32c04f2231fda2e35db6b9759c6b9fb0fc4366ae9bdac8fe0e70"),
            "A1": (37, 4141, "fe34d48ef4704b2d65d3776cec347f434f92c6e5dd614aa0a368080d0161972c"),
            "B1": (37, 3807, "2608e4464091f06e8c06c3d577fb420cd9876ec04ee745f2cb25ef6db59a43ef"),
        },
        "F07-R02": {
            "K8": (8, 72, "68a4b4515142e10e3ea36478ecb3126e60724a47511f61b85ff683c5b52fe33f"),
            "K10": (10, 130, "70c3b9e8ac39dc5fc64d873d3f78f44e2f4af47e95cfea0f4ff71419eb7c62ed"),
            "A1": (38, 4141, "bf60273c28ccea71a46abea635c87b46fd030c4265e15f6cc3dbe7839af98c5d"),
            "B1": (37, 3807, "ab0ca2f11e6add1c5215fa8cd1a0a3fefcb8ac6665eef4215f5da1461cd62dbf"),
        },
    }
    basis_expected = {
        ("F04-R02", "a0_k10_nonzero"): (62, "2d3e257ff476511a872c916f01d3845677a68bed8d25ebf084f1569be8e7462c", 17),
        ("F04-R02", "k8_k10_zero"): (27, "bba361cee0aeda5efd2d1c8a6aa534a41ed7954970cc2ea80af9f1cef5190464", 16),
        ("F05-R02", "a0_k10_nonzero"): (61, "f9c6b259161dadb3d7a1881f703bf261d4dfc894ea1ba200557e9e5d94306815", 17),
        ("F05-R02", "k8_k10_zero"): (27, "eb18865c2e1ba657caa0fbc3d3fb8fa2fc163a8144f53d8cc77003cb86275d83", 16),
        ("F06-R02", "a0_k10_nonzero"): (61, "1a8425482442ee9378b91d04718bcbc10158e2e00c2128bd0698c1852b9ca14e", 17),
        ("F06-R02", "k8_k10_zero"): (27, "eb18865c2e1ba657caa0fbc3d3fb8fa2fc163a8144f53d8cc77003cb86275d83", 16),
        ("F07-R02", "a0_k10_nonzero"): (62, "9595eda197924629d1f7d79aa3b4fa15ad5f75e7023de4f3401cfa67af27a768", 17),
        ("F07-R02", "k8_k10_zero"): (27, "bba361cee0aeda5efd2d1c8a6aa534a41ed7954970cc2ea80af9f1cef5190464", 16),
    }

    for key, row in rows.items():
        cell, mode = key
        assert row["status"] == "PASS"
        source = record(row, "SOURCE_COMPILED")
        expected_source = source_expected[cell]
        for name in ("K8", "K10"):
            value = source[name]
            assert (value["degree"], value["terms"], value["sha256"]) == expected_source[name]
        for name in ("A1", "B1"):
            value = source["cores"][name]
            assert (value["degree"], value["terms"], value["sha256"]) == expected_source[name]

        done = record(row, "DONE")
        basis_size, basis_hash, final_index = basis_expected[key]
        assert (done["basis_size"], done["basis_sha256"], done["dimension"]) == (
            basis_size,
            basis_hash,
            1,
        )
        assert not done["unit_ideal"]
        assert done["terminal"] == "K8_BRANCH_EMPTY"
        assert done["saturation_unit_ideal"]
        assert done["saturation_basis_size"] == 1
        steps = done["localizer_steps"]
        assert steps[-1]["index"] == final_index
        assert steps[-1]["label"] == "unit_14" and steps[-1]["zero"]
        assert all(not step["zero"] for step in steps[:-1])

    original = load("modal_degree12_k8_branch_output.json")
    assert original["counts"] == {
        "FAIL": 0,
        "PASS": 2,
        "REMOTE_ERROR": 0,
        "TIMEOUT": 0,
    }
    for row in original["results"]:
        done = record(row, "DONE")
        expected = basis_expected[("F04-R02", row["mode"])]
        assert (done["basis_size"], done["basis_sha256"]) == expected[:2]
        assert done["terminal"] == "K8_BRANCH_EMPTY"

    print(
        "KB_C2_112_DEGREE12_R02_K8_BRANCH_COVER_PASS "
        "cells=4 branches=8 basis_sizes=62,61,61,62,27"
    )


if __name__ == "__main__":
    main()
