#!/usr/bin/env python3
"""Check the Pade exponent and correction-quartic degree ledger."""


def main():
    checks = 0
    for e in range(7, 5000, 2):
        p = (3 * e - 1) // 2
        d = 2 * p - 1
        n0 = 3 * p - 2
        n = p - 3

        assert n0 + d - 1 - n == 2 * d + 1
        assert (e - 6) + 2 * 2 == e - 2
        assert (e - 3) // 2 + (e - 9) // 2 + 1 + 3 == e - 2
        checks += 3

    print(f"PASS quadratic gap-four Pade regular factor checks={checks}")


if __name__ == "__main__":
    main()
