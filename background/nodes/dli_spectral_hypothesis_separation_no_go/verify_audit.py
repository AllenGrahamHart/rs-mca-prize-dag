#!/usr/bin/env python3
"""Independent syndrome-mask audit for the spectral separation no-go."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def main() -> None:
    n, q, root = 16, 17, 3
    records = []
    for bits in product((0, 1), repeat=n):
        zeros = {
            frequency
            for frequency in range(1, n)
            if sum(bits[i] * pow(root, frequency * i, q) for i in range(n)) % q == 0
        }
        records.append((zeros, all(bits[i] == bits[i + 8] for i in range(8))))

    def count(required: set[int], primitive: bool | None = None) -> int:
        return sum(
            required <= zeros and (primitive is None or (not owner) == primitive)
            for zeros, owner in records
        )

    a, b = {2, 3}, {4, 6}
    assert max(a | b) < n // 2 and not a & b
    assert (count(a), count(b), count(a | b), count(a | b, True)) == (160, 388, 20, 16)
    first = Fraction(16 * (1 << n), 160 * 388)
    assert first == Fraction(8192, 485) and first * first > 32

    rows = ({1}, {2, 6}, {4})
    assert all(len({(f & -f).bit_length() - 1 for f in row}) == 1 for row in rows)
    margins = tuple(count(row) for row in rows)
    union = set().union(*rows)
    assert margins == (3856, 1296, 5124)
    assert (count(union), count(union, True)) == (20, 16)
    constant = Fraction(20 * (1 << 32), 3856 * 1296 * 5124)
    second = constant**2 * (1 - Fraction(1, 5) ** 2)
    assert second == Fraction(2251799813685248, 208440030324267)
    assert second * second > 64
    print(
        "DLI_SPECTRAL_HYPOTHESIS_NO_GO_AUDIT_PASS "
        "words=65536 one_sided=8192/485 tensor2_fires=1"
    )


if __name__ == "__main__":
    main()
