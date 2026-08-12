# Proof

The direction-support affine-basis proof gives, for zero-normal parameters
`z=g+c` with `0<=z<=K-r`,

```text
|Z| <= ((n-z)_(fall r+1)-(n-e-z)_(fall r+1))
       /((m-g)(d+c)_(rise r)).                        (1)
```

Fix `z` and substitute `g=z-c`.  The numerator is fixed, while the
denominator becomes

```text
(m-z+c)(d+c)_(rise r).
```

Both factors are positive and increasing in `c`.  Thus `(1)` is maximized
at `c=0`, `g=z`.

Put `x=n-z=R+K-z`.  Since `0<=z<=K-r`,

```text
R+r<=x<=R+K,
m-z=d+K-z=x-R+d.
```

Substitution gives `(CZ1)`.  Taking the larger interval
`[R+r,2R]` proves the uniform form for every `K<=R`.

For fixed `x`, its numerator increases with `e`; hence the maximum in
`(CZ1)` also increases with `e`.  The primary certificate exhausts every
integer `x` in the uniform interval at each last-paid support and adjacent
first-unpaid support.  Exact rational comparison identifies the printed
maximizer and exact floor, so monotonicity certifies the complete paid
prefix.  The independent recurrence scan reproduces every maximum without
calling the primary product routine.
