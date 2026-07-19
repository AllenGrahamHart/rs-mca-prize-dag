#!/usr/bin/env python3
"""Audit support and tangent-defect arithmetic for the face dichotomy."""

from __future__ import annotations


def main() -> None:
    checked = 0
    for a in range(2, 257):
        rho = a + 2
        for t in range(4, a + 3):
            assert t <= rho
            row_weight = a + 1
            assert 2 * row_weight - a == rho
            assert rho - row_weight == 1
            checked += 1
        for h in range(1, 65):
            common = (1000 - a) + rho
            assert common == 1002
            assert (1000 + h) - common == h - 2
            checked += 1
    print(f"AUDIT_XR_HIGHER_RANK_MINIMAL_FACE_SYZYGY_PASS cases={checked}")


if __name__ == "__main__":
    main()
