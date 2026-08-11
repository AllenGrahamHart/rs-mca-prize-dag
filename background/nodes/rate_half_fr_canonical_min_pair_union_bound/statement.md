# Canonical minimum-pair-union FR bound

- **status:** PROVED
- **closure:** elementary set identity
- **consumer:** `rate_half_band_crossing_location`

Let the supported slopes have finite locator sets `S_gamma` with

```text
|S_gamma|=u_gamma=rho-o_gamma,       o_gamma>=0.
```

Define the minimum pair-union size and choose a minimizing pair by

```text
a*=min_(g!=h) |S_g union S_h|,
W*=S_g union S_h,       |W*|=a*.                      (FRC1)
```

Then every supported `gamma` distinct from `g,h` satisfies

```text
|S_gamma intersect W*|
 <=2u_gamma+u_g+u_h-2a*
 =4rho-2a*-2o_gamma-o_g-o_h,                          (FRC2)

|S_gamma \ W*|
 >=2a*-u_gamma-u_g-u_h
 =2a*-3rho+o_gamma+o_g+o_h.                           (FRC3)
```

At the clean rate-half endpoint

```text
rho=4m-1,       a*=7m-1,       o_gamma=o_g=o_h=0,
```

these specialize to

```text
|S_gamma intersect W*|<=2m-2,
|S_gamma \ W*|>=2m+1.                                 (FRC4)
```

## Scope

The choice of `W*` as a minimum pair union is essential. The theorem makes no
claim for an arbitrary `a*`-set `W`, and it does not require saturation,
Hankel-pencil realizability, or locator-polynomial algebra. The endpoint spend
in `(FRC4)` improves the old minimum-distance spend but is still below the
separately calibrated closing spend `9m/4+1`.
