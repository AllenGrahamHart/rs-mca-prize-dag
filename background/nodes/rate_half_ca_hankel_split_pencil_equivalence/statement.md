# Far-CA as a split-locator Hankel pencil

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`

Let `C=RS[F,D,k]`, let `R=n-k`, and choose nonzero dual column multipliers
`v_x` so that a syndrome has moments

```text
y_m=sum_{x in D} e(x)v_x x^m,       0<=m<R.
```

For `1<=r<=R`, form the `(R-r) x (r+1)` Hankel matrix

```text
M_r(y)=(y_{i+j})_{0<=i<R-r, 0<=j<=r}.
```

Let `D_r(D)` be the coefficient vectors of monic squarefree degree-`r`
polynomials whose roots are distinct points of `D`. Then

```text
dist(f,C)<=r
iff ker M_r(syn(f)) intersects D_r(D).                 (HS1)
```

For a received pair with syndrome vectors `y_0,y_1`, column distance to
`C^2` is at most `r` exactly when

```text
ker M_r(y_0) intersect ker M_r(y_1) intersect D_r(D)
is nonempty.                                           (HS2)
```

Consequently, if the pair is column-far, its finite CA-bad slope set is
exactly

```text
{gamma in F:
 ker(M_r(y_0)+gamma M_r(y_1)) intersects D_r(D)}.       (HS3)
```

At the first unresolved official rate-half candidate,
`R=k=2^40` and `r=B*(q)-1<=R/2`. The remaining bound
`B_ca^far(n-r)<=r+1` is therefore an exact supported-slope census for a
Hankel pencil with no common split locator.

This is the same incidence type used by the repository's SPI component
machinery. That machinery controls components and exceptional strata, but its
generic horizontal split-divisor point count remains open; no SPI point bound
is imported here.

## Coordinator shape fence (2026-08-11, round-36 bank 3)

The deployed corollary "B_ca^far(n-r) <= r+1" is PROVED for
r <= R/2-2 (the official candidate row's own shape) and MUST NOT
be transported to r > R/2: at razor-faithful shape (r = 0.8R) on a
negation-closed domain there are column-far pencils with T = 95
against r+1 = 9, field-size independent (r36_hrlow, round 36; the
mechanism is the orbit-invariant even-locator collapse, count
C(m-1, r/2-1), requiring ceil(rho/M) = 1 — dead at rho = 2^34).
