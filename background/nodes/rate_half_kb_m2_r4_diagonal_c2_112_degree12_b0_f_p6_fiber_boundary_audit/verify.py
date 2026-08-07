#!/usr/bin/env python3
"""Verify the exact degree-six finite-field fiber boundary audit."""

from __future__ import annotations

import collections
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent / (
    "rate_half_kb_m2_r4_diagonal_c2_112_quadratic_pseudoremainder_"
    "determinant_reduction/modal_degree12_quadratic_prem_determinant_"
    "fiber_f_p6_b0_output.json"
)
OUTPUT_SHA256 = "c8d042bfbb720522883b5677ce5532f59170a5bb151c7dfd9d344551b2befbd2"


def main() -> None:
    raw = OUTPUT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == OUTPUT_SHA256
    payload = json.loads(raw)
    assert payload["counts"] == {
        "FAIL": 0,
        "PASS": 1,
        "REMOTE_ERROR": 0,
        "TIMEOUT": 0,
    }
    row = payload["results"][0]
    assert row["status"] == "PASS"
    assert (row["cell"], row["divisor"], row["field_degree"]) == (
        "F04-R02",
        "B0",
        6,
    )
    done = next(record for record in row["records"] if record["phase"] == "DONE")
    audit = done["fiber_search"]
    assert audit["witness"] is None
    fibers = audit["fibers"]
    assert [fiber["s"] for fiber in fibers] == list(range(1, 65))
    exceptional = [fiber for fiber in fibers if fiber["dimension"] != 0]
    assert len(exceptional) == 1
    assert (exceptional[0]["s"], exceptional[0]["dimension"]) == (2, 1)

    death = collections.Counter()
    for fiber in fibers:
        if fiber["s"] == 2:
            assert "field_basis_size" not in fiber
            continue
        assert fiber["dimension"] == 0
        assert fiber["field_extension_degree"] == 6
        assert not fiber["field_unit_ideal"]
        assert fiber["open_product_zero"]
        steps = fiber["open_product_steps"]
        assert steps and steps[-1]["zero"]
        assert all(not step["zero"] for step in steps[:-1])
        death[steps[-1]["index"]] += 1
    assert death == {3: 2, 5: 61}
    assert [
        fiber["s"]
        for fiber in fibers
        if fiber.get("open_product_steps")
        and fiber["open_product_steps"][-1]["index"] == 3
    ] == [1, 4]
    print("KB_C2_112_B0_F_P6_FIBER_BOUNDARY_PASS closed=63 exceptional_s=2 deaths=V:2,disc:61")


if __name__ == "__main__":
    main()
