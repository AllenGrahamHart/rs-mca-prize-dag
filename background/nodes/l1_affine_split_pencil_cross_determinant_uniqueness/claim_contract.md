# Claim contract - L1 affine split-pencil cross-determinant uniqueness

## Inputs

- one fixed affine syndrome cell from
  `l1_bounded_mark_affine_split_pencil_compiler`;
- exact monic degree-`d` defect locators and saturated numerator pairs;
- pairwise disjoint dense petals and their exact marks.

## Output

The cross determinant obeys `(CD4)`. Every cell above
`t ell=2d+v` is a singleton, and every potentially nonsingleton
bounded-polarity arbitrary-locator cell lies in the explicit window `(CD7)`.

## Consumer rule

Consumers may pay the per-chart region `(CD6)` using the compiler's
polynomial support/syndrome count. They must retain cells in `(CD7)`,
non-intrinsic first-match chart supply, and the growing-polarity branch.

## Falsifier

Two distinct exact saturated monic pairs in one fixed support/syndrome cell
with `t ell>2d+v`; or failure of `product_i L_(T_i)|J Delta`.
