# Proof

## 1. Saturation of the reduced determinant

For a top pair put `c=deg C_ij`. The planted part of its common residual
support has size `c`, so the external part has size `t-c`. Since every
`H_i` contains `L_S`, exact support gives

```text
deg K_ij=sigma+t-c.                                  (1)
```

The canonical source factorization proves that `K_ij` divides

```text
D_ij=A_i^G b_j-A_j^G b_i.                           (2)
```

Here

```text
deg A_i^G=q_j-c,       deg A_j^G=q_i-c,
q_i=deg Q_i.
```

Since `deg b_i<=g-q_i-w-1`, both terms in `(2)` have degree at most

```text
g-w-c-1=d-c-1=sigma+t-c.                            (3)
```

The determinant is nonzero by the source normal form. Equations `(1)--(3)`
therefore force equality of degrees and `D_ij=lambda K_ij` for a nonzero
scalar `lambda`.

Because every `Q_i` and every `A_i^G` is monic, the coefficient of degree
`d-c-1` in `(2)` is

```text
gamma_j-gamma_i.
```

Thus `lambda=gamma_j-gamma_i`, proving `(HS1)` and showing that the two head
values differ. The source identities also give

```text
D_ij=L_S T_ij,       a_i-a_j=-C_ij T_ij.
```

Substituting `(HS1)` proves `(HS2)`.

## 2. Head-fiber cap

Two members with the same `gamma` cannot be a top pair. Their exact combined
agreement supports therefore have size `m` and pairwise intersection at
most `t-1=4979` in an `N`-point universe.

For `M_gamma` such supports, the constant-weight Cauchy inequality gives

```text
M_gamma <= floor(N(m-(t-1))/(m^2-N(t-1))).           (4)
```

The exact deployed values are

```text
m^2-N(t-1)=154881,
N(m-t+1)=71061366093
             =458812*154881+104721.
```

This proves `(HS3)`. Since `4*458812<M0<=5*458812`, at least five head
values occur. The zero-head fiber has at most `458812` members, proving
`(HS4)`. Finally, `Q_i` is monic of degree `q_i`, so `gamma_i!=0` is
equivalent to

```text
deg b_i=g-q_i-w-1=deg G_i-w-1,
deg f_i=d-1.
```

## 3. A nonzero-head dense anchor

The dense-top predecessor gives more than `C(M,2)/10` top edges. Every top
edge has at least one nonzero-head endpoint. Hence the sum of top degrees
over nonzero-head vertices is larger than `C(M,2)/10`. There are at most
`M` such vertices, so one has degree strictly larger than

```text
(M-1)/20 >=107896.4.
```

Its integer degree is at least `107897`.

The fixed-direction and fixed-core bounds from the predecessors now give

```text
ceil(107897/14)=7707 directions,
ceil(107897*4980/240)=2238863 degree-4979 cores.
```

For a fixed degree-`4979` core `R` and fixed neighbor head `gamma_j`, the
scalar in `(HS2)` is fixed. Writing the direction as `R(X-alpha)` puts all
such neighbors in one affine codeword line. The affine-span line cap is
`15`. Double counting neighbor/core incidences therefore gives

```text
107897*4980/15=35821804
```

distinct `(R,gamma_j)` pairs. QED.
