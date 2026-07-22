# Upstream crosswalk - tangent Hasse root pinning

## Base-field-normalized split-pencil census

The tangent/common-factor portion of the low-remainder Pade section has a
canonical base-field owner `D=gcd(L,Q)`.  Fixing its `r` domain roots forces
the codeword polynomial to match the received polynomial to multiplicity two
at those roots.  The resulting confluent interpolation fiber has exact
dimension `max(k-2r,0)` when nonempty.

## What is portable

This supplies an exact SPI/shift-pair ledger input: tangent degree `r`, root
set `D`, affine codeword fiber, and a proof that projected rank can lose at
most `r`.  It is constants-first and works over the base field in every
characteristic.

## Remaining statement

Raw summation over all `binom(n,r)` root sets is generally too expensive.
Upstream still needs either an exchange/quotient mechanism showing that only
a sparse family of `D` is feasible, or a first-owner payment absorbing the
feasible family.  The packet should be vendored as the exact tangent stratum
normal form, not as a complete tangent bound.
