#!/usr/bin/env python3
"""Verify the global B0 K8-nonzero degree-six exclusion."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / (
    "rate_half_kb_m2_r4_diagonal_c2_112_quadratic_pseudoremainder_"
    "determinant_reduction"
)
FILES = {
    "modal_degree12_quadratic_prem_determinant_global_saturation_b0_output.json":
        "7625dbbff7ad3550b1c0a78cb3e8f972e543e9adbb64f324db902691d40df2dc",
    "modal_degree12_quadratic_prem_determinant_linear_s_f_p6_b0_output.json":
        "4cc6c767bf838e1a1906e583e16d7f93cb80eca283088af336f72390a047e6d5",
}


def load(name: str) -> dict[str, object]:
    raw = (SOURCE / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == FILES[name]
    return json.loads(raw)


def main() -> None:
    global_payload = load(
        "modal_degree12_quadratic_prem_determinant_global_saturation_b0_output.json"
    )
    assert global_payload["counts"] == {
        "FAIL": 0,
        "PASS": 1,
        "REMOTE_ERROR": 0,
        "TIMEOUT": 0,
    }
    global_row = global_payload["results"][0]
    assert global_row["status"] == "PASS"
    done = next(
        record for record in global_row["records"] if record["phase"] == "DONE"
    )
    saturation = done["global_saturation"]
    assert saturation["terminal"] == "GLOBAL_OPEN_CHART_ELIMINATED_TO_S"
    assert (
        saturation["global_basis_size"],
        saturation["saturation_basis_size"],
        saturation["saturation_dimension"],
        saturation["saturation_unit_ideal"],
    ) == (142, 25, 0, False)
    assert saturation["saturation_basis_sha256"] == (
        "20aa338953e0bc2a121f84b908ca6ee264f7733650a58a9cebb516b7e2ab6c8d"
    )
    assert len(saturation["elimination"]) == 1
    eliminant = saturation["elimination"][0]
    assert (eliminant["degree"], eliminant["terms"], eliminant["sha256"]) == (
        30,
        31,
        "f8b09f88c05017ec2c4381579e38df84cde883aa0afeb6a195b0131975bd1b06",
    )
    factors = eliminant["factors"]
    assert [(factor["degree"], factor["exponent"]) for factor in factors] == [
        (1, 1),
        (1, 2),
        (1, 2),
        (1, 2),
        (1, 2),
        (4, 2),
        (4, 2),
        (5, 1),
    ]
    roots = [factor["root"] for factor in factors if factor["degree"] == 1]
    assert roots == [
        1691727589,
        2130706429,
        1804255948,
        1065353214,
        675900418,
    ]
    assert all(factor["degree"] not in (2, 3, 6) for factor in factors)

    fibers_payload = load(
        "modal_degree12_quadratic_prem_determinant_linear_s_f_p6_b0_output.json"
    )
    assert fibers_payload["counts"] == {
        "FAIL": 0,
        "PASS": 5,
        "REMOTE_ERROR": 0,
        "TIMEOUT": 0,
    }
    expected_death = {
        1691727589: 5,
        2130706429: 5,
        1804255948: 16,
        1065353214: 5,
        675900418: 15,
    }
    assert {row["fiber_start"] for row in fibers_payload["results"]} == set(roots)
    for row in fibers_payload["results"]:
        assert row["status"] == "PASS" and row["field_degree"] == 6
        done = next(record for record in row["records"] if record["phase"] == "DONE")
        audit = done["fiber_search"]
        assert audit["witness"] is None
        assert len(audit["fibers"]) == 1
        fiber = audit["fibers"][0]
        assert fiber["s"] == row["fiber_start"]
        assert fiber["dimension"] == 0
        assert fiber["field_extension_degree"] == 6
        assert not fiber["field_unit_ideal"]
        assert fiber["open_product_zero"]
        steps = fiber["open_product_steps"]
        assert steps[-1]["zero"]
        assert all(not step["zero"] for step in steps[:-1])
        assert steps[-1]["index"] == expected_death[fiber["s"]]
    print("KB_C2_112_B0_K8_NONZERO_F_P6_EXCLUSION_PASS eliminant=30 factors=8 fibers=5")


if __name__ == "__main__":
    main()
