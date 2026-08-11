#!/usr/bin/env python3
"""Exact constant-profile heavy-incidence arithmetic."""


def main():
    m = 1 << 37
    rho = 4 * m
    e = (rho + 1) // 3
    t = rho + 4

    expected = {0: tuple(range(2, 6)), 1: (1, 2)}
    for s in (0, 1):
        d = rho - s
        delta = d - (s + 1) * e
        allowed = []
        for a in range((5, 2)[s] + 1):
            light = (3 * rho + 3 + a) * e
            total_gap = t * d - light
            if total_gap <= 2 * delta:
                allowed.append(a)
        assert tuple(allowed) == expected[s]

    delta0 = 2 * e - 1
    gap0 = (6 - 2) * e - 3
    assert 2 * delta0 - gap0 == 1

    delta1 = e - 2
    gap1 = (3 - 1) * e - 6
    assert 2 * delta1 - gap1 == 2

    print(
        "RATE_HALF_CA_HANKEL_A1_FIRST_DEGREE_CONSTANT_HEAVY_PIN_PASS "
        f"e={e} allowed={expected}"
    )


if __name__ == "__main__":
    main()
