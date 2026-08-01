# KoalaBear m2 r4 coordinate negative zero-loop 433 product-skeleton router

- **status:** PROVED
- **scope:** the 32 common packets in cells `[2,5,6,9]` over the deployed
  field `F_(2130706433^6)`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_aligned_doubled_pair_finite_classifier`,
  `rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_complete_edge_skeleton_classifier`,
  and `rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate`
- **consumer:** `rate_half_band_closure`

For each of the four distinct `(b,c)` rows in the common classifier, the two
common product pairs are

```text
(-b,bc), (c,-c), with singleton b.                 (KBZ433P-1)
```

Their projective product involution has

```text
Gamma=b(c-1), Alpha=c(c-b^2)=0, Beta=-bc^2(c-1),
I(y)=-c^2/y,                 I(b)=-c^2/b.           (KBZ433P-2)
```

Compile every signed product form from the five outside skeletons
`Z0,...,Z4`, force one of the seven products to `I(b)`, and pair the other
six under `(KBZ433P-2)`.  The exact deployed-extension census per `(b,c)` is

```text
type  raw cells  compatible systems  isolated solutions  families  guarded
Z0       420             86                 216              0       48
Z1      3360            480                1216              0      128
Z2      1680            312                 736             16        0
Z3      3360            432                 864              0        0
Z4      1680            240                 536              0       64. (KBZ433P-3)
```

Every `Z2` family forces a signed-target or product collision, and every
isolated `Z2` or `Z3` solution fails target-pair or twelve-product
injectivity.  Hence `Z2` and `Z3` are empty as complete product packets for
all 32 common packets.  Conversely, each of `Z0,Z1,Z4` has guarded product
certificates, so the product gate alone cannot delete those types.

This theorem does not assign the seven outside quotient labels, impose the
outside q rows or complete interpolation, prove that a guarded product
certificate is an actual packet, classify cells `[12,13,14]`, close the
coordinate orientation, close a Prize row, or prove either Prize result.

## Falsifier

A guarded deployed-extension product lift of `Z2` or `Z3`, failure of a
printed live-type certificate, or a complete product packet omitted by the
five skeleton compiler.
