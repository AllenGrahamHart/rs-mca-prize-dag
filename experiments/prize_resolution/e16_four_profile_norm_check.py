#!/usr/bin/env python3
"""Check the dual exact E16 cyclotomic norm ledger."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e16_four_profile_norm_modal.py"
CENSUS = HERE / "e16_four_profile_census_result.json"
RESULT = HERE / "e16_four_profile_norm_result.json"


def main() -> None:
    packet = json.loads(RESULT.read_text())
    census = json.loads(CENSUS.read_text())
    assert packet["schema"] == "e1-e16-four-profile-norm-v1"
    assert packet["complete"] is True and packet["agreement"] is True
    assert packet["error"] is None
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == packet["source_sha256"]
    assert hashlib.sha256(CENSUS.read_bytes()).hexdigest() == packet["census_sha256"]
    assert packet["completed_flint"] == packet["expected_batches"]
    assert packet["completed_pari"] == packet["expected_batches"]
    vectors = [
        match for row in census["rows"] for match in row["primary"]["matches"]
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
    assert len(flint) == len(vectors) == census["summary"]["collected_full_conductor"]
    assert flint == pari and all(value > 0 for value in flint)
    summary = packet["summary"]
    maximum = max(flint)
    assert summary["vectors"] == len(vectors)
    assert summary["distinct_norms"] == len(set(flint))
    assert summary["maximum_norm"] == maximum
    assert summary["maximum_norm_bits"] == maximum.bit_length()
    hits = sum(value >= 2**250 for value in flint)
    assert summary["norms_at_or_above_2_250"] == hits
    assert summary["maximizing_indices"] == [
        index for index, value in enumerate(flint) if value == maximum
    ]
    profile_maxima = [
        max(
            (
                value
                for value, vector in zip(flint, vectors)
                if int(vector["profile"]) == profile
            ),
            default=0,
        )
        for profile in range(4)
    ]
    assert summary["profile_maximum_norms"] == profile_maxima
    assert summary["profile_maximum_bits"] == [value.bit_length() for value in profile_maxima]
    valuations = [(value & -value).bit_length() - 1 for value in flint]
    odd_parts = [value >> valuation for value, valuation in zip(flint, valuations)]
    profile_odd_maxima = [
        max(
            (
                value
                for value, vector in zip(odd_parts, vectors)
                if int(vector["profile"]) == profile
            ),
            default=0,
        )
        for profile in range(4)
    ]
    assert summary["maximum_odd_part"] == max(odd_parts)
    assert summary["maximum_odd_part_bits"] == max(odd_parts).bit_length()
    assert summary["odd_parts_at_or_above_2_250"] == sum(
        value >= 2**250 for value in odd_parts
    )
    assert summary["maximum_valuation"] == max(valuations)
    assert summary["profile_maximum_odd_parts"] == profile_odd_maxima
    assert summary["profile_maximum_odd_bits"] == [
        value.bit_length() for value in profile_odd_maxima
    ]
    assert summary["odd_part_maximizing_indices"] == [
        index for index, value in enumerate(odd_parts) if value == max(odd_parts)
    ]
    assert max(odd_parts) < 2**250
    mutated = list(pari)
    mutated[0] += 1
    assert mutated != flint
    print(
        "E16_FOUR_PROFILE_NORM_CHECK_PASS "
        f"vectors={len(vectors)} distinct={len(set(flint))} max={maximum} "
        f"bits={maximum.bit_length()} hits={hits} "
        f"odd_max={max(odd_parts)} odd_bits={max(odd_parts).bit_length()} "
        "odd_hits=0 engines=2 mutations=1"
    )


if __name__ == "__main__":
    main()
