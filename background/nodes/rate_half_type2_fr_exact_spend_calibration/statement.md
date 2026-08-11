# Exact spend calibration for the rate-half type-2 FR route

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_crossing_location`

Retain the strict endpoint parameters

```text
N=16m,       rho=4m-1,       T_target=rho+1=4m,
```

and the Round-31 bound `a=|W|<=7m-1`. At the worst allowed value
`a=7m-1`, the printed type-1 cap is at most two. If every type-2 slope
spends at least `p` locator roots outside `W`, the outside-incidence count
gives only

```text
T<=2+floor(((9m+1)m)/p).                              (FRC1)
```

Consequently the exact least integer spend that makes this counting route
prove `T<=4m` is

```text
p_req=floor(((9m+1)m)/(4m-1))+1.                     (FRC2)
```

When `4|m`, including the official `m=2^37`, this simplifies to

```text
p_req=9m/4+1.                                         (FRC3)
```

For a clean type-2 locator of size `rho`, the equivalent intersection cap is

```text
|S_gamma intersect W|<=rho-p_req=7m/4-2.             (FRC4)
```

The previously named spend `p=2m+2` is insufficient once `m>=8` and
`4|m`. At the official scale it yields

```text
2+floor(((9m+1)m)/(2m+2))=618475290622
```

against `4m=549755813888`, leaving a factor asymptotic to `9/8`.

This theorem corrects the constant in the proposed Round-31 `(FR)`
continuation. It does not assert `(FRC4)` for realizable pencils and does not
close the type-2 residual. It says that a per-slope-spend proof through the
printed outside-capacity ledger must reach `(FRC2)`, not merely `2m+2`.
