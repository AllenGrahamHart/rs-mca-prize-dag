# Claim contract - L1 full-locator Pade section

## Inputs

- normalized `U`, shell size `a`, and `h=deg U`;
- `w=a-k`, `e=h-a`, `d=e+w`;
- monic split degree-`a` locators and the complement exactness guard.

## Outputs

- one `w`-equation reciprocal-series section `V_(U,a)` for every `e>=0`;
- exact recovery of the degree-`e` cofactor;
- exact-shell equality with split points of the section satisfying the gcd
  guard;
- graph-cylinder cardinality `q^k` when `e<k`;
- a proved representation, without a cardinality claim, when `e>=k`.

## Consumer rule

For every shell degree, count split locators in `V_(U,a)` after first-match
quotient payments.  Use the prefix graph optimization below `e=k`; at and
above the cap, retain all reciprocal coefficients through `e+w`.  Never
replace the capped range by the raw `q^e` cofactor union. Apply
`l1_pade_remainder_jacobian_tangent_dichotomy` and first-match the tangent gcd
before any primitive smooth-section argument.

## Nonclaims

The `w` equations are not claimed independent at `e>=k`.  No codimension,
section cardinality, split-divisor transversality, finite-row constant, or
quotient payment is proved there.  The formal density `q^(-w)` is a target,
not a conclusion.

## Falsifier

An exact shell locator failing `(FA1)`, a section locator whose reconstructed
difference has degree at least `k`, a mismatch of the gcd guard and exactness,
failure of `(FA4)` below the cap, or any hidden use of `(FA4)` at `e>=k`.
