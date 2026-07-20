#!/usr/bin/env python3
"""Ledger and witness checks for the primary/secondary rigidity sweep."""

from __future__ import annotations

from hashlib import sha256
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RESULT = HERE / "rate_half_list_primary_gap_rigidity_sweep_result.json"


def denominator(roots: list[int], prime: int) -> list[int]:
    out = [1]
    for root in roots:
        updated = [0] * (len(out) + 1)
        for index, value in enumerate(out):
            updated[index] = (updated[index] + value) % prime
            updated[index + 1] = (updated[index + 1] - root * value) % prime
        out = updated
    return out


def coefficients(poly: list[int], maximum: int, prime: int) -> list[int]:
    out = [1]
    for n in range(1, maximum + 1):
        value = sum(
            (4 * n - 3 * j) * poly[j] * out[n - j]
            for j in range(1, min(4, n) + 1)
        )
        out.append(-value * pow(4 * n, -1, prime) % prime)
    return out


def secondary_passes(values: list[int], height: int, prime: int) -> bool:
    leading = values[2 * height]
    square = [0] * height
    for i, left in enumerate(values[:height]):
        for j, right in enumerate(values[2 * height : 3 * height]):
            if i + j >= height:
                break
            square[i + j] = (square[i + j] + left * right) % prime
    inverse = pow(leading, -1, prime)
    square = [value * inverse % prime for value in square]
    root = [1]
    inverse_two = pow(2, -1, prime)
    for n in range(1, height):
        cross = sum(root[index] * root[n - index] for index in range(1, n))
        root.append((square[n] - cross) * inverse_two % prime)
    return root[-2:] == [0, 0]


def main() -> None:
    payload = json.loads(RESULT.read_text())
    script = ROOT / payload["script"]
    assert sha256(script.read_bytes()).hexdigest() == payload["script_sha256"]

    rows = payload["rows"]
    assert len(rows) == 20
    for row in rows:
        assert row["N"] == 8 * row["H"] - 8
        assert (row["p"] - 1) % (2 * row["N"]) == 0
        assert row["sets"] == comb(row["N"] - 1, 3)
        assert 0 <= row["secondary"] <= row["primary_pure"] <= row["primary"]

    for witness in payload["representative_nonpure_primary_witnesses"]:
        height = witness["H"]
        order = witness["N"]
        prime = witness["p"]
        roots = witness["roots"]
        assert len(set(roots)) == 4 and roots[0] == 1
        assert all(pow(root, order, prime) == 1 for root in roots)
        assert all(pow(root, (prime - 1) // 2, prime) == 1 for root in roots)
        values = coefficients(denominator(roots, prime), 3 * height - 1, prime)
        assert values[2 * height - 2] == 0
        assert values[2 * height - 1] == 0
        assert values[2 * height] != 0
        assert not secondary_passes(values, height, prime)

    totals = payload["totals"]
    assert totals["normalized_quartets"] == sum(row["sets"] for row in rows)
    assert totals["primary_survivors"] == sum(row["primary"] for row in rows)
    assert totals["primary_pure"] == sum(row["primary_pure"] for row in rows)
    assert totals["primary_nonpure"] == (
        totals["primary_survivors"] - totals["primary_pure"]
    )
    assert totals["secondary_survivors"] == sum(row["secondary"] for row in rows)
    assert totals["secondary_pure"] == totals["secondary_survivors"]
    assert totals["secondary_nonpure"] == 0

    print(
        "RATE_HALF_LIST_PRIMARY_SECONDARY_RIGIDITY_SWEEP_CHECK_PASS "
        f"rows={len(rows)} quartets={totals['normalized_quartets']} "
        f"primary_nonpure={totals['primary_nonpure']} secondary_nonpure=0"
    )


if __name__ == "__main__":
    main()
