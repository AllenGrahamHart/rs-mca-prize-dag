#!/usr/bin/env python3
"""Check the extremal resultant and four-slack arithmetic."""


def main():
    checks = 0
    for e in range(7, 2000, 2):
        p = (3 * e - 1) // 2
        d = 3 * e - 2
        n = p - 3
        m = e - 2
        intersection = d * m + e * n

        for d_a in (0, 1):
            rows = 3 * p - 3 + d_a
            cap = intersection - rows * m
            expected_cap = 2 * e - 5 if d_a == 0 else e - 3
            assert cap == expected_cap
            total_r = e - 6 - d_a
            for r_bad in {0, total_r // 2, total_r}:
                r_zero = total_r - r_bad
                mandatory = (e - 3 if d_a == 0 else 0) + r_zero
                assert cap - mandatory == 4 + r_bad
                checks += 1
            checks += 1

    e = 183251937963
    p = 274877906944
    d = 549755813887
    n = 274877906941
    m = 183251937961
    intersection = d * m + e * n
    assert intersection == (9 * e * e - 23 * e + 8) // 2
    assert intersection - (3 * p - 3) * m == 2 * e - 5
    assert intersection - (3 * p - 2) * m == e - 3
    checks += 3
    print(f"PASS extremal coprime-resultant four-slack checks={checks}")


if __name__ == "__main__":
    main()
