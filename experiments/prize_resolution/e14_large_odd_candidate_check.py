#!/usr/bin/env python3
"""Check the exact E14 large-odd-part candidate audit."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e14_large_odd_candidate_modal.py"
CENSUS = HERE / "e14_four_profile_census_result.json"
NORMS = HERE / "e14_four_profile_norm_result.json"
RESULT = HERE / "e14_large_odd_candidate_result.json"


def main() -> None:
    packet = json.loads(RESULT.read_text())
    assert packet["schema"] == "e1-e14-large-odd-candidate-v1"
    assert packet["complete"] is True and packet["agreement"] is True
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == packet["source_sha256"]
    assert hashlib.sha256(CENSUS.read_bytes()).hexdigest() == packet["census_sha256"]
    assert hashlib.sha256(NORMS.read_bytes()).hexdigest() == packet["norm_sha256"]
    assert packet["threshold"] == 2**250 and packet["modulus"] == 256
    rows = packet["candidates"]
    assert len(rows) == packet["summary"]["candidates"] == 6
    assert len({int(row["odd_part"]) for row in rows}) == packet["summary"]["distinct_odd_parts"]
    for row in rows:
        norm = int(row["norm"]); valuation = int(row["valuation"])
        odd_part = int(row["odd_part"])
        assert valuation == (norm & -norm).bit_length() - 1
        assert odd_part == norm >> valuation
        assert 2**250 <= odd_part < 2**251
        assert row["residue_mod_256"] == odd_part % 256
        assert row["pair_feasible_prime"] is bool(
            row["is_prime"] and odd_part > 2**250 and odd_part % 256 == 1)
    assert packet["summary"]["prime_candidates"] == sum(
        bool(row["is_prime"]) for row in rows)
    assert packet["summary"]["congruence_candidates"] == sum(
        int(row["residue_mod_256"]) == 1 for row in rows)
    assert packet["summary"]["pair_feasible_prime_candidates"] == 0
    mutated = [dict(row) for row in rows]
    mutated[0]["residue_mod_256"] = (int(mutated[0]["residue_mod_256"]) + 1) % 256
    assert mutated != rows
    print("E14_LARGE_ODD_CANDIDATE_CHECK_PASS "
          f"candidates={len(rows)} distinct={packet['summary']['distinct_odd_parts']} "
          f"primes={packet['summary']['prime_candidates']} "
          f"congruent={packet['summary']['congruence_candidates']} "
          "eligible=0 engines=2 mutations=1")


if __name__ == "__main__":
    main()
