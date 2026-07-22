# L1 m=4, h=3, nu=0, h=0 universal packet exclusion

- **status:** PROVED
- **dependency:** `l1_m4_h3_nu0_h0_projective_quarter_certificate`
- **consumer:** `l1_mixed_petal_amplification`

Assume the nonzero-`b`, constant-eliminant endpoint and put `r=R(0)`. The
universal projective packet

```text
a=6r^2,       b=20r^3                                  (UPE1)
```

is impossible on every official characteristic. More precisely, its Euler
identity would force

```text
F=X^n(R-4r)/(D(R-r)^4) in F(X)^p.                     (UPE2)
```

The valuation of `F` at zero forces `ord_0(R-r)=1`. At every nonzero root of
`R-r`, squarefreeness of `D` and `(UPE2)` force that root to lie in `D` and
to have multiplicity

```text
e=(3p-1)/4.                                            (UPE3)
```

But the remaining degree `p-1` of `R-r` is strictly between `e` and `2e`, a
contradiction. Consequently

```text
p=8191,131071,524287:       no nu=0,b!=0,deg H=0 record;
p=2147483647:               only the exceptional projective packet
                             (844833809,2002167159) remains possible.        (UPE4)
```

This does not exclude the exceptional packet, the cubic-eliminant endpoint,
zero `b`, positive valuation, wider `m`, or close L1.
