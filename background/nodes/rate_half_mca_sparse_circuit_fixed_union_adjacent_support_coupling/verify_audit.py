#!/usr/bin/env python3
"""Independent arithmetic audit of adjacent-support specializations."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
DEFICITS = {2: 36, 3: 28, 4: 21, 5: 15, 6: 10, 7: 6, 8: 3, 9: 1}


def vertex_cap(k: int, m: int, u: int, g: int, d: int) -> int:
    r, n = k - u - g, m - u
    wd = DEFICITS[d] * comb(m - d, 11 - d)
    wn = DEFICITS[d + 1] * comb(m - d - 1, 10 - d)
    answer = 0
    for i in range(d - 1):
        a = d + 1 - i
        b = n - r - d + 1 + i
        rhs = comb(u, i) * r * comb(n, d - i)
        xmax = comb(u, i) * r * comb(n, d - 1 - i) // (d - i)
        values = [Fraction(wn * rhs, a)]
        values.append(Fraction(wd * xmax, 1) + Fraction(wn * (rhs - b * xmax), a))
        answer += max(values).__floor__()
    answer += wd * (comb(u, d - 1) * r + comb(u, d))
    answer += wn * (
        comb(u, d - 1) * r * n // 2
        + comb(u, d) * r
        + comb(u, d + 1)
    )
    return answer


def main() -> None:
    rows = json.loads((HERE / "source_contract.json").read_text())["k83_specializations"]
    checked = []
    for row in rows:
        key = (row["union"], row["dimension"], row["support_pair"][0])
        value = vertex_cap(83, 67555, *key)
        assert value == row["weighted_cap"]
        checked.append([*key, value])
    proof = (HERE / "proof.md").read_text()
    for marker in ("N>=R+d-1", "lambda_i", "division by two", "disjoint"):
        assert marker in proof
    print(json.dumps({"status": "AUDIT_PASS", "checked": checked}, sort_keys=True))


if __name__ == "__main__":
    main()
