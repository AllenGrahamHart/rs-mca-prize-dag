#!/usr/bin/env python3
"""Exact finite-field replay of the scalar-weld equations."""

Q = 101
E = 183251937963
P = 274877906944


def row_poly(x: int, t: int) -> int:
    return (t + 3) * (t - x) * (t - (x - 1)) % Q


def fiber_poly(t: int, x: int) -> int:
    return (x - t) * (x - (t + 1)) % Q


def weld_replay() -> None:
    xset = list(range(5, 11))
    zset = [1, 2, 3, 4]
    lam = {x: 1 for x in xset}
    rows = []

    for t in zset:
        nonincident = [x for x in xset if fiber_poly(t, x) != 0]
        anchor = nonincident[0]
        for x in nonincident[1:]:
            value = (
                lam[x] * row_poly(x, t) * fiber_poly(t, anchor)
                - lam[anchor] * row_poly(anchor, t) * fiber_poly(t, x)
            ) % Q
            rows.append(value)
    assert rows and rows == [0] * len(rows)

    lam[xset[-1]] = 2
    caught = False
    for t in zset:
        nonincident = [x for x in xset if fiber_poly(t, x) != 0]
        anchor = nonincident[0]
        for x in nonincident[1:]:
            value = (
                lam[x] * row_poly(x, t) * fiber_poly(t, anchor)
                - lam[anchor] * row_poly(anchor, t) * fiber_poly(t, x)
            ) % Q
            caught |= value != 0
    assert caught


def main() -> None:
    assert (3 * E - 1) // 2 == P
    assert 2 * E * (2 * P - 1) == 201487636602438195784362
    assert (P + 2) * (P + 1) == 75557863726738957139970
    weld_replay()
    print("PASS paired scalar-weld gate tamper=1/1")


if __name__ == "__main__":
    main()
