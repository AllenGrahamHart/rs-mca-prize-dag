#!/usr/bin/env python3
"""Independent off-by-one audit for the two-fibre route."""

from __future__ import annotations


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    cases = 0
    for u in range(1, 4097):
        m = 4 * u
        rho = 4 * m - 1
        a = 7 * m - 1
        capacity = (16 * m - a) * m

        nsum_floor = 2 * (a - rho)
        p_floor = nsum_floor - rho
        require(p_floor == 2 * m + 1, "baseline spend")
        require(capacity // p_floor == 9 * m // 2 - 2, "division identity")

        p_close = 9 * m // 4 + 1
        nsum_close = rho + p_close
        require(nsum_close == 25 * m // 4, "concentration threshold")
        require(capacity // p_close <= 4 * m - 2, "closing spend")
        require(capacity // (p_close - 1) >= 4 * m - 1, "one-less spend")

        require(nsum_close - nsum_floor == m // 4, "missing fibre mass")
        require((nsum_close - 1) - rho == p_close - 1, "hostile fibre mutation")
        require(
            capacity // ((nsum_close - 1) - rho) >= 4 * m - 1,
            "one-less fibre sum unexpectedly closes",
        )
        cases += 1

    m = 2**37
    total = 2 + ((9 * m + 1) * m) // (2 * m + 1)
    require(total * 8 == 9 * (4 * m), "exact 9/8 cap")
    require(total - 4 * m == m // 2, "exact residual")

    print(
        "RH_TYPE2_FR_TWO_TYPE1_FIBRE_SPEND_AUDIT_PASS "
        f"cases={cases} official_total={total} residual={m//2}"
    )


if __name__ == "__main__":
    main()
