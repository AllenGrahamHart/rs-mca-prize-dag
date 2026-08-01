# KoalaBear m2 r4 coordinate negative zero-loop 433 BC-singleton product router

- **status:** PROVED
- **scope:** the 32 common packets in cells `[12],[13],[14]` over
  `F_(2130706433^6)`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_bc_singleton_finite_classifier`,
  `rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_complete_edge_skeleton_classifier`,
  and `rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate`
- **consumer:** `rate_half_band_closure`

The common product involutions and forced singleton mates are

```text
cell 12: I(y)=-y,       I(bc)=-bc;
cell 13: I(y)=bc/y,     I(bc)=1;
cell 14: I(y)=-bc/y,    I(bc)=-1.                  (KBZ433BP-1)
```

Compile every signed form of `Z0,...,Z4`, force one outside product to the
mate in `(KBZ433BP-1)`, and match the remaining six under the corresponding
involution.  Exact Smith enumeration modulo `p^6-1`, followed by signed
target-pair and twelve-product injectivity, gives the exclusions

```text
cell 12: Z0 and Z1 are empty;
cell 13: Z0 and Z4 are empty;
cell 14: Z0 and Z4 are empty.                       (KBZ433BP-2)
```

This holds for all eight distinct `(b,c)` rows in cell `12` and all four in
each of cells `13,14`, hence for all 32 common packets.  The 16 rank-two
`Z0` systems per cell-12 product row all force a target-square collision;
the other deleted types have no positive-dimensional system.

The product gate is genuinely live on the complementary types: guarded
certificates exist for `Z2,Z3,Z4` in cell `12` and for `Z1,Z2,Z3` in each of
cells `13,14`.  These are necessary product packets only.

This theorem does not assign outside quotient labels, impose q/interpolation,
delete a live type, close the coordinate orientation, close a Prize row, or
prove either Prize result.

## Falsifier

A guarded deployed-extension lift in a type deleted by `(KBZ433BP-2)`, a
collision-free deleted family, or failure of a printed live-type product
certificate.
