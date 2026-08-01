# KoalaBear m2 r4 coordinate negative one-loop 442 AB-singleton finite classifier

- **status:** PROVED
- **scope:** the one-loop `(4,4,2)` common-`K` matching orbit
  `[3,6]`, where one `AB` record is the singleton, the loop is paired
  with the other `AB` record, and the two `AC` records are paired
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate` and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_product_q_weld`
- **consumer:** `rate_half_band_closure`

In the deployed prime field, normalize one cell by

```text
(x_L,x_AB+,x_AB-,x_AC+,x_AC-)=(1,t,epsilon_1*i,r,epsilon_2*i*r),
i^2=-1,                  epsilon_1,epsilon_2 in {+1,-1}. (KB41B-1)
```

Its labels and products are

```text
(1,t^2,-1,r^2,-r^2),       (-b^2,b,-b,c,-c).     (KB41B-2)
```

The guarded common product equations and both one-loop q welds hold if and
only if

```text
r^2=-epsilon_2*i,          2b^2+3b+2=0,           (KB41B-3)

t=(-epsilon_1*i*r^2-2r-epsilon_1*i)
    /(r^2+2epsilon_1*i*r+1),                       (KB41B-4)

U=r^2t^2-3r^2+3t^2-1,   V=(r^2-1)(t^2+1),
c=b(bU-V)/(bV-U).                                  (KB41B-5)
```

Both displayed denominators are nonzero on the locus.  Each root-sign row
has exactly four guarded solutions in the deployed field, and all four
original determinant equations vanish at each one.  Target representative
sign changes carry the normalization over both cells `3` and `6`.

Thus this orbit is finite but not deleted.  This theorem does not impose
the seven outside products, their q values, or full interpolation; classify
the induced product involution before deciding whether any of these sixteen
common packets survive outside realization.

## Falsifier

A guarded common-`K` solution outside `(KB41B-3)--(KB41B-5)`, failure of
one listed candidate to satisfy an original equation or guard, a lost
denominator branch, or a sign/cell class not covered by the normalization.
