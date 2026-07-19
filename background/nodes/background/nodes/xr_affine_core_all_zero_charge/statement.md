# Affine-core all-zero charge

- **status:** see `dag.json` (single source of truth)
- **consumers:** `xr_highcore_collision_count`, `xr_lowcore_spread_heart`
- **dependency:** `xr_affine_core_cogirth_ray_bound`

Use the hypotheses and notation of the affine-core cogirth ray bound. Thus
`H:F^U->Y` is linear, `ker H` has minimum distance at least `Delta`, `A` is
an affine space of dimension `s>=1` above the nonconstant syndrome line
`y_0+gamma y_1`, and

```text
N=|U|,       V=A-A,       K=V intersect ker H,       a=dim K=s-1.
```

Let `P` be a finite family of distinct pairs `(gamma,e)` with

```text
e in A,       He=y_0+gamma y_1,       wt(e)<=r.
```

Assume `Delta>r`, `N-r>=a+1`, and genericity at radius `r`: no coordinate
set of size at most `r` supports lifts of both `y_0` and `y_1`. Then

```text
|P| C(Delta-r+a-1,a) <= C(N,a)(r+1).                 (AZC)
```

This strengthens the former right side `C(N,a)(N-a)`. For an RS row,
`Delta=R+1` and `r=R-h`, so the denominator is `C(h+a,a)`.

On the six XR rows, exact arithmetic pays full-domain selector ranks

```text
4,4,4,11,11,10.
```

In particular, RowC `1/16` rank four is paid without any collision-line
coverage premise. Its exact bound is

```text
floor(C(1024,3) 958 / C(6,3)) = 8,546,941,849
                                     < 8,589,934,592 = 8*1024^3.
```

Rank five still fails this arithmetic by a factor greater than `145`, so the
theorem removes catch #158 but does not close either XR target.
