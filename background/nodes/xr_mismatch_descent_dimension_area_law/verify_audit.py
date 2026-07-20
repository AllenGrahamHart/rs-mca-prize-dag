#!/usr/bin/env python3
"""Independent edge-case audit of the XR dimension-area law."""

from __future__ import annotations


def audit_chain(
    states: tuple[tuple[int, int], ...], h: int, drops: tuple[int, ...]
) -> None:
    transitions = len(states) - 1
    assert transitions == len(drops)
    H = h + 1
    for index, d in enumerate(drops):
        n, k = states[index]
        next_n, next_k = states[index + 1]
        assert next_n <= n - k - h
        assert next_k == k - d
        assert 0 <= d <= k - 1
        assert next_n >= next_k + h

    area = sum(k + h for _, k in states[:-1])
    assert area <= states[0][0] - H
    assert sum(drops) == states[0][1] - states[-1][1]
    assert sum(k - 1 for _, k in states[:-1]) <= states[0][0] - H - transitions * H

    depth_cap = states[0][0] // H - 1
    slack = depth_cap - transitions
    remainder = states[0][0] - H - depth_cap * H
    assert sum(k - 1 for _, k in states[:-1]) <= remainder + slack * H


def main() -> None:
    # Maximal-depth dimension-one chain: XDA6 is sharp.
    h = 3
    states = tuple((20 - 4 * index, 1) for index in range(5))
    audit_chain(states, h, (0, 0, 0, 0))

    # One large external-zero collapse followed by the dimension-one tail.
    states = ((30, 7), (20, 1), (16, 1), (12, 1), (8, 1), (4, 1))
    audit_chain(states, h, (6, 0, 0, 0, 0))

    # Threshold layer cake on the second fixture.
    dimensions = [k for _, k in states[:-1]]
    layer_sum = sum(
        sum(k >= kappa for k in dimensions)
        for kappa in range(1, max(dimensions) + 1)
    )
    assert layer_sum == sum(dimensions)

    print("AUDIT_XR_MISMATCH_DESCENT_DIMENSION_AREA_LAW_PASS fixtures=2")


if __name__ == "__main__":
    main()

