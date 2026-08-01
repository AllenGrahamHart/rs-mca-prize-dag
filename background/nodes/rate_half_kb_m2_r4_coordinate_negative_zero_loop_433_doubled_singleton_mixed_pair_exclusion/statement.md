# KoalaBear m2 r4 coordinate negative zero-loop 433 doubled-singleton mixed-pair exclusion

- **status:** PROVED
- **scope:** common matching cells `[0,4,7,11]` in every root-sign row over
  the deployed field
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate` and
  `rate_half_kb_m2_r4_coordinate_negative_zero_loop_product_q_weld`
- **consumer:** `rate_half_band_closure`

Normalize the zero-loop products and sums as

```text
roles:    (AB+,AB-,AC+,AC-,BC+),
products: (b,-b,c,-c,bc),
sums:     (1+b,1-b,1+c,1-c,b+c).                 (KBZ433M-1)
```

In cell `0`, `AB+` is the singleton and the source antipodal pairs are
`AB-:AC+` and `AC-:BC+`.  Put

```text
roots=(t,1,epsilon_1 i,r,epsilon_2 i r),
x=t^2, y=r^2.                                    (KBZ433M-2)
```

After the two product rows, removal of target guards leaves the equation

```text
b^2(y+1)^2+b(y^2-6y+1)
 +c[b(y^2-6y+1)+(y+1)^2]=0.                     (KBZ433M-3)
```

Its lost coefficient branch is guarded.  On the regular branch it fixes
`c`, and the first product row fixes `x`.  The two quadratic q welds then
form an affine-linear `2 x 2` system in `(t,r)`.  After Cramer reduction and
the protected equations `t^2=x,r^2=y`, the only common cleared factor is
the product denominator times `y^2-1`.  Removing it leaves a
zero-dimensional ideal.

The exact degree-20 `b` eliminants have the following base-field root gcds:

```text
(epsilon_1,epsilon_2)     gcd(E_b,b^p-b)
(+,+)                     1
(+,-)                     b^2+6b+1
(-,+)                     b^4-295154008b^3+359782351b^2-295154008b+1
(-,-)                     1,                       (KBZ433M-4)
```

where `p=2130706433`.  The two roots in the `(+,-)` row force `y=1`.
In the `(-,+)` row, two roots again force `y=1`; the other two force the
product denominator to zero while its numerator is nonzero.  Thus every
generic projection is false or guarded.  Exact lost-branch elimination
shows that the linear-`c` and product-solve branches contain only

```text
(b,y)=(0,-1),(1,1),(-1,0),                       (KBZ433M-5)
```

and the singular-q branches add no valid point.  Hence cell `0` is empty.

Simultaneous target sign change and target exchange generate the role
permutations `(AB+ AB-)(AC+ AC-)` and
`(AB+ AC+)(AB- AC-)`.  They transport cell `0` through the orbit
`[0,4,7,11]`.  All four cells are therefore empty at the common stage.

This theorem does not classify cells `[1,3,8,10]`, `[2,5,6,9]`, or
`[12,13,14]`, impose the seven outside fibers, close the coordinate
orientation, close a Prize row, or prove either Prize result.

## Falsifier

A guarded solution of the original four common equations in one of these
cells, an unrecorded base-field point on a lost branch, or failure of one of
the target transports.
