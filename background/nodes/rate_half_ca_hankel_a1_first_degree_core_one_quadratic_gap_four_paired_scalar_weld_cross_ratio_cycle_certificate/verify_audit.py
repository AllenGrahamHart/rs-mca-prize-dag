#!/usr/bin/env python3
"""Independent audit of the profile overlap margins."""


def main():
    checks = 0
    for e in range(7, 500, 2):
        p = (3 * e - 1) // 2
        for d_a in (0, 1):
            rows = 3 * p - 3 + d_a
            fiber_degree = p - 3
            assert rows - 3 * fiber_degree == 6 + d_a > 0
            checks += 1
        for r_a in range(5):
            rows = 2 * p + r_a
            fiber_degree = p - 2
            assert rows - 2 * fiber_degree == 4 + r_a > 0
            checks += 1
    print(f"PASS scalar-weld cross-ratio margin audit checks={checks}")


if __name__ == "__main__":
    main()
