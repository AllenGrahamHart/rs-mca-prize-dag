#!/usr/bin/env python3
"""Checker for the staged generic q7 coefficient bank."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
GENERIC = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_t_julia_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q7_coefficients_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q7_coefficients_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
GENERIC_SHA256 = "c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e"
LABELS = ["a2m", "bm", "a2m_square", "bm_square", "D0", "D1", "D2"]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(GENERIC.read_bytes()).hexdigest() == GENERIC_SHA256,
            "generic custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-generic-q7-coefficients-v1",
            "schema")
    require(payload["collection_complete"] is True and payload["field"] == 2130706433
            and payload["source_cache_sha256"] == CACHE_SHA256
            and payload["source_generic_sha256"] == GENERIC_SHA256
            and payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest(), "envelope")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"} and
            row["relation"] == "generic staged FFF q7 coefficient bank" and
            row["engine"] == "AbstractAlgebra+Groebner.jl" and
            row["coefficient_field"] == "GF(2130706433)(t)" and
            row["fiber_variables"] == ["x", "r", "c", "b"] and
            row["source_basis_sha256"] ==
            "661fcbaa51996c4051f799c6ac3c56d95ea213f56305818ffedb6d0859531aa2" and
            row["source_quotient_dimension"] == 8 and row["value_labels"] == LABELS
            and row["q7_coefficient_labels"] == ["D0", "D1", "D2"] and
            row["transformation_denominators_open"] is True, "row input")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout")
        return row
    require(row["input_program"] == "" and
            [value["label"] for value in row["values"]] == LABELS and
            [value["label"] for value in row["profiles"]] == LABELS and
            all(value["polynomial"] and value["polynomial_sha256"] ==
                hashlib.sha256(value["polynomial"].encode()).hexdigest()
                for value in row["values"]), "values")
    canonical_values = [{"label": x["label"], "polynomial": x["polynomial"],
                         "polynomial_sha256": x["polynomial_sha256"]}
                        for x in row["values"]]
    canonical_entries = [{"label": x["label"], "term_index": x["term_index"],
                          "numerator": x["numerator"], "denominator": x["denominator"]}
                         for x in row["coefficient_entries"]]
    require(row["values_sha256"] == hashlib.sha256(
                json.dumps(canonical_values, separators=(",", ":")).encode()).hexdigest()
            and row["coefficient_entry_count"] == len(row["coefficient_entries"]) > 0
            and row["coefficient_entries_sha256"] == hashlib.sha256(
                json.dumps(canonical_entries, separators=(",", ":")).encode()).hexdigest()
            and row["unique_denominator_count"] == len(row["unique_denominators"]) > 0
            and row["unique_denominators_sha256"] == hashlib.sha256(
                json.dumps(row["unique_denominators"], separators=(",", ":")).encode()
            ).hexdigest(), "ledgers")
    return row


def expect_rejected(payload, label):
    try:
        verify(payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def hostile_audit():
    payload = json.loads(RESULT.read_text()); mutations = []
    mutation = deepcopy(payload); mutation["collection_complete"] = False
    mutations.append((mutation, "collection"))
    mutation = deepcopy(payload); mutation["row"]["q7_coefficient_labels"] = ["D2", "D1", "D0"]
    mutations.append((mutation, "labels"))
    mutation = deepcopy(payload); mutation["row"]["transformation_denominators_open"] = False
    mutations.append((mutation, "denominators"))
    if payload["row"]["status"] == "COMPLETE":
        mutation = deepcopy(payload); mutation["row"]["values"][0]["polynomial_sha256"] = "0" * 64
        mutations.append((mutation, "value"))
    for mutation, label in mutations:
        expect_rejected(mutation, label)
    return len(mutations)


def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args(); row = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_GENERIC_Q7_COEFFICIENTS_CHECK_PASS "
          f"status={row['status']} mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()
