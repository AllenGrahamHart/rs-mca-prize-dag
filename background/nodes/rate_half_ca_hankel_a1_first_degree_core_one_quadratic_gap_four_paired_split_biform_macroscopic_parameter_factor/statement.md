# `A=1` quadratic paired split-biform macroscopic parameter factor

- **status:** PROVED
- **closure:** factorwise row saturation and a macroscopic irreducible component
- **consumer:** `rate_half_band_crossing_location`

Retain the extremal paired split biform. Put

```text
M=e-2,       N=p-3,       R=3p-3+d_A,
T=3e,       2p=3e-1,       d_A in {0,1}.           (PMF1)
```

Thus `G(t,X)` has bidegree exactly `(M,N)`, and at every one of the `R`
classified domain rows its parameter polynomial has exactly `M` distinct
roots among the `T` off-line supported slopes.

Factor over `F(X)` and choose primitive polynomial representatives:

```text
G(t,X)=c(X) product_(j=1)^s Q_j(t,X),
m_j=deg_t Q_j>0,       n_j=deg_X Q_j.              (PMF2)
```

Then every factor obeys

```text
T n_j>=R m_j.                                      (PMF3)
```

More strongly, on every classified domain row, `Q_j(-,x)` has exact degree
`m_j` and splits into `m_j` distinct roots among the supported slopes; the
root sets of different factors are disjoint there.

On every clean parameter fiber from the dual-MDS reduction,
`Q_j(delta,-)` likewise has exact degree `n_j` and splits into distinct
roots over `U_0`. There are at least

```text
e+6+d_A                                                (PMF3a)
```

such fibers. Thus every irreducible factor, including the macroscopic one
below, inherits the proved two-directional splitting.

At least one irreducible factor has parameter degree

```text
d_A=0:  m_j>=ceil(e/3),
d_A=1:  m_j>=ceil(3e/7).                            (PMF4)
```

On the official row `e=183251937963`, these lower bounds are respectively

```text
61083979321,       78536544842.                     (PMF5)
```

In particular, the paired biform cannot be a product of bounded-degree
parameter factors. Any surviving reducible packet contains a macroscopic
factor that itself splits completely in both proved directions.

## Scope

The theorem does not prove that the macroscopic factor is incompatible
with the Hankel source or the multiplicative domain. It does not assert
that the factor is unique, and it makes no analogous claim for the first
strict profile or the two-simple heavy-row factorization.
