#!/usr/bin/env python3
"""Independently audit the shape and terminal of the K10-zero certificates."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
FILES = (
    "modal_degree12_r20_k10_zero_linear_source_f04_output.json",
    "modal_degree12_r20_k10_zero_linear_source_f06_output.json",
)


def main() -> None:
    cells = set()
    basis_sizes = set()
    for filename in FILES:
        row = json.loads((HERE / filename).read_text())["results"][0]
        cells.add(row["cell"])
        records = {record["phase"]: record for record in row["records"]}
        generators = records["GROEBNER_BEGIN"]["generators"]
        assert [item["degree"] for item in generators] == [12, 10, 58, 58]
        assert [item["terms"] for item in generators[2:]] == [5431, 5293]
        assert records["GROEBNER_DONE"]["dimension"] == 1
        basis_sizes.add(records["GROEBNER_DONE"]["basis_size"])
        labels = [item["label"] for item in records["DONE"]["localizer_steps"]]
        assert labels[:2] == ["prior_s", "prior_L6"]
        assert labels[2:] == [f"unit_{index}" for index in range(1, 25)]
        assert not any(item["zero"] for item in records["DONE"]["localizer_steps"])
        assert records["DONE"]["saturation_basis_size"] == 1
        assert records["DONE"]["saturation_dimension"] == -1

    assert cells == {"F04-R20", "F06-R20"}
    assert basis_sizes == {80, 82}
    print("KB_C2_112_R20_K10_ZERO_INDEPENDENT_AUDIT_PASS cases=2")


if __name__ == "__main__":
    main()
