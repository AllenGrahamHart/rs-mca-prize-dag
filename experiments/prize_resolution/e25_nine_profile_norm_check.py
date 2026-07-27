#!/usr/bin/env python3
"""Check the dual exact E25 exceptional-norm packet."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CENSUS = HERE / "e25_nine_profile_census_result.json"
SOURCE = HERE / "e25_nine_profile_norm_modal.py"
RESULT = HERE / "e25_nine_profile_norm_result.json"


def flatten(rows: list[dict[str, object]], batches: int, final_size: int) -> list[int]:
    assert len(rows) == batches
    values: list[int] = []
    for batch, row in enumerate(sorted(rows, key=lambda item: int(item["batch"]))):
        assert int(row["batch"]) == batch
        expected = final_size if batch == batches - 1 else 1_000
        assert len(row["norms"]) == expected
        values.extend(int(value) for value in row["norms"])
    return values


def main() -> None:
    census = json.loads(CENSUS.read_text())
    vectors = [
        vector
        for row in census["production"]
        for vector in row["matches"]
        if int(vector["conductor"]) == 1
    ]
    assert len(vectors) == 16_984

    packet = json.loads(RESULT.read_text())
    assert packet["schema"] == "e1-e25-nine-profile-norm-v1"
    assert packet["complete"] is packet["agreement"] is True
    assert packet["error"] is None
    assert packet["vectors"] == len(vectors)
    assert packet["batch_size"] == 1_000
    assert packet["expected_batches"] == packet["completed_flint"] == packet["completed_pari"] == 17
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == packet["source_sha256"]
    assert hashlib.sha256(CENSUS.read_bytes()).hexdigest() == packet["census_sha256"]
    flint_norms = flatten(packet["flint"], 17, 984)
    pari_norms = flatten(packet["pari"], 17, 984)
    assert flint_norms == pari_norms and len(flint_norms) == len(vectors)

    summary = packet["summary"]
    assert summary["vectors"] == len(vectors)
    assert summary["distinct_norms"] == len(set(flint_norms))
    assert summary["maximum_norm"] == max(flint_norms)
    assert summary["maximum_norm_bits"] == max(flint_norms).bit_length()
    assert summary["norms_at_or_above_2_250"] == sum(value >= 2**250 for value in flint_norms)
    maxima = [
        max(
            (norm for norm, vector in zip(flint_norms, vectors) if int(vector["profile"]) == profile),
            default=-1,
        )
        for profile in range(9)
    ]
    assert summary["profile_maximum_norms"] == maxima
    assert summary["profile_maximum_bits"] == [value.bit_length() if value >= 0 else -1 for value in maxima]

    valuations = [(norm & -norm).bit_length() - 1 for norm in flint_norms]
    odd_parts = [norm >> valuation for norm, valuation in zip(flint_norms, valuations)]
    eligible = {value for value in odd_parts if 2**250 < value < 2**256}
    assert summary["eligible_distinct_odd_parts"] == len(eligible)
    assert len(packet["candidate_records"]) == summary["candidate_vectors"]
    assert [int(row["index"]) for row in packet["candidate_records"]] == summary["candidate_indices"]
    for row in packet["candidate_records"]:
        index = int(row["index"])
        assert row["vector"] == vectors[index]
        assert int(row["norm"]) == flint_norms[index]
        assert int(row["valuation"]) == valuations[index]
        assert int(row["odd_part"]) == odd_parts[index]

    source = SOURCE.read_text()
    assert "python-flint" in source and "polresultant" in source
    print(
        "E25_NINE_PROFILE_NORM_CHECK_PASS "
        f"vectors={len(vectors)} distinct={len(set(flint_norms))} "
        f"max_bits={max(flint_norms).bit_length()} candidates={summary['candidate_vectors']} engines=2"
    )


if __name__ == "__main__":
    main()
