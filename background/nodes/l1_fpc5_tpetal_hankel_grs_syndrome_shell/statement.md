# FPC5 Hankel charts are exact GRS syndrome shells

- **status:** PROVED
- **consumer:** `l1_fpc5_large_source_payment`

Fix one owner-free FPC5 Hankel chart on a core `C` of `N` distinct points.
Let its monic locator degree be `d`, its number of Hankel rows be `c`, and
put

```text
D=d+c.                                                (GS1)
```

Thus `c=h-d-1` in the unaugmented chart, while `c=ell-1` and
`D=d+ell-1` after fixing a required background set. Write
`mu=(mu_0,...,mu_(D-1))` for the chart's rational moment segment and define

```text
v_x=1/L_C'(x),
H_D=(v_x x^a)_(0<=a<D, x in C).                       (GS2)
```

For every primitive core-split locator `G` in the chart, let `w_x` be its
Cramer amplitude on `Z_C(G)` and define

```text
e_x=w_x/v_x  for x in Z_C(G),
e_x=0        otherwise.                               (GS3)
```

Then `G -> e` is a bijection between the primitive split locators in the
Hankel chart and

```text
{e in F^C: wt(e)=d and H_D e=mu}.                     (GS4)
```

If `D<N`, the kernel of `H_D` is the generalized Reed-Solomon code

```text
RS[F,C,N-D].                                          (GS5)
```

Consequently, for any received word `y` with `H_D y=mu`, `(GS4)` is exactly
the radius-`d` exact shell

```text
{y-P:P in RS[F,C,N-D], wt(y-P)=d}.                    (GS6)
```

If `D>=N`, the first `N` rows of `H_D` are invertible and the fixed Hankel
chart contains at most one primitive split locator.

For `D<N`, two distinct locator supports `S,T` in the same chart obey

```text
|S intersect T| <= 2d-D-1=d-c-1.                     (GS7)
```

In a fixed-background chart this is `|S intersect T|<=d-ell`.

The background Cauchy guards, first-owner rule, and chronology filters are
retained on the exact shell in `(GS6)`.

## Scope

This theorem identifies the local point count with an ordinary GRS exact
shell. It does not bound that shell when `D<N`, coalesce required background
sets, or pay the first-owner/profile aggregation. The injective `D>=N`
statement is per fixed chart; summing exponentially many charts is not
licensed.
