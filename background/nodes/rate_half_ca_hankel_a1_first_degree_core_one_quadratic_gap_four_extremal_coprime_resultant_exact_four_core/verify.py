#!/usr/bin/env python3
"""Check the exact four-core subtraction."""


def main():
    checks = 0
    for e in range(7, 5000, 2):
        for d_a in (0, 1):
            cap = 2 * e - 5 if d_a == 0 else e - 3
            exceptional = e - 3 if d_a == 0 else 0
            total_padding = e - 6 - d_a
            assert cap - exceptional - total_padding == 4
            checks += 1

        n = (3 * e - 7) // 2
        intersection = (3 * e - 2) * (e - 2) + e * n
        mandatory = 3 * e * n - e
        assert intersection - mandatory == 4
        checks += 1

    e = 183251937963
    assert (2 * e - 5) - (e - 3) - (e - 6) == 4
    assert (e - 3) - (e - 7) == 4
    checks += 2
    print(f"PASS extremal coprime-resultant exact four-core checks={checks}")


if __name__ == "__main__":
    main()
