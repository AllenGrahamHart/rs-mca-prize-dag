#!/usr/bin/env python3
"""Checker for the bounded long-wall generic q5 C1 retry."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
Q5 = HERE / "rate_half_kb_positive_433_1b_o0b_fff_q5_coefficients_result.json"
GENERIC = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_t_julia_result.json"
FRONTIER = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_coefficients_julia_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_coefficients_julia_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_c1_resume_result.json"
Q5_SHA256 = "25b3ac23d74e0bb710c50d636048c0f95ea4b94d51f3c5e02634cbfdfddf5f6e"
GENERIC_SHA256 = "c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e"
FRONTIER_SHA256 = "29a3236a322bf5ec1b797615fed99ccbb0b584981656eec04bd41da00989700c"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(Q5.read_bytes()).hexdigest() == Q5_SHA256,
            "q5 custody")
    require(hashlib.sha256(GENERIC.read_bytes()).hexdigest() == GENERIC_SHA256,
            "generic custody")
    require(hashlib.sha256(FRONTIER.read_bytes()).hexdigest() == FRONTIER_SHA256,
            "frontier custody")
    source = json.loads(Q5.read_text())["row"]["coefficients"][1]
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-generic-q5-c1-resume-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and
            payload["source_q5_sha256"] == Q5_SHA256 and
            payload["source_generic_sha256"] == GENERIC_SHA256 and
            payload["source_frontier_sha256"] == FRONTIER_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest(), "envelope")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"} and
            row["relation"] ==
            "generic normal form of banked FFF q5 coefficient" and
            row["coefficient_index"] == 1 and
            row["source_polynomial_sha256"] == source["polynomial_sha256"] and
            row["source_basis_sha256"] ==
            "661fcbaa51996c4051f799c6ac3c56d95ea213f56305818ffedb6d0859531aa2" and
            row["source_quotient_dimension"] == 8 and
            row["transformation_denominators_open"] is True, "row")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout")
        return row
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
            and row["coefficient_entries_sha256"] == hashlib.sha256(entries_text.encode()).hexdigest()
            and row["unique_denominator_count"] == len(row["unique_denominators"]) > 0
            and row["unique_denominators_sha256"] ==
            hashlib.sha256(denominators_text.encode()).hexdigest(), "ledger")
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
    mutation["source_frontier_sha256"] = "0" * 64
    mutations.append((mutation, "frontier"))
    mutation = deepcopy(payload)
    mutation["row"]["coefficient_index"] = 0
    mutations.append((mutation, "index"))
    mutation = deepcopy(payload)
    mutation["row"]["transformation_denominators_open"] = False
    mutations.append((mutation, "denominators"))
    if payload["row"]["status"] == "COMPLETE":
        mutation = deepcopy(payload)
        mutation["row"]["normal_sha256"] = "0" * 64
        mutations.append((mutation, "normal"))
    for mutation, label in mutations:
        expect_rejected(mutation, label)
    return len(mutations)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    row = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_GENERIC_Q5_C1_RESUME_CHECK_PASS "
          f"status={row['status']} mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()
