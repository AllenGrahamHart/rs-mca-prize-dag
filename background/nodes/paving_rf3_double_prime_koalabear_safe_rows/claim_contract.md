# Claim contract

- **object:** support-wise finite-slope MCA bad-slope numerator.
- **challenge:** the complete scalar field `Gamma=F_(p^6)`.
- **code:** `RS[F_(p^6),D,K]`, where `D` is the order-`2^21` subgroup of
  `F_p^*` and `K/n` is one of `1/2,1/4,1/8,1/16`.
- **agreement:** `A=n-r`, with the four exact `r` values in `statement.md`.
- **denominator:** `q=p^6`, not `p`, `q-1`, or the number of supports.
- **endpoint:** the proved upper packet certifies the closed Hamming radius
  `r=n-A`; it makes no assertion at radius `r+1`.
- **quantifiers:** every received pair over the stated code and every bad
  slope in the full-field challenge.
- **field transport:** none; the evaluation domain is contained in the base
  field while received words and slopes range over the degree-six field.

## RF3-double-prime interface

For a finite field `F_q`, a domain of size `n`, dimension `K`, agreement
`A=n-r`, and a nonzero interpolant `Q(X,Y,Z)`, put

```text
E = wdeg_(1,K,0)(Q),
d = deg_Y(Q),
G = wdeg_(0,1,1)(Q).
```

Assume `E<=U-1`, `char(F)>d`, `q>2Ud`, and

```text
(A-K)(2U-1) > (n-K)(2K-1).
```

For every slope `gamma` in a set `S`, assume a polynomial
`P_gamma` of degree below `K` satisfies `Q(X,P_gamma(X),gamma)=0` and
agrees with the received affine combination on a chosen `A`-set. Then

```text
|S| > (1+2Ud^2)G + (r+1)d
```

forces one chosen `A`-set on which both received coordinates are explained by
degree-below-`K` polynomials. The Paving parameter bounds
`d<D_Y`, `G<D_Z` give the displayed RF3-double-prime threshold.

## Nonclaims

- no proof of the weaker RF3 or RF3-prime threshold;
- no exact MCA numerator;
- no adjacent unsafe packet or maximal radius;
- no list or interleaved-list claim;
- no uniform all-row closure of `mca_safe`.
