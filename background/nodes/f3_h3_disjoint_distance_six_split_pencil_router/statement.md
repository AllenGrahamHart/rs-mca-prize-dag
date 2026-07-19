# H3 disjoint distance-six split-pencil router

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half`
- **dependencies:** `f3_h3_low_distance_quotient_incidence_router`,
  `f3_h3_distance_six_support_overlap_payment`

Fix an official row, write `H` for its order-`n` subgroup, and fix a
nonzero target `t`. For `r in H` put

```text
Q_(t,r)(X)=X^2-(1+r-t)X+r
            =X^2+(t-1)X+r(1-X).                    (DSP1)
```

Let `S_t` be the set of parameters `r` for which `Q_(t,r)` splits as
`(X-x)(X-y)` with `x,y in H\{1}`. Then

```text
r <--> {x,y}                                        (DSP2)
```

is a bijection from `S_t` to the unordered representations
`t=(1-x)(1-y)`. If

```text
diag(t)=#{a in (1-H)\{0}:a^2=t},
```

then

```text
P(t)=2|S_t|-diag(t).                                (DSP3)
```

Let `G_t` retain the generic members of `S_t`, namely those whose signed
half-basis vector `+xy-x-y` has three distinct unit atoms. For `r in G_t`
write `Sigma_t(r)` for the underlying three-coordinate support. Then the
disjoint distance-six edge count is exactly

```text
N_6^disj(t)=#{ {r,s} subset G_t :
                Sigma_t(r) intersect Sigma_t(s)=empty }.       (DSP4)
```

The quotient weight is the affine subgroup-line fiber

```text
Z_t={z in H\{1}: 1-t(1-z) in H\{1}},
R(t)=|Z_t|.                                         (DSP5)
```

Thus the remaining C36' moment is a correlation between disjoint pairs of
split members of the quadratic pencil `(DSP1)` and the line fiber `(DSP5)`.
The split-pair form is explicit. For distinct `r,s in S_t`,

```text
(X-r)Q_(t,s)(X)-(X-s)Q_(t,r)(X)=t(s-r)X.            (DSP6)
```

Both cubics split over `H`; on the locus in `(DSP4)` their two three-root
supports are disjoint. They agree in the leading, quadratic, and constant
coefficients and differ only in the linear coefficient. This is a
linear-shift split-pencil pair, not the constant-shift top stratum.

Finally let `J_25^0,J_25^A` count the corresponding raw ordered tuples
`(x,y,u,v,z,w)`, before canonical pair and edge orientation, on the
antipodal-free and antipodal target classes with `P(t)>=25`. Then

```text
J_25^0=8D_6,25^0,       J_25^A=8D_6,25^A.           (DSP7)
```

Consequently the preferred direct-incidence target is equivalently the
integer inequality

```text
10J_25^0+17J_25^A <=892n^2.                         (DSP8)
```

This theorem is an exact router. It supplies no bound for the split-pencil /
line-fiber correlation in `(DSP8)`.
