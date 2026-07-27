#!/usr/bin/env python3
"""Check the dual exact E24 cyclotomic norm ledger."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e24_six_profile_norm_modal.py"
COLLECT = HERE / "e24_six_profile_collect_result.json"
RESULT = HERE / "e24_six_profile_norm_result.json"


def main() -> None:
    packet = json.loads(RESULT.read_text())
    collection = json.loads(COLLECT.read_text())
    assert packet["schema"] == "e1-e24-six-profile-norm-v1"
    assert packet["complete"] is True and packet["agreement"] is True
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == packet["source_sha256"]
    assert hashlib.sha256(COLLECT.read_bytes()).hexdigest() == packet["collection_sha256"]
    assert packet["completed_flint_batches"] == packet["expected_batches"]
    assert packet["completed_pari_batches"] == packet["expected_batches"]

    vectors = [
        match for row in collection["rows"] for match in row["primary"]["matches"]
    ]
    assert packet["vectors"] == vectors
    flint = [int(value) for value in packet["flint_norms"]]
    pari = [int(value) for value in packet["pari_norms"]]
    assert len(flint) == len(vectors) == collection["summary"]["collected_full_conductor"]
    assert flint == pari and all(value > 0 for value in flint)
    summary = packet["summary"]
    maximum = max(flint)
    assert summary["vectors"] == len(vectors)
    assert summary["distinct_norms"] == len(set(flint))
    assert summary["maximum_norm"] == maximum
    assert summary["maximum_norm_bits"] == maximum.bit_length()
    assert summary["norm_at_or_above_2_250"] == sum(value >= 2**250 for value in flint)
    assert summary["maximizing_indices"] == [i for i, value in enumerate(flint) if value == maximum]
    assert maximum < 2**250

    mutated = list(pari)
    mutated[0] += 1
    assert mutated != flint
    assert 2*maximum < 2**251
    print(
        "E24_SIX_PROFILE_NORM_CHECK_PASS "
        f"vectors={len(vectors)} distinct={len(set(flint))} max={maximum} "
        f"bits={maximum.bit_length()} hits={summary['norm_at_or_above_2_250']} "
        "engines=2 mutations=2"
    )


if __name__ == "__main__":
    main()
