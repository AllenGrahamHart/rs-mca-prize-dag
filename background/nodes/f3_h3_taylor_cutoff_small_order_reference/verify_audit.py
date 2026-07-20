#!/usr/bin/env python3
"""Mutation audit for the bounded C36 Taylor-cutoff reference."""

from __future__ import annotations

import copy
import tempfile
from pathlib import Path

import verify


def rejected(action) -> None:
    try:
        action()
    except (AssertionError, ValueError):
        return
    raise AssertionError("mutation was accepted")


def main() -> None:
    payload = verify.checked_packet()

    wrong_count = copy.deepcopy(payload)
    wrong_count["expected_blocks"] = 11
    rejected(lambda: verify.validate_payload(wrong_count))

    missing_block = copy.deepcopy(payload)
    missing_block["blocks"].pop()
    rejected(lambda: verify.validate_payload(missing_block))

    shifted_cutoff = copy.deepcopy(payload)
    shifted_cutoff["blocks"][0]["cutoffs"]["4"] = shifted_cutoff["blocks"][0][
        "cutoffs"
    ].pop("3")
    rejected(lambda: verify.validate_payload(shifted_cutoff))

    erased_support = copy.deepcopy(payload)
    for block in erased_support["blocks"]:
        block["cutoffs"]["2"]["odd_content"] = "1"
    rejected(lambda: verify.cross_check(erased_support))

    with tempfile.TemporaryDirectory() as directory:
        output = Path(directory) / "too-large.json"
        rejected(lambda: verify.reference.run_reference(5, [2], output, 1.0))

    with tempfile.TemporaryDirectory() as directory:
        output = Path(directory) / "partial.json"
        partial = verify.reference.run_reference(3, [2], output, 30.0, max_blocks=1)
        assert partial["complete"] is False
        assert partial["stage"] == "partial_selection"
        assert len(partial["blocks"]) == 1

    original = verify.reference.shifted_product_polynomial

    def synthetic_timeout(_exponent: int):
        raise verify.reference.ReferenceTimeout("synthetic timeout")

    try:
        verify.reference.shifted_product_polynomial = synthetic_timeout
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "timeout.json"
            timed_out = verify.reference.run_reference(3, [2], output, 30.0)
            assert timed_out["complete"] is False
            assert timed_out["stage"] == "timeout"
            assert timed_out["blocks"] == []
            assert "synthetic timeout" in timed_out["error"]
    finally:
        verify.reference.shifted_product_polynomial = original

    print(
        "F3_H3_TAYLOR_CUTOFF_SMALL_ORDER_REFERENCE_AUDIT_PASS "
        "mutations=7 timeout_fail_closed=1"
    )


if __name__ == "__main__":
    main()
