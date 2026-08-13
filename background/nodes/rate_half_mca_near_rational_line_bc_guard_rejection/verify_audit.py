#!/usr/bin/env python3
"""Independent arithmetic audit of the #1160 BC-guard regression."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "dccd5b094d00570cca5c6b7453b20d7f190f53d733df2948fabc77c601eabfc0"


class Reject(ValueError):
    pass


def check(data: object) -> None:
    if not isinstance(data, dict):
        raise Reject("object")
    row = data.get("row")
    construction = data.get("construction")
    candidate = data.get("candidate_contract")
    if not all(isinstance(value, dict) for value in (row, construction, candidate)):
        raise Reject("records")
    fixed_row = (2130706433, 2097152, 1048576, 1048577, 1116048, 67472)
    if tuple(
        row.get(key)
        for key in (
            "base_prime",
            "domain_size",
            "code_dimension",
            "effective_locator_dimension",
            "agreement",
            "w",
        )
    ) != fixed_row:
        raise Reject("fixed row")
    _, _, k, effective_k, agreement, w = fixed_row
    support = construction.get("slope_word_support_size")
    degree = construction.get("support_locator_degree")
    slopes = construction.get("distinct_displayed_slopes")
    guard = candidate.get("minimum_shifted_degree_guard")
    if (
        effective_k != k + 1
        or w != agreement - k
        or support != w - 1
        or degree != support
        or support != agreement - effective_k
        or slopes != w
        or guard != support + 1
        or not degree < guard
        or construction.get("expected_accepted_displayed_slopes") != 0
    ):
        raise Reject("guard contradiction")


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != SHA256:
        raise Reject("contract hash")
    data = json.loads(CONTRACT.read_text())
    check(data)
    controls = []
    for section, key, value in (
        ("row", "agreement", 1116047),
        ("construction", "slope_word_support_size", 67472),
        ("candidate_contract", "minimum_shifted_degree_guard", 67471),
    ):
        altered = copy.deepcopy(data)
        altered[section][key] = value
        try:
            check(altered)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("audit controls")
    print(
        "RATE_HALF_MCA_NEAR_RATIONAL_LINE_BC_GUARD_REJECTION_AUDIT_PASS "
        f"checks=row,support,locator,shifted-degree,guard controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
