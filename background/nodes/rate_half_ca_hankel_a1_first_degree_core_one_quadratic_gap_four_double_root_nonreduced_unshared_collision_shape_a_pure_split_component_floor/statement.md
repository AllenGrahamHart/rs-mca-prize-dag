# `A=1` collision shape-A pure-split component floor

- **status:** PROVED
- **closure:** an off-diagonal component carries at least `n+14` subgroup points
- **consumer:** `rate_half_band_crossing_location`

Retain shape A and put

```text
m=e-2,       n=(3e-7)/2,       R=(9e-7)/2,
Gamma=the 3e off-line slopes.                        (PSC1)
```

At least `e+7` slopes `delta in Gamma` are pure split fibers:

```text
a_delta=r_delta=q_delta=0,
G(delta,X)=zeta_delta A_delta(X),
|Z(A_delta)|=n,       Z(A_delta) subset U_0.        (PSC2)
```

The shape-A biform is absolutely irreducible. Its divided off-diagonal
resultant

```text
K_G(X,Y)=Res_t(G(t,X),G(t,Y))/(X-Y)^m              (PSC3)
```

is nonzero and has bidegree at most

```text
(m(n-1),m(n-1)).                                   (PSC4)
```

On the official row, its reduced off-diagonal locus contains at least

```text
P_A=ceil((e+7)n(n-1)/(e-2))
   =75557863727701029814224                         (PSC5)
```

distinct points of `U_0^2`. The connected degree-`n` cover
`G=0 -> P^1_t` has at most `n-1` geometric off-diagonal fiber-product
components. Consequently at least one component image contains at least

```text
ceil(P_A/(n-1))=ceil((e+7)n/(e-2))=n+14
              =274877906955                        (PSC6)
```

distinct official subgroup points.

## Scope

This is a component floor, not a torus conclusion. The resultant degree in
`(PSC4)` is macroscopic, so the low-degree Corvaja--Zannier comparisons that
excluded the ordinary companions do not close shape A. A next theorem must
bound one component's subdegree or couple these coincidences to the source.
