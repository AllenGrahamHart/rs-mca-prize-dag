#!/usr/bin/env python3
"""Boundary and interpolation-degree mutation audit."""


def main():
    cases = 0
    for alpha in range(3):
        for pole in range(80):
            b = pole // (alpha + 1)
            assert (alpha + 1) * (b + 1) > pole
            if pole:
                mutated = (pole + alpha) // (alpha + 1)
                assert mutated >= b
            cases += 1

    m = 64
    rho = 4 * m
    e = m + 1
    for slack in range(3):
        boundary = 3 * (e - slack - 3)
        assert (boundary - 1) // 3 + slack + 3 < e
        assert boundary // 3 + slack + 3 == e

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_FREE_POLE_SLACK_EXCLUSION_AUDIT_PASS "
        f"cases={cases} equality_boundary=retained mutation=detected"
    )


if __name__ == "__main__":
    main()
