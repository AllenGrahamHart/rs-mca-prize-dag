# KoalaBear m2 r4 coordinate negative one-loop 433 opposite-pair exclusion

- **status:** PROVED
- **scope:** common matching cells `[11,14]` in every root-sign row over the
  deployed field
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate` and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_product_q_weld`
- **consumer:** `rate_half_band_closure`

Use representative cell `11`, with singleton `BC+` and source antipodal
pairs `L:BC-`, `AB:AC`.  As in the neighboring BC orbit, the product and q
systems each have one moving and one static row.  Exact guarded elimination
has terminal degree/multiplicity pattern

```text
(1,1), (1,3), (1,10), (1,10), (2,2), (4,2).       (KB433OP-1)
```

The four linear projections in each sign row occur in both the ordinary
square route and the lost moving-q coefficient route.  At every such root,
the exact candidate gcd in `b` is `b` or `b+1`.  Hence each forces the
forbidden target value `b=0` or `b=-1`.

The four quadratic and four quartic sign-row factors are irreducible over
`F_2130706433`, so they have no base-field roots.  Cell `11` is empty.
Target sign change `C->-C` transports it to cell `14`; therefore orbit
`[11,14]` is empty at the common stage.

This theorem does not by itself compose the other matching orbits, close
the coordinate orientation, close a Prize row, or prove either Prize
result.

## Falsifier

A linear branch with `b` outside `{0,-1}`, a reducible nonlinear factor, a
guarded common packet, or failure of the cell-11/14 target transport.
