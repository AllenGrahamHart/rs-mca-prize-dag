# XR prize primitive rank-two shell band

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependency:** `xr_higher_rank_rank_two_shell_maxwell_router`

At a prize P-A row, let `G` be the minimal uniform Maxwell core from the
higher-rank compiler. Its block count has the exact row-only bound

```text
|G|<=L_max=floor((2R+h-1)/h).                       (PB1)
```

The three prize rows have

```text
rate       h             L_max
1/4        2^33+1          384
1/8        2^33+1          448
1/16       2^32+1          960.                     (PB2)
```

Suppose a rank-two trade is supported on every block of `G` and has shell

```text
|X|=a+d+1,       d>=2.
```

Then the shell/Maxwell router implies

```text
Delta_G>=B_(h,d)(t)
 =th+(1-d)t^2+(d-3)t+2(d+1),       t=|G|.           (PB3)
```

For `d>=2`, `(PB3)` is concave in `t`, so it is positive throughout
`4<=t<=L_max` once it is positive at both endpoints. Exact endpoint
arithmetic gives

```text
rate       D_row       B_(h,D_row)(4)   B_(h,D_row)(L_max)
1/4       22,428,333      34,135,455,048              95,708
1/8       19,217,048      34,167,567,898             166,834
1/16       4,478,600      17,135,083,194             177,042. (PB4)
```

Therefore no rank-two relation supported on the complete primitive Maxwell
core exists on any shell

```text
2<=d<=D_row,                                         (PB5)
```

at any affine kernel rank `a` for which that shell exists. The endpoint is
exact for this uniform lower bound: at `d=D_row+1`, `(PB3)` is negative at
`t=L_max` by `51,362`, `33,420`, and `743,596`, respectively.

This is a primitive full-core exclusion. It does not remove proper local
rank-two circuits, rank two beyond `(PB5)`, trade rank at least three, or the
nonuniform cells, and it does not promote the consumer.
