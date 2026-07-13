# Affine-core cogirth ray bound

- **status:** see `dag.json` (single source of truth)
- **consumers:** `xr_highcore_collision_count`, `xr_lowcore_spread_heart`

Let `H:F^U->Y` be linear and let `C=ker H` have minimum distance at least
`Delta`. Let `A subset F^U` be an affine space of dimension `s>=1` whose
syndrome image is the nonconstant line `y_0+gamma y_1`. Put

```text
V=A-A,        K=V intersect C,        a=dim K=s-1.
```

Assume `Delta>r` and genericity at radius `r`: no coordinate set of size at
most `r` supports both a lift of `y_0` and a lift of `y_1`. Let `P` be any finite set
of distinct pairs `(gamma,e)` with `e in A`, `He=y_0+gamma y_1`, and
`wt(e)<=r`. If

```text
|U|-r>=a+1,
```

then

```text
|P| C(Delta-r+a-1,a) <= C(|U|,a)(|U|-a).                (ACG)
```

For an RS row, `Delta=R+1`, `r=R-h`, and therefore the denominator is
`C(h+a,a)`. The theorem counts complete pairs; applying it to a one-per-slope
selector gives the same distinct-slope bound.

On the full `n`-coordinate chart, exact arithmetic pays selector rank four on
both RowC rates `1/4,1/8` and pays substantially higher ranks on the prize
rows. Combined with the collision-line low-basis charts, it closes the rank-four
high-core branch unconditionally on five rows; at RowC `1/16` the combined
close applies for line-covered members (CLB3/CLB4 coverage is not automatic
— catch #158), and the line-free/line-uncovered rank-four sub-case remains
open.
