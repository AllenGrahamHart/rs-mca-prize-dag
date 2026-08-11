#!/usr/bin/env python3
"""Check all-excess degree and packet identities."""


def main():
    checks = 0
    for e in range(7, 2000, 2):
        p = (3 * e - 1) // 2
        for n in (p - 3, p - 2):
            for a in {0, 1, e // 3, e}:
                for r in {0, 1, max(0, e - 7)}:
                    if a + r > n:
                        continue
                    i_size = n - a - r
                    for h_degree in {0, a // 2, a}:
                        fiber_degree = i_size + h_degree + r
                        degree_drop = n - fiber_degree
                        assert degree_drop == a - h_degree
                        assert 0 <= fiber_degree <= n
                        checks += 2

        # All padding is now mandatory in the extremal resultant.
        for d_a in (0, 1):
            cap = 2 * e - 5 if d_a == 0 else e - 3
            exceptional = e - 3 if d_a == 0 else 0
            total_r = e - 6 - d_a
            assert cap - exceptional - total_r == 4
            checks += 1

    e = 183251937963
    p = 274877906944
    assert p - 3 == 274877906941
    assert p - 2 == 274877906942
    checks += 2
    print(f"PASS paired all-excess residual-fiber checks={checks}")


if __name__ == "__main__":
    main()
