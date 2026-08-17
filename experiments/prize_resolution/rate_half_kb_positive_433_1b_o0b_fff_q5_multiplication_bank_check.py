#!/usr/bin/env python3
"""Checker for the q5 quotient multiplication bank."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
GENERIC = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_t_julia_result.json"
Q5 = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_bank_extension_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_q5_multiplication_bank_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_q5_multiplication_bank_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
GENERIC_SHA256 = "c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e"
Q5_SHA256 = "b5320657fc191da5adf2743ad020ab6a30934fd584f7f3f3a995caf9a712953c"
MATRIX_LABELS = ["s", "x", "r", "c", "b"]
KERNEL_LABELS = [f"k{index}" for index in range(6)]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    for path, digest in ((CACHE, CACHE_SHA256), (GENERIC, GENERIC_SHA256),
                         (Q5, Q5_SHA256)):
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest, "custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-q5-multiplication-bank-v1",
            "schema")
    require(payload["collection_complete"] is True and payload["field"] == 2130706433
            and payload["source_cache_sha256"] == CACHE_SHA256
            and payload["source_generic_sha256"] == GENERIC_SHA256
            and payload["source_q5_sha256"] == Q5_SHA256
            and payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest(), "envelope")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"} and
            row["relation"] == "generic q5 quotient multiplication bank" and
            row["engine"] == "AbstractAlgebra+Groebner.jl" and
            row["coefficient_field"] == "GF(2130706433)(t)" and
            row["quotient_variables"] == MATRIX_LABELS and
            row["matrix_labels"] == MATRIX_LABELS and
            row["kernel_labels"] == KERNEL_LABELS and
            row["source_basis_size"] == 16 and row["source_basis_sha256"] ==
            "bd4b2bf32d58c5f344d8d244eb2632646f0a7ca807bbefc5cf1c9c3737d6ab3b" and
            row["source_quotient_dimension"] == 16 and
            row["commutation_required"] is True and
            row["transformation_denominators_open"] is True, "input")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout")
        return row
    require(row["input_program"] == "" and row["quotient_dimension"] == 16 and
            row["matrix_count"] == 5 and
            len(row["quotient_basis"]) == 16 and
            row["matrix_nonzero_entry_count"] == len(row["matrix_entries"]) > 0
            and [x["label"] for x in row["kernel_normals"]] == KERNEL_LABELS and
            [x["label"] for x in row["kernel_profiles"]] == KERNEL_LABELS,
            "profile")
    require(all(x["label"] in MATRIX_LABELS and 1 <= x["row"] <= 16 and
                1 <= x["column"] <= 16 and x["numerator"] and x["denominator"]
                for x in row["matrix_entries"]), "matrix entries")
    require(all(x["polynomial"] and x["polynomial_sha256"] ==
                hashlib.sha256(x["polynomial"].encode()).hexdigest()
                for x in row["kernel_normals"]), "kernel normals")
    canonical_m = [{"label": x["label"], "row": x["row"], "column": x["column"],
                    "numerator": x["numerator"], "denominator": x["denominator"]}
                   for x in row["matrix_entries"]]
    canonical_kn = [{"label": x["label"], "polynomial": x["polynomial"],
                     "polynomial_sha256": x["polynomial_sha256"]}
                    for x in row["kernel_normals"]]
    canonical_ke = [{"label": x["label"], "term_index": x["term_index"],
                     "numerator": x["numerator"], "denominator": x["denominator"]}
                    for x in row["kernel_entries"]]
    require(row["quotient_basis_sha256"] == hashlib.sha256(
                "\n".join(row["quotient_basis"]).encode()).hexdigest()
            and row["matrix_entries_sha256"] == hashlib.sha256(
                json.dumps(canonical_m, separators=(",", ":")).encode()).hexdigest()
            and row["kernel_normals_sha256"] == hashlib.sha256(
                json.dumps(canonical_kn, separators=(",", ":")).encode()).hexdigest()
            and row["kernel_entries_sha256"] == hashlib.sha256(
                json.dumps(canonical_ke, separators=(",", ":")).encode()).hexdigest(),
            "hashes")
    return row


def expect_rejected(payload, label):
    try:
        verify(payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def hostile_audit():
    payload = json.loads(RESULT.read_text()); mutations = []
    mutation = deepcopy(payload); mutation["source_q5_sha256"] = "0" * 64
    mutations.append((mutation, "source"))
    mutation = deepcopy(payload); mutation["row"]["matrix_labels"] = list(reversed(MATRIX_LABELS))
    mutations.append((mutation, "labels"))
    mutation = deepcopy(payload); mutation["row"]["commutation_required"] = False
    mutations.append((mutation, "commutation"))
    if payload["row"]["status"] == "COMPLETE":
        mutation = deepcopy(payload); mutation["row"]["quotient_basis_sha256"] = "0" * 64
        mutations.append((mutation, "basis"))
    for mutation, label in mutations:
        expect_rejected(mutation, label)
    return len(mutations)


def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args(); row = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_Q5_MULTIPLICATION_BANK_CHECK_PASS "
          f"status={row['status']} mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()
