# `A=1` fixed-core pole-slack exclusion

- **status:** PROVED
- **closure:** contracted pole interpolation and three-contact vanishing
- **consumer:** `rate_half_band_crossing_location`

Retain a failing fixed-core profile `s in {1,2}`. Put

```text
d=rho-s,       Delta=d-(s+1)e,
T=T_max-ell,   beta=T_max-4e,                         (A1X1)
```

where `beta=1`, except that `s=2,3e=d` has `beta=2`. Let `p<=O<=Delta`
be the actual pole-ideal colength on the residual curve. If

```text
floor(p/3)+ell+3-beta<e,                              (A1X2)
```

then the profile is impossible.

Consequences:

1. every surviving `s=1` profile satisfies

```text
p>=3(e-ell-2);                                        (A1X3)
```

2. the first `s=1` degree `e=m+1` is impossible on the official row;
3. **every `s=2` profile is impossible.**

## Scope

This closes the fixed-core-two branch and narrows fixed-core one. It does not
close all `s=1` or core-free profiles.
