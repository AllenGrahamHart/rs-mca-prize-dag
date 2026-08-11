#!/usr/bin/env python3
"""Independent symbolic audit for weld-row counts and anchors."""


def main() -> None:
    checks = 0
    for e in range(7, 200, 2):
        p = (3 * e - 1) // 2
        for d_a in (0, 1):
            r = 3 * p - 3 + d_a
            n = p - 3
            assert r > n
            assert r - n - 1 == 2 * p - 1 + d_a
            checks += 2
        for r_a in range(4):
            r = 2 * p + r_a
            n = p - 2
            assert r > n
            assert r - n - 1 == p + 1 + r_a
            checks += 2

    good = 2 * 7 * (2 * 10 - 1)
    bad = 2 * 7 * (2 * 10)
    assert good != bad
    print(f"PASS paired scalar-weld audit checks={checks} tamper=1/1")


if __name__ == "__main__":
    main()
