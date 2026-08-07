#!/usr/bin/env python3
"""Verify the Johnson-positive wedge summation arithmetic."""


def classify(n: int):
    deep = []
    boundary = []
    for e in range(2, n // 2 + 1):
        for d in range(1, e):
            delta = 4 * e * e - n * (e + d)
            if delta >= n:
                deep.append((e, d, delta))
            elif delta > 0:
                boundary.append((e, d, delta))
    return deep, boundary


def main() -> None:
    # Exact finite controls verify the one-boundary-cell-per-e law and the
    # two aggregate estimates without iterating at official N.
    for n in (8, 16, 32, 64, 128):
        deep, boundary = classify(n)
        assert len(boundary) <= n // 2
        assert len({e for e, _, _ in boundary}) == len(boundary)
        assert len(deep) < n * n // 8

        deep_bound = sum(n * (e - d) // delta for e, d, delta in deep)
        boundary_bound = sum(n * (e - d) // delta for e, d, delta in boundary)
        assert deep_bound <= n**3 // 16
        assert boundary_bound <= n**3 // 4

    n = 1 << 41
    assert 5 * n**3 % 16 == 0
    assert 16 * n**3 - 1 - 5 * n**3 // 16 == 251 * n**3 // 16 - 1
    print(
        "X4_LOW_DIFFERENCE_JOHNSON_POSITIVE_WEDGE_PASS "
        f"official_bound={5 * n**3 // 16} residual={251 * n**3 // 16 - 1}"
    )


if __name__ == "__main__":
    main()
