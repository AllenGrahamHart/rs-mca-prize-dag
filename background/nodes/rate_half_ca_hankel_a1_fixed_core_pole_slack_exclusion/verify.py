#!/usr/bin/env python3
"""Exact official fixed-core survivor classification."""


def data(rho, s, e):
    d = rho - s
    delta = d - (s + 1) * e
    if s == 2 and delta == 0:
        beta = 2
    else:
        beta = 1
    tmax = 4 * e + beta
    slack_max = tmax - rho - 2
    return d, delta, beta, slack_max


def excluded(e, slack, pole, beta):
    return pole // 3 + slack + 3 - beta < e


def main():
    profiles = s2_profiles = 0
    for m in range(8, 180):
        rho = 4 * m
        for s in (1, 2):
            d = rho - s
            for e in range(m + 1, d // (s + 1) + 1):
                _, delta, beta, slack_max = data(rho, s, e)
                if slack_max < 0:
                    continue
                for slack in range(slack_max + 1):
                    assert excluded(e, slack, delta, beta) or s == 1
                    if s == 2:
                        assert excluded(e, slack, delta, beta)
                        s2_profiles += 1
                    profiles += 1

    m = 1 << 37
    rho = 4 * m
    e = m + 1
    _, delta, beta, slack_max = data(rho, 1, e)
    assert (delta, beta, slack_max) == (2 * m - 3, 1, 3)
    for slack in range(slack_max + 1):
        assert excluded(e, slack, delta, beta)

    e2 = (rho - 2) // 3
    _, delta2, beta2, slack2 = data(rho, 2, e2)
    assert (delta2, beta2, slack2) == (0, 2, e2 - 2)
    assert excluded(e2, slack2, 0, beta2)

    print(
        "RATE_HALF_CA_HANKEL_A1_FIXED_CORE_POLE_SLACK_EXCLUSION_PASS "
        f"profiles={profiles} s2_profiles={s2_profiles} official_m={m} "
        "s2_survivors=0"
    )


if __name__ == "__main__":
    main()
