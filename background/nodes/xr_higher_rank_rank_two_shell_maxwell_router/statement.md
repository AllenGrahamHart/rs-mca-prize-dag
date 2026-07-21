# XR higher-rank rank-two shell and Maxwell router

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_higher_rank_uniform_split_pencil_reduction`,
  `xr_higher_rank_collapsed_face_exclusion`

Use the uniform high-core split-pencil setup at affine kernel rank `a`. Let a
rank-two trade have `t` active rows and active-coordinate union

```text
rho=|X|=a+d+1,       1<=d<=a-1.                     (SR1)
```

For row `i`, put `Z_i=X\supp(lambda_i)` and `z_i=|Z_i|`. Then

```text
1<=z_i<=d,
Z_i are pairwise disjoint,
z_i+z_j>=d+1                    for i!=j.             (SR2)
```

Consequently the total zero mass satisfies

```text
sum_i z_i >= M_d(t),                                  (SR3)

M_d(t) = t(d+1)/2                       if d is odd,
       = t(d/2+1)-1                     if d is even.
```

Since the zero sets are disjoint in `X`, `M_d(t)<=a+d+1`. In particular,

```text
t <= floor(2(a+d+1)/(d+1))             if d is odd,
t <= floor(2(a+d+2)/(d+2))             if d is even.  (SR4)
```

The polynomial-pencil map has degree between `max_i z_i` and `d`. Equality
in `(SR3)` forces all `z_i=(d+1)/2` for odd `d`; for even `d`, it forces one
`z_i=d/2` and all other `z_j=d/2+1`.

There is also an exact primitive-core test. Let `A_i` be the selected blocks
of the active rows, each of size `a+h`, let `v_J=|union_i A_i|`, put
`Z=sum_i z_i`, and define the Maxwell deficit

```text
Delta_J=2v_J-2a-ht.
```

Then

```text
Delta_J >= 2(d+1)+t(h-2d-2)+(d+1)t(t-1)-2(t-2)Z
        >= D_min(a,h,d,t),                            (SR5)

D_min=2(d+1)+t(h-2d-2)+(d+1)t(t-1)
      -2(t-2) min(td,a+d+1).
```

If `D_min>0`, the active rows cannot be all blocks of their minimal Maxwell
core, because a full core has `Delta_J=-e<=0`.

Useful exact consequences are:

1. On the first residual shell `d=2`,
   `Delta_J>=6+t(h-t-1)`. Full-core rank two is excluded at the two RowC
   `h=5` rows for `a<=7`, at the RowC `h=3` row for `a=4`, and at either
   prize `h=2^33+1` row for `a<=2^34-3`; at the prize `h=2^32+1` row it is
   excluded for `a<=2^33-3`.
2. On the second residual shell `d=3`,
   `Delta_J>=8+t(h-2t)`. At the prize rows this excludes full-core rank two
   for `a<=2^33-3,2^33-3,2^32-3`, respectively.
3. If `a` is odd, the top shell `d=a-1` is empty. If `a` is even, that shell
   can only have `t=4`, four zero fibers of size `a/2`, and no coordinate
   outside those fibers.

This theorem removes rank-two primitive full-core anomalies on the printed
shell/rank ranges. Proper local rank-two circuits, their ownership and
aggregate count, higher shells outside the positive-deficit region, trade
rank at least three, and nonuniform cells remain open.
