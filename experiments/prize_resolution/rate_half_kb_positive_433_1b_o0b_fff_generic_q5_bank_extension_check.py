#!/usr/bin/env python3
"""Checker for the generic q5 coefficient-bank extension."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
GENERIC = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_t_julia_result.json"
FRONTIER = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_coefficients_julia_result.json"
C1 = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_c1_resume_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_bank_extension_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_bank_extension_result.json"
GENERIC_SHA256 = "c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e"
FRONTIER_SHA256 = "29a3236a322bf5ec1b797615fed99ccbb0b584981656eec04bd41da00989700c"
C1_SHA256 = "899f7706130a8ef3d6556ecc14aeda397868dcd8261db5f6df96c85519d3fc1c"
NORMAL_HASHES = [
    "e008780fd3d46e30c2471900384068de9b384cf3f3a99fbb038d00364b3428c3",
    "76be8227ceaae91dd6e96df64fbc80ee40f058fb9bb94bebaf7f69df66ee702d",
    "e890823e9f38e2919f38a73bcd0b7d20c52882e5ea069a05abfa147f637f8ce8",
]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    for path, digest in ((GENERIC, GENERIC_SHA256), (FRONTIER, FRONTIER_SHA256),
                         (C1, C1_SHA256)):
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest, "custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-generic-q5-bank-extension-v1",
            "schema")
    require(payload["collection_complete"] is True and payload["field"] == 2130706433
            and payload["source_generic_sha256"] == GENERIC_SHA256
            and payload["source_frontier_sha256"] == FRONTIER_SHA256
            and payload["source_c1_sha256"] == C1_SHA256
            and payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest(), "envelope")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"} and
            row["relation"] ==
            "generic admissible FFF q5 coefficient-bank extension" and
            row["engine"] == "AbstractAlgebra+Groebner.jl" and
            row["coefficient_field"] == "GF(2130706433)(t)" and
            row["fiber_variables"] == ["s", "x", "r", "c", "b"] and
            row["source_basis_size"] == 10 and row["source_quotient_dimension"] == 8
            and row["coefficient_normal_hashes"] == NORMAL_HASHES and
            row["equation"] == "q5" and
            row["transformation_denominators_open"] is True, "row input")
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
    entries_text = json.dumps(canonical, separators=(",", ":"))
    denominators_text = json.dumps(row["unique_denominators"], separators=(",", ":"))
    require(row["basis_sha256"] == hashlib.sha256(basis_text.encode()).hexdigest()
            and row["coefficient_entry_count"] == len(row["coefficient_entries"]) > 0
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
    mutation = deepcopy(payload); mutation["source_c1_sha256"] = "0" * 64
    mutations.append((mutation, "c1"))
    mutation = deepcopy(payload); mutation["row"]["coefficient_normal_hashes"][1] = "0" * 64
    mutations.append((mutation, "normal"))
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
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_GENERIC_Q5_BANK_EXTENSION_CHECK_PASS "
          f"status={row['status']} mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()
