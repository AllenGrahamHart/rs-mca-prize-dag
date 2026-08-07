# Audit

1. The old 15-layer theorem was valid only at rate `1/2`; the replacement
   uses `15,14,13,12` layers and covers all four exact-slice rows.
2. No generated-field balance guard is used.
3. Entropy comparisons and final budgets are verified as exact integer
   inequalities; printed corridor depths are not hypotheses.
4. The result counts all null sets in the paid layers, so quotient or trade
   overlaps cannot invalidate the upper bound.
5. A non-load-bearing replay at the printed depths puts the bound with one
   extra layer at `2^128.998`, `2^125.389`, `2^125.086`, and `2^125.090`.
   The displayed widths are therefore maximal for this interpolation payment
   on those rows; a wider strip needs a new structural input.
