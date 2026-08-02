# KoalaBear positive 433-1a cell-5/8 epsilon-2-minus transport exclusion

- **status:** PROVED
- **scope:** every deployed parameter, matching cells `5,8`, common root
  signs `(epsilon_1,epsilon_2)=(+/-1,-1)`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_universal_target_elimination_compiler`,
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_cell5_complete_sign_row_exclusion`
- **consumer:** `rate_half_band_closure`

In the exact common matching atlas, cells `5` and `8` are

```text
cell 5: singleton AB+1, pairs (LC,AC),(AB+2,AB-),
cell 8: singleton AB+2, pairs (LC,AC),(AB+1,AB-).   (KBC58-1)
```

The two `AB+` records have identical target product and sum.  Their
transposition therefore gives an exact packet relabeling

```text
rho: cell 5 <-> cell 8                              (KBC58-2)
```

which preserves both common and outside Vieta systems and every guard.

For either cell, the second exact transport is

```text
(epsilon_1,epsilon_2,r,t)
    -> (-epsilon_1,epsilon_2,-r,-t).                (KBC58-3)
```

The five common quotient labels and every product row are fixed, while all
four nonloop values `q=z*s` are negated.  Negating every outside source lift
has the same effect.  The simultaneous coefficient involution

```text
B_1 -> -B_1                                             (KBC58-3a)
```

carries every transformed nonloop sum equation to the negative original
equation; it also negates the loop sum row, whose `q` part is zero.  Thus the
complete Vieta system, coefficient-kernel condition, target equations, and
source and target guards are preserved bijectively.

The proved complete cell-5 row `(-1,-1)` is empty for every deployed `t`.
Applying `(KBC58-3)` and `(KBC58-2)` proves that all four rows

```text
(cell,epsilon_1,epsilon_2) in
{5,8} x {-1,+1} x {-1}                            (KBC58-4)
```

are empty.

This does not treat `epsilon_2=+1`, any matching cell outside `{5,8}`,
delete the full positive `433-1a -> O0b` route, close K3 or a Prize row, or
prove LIST or MCA.

## Falsifier

An admissible packet in one of `(KBC58-4)`, a failure of the `AB+` role
transposition to preserve the full source placement, or failure of the
printed `B_1` coefficient involution to carry the complete transformed
Vieta system to the original one.
