#!/usr/bin/env python3
"""Replay the factorwise Bezout four-shape arithmetic."""


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def ordinary_records():
    records = []
    for b in range(3):
        for t in range(4):
            m = 2 * (b - t)
            if m <= 0 or m % 2:
                continue
            r = m - b - t
            if r < 0:
                continue
            n = 3 * m // 2
            ell = 2 * b
            c = 3 * m // 2
            require(c == r + ell, "ordinary capacity")
            records.append((m, n, r, b, t, ell))
    return sorted(records)


ORDINARY = ordinary_records()
EXPECTED_ORDINARY = [(2, 3, 1, 1, 0, 2), (4, 6, 2, 2, 0, 4)]
require(ORDINARY == EXPECTED_ORDINARY, "ordinary record classification")


def shapes(e):
    candidates = []
    for quadratic_count in range(3):
        for quartic_count in range(2):
            ordinary = (
                [EXPECTED_ORDINARY[0]] * quadratic_count
                + [EXPECTED_ORDINARY[1]] * quartic_count
            )
            if sum(row[3] for row in ordinary) > 2:
                continue
            m_o = sum(row[0] for row in ordinary)
            n_o = sum(row[1] for row in ordinary)
            r_o = sum(row[2] for row in ordinary)
            b_o = sum(row[3] for row in ordinary)
            t_o = sum(row[4] for row in ordinary)
            ell_o = sum(row[5] for row in ordinary)

            large = (
                e - 2 - m_o,
                (3 * e - 7) // 2 - n_o,
                e - 7 - r_o,
                2 - b_o,
                3 - t_o,
                4 - ell_o,
            )
            m, n, r, b, t, ell = large
            if min(m, n, r, b, t, ell) < 0 or m % 2 != 1:
                continue
            if 2 * n - 3 * m != -1:
                continue
            if m != e + 2 * b - 2 * t:
                continue
            if (3 * m - e) // 2 != r + ell:
                continue
            if 7 * m < 3 * e or 5 * m < 3 * e - 10:
                continue
            candidates.append((large, tuple(sorted(ordinary))))
    return sorted(candidates)


def expected(e):
    table = [((e - 2, (3 * e - 7) // 2, e - 7, 2, 3, 4), ())]
    if e >= 9:
        table.append((
            (e - 4, (3 * e - 13) // 2, e - 8, 1, 3, 2),
            (EXPECTED_ORDINARY[0],),
        ))
    if e >= 11:
        table.extend([
            (
                (e - 6, (3 * e - 19) // 2, e - 9, 0, 3, 0),
                (EXPECTED_ORDINARY[1],),
            ),
            (
                (e - 6, (3 * e - 19) // 2, e - 9, 0, 3, 0),
                (EXPECTED_ORDINARY[0], EXPECTED_ORDINARY[0]),
            ),
        ])
    return sorted(table)


checks = 1
for e in list(range(7, 200, 2)) + [183251937963]:
    actual = shapes(e)
    require(actual == expected(e), f"shape exhaustion e={e}")
    checks += 1
    for large, ordinary in actual:
        all_rows = (large, *ordinary)
        require(sum(row[0] for row in all_rows) == e - 2, "parameter total")
        require(sum(row[1] for row in all_rows) == (3 * e - 7) // 2, "row total")
        require(sum(row[2] for row in all_rows) == e - 7, "padding total")
        require(sum(row[3] for row in all_rows) == 2, "correction total")
        require(sum(row[4] for row in all_rows) == 3, "residual total")
        require(sum(row[5] for row in all_rows) == 4, "contact total")
        checks += 6

official = expected(183251937963)
require({row[0][0] for row in official} == {
    183251937961,
    183251937959,
    183251937957,
}, "official large degrees")
checks += 1

print(f"RATE_HALF_COLLISION_FACTORWISE_BEZOUT_SHAPES_PASS checks={checks}")
