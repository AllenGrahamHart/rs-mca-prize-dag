#!/usr/bin/env python3
"""Classify residual M720 h=7..20 scan cells under the Modal window rule."""

from __future__ import annotations

from math import comb

COUNT_CEILING = 6_000_000


def chosen_window(n: int, h: int) -> tuple[int, int]:
    best = 2 * h
    best_cost = comb(best - 1, h - 1) + comb(best, h)
    w = 2 * h
    while w <= n:
        cost = comb(w - 1, h - 1) + comb(w, h)
        if cost <= COUNT_CEILING:
            best = w
            best_cost = cost
            w += 1
        else:
            break
    return best, best_cost


def main() -> None:
    under_ceiling_complete = []
    over_ceiling_complete = []
    slices = []
    for h in range(7, 21):
        for n in (16, 32, 64, 128, 256, 1024):
            if n < 2 * h:
                continue
            w, cost = chosen_window(n, h)
            for exp in (2, 3):
                rec = (n, h, exp, w, cost)
                if w == n and cost <= COUNT_CEILING:
                    under_ceiling_complete.append(rec)
                elif w == n:
                    over_ceiling_complete.append(rec)
                else:
                    slices.append(rec)

    expected_under = {
        (16, 7, 2),
        (16, 7, 3),
        (32, 7, 2),
        (32, 7, 3),
        (16, 8, 2),
        (16, 8, 3),
    }
    expected_over = {
        (32, 16, 2),
        (32, 16, 3),
    }
    assert {(n, h, exp) for n, h, exp, _, _ in under_ceiling_complete} == expected_under
    assert {(n, h, exp) for n, h, exp, _, _ in over_ceiling_complete} == expected_over
    assert all(w < n for n, _, _, w, _ in slices)

    print("under-ceiling complete cells:")
    for rec in under_ceiling_complete:
        print(f"  n={rec[0]} h={rec[1]} q_exp={rec[2]} W={rec[3]} cost={rec[4]}")
    print("over-ceiling complete-window cells:")
    for rec in over_ceiling_complete:
        print(f"  n={rec[0]} h={rec[1]} q_exp={rec[2]} W={rec[3]} cost={rec[4]}")
    print(f"window-slice cells: {len(slices)}")
    print("M720 residual slice metadata PASS")


if __name__ == "__main__":
    main()
