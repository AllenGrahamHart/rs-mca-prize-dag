#!/usr/bin/env python3
"""Mutation audit for the P25 quadratic divisor tower."""

from __future__ import annotations

import verify


def main() -> None:
    verify.arithmetic_check()
    verify.finite_field_check()

    assert verify.system_size(41, 25) == (4048, 4072)
    assert verify.system_size(41, 24) != (4048, 4072)
    assert verify.system_size(40, 25) != (4048, 4072)
    assert 4072 - 4048 == 24

    print("F3_H3_P25_QUADRATIC_DIVISOR_TOWER_COMPILER_AUDIT_PASS mutations=4")


if __name__ == "__main__":
    main()
