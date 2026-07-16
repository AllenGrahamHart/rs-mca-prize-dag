# Claim contract - PMA three-petal projective Johnson bound

## Inputs

1. A fixed three-petal reduced mu-basis with coefficient allowances summing
   to `e-1`.
2. A core disjoint from the determinant/petal product.
3. Projective primitive coefficient pairs producing monic split degree-`d`
   core divisors.
4. For official consequences, the exact maximal-source equations.

## Outputs

1. Pairwise core-root intersection at most `e-1`.
2. The exact projective Johnson bound
   `N(d-e+1)/(d^2-N(e-1))` when the denominator is positive.
3. A complete `16n^3` payment for rate-quarter `M=4,t=3`.
4. Complete payment for rate-half `M=4,t=3` when `b<=6`.
5. The explicit necessary non-Johnson tail (PJ8).

## Consumer obligation

Delete all positive-denominator cells before attacking the remaining tail.
Any successor must preserve coefficient primitivity, exact defect, carried
source, touched triple, and first-match ownership.

## Nonclaims

- no count when `J<=0`;
- no assertion that the residual tail is populated;
- no two-petal, larger-source, or partial-petal payment;
- no promotion of `petal_mixed_amplification`.

## Falsifiers

- two distinct primitive projective pairs with more than `e-1` common core
  roots;
- a compatible root-set family exceeding (PJ4) with `J>0`;
- a valid rate-quarter upper cell with `J<=0`;
- a valid rate-half `b<=6` upper cell with `J<=0`.
