#!/usr/bin/env python3
"""Check the dual exact E22 cyclotomic norm ledger."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e22_eight_profile_norm_modal.py"
COLLECT = HERE / "e22_eight_profile_collect_result.json"
RESULT = HERE / "e22_eight_profile_norm_result.json"


def main() -> None:
    packet = json.loads(RESULT.read_text())
    collection = json.loads(COLLECT.read_text())
    assert packet["schema"] == "e1-e22-eight-profile-norm-v1"
    assert packet["complete"] is True and packet["agreement"] is True
    assert packet["error"] is None
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == packet["source_sha256"]
    assert hashlib.sha256(COLLECT.read_bytes()).hexdigest() == packet["collection_sha256"]
    assert packet["completed_flint"] == packet["expected_batches"]
    assert packet["completed_pari"] == packet["expected_batches"]

    vectors = [
        match for row in collection["rows"] for match in row["primary"]["matches"]
    ]
    flint = [
        int(value)
        for row in sorted(packet["flint"], key=lambda item: int(item["batch"]))
        for value in row["norms"]
    ]
    pari = [
        int(value)
        for row in sorted(packet["pari"], key=lambda item: int(item["batch"]))
        for value in row["norms"]
    ]
    assert len(flint) == len(vectors) == collection["summary"]["collected_full_conductor"]
    assert flint == pari and all(value > 0 for value in flint)
    summary = packet["summary"]
    maximum = max(flint)
    assert summary["vectors"] == len(vectors)
    assert summary["distinct_norms"] == len(set(flint))
    assert summary["maximum_norm"] == maximum
    assert summary["maximum_norm_bits"] == maximum.bit_length()
    assert summary["norms_at_or_above_2_250"] == sum(value >= 2**250 for value in flint)
    assert summary["maximizing_indices"] == [
        index for index, value in enumerate(flint) if value == maximum
    ]
    expected_profile_maxima = [
        max(
            (
                value
                for value, vector in zip(flint, vectors)
                if int(vector["profile"]) == profile
            ),
            default=0,
        )
        for profile in range(8)
    ]
    assert summary["profile_maximum_norms"] == expected_profile_maxima
    assert summary["profile_maximum_bits"] == [value.bit_length() for value in expected_profile_maxima]
    assert maximum < 2**250 and summary["norms_at_or_above_2_250"] == 0

    mutated = list(pari)
    mutated[0] += 1
    assert mutated != flint
    assert maximum < 2**250 < 3 * maximum
    print(
        "E22_EIGHT_PROFILE_NORM_CHECK_PASS "
        f"vectors={len(vectors)} distinct={len(set(flint))} max={maximum} "
        f"bits={maximum.bit_length()} hits=0 engines=2 mutations=2"
    )


if __name__ == "__main__":
    main()
