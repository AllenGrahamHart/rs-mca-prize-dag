#!/usr/bin/env python3
"""Replay the two E32 profile-(3,5,1) quotient obstruction witnesses."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BASE_CHECKER = (
    ROOT
    / "background/nodes/e1_n256_s16_e33_profile_451_quotient_exclusion/verify.py"
)
RESULT = HERE / "e32_profile351_quotient_probe_result.json"
CAPACITIES = {
    128: (3, 8, 8, 8, 8, 8, 8, 8, 4),
    64: (1, 4, 4, 4, 4, 4, 4, 4, 2),
}


def main() -> None:
    spec = importlib.util.spec_from_file_location("profile451_checker", BASE_CHECKER)
    assert spec is not None and spec.loader is not None
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    checker.PROFILE_COUNTS = (3, 5, 1)

    result = json.loads(RESULT.read_text())
    assert result["schema"] == "e32-profile351-quotient-probe-v1"
    assert result["threshold"] == 1517
    assert result["profile"] == [3, 5, 1]
    expected = {128: (1_828_183, 1610), 64: (1_165_828, 1594)}
    for order, (tested, maximum) in expected.items():
        row = result["orders"][str(order)]
        exact = tuple(tuple(values) for values in row["witness_exact"])
        assert tuple(sum(values) for values in exact) == (3, 5, 1)
        outer = tuple(sum(exact[level][category] for level in range(3)) for category in range(9))
        assert all(value <= cap for value, cap in zip(outer, CAPACITIES[order]))
        assert any(outer[index] for index in (1, 3, 5, 7))
        assert checker.objective(exact) == maximum > result["threshold"]
        assert checker.allocation_count(CAPACITIES[order]) == tested == row["tested"]

    print(
        "E32_PROFILE351_QUOTIENT_PROBE_CHECK_PASS "
        "order128=1828183/1610 order64=1165828/1594 threshold=1517"
    )


if __name__ == "__main__":
    main()
