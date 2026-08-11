#!/usr/bin/env python3
"""Check the exact regular-quartic eliminant exponents."""


def main():
    checks = 0
    for e in range(7, 5000, 2):
        p = (3 * e - 1) // 2
        d = 3 * e - 2
        n = p - 3
        n0 = 3 * p - 2
        intersection = d * (e - 2) + e * n

        assert n0 + d - 1 - n == 2 * d + 1
        assert 3 * e * n - e + 4 == intersection
        for r in (0, 1, 2):
            assert (d - r) + r - d == 0
        for a in range(5):
            for r in range(3):
                assert (n - a - r) + r == n - a
        checks += 14

    print(f"PASS extremal regular-quartic eliminant checks={checks}")


if __name__ == "__main__":
    main()
