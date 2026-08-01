# KoalaBear m2 r4 coordinate negative one-loop 433 mixed-pair exclusion

- **status:** PROVED
- **scope:** common matching cells `[4,5,7,8]` in every root-sign row over
  the deployed field
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate` and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_product_q_weld`
- **consumer:** `rate_half_band_closure`

Use representative cell `4`, with singleton `AB` and antipodal source pairs
`L:BC+`, `AC:BC-`.  Normalize its roots to

```text
(1,t,r,epsilon_1 i,epsilon_2 i r).                 (KB433MX-1)
```

After removing only source/target guards, both q welds are linear in `t`.
Eliminate `t`, put `x=t^2` in the product rows, and eliminate `x`.  The
product compatibility is linear in `c`; its coefficient and constant cannot
vanish together off the guards.  Substituting its unique `c` into q
compatibility and the protected square equation gives, after removing
`r=0,+/-1,+/-i`, the square of one of

```text
(+,+): r^3+33423357r^2+33423359r-1,
(+,-): r^3+33423359r^2-33423357r+1,
(-,+): r^3-33423357r^2+33423359r+1,
(-,-): r^3-33423359r^2-33423357r-1.               (KB433MX-2)
```

All four cubics are irreducible over `F_2130706433`.  Therefore cell `4`
is empty.  Target sign change `C->-C`, target exchange `B<->C`, and their
composition transport this exclusion to cells `5,7,8`, respectively.
Thus the whole orbit `[4,5,7,8]` is empty at the common stage.

This theorem does not classify cells `[9,10,12,13]` or `[11,14]`, impose an
outside skeleton, close the coordinate orientation, close a Prize row, or
prove either Prize result.

## Falsifier

A guarded root of a cubic in `(KB433MX-2)`, a lost coefficient branch off
the printed guards, or failure of one of the three target transports.
