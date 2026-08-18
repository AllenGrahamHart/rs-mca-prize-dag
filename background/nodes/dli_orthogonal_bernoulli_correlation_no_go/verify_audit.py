#!/usr/bin/env python3
"""Independent exhaustive r=3 audit of the Bernoulli no-go fixture."""

from __future__ import annotations

from itertools import product


def main() -> None:
    rows_u = []
    rows_v = []
    for block in range(3):
        u = [0] * 12
        v = [0] * 12
        u[4 * block:4 * block + 4] = [1, 1, -1, -1]
        v[4 * block:4 * block + 4] = [1, -1, 1, -1]
        rows_u.append(u)
        rows_v.append(v)

    assert all(sum(row) == 0 for row in rows_u + rows_v)
    assert all(
        sum(a * b for a, b in zip(left, right, strict=True)) == 0
        for left in rows_u
        for right in rows_v
    )

    count_a = count_b = count_joint = 0
    for bits in product((0, 1), repeat=12):
        event_a = all(
            sum(a * bit for a, bit in zip(row, bits, strict=True)) == 0
            for row in rows_u
        )
        event_b = all(
            sum(a * bit for a, bit in zip(row, bits, strict=True)) == 0
            for row in rows_v
        )
        count_a += event_a
        count_b += event_b
        count_joint += event_a and event_b

    assert (count_a, count_b, count_joint) == (6**3, 6**3, 4**3)
    total = 1 << 12
    assert count_joint * total > count_a * count_b
    assert (count_joint * total) ** 2 > 24 * (count_a * count_b) ** 2
    print(
        "DLI_ORTHOGONAL_BERNOULLI_NO_GO_AUDIT_PASS "
        "bits=12 counts=216,216,64 square_root_bound=failed"
    )


if __name__ == "__main__":
    main()
