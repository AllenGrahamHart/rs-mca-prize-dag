#!/usr/bin/env python3
"""Independent arithmetic audit of the near-saturation cap."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    k22 = data["parameters"]["K22"]
    q = k22["q"]
    m = k22["m"]
    weighted = 0
    checks = 0
    for support in (2, 3, 4):
        assert q + 3 * support - 2 <= q + 10
        carrier = comb(q + 2 * support - 2, support) * comb(
            m - support, 11 - support
        )
        values = [
            completions * comb(m - support + 1 - completions, 11 - support)
            for completions in range(q - 1)
        ]
        assert values.index(max(values)) == q - 2
        fallback_numerator = comb(m, support - 1) * max(values)
        fallback = fallback_numerator // support
        old = (
            comb(m, support - 1)
            * (q - 1)
            * comb(m - support + 2 - q, 11 - support)
            // support
        )
        active = max(carrier, fallback)
        assert active == k22["active_caps"][str(support)]
        weighted += k22["premium_weights"][str(support)] * (old - active)
        checks += 4
    assert q + 3 * 5 - 2 > q + 10
    assert weighted == k22["weighted_premium_saving"]
    print(
        "RATE_HALF_MCA_SPARSE_CIRCUIT_NEAR_SATURATION_CARRIER_AUDIT_PASS "
        f"checks={checks + 2} saving={weighted}"
    )


if __name__ == "__main__":
    main()
