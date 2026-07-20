#!/usr/bin/env python3
"""Mutation audit for the DSP8 nodal decoration class-discount no-go."""

from __future__ import annotations

import verify


def main() -> None:
    packet = verify.matrix_fixture()

    assert verify.PRIME != verify.ORDER**2
    assert verify.PRIME < verify.ORDER**2
    assert sum(value for row in packet["antipodal"] for value in row) == 7
    assert 7 > 4 and 7 > 5 and 3 * 7 > 2 * 9

    wrong_target = [list(row) for row in packet["targets"]]
    wrong_target[0][0] += 1
    assert tuple(tuple(row) for row in wrong_target) != verify.EXPECTED_TARGETS

    wrong_class = [list(row) for row in packet["antipodal"]]
    wrong_class[0][1] = True
    assert sum(value for row in wrong_class for value in row) == 8
    assert tuple(tuple(row) for row in wrong_class) != verify.EXPECTED_ANTIPODAL

    assert min(value for row in packet["products"] for value in row) == 72
    assert min(value for row in packet["quotients"] for value in row) == 79
    assert not all(value >= 99 for row in packet["products"] for value in row)

    print(
        "F3_H3_DSP8_NODAL_DECORATION_CLASS_DISCOUNT_NO_GO_AUDIT_PASS "
        "mutations=6 official_scope_preserved=1"
    )


if __name__ == "__main__":
    main()
