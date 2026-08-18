#!/usr/bin/env python3
"""Independent quotient audit for the two-threshold route wall."""

from math import prod


def main() -> None:
    m = 1_116_048
    h_total = 38_385
    x0 = 18_166
    d2_values = [(x * (h_total - x) ** 2, x) for x in range(x0, h_total)]
    d3_values = [(x * (h_total - x), x) for x in range(x0, h_total)]
    d2, at2 = max(d2_values)
    d3, at3 = max(d3_values)
    assert (d2, at2) == (7_426_405_419_526, 18_166)
    assert d3 == 368_352_056 and at3 in (19_192, 19_193)

    count2 = prod((m, m - 1, m - 2)) // d2
    count3 = prod((m, m - 1)) // d3
    charge = count2 * 63_397_365_764 + count3 * 16_100_859_197_492
    assert (count2, count3) == (187_184, 3_381)
    assert charge - 65_167_969_673_715_470 == 1_136_007_786_173_558
    print(
        "RANK11_FACTOR_FLAG_TWO_THRESHOLD_WALL_AUDIT_PASS "
        f"at2={at2} at3={at3}"
    )


if __name__ == "__main__":
    main()
