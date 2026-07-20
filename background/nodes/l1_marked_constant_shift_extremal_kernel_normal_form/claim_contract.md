# Claim contract - L1 marked constant-shift extremal kernel normal form

## Inputs

- `l1_marked_constant_shift_multistrip_exclusion` for the marked `P`-adic
  kernel and oversized-common-factor argument;
- `pma_saturated_mixed_support_kernel` for exact `gcd(F,W)=1` in the L1
  application.

## Output

The upper survivor endpoint `T=2m` is an exact rank-`2m`, two-generator
polynomial matrix whose determinant is the complete quotient locator `Q`.
The endpoint is genuinely nonempty in every strip.

## Consumer Rule

Consumers may replace the endpoint by `(EK3)--(EK5)`, but may not call it
empty or already profile-owned. The lower-petal cells remain separate.

## Falsifier

A saturated endpoint tuple with row rank different from `2m`, zero or
non-`Q` kernel determinant, failure of `(EK4)--(EK5)`, or failure of the
sharp family `(EK6)`.
