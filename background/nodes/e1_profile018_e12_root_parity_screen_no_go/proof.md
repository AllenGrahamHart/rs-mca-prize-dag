# Proof

Let

```text
D={1,2,...,11,15},
Y(X)=18+sum_(d in D)(X^d+X^(-d)).                    (1)
```

There are twelve distinct unit autocorrelation coefficients in `(1)`, so
its positive-half magnitude profile is `(E;n_1,n_2,n_3)=(12;12,0,0)`.

Modulo two, fold `(1)-18` into

```text
P(X)=sum_(d in D)(X^d+X^(128-d)).                    (2)
```

The zeroth Hasse derivative at one is zero because `(2)` has 24 terms. The
first derivative is also zero because each paired contribution is
`d+(128-d)=128`. For the second derivative, Lucas' criterion gives

```text
C(d,2)+C(128-d,2)=d mod 2.
```

Exactly seven elements of `D` are odd, hence the second Hasse derivative is
one. Thus `(2)` has exact multiplicity two at `X=1`, the parity condition
forced by local valuation one.

The residue `3` has order 256 modulo 257. Since `gcd(59,256)=1`,

```text
s=3^59=148 mod 257
```

also has order 256. Direct repeated squaring gives

```text
sum_(d in D)(s^d+s^(-d))=239=-18 mod 257,           (3)
```

so `Y(s)=0`.

It remains to check that `(1)` is not defeated by positivity. The normalized
Fejer kernel

```text
F_12(theta)
 =1+2 sum_(d=1)^11 (1-d/12)cos(d theta)
 =(1/12)|sum_(j=0)^11 exp(i j theta)|^2
```

is nonnegative. Therefore

```text
Y(exp(i theta))
 =F_12(theta)+17+(1/6)sum_(d=1)^11 d cos(d theta)
                    +2cos(15 theta)
 >=17-(1/6)sum_(d=1)^11 d-2
 =4.                                                       (4)
```

Finally, for `Omega={+/-d:d in D}`, direct grouping of ordered triples by
sum `0` and `+/-128` gives

```text
K=#_signed{a+b+c=0}-#_signed{a+b+c=+/-128}=378.     (5)
```

Equations `(1)--(5)` prove that the complete
energy/parity/root/positivity screen is nonempty. They do not construct a
singleton spectral factor or compute an official norm. QED.
