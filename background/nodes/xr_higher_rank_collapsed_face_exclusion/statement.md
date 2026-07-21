# XR higher-rank collapsed-face exclusion

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependency:** `xr_higher_rank_minimal_face_syzygy_dichotomy`

Use the uniform high-core split-pencil setup at selector rank `s=a+1`. After
puncturing the common zero set `P_0`, where

```text
|P_0|=k-a,
```

the kernel is a fixed-coordinate scaling of `GRS_a`, selected agreement
blocks have pairwise intersection at most `a`, and a minimum-union rank-two
trade has

```text
|X|=a+2,       S_i=X\{x_i},       |S_i|=a+1.        (CFE1)
```

The collapsed branch of the preceding dichotomy cannot occur. Indeed, if
both facet divided-difference forms vanished identically, the normalized
received word `U` and direction `q` would have interpolants

```text
p_U,p_q in F[T]_<a
```

on all of `X`. For every active slope `gamma_i`, let
`w_i in F[T]_<a` be its selected kernel codeword. Since `S_i` lies in its
agreement block,

```text
w_i=p_U-gamma_i p_q       on S_i.                    (CFE2)
```

The two sides have degree less than `a` and agree at `a+1` points, so they
are the same polynomial. Thus the selected error at every active slope
vanishes on all of `X`, not merely on its facet. Any two active selected
errors then have the common zero set

```text
P_0 union X,       |P_0 union X|=k+2,                (CFE3)
```

contradicting the proved post-strip cap `k`.

Consequently every minimum-union rank-two trade is in the regular
face-syzygy branch. After quotienting those known Plucker syzygies, every
surviving rank-two trade has active union at least

```text
a+3.                                                  (CFE4)
```

This removes the former near-tangent exception at every official P-A row. It
does not pay larger-union rank-two trades, trade rank at least three, or the
aggregate XR slope count.
