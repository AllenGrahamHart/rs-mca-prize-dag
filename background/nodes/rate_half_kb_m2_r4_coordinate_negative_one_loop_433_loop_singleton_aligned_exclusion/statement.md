# KoalaBear m2 r4 coordinate negative one-loop 433 aligned loop-singleton exclusion

- **status:** PROVED
- **scope:** common matching cell `0` of the negative one-loop `(4,3,3)`
  skeleton, in every source root-sign row
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate` and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_product_q_weld`
- **consumer:** `rate_half_band_closure`

Normalize the five common records by

```text
roles:    (L,AB,AC,BC+,BC-),
products: (-1,b,c,bc,-bc),
sums:     (0,1+b,1+c,b+c,b-c),
roots:    (t,1,epsilon_1*i,r,epsilon_2*i*r).       (KB431A-1)
```

Thus the loop is the singleton, while `AB:AC` and `BC+:BC-` are the two
source antipodal pairs.  After source and target guards, the two q welds
have direct `r`-resultant

```text
(b^2-1)(c^2-1)(bc-i)(bc+i).                       (KB431A-2)
```

Hence `bc=+i` or `bc=-i`.  In every one of the eight
`(epsilon_1,epsilon_2,sign(bc/i))` branches the q gcd is linear in `r`.
Substitution into the two product minors and elimination of `x=t^2` leaves
one of four guarded quartics in `b`:

```text
P0=b^4-(1+i)b^3+(1-i)b-1,
P1=b^4+(-1+i)b^3+(1+i)b-1,
P2=b^4+(1+i)b^3+(-1+i)b-1,
P3=b^4+(1-i)b^3+(-1-i)b-1.                       (KB431A-3)
```

Over `F_2130706433`, each `Pj` is a product of two irreducible quadratics.
Their four distinct discriminants are

```text
2130641919, 66911228, 2063795205, 64514,
```

and each has Euler value `-1`.  Therefore no deployed-field `b` survives,
so cell `0` is empty in every root-sign row.

This theorem does not delete the other fourteen one-loop 433 matching
cells, build an outside skeleton, close zero-loop or another parity, close
the coordinate orientation, close a Prize row, or prove either Prize
result.

## Falsifier

A guarded q branch outside `bc=+/-i`, an omitted root-sign branch, a lost
product-resultant factor, or a deployed-field root of one of `(KB431A-3)`.
