# Proof

Suppose `T,T'` are two minimal quotient supports of size `h`, with nonzero
coefficients, and choose their source representations after adding columns
from `R_A`. Subtracting the two representations gives a moment-column
relation supported on

```text
R_A union T union T'.                                  (1)
```

There are at most

```text
(r-1)+2h=2e+2h<=4e+2<2r+1                             (2)
```

columns under `(QMU2)`. Every set of at most `2r+1` distinct residual-domain
moment columns is Vandermonde-independent. The relation is therefore zero.
A point in `T\T'` would retain its nonzero minimal coefficient, so no such
point exists; symmetrically `T=T'`. Independence also gives uniqueness of
the quotient coefficients and proves the first claim.

For an ordinary slope, reduce its clean source representation modulo `W_A`
and divide by the nonzero slope. This represents `[h_1]` on `H_z`, so
minimality gives `|H_z|>=h`.

Assume equality. The first part gives `H_z=T`. Compare the clean
representation on `G_z` with the canonical representation

```text
h_0+zh_1
 =sum_(a in R_A)(beta_a+z alpha_a)c(a)
  +z sum_(t in T)omega_t c(t).                         (3)
```

Their union lies in `R_A union T`, of size

```text
(r-1)+h<=3e+1<2r+1.                                   (4)
```

Vandermonde independence makes the representations identical. Every point
of `T` occurs, while exactly `a_z=r-h` points of `R_A` occur. Formula `(3)`
therefore has exactly `h-1` cancelled exceptional coefficients. This proves
`(QMU4)` and says precisely that the fiber is internal.

Conversely, the definition and proved structure of an internal fiber give
`j_z=h-1` and

```text
G_z=(R_A minus the cancellation set) union T,
```

so `H_z=T` and `|H_z|=h`.

Finally, each affine coefficient `beta_a+z alpha_a` has at most one zero
because `beta_a!=0`. Thus cancellation sets belonging to distinct internal
slopes are disjoint. Each has size `h-1` inside the `2e`-point set `R_A`,
which proves `(QMU5)`. The numerical split `(QMU6)` combines `(QMU2)` with
the existing gap and ceiling. QED.
