# Audit - L1 marked constant-shift multistrip exclusion

## Checked axes

1. The enlarged gcd is exactly the total selected mark locator `J`.
2. Rank at least `2m+1`, not full rank, already forces a one-dimensional
   block kernel and a common divisor larger than `J`.
3. The cross product has degree at most `2m`, so `2m+1` distinct labels are
   the exact root-count threshold used by the proof.
4. Two independent kernel pairs force primitive degree at most `m-1`.
5. The final common-factor degree is bounded from the actual degree of `F'`;
   no cancellation across the product `A(P)H` is possible.
6. The source application remains restricted to common constant-shift petal
   locators and charges only the selected missing degrees.
7. The lower petal-window endpoint uses the strict maximality cap `r<ell`;
   replacing it by `r<=ell` loses the `+1` in `(MT4)`.

## Remaining attack

Classify the low-petal kernel rank cells `t<=2m`, produce a
contributor-dependent common-pencil bridge, or handle arbitrary locator
modules directly.
