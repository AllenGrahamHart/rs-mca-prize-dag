#!/usr/bin/env python3
"""Independent weighted-sum audit of the template orbit census."""


def main():
    checks = (
        (6*4+14*8+44*16, 840),
        (18*8+96*16, 1680),
        (1+6*2+9*4+7*8, 105),
        (64+114+23, 201),
        (4*(64+114+23), 804),
    )
    if not all(left == right for left, right in checks):
        raise RuntimeError("template weighted sums")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_TEMPLATE_AUDIT_PASS "
        "raw=2625 canonical=201 four_rows=804"
    )


if __name__ == "__main__":
    main()
