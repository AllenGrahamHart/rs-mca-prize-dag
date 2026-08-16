#!/usr/bin/env python3
"""Verify the fixed-union adjacent-support coupling contract."""

from __future__ import annotations

import hashlib
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "7bd4c049776213cf1aacfe4f2804aa485e19d3aca1102dd696d46d0e89989772"
DEFICITS = {2: 36, 3: 28, 4: 21, 5: 15, 6: 10, 7: 6, 8: 3, 9: 1}


def weighted_cap(k: int, m: int, u: int, g: int, d: int) -> int:
    assert 2 <= d <= g - 1
    residual, outside = k - u - g, m - u
    assert residual >= 0 and outside >= residual + d - 1
    wd = DEFICITS[d] * comb(m - d, 11 - d)
    wn = DEFICITS[d + 1] * comb(m - d - 1, 10 - d)
    total = 0
    for inside in range(d - 1):
        choices = comb(u, inside)
        low = choices * residual * comb(outside, d - 1 - inside) // (d - inside)
        adjacent = choices * residual * comb(outside, d - inside)
        coefficient = outside - residual - d + 1 + inside
        slope = (d + 1 - inside) * wd - coefficient * wn
        total += (wn * adjacent + max(slope, 0) * low) // (d + 1 - inside)
    count_d = comb(u, d - 1) * residual + comb(u, d)
    count_next = (
        comb(u, d - 1) * residual * outside // 2
        + comb(u, d) * residual
        + comb(u, d + 1)
    )
    return total + wd * count_d + wn * count_next


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    assert data["schema"] == "rate-half-mca-fixed-union-adjacent-support-coupling-v1"
    assert data["formula"] == {
        "adjacent_coefficient": "N-R-d+1+i",
        "inside_range": "0<=i<=d-2",
        "dimension_range": "2<=d<=g-1",
    }
    expected = {
        (row["union"], row["dimension"], row["support_pair"][0]): row["weighted_cap"]
        for row in data["k83_specializations"]
    }
    actual = {
        key: weighted_cap(83, 67555, *key)
        for key in expected
    }
    assert actual == expected
    probe = data["probe"]
    assert probe["T23_premium"] < probe["safe_ceiling"]
    assert probe["A23_premium"] < probe["safe_ceiling"]
    statement = (HERE / "statement.md").read_text()
    assert "disjoint adjacent pairs" in statement
    node = json.loads((HERE / "node.json").read_text())
    assert node["node"]["status"] == "PROVED"
    assert {row["from"] for row in node["requires"]} == {
        "rate_half_mca_adjacent_flat_circuit_coupling",
        "rate_half_mca_sparse_circuit_multicarrier_collision_charge",
    }
    print(json.dumps({
        "status": "PASS",
        "specializations": [
            [*key, value] for key, value in sorted(actual.items())
        ],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
