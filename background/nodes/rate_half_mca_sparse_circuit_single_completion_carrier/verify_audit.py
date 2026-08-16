#!/usr/bin/env python3
"""Independent endpoint audit for the single-carrier formula."""

rows = ((2, 29, 30, 9), (3, 36, 38, 8), (9, 1, 9, 2))
for support, maximum, union, dimension in rows:
    assert union - maximum == support - 1
    assert dimension + support == 11
print({"independent_checks": 2 * len(rows)})
