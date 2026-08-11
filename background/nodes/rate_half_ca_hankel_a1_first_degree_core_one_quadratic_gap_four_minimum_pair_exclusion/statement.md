# `A=1` quadratic gap-four minimum-pair exclusion

- **status:** PROVED
- **closure:** the actual-support boundary `rho+3` is empty
- **consumer:** `rate_half_band_crossing_location`

Retain either core-one quadratic `u=4` arm. For every two distinct supported
slopes,

```text
|S_alpha union S_beta|>=rho+4.                     (QME1)
```

Consequently, if one affine codeword line contains assigned centers at a
set `A` of `h>=2` supported slopes, then

```text
4h+sum_(gamma in A)r_gamma<=rho+4.                 (QME2)
```

For every fixed pair `alpha,beta`, at least

```text
rho+4-floor((rho+4-r_alpha-r_beta)/4)
 =ceil((3rho+12+r_alpha+r_beta)/4)                  (QME3)
```

other supported slopes `gamma` have

```text
|E_alpha union E_beta union E_gamma|>=2rho+1.      (QME4)
```

## Scope

The theorem excludes only pair union `rho+3`; it does not exclude either
quadratic packet. At equality in `(QME1)`, the complete coefficient-row
rank is at most three, so the next exact boundary is a rank-three
interpolation problem.
