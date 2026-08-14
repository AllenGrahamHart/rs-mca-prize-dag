# Proof

Owners agreeing with the received pair on `B` form one affine translate of
`U^2`. Choose an origin `(A_*,B_*)`. Every owner has the form

```text
(A_*,B_*)+(alpha,beta),       (alpha,beta) in U^2.  (1)
```

Consider a marked component incidence `(gamma,T)` with
`T=B union {x,y}`. Its component is in the affine-owner lane and has
`rank(ev_T)=10`. Since `rank(ev_B)=8`, the map

```text
ev_{x,y}:U -> F^2
```

has rank two. The two equations making `A_*+alpha` agree with the first
received column on `{x,y}` therefore determine `alpha` uniquely. The two
equations for `B_*+beta` determine `beta` uniquely as well. Hence the
unordered pair `{x,y}` determines at most one owner point `p` in (1).

For an owner point `p`, let `q_p` be the number of full-rank coordinate
pairs outside `B` that determine it. Coordinate-pair uniqueness gives

```text
sum_p q_p <=C(n'-9,2).                              (2)
```

Let `t_p` be the number of selected records owned by `p`. The owner point
defines one affine codeword line. Exact support-wise pair noncontainment and
fixed-owner exception disjointness give

```text
t_p <=n'-m'+1=981105.                               (3)
```

For fixed `p`, at most `t_p q_p` marked `(record,T)` incidences can use
that owner. Combining (2) and (3), without discarding extension weight,
gives

```text
W_B <=sum_p t_p q_p
    <=981105*sum_p q_p
    <=981105*C(n'-9,2).
```

This is exactly (R8W1).
