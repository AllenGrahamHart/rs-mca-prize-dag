#!/usr/bin/env python3
"""Mutation audit for the c=1 parity harmonic exclusion packet."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
EXPERIMENT = ROOT / "experiments" / "prize_resolution"
RESULT = (
    EXPERIMENT
    / "rate_half_list_fiber_two_cycle_c1_parity_harmonic_characteristic_result.json"
)
SOURCE = (
    EXPERIMENT
    / "rate_half_list_fiber_two_cycle_c1_parity_harmonic_characteristic_modal.py"
)


def main() -> None:
    packet = json.loads(RESULT.read_text())
    assert packet["hits"] == []
    assert packet["processed"] == packet["expected_candidates"]
    assert packet["source_sha256"] == hashlib.sha256(SOURCE.read_bytes()).hexdigest()

    mutated_hits = [{"branch": "H_R", "k": packet["k_start"]}]
    assert mutated_hits != packet["hits"]
    assert packet["processed"] - 1 != packet["expected_candidates"]
    assert hashlib.sha256(SOURCE.read_bytes() + b"\n").hexdigest() != packet[
        "source_sha256"
    ]

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_PARITY_HARMONIC_EXCLUSION_AUDIT_PASS "
        "mutations=3"
    )


if __name__ == "__main__":
    main()

