#!/usr/bin/env python3
"""Independent audit of the completion-defect depths and K'=23 caps."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    k23 = p["K23"]
    q = k23["q"]
    m = k23["m"]
    checks = 0
    premium = 0
    for support in (2, 3, 4, 5):
        depth = max(
            [0]
            + [
                defect
                for defect in range(1, 11)
                if (defect + 2) * support - defect - 1 <= 10
            ]
        )
        assert depth == p["depths"][str(support)]
        ceiling = q - depth - 1
        values = [
            b * comb(m - support + 1 - b, 11 - support)
            for b in range(ceiling + 1)
        ]
        maximizing = values.index(max(values))
        deletion = comb(m, support - 1) * max(values) // support
        carriers = [
            comb(q + (defect + 1) * (support - 1), support)
            * comb(m - support, 11 - support)
            for defect in range(1, depth + 1)
        ]
        active = max([deletion] + carriers)
        assert maximizing == k23["completion_maximizers"][str(support)]
        assert active == k23["active_caps"][str(support)]
        premium += k23["premium_weights"][str(support)] * active
        checks += 5
    assert premium == k23["weighted_premium"]
    print(
        "RATE_HALF_MCA_SPARSE_CIRCUIT_COMPLETION_DEFECT_HIERARCHY_AUDIT_PASS "
        f"checks={checks + 1} premium={premium}"
    )


if __name__ == "__main__":
    main()
