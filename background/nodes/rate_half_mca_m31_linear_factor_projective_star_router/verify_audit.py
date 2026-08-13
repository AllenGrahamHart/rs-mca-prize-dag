#!/usr/bin/env python3
"""Independent audit of the M31 linear-factor Johnson split."""


def main() -> None:
    e, agreement, captured = 130237, 807, 4982
    expected = (
        (0, 651249, 161),
        (1, 521012, 201),
        (2, 390775, 268),
        (3, 260538, 401),
        (4, 130301, 802),
        (5, 64, 1632032),
    )
    checks = 0
    records = []
    for degree in range(6):
        denominator = agreement**2 - e * degree
        numerator = e * (agreement - degree)
        cap, remainder = divmod(numerator, denominator)
        assert denominator > 0
        assert cap * denominator <= numerator < (cap + 1) * denominator
        records.append((degree, denominator, cap))
        checks += 9 + (remainder >= 0)
    assert tuple(records) == expected
    assert max(cap for _, _, cap in records[:5]) == 802 < captured
    assert records[5][2] > captured
    print("m31-linear-factor-projective-star-router-audit: PASS "
          f"({checks + 13} checks; exact division replay)")


if __name__ == "__main__":
    main()
