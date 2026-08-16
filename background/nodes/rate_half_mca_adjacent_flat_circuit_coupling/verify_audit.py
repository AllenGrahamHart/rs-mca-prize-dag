#!/usr/bin/env python3
"""Independent coefficient audit for adjacent-flat circuit coupling."""

from math import comb


checks = 0
for r, n in ((1, 4), (2, 5), (3, 7), (4, 8)):
    b = n - 1
    high = comb(n, r + 2)
    assert (r + 2) * high == (b - r) * comb(n, r + 1)
    assert (r + 1) * high < (b - r) * comb(n, r + 1)
    checks += 2
print({"independent_checks": checks})
