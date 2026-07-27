# Proof

Mattarei's published Corollary concerns the projective Fermat curve

```text
a X^d+b Y^d=Z^d,
```

where `a,b` are arbitrary nonzero elements of `F_p`. If `d>=4`,
`d|(p-1)`, and `d^4>=4(p-1)`, its number `N_d(a,b,p)` of projective
`F_p`-points satisfies

```text
N_d(a,b,p)<3*2^(-2/3)d^(4/3)(p-1)^(2/3).           (1)
```

We transport `(1)` to affine coset intersections. Write

```text
L_1(x)=a_1 x+b_1,       L_2(x)=a_2 x+b_2.
```

Both leading coefficients are nonzero. Because the forms are
nonproportional, after setting `u=L_1(x)` their relation has the form

```text
L_2(x)=alpha u+beta,    alpha,beta in F_p^*.       (2)
```

The affine change `x -> u` is bijective. Hence the count in `(MAC1)` is
the number of pairs `(u,v) in K^2` satisfying

```text
v-alpha u=beta.                                     (3)
```

Every element of `K` has exactly `d` nonzero `d`th roots. Therefore every
pair in `(3)` has exactly `d^2` lifts `(X,Y) in (F_p^*)^2` on

```text
(-alpha/beta)X^d+(1/beta)Y^d=1.                    (4)
```

These lifts are among the projective points counted by `(1)`. Consequently,

```text
d^2 #{(u,v) in K^2:v-alpha u=beta}
 <3*2^(-2/3)d^(4/3)(p-1)^(2/3).
```

Since `p-1=dm`, division by `d^2` gives `(MAC1)` exactly. Notice that the
arbitrary coefficients in `(4)`, not a same-coset specialization, are what
permit `alpha notin K`.

It remains to check the official rows. There `n=2^s`, `13<=s<=41`,
`p>=n^2`, and `m` is `n` or `3n`. Since `p-1=dm` and `m<=3n`,

```text
d=(p-1)/m>(n^2-1)/(3n)>n/4.
```

Also `n^2>=2^26>768`, so

```text
d^3>n^3/64>=12n>=4m.
```

In particular `d>=4`, and `d^4=d(p-1)>=4(p-1)`. Thus all hypotheses of
Mattarei's Corollary hold for both official subgroup orders.

There is no conflict with the proved `2^(5/3)` NSB2 floor. NSB2 fences the
one-auxiliary-polynomial Heath-Brown--Konyagin/Stepanov ansatz used by the
in-house theorem. Mattarei derives `(1)` by optimizing the distinct
Garcia--Voloch family of algebraic-geometric Fermat-curve bounds. His Remark 3
explicitly records that attempts to optimize the former method did not attain
a constant below `2^(5/3)`, while the Corollary uses the latter method.

