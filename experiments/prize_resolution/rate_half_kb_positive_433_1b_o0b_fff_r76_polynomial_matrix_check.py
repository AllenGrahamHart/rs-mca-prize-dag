#!/usr/bin/env python3
"""Checker for the column-cleared FFF R76 polynomial-matrix bank."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
MATRIX = HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_matrix_bank_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_polynomial_matrix_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_polynomial_matrix_result.json"
MATRIX_SHA256 = "701f4a255f2f573b4f50d7bbf3ea14b80ae8562ae09d93f96a8409cb45babbfb"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(MATRIX.read_bytes()).hexdigest() == MATRIX_SHA256,
            "matrix custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-r76-polynomial-matrix-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and
            payload["source_matrix_sha256"] == MATRIX_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest(), "envelope")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"} and
            row["relation"] == "column-cleared generic admissible FFF R76 matrix" and
            row["engine"] == "AbstractAlgebra.jl" and
            row["coefficient_ring"] == "GF(2130706433)[t]" and
            row["dimension"] == 16 and row["clearing"] == "column LCM" and
            row["source_matrix_entries_sha256"] ==
            "24a8cc69a613bae3d367a087b524979de2bb8ec64174f97a2155c5227b7883f4" and
            row["source_unique_denominators_sha256"] ==
            "b9623adc3fe54844a3a61c3a4d06a80f51fab713f6813e9599c1038287f280cc" and
            row["source_witness_determinant"] == 244686406 and
            row["witness_t"] == 2 and
            row["expected_witness_determinant"] == 244686406 and
            row["determinant_open"] is True, "input")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout")
        return row
    require(row["input_program"] == "" and
            [item["column"] for item in row["column_lcm_profiles"]] ==
            list(range(1, 17)) and
            [item["column"] for item in row["column_lcms"]] ==
            list(range(1, 17)) and
            all(len(item["coefficients"]) == profile["degree"] + 1
                for item, profile in zip(row["column_lcms"],
                                         row["column_lcm_profiles"])) and
            row["matrix_nonzero_entry_count"] == len(row["matrix_entries"]) == 256 and
            {(item["row"], item["column"]) for item in row["matrix_entries"]} ==
            {(i, j) for i in range(1, 17) for j in range(1, 17)} and
            row["matrix_minimum_degree"] >= 0 and
            row["matrix_maximum_degree"] >= row["matrix_minimum_degree"] and
            row["witness_t"] == 2 and
            row["witness_rational_determinant"] == 244686406 and
            0 < row["witness_polynomial_determinant"] < 2130706433 and
            0 < row["witness_column_scaling"] < 2130706433 and
            row["witness_polynomial_determinant"] ==
            244686406 * row["witness_column_scaling"] % 2130706433,
            "bank")
    require(row["column_lcms_sha256"] == hashlib.sha256(
                json.dumps(row["column_lcms"], separators=(",", ":")).encode()
            ).hexdigest() and
            row["matrix_entries_sha256"] == hashlib.sha256(
                json.dumps(row["matrix_entries"], separators=(",", ":")).encode()
            ).hexdigest(), "hashes")
    return row


def expect_rejected(payload, label):
    try:
        verify(payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def hostile_audit():
    payload = json.loads(RESULT.read_text())
    mutations = []
    mutation = deepcopy(payload)
    mutation["source_matrix_sha256"] = "0" * 64
    mutations.append((mutation, "source"))
    mutation = deepcopy(payload)
    mutation["row"]["clearing"] = "global"
    mutations.append((mutation, "clearing"))
    mutation = deepcopy(payload)
    mutation["row"]["determinant_open"] = False
    mutations.append((mutation, "boundary"))
    if payload["row"]["status"] == "COMPLETE":
        mutation = deepcopy(payload)
        mutation["row"]["witness_polynomial_determinant"] = 0
        mutations.append((mutation, "witness"))
        mutation = deepcopy(payload)
        mutation["row"]["matrix_entries_sha256"] = "0" * 64
        mutations.append((mutation, "matrix"))
    for mutation, label in mutations:
        expect_rejected(mutation, label)
    return len(mutations)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    row = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_R76_POLYNOMIAL_MATRIX_"
          f"CHECK_PASS status={row['status']} mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()
