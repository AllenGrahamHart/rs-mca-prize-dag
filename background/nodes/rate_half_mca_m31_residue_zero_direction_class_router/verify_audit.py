#!/usr/bin/env python3
"""Independent integer audit of the residue-zero router."""

from math import ceil


def main():
    e, H, c = 98232, 65489, 5
    A = 2 * H - e
    classes = e * (A - c) // (A * A - e * c)
    assert (A, classes) == (32746, 3)
    Q = (950350 - c) // (1965 - c)
    boundary = 1 + classes * (Q - 1)
    assert (Q, boundary) == (484, 1450)
    prefix, budget = 16432695, 16777215
    threshold = budget - prefix - boundary + 1
    assert threshold == 343071
    core = ceil((threshold * 67454 - 1048582) / (threshold - 1))
    assert core == 67452
    print("RATE_HALF_MCA_M31_RESIDUE_ZERO_DIRECTION_CLASS_ROUTER_AUDIT_PASS "
          "classes=3 boundary=1450 top=343071 core=67452")


if __name__ == "__main__":
    main()
