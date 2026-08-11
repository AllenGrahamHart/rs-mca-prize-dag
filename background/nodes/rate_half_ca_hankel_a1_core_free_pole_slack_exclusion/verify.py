#!/usr/bin/env python3
"""Exact profile checks for the A=1 core-free pole-slack exclusion."""


def alpha_for(rho, e):
    if e <= rho // 2 - 1:
        return 2
    if e <= rho - 1:
        return 1
    return 0


def excluded(rho, e, slack, pole):
    alpha = alpha_for(rho, e)
    b = pole // (alpha + 1)
    return b + slack + 3 < e


def main():
    profiles = excluded_profiles = 0
    for m in range(4, 36):
        rho = 4 * m
        for e in range(m + 1, rho + 1):
            delta = rho - e
            alpha = alpha_for(rho, e)
            if alpha == 2:
                assert 2 * (e + 1) < rho + 1
            elif alpha == 1:
                assert e < rho
            else:
                assert e == rho
            max_slack = 4 * e - rho - 2
            for slack in range(max_slack + 1):
                for pole in range(delta + 1):
                    b = pole // (alpha + 1)
                    assert (alpha + 1) * (b + 1) > pole
                    if excluded(rho, e, slack, pole):
                        target = (rho + alpha - 3, b - e + slack + 3)
                        left = (alpha - 3, b - 2 * e + slack + 3)
                        assert target[1] < 0
                        assert left[0] < 0 and left[1] < 0
                        excluded_profiles += 1
                    profiles += 1

    m = 1 << 37
    rho = 4 * m
    e = m + 1
    delta = 3 * m - 1
    for slack in range(3):
        pole_min = 3 * (m - slack - 2)
        assert excluded(rho, e, slack, pole_min - 1)
        assert not excluded(rho, e, slack, pole_min)
        assert delta - pole_min == 3 * slack + 5

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_FREE_POLE_SLACK_EXCLUSION_PASS "
        f"profiles={profiles} excluded={excluded_profiles} official_m={m} "
        "first_degree_chambers=3"
    )


if __name__ == "__main__":
    main()
