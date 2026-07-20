#!/usr/bin/env python3
"""Verify the joint-Johnson source-scale gate by exact integer arithmetic."""

from __future__ import annotations


RATES = (2, 4, 8, 16)


def official_source_audit() -> tuple[int, int]:
    excluded = 0
    live = 0
    for rate in RATES:
        for k in range(2, 201):
            total = (rate - 1) * k + 1
            for ell in range(1, total + 1):
                petals, background = divmod(total, ell)
                if petals == 0:
                    continue
                n_core = k - 1
                if petals < 3 * (rate - 1):
                    assert n_core + background < 4 * ell
                    assert n_core < 3 * ell
                    excluded += 1
                else:
                    live += 1
    return excluded, live


def variance_audit() -> tuple[int, int]:
    paid = 0
    tail = 0
    for n_core in range(2, 51):
        for ell in range(1, 16):
            for background in range(ell):
                for a in range(n_core + 1):
                    for u in range(background + 1):
                        c = a + u - ell
                        if not (0 <= c <= a):
                            continue
                        if background == 0:
                            nonpositive = a * a <= n_core * c
                        else:
                            nonpositive = (
                                background * a * a + n_core * u * u
                                <= n_core * background * c
                            )
                        if nonpositive:
                            assert n_core + background >= 4 * ell
                            assert n_core >= 3 * ell + 1
                            tail += 1
                        else:
                            paid += 1
    return paid, tail


def boundary_family() -> tuple[tuple[int, int, int, int, int], ...]:
    rows = []
    for rate in RATES:
        ell = 2 * rate
        background = 2 * rate - 1
        k = 6 * rate + 2
        petals = 3 * (rate - 1)
        assert (rate - 1) * k + 1 == petals * ell + background
        assert (k - 1) + background == 4 * ell
        rows.append((rate, k, ell, background, petals))
    return tuple(rows)


def main() -> None:
    excluded, live = official_source_audit()
    paid, tail = variance_audit()
    rows = boundary_family()
    assert excluded > 0 and live > 0 and paid > 0 and tail > 0
    print(
        "L1_JOINT_JOHNSON_SOURCE_SCALE_GATE_PASS "
        f"excluded={excluded} live={live} paid={paid} tail={tail} "
        f"boundary={rows}"
    )


if __name__ == "__main__":
    main()
