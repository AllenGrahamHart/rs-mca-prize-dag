#!/usr/bin/env python3
"""Independent contract and boundary audit for the CS supplier."""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE_DIR = Path(__file__).resolve().parent
PILOT = ROOT / "notes/pilots_20260806/cs_transport"


def margin(w: int) -> Decimal:
    n = 2**41
    r = 2**40 - w
    log2_r = Decimal(r).ln() / Decimal(2).ln()
    return Decimal((w // 2) * 256) - Decimal(n // 4) * log2_r


def main() -> None:
    getcontext().prec = 80
    assert margin(170_752_922_587) <= 0
    assert margin(170_752_922_588) > 0

    for v in range(2, 12):
        w = 2**v
        for a in range(v):
            exact = ((w - 1) // 2**a + 1) // 2
            assert 2**a * exact == w // 2
    assert 2 * (((6 - 1) // 2 + 1) // 2) < 6 // 2

    failed = json.loads((PILOT / "cs_independent_audit_result.json").read_text())
    passed = json.loads(
        (PILOT / "cs_independent_audit_rerun_result.json").read_text()
    )
    assert failed["status"] == "FAIL"
    assert passed["status"] == "PASS"
    assert passed["audit"]["finite_fields"]["exact_exponent_witnesses"] > 0

    contract = (NODE_DIR / "claim_contract.md").read_text()
    proof = (NODE_DIR / "proof.md").read_text()
    assert "no uniform percentage" in contract
    assert "no adjacent list crossing" in contract
    assert "arbitrary `w` uses each exact" in (
        NODE_DIR / "audit.md"
    ).read_text()
    assert "p^|Z_w^odd(p)| divides" in proof
    print(
        "AUDIT_RATE_HALF_CROSSING_IDEAL_GALOIS_MULTIPLICITY_EXCLUSION_PASS "
        "boundary=2/2 tower=65/65 failed_run_preserved=1 tamper=1"
    )


if __name__ == "__main__":
    main()
