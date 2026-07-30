# KoalaBear m2 r2 full-V4 exclusion

- **status:** PROVED
- **scope:** actual KoalaBear inner-degree-two type
  `(m,r,delta)=(2,2,4)`
- **dependencies:** the exhaustive dihedral outer-factor reduction and the
  `n=2,3,5,6` exclusions
- **consumer:** `rate_half_band_closure`

Every actual full-V4 component has a Dickson/Chebyshev outer factor of
degree

```text
n in {2,3,5,6}.                                    (KBV4-1)
```

The degree-two source-star, degree-three source-facet, degree-five
source-star, and degree-six common-pole theorems exclude the four values
in `(KBV4-1)`. Therefore the full-V4 type

```text
(m,r,delta)=(2,2,4)
```

is empty.

The two other `m=2` stabilizer types `(r,delta)=(4,2)` and `(8,1)` remain
open. This node constructs no owner or payment and closes no endpoint,
KoalaBear, or Prize row.

## Falsifier

An actual full-V4 component whose factor degree lies outside `(KBV4-1)`,
or a surviving component in any of the four listed degrees.
