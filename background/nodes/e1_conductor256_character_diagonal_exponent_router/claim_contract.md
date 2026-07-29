# Claim contract

## Consumed theorems

- `e1_conductor256_full_unit_circular_basis`: the 63 units `eta_a` are the
  full unit basis modulo `mu_256`, and their log columns are independent.
- `e1_pure_cofactor_common_prime_associate_router`: same-root pure-cofactor
  collisions are unit associates; fixed-cofactor units and inverses satisfy
  the printed coefficient boxes and the log-body bound `(CER6)`.

## New proved content

1. The full conductor-256 log map is a cyclic convolution on the 64-element
   group `G`.
2. Its 63 nontrivial character eigenvalues are the explicit nonzero numbers
   `(CER1)`.
3. The log body implies the Fourier, Euclidean, coordinate, and weighted-
   ellipsoid bounds `(CER7)--(CER10)`.
4. Together with exact sparse multiplication, these bounds give a complete
   finite exponent search for each fixed-cofactor associate family.

## Guards

1. The theorem compares collisions at one reduction root and in one fixed
   cofactor. It does not merge the four cofactors without summing their
   separately certified counts.
2. Nonvanishing of `kappa_j` is proved from the full-unit basis and log-map
   injectivity, not from floating-point evaluation.
3. A numerical FFT is not a certificate. An implementation must use outward
   interval bounds for every `|kappa_j|` used to truncate the search.
4. Passing the log ellipsoid is only a necessary filter. Exact multiplication
   in `Z[X]/(X^128+1)` and the profile test are mandatory.
5. The result gives no value for the associate count and no E1 status change.
