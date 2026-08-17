# Raw-clipped adjacent-support circuit coupling

- **status:** PROVED
- **correction dimension:** `10`

Assume the hypotheses and notation of
`rate_half_mca_sparse_circuit_fixed_union_adjacent_support_coupling`. Fix
`2<=d<=g-1`, put `R=K-u-g`, `N=m-u`, and let

```text
s_d     = C(m-d,11-d),
s_(d+1) = C(m-d-1,10-d).
```

Suppose independent arguments give selected-incidence caps `U_d,U_(d+1)`
on the two supports. Then their circuit-count caps are

```text
X=floor(U_d/s_d),       Y=floor(U_(d+1)/s_(d+1)).       (RCA1)
```

For `0<=i<=d-2`, define

```text
a_i=d+1-i,                    b_i=N-R-d+1+i,
A_i=C(u,i)R C(N,d-i),
L_i=floor(C(u,i)R C(N,d-1-i)/(d-i)).                 (RCA2)
```

Let nonnegative rational variables `x_i,y_i` satisfy

```text
b_i x_i+a_i y_i<=A_i,          x_i<=L_i.             (RCA3)
```

Include uncoupled capacities

```text
X_0=C(u,d-1)R+C(u,d),
Y_0=floor(C(u,d-1)RN/2)+C(u,d)R+C(u,d+1).            (RCA4)
```

The actual circuit strata embed in the rational polytope

```text
sum_i x_i+x_0<=X,     0<=x_0<=X_0,
sum_i y_i+y_0<=Y,     0<=y_0<=Y_0.                   (RCA5)
```

Consequently the selected-incidence contribution is at most the floor of

```text
max [Delta_d s_d (x_0+sum_i x_i)
    +Delta_(d+1) s_(d+1) (y_0+sum_i y_i)]            (RCA6)
```

over `(RCA3)--(RCA5)`.

The maximum is explicit. For a fixed total support-`d` count, fill `x_0`
first and then the coupled strata in increasing order of `b_i/a_i`; the
resulting support-`(d+1)` envelope is piecewise linear, so only its endpoints
and intersections with `Y` need be checked. Equivalently, fix support
`d+1`, fill its uncoupled capacity first, and traverse the coupled strata in
increasing order of `a_i/b_i`. Both orders give the same rational optimum.

This bound may replace the raw contribution of one adjacent support pair.
Bounds on support-disjoint pairs may be composed. Nothing here composes two
overlapping pair bounds.

## Falsifier

An admissible fixed union and raw cap pair whose exact circuit strata satisfy
`(RCA1)--(RCA5)` but exceed `(RCA6)`; disagreement between the two exact
allocation orders; or use of a selected-incidence cap without flooring by
its extension factor.
