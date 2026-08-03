#!/usr/bin/env python3
"""Exact Route-T budget check for the conditional SL-2 close."""

ROWS = (
    ("RowC 1/4", 1024, 261, 828,
     5316907684064982757706454868357010004),
    ("RowC 1/8", 1024, 133, 967,
     5316911983139662876649441458673435346),
    ("RowC 1/16", 1024, 67, 479,
     5316911982997375233704305906531142556),
    ("prize 1/4", 2**41, 558345748481, 36839268578566,
     147353487015924860717424845526640272811),
    ("prize 1/8", 2**41, 283467841537, 43010571891409,
     147353491314999540836367831842078791337),
    ("prize 1/16", 2**41, 141733920769, 44764496190275,
     147353491314857253193422696148202577845),
)


def charged_column(n, A, sum_l, numerator):
    proper_band = (numerator * n * n // 25) * sum_l
    cascade = (n // 2) * (n - A + 1)
    return proper_band + cascade


checks = 0
for name, n, A, sum_l, headroom in ROWS:
    assert headroom >= 13 * n**3, name
    checks += 1
    if name.startswith("prize"):
        assert headroom < 14 * n**3, name
        checks += 1
    assert charged_column(n, A, sum_l, 17) <= headroom, name
    checks += 1

# This negative control protects the tight two rows from a rounded rewrite.
failed_at_18 = tuple(
    name
    for name, n, A, sum_l, headroom in ROWS
    if name.startswith("prize")
    and charged_column(n, A, sum_l, 18) > headroom
)
assert failed_at_18 == ("prize 1/8", "prize 1/16")
checks += 1

print(f"XR_GRADED_TANGENT_BAND_CHARGE_ALL_PASS checks={checks}")
