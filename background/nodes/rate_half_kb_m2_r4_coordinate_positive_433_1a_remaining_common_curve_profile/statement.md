# KoalaBear positive 433-1a remaining common curve profile

- **status:** PROVED
- **scope:** one exact representative of each of the seven unclosed common
  root-sign orbits over the deployed field
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient`,
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_cell1_2_common_root_sign_orbit_exclusion`
- **consumer:** `rate_half_band_closure`

For signs `(-1,-1)`, guard-saturate the six stripped common Vieta minors in
one representative of each remaining cell orbit:

```text
[0], [3,6], [4,7], [9,10], [11], [12,13], [14].
```

Every resulting ideal in `F_2130706433[z,t,r,c,b]` is proper and has Krull
dimension one.  Exact reduced Singular bases have sizes

```text
cell:        0   3   4   9  11  12  14
basis size:  7  23  24  23  26  29  31.             (KBRCP-1)
```

The corresponding three-minor chart calculations are also dimension one
and have the same recorded sizes.  This is a complexity profile, not an
assertion that the chart and full ideals are equal.

Exact source projectivities transport each representative throughout its
four-sign and duplicate-role orbit.  Thus no remaining orbit can be
deleted merely by proving its displayed localized common ideal is the unit
ideal: each has a nonempty geometric common curve.

This does not prove an `F_2130706433`-rational point, any outside record,
the positive route, K3, a Prize row, LIST, or MCA.

## Falsifier

A unit full ideal, a dimension other than one, a basis-size mismatch, or a
claim that geometric nonemptiness automatically gives a deployed rational
point or outside completion.
