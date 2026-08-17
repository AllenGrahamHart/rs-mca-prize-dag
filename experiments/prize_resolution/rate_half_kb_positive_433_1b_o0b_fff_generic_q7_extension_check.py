#!/usr/bin/env python3
"""Checker for the generic q5-q7 extension."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
Q5 = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_bank_extension_result.json"
Q7 = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q7_coefficients_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q7_extension_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q7_extension_result.json"
Q5_SHA256 = "b5320657fc191da5adf2743ad020ab6a30934fd584f7f3f3a995caf9a712953c"
Q7_SHA256 = "37e2f17f8546e195024c23766f63cd36ba8681c115f3bf18f7410c19c902c45d"
COEFFICIENT_HASHES = [
    "175919493e8500089bd1d528d2d768b83f9e47df021048ceea6ea637bf9a5b34",
    "1d7f55723f5a0cee8ebe409c879a480637a0b0bd6fa5fb9d2b4a95f25cb7f8dd",
    "d52a21d795e753e4aa04582fa3d67f65003a48b3406383db4a84730b528e961d",
]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(Q5.read_bytes()).hexdigest() == Q5_SHA256, "q5 custody")
    require(hashlib.sha256(Q7.read_bytes()).hexdigest() == Q7_SHA256, "q7 custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-generic-q7-extension-v1",
            "schema")
    require(payload["collection_complete"] is True and payload["field"] == 2130706433
            and payload["source_q5_sha256"] == Q5_SHA256
            and payload["source_q7_sha256"] == Q7_SHA256
            and payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest(), "envelope")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"} and
            row["relation"] == "generic admissible FFF q5-q7 extension" and
            row["engine"] == "AbstractAlgebra+Groebner.jl" and
            row["coefficient_field"] == "GF(2130706433)(t)" and
            row["fiber_variables"] == ["E", "s", "x", "r", "c", "b"] and
            row["source_basis_size"] == 16 and row["source_basis_sha256"] ==
            "bd4b2bf32d58c5f344d8d244eb2632646f0a7ca807bbefc5cf1c9c3737d6ab3b" and
            row["source_quotient_dimension"] == 16 and
            row["coefficient_hashes"] == COEFFICIENT_HASHES and
            row["equations"] == ["q5", "q7"] and
            row["transformation_denominators_open"] is True, "input")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout")
        return row
    require(row["input_program"] == "" and row["input_term_count"] == 24 and
            row["basis_size"] == len(row["basis"]) > 0 and
            row["unit"] == (row["basis"] == ["1"]) and
            ((row["unit"] and row["dimension"] == -1 and row["quotient_dimension"] == 0)
             or (not row["unit"] and row["dimension"] >= 0)), "profile")
    basis_text = "\n".join(row["basis"])
    canonical = [{"basis_index": x["basis_index"], "term_index": x["term_index"],
                  "numerator": x["numerator"], "denominator": x["denominator"]}
                 for x in row["coefficient_entries"]]
    require(row["basis_sha256"] == hashlib.sha256(basis_text.encode()).hexdigest()
            and row["coefficient_entry_count"] == len(row["coefficient_entries"]) > 0
            and row["coefficient_entries_sha256"] == hashlib.sha256(
                json.dumps(canonical, separators=(",", ":")).encode()).hexdigest()
            and row["unique_denominator_count"] == len(row["unique_denominators"]) > 0
            and row["unique_denominators_sha256"] == hashlib.sha256(
                json.dumps(row["unique_denominators"], separators=(",", ":")).encode()
            ).hexdigest(), "ledger")
    return row


def expect_rejected(payload, label):
    try:
        verify(payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def hostile_audit():
    payload = json.loads(RESULT.read_text()); mutations = []
    mutation = deepcopy(payload); mutation["source_q7_sha256"] = "0" * 64
    mutations.append((mutation, "source"))
    mutation = deepcopy(payload); mutation["row"]["equations"] = ["q7", "q5"]
    mutations.append((mutation, "equations"))
    mutation = deepcopy(payload); mutation["row"]["transformation_denominators_open"] = False
    mutations.append((mutation, "denominators"))
    if payload["row"]["status"] == "COMPLETE":
        mutation = deepcopy(payload); mutation["row"]["basis_sha256"] = "0" * 64
        mutations.append((mutation, "basis"))
    for mutation, label in mutations:
        expect_rejected(mutation, label)
    return len(mutations)


def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args(); row = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_GENERIC_Q7_EXTENSION_CHECK_PASS "
          f"status={row['status']} mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()
