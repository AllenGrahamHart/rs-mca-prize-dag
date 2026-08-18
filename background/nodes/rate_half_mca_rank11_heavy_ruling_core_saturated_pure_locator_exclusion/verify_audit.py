#!/usr/bin/env python3
"""Independent audit of the core-saturated pure-locator exclusion."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "1fd80f10d27b398d80c5636f4869ba58b71c18a46b935391af678d891ab2f1ca"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256
    data = json.loads(CONTRACT.read_text())
    row = data["official"]
    dimension, agreement = row["K"], row["m"]
    excess, margin = agreement - dimension, row["pair_core_margin"]
    surplus = excess - 2 * margin + 1
    assert (excess, margin, surplus) == (67472, 11, 67451)
    for c in (0, 1, 4130, 1045975, dimension - 3):
        kp, mp = dimension - c, agreement - c
        union_floor = 2 * (mp - margin) - (kp - 1)
        assert kp >= 3
        assert union_floor == mp + surplus > mp

    toy = data["toy"]
    p = toy["field"]
    union = sorted(set(toy["core_0"]) | set(toy["core_1"]))
    first_eight = union[: toy["locator_degree_maximum"] + 1]
    determinant = 1
    for j, right in enumerate(first_eight):
        for left in first_eight[:j]:
            determinant = determinant * (right - left) % p
    assert determinant != 0
    assert len(union) == 9 > toy["locator_degree_maximum"]
    proof = Path(__file__).with_name("proof.md").read_text().lower()
    assert "support-wise pair noncontainment" in proof
    assert "after pair ownership is fixed" in proof
    assert "nontrivial rational-profile or official" in proof
    print(
        "RANK11_CORE_SATURATED_PURE_LOCATOR_AUDIT_PASS "
        f"surplus={surplus} vandermonde_det={determinant} endpoint={dimension - 3}"
    )


if __name__ == "__main__":
    main()
