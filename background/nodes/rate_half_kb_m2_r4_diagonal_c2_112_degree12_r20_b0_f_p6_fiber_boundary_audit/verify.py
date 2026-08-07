#!/usr/bin/env python3
"""Verify the four-cell R20 degree-six fiber-boundary audit."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent / (
    "rate_half_kb_m2_r4_diagonal_c2_112_quadratic_pseudoremainder_"
    "determinant_reduction/modal_degree12_quadratic_prem_determinant_"
    "fiber_f_p6_r20_smoke_output.json"
)
OUTPUT_SHA256 = "df65edb465bacd160026297b0f9bcd4ce9a4afad782cf8d53328bf03b9d40481"
CELLS = tuple(f"F{index:02d}-R20" for index in range(4, 8))


def main() -> None:
    raw = OUTPUT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == OUTPUT_SHA256
    payload = json.loads(raw)
    assert payload["counts"] == {
        "FAIL": 0,
        "PASS": 4,
        "REMOTE_ERROR": 0,
        "TIMEOUT": 0,
    }
    assert tuple(row["cell"] for row in payload["results"]) == CELLS

    closed = 0
    for row in payload["results"]:
        assert row["status"] == "PASS"
        assert row["divisor"] == "B0"
        assert row["field_degree"] == 6
        done = next(
            record for record in row["records"] if record["phase"] == "DONE"
        )
        audit = done["fiber_search"]
        assert audit["witness"] is None
        fibers = audit["fibers"]
        assert [fiber["s"] for fiber in fibers] == list(range(1, 17))
        for fiber in fibers:
            assert fiber["dimension"] == 0
            assert not fiber["unit_ideal"]
            assert fiber["field_extension_degree"] == 6
            assert not fiber["field_unit_ideal"]
            assert fiber["open_product_zero"]
            steps = fiber["open_product_steps"]
            assert [step["index"] for step in steps] == list(range(1, 9))
            assert all(not step["zero"] for step in steps[:7])
            assert steps[7]["zero"]
            closed += 1
    assert closed == 64
    print(
        "KB_C2_112_R20_B0_F_P6_FIBER_BOUNDARY_PASS "
        "cells=4 fibers=64 first_zero_step=8"
    )


if __name__ == "__main__":
    main()
