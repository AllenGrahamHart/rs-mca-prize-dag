#!/usr/bin/env python3
"""Replay the finite arithmetic in the squarefree cubic gap-one theorem."""

from itertools import product


E = 183_251_937_963
DELTA = 2 * E - 1


def global_regimes():
    out = []
    for i0, w, eps in product(range(2), range(3), range(3)):
        r_out = 1 - w - i0 - eps
        if r_out == 0:
            out.append((i0, w, eps))
    return out


assert global_regimes() == [(0, 0, 1), (0, 1, 0), (1, 0, 0)]

q_rows = [q for q in product(range(0, 7, 3), repeat=3) if sum(q) == 3]
assert q_rows == [(0, 0, 3), (0, 3, 0), (3, 0, 0)]


def check_row(c, eps, q, augmented):
    d = E - c
    t = c + eps - q
    assert 0 <= t <= d
    horizontal = 2 * d - t + eps

    if eps == 0:
        vertical = d + t + q
        contact = d + q // 3
    elif augmented == "new":
        assert t >= 1
        vertical = d + t - 1 + q
        contact = d + q // 3
    elif augmented == "overlap":
        assert d - t >= 1
        assert q == 3
        vertical = d + t + 2
        contact = d + 1
    else:
        raise AssertionError("bad augmented type")

    assert vertical == E
    assert horizontal + vertical == 3 * contact


check_row(c=7, eps=0, q=0, augmented=None)
check_row(c=7, eps=0, q=3, augmented=None)
check_row(c=7, eps=1, q=0, augmented="new")
check_row(c=7, eps=1, q=3, augmented="new")
check_row(c=7, eps=1, q=3, augmented="overlap")

for i0, w, eps in global_regimes():
    c_sum = E + 2 + i0
    t_sum = E - w
    assert c_sum + eps - t_sum == 3
    i_e = DELTA - 1 - i0
    assert i_e + 1 + i0 == DELTA
    picard_degree = (E + 2 + i0) - 1 - i0
    assert picard_degree == E + 1

print(
    "CUBIC_SQUAREFREE_GAP_ONE_NORMAL_FORMS_PASS",
    f"e={E}",
    f"regimes={len(global_regimes())}",
    f"correction_rows={len(q_rows)}",
)
