# Claim contract

## Imported facts

From `e1_prize_n256_s18_profile_36_cofactor_windows`:

- both cofactors `1024` and `1028` have positive even variance;
- `V=2` is impossible;
- their residual logarithmic windows end at `V=34`;
- a collision norm is `R=mp` with `p>=B_P 2^128`.

## New theorem

The exact mean and variance of the 64 conjugate squares imply a sharp
two-level product envelope. That envelope is below `1024 B_P 2^128` for
every even `14<=V<=34`. Hence only `V in {4,6,8,10,12}` remains for either
cofactor.

## Exclusions

1. This node does not exclude either cofactor completely.
2. It does not assert that the real two-level extrema are realizable by a
   profile polynomial.
3. It does not exclude `V=12`; the verifier certifies the opposite for this
   envelope method.
4. It does not change any of the other ten cofactor windows.
5. It contributes zero pair count only after a successor excludes the five
   residual variance values.
