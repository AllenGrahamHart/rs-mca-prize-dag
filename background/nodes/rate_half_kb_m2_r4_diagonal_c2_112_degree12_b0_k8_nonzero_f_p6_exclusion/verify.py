#!/usr/bin/env python3
"""Verify the four R02 B0 K8-nonzero degree-six exclusions."""

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
        "4f4625f527e37d61a75b4c66fb614b1ecb76f2720ae724a398d8258da31fd470",
    "modal_degree12_quadratic_prem_determinant_global_saturation_all_b0_output.json":
        "983bfed32fb0cddf2f38d9506842463cb22c852d3fd7da2c91d81af4c1ef2107",
    "modal_degree12_quadratic_prem_determinant_linear_s_f_p6_b0_output.json":
        "4cc6c767bf838e1a1906e583e16d7f93cb80eca283088af336f72390a047e6d5",
}


def load(name: str) -> dict[str, object]:
    raw = (SOURCE / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == FILES[name]
    return json.loads(raw)


def done_record(row: dict[str, object]) -> dict[str, object]:
    return next(record for record in row["records"] if record["phase"] == "DONE")


def verify_all_cell_replay() -> None:
    payload = load(
        "modal_degree12_quadratic_prem_determinant_global_saturation_all_b0_output.json"
    )
    assert payload["counts"] == {
        "FAIL": 0,
        "PASS": 8,
        "REMOTE_ERROR": 0,
        "TIMEOUT": 0,
    }
    rows = {row["cell"]: row for row in payload["results"]}
    assert set(rows) == {
        f"F{assignment:02d}-{target}"
        for assignment in range(4, 8)
        for target in ("R02", "R20")
    }

    r02_expected = {
        "F04-R02": (
            142,
            "d6e07666f104db61e0cd4dcdac69f0a4c9bc05438940fdaeb45db5201a0ab407",
            25,
            "20aa338953e0bc2a121f84b908ca6ee264f7733650a58a9cebb516b7e2ab6c8d",
            10,
            "e43eb59adcf5158300ad3184b5ae2c36c7088f8b5688dcf3b0b53882a95a09db",
        ),
        "F05-R02": (
            143,
            "798289217cb325cb94d667ae4a362d6753a145dd03c033bcaca2c0412ddaccd6",
            25,
            "b809d74d6914529f18d5edc7961ce02e9ec3309ad22995700d93113189e0ded3",
            10,
            "0e24800832f5e8d31fd0718d7b0449e9e9bf962e0b25f42b6c212e656275c137",
        ),
        "F06-R02": (
            142,
            "932250b1156c591b852eef30d7dbe3074761dc2e764fef6b6e96b24aa106e166",
            26,
            "7ac111c3eae1497397ccb2994647018154b8a3ad94cf00968a4bbd248892b51f",
            20,
            "b1cffbebe98c6f25265ee4e61f3ae17555e6ca52ce0d383ba4c8507aefd03fd5",
        ),
        "F07-R02": (
            143,
            "dcaa2b678d7e8204e9dc475abc485ce7432415a9b1bf01b250a0e7a7228e563c",
            26,
            "152a9a9b612efe501cc775e11fddd0402016b600994692690cc0b82212cc07eb",
            20,
            "f9615258cd61c837c31c21554b19374d5d275fd999f37b2b794d154fc0215683",
        ),
    }
    for cell, expected in r02_expected.items():
        row = rows[cell]
        assert row["status"] == "PASS" and row["skip_elimination"]
        saturation = done_record(row)["global_saturation"]
        assert (
            saturation["global_basis_size"],
            saturation["global_basis_sha256"],
            saturation["saturation_basis_size"],
            saturation["saturation_basis_sha256"],
            saturation["field_basis_size"],
            saturation["field_basis_sha256"],
        ) == expected
        assert saturation["saturation_dimension"] == 0
        assert not saturation["saturation_unit_ideal"]
        assert not saturation["field_unit_ideal"]
        assert saturation["field_extension_degree"] == 6
        assert len(saturation["field_steps"]) == 18
        assert saturation["full_open_product_zero"]
        assert saturation["terminal"] == (
            "GLOBAL_COMPLETE_OPEN_CHART_HAS_NO_F_P6_POINTS"
        )
        steps = saturation["full_open_steps"]
        assert len(steps) == 18 and steps[-1] == {
            "index": 18,
            "sha256": "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9",
            "terms": 0,
            "zero": True,
        }
        assert all(not step["zero"] for step in steps[:-1])

    r20_expected = {
        "F04-R20": (44, "285b23ee632cd0fddc61347578650c5b6bf3056b530a5b36db1293b976cb51ef"),
        "F05-R20": (39, "59f28d2813d7dd4a09141eddb086578cc6905eb3da5d497c86e665d7b07ecd64"),
        "F06-R20": (33, "c41c9792d1dd49b07b361506e5fd3dd5a275a3239744c98a19b527d645b35c08"),
        "F07-R20": (35, "a018d9917cb460afca085a82c04676c8186d58810a5bd05ce35d1bab662954a0"),
    }
    for cell, (basis_size, basis_hash) in r20_expected.items():
        row = rows[cell]
        assert row["status"] == "PASS" and row["skip_elimination"]
        saturation = done_record(row)["global_saturation"]
        assert saturation["global_basis_size"] == 170
        assert saturation["saturation_basis_size"] == basis_size
        assert saturation["saturation_basis_sha256"] == basis_hash
        assert saturation["saturation_dimension"] == 1
        assert not saturation["saturation_unit_ideal"]
        assert saturation["field_basis_size"] == basis_size
        assert saturation["field_basis_sha256"] == basis_hash
        assert not saturation["field_steps"]
        assert not saturation["full_open_steps"]
        assert not saturation["full_open_product_zero"]
        assert saturation["terminal"] == "GLOBAL_OPEN_CHART_DOMINATES_S"


def verify_f04_independent_elimination() -> None:
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
    assert global_row["status"] == "PASS" and global_row["cell"] == "F04-R02"
    saturation = done_record(global_row)["global_saturation"]
    assert saturation["terminal"] == (
        "GLOBAL_COMPLETE_OPEN_CHART_HAS_NO_F_P6_POINTS"
    )
    assert (
        saturation["global_basis_size"],
        saturation["saturation_basis_size"],
        saturation["saturation_dimension"],
        saturation["saturation_unit_ideal"],
        saturation["field_basis_size"],
        saturation["field_unit_ideal"],
        saturation["full_open_product_zero"],
    ) == (142, 25, 0, False, 10, False, True)
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
        audit = done_record(row)["fiber_search"]
        assert audit["witness"] is None and len(audit["fibers"]) == 1
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


def main() -> None:
    verify_all_cell_replay()
    verify_f04_independent_elimination()
    print(
        "KB_C2_112_R02_B0_K8_NONZERO_F_P6_EXCLUSIONS_PASS "
        "cells=4 direct=4 eliminant=30 fibers=5 r20_residuals=4"
    )


if __name__ == "__main__":
    main()
