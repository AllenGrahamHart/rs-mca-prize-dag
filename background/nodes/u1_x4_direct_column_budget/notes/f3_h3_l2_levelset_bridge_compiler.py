#!/usr/bin/env python3
"""Verify the h=3 L2/level-set pair-count compiler."""

from __future__ import annotations

from f3_h3_pair_count_from_charts_compiler import (
    chart_count_for_fiber,
    ordered_fibers,
    root_table,
)


def pair_count_from_r_values(r_values: list[int]) -> int:
    total = 0
    for r_count in r_values:
        if r_count % 6:
            raise AssertionError(("ordered triple count not divisible by 6", r_count))
        n_triples = r_count // 6
        total += n_triples * (n_triples - 1) // 2
    return total


def exact_l2_numer(r_values: list[int]) -> int:
    return sum(r_count * (r_count - 6) for r_count in r_values)


def square_l2_numer(r_values: list[int]) -> int:
    return sum(r_count * r_count for r_count in r_values)


def tail_pair_count(r_values: list[int]) -> tuple[int, dict[int, int]]:
    n_values = [r_count // 6 for r_count in r_values]
    tails: dict[int, int] = {}
    max_n = max(n_values, default=0)
    total = 0
    for level in range(2, max_n + 1):
        count = sum(1 for n_triples in n_values if n_triples >= level)
        tails[level] = count
        total += (level - 1) * count
    return total, tails


def check_ledger(name: str, n: int, r_values: list[int]) -> dict[str, int]:
    pair_total = pair_count_from_r_values(r_values)
    exact_numer = exact_l2_numer(r_values)
    square_numer = square_l2_numer(r_values)
    tail_total, tails = tail_pair_count(r_values)
    if 72 * pair_total != exact_numer:
        raise AssertionError((name, "exact L2 identity", pair_total, exact_numer))
    if tail_total != pair_total:
        raise AssertionError((name, "tail identity", pair_total, tail_total))
    exact_safe = exact_numer <= 1152 * n
    square_safe = square_numer <= 1152 * n
    if exact_safe != (pair_total <= 16 * n):
        raise AssertionError((name, "exact L2 target equivalence"))
    if square_safe and not exact_safe:
        raise AssertionError((name, "square L2 should imply exact safety"))
    return {
        "charts": len(r_values),
        "pairs": pair_total,
        "exact_numer": exact_numer,
        "square_numer": square_numer,
        "safe": int(pair_total <= 16 * n),
        "exact_safe": int(exact_safe),
        "square_safe": int(square_safe),
        "tail_levels": len(tails),
        "max_tail": max(tails.values(), default=0),
    }


def synthetic_ledgers() -> list[tuple[str, int, list[int]]]:
    return [
        ("empty", 64, []),
        ("singletons", 64, [6] * 100),
        ("boundary_exact", 64, [12] * 1024),
        ("one_rich_fiber", 64, [6 * 45]),
        ("mixed_tail_safe", 128, [6 * 8] * 16 + [6 * 3] * 128 + [6] * 256),
    ]


def finite_row_ledgers() -> list[tuple[str, int, list[int]]]:
    rows = []
    for p, n in ((97, 16), (97, 32), (193, 64)):
        hset = set(root_table(p, n))
        fibers = ordered_fibers(p, n)
        selected = sorted(
            ((len(ordered), key, ordered) for key, ordered in fibers.items()),
            reverse=True,
        )[:32]
        r_values = []
        for _, key, ordered in selected:
            t_count, epsilon, skipped = chart_count_for_fiber(p, hset, key, ordered)
            if skipped:
                continue
            r_count = t_count + epsilon
            if r_count != len(ordered):
                raise AssertionError((p, n, key, r_count, len(ordered)))
            r_values.append(r_count)
        rows.append((f"finite_row_p{p}_n{n}", n, r_values))
    return rows


def main() -> None:
    print("h=3 L2/level-set bridge compiler")
    for name, n, r_values in synthetic_ledgers() + finite_row_ledgers():
        row = check_ledger(name, n, r_values)
        print(
            f"{name}: n={n} charts={row['charts']} pairs={row['pairs']} "
            f"exact_numer={row['exact_numer']} square_numer={row['square_numer']} "
            f"safe={row['safe']} exact_safe={row['exact_safe']} "
            f"square_safe={row['square_safe']} tail_levels={row['tail_levels']} "
            f"max_tail={row['max_tail']}"
        )
    print("exact condition: sum R_z(R_z-6) <= 1152 n")
    print("level-set identity: P_total = sum_{m>=2} (m-1)L_m")
    print("H3_L2_LEVELSET_BRIDGE_COMPILER_PASS")


if __name__ == "__main__":
    main()
