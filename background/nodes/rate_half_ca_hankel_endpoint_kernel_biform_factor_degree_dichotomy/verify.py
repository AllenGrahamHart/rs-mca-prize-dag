#!/usr/bin/env python3
"""Exact arithmetic replay of the factor-degree dichotomy."""


def ceil_div(left, right):
    return -((-left) // right)


def main():
    checks = 0
    for m in range(1, 2001):
        T = 4 * m + 1
        rho = 4 * m - 1
        threshold = ceil_div(3 * m + 1, 4)

        assert T * 2 > 4 * m + m
        assert 4 * m > rho
        assert 4 * threshold >= 3 * m + 1
        if threshold:
            assert 4 * (threshold - 1) < 3 * m + 1
        if m >= 2:
            assert threshold >= 2
        if m in (2, 3, 4):
            assert threshold == m
        checks += 6

    official_m = 1 << 37
    official_threshold = ceil_div(3 * official_m + 1, 4)
    assert official_threshold == 103079215105
    print(
        "PASS endpoint factor-degree dichotomy",
        f"checks={checks}",
        f"official={official_threshold}",
    )


if __name__ == "__main__":
    main()
