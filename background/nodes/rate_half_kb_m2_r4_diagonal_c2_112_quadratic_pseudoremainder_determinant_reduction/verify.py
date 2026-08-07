#!/usr/bin/env python3
"""Verify the quadratic pseudo-remainder determinant reduction packet."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
FILES = {
    "modal_degree12_quadratic_prem_determinant_output.json":
        "12446e7fb1fc4d94247a212f32a9738033bc6e8eb4755f6ad7cc811843aea429",
    "modal_degree12_quadratic_prem_determinant_groebner_b0_output.json":
        "47d7c49bca22825c87ea94d019a5496e268a23bd757014181bdb092828a070de",
}


def load(name: str) -> dict[str, object]:
    raw = (HERE / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == FILES[name]
    return json.loads(raw)


def main() -> None:
    metrics = load("modal_degree12_quadratic_prem_determinant_output.json")
    assert metrics["counts"] == {
        "FAIL": 0,
        "PASS": 2,
        "REMOTE_ERROR": 0,
        "TIMEOUT": 0,
    }
    rows = {row["divisor"]: row for row in metrics["results"]}
    assert set(rows) == {"A0", "B0"}
    expected = {
        "A0": {
            "leading": [(10, 130, False, "70c3b9e8ac39dc5fc64d873d3f78f44e2f4af47e95cfea0f4ff71419eb7c62ed")],
            "A1": [(10, 130, "70c3b9e8ac39dc5fc64d873d3f78f44e2f4af47e95cfea0f4ff71419eb7c62ed"), (37, 4124, "b3dd925bfeb1af9bed7691bec6ae50cfa1c6fe897eeba47bd650b5ee769abd0d")],
            "B1": [(10, 130, "70c3b9e8ac39dc5fc64d873d3f78f44e2f4af47e95cfea0f4ff71419eb7c62ed"), (37, 3813, "aaaa336395cce7de3d265752464c12913ea570fdd921d73613efe08f18dbc61a")],
        },
        "B0": {
            "leading": [(1, 2, True, "2cd751e45834c2b2c521bd19eeb5e80113d69847f1dbdda7d0ea2b26d1fbf330"), (8, 72, False, "68a4b4515142e10e3ea36478ecb3126e60724a47511f61b85ff683c5b52fe33f")],
            "A1": [(8, 72, "68a4b4515142e10e3ea36478ecb3126e60724a47511f61b85ff683c5b52fe33f"), (34, 3201, "5dda9c22124c95f464b4ae706013dfc40d5edebf6d09fdd5f6cbf64f81bb4682")],
            "B1": [(8, 72, "68a4b4515142e10e3ea36478ecb3126e60724a47511f61b85ff683c5b52fe33f"), (34, 2937, "c7f34204557891adae5bc08ccc161d3071c2f316d6b096619256e0a83cc4aa71")],
        },
    }
    for divisor, row in rows.items():
        assert row["status"] == "PASS" and row["cell"] == "F04-R02"
        done = next(record for record in row["records"] if record["phase"] == "DONE")
        assert done["terminal"] == "QUADRATIC_PSEUDOREMAINDER_DETERMINANTS_COMPILED"
        leading = [
            (
                factor["degree"],
                factor["terms"],
                factor["named_unit_factor"],
                factor["sha256"],
            )
            for factor in done["leading_factors"]
        ]
        assert leading == expected[divisor]["leading"]
        for name in ("A1", "B1"):
            record = done["records"][name]
            assert record["pseudo_exponent"] == 3
            nonnamed = [
                (factor["degree"], factor["terms"], factor["sha256"])
                for factor in record["factors"]
                if not factor["named_unit_factor"]
            ]
            assert nonnamed == expected[divisor][name]

    groebner = load("modal_degree12_quadratic_prem_determinant_groebner_b0_output.json")
    assert groebner["counts"] == {
        "FAIL": 0,
        "PASS": 0,
        "REMOTE_ERROR": 0,
        "TIMEOUT": 1,
    }
    row = groebner["results"][0]
    assert row["status"] == "TIMEOUT" and row["divisor"] == "B0"
    basis = next(record for record in row["records"] if record["phase"] == "GROEBNER_DONE")
    assert (basis["basis_size"], basis["dimension"], basis["unit_ideal"]) == (142, 1, False)
    assert basis["basis_sha256"] == "abc0bb69d721dc35e2d3c9545cde751a86b4086ebf836fc73c053249d6e04e9a"
    powers = [
        record for record in row["records"]
        if record["phase"] == "CHART_LOCALIZER_POWER"
    ]
    assert [record["exponent"] for record in powers] == list(range(1, 13))
    assert all(not record["zero"] for record in powers)
    assert (powers[0]["terms"], powers[-1]["terms"]) == (1461, 36492)
    print("KB_C2_112_QUADRATIC_PSEUDOREMAINDER_REDUCTION_PASS charts=2 basis=142 powers=12")


if __name__ == "__main__":
    main()
