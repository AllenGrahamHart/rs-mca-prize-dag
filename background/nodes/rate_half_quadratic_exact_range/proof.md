# Proof

Use the proved quadratic MCA staircase
`mca_quadratic_prize_rows`. For a rate-half MDS code, `n=2k`, and its
hypothesis at radius `r` is

```text
(n-r)^2>=n(k+r)
iff r^2-6kr+2k^2>=0.                                  (RQ2)
```

The roots of the quadratic are `k(3-sqrt(7))` and
`k(3+sqrt(7))`. On the relevant interval `0<=r<=k-1`, the left side of
`(RQ2)` is strictly decreasing. Since `7k^2` is not a square, its largest
admissible integer radius is

```text
r_Q=floor(k(3-sqrt(7)))
   =3k-ceil(sqrt(7k^2))
   =3k-floor(sqrt(7k^2))-1
   =389,500,552,608.                                  (RQ3)
```

Now put `B=floor(q/2^128)` and suppose `1<=B<=B_Q=r_Q+1`. At radius
`r=B-1`, `(RQ2)` holds, so the quadratic staircase gives

```text
B_mca(n-B+1)=B.                                       (RQ4)
```

At the immediately larger radius `r=B`, the universal MDS
coordinate-tangent construction supplies at least `B+1` bad slopes. Hence

```text
B_mca(n-B)>=B+1>B,                                    (RQ5)
```

which proves the adjacent certificate. Finally,
`floor(q/2^128)<=B_Q` is equivalent to
`q<(B_Q+1)2^128`. QED.

## Post-cutoff bracket

Let `1<=B<=k-1` and set `r_safe=min(B-1,r_Q)`. The quadratic hypothesis
holds at `r_safe`, so the same theorem gives

```text
B_mca(n-r_safe)=r_safe+1<=B.
```

The unconditional tangent construction is legal at radius `B<=n-k-1` and
gives `B_mca(n-B)>=B+1`. Monotonicity places the adjacent safe agreement
between `n-B+1` and `n-r_safe`, proving `(RQ2)--(RQ3)`.

If `B<=2^39+1`, the radius of the lower candidate `a_0=n-B+1` is
`B-1<=2^39=(n-k)/2`. The proved sparse half-distance theorem gives
`S_sparse(a_0)<=B-1`. By the exact MCA sparsification identity,

```text
B_mca(a_0)=max(B_ca^far(a_0),S_sparse(a_0)),
```

so `B_mca(a_0)<=B` is equivalent to `B_ca^far(a_0)<=B`. Unsafety at
`a_0-1=n-B` is already supplied by the tangent construction. This proves
`(RQ4)`.
