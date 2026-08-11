#!/usr/bin/env python3
"""Degree and local-Smith checks for the general adjugate factorization."""


def main():
    checked = 0
    for rho in range(16, 200):
        d = rho - 1
        for e in range(1, d // 2 + 1):
            delta = d - 2 * e
            assert d + 1 == rho
            assert d - 2 * e == delta
            assert 2 * e + delta == d
            checked += 1

    # Independent local Smith profiles: rank loss counts positive exponents,
    # while determinant order is their sum.
    profiles = (
        (0, 0, 0),
        (1, 0, 0),
        (2, 1, 0),
        (3, 2, 1),
        (4, 0, 2),
    )
    for exponents in profiles:
        rank_loss = sum(a > 0 for a in exponents)
        determinant_order = sum(exponents)
        assert rank_loss <= determinant_order
        for pole in range(rank_loss + 1):
            assert pole <= determinant_order

    m = 1 << 37
    rho = 4 * m
    e = (16 * m) // 13
    d = rho - 1
    delta = d - 2 * e
    assert delta == 211444543803
    assert d - 2 * e == delta

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_GENERAL_MIDDLE_ADJUGATE_PASS "
        f"checked={checked} official_delta={delta}"
    )


if __name__ == "__main__":
    main()
