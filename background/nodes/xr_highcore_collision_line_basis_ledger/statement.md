# High-core collision-line basis ledger

- **status:** see `dag.json` (single source of truth)
- **consumer:** `xr_highcore_collision_count`

Let `H:F^D->Y` be linear, where `|D|=n` and `ker H` has minimum distance
`R+1` with `R=n-k`. Fix `y_1!=0`. Let `P` be a finite family of pairs
`(gamma,e)` on one syndrome line,

```text
H e=y_0+gamma y_1,       wt(e)<=r=R-h,
```

and let `A=aff{e:(gamma,e) in P}` have affine dimension `s>=1`.

A collision line is a distinct affine line `ell subset A` containing two
errors at distinct slopes whose common zero set has size exactly `k`. Put

```text
W_ell={x in D:e(x)=0 for every e in ell},
b_ell=#{J subset W_ell:|J|=s-1 and rank(A-A restricted to J)=s-1}.
```

Then

```text
|W_ell|=k,                    rank(A-A restricted to W_ell)=s-1,
b_ell>=1,                     sum_ell b_ell<=C(n,s-1).       (CLB1)
```

If `m_ell` is the number of nonloop coordinate rows of `A-A` inside
`W_ell`, then

```text
m_ell<=b_ell+s-2,
A subset F^U_ell for some |U_ell|=R+m_ell.                  (CLB1b)
```

Thus one basis-poor collision line puts the entire affine family in a fixed
small-excess chart.

Every line contains at most

```text
L=floor(R/h)                                                   (CLB2)
```

members of `P`. Consequently, if `P_hi(B)` consists of high-core members
admitting a witness collision line with `b_ell>=B`, then

```text
|P_hi(B)| <= L floor(C(n,s-1)/B).                             (CLB3)
```

If `b_*` is the minimum basis count over all collision lines, choosing a line
that attains it in `(CLB1b)` globally removes all but at most
`R+b_*+s-2` nonzero coordinates. Repeating the basis injection inside that
chart gives the sharper unconditional bound

```text
|P_hi| <= L floor(C(min(n,R+b_*+s-2),s-1)/b_*).              (CLB4)
```

The same statement applies to any one-per-slope selector, so `(CLB3)` is a
distinct-slope bound. It is unconditional and does not assert that every
collision line is basis-rich. Lines below the printed basis threshold remain
inside the target.

At selector rank `s=4`, the exact sufficient basis thresholds at the six XR
rows are

```text
RowC rates 1/4,1/8,1/16:  B>=4,4,7,
prize rates 1/4,1/8,1/16: B>=4,5,10.
```

Combining `(CLB4)` and `(CLB1b)` with the proved GRK chart thresholds closes
the entire rank-four branch on RowC `1/4` and prize `1/4,1/8`. The only
unresolved minimum-basis values are `b_*=2` on RowC `1/8`, `b_* in {2,...,5}`
on RowC `1/16`, and `b_*=8` on prize `1/16`. These are classifications of the
line-ledger remainder, not new assumptions, and the CLB3/CLB4 closes apply
only for line-covered members (a selected member may lie on no collision
line of the family the lemmas are applied to — catch #158). The separate
proved `xr_affine_core_cogirth_ray_bound` pays the RowC `1/8` remainder and
the prize `1/16` remainder in full-domain (covering-free) form; at RowC
`1/16` the rank-four branch is closed for line-covered members and for
hulls admitting a collision line with `b <= 47` (localized chart `R+m`,
`m <= 49`), while the line-free/line-uncovered rank-four sub-case remains
open (catch #158).
