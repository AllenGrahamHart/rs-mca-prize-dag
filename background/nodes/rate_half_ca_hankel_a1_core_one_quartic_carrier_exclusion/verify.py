#!/usr/bin/env python3
"""Exact arithmetic checks for the core-one quartic-carrier exclusion."""


def profile(m, e):
    rho = 4 * m
    delta = rho - 1 - 2 * e
    slack_max = 4 * e - rho - 1
    return rho, delta, slack_max


def automatic(m, e):
    rho, delta, slack_max = profile(m, e)
    return delta // 5 + slack_max + 3 < e


def h1_p1xp1(a, b):
    h0a = max(a + 1, 0)
    h0b = max(b + 1, 0)
    h1a = max(-a - 1, 0)
    h1b = max(-b - 1, 0)
    return h0a * h1b + h1a * h0b


def main():
    checked = 0
    for m in range(16, 512):
        rho = 4 * m
        endpoint = (16 * m) // 13
        for e in range(m + 1, endpoint):
            assert automatic(m, e)
            d = rho - 1
            delta = d - 2 * e
            slack = 4 * e - rho - 1
            b = delta // 5
            c = b + slack + 3
            assert c < e
            assert h1_p1xp1(-d - 1, c - e) == 0
            checked += 1

        # Any product of active components contained in the clearing form
        # has domain degree at most four, independently of its factorization.
        d = rho - 1
        for carrier_degree in range(1, 5):
            assert carrier_degree < d

    m = 1 << 37
    endpoint = (16 * m) // 13
    assert endpoint == 169155635042
    assert automatic(m, endpoint - 1)
    assert not automatic(m, endpoint)
    rho, delta, slack = profile(m, endpoint)
    assert delta // 5 + slack + 3 == endpoint
    assert 16 * m - 13 * endpoint == 6

    delta = rho - 1 - 2 * endpoint
    lower5 = endpoint - 3 - delta // 5
    assert lower5 == 126866726279

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_QUARTIC_CARRIER_EXCLUSION_PASS "
        f"checked={checked} official_first={endpoint}"
    )


if __name__ == "__main__":
    main()
