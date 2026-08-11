#!/usr/bin/env python3
"""Exact official all-core sharp-cap exclusion replay."""


def alpha_for(rho, e):
    if e <= rho // 2 - 1:
        return 2
    if e <= rho - 1:
        return 1
    return 0


def main():
    checks = 0

    # Bounded exhaustive replay of every degree and interpolation transition.
    for m in range(32, 160):
        rho = 4 * m
        for e in range(m + 1, rho + 1):
            delta = rho - e
            if e <= m + 2:
                assert 3 * (e + 1) < rho + 1
                assert delta // 4 + 4 < e
            else:
                alpha = alpha_for(rho, e)
                assert delta // (alpha + 1) + 3 < e
            checks += 1
        for e in range(m + 1, (rho - 1) // 2 + 1):
            delta = rho - 1 - 2 * e
            assert delta // 3 + 2 < e
            assert e - 2 - delta // 3 >= 1
            checks += 1

    # Official proof is by monotonic endpoints, not iteration over O(m)
    # degrees.
    m = 1 << 37
    rho = 4 * m
    for e in (m + 1, m + 2):
        delta = rho - e
        assert delta // 4 + 4 < e
    e = m + 3
    assert (rho - e) // 3 + 3 < e
    e = rho // 2
    assert (rho - e) // 2 + 3 < e
    e = rho
    assert 3 < e
    e = m + 1
    delta = rho - 1 - 2 * e
    assert delta // 3 + 2 < e

    print(
        "RATE_HALF_CA_HANKEL_A1_ALL_CORE_SHARP_CAP_EXCLUSION_PASS "
        f"checks={checks} official_m={m} sharp_survivors=0"
    )


if __name__ == "__main__":
    main()
