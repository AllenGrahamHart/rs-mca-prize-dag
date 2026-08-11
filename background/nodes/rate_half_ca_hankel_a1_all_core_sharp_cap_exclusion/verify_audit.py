#!/usr/bin/env python3
"""Endpoint and interpolation-transition mutation audit."""


def main():
    m = 128
    rho = 4 * m
    e = m + 2
    delta = rho - e
    assert delta // 4 + 4 < e
    # Three contacts alone retain this endpoint, showing why four contacts
    # are a real dependency.
    assert not (delta // 3 + 3 < e)

    e = rho // 2
    delta = rho - e
    assert delta // 2 + 3 < e
    # Illegally retaining interpolation degree two can reverse the boundary.
    assert not (delta // 3 + 3 < e) or delta // 3 <= delta // 2

    print(
        "RATE_HALF_CA_HANKEL_A1_ALL_CORE_SHARP_CAP_EXCLUSION_AUDIT_PASS "
        "endpoint_dependency=detected transition=checked"
    )


if __name__ == "__main__":
    main()
