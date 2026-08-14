# Rank-eleven relative correction-space incidence router

- **status:** PROVED
- **scope:** the non-core-compatible, many-ray residual of one `(H_C)` core
- **row family:** `(n',K',m')=(R+K',K',d+K')`, `10<=K'<=K`

Let `W` be the linear span of selected nonzero correction codewords and put
`s=dim W`. For each residual coordinate, the rich-point equation is a
hypersurface of bidegree at most `(31,1)` in
`P^1_gamma x P^s_W`.

1. If every `s+1` coordinate hypersurfaces have empty or zero-dimensional
   common intersection, then

   ```text
   N_W <= floor(31(s+1) C(n',s+1)/C(m',s+1)).
   ```

   Uniformly over every shortening, this pays every proper correction space
   through `s=11`. The worst admissible dimension-11 cap is
   `73766883380602812 < B_*`. The first adjacent method wall is
   `s=12,K'=12`, where the formula is
   `1241731241521316220 > B_*`.
2. Let `V=span(W,H_2,...,H_31)` and write its minimum support as `R+a`,
   `a>=1`. If `W` does not absorb all high coefficients `H_j`, then

   ```text
   N_W <= floor(M_a n'_fall_s/(d+a)_rise_s),
   M_a=floor(31(R+a)/(d+a)).
   ```

   This pays uniformly through `s=9`; the worst cap is
   `13013823503882165`. At `s=10,a=1` the deployed endpoint is
   `404431535289439486`, so no uniform dimension-10 payment is claimed.

Consequently an over-budget `(H_C)` residual satisfies one of these exact
alternatives:

- `s>=12`;
- `s<=11` and some `s+1` coordinate equations have a positive-dimensional
  intersection, which is an evaluation rank-flat or an exact polynomial
  clone component;
- in the subrange `s<=9`, every survivor additionally absorbs all high core
  coefficients.

This is a route theorem, not a payment of the positive-dimensional
component or the high-dimensional `s>=12` branch.

## Falsifier

A proper intersection exceeding degree `31(s+1)`; failure of the incidence
double count; a shortened proper cap above its minimum-dimension endpoint;
a restricted generalized weight below `d+a+j-1`; an identity clone larger
than `K'-a`; a nonabsorbing dimension-at-most-nine family above budget; or a
nonproper full-rank tuple yielding neither a rank-flat nor a polynomial clone
curve.
