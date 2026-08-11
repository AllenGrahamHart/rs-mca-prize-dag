#!/usr/bin/env python3
"""Replay the exact off-line norm degree ledgers."""


def main():
    checks = 0
    for e in range(7, 1000, 2):
        p = (3 * e - 1) // 2
        assert 2 * p == 3 * e - 1

        for d_a in (0, 1):
            raw = 3 * e * (p - 3) - (3 * p - 3 + d_a) * (e - 2)
            closed = (3 - d_a) * e - 9 + 2 * d_a
            assert raw == closed >= 0
            excess_sum = e
            off_line_padding = e - 6 - d_a
            exceptional_incidences = e - 3 if d_a == 0 else 0
            assert (
                excess_sum + off_line_padding + exceptional_incidences
                == closed
            )
            checks += 1

        for r_a in range(e - 5):
            numerator = 3 * e * e - 4 * e - 7 - 2 * r_a * (e - 1)
            assert numerator % 2 == 0
            raw = (3 * e + 1) * (p - 2) - (2 * p + r_a) * (e - 1)
            assert raw == numerator // 2 >= 0
            checks += 1

    official_e = 183251937963
    assert 3 * official_e - 9 == 549755813880
    assert 2 * official_e - 7 == 366503875919
    print(f"PASS paired split-biform off-line norm arithmetic checks={checks}")


if __name__ == "__main__":
    main()
