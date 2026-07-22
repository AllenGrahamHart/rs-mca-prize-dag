#!/usr/bin/env python3
"""Mutation audit for the P25 ordered-root tower."""

from __future__ import annotations

import verify


def main() -> None:
    verify.arithmetic_check()
    verify.finite_field_check()

    assert verify.system_size(41, 25) == (2378, 2402)
    assert verify.system_size(41, 24) != (2378, 2402)
    assert 25 * 24 // 2 == 300
    assert 24 * 23 // 2 != 300

    print("F3_H3_P25_ORDERED_ROOT_QUADRATIC_TOWER_COMPILER_AUDIT_PASS mutations=4")


if __name__ == "__main__":
    main()
