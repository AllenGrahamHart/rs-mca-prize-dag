# KoalaBear m2 r4 coordinate negative two-loop 442 H8-M-minus transport exclusion

- **status:** PROVED
- **scope:** all six invariant-product cells over the common row
  `H8-M,tau=-1`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_exceptional_product_classifier`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_product_invariance_router`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_h8l_minus_complete_product_exclusion`
- **consumer:** `rate_half_band_closure`

All six cells are empty over the deployed KoalaBear field.

Swap the two degree-four loop pairs `A <-> B` in an `H8-L,tau=-1` packet
and renormalize the new `A` representative to one.  On parameters this is
the involution

```text
b'=1/b,       c'=-c/b,       l'=l.                (KB44M-1)
```

It sends the `H8-L` row equations and label tuple to the `H8-M` equations
and tuple:

```text
(l,-l^2,1,-1,l^2) -> (-l^2,l,1,l^2,-1).          (KB44M-2)
```

After the common product scaling `p'=p/b^2`, the swapped product vector is
exactly

```text
(-1,-b'^2,b',c',-b'c').                           (KB44M-3)
```

The forced product on the `H8-M` row is `p_xi=b'^2`, the image of the
`H8-L` forced value `1`.  Send the horizontal representatives by

```text
D'=-D/b,       E'=-E/b,       F'=-F/b.            (KB44M-4)
```

Then every product in

```text
{cD,cE,sigma DE,DF,-DF,EF,-EF}
```

is sent to its same named product divided by `b^2`.  Thus `(KB44M-1)`--
`(KB44M-4)` preserve both values of `sigma`, all three canonical forced
types, product distinctness, and the complete paired-product involution
gate.  The transformation is involutive.

The proved emptiness of every `H8-L,tau=-1` cell therefore transports to
every `H8-M,tau=-1` cell.  The exact `442` frontier drops from five to four
common rows, from 30 to 24 invariant cells, and from matching cap 390 to
312.

This theorem does not delete either `tau=+1` eighth-root row or an `H6`
row, impose full interpolation or remaining q/colored-resultant equations
on survivors, close the coordinate orientation, move an owner/payment,
close a Prize row, or prove either Prize result.

## Falsifier

A guarded `H8-M,tau=-1` completion whose inverse transport is not an
`H8-L,tau=-1` completion, or a failure of any printed row, product, forced-
type, or sign identity.
