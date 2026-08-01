# KoalaBear m2 r4 coordinate negative one-loop 433 AB/AC complete-product exclusion

- **status:** PROVED
- **scope:** common matching cells `[3,6]` and every complete outside
  skeleton over their sixteen deployed common packets
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_433_nonloop_singleton_ab_ac_finite_classifier`,
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_433_complete_edge_skeleton_classifier`,
  and `rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate`
- **consumer:** `rate_half_band_closure`

In cell `3`, the two common product pairs and singleton are

```text
(-1,c),       (bc,-bc),       singleton b.          (KB433PX-1)
```

Their unique product involution has

```text
Gamma=c-1,
Alpha=c(b^2c-1),
Beta=b^2c^2(1-c),
Delta=Alpha^2+Beta Gamma
     =c^2(b^2-1)(b^2c^2-1) != 0.                   (KB433PX-2)
```

The two target tuples retained by the finite classifier give forced mates

```text
(b,c)=(1375161449,1621120540) -> mate(b)=673740240,
(b,c)=( 477266026,1039843884) -> mate(b)=443602659. (KB433PX-3)
```

For every signed `S0,S1,S2` outside form, force one of its seven records to
the appropriate mate and pair the remaining six records in all fifteen
ways under `(KB433PX-2)`.  Over `F_2130706433`, every resulting ideal in
`(D,E,F)` is the unit ideal.  The exact raw census, including direct target-
exchanged replay of cell `6`, is

```text
S0: 3360,       S1: 6720,       S2: 1680,       total: 11760. (KB433PX-4)
```

Thus none of the sixteen common packets has a complete paired-product lift,
and cells `[3,6]` are empty as complete packets.

This theorem does not classify the other one-loop 433 common orbits, impose
outside q or interpolation, close the coordinate orientation, close a Prize
row, or prove either Prize result.

## Falsifier

A nonunit ideal in `(KB433PX-4)`, a complete outside product lift of one of
the sixteen packets, or a cell-`6` packet not covered by direct exchange.
