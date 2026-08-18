#!/usr/bin/env python3
"""Checker for the direct generic FFF R76 determinant."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
BANK = HERE / "rate_half_kb_positive_433_1b_o0b_fff_q5_multiplication_bank_result.json"
Q7 = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q7_coefficients_result.json"
BASE_PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_q6_block_determinant_program.py"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_multiplication_determinant_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_multiplication_determinant_result.json"
BANK_SHA256 = "3d216da7d91c82a1360f932673ce3529278c90f81e6a8a6767f14a34ad73a45e"
Q7_SHA256 = "37e2f17f8546e195024c23766f63cd36ba8681c115f3bf18f7410c19c902c45d"
BASE_PROGRAM_SHA256 = "fff178007fdea5ae7c14a0bee59fde6053aacc1a47f7a23f5d0c3bc654ab6224"
PRIME = 2130706433
EXPECTED_WITNESS = 244686406
DETERMINANT_LABELS = ["R76_NUM", "R76_DEN"]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    for path, digest in ((BANK, BANK_SHA256), (Q7, Q7_SHA256),
                         (BASE_PROGRAM, BASE_PROGRAM_SHA256)):
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "source custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-r76-multiplication-determinant-v1",
            "schema")
    require(payload["collection_complete"] is True and payload["field"] == PRIME and
            payload["source_bank_sha256"] == BANK_SHA256 and
            payload["source_q7_sha256"] == Q7_SHA256 and
            payload["source_base_program_sha256"] == BASE_PROGRAM_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest(), "envelope")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"} and
            row["relation"] ==
            "generic admissible FFF R76 multiplication determinant" and
            row["engine"] == "AbstractAlgebra.jl" and
            row["coefficient_field"] == "GF(2130706433)(t)" and
            row["quotient_dimension"] == 16 and
            row["matrix_relation"] == "R76=Res_E(q7,q6)" and
            row["source_base_generated_program_sha256"] ==
            "d6e3b1aae07a3e89f24c0b65b120d064f665541611dfa858de9db8fd55f754cd" and
            row["source_quotient_basis_sha256"] ==
            "aa3090c6c61b29e8a19f456d5a04b826423d9b08eb625d78c62b725ee00b5c8b" and
            row["source_matrix_entries_sha256"] ==
            "29300862188e3e23b2b4a855c38ca82c0cc93c082932d6bff0fb517f7b71942e" and
            row["source_kernel_normals_sha256"] ==
            "12ee5cd0578f1eff0f4a3827f7c905f1b04c390f74806c89a3a0a80178cca675" and
            row["source_q7_values_sha256"] ==
            "edf90ca1a3eb2563b6d56f00ff0b80b81a869846a7fe4984802e043fb6ab18a5" and
            row["witness_t"] == 2 and
            row["expected_witness_determinant"] == EXPECTED_WITNESS and
            row["transformation_denominators_open"] is True and
            row["symbolic_determinant_roots_open_until_complete"] is True,
            "input")
    require(row["witness_complete"] is True and row["witness_t"] == 2 and
            row["witness_determinant"] == EXPECTED_WITNESS and
            0 < row["witness_nonzero_entries"] <= 256, "witness")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout")
        return row
    require(row["input_program"] == "" and
            0 < row["symbolic_matrix_nonzero_entries"] <= 256 and
            row["symbolic_numerator_degree"] >= 0 and
            row["symbolic_denominator_degree"] >= 0 and
            [item["label"] for item in row["symbolic_determinants"]] ==
            DETERMINANT_LABELS and
            all(item["coefficients"] for item in row["symbolic_determinants"]),
            "symbolic result")
    canonical = [{"label": item["label"], "coefficients": item["coefficients"]}
                 for item in row["symbolic_determinants"]]
    require(row["symbolic_determinants_sha256"] == hashlib.sha256(
                json.dumps(canonical, separators=(",", ":")).encode()).hexdigest(),
            "determinant hash")
    values = {item["label"]: item["coefficients"]
              for item in row["symbolic_determinants"]}
    require(len(values["R76_NUM"]) == row["symbolic_numerator_degree"] + 1 and
            len(values["R76_DEN"]) == row["symbolic_denominator_degree"] + 1 and
            values["R76_NUM"][-1] != 0 and values["R76_DEN"][-1] != 0,
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
    mutation["row"]["witness_determinant"] = 0
    mutations.append((mutation, "witness"))
    mutation = deepcopy(payload)
    mutation["row"]["matrix_relation"] = "q7"
    mutations.append((mutation, "relation"))
    mutation = deepcopy(payload)
    mutation["row"]["transformation_denominators_open"] = False
    mutations.append((mutation, "denominators"))
    if payload["row"]["status"] == "COMPLETE":
        mutation = deepcopy(payload)
        mutation["row"]["symbolic_determinants_sha256"] = "0" * 64
        mutations.append((mutation, "determinant"))
    for mutation, label in mutations:
        expect_rejected(mutation, label)
    return len(mutations)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    row = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_R76_MULTIPLICATION_"
          f"DETERMINANT_CHECK_PASS status={row['status']} "
          f"witness={int(row['witness_complete'])} mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()
