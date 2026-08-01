# KoalaBear m2 r4 coordinate negative one-loop 433 BC mixed-pair exclusion

- **status:** PROVED
- **scope:** common matching cells `[9,10,12,13]` in every root-sign row
  over the deployed field
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate` and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_product_q_weld`
- **consumer:** `rate_half_band_closure`

Use representative cell `9`, with singleton `BC+` and source antipodal
pairs `L:AB`, `AC:BC-`.  One product row is linear in `x=t^2` and the
other is independent of `x`; one q row is quadratic in `t` and the other
is independent of `t`.

The two static rows reconstruct `c` and leave a quadratic compatibility in
`(b,r)`.  Substitute `x` in the moving q row, protect its linear coefficient
in `t`, impose `t^2=x`, and eliminate `b`.  After source guards, every sign
row has terminal factor degrees and multiplicities

```text
(1,2), (2,1), (2,2), (5,2).                       (KB433BC-1)
```

The four linear roots are

```text
(+,+): 848940237,   (+,-): 1701222811,
(-,+): 1281766196,  (-,-):  429483622.            (KB433BC-2)
```

At each root, the exact candidate gcd in `b` divides the vanished `x`
coefficient and is coprime to the nonzero product constant.  Thus every
linear candidate fails the original product row.  All eight quadratic and
four quintic sign-row factors in `(KB433BC-1)` are irreducible over
`F_2130706433`, so they have no base-field `r`.

Target exchange `B<->C`, target sign change `C->-C`, and their composition
transport cell `9` to cells `10,12,13`.  Hence the complete orbit
`[9,10,12,13]` is empty at the common stage.

This theorem does not classify cells `[11,14]`, impose outside records,
close the coordinate orientation, close a Prize row, or prove either Prize
result.

## Falsifier

A valid linear candidate with nonzero `x` coefficient, a reducible nonlinear
factor, a guarded common packet, or failure of a target transport.
