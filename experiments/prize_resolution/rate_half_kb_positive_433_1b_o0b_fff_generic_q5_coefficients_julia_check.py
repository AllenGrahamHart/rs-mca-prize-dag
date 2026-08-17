#!/usr/bin/env python3
"""Checker for the three generic q5 coefficient normal forms."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
Q5 = HERE / "rate_half_kb_positive_433_1b_o0b_fff_q5_coefficients_result.json"
GENERIC = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_t_julia_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_coefficients_julia_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_coefficients_julia_result.json"
Q5_SHA256 = "25b3ac23d74e0bb710c50d636048c0f95ea4b94d51f3c5e02634cbfdfddf5f6e"
GENERIC_SHA256 = "c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(Q5.read_bytes()).hexdigest() == Q5_SHA256,
            "q5 custody")
    require(hashlib.sha256(GENERIC.read_bytes()).hexdigest() == GENERIC_SHA256,
            "generic custody")
    q5 = json.loads(Q5.read_text())["row"]
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-generic-q5-coefficients-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and
            payload["source_q5_sha256"] == Q5_SHA256 and
            payload["source_generic_sha256"] == GENERIC_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest() and
            len(payload["rows"]) == 3, "envelope")
    for index, row in enumerate(payload["rows"]):
        require(row["status"] in {"COMPLETE", "TIMEOUT"} and
                row["relation"] ==
                "generic normal form of banked FFF q5 coefficient" and
                row["engine"] == "AbstractAlgebra+Groebner.jl" and
                row["coefficient_field"] == "GF(2130706433)(t)" and
                row["fiber_variables"] == ["x", "r", "c", "b"] and
                row["coefficient_index"] == index and
                row["source_polynomial_sha256"] ==
                q5["coefficients"][index]["polynomial_sha256"] and
                row["source_basis_sha256"] ==
                "661fcbaa51996c4051f799c6ac3c56d95ea213f56305818ffedb6d0859531aa2" and
                row["source_quotient_dimension"] == 8 and
                row["transformation_denominators_open"] is True, "row input")
        if row["status"] == "TIMEOUT":
            require(isinstance(row["partial_stdout"], str) and
                    isinstance(row["partial_stderr"], str), "timeout")
            continue
        require(row["input_program"] == "" and row["normal"] and
                row["normal_degree"] >= 0 and row["normal_term_count"] > 0 and
                row["normal_sha256"] == hashlib.sha256(row["normal"].encode()).hexdigest(),
                "normal")
        canonical_entries = [{
            "term_index": entry["term_index"],
            "numerator": entry["numerator"],
            "denominator": entry["denominator"],
        } for entry in row["coefficient_entries"]]
        entries_text = json.dumps(canonical_entries, separators=(",", ":"))
        denominators_text = json.dumps(row["unique_denominators"], separators=(",", ":"))
        require(row["coefficient_entry_count"] == len(row["coefficient_entries"]) > 0
                and row["coefficient_entries_sha256"] ==
                hashlib.sha256(entries_text.encode()).hexdigest() and
                row["unique_denominator_count"] == len(row["unique_denominators"]) > 0
                and row["unique_denominators_sha256"] ==
                hashlib.sha256(denominators_text.encode()).hexdigest(), "ledger")
    return payload["rows"]


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
    mutation["rows"][0]["coefficient_index"] = 2
    mutations.append((mutation, "index"))
    mutation = deepcopy(payload)
    mutation["rows"][0]["transformation_denominators_open"] = False
    mutations.append((mutation, "denominators"))
    complete = next((row for row in payload["rows"] if row["status"] == "COMPLETE"), None)
    if complete is not None:
        mutation = deepcopy(payload)
        index = next(i for i, row in enumerate(payload["rows"])
                     if row["status"] == "COMPLETE")
        mutation["rows"][index]["normal_sha256"] = "0" * 64
        mutations.append((mutation, "normal"))
    for mutation, label in mutations:
        expect_rejected(mutation, label)
    return len(mutations)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    rows = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_GENERIC_Q5_COEFFICIENTS_CHECK_PASS "
          f"statuses={[row['status'] for row in rows]} mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()
