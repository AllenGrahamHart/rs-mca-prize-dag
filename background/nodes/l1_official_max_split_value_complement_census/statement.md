# L1 official maximal split-value complement census

- **status:** PROVED
- **role:** pay the maximal-value part of the surviving first-checkpoint
  split-pencil census
- **consumer:** `l1_mixed_petal_amplification`

Let `H` be an official multiplicative coset of size `n` in characteristic
`p<n`, put

```text
m=floor(n/p),       s=n-mp,       1<=s<p,
```

and normalize

```text
P(Z)=Z^p+Q(Z),       Q(0)=0,       deg Q<p.
```

More generally, suppose exactly `h` values have complete `p`-point fibers,
where `2<=h<=m`, and put `u=n-hp`. If `G` is their monic value polynomial,
then

```text
G(P(Z)) C(Z)=Z^n-alpha,       deg C=u.                  (MSC1)
```

where `C` is the locator of the unused domain points.

Write `r=deg Q` and `j=p-r`. Then `Q` is nonzero and

```text
1<=j<=u,
C(Z)=Z^u+0 Z^(u-1)+...+0 Z^(u-j+1)+c_(u-j)Z^(u-j)+...,
c_(u-j)=-h lc(Q).                                      (MSC2)
```

At first-checkpoint depth `p<=d<=2p-2`, the split-pencil reduction gives
`r<=2p-d-1`. Therefore every realized complement has its top `d-p`
nonleading coefficients zero. Put

```text
ell_h=u-d+p.                                             (MSC3)
```

If `ell_h<=0`, no degree-`h` record exists. If `ell_h>=1`, any `ell_h`
roots of `C` determine all of `C` by an invertible Vandermonde system.
Moreover `C` determines the normalized `P`, hence the complete value set,
uniquely. Consequently

```text
# degree-h normalized Q records
    <=floor(binom(n,ell_h)/binom(u,ell_h)),
# associated unordered fiber pairs
    <=binom(h,2) floor(binom(n,ell_h)/binom(u,ell_h)).    (MSC4)
```

At maximal capacity `h=m`, one has `u=s` and `ell_h=ell=s-d+p`.
The official checkpoint atlas has exactly nine `m>=3` rows with `s<=16`.
On all nine, `(MSC4)` is at most `binom(16,2)n^16`, uniformly over the
whole first-checkpoint band. Thus their maximal-capacity branch is already
polynomially paid. On every row, the final `B` possible depth layers of this
branch cost at most `binom(m,2)n^B`.

There is a further exact endpoint exclusion. At `d=p+s-1`, `(MSC2)` forces
`C=Z^s-b`. Divisibility by `Z^n-alpha` forces `s|m`. The seven broad official
rows have `s>m`, so are impossible. The other nine have `s=m` and
`p=-1 mod m`. A terminal decomposition with `s=m` would instead force
`p=1 mod m`. Hence

```text
all 16 official m>=3 rows have no maximal-capacity record
at d=p+s-1, and none at d>=p+s.                          (MSC5)
```

For `h<m`, `(MSC4)` is an exact compression but its exponent `ell_h` can
still grow with `p`; it is not a polynomial payment in general. The theorem
does not bound those growing-exponent lower-value strata, any tail width above
`p`, or the complete L1 fiber.
