#!/usr/bin/env python3
"""Check the dual exact E23 norm ledger."""

from __future__ import annotations

import hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
SOURCE=HERE/"e23_four_profile_norm_modal.py"
CENSUS=HERE/"e23_four_profile_census_result.json"
RESULT=HERE/"e23_four_profile_norm_result.json"


def main()->None:
    packet=json.loads(RESULT.read_text()); census=json.loads(CENSUS.read_text())
    assert packet["schema"]=="e1-e23-four-profile-norm-v1"
    assert packet["complete"] is True and packet["agreement"] is True
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==packet["source_sha256"]
    assert hashlib.sha256(CENSUS.read_bytes()).hexdigest()==packet["census_sha256"]
    assert packet["completed_flint_batches"]==packet["expected_batches"]
    assert packet["completed_pari_batches"]==packet["expected_batches"]
    vectors=[match for row in census["rows"] for match in row["primary"]["matches"]]
    assert packet["vectors"]==vectors
    flint=[int(v) for v in packet["flint_norms"]]; pari=[int(v) for v in packet["pari_norms"]]
    assert len(flint)==len(vectors)==census["summary"]["collected_full_conductor"]
    assert flint==pari and all(value>0 for value in flint)
    summary=packet["summary"]; maximum=max(flint)
    assert summary["vectors"]==len(vectors)
    assert summary["distinct_norms"]==len(set(flint))
    assert summary["maximum_norm"]==maximum
    assert summary["maximum_norm_bits"]==maximum.bit_length()
    assert summary["norm_at_or_above_2_250"]==sum(value>=2**250 for value in flint)
    assert summary["maximizing_indices"]==[i for i,value in enumerate(flint) if value==maximum]
    assert maximum<2**250
    mutated=list(pari); mutated[-1]+=1; assert mutated!=flint
    print("E23_FOUR_PROFILE_NORM_CHECK_PASS "
          f"vectors={len(vectors)} distinct={len(set(flint))} max={maximum} "
          f"bits={maximum.bit_length()} hits={summary['norm_at_or_above_2_250']} engines=2 mutations=1")


if __name__=="__main__":
    main()
