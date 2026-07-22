#!/usr/bin/env python3
"""Deterministically replay the bounded HNF toy gcd certificate."""

import json
from pathlib import Path

from l1_mersenne_hnf_toy_gcd_modal import classify


HERE = Path(__file__).resolve().parent
certificate = json.loads((HERE / "l1_mersenne_hnf_toy_gcd_result.json").read_text())
replayed = classify(certificate["p"], certificate["m"])
assert replayed["payload_sha256"] == certificate["payload_sha256"]
for key in (
    "p",
    "m",
    "h",
    "n",
    "common_gcd",
    "prime_field_part",
    "outside_prime_field",
    "outside_factors",
):
    assert replayed[key] == certificate[key]
assert certificate["app_id"] == "ap-gT0DyToHmnD911PEFFilTd"
assert 0 < certificate["worker_seconds"] < 120

outside = certificate["outside_prime_field"]
status = "EMPTY_OUTSIDE_FP" if outside == [1] else "OUTSIDE_FP_SURVIVOR"
print(
    "L1_MERSENNE_HNF_TOY_GCD_CERTIFICATE_PASS "
    f"status={status} degree={len(outside) - 1} "
    f"seconds={certificate['worker_seconds']}"
)
