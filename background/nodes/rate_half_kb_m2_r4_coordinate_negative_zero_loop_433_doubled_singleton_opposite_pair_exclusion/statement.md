# KoalaBear m2 r4 coordinate negative zero-loop 433 doubled-singleton opposite-pair exclusion

- **status:** PROVED
- **scope:** common matching cells `[1,3,8,10]` in every root-sign row over
  the deployed field
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate` and
  `rate_half_kb_m2_r4_coordinate_negative_zero_loop_product_q_weld`
- **consumer:** `rate_half_band_closure`

Use the products and sums `(KBZ433M-1)`.  In cell `1`, `AB+` is the
singleton and the source antipodal pairs are `AB-:AC-` and `AC+:BC+`.
Normalize

```text
roots=(t,1,r,epsilon_1 i,epsilon_2 i r),
x=t^2, y=r^2.                                    (KBZ433O-1)
```

Put `S=(y+1)^2` and `Q=y^2-6y+1`.  Product compatibility is

```text
c(bQ-S)-b(bS-Q)=0.                               (KBZ433O-2)
```

Its lost coefficient branch is guarded.  On the regular branch it fixes
`c`; a product row fixes `x`; and the two quadratic q welds form an
affine-linear system in `(t,r)`.  After the protected square equations, the
only common cleared factor is the product denominator times `y^2-1`.

The residual lex/Frobenius census is

```text
(epsilon_1,epsilon_2)   basis   deg E_b   gcd(E_b,b^p-b)
(+,+)                     8        18     b^2-595625887b+1
(+,-)                     9        14     1
(-,+)                     9        14     1
(-,-)                     8        18     1,               (KBZ433O-3)
```

where `p=2130706433`.  The two roots in the first row both force

```text
y=1605884903,       X_den=0,       X_num!=0,       (KBZ433O-4)
```

so they are false product projections.  Exact lost-branch elimination gives
only guarded points, apart from the same two false projections in the
`(+,+)` singular-q row.  Hence cell `1` is empty.

The target sign/exchange group transports cell `1` through
`[1,3,8,10]`; therefore the complete four-cell orbit is empty at the common
stage.

This theorem does not classify cells `[2,5,6,9]` or `[12,13,14]`, impose
outside fibers, close the coordinate orientation, close a Prize row, or
prove either Prize result.

## Falsifier

A guarded solution of the original four common equations in this orbit, an
unrecorded base-field point on a lost branch, or a failed target transport.
