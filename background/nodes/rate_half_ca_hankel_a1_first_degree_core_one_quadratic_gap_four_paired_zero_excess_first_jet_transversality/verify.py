#!/usr/bin/env python3
"""Check the padding-budget common-factor reductions."""


def main():
    checks = 0
    for e in range(7, 1000, 2):
        p = (3 * e - 1) // 2

        # Extremal: (2e-b)a <= e-6-d_A and b<=e-2.
        for d_a in (0, 1):
            min_full_degree_fibers = 2 * e - (e - 2)
            assert min_full_degree_fibers == e + 2
            assert min_full_degree_fibers > e - 6 - d_a
            checks += 2

        # Strict: (p+2-b)a <= e-6-r_A and b<=e-1.
        min_full_degree_fibers = p + 2 - (e - 1)
        assert min_full_degree_fibers == (e + 5) // 2
        assert 2 * min_full_degree_fibers == e + 5
        checks += 2
        r_a_values = set(range(0, min(e - 6, 32) + 1))
        r_a_values.update({max(0, (e - 17) // 2), max(0, (e - 17) // 2 + 1), e - 6})
        for r_a in sorted(r_a_values):
            assert 2 * min_full_degree_fibers > e - 6 - r_a
            b_floor = p + 2 - (e - 6 - r_a)
            assert b_floor == (e + 15) // 2 + r_a
            assert (b_floor <= e - 1) == (r_a <= (e - 17) // 2)
            r_rows = 2 * p + r_a
            assert b_floor * (r_rows - 1) > 3 * e + 1
            checks += 4

    e = 183251937963
    p = 274877906944
    assert (e + 15) // 2 == 91625968989
    assert p + 2 == 274877906946
    checks += 2
    print(f"PASS paired zero-excess first-jet arithmetic checks={checks}")


if __name__ == "__main__":
    main()
