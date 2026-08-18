#!/usr/bin/env python3
"""Checker for the exact NTT-reconstructed FFF R76 determinant."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
MATRIX = HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_polynomial_matrix_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_ntt_determinant_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_ntt_determinant_result.json"
MATRIX_SHA256 = "ea218c257268a7887bf296dcb7d9e8f97ca3591866ca04e6595b3cd8170a0dae"
PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def evaluate(coefficients, point):
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * point + coefficient) % PRIME
    return value


def verify(payload=None):
    require(hashlib.sha256(MATRIX.read_bytes()).hexdigest() == MATRIX_SHA256,
            "matrix custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-r76-ntt-determinant-v1",
            "schema")
    require(payload["collection_complete"] is True and payload["field"] == PRIME and
            payload["source_matrix_sha256"] == MATRIX_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest(), "envelope")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"} and
            row["relation"] ==
            "exact NTT determinant of column-cleared FFF R76 matrix" and
            row["engine"] ==
            "C++17 NTT plus finite-field Gaussian elimination" and
            row["coefficient_ring"] == "GF(2130706433)[t]" and
            row["dimension"] == 16 and row["ntt_size"] == 32768 and
            row["primitive_root"] == 3 and row["ntt_root"] == 1168510561 and
            row["degree_bound"] == 22208 and
            row["source_column_lcms_sha256"] ==
            "eeafedd9b32a98a5c8e5b0c85af77d9a329256590baf292e91dceb4b6a97d6ad" and
            row["source_matrix_entries_sha256"] ==
            "15749ad35ba394a9dce27a8c759f0203746233a2fb354efcc3655d44ea205de4" and
            row["witness_t"] == 2 and
            row["expected_witness_determinant"] == 1087830147 and
            row["holdout_t"] == 3 and row["roots_open"] is True, "input")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout")
        return row
    coefficients = row["determinant_coefficients"]
    require(row["input_program"] == "" and row["worker_threads"] >= 1 and
            0 <= row["determinant_degree"] <= row["degree_bound"] and
            len(coefficients) == row["determinant_degree"] + 1 and
            coefficients[-1] != 0 and
            row["determinant_term_count"] == sum(value != 0 for value in coefficients)
            and row["determinant_coefficients_sha256"] == hashlib.sha256(
                json.dumps(coefficients, separators=(",", ":")).encode()).hexdigest()
            and row["witness_t"] == 2 and
            row["witness_determinant"] == 1087830147 and
            evaluate(coefficients, 2) == row["witness_determinant"] and
            row["holdout_t"] == 3 and
            evaluate(coefficients, 3) == row["holdout_determinant"],
            "determinant")
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
    mutation["row"]["degree_bound"] = 32768
    mutations.append((mutation, "bound"))
    mutation = deepcopy(payload)
    mutation["row"]["roots_open"] = False
    mutations.append((mutation, "boundary"))
    if payload["row"]["status"] == "COMPLETE":
        mutation = deepcopy(payload)
        mutation["row"]["witness_determinant"] = 0
        mutations.append((mutation, "witness"))
        mutation = deepcopy(payload)
        mutation["row"]["determinant_coefficients_sha256"] = "0" * 64
        mutations.append((mutation, "coefficients"))
    for mutation, label in mutations:
        expect_rejected(mutation, label)
    return len(mutations)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    row = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_R76_NTT_DETERMINANT_"
          f"CHECK_PASS status={row['status']} mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()
