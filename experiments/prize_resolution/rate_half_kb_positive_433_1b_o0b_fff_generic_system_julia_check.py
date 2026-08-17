#!/usr/bin/env python3
"""Outcome-neutral checker for the generic FFF necessary subsystem."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
GENERIC = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_t_julia_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_system_julia_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_system_julia_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
GENERIC_SHA256 = "c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e"


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
            "rate-half-kb-positive-433-1b-o0b-fff-generic-system-julia-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and
            payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_generic_sha256"] == GENERIC_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest(), "envelope")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"}, "status")
    require(row["relation"] ==
            "generic admissible FFF q5-q7-q6 necessary subsystem" and
            row["engine"] == "AbstractAlgebra+Groebner.jl" and
            row["coefficient_field"] == "GF(2130706433)(t)" and
            row["fiber_variables"] == ["E", "s", "x", "r", "c", "b"] and
            row["source_basis_size"] == 10 and
            row["source_basis_sha256"] ==
            "661fcbaa51996c4051f799c6ac3c56d95ea213f56305818ffedb6d0859531aa2" and
            row["source_quotient_dimension"] == 8 and
            row["equation_order"] == ["q5", "q7", "q6"] and
            row["omitted_finite_pair"] == "q4" and
            row["transformation_denominators_open"] is True and
            row["basis_denominator_roots_open"] is True, "input ledger")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout")
        return row
    require(row["input_program"] == "" and row["basis_size"] > 0 and
            len(row["basis"]) == row["basis_size"] and
            row["unit"] == (row["basis"] == ["1"]) and
            ((row["unit"] and row["dimension"] == -1 and
              row["quotient_dimension"] == 0) or
             (not row["unit"] and row["dimension"] >= 0)), "basis profile")
    basis_text = "\n".join(row["basis"])
    canonical_entries = [{
        "basis_index": entry["basis_index"],
        "term_index": entry["term_index"],
        "numerator": entry["numerator"],
        "denominator": entry["denominator"],
    } for entry in row["coefficient_entries"]]
    entries_text = json.dumps(canonical_entries, separators=(",", ":"))
    denominators_text = json.dumps(row["unique_denominators"], separators=(",", ":"))
    require(row["basis_sha256"] == hashlib.sha256(basis_text.encode()).hexdigest()
            and row["coefficient_entry_count"] ==
            len(row["coefficient_entries"]) > 0 and
            row["coefficient_entries_sha256"] ==
            hashlib.sha256(entries_text.encode()).hexdigest() and
            row["unique_denominator_count"] ==
            len(row["unique_denominators"]) > 0 and
            row["unique_denominators_sha256"] ==
            hashlib.sha256(denominators_text.encode()).hexdigest(), "hashes")
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
    mutation["collection_complete"] = False
    mutations.append((mutation, "collection"))
    mutation = deepcopy(payload)
    mutation["row"]["equation_order"] = ["q6", "q7", "q5"]
    mutations.append((mutation, "equations"))
    mutation = deepcopy(payload)
    mutation["row"]["transformation_denominators_open"] = False
    mutations.append((mutation, "denominators"))
    if payload["row"]["status"] == "COMPLETE":
        mutation = deepcopy(payload)
        mutation["row"]["basis_sha256"] = "0" * 64
        mutations.append((mutation, "basis"))
    for mutation, label in mutations:
        expect_rejected(mutation, label)
    return len(mutations)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    row = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_GENERIC_SYSTEM_JULIA_CHECK_PASS "
          f"status={row['status']} mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()
