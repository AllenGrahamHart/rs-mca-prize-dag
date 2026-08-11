#!/usr/bin/env python3
"""Independent symbolic audit of both connectivity margins."""


def main() -> None:
    checks = 0
    for e in range(7, 500, 2):
        p = (3 * e - 1) // 2
        for d_a in (0, 1):
            r = 3 * p - 3 + d_a
            n = p - 3
            m = e - 2
            c = 2 * e
            assert r - 2 * n == p + 3 + d_a > 0
            assert c - m == e + 2 > 0
            checks += 2
        for r_a in range(4):
            r = 2 * p + r_a
            n = p - 2
            m = e - 1
            c = p + 2
            assert r - 2 * n == 4 + r_a > 0
            assert c - m == (e + 5) // 2 > 0
            checks += 2

    print(f"PASS connected scalar-weld margin audit checks={checks}")


if __name__ == "__main__":
    main()
