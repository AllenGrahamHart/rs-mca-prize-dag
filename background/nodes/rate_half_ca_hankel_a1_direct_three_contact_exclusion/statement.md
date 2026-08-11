# `A=1` direct three-contact exclusion

- **status:** PROVED
- **closure:** pole-absorbing contact product and restriction vanishing
- **consumer:** `rate_half_band_crossing_location`

Retain a failing half-distance `A=1` profile with core size
`s in {0,1,2}`. Write

```text
d=rho-s,       T=4e+beta-ell,
beta=T_max-4e.                                         (DTC1)
```

Then every survivor satisfies

```text
ell>=e-3+beta.                                         (DTC2)
```

Indeed, one Forney contact copy absorbs the poles of `G/H`, and three
copies give a nonzero regular section

```text
s_F^3 G/H in H^0(C,O_C(d-3,ell-e+3-beta)).             (DTC3)
```

The section space in `(DTC3)` is zero when the second coordinate is
negative.

On the official row `rho=4m`, `m=2^37`, this excludes every core-free and
core-one degree below

```text
e_0=ceil((rho-1)/3)=183251937963.                       (DTC4)
```

At the first unexcluded degree, the only remaining slope counts are

```text
s=0: ell in {e_0-3,e_0-2,e_0-1},
s=1: ell in {e_0-2,e_0-1,e_0},
T in {rho+2,rho+3,rho+4}.                              (DTC5)
```

The core-two branch was already empty.

## Scope

The theorem does not exclude the six first-degree corners in `(DTC5)` or
higher `s=0,1` degrees.
