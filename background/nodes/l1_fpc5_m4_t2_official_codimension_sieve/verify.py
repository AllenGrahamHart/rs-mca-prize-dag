#!/usr/bin/env python3
"""Check the official codimension inequalities on small congruent analogues."""

from __future__ import annotations


def main() -> None:
    cells = 0
    for k in (2**4, 2**8, 2**12):
        assert k % 5 == 1
        for rate_denominator in (2, 4):
            source = (rate_denominator - 1) * k + 1
            for ell in range(1, source // 4 + 1):
                b = source - 4 * ell
                if not 0 <= b < ell:
                    continue
                max_s = min(ell - 1, b, k - 1 - ell)
                if max_s < 0:
                    continue
                codim = ell - max_s - 1
                if rate_denominator == 2:
                    assert codim >= 2
                    assert (ell - b) % 5 == 3
                else:
                    assert codim >= (k + 4) // 5
                cells += 1
    k = 2**40
    assert k % 5 == 1
    assert (k + 4) % 5 == 0
    print(f"FPC5_M4_T2_CODIMENSION_PASS analogue_cells={cells} official_k={k}")


if __name__ == "__main__":
    main()
