# KoalaBear m2 r4 coordinate negative one-loop 442 nonloop-singleton mixed-pair exclusion

- **status:** PROVED
- **scope:** the one-loop `(4,4,2)` common-`K` matching orbit
  `[4,5,7,8]`, where an `AB` record is the singleton, the loop is
  paired with an `AC` record, and the other `AB/AC` records are paired
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate` and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_product_q_weld`
- **consumer:** `rate_half_band_closure`

Normalize one cell by

```text
(x_L,x_AB+,x_AB-,x_AC+,x_AC-)=(1,t,r,epsilon_1*i,epsilon_2*i*r),
i^2=-1,                  epsilon_1,epsilon_2 in {+1,-1}. (KB41M-1)
```

Its labels and products are

```text
(1,t^2,r^2,-1,-r^2),       (-b^2,b,-b,c,-c).     (KB41M-2)
```

The first product equation safely reconstructs

```text
A=r^2t^2-1,       B=r^2-t^2,
c=-b(bA+B)/(bB+A).                                  (KB41M-3)
```

After this substitution, one q weld splits every guarded solution into

```text
Q0: rt+1=0,
Q1: rt-epsilon_1*i(r+t)-1=0.                       (KB41M-4)
```

Direct branchwise elimination of the remaining product equation and q weld
leaves only source-label collisions, `r=0`, or `b in {0,+1,-1}`.
Hence all four sign rows are empty.  Target representative changes carry
the normalization over cells `4,5,7,8`, so this entire common matching
orbit is deleted.

Together with the earlier opposite-pair exclusion and complete product
closes for `[3,6]` and `[9,10,12,13]`, this finishes every
nonloop-singleton common orbit.  It does not close the surviving aligned
loop-singleton families, complete one-loop 442, close a row, or prove
either Prize result.

## Falsifier

A guarded common-`K` packet in this orbit, a solution outside the two
branches, a lost denominator/degree-drop case, or a sign/cell class not
covered by the normalization.
