# Claim contract

## Consumed theorems

- `l1_exact_shell_balanced_shifted_lattice_reduction`: exact shell members
  have unique degree-capped coordinates in one balanced interpolation-module
  basis, with `d_1+d_2=omega+w+1`.
- `l1_split_pencil_content_exact_shell_descent`: exact shell coordinates are
  primitive, `gcd(A,B)=1`.

## New theorem

For one fixed exact anchor, the coefficient determinant is an affine
coordinate system on the complete balanced coefficient body. It recovers
the exact common complement by gcd. At fixed common complement and
common-agreement deficiency `j`, all exact neighbors lie in a split linear
system of projective dimension at most `j+1` and satisfy `(DA10)`.

## Guards

1. The shell is in the balanced band `2m<=n+k-1`; equivalently `s>=1`.
2. The coefficient pair used as anchor is exact and therefore primitive.
3. `(DA10)` is per fixed `D`; summing over `D` is explicitly retained in
   `(DA12)` and may be exponential.
4. The theorem counts exact list codewords, not MCA slopes or saturated
   line-rays. Any MCA use needs its own slope-to-pencil injection.
5. `j=0` is the one-parameter pencil stratum. No claim is made that all
   `j>=1` systems decompose into a paid number of pencils.
6. The root-matroid bound uses full splitting and exact degree `h`; it is not
   a bound for arbitrary polynomial subspaces or partially split members.
7. No row reserve inequality or critical-status promotion follows.
