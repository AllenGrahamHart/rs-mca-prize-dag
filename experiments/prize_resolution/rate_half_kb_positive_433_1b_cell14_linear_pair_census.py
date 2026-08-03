#!/usr/bin/env python3
"""Aggregate the exact positive 433-1b cell-14 linear-pair census."""

import hashlib
import itertools
import json
from pathlib import Path


DIRECTORY = Path(__file__).resolve().parent
SCRIPT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_generic_fiber_modal.py"
CURVE = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_curve_kernel_result.json"
PAIRING0 = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_linear_pair_pairing0_complete_result.json"
OPEN = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_linear_pair_pairings1_2_open_result.json"
BOUNDARY01 = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_linear_pair_xi0_1_pairings1_2_boundary_result.json"
BOUNDARY2 = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_linear_pair_xi2_pairings1_2_boundary_result.json"
REPLAY = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_linear_pair_xi2_boundary_timeout_replay_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_linear_pair_census_result.json"
FIELD = 2130706433
SCHEMA = "rate-half-kb-positive-433-1b-cell14-generic-fiber-v2"
SIGNS = tuple(itertools.product((-1, 1), repeat=2))


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    payload = json.loads(path.read_text())
    require(payload["schema"] == SCHEMA, f"schema: {path.name}")
    require(payload["field"] == FIELD, f"field: {path.name}")
    require(payload["source_script_sha256"] == digest(SCRIPT),
            f"script custody: {path.name}")
    require(payload["source_curve_sha256"] == digest(CURVE),
            f"curve custody: {path.name}")
    return payload


def key(row):
    return (
        tuple(row["epsilon"]), tuple(row["sigma"]),
        row["xi_index"], row["pairing_index"],
    )


def cut(row):
    require(len(row["parameter_cuts"]) == 1, "single parameter cut")
    return row["parameter_cuts"][0]


def factor_count(row):
    return len(cut(row)["boundary_factors"])


def main():
    pairing0 = load(PAIRING0)
    open_payload = load(OPEN)
    boundary01 = load(BOUNDARY01)
    boundary2 = load(BOUNDARY2)
    replay = load(REPLAY)

    expected_pairing0 = set(itertools.product(SIGNS, SIGNS, range(3), (0,)))
    pairing0_rows = {key(row): row for row in pairing0["rows"]}
    require(set(pairing0_rows) == expected_pairing0 and len(pairing0["rows"]) == 48,
            "pairing-0 Cartesian census")
    for case, row in pairing0_rows.items():
        expected_factors = 12 if case[2] in (0, 1) else 10
        require(row["status"] == "COMPLETE" and row["unit"] and row["open_unit"],
                f"pairing-0 unit: {case}")
        require(factor_count(row) == expected_factors, f"pairing-0 factors: {case}")
        require(len(row["boundary_results"]) == expected_factors and
                all(item["unit"] and item["dimension"] == -1 and
                    item["basis_size"] == 1
                    for item in row["boundary_results"]),
                f"pairing-0 boundaries: {case}")

    expected_open = set(itertools.product(SIGNS, SIGNS, range(3), (1, 2)))
    open_rows = {key(row): row for row in open_payload["rows"]}
    require(set(open_rows) == expected_open and len(open_payload["rows"]) == 96,
            "pairing-1/2 open Cartesian census")
    for case, row in open_rows.items():
        require(row["status"] == "COMPLETE" and row["unit"] and
                row["dimension"] == -1 and row["basis_size"] == 1,
                f"open unit: {case}")
        require(factor_count(row) == (12 if case[2] in (0, 1) else 10),
                f"open factor count: {case}")

    boundary_rows = {}
    for payload in (boundary01, boundary2):
        for row in payload["rows"]:
            boundary_key = (*key(row), row["factor_index"])
            require(boundary_key not in boundary_rows, f"duplicate boundary: {boundary_key}")
            boundary_rows[boundary_key] = row
    expected_boundary = {
        (epsilon, sigma, xi_index, pairing_index, factor_index)
        for epsilon in SIGNS
        for sigma in SIGNS
        for xi_index in range(3)
        for pairing_index in (1, 2)
        for factor_index in range(12 if xi_index in (0, 1) else 10)
    }
    require(set(boundary_rows) == expected_boundary and len(boundary_rows) == 1088,
            "boundary Cartesian census")

    replay_rows = replay["rows"]
    require(len(replay_rows) == 1, "single timeout replay")
    replay_row = replay_rows[0]
    replay_key = (*key(replay_row), replay_row["factor_index"])
    timed_out = boundary_rows[replay_key]
    require(timed_out["status"] == "TIMEOUT" and
            timed_out["program_sha256"] == replay_row["program_sha256"] and
            timed_out["definitions_sha256"] == replay_row["definitions_sha256"],
            "hash-identical timeout replay")
    boundary_rows[replay_key] = replay_row

    logical_rows = []
    for case in sorted(expected_pairing0 | expected_open):
        epsilon, sigma, xi_index, pairing_index = case
        if pairing_index == 0:
            row = pairing0_rows[case]
            boundary_programs = [row["program_sha256"]] * factor_count(row)
            open_program = row["program_sha256"]
        else:
            row = open_rows[case]
            open_program = row["program_sha256"]
            boundary_programs = []
            for factor_index in range(factor_count(row)):
                boundary = boundary_rows[(*case, factor_index)]
                require(boundary["status"] == "COMPLETE" and boundary["unit"] and
                        boundary["dimension"] == -1 and boundary["basis_size"] == 1,
                        f"boundary unit: {(*case, factor_index)}")
                require(cut(boundary) == cut(row),
                        f"open/boundary cut custody: {(*case, factor_index)}")
                boundary_programs.append(boundary["program_sha256"])
        logical_rows.append({
            "epsilon": list(epsilon),
            "sigma": list(sigma),
            "xi_index": xi_index,
            "pairing_index": pairing_index,
            "open_program_sha256": open_program,
            "open_cut_sha256": cut(row)["open_cut_sha256"],
            "boundary_factor_count": factor_count(row),
            "boundary_program_sha256": boundary_programs,
        })

    payload = {
        "schema": "rate-half-kb-positive-433-1b-cell14-linear-pair-census-v1",
        "field": FIELD,
        "scope": (
            "All cell-14 outside cases in which the missing record is one of "
            "de,de,-de and the two residual de records are paired."
        ),
        "source_script_sha256": digest(SCRIPT),
        "source_curve_sha256": digest(CURVE),
        "input_sha256": {
            path.name: digest(path)
            for path in (PAIRING0, OPEN, BOUNDARY01, BOUNDARY2, REPLAY)
        },
        "logical_case_count": len(logical_rows),
        "open_ideal_count": 144,
        "boundary_ideal_count": 1632,
        "unit_ideal_count": 1776,
        "raw_outside_case_count": 1680,
        "excluded_outside_case_count": 144,
        "retained_outside_case_count": 1536,
        "timeout_replay": {
            "case": [list(replay_key[0]), list(replay_key[1]), *replay_key[2:]],
            "program_sha256": replay_row["program_sha256"],
        },
        "rows": logical_rows,
    }
    require(payload["logical_case_count"] == 144, "logical count")
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("cell14 linear-pair census: cases=144 open=144 boundary=1632 unit=1776")


if __name__ == "__main__":
    main()
