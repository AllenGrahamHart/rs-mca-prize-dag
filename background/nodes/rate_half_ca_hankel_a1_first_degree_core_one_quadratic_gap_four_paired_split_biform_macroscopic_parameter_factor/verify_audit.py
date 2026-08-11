#!/usr/bin/env python3
"""Exhaust small factor-degree partitions against the proved inequality."""


def partitions(total: int, ceiling: int | None = None):
    if total == 0:
        yield ()
        return
    if ceiling is None or ceiling > total:
        ceiling = total
    for first in range(ceiling, 0, -1):
        for tail in partitions(total - first, first):
            yield (first, *tail)


def ceil_div(left: int, right: int) -> int:
    return (left + right - 1) // right


def main() -> None:
    checks = 0
    feasible = 0
    for e in range(7, 32, 2):
        p = (3 * e - 1) // 2
        m = e - 2
        n = p - 3
        for d_a in (0, 1):
            r = 3 * p - 3 + d_a
            t = 3 * e
            threshold = ceil_div(3 * e, 9 - 2 * d_a)
            for profile in partitions(m):
                needed = sum(ceil_div(r * degree, t) for degree in profile)
                if needed <= n:
                    feasible += 1
                    assert max(profile) >= threshold
                checks += 1

    assert checks > 10000
    assert feasible > 0
    print(
        "RATE_HALF_PAIRED_BIFORM_MACRO_FACTOR_AUDIT_PASS "
        f"partitions={checks} feasible={feasible}"
    )


if __name__ == "__main__":
    main()
