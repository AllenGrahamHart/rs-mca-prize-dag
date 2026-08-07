#!/usr/bin/env python3
"""Verify the two R20 B0 generic-boundary certificates."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTPUT_DIR = HERE.parent / (
    "rate_half_kb_m2_r4_diagonal_c2_112_quadratic_"
    "pseudoremainder_determinant_reduction"
)
CASES = (
    (
        "F04-R20",
        "modal_degree12_quadratic_prem_determinant_"
        "generic_saturated_f04_r20_b0_output.json",
        "de485f8ae66caa38a7fc5371d6329ea8160c57a539ea7b5d462a1766f152db53",
        44,
        "285b23ee632cd0fddc61347578650c5b6bf3056b530a5b36db1293b976cb51ef",
        "eccabac53df1d65500ee805a63bf9dc03fef3388cddb3f1e471eda8e7e9f2773",
        "4e671f32df1e2e3deedafc2eb42c178adee8a48db10747b359608e0140f6784e",
    ),
    (
        "F06-R20",
        "modal_degree12_quadratic_prem_determinant_"
        "generic_saturated_r20_b0_output.json",
        "7267914b0269d058934a7fecb4332f0e1e1ab4deb7380ec40370b63048e0a2fe",
        33,
        "c41c9792d1dd49b07b361506e5fd3dd5a275a3239744c98a19b527d645b35c08",
        "6e8fc9dd5a77518c608c831edca9c8224d7cb48b845e7d1e73fae031aa29ab4e",
        "492a39b77224511058e7e3c36bb12616e9382292e9085ac236e0e380fbb731f0",
    ),
)
UNIT_SHA256 = "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"
DENOMINATOR_FACTORS = (
    ("sparam", 1),
    ("sparam + 2", 1),
    ("sparam^2 + 2*sparam + 4", 2),
)


def main() -> None:
    for (
        cell,
        filename,
        output_sha256,
        saturation_size,
        saturation_sha256,
        block_sha256,
        reduced_sha256,
    ) in CASES:
        raw = (OUTPUT_DIR / filename).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == output_sha256
        payload = json.loads(raw)
        assert payload["counts"] == {
            "FAIL": 0,
            "PASS": 1,
            "REMOTE_ERROR": 0,
            "TIMEOUT": 0,
        }
        row = payload["results"][0]
        assert row["cell"] == cell
        assert row["divisor"] == "B0"
        assert row["status"] == "PASS"
        done = next(record for record in row["records"] if record["phase"] == "DONE")
        global_record = done["global_saturation"]
        assert global_record["saturation_dimension"] == 1
        assert global_record["saturation_basis_size"] == saturation_size
        assert global_record["saturation_basis_sha256"] == saturation_sha256

        generic = global_record["generic_fiber"]
        assert generic["block_basis_size"] == 7
        assert generic["block_basis_sha256"] == block_sha256
        assert generic["zero_dimensional"]
        assert generic["pure_power_bounds"] == [1, 1, 2]
        assert generic["standard_monomial_count"] == 2
        assert generic["reduced_basis_size"] == 3
        assert generic["reduced_basis_sha256"] == reduced_sha256

        boundary = generic["reduced_basis"][0]
        assert boundary["leading_monomial"] == "(0, 0, 2)"
        coefficients = {
            entry["monomial"]: entry["numerator"]
            for entry in boundary["coefficients"]
        }
        assert coefficients == {
            "(0, 0, 2)": "1",
            "(0, 0, 1)": "2*sparam + 2",
            "(0, 0, 0)": "sparam^2 + 2*sparam + 1",
        }
        assert all(
            entry["denominator"] == "1" for entry in boundary["coefficients"]
        )

        denominator_factors = {
            (factor["polynomial"], factor["degree"])
            for relation in generic["reduced_basis"][1:]
            for coefficient in relation["coefficients"]
            for factor in coefficient["denominator_factors"]
        }
        assert denominator_factors == set(DENOMINATOR_FACTORS)

        exceptional = generic["exceptional_records"]
        assert len(exceptional) == 3
        assert [record["factor"]["degree"] for record in exceptional] == [1, 1, 2]
        for record in exceptional:
            assert record["unit_ideal"]
            assert record["basis_size"] == 1
            assert record["basis_sha256"] == UNIT_SHA256
            assert record["field_unit_ideal"]
            assert record["all_f_p6_points_on_boundary"]
            assert record["field_steps"] == []

    print(
        "KB_C2_112_R20_B0_GENERIC_BOUNDARY_PASS "
        "representatives=2 transported_cells=4 exceptional_ideals=6"
    )


if __name__ == "__main__":
    main()
