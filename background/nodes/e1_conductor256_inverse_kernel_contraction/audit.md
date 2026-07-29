# Audit

## Arithmetic seams

- The parent verifier is SHA-256 pinned before import.
- Complex inversion uses `conj(kappa)/|kappa|^2`; the squared-modulus lower
  endpoint is checked strictly positive.
- Every complex product and sum is rounded outward with the parent's Decimal
  interval operations.
- The inverse DFT omits frequency zero because both vectors are zero-sum.
- Every imaginary kernel interval contains zero, as required by exact
  conjugate pairing.
- The independent audit reconstructs the 64 time-domain identities
  `sum_r q_(d+r)f_r=delta_(d,0)-1/64`; it does not trust the DFT indexing as
  an unchecked convention.
- The coordinate operator uses half the global real range, not a sum of
  per-frequency magnitude bounds.
- The aggregate operator uses a cyclic row sum, and the final integer `L1`
  bound consumes its evenness.

## Scope ruling

The new box still contains the 38-trillion balanced `0,+1,-1` family already
proved to lie in the universal weighted ellipsoid. This contraction improves
a sparse-first search but does not rehabilitate ellipsoid-first enumeration.

## Compute ruling

The verifier performs 64 by 63 directed interval operations with tiny RAM and
no Modal credit. No exponent-vector enumeration is run.
