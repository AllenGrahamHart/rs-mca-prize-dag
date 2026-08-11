#!/usr/bin/env python3
"""Exact official prefix verification for four-contact exclusion."""


def profile(rho, s, e):
    d = rho - s
    delta = d - (s + 1) * e
    beta = 2 if s == 2 and delta == 0 else (0 if s == 0 else 1)
    slack_max = 4 * e + beta - rho - 2
    return delta, beta, slack_max


def automatic(rho, s, e):
    delta, beta, slack = profile(rho, s, e)
    return delta // 4 + slack + 4 - beta < e


def main():
    profiles = 0
    for m in range(8, 1000):
        rho = 4 * m
        first0 = (12 * m) // 11
        first1 = (6 * m) // 5
        for s, first in ((0, first0), (1, first1)):
            assert automatic(rho, s, first - 1)
            assert 3 * (first + 1) < rho + 1
            for e in range(m + 1, first):
                assert automatic(rho, s, e)
                profiles += 1

    m = 1 << 37
    rho = 4 * m
    first0 = (12 * m) // 11
    first1 = (6 * m) // 5
    assert first0 == 149933403787
    assert first1 == 164926744166
    assert automatic(rho, 0, first0 - 1)
    assert not automatic(rho, 0, first0)
    assert automatic(rho, 1, first1 - 1)
    assert not automatic(rho, 1, first1)

    # All first core-free slack chambers are excluded even at maximal pole
    # length.
    e = m + 1
    delta, beta, slack_max = profile(rho, 0, e)
    assert slack_max == 2
    for slack in range(3):
        assert delta // 4 + slack + 4 - beta < e

    print(
        "RATE_HALF_CA_HANKEL_A1_FOUR_CONTACT_LOW_DEGREE_EXCLUSION_PASS "
        f"profiles={profiles} official_s0_first={first0} "
        f"official_s1_first={first1}"
    )


if __name__ == "__main__":
    main()
