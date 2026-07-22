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

There is also a general polynomial-abc dichotomy. Translate `P` by the
constant that depresses `G`, call the resulting monic degree-`p` polynomial
`R`, and put `nu=ord_0(R)`. Let `e_h` be the least positive integer satisfying

```text
h e_h+1=0 mod p.
```

Polynomial Mason--Stothers, retaining its characteristic-`p` exception,
proves that every degree-`h` record satisfies

```text
nu<=u-p       or       u e_h<=p.                         (MSC5)
```

When `h<m`, one has `u>p`, so the second arm is impossible and

```text
nu<=u-p.                                                 (MSC6)
```

In particular, at `h=m-1` this is `nu<=s`.

At maximal capacity `h=m`, one has `u=s<p`, so the first arm is impossible.
Writing `e_0=e_m`, every maximal-capacity record must satisfy

```text
s e_0<=p.                                                (MSC7)
```

For `m=2`, `(MSC7)` is `s(p-1)/2<=p`, hence `s<=2`; it
independently recovers the necessary half of the exact antipodal
classification.

The exact checkpoint atlas has `s e_0>p` on all 16 rows with `m>=3`.
Consequently their maximal split-value strata are empty at every depth. In
particular, the four `m=3` rows retain only `h=2`; the general live range is

```text
2<=h<=m-1.                                               (MSC8)
```

For `h<m`, `(MSC4)` is an exact compression but its exponent `ell_h` can
still grow with `p`; it is not a polynomial payment in general. The theorem
does not bound those growing-exponent lower-value strata, any tail width above
`p`, or the complete L1 fiber.
