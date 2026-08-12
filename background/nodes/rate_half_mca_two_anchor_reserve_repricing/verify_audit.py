#!/usr/bin/env python3
"""Independent endpoint audit of the two-anchor reserve repricing."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "172934ca92647c61e054f30b8ec25be83844f2859f32245a20c5234eda11f56e"


class Reject(ValueError):
    pass


def check(data: object) -> None:
    if not isinstance(data, dict) or data.get("old_exception_cap") != 31:
        raise Reject("header")
    rows = data.get("rows")
    if not isinstance(rows, list) or len(rows) != 2:
        raise Reject("rows")
    expected_rows = (
        ("KoalaBear MCA", 2097152, 1048576, 1116048, 274980728111395087, 57198030366),
        ("Mersenne-31 MCA", 2097152, 1048576, 1116024, 16777215, 1752700),
    )
    for row, fixed in zip(rows, expected_rows):
        name, n, dimension, agreement, budget, average = fixed
        if tuple(row.get(key) for key in ("name", "n", "K", "m", "B_star", "average_ceiling")) != fixed:
            raise Reject("fixed row")
        w = agreement - dimension
        reserve = 2 * w + 31
        g_min = 2 * agreement - dimension + 1
        endpoint = budget - reserve - (n - g_min)
        full = budget - reserve
        quotient, remainder = divmod(full, average)
        expected = row.get("expected")
        if not isinstance(expected, dict):
            raise Reject("expected")
        if (
            expected.get("w") != w
            or expected.get("two_w") != 2 * w
            or expected.get("combined_reserve") != reserve
            or expected.get("g_min") != g_min
            or expected.get("target_g_min") != endpoint
            or expected.get("target_full") != full
            or expected.get("full_average_quotient") != quotient
            or expected.get("full_average_remainder") != remainder
            or 2 * w <= 31
            or reserve + n >= budget
        ):
            raise Reject(f"row arithmetic: {name}")
        # The target is affine in g, so endpoint checks certify the interval.
        for g in (g_min, (g_min + n) // 2, n):
            target = endpoint + (g - g_min)
            if reserve + (n - g) + target != budget:
                raise Reject("affine target identity")


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != SHA256:
        raise Reject("contract hash")
    data = json.loads(CONTRACT.read_text())
    check(data)
    controls = []
    for row_index, field in ((0, "target_g_min"), (0, "target_full"), (1, "full_average_quotient")):
        altered = copy.deepcopy(data)
        altered["rows"][row_index]["expected"][field] += 1
        try:
            check(altered)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("audit controls")
    print(
        "RATE_HALF_MCA_TWO_ANCHOR_RESERVE_REPRICING_AUDIT_PASS "
        f"rows=2 endpoints=6 controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
