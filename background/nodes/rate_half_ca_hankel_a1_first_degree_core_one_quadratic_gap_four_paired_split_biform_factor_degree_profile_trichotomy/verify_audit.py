#!/usr/bin/env python3
"""Exhaust small factor partitions against the exact deficit equation."""


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
    profile_counts = {(0, 1, 0): 0, (1, 2, 0): 0, (1, 0, 1): 0}

    for e in range(7, 32, 2):
        p = (3 * e - 1) // 2
        capital_m = e - 2
        capital_n = p - 3
        for d_a in (0, 1):
            q = 9 - 2 * d_a
            r = 3 * p - 3 + d_a
            t = 3 * e
            for factor_degrees in partitions(capital_m):
                checks += 1
                minima = [ceil_div(r * degree, t) for degree in factor_degrees]
                if sum(minima) > capital_n:
                    continue

                feasible += 1
                slack = capital_n - sum(minima)
                small = sum(
                    degree % 2 == 1 and q * degree < 3 * e
                    for degree in factor_degrees
                )
                large = sum(
                    degree % 2 == 1 and q * degree >= 3 * e
                    for degree in factor_degrees
                )
                huge = sum(
                    degree % 2 == 0 and q * degree >= 6 * e
                    for degree in factor_degrees
                )
                assert small - large - 2 * huge + 2 * slack == -1
                assert slack == 0
                profile = (small, large, huge)
                assert profile in profile_counts
                profile_counts[profile] += 1

    assert checks == 25504
    assert feasible == 776
    assert profile_counts == {
        (0, 1, 0): 622,
        (1, 2, 0): 73,
        (1, 0, 1): 81,
    }
    print(
        "RATE_HALF_PAIRED_BIFORM_FACTOR_TRICHOTOMY_AUDIT_PASS "
        f"partitions={checks} feasible={feasible} profiles={profile_counts}"
    )


if __name__ == "__main__":
    main()
