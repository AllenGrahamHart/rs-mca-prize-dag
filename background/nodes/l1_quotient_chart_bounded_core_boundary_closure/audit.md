# Audit - L1 quotient-chart bounded core-boundary closure

## Checked axes

1. The `2^M` support factor and `2^N` quotient-core factor combine to
   `2^(M+N)`; `(BC1)` is required to make this polynomial at the cutoff.
2. Polarized entropy counts symmetric-difference points after the
   dense/sparse orientation is fixed.
3. Background agreements need no multiplier: the defect locator and
   numerator reconstruct the codeword and hence all exact agreements.
4. The ambient `2^N` bound avoids any unproved quotient flatness claim.
5. The strict CRT theorem and thin-edge CRT theorem partition every degree
   strip; the latter requires `ell>2P_0`.
6. The exponent depends on fixed `P_0,B_0,c_0,gamma`, but not on `d` or the
   strip index.
7. Nothing here bounds the number of source charts.

## Remaining attack

For quotient/coset common-pencil charts, handle unbounded partial-core-fiber
boundary, then prove aggregate first-match control across source charts.
Non-quotient cores and arbitrary petal locators remain separate.
