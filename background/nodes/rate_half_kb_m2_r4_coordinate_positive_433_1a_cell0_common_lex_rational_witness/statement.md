# KoalaBear positive 433-1a cell-0 common lex basis and rational witnesses

- **status:** PROVED
- **scope:** cell `0`, signs `(-1,-1)`, over the deployed field
  `F_p`, `p=2130706433`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler`
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_remaining_common_curve_profile`
- **consumer:** `rate_half_band_closure`

Let `i=16711679`, so `i^2=-1 mod p`.  The guard-localized full six-minor
cell-0 ideal has dimension one and a seven-element block basis.  After
eliminating the guard inverse, its projected lexicographic basis in
`F_p[r,c,b,t]` consists of the following four polynomials:

```text
b^2-6b+1,

c t^4-i c-1056997377 b t^4-8355839 b t^2+1065353216 b
  +1056997377 t^4-8355839 t^2-1065353216,

c b-33423356 c t^2-3c+16711680 b t^2-i b
  -16711680 t^2-i,

r+i t^2.                                           (KBC0L-1)
```

The quadratic in `b` splits over `F_p`.  At `t=2`, direct substitution in
all six stripped compiler minors and all twenty source/target guards gives
two deployed rational common points:

```text
(t,r,c,b)=(2,2063859717,572859116,1547071505),
(t,r,c,b)=(2,2063859717,396175561,583634934).       (KBC0L-2)
```

Every minor value is zero and every guard value is nonzero at both points.
Thus cell `0` genuinely survives the common stage over the deployed base
field, not only geometrically after algebraic closure.

This does not prove the projected basis lifts at every parameter, any
outside record or complete target realization, the positive route, K3, a
Prize row, LIST, or MCA.

## Falsifier

A mismatch in `(KBC0L-1)`, a nonzero compiler minor or zero guard at either
point in `(KBC0L-2)`, or an inference from common survival to outside
completion.
