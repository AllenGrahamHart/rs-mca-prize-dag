# Claim contract - PMA three-petal mu-basis reduction

## Inputs

1. Three pairwise-coprime monic degree-`ell` full-petal locators.
2. Three distinct source labels.
3. Strict-strip degree `d=ell+s` with `0<=s<ell`.
4. For the balance conclusion, an exact pair with `deg F=d` and
   `gcd(F,W)=1`.

## Outputs

1. A linear bijection between contributor pairs and degree-`s` syzygies.
2. A reduced syzygy basis of degrees `mu` and `ell-mu` with predictable
   degree.
3. The exact filtered dimension formula.
4. The saturated balance alternative `mu=s` or `mu>=ell-s`.
5. A one-projective-point lower-half branch and a two-generator upper-half
   branch whose coefficient-degree budget is `e-1`.
6. Pairwise coprimality of the three nonzero fiber products.
7. A basis-pair determinant equal to a nonzero scalar times
   `L_1L_2L_3`.
8. On core-divisor candidates, saturation exactly when `(u,v)` is primitive.

## Consumer obligation

To use this theorem toward PMA closure, a successor must count the monic split
degree-`d` core divisors `F=uF_p+vF_q` arising from primitive coefficient
pairs, or route them once to an already-paid natural-scale owner. It must
retain the carried source, touched triple, exact-defect guard, and first-match
multiplicity.

## Nonclaims

- no growing-`e` polynomial bound;
- no source-only or contributor-level common-pencil rechart;
- no extension from full to partial petals;
- no change to the status of `petal_mixed_amplification`.

## Falsifiers

- a pairwise-coprime equal-degree locator triple whose reduced syzygy degrees
  do not sum to `ell`;
- a saturated exact-degree pair with `s<ell/2` and `mu!=s`;
- a saturated exact-degree pair with `s>=ell/2` and `mu<ell-s`;
- a failure of the stated filtered dimension or affine reconstruction.
