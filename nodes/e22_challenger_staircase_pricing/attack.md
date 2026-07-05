# ATTACK - e22_challenger_staircase_pricing

Use light local computation only.

## Formula extraction

Extract candidate formulas from small exhaustive E22 cells already covered by
the gate and any future remote `challenger_count_grid`. The target is not a
fit to toy data alone; it must be a parametrization with an injective map to
codewords.

## Expected structure

The ledger says the mixed-petal anomaly is the quotient-coset staircase:
`L_B G(X^M)` locators, with exact counts of the form
`C(n/M - 1, h)` at matched radius. Verify the exact parameters, equivalences,
and scalar/core multiplicities before using this in list arithmetic.

## Arithmetic comparison

Once the formula is proved, add the challenger column to the planted column
and run the same exact integer-window comparison used by
`list_planted_arithmetic`.
