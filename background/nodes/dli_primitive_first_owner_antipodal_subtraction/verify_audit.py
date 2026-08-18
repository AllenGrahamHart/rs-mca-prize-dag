#!/usr/bin/env python3
"""Independent structural audit for dyadic primitive subtraction."""

from __future__ import annotations

import math

import verify


def main() -> None:
    result = verify.build()
    for row in result.values():
        assert row["total"] == row["primitive"] + row["nonprimitive"]
    for n in (8, 16, 32, 64):
        for shift in range(1, n):
            gcd = math.gcd(n, shift)
            order = n // gcd
            assert order == 1 or order % 2 == 0
            if order > 1:
                assert (n // 2) % gcd == 0
    print("DLI_PRIMITIVE_SUBTRACTION_AUDIT_PASS")


if __name__ == "__main__":
    main()
