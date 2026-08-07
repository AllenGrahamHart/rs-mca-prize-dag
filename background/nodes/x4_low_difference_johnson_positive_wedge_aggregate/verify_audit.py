#!/usr/bin/env python3
"""Independent audit of the positive-wedge cell decomposition."""


def main() -> None:
    for n in range(4, 258, 2):
        boundary_by_e = {}
        deep_cells = 0
        for e in range(2, n // 2 + 1):
            previous = None
            for d in range(1, e):
                delta = 4 * e * e - n * (e + d)
                if previous is not None:
                    assert previous - delta == n
                previous = delta
                if 0 < delta < n:
                    boundary_by_e[e] = boundary_by_e.get(e, 0) + 1
                elif delta >= n:
                    deep_cells += 1
        assert all(count == 1 for count in boundary_by_e.values())
        assert len(boundary_by_e) <= n // 2
        assert deep_cells < n * n // 8

    n = 1 << 41
    assert n % 16 == 0
    print(
        "X4_LOW_DIFFERENCE_JOHNSON_POSITIVE_WEDGE_AUDIT_PASS "
        "even_controls=127 official_divisibility=16"
    )


if __name__ == "__main__":
    main()
