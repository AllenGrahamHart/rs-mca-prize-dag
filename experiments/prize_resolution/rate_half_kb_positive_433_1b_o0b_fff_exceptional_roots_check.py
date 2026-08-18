#!/usr/bin/env python3
"""Checker for the complete generic FFF exceptional-root ledger."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_roots_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_roots_result.json"
SOURCES = [
    HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_t_julia_result.json",
    HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_coefficients_julia_result.json",
    HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_c1_resume_result.json",
    HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_bank_extension_result.json",
    HERE / "rate_half_kb_positive_433_1b_o0b_fff_q5_multiplication_bank_result.json",
    HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_q7_coefficients_result.json",
    HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_polynomial_matrix_result.json",
    HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_ntt_determinant_result.json",
]
SOURCE_HASHES = [
    "c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e",
    "29a3236a322bf5ec1b797615fed99ccbb0b584981656eec04bd41da00989700c",
    "899f7706130a8ef3d6556ecc14aeda397868dcd8261db5f6df96c85519d3fc1c",
    "b5320657fc191da5adf2743ad020ab6a30934fd584f7f3f3a995caf9a712953c",
    "3d216da7d91c82a1360f932673ce3529278c90f81e6a8a6767f14a34ad73a45e",
    "37e2f17f8546e195024c23766f63cd36ba8681c115f3bf18f7410c19c902c45d",
    "ea218c257268a7887bf296dcb7d9e8f97ca3591866ca04e6595b3cd8170a0dae",
    "a222789bb3e54df1a4198536644a6d331972087d968b61b227634eca22a79786",
]
GROUP_LABELS = [
    "generic_basis_denominators", "q5_coefficient_denominators",
    "q5_extension_denominators", "q5_multiplication_denominators",
    "q7_coefficient_denominators", "r76_column_lcms", "r76_determinant",
]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    for path, digest in zip(SOURCES, SOURCE_HASHES):
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "source custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-exceptional-roots-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and
            payload["source_sha256"] == SOURCE_HASHES and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest(), "envelope")
    row = payload["row"]
    require(row["status"] == "COMPLETE" and
            row["relation"] == "complete generic FFF exceptional-polynomial ledger" and
            row["method"] == "LCM union then gcd(H,t^p-t) over the base field" and
            row["field"] == 2130706433 and row["group_labels"] == GROUP_LABELS and
            [group["label"] for group in row["groups"]] == GROUP_LABELS and
            row["source_generic_denominators_sha256"] ==
            "cf5f6cd0bcf52fbc0cd58e5da63d573cabdbea87bda7c91867a3d135ae7f1985" and
            row["source_q5_extension_denominators_sha256"] ==
            "125dfc37ef1bf4d8b093b66624408be8120299cc978ecef399f28cfb1df4ccdc" and
            row["source_q5_matrix_entries_sha256"] ==
            "29300862188e3e23b2b4a855c38ca82c0cc93c082932d6bff0fb517f7b71942e" and
            row["source_q5_kernel_entries_sha256"] ==
            "dbf9fcbbfede48c3e6f760afb409018303ff1251322c22f66a7b334e2dce8d31" and
            row["source_q7_denominators_sha256"] ==
            "8da469828f4c09bf015c708b153fdec7a50c5dac1f435c591d77d2c06dae9fdc" and
            row["source_column_lcms_sha256"] ==
            "eeafedd9b32a98a5c8e5b0c85af77d9a329256590baf292e91dceb4b6a97d6ad" and
            row["source_determinant_sha256"] ==
            "4f34c966c8cc12eb1b40227b9b7a7d6b232fba7990c2e55e09608cdbc3469ae5",
            "input")
    require(row["root_count"] == len(row["roots"]) and
            row["roots"] == sorted(set(row["roots"])) and
            len(row["field_root_polynomial"]) == row["root_count"] + 1 and
            row["field_root_polynomial"][-1] == 1 and
            row["field_root_polynomial_sha256"] == hashlib.sha256(
                json.dumps(row["field_root_polynomial"],
                           separators=(",", ":")).encode()).hexdigest() and
            row["global_unique_polynomial_count"] <=
            row["group_unique_polynomial_count"] <= row["raw_polynomial_count"] and
            row["global_lcm_degree"] >= row["root_count"] and
            all(group["root_count"] == len(group["roots"]) and
                group["roots"] == sorted(set(group["roots"])) and
                len(group["field_root_polynomial"]) == group["root_count"] + 1
                for group in row["groups"]) and
            row["roots"] == sorted({root for group in row["groups"]
                                    for root in group["roots"]}) and
            row["groups_sha256"] == hashlib.sha256(
                json.dumps(row["groups"], separators=(",", ":"),
                           sort_keys=True).encode()).hexdigest(), "roots")
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
    mutation["source_sha256"][0] = "0" * 64
    mutations.append((mutation, "source"))
    mutation = deepcopy(payload)
    mutation["row"]["group_labels"] = list(reversed(GROUP_LABELS))
    mutations.append((mutation, "groups"))
    mutation = deepcopy(payload)
    mutation["row"]["root_count"] += 1
    mutations.append((mutation, "count"))
    mutation = deepcopy(payload)
    mutation["row"]["field_root_polynomial_sha256"] = "0" * 64
    mutations.append((mutation, "polynomial"))
    for mutation, label in mutations:
        expect_rejected(mutation, label)
    return len(mutations)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    row = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_EXCEPTIONAL_ROOTS_CHECK_PASS "
          f"roots={row['root_count']} mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()
