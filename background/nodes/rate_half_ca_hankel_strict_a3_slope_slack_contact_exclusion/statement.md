# Strict `A=3` slope-slack contact exclusion

- **status:** PROVED
- **closure:** general pole interpolation and three-contact vanishing
- **consumer:** `rate_half_band_crossing_location`

Retain a failing strict profile and write

```text
delta=rho-3e,       T=4e+1-h,
0<=O<=delta,        0<=h<=4(e-m).                     (SSC1)
```

Put

```text
ell=floor(delta/2).                                   (SSC2)
```

If

```text
ell+h+2<e,                                             (SSC3)
```

then the profile is impossible.

For the official `m=2^37`, condition `(SSC3)` excludes every strict `A=3`
failure profile except the single integer corner

```text
e=floor(rho/3)=(4m-2)/3,
delta=1,
h=e-2,
T=rho+2.                                              (SSC4)
```

Thus the entire remaining strict `A=3` program is one minimal-violation
profile with at most one root omission and at most one unit of total rank
loss.

## Scope

The theorem does not exclude `(SSC4)`, any residual `A=1` profile, or the
adjacent unsafe witness.
