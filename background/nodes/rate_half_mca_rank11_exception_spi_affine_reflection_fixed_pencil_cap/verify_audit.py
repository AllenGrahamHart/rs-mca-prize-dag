#!/usr/bin/env python3
"""Independent audit of the exact fixed affine-reflection pencil cap."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "ad63a47a7e9a528e1379d3c42cad6781a3be64dafbeaa4c643b180c6c21096eb"
RESULT = ROOT / "experiments/prize_resolution/rate_half_mca_rank11_affine_reflection_cyclotomic_census_result.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    assert digest(CONTRACT) == CONTRACT_SHA256
    contract = json.loads(CONTRACT.read_text())
    assert digest(RESULT) == contract["result_sha256"]
    result = json.loads(RESULT.read_text())
    p, n, q, g = result["p"], result["domain_order"], result["index"], result["primitive_generator"]
    assert (p, n, q, g) == (2130706433, 2**21, 1016, 3)
    assert p - 1 == q * n
    rows = result["rows"]
    assert len(rows) == q

    # Reconstruct representatives in reverse order, independently of the
    # primary verifier's forward recurrence.
    inverse_g = pow(g, p - 2, p)
    expected = pow(g, q - 1, p)
    inverse_two = pow(2, p - 2, p)
    summary = []
    for index in range(q - 1, -1, -1):
        row_index, c, left, right = rows[index]
        assert (row_index, c) == (index, expected)
        assert left == right
        fixed = int(pow(c * inverse_two % p, n, p) == 1)
        assert left % 2 == fixed
        summary.append((index, left, (left - fixed) // 2, fixed))
        expected = expected * inverse_g % p
    assert expected == pow(g, p - 2, p)

    assert sum(row[1] for row in summary) == n - 1
    assert sum(row[2] for row in summary) == n // 2 - 1
    assert sum(row[3] for row in summary) == 1
    maximum = max(row[1] for row in summary)
    maximizers = [row[0] for row in summary if row[1] == maximum]
    assert maximum == 2308 and maximizers == [74]
    assert rows[74] == [74, 1177199610, 2308, 2308]
    assert max(row[2] for row in summary) == 1154

    proof = (HERE / "proof.md").read_text().lower()
    frontier = (HERE / "frontier.md").read_text().lower()
    assert "r_(hc)=r_c" in proof
    assert "not merely a reported summary" in proof
    assert "different packets from the same heavy pair type" in frontier
    assert "yet proved to return the same `c`" in frontier
    assert "not an aggregate" in contract["nonclaim"].lower()
    print(
        "RANK11_AFFINE_FIXED_PENCIL_CAP_AUDIT_PASS "
        f"maximum={maximum} fibers=1154 cosets={len(rows)}"
    )


if __name__ == "__main__":
    main()
