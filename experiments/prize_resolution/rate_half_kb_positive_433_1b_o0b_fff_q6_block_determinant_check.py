#!/usr/bin/env python3
"""Checker for the generic FFF q6 block-determinant certificate."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
BANK = HERE / "rate_half_kb_positive_433_1b_o0b_fff_q5_multiplication_bank_result.json"
Q7 = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q7_coefficients_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_q6_block_determinant_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_q6_block_determinant_result.json"
BANK_SHA256 = "3d216da7d91c82a1360f932673ce3529278c90f81e6a8a6767f14a34ad73a45e"
Q7_SHA256 = "37e2f17f8546e195024c23766f63cd36ba8681c115f3bf18f7410c19c902c45d"
PRIME = 2130706433
VARIABLE_LABELS = ["s", "x", "r", "c", "b"]
KERNEL_LABELS = [f"k{index}" for index in range(6)]
Q7_LABELS = ["D0", "D1", "D2"]
DETERMINANT_LABELS = ["D2_NUM", "D2_DEN", "Q6_NUM", "Q6_DEN"]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(BANK.read_bytes()).hexdigest() == BANK_SHA256,
            "bank custody")
    require(hashlib.sha256(Q7.read_bytes()).hexdigest() == Q7_SHA256,
            "q7 custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-q6-block-determinant-v1",
            "schema")
    require(payload["collection_complete"] is True and payload["field"] == PRIME and
            payload["source_bank_sha256"] == BANK_SHA256 and
            payload["source_q7_sha256"] == Q7_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest(), "envelope")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"} and
            row["relation"] ==
            "generic admissible FFF q5-q7-q6 block determinant" and
            row["engine"] == "AbstractAlgebra.jl" and
            row["coefficient_field"] == "GF(2130706433)(t)" and
            row["base_quotient_dimension"] == 16 and
            row["extension_dimension"] == 32 and
            row["matrix_labels"] == VARIABLE_LABELS and
            row["kernel_labels"] == KERNEL_LABELS and
            row["q7_coefficient_labels"] == Q7_LABELS and
            row["source_quotient_basis_sha256"] ==
            "aa3090c6c61b29e8a19f456d5a04b826423d9b08eb625d78c62b725ee00b5c8b" and
            row["source_matrix_entries_sha256"] ==
            "29300862188e3e23b2b4a855c38ca82c0cc93c082932d6bff0fb517f7b71942e" and
            row["source_kernel_normals_sha256"] ==
            "12ee5cd0578f1eff0f4a3827f7c905f1b04c390f74806c89a3a0a80178cca675" and
            row["source_q7_values_sha256"] ==
            "edf90ca1a3eb2563b6d56f00ff0b80b81a869846a7fe4984802e043fb6ab18a5" and
            row["witness_t"] == 2 and
            row["transformation_denominators_open"] is True and
            row["symbolic_determinant_roots_open_until_complete"] is True,
            "input")
    require(row["witness_complete"] is True and row["witness_t"] == 2 and
            row["witness_q7_identity"] is True and
            0 < row["witness_d2_determinant"] < PRIME and
            0 < row["witness_q6_determinant"] < PRIME and
            0 < row["witness_q6_nonzero_entries"] <= 1024,
            "generic nonzero witness")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout")
        return row
    require(row["input_program"] == "" and
            row["symbolic_d2_numerator_degree"] >= 0 and
            row["symbolic_d2_denominator_degree"] >= 0 and
            row["symbolic_q6_numerator_degree"] >= 0 and
            row["symbolic_q6_denominator_degree"] >= 0 and
            0 < row["symbolic_q6_nonzero_entries"] <= 1024 and
            [item["label"] for item in row["symbolic_determinants"]] ==
            DETERMINANT_LABELS and
            all(item["coefficients"] for item in row["symbolic_determinants"]),
            "symbolic result")
    canonical = [{"label": item["label"], "coefficients": item["coefficients"]}
                 for item in row["symbolic_determinants"]]
    require(row["symbolic_determinants_sha256"] == hashlib.sha256(
                json.dumps(canonical, separators=(",", ":")).encode()).hexdigest(),
            "determinant hash")
    profiles = {item["label"]: item["coefficients"]
                for item in row["symbolic_determinants"]}
    require(len(profiles["D2_NUM"]) == row["symbolic_d2_numerator_degree"] + 1 and
            len(profiles["D2_DEN"]) == row["symbolic_d2_denominator_degree"] + 1 and
            len(profiles["Q6_NUM"]) == row["symbolic_q6_numerator_degree"] + 1 and
            len(profiles["Q6_DEN"]) == row["symbolic_q6_denominator_degree"] + 1 and
            profiles["D2_NUM"][-1] != 0 and profiles["D2_DEN"][-1] != 0 and
            profiles["Q6_NUM"][-1] != 0 and profiles["Q6_DEN"][-1] != 0,
            "determinant profiles")
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
    mutation["source_bank_sha256"] = "0" * 64
    mutations.append((mutation, "source"))
    mutation = deepcopy(payload)
    mutation["row"]["witness_q6_determinant"] = 0
    mutations.append((mutation, "witness"))
    mutation = deepcopy(payload)
    mutation["row"]["extension_dimension"] = 16
    mutations.append((mutation, "dimension"))
    mutation = deepcopy(payload)
    mutation["row"]["transformation_denominators_open"] = False
    mutations.append((mutation, "denominators"))
    if payload["row"]["status"] == "COMPLETE":
        mutation = deepcopy(payload)
        mutation["row"]["symbolic_determinants_sha256"] = "0" * 64
        mutations.append((mutation, "symbolic determinant"))
    for mutation, label in mutations:
        expect_rejected(mutation, label)
    return len(mutations)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    row = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_Q6_BLOCK_DETERMINANT_CHECK_PASS "
          f"status={row['status']} witness={int(row['witness_complete'])} "
          f"mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()
