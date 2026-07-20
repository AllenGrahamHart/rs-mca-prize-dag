# Claim contract - L1 marked common-pencil CRT fiber bound

## Inputs

- `l1_marked_constant_shift_forney_window_normal_form` for `m<=t<=2m` in
  every away-from-boundary common-pencil cell;
- `l1_bounded_polarity_marked_full_pencil_reduction` for the fixed-chart
  reconstruction and selected mark charge `v<=p`.

## Output

For fixed defect locator and marks, the numerator is unique when `t>=m+1`
and has multiplicity at most `q^(2p)` when `t=m`.

## Consumer Rule

Consumers may discard numerator multiplicity up to the fixed polynomial
factor `q^(2P)`. They must still count squarefree defect locators and retain
arbitrary-locator cells.

## Falsifier

Two distinct numerators in an asserted singleton fiber, an endpoint fiber
larger than `q^(eta+v+1)`, failure of `eta<=p-1`, or noninjective codeword
reconstruction from fixed chart/locator/numerator data.
