#!/usr/bin/env python3
"""Audit the independent exact generic-gcd replay packet."""

import argparse
import hashlib
import json
import re
from pathlib import Path


HERE = Path(__file__).parent
RESULT = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd_audit_result.json"
)
EXPECTED_RESULT_SHA256 = (
    "e1651bf40f716eeef1daafab71b0f0b49a010d2d38395aa6ecde1d3e82b7bb81"
)
FACTORS = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization_result.json"
)
CERTIFICATE = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd_result.json"
)
MARKER = re.compile(
    r"COLORED_GENERIC_GCD_AUDIT_PASS factor=(\d+) "
    r"factor_degree=(\d+) common=(one|e2_minus_1)"
)
EXPECTED_PROGRAM_SHA256 = {
    1: "118e36206f215c7774fee5d79a25d4c4fefdeac918ca03d5d6508a096d20d95f",
    2: "509d2c78c79b446196aee2ab021b9320ae6c1ecc54d0a3d972fe8c589c96d1b5",
    3: "d9b5df1a105d61c9dd2ff8f815d8b9fb8e856535c21888a9dbd5c2f8497a574a",
    4: "1aeb759de824d5c15ea98c367d594975eb72fd95177662d967dfa81ebfecb3a1",
    5: "44daee2e4b4840f8bc4c91dd908b17e2217f30a46554452e2f05cde9b8221517",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(path=RESULT):
    raw = path.read_bytes()
    if path.resolve() == RESULT.resolve():
        require(
            hashlib.sha256(raw).hexdigest() == EXPECTED_RESULT_SHA256,
            "audit result packet hash mismatch",
        )
    payload = json.loads(raw)
    factors = json.loads(FACTORS.read_text())
    certificate = json.loads(CERTIFICATE.read_text())
    require(isinstance(payload, list) and len(payload) == 5, "audit shard count mismatch")
    require([row["factor"] for row in payload] == list(range(1, 6)),
            "audit factor coverage mismatch")
    factor_hash = hashlib.sha256(FACTORS.read_bytes()).hexdigest()
    certificate_hash = hashlib.sha256(CERTIFICATE.read_bytes()).hexdigest()
    markers = []
    for row in payload:
        index = row["factor"]
        require(row["status"] == "COMPLETE" and row["returncode"] == 0,
                f"factor {index} audit incomplete")
        require(row["factorization_sha256"] == factor_hash,
                "audit factorization provenance mismatch")
        require(row["certificate_sha256"] == certificate_hash,
                "audit certificate provenance mismatch")
        require(
            row["program_sha256"] == EXPECTED_PROGRAM_SHA256[index],
            "audit program hash mismatch",
        )
        match = MARKER.search(row["stdout"])
        require(match is not None and int(match.group(1)) == index,
                "audit marker mismatch")
        expected_degree = certificate[index - 1]["factor_degree"]
        expected_common = "one" if index == 4 else "e2_minus_1"
        require(int(match.group(2)) == expected_degree, "audit degree mismatch")
        require(match.group(3) == expected_common, "audit common-factor mismatch")
        markers.append(match.groups())
    return payload, markers


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--result", type=Path, default=RESULT)
    args = parser.parse_args()
    payload, markers = verify(args.result)
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_COLORED_GENERIC_GCD_AUDIT_PASS "
        f"factors={len(payload)} commons={','.join(row[2] for row in markers)}"
    )


if __name__ == "__main__":
    try:
        main()
    except (KeyError, RuntimeError, ValueError) as error:
        print(f"RATE_HALF_KB_POSITIVE_433_1A_CELL5_COLORED_GENERIC_GCD_AUDIT_FAIL {error}")
        raise SystemExit(1)
