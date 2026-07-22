# Proof

Because `N` is divisible by eight, `(RAC1)` gives `p=7 mod 8`. Quadratic
reciprocity therefore gives

```text
(-2|p)=-1.                                             (1)
```

The two roots of `X^2+2` lie in `F_(p^2)\F_p`, so the nontrivial Frobenius
acts by

```text
a^p=-a.                                                (2)
```

The torsion-field router sends every member of `mu_N` to its inverse. Apply
Frobenius to `u=A_a(y)` in `(RAC2)`. Directly,

```text
u^p=A_(-a)(y^(-1))
   =(2-a)y^(-1)+(a-1)
   =v/y.                                               (3)
```

But `u in mu_N` also gives `u^p=u^(-1)`. Hence

```text
uv=y.                                                  (4)
```

Using `a^2=-2`, expansion factors `(4)` as

```text
uv-y=(a-4)y^2+8y-(a+4)
    =(y-1)((a-4)y+(a+4)).                              (5)
```

The affine compiler has `y!=1`. Official characteristic is greater than
three, so `(5)` has the unique remaining solution

```text
y=-(a+4)/(a-4)=(7+4a)/9.                              (6)
```

Substitution into the two affine forms gives

```text
u=(2a-1)/3=:r,       v=(1-2a)/3=-r.                  (7)
```

Finally

```text
r^2=(-7-4a)/9,
```

so `y=-r^2`. This proves `(RAC3)`. Since `u=r` belongs to `mu_N`, `(RAC4)`
is necessary. Conversely, inside the affine normal form, `r^N=1` puts
`r,-r,-r^2` in `mu_N` because `N` is even, so it is also equivalent to the
three membership conditions in `(RAC2)`.

The norm of `r` from `F_(p^2)` to `F_p` is one, and

```text
r+r^(-1)=-2/3.                                        (8)
```

Induction in `(RAC5)` therefore gives

```text
R_j=r^(2^j)+r^(-2^j).                                 (9)
```

At `j=40`,

```text
R_40-2=(r^N-1)^2/r^N.                                (10)
```

Thus `(RAC4)` and `(RAC6)` are equivalent.

It remains only to count the official progression. The budget interval for
`q=p^2` is exactly the first inequality in `(RAC7)`, while the reciprocal
field chamber is `p=-1 mod 2^40`. Integer square roots give

```text
ceil(sqrt(3*2^128))=31950697969885030204,
p<2^65,
29058991<=k<=33554432.                                (11)
```

The inclusive interval contains
`33554432-29058991+1=4,495,442` values.

The preregistered Modal launcher partitions that interval into sixteen
disjoint contiguous shards. Every shard records its endpoints, processed
count, factor-three count, rolling digest, hits, and elapsed time. The banked
result has exact coverage, all shards complete, and no hit even before
primality filtering. Its independent checker reconstructs the interval and
partition, pins the launcher hash, recomputes every no-hit digest and
factor-three count, samples the recurrence in each shard, and verifies the
positive control `N=32,p=31`.

An official reciprocal characteristic is prime, lies in `(RAC7)`, and is not
three. It would have to satisfy `(RAC6)`, contrary to the complete no-hit
certificate `(RAC8)`. Hence the covered shard is empty. QED.
