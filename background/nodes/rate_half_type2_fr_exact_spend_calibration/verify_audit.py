#!/usr/bin/env python3
"""Independent floor-transition audit for the FR spend correction."""

from __future__ import annotations


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    cases = 0
    for exponent in range(2, 38):
        m = 2**exponent
        capacity = (9 * m + 1) * m
        threshold = 9 * m // 4 + 1
        target_type2 = 4 * m - 2

        require(capacity < threshold * (target_type2 + 1), "strict floor gate")
        require(capacity >= (threshold - 1) * (target_type2 + 1), "minimality gate")
        require(capacity // threshold <= target_type2, "threshold cap")
        require(capacity // (threshold - 1) > target_type2, "hostile off-by-one")

        old = 2 * m + 2
        if m >= 8:
            require(capacity // old > target_type2, "old proposal unexpectedly closes")
        cases += 1

    m = 2**37
    numerator = (9 * m + 1) * m
    old_total = 2 + numerator // (2 * m + 2)
    require(9 * (4 * m) - old_total * 8 == 16, "9/8 residual calibration")
    require(old_total > 4 * m, "official residual vanished")

    print(
        "RH_TYPE2_FR_EXACT_SPEND_CALIBRATION_AUDIT_PASS "
        f"power_two_cases={cases} p_req={9*m//4+1} old_residual={old_total-4*m}"
    )


if __name__ == "__main__":
    main()
