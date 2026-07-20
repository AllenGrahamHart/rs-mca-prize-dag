# Claim contract

- **Claim:** the Paper D v13.2 identity-prefix floor applies the prefix
  ceiling before the support multiplier, with the eight printed deployed
  values in `statement.md`.
- **Inputs:** `C=RS[F,D,K]`, `D subseteq B`, `K<=m`,
  `2(m-K)<=n-K`, `w'=m-K`,
  `w'+1<=d1<=floor((n-K+1)/2)`, `m'=K-1+d1`, and `m'+d1<=n`;
  the prefix partition and distinct support-lift contract of
  `prop:capg-census-floor`; exact deployed row parameters.
- **Output:** the discrete lower floor and its soft mean-plus-one model.
- **Falsifier:** a prefix partition with a smaller heaviest-fiber lower
  bound, a failure of the source support-lift contract, a mismatch in any
  of the eight exact ceilings, or equality with the ceiling-after-product
  mutation in one of the below-one deployed cells.
- **Nonclaims:** no safe-side upper census, max-fiber theorem, bucket
  coverage, coalescing, or adjacent-row closure.
