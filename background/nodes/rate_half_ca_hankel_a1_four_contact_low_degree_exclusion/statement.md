# `A=1` four-contact low-degree exclusion

- **status:** PROVED
- **closure:** degree-three pole interpolation and four-contact vanishing
- **consumer:** `rate_half_band_crossing_location`

For a failing `A=1` profile with core size `s in {0,1,2}`, retain

```text
d=rho-s,       Delta=d-(s+1)e,
T=4e+beta-ell, p<=O<=Delta,                           (A1Q1)
```

where `beta=T_max-4e`. Assume

```text
3(e+1)<rho+1.                                         (A1Q2)
```

If

```text
floor(p/4)+ell+4-beta<e,                              (A1Q3)
```

then the profile is impossible.

On the official row `rho=4m`, this excludes the complete degree prefixes

```text
s=0: m+1<=e<=floor(12m/11)-1,
s=1: m+1<=e<=floor(6m/5)-1.                           (A1Q4)
```

In particular, all three core-free first-degree chambers from the
three-contact theorem are empty.

## Scope

The theorem complements rather than replaces the three-contact bounds. It
does not exclude core-free degrees at or above `floor(12m/11)` or core-one
degrees at or above `floor(6m/5)`.
