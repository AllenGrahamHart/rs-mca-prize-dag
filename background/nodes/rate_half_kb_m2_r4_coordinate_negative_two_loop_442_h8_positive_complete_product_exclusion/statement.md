# KoalaBear m2 r4 coordinate negative two-loop 442 H8-positive complete-product exclusion

- **status:** PROVED
- **scope:** all twelve invariant-product cells over the two common rows
  `H8-L,tau=+1` and `H8-M,tau=+1`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_exceptional_product_classifier`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_outside_product_involution_compiler`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_product_invariance_router`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_signed_pair_matching_template_exclusion`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_h8m_minus_transport_exclusion`
- **consumer:** `rate_half_band_closure`

All twelve cells are empty over the deployed KoalaBear field.

On `H8-L,tau=+1`, eliminate `l` from the exact row equations and reduce the
locator and forced product.  This gives

```text
P_+(b)=b^4-2b^3-5b^2-2b+1=0,
c=(-b^2+3b+3)/2,
p=(5b^3-16b^2+8b+8)/23.                         (KB44E-1)
```

The two common antipodal product pairs give the bilinear involution

```text
Guv-A(u+v)-B=0,
G=b^2-bc+b+c,
A=bc(b^2+1),
B=-b^2c(b^2+bc-b+c).                             (KB44E-2)
```

For the three forced types, the residual product sextics can be written as

```text
cD: (a,sigma pa/c^2,x,-x,ax/p,-ax/p),
DE: (a,sigma pc^2/a,x,-x,sigma pc^2x/a^2,-sigma pc^2x/a^2),
DF: (a,q,sigma aq/c^2,-p,pq/a,-pq/a).            (KB44E-3)
```

For `cD` and `DE`, the signed-pair parent deletes matching indices
`0,1,2`.  The other twelve matchings are represented by
`3,4,5,9,10,11` under `F -> -F`.  For each sign and representative, the
three copies of `(KB44E-2)` have an exact resultant obstruction whose every
factor has nonzero norm against `P_+` in deployed characteristic.

For `DF`, the same primary chain has nonzero factor norms for twelve of the
fifteen matchings in each sign.  At indices `6,7,8` its final projection is
identically zero, but the complete three-equation ideal with `P_+` has
Groebner basis `[1]` directly over `F_2130706433`, in both signs.  An
independent chain sharing the second rather than first pair equation has a
nonzero deployed-field norm for all 54 sign/matching cases in `(KB44E-3)`.
Thus every `H8-L,tau=+1` cell is empty.

Exchange the two degree-four loops and renormalize:

```text
b'=1/b,       c'=c/b,       l'=l,
(D',E',F')=(D,E,F)/b.                            (KB44E-4)
```

This involution sends the `H8-L,tau=+1` row to `H8-M,tau=+1`, scales every
common and outside product by `b^-2`, preserves `sigma` and all three forced
types, and sends the forced product to its `H8-M` value.  Therefore all six
`H8-M,tau=+1` cells are empty as well.

The exact `442` frontier drops from four to two common rows, from 24 to 12
invariant cells, and from matching cap 312 to 156.  Only `H6,tau=-1` and
`H6,tau=+1` remain at this gate.

This theorem does not delete either `H6` row, impose full interpolation or
the remaining q/colored-resultant equations on any survivor, close the
coordinate orientation, move an owner/payment, close a Prize row, or prove
either Prize result.

## Falsifier

A guarded deployed-field complete-product packet over either positive H8
row; a zero deployed norm in either resultant order; a nonunit exceptional
ideal; or a failure of the row, product, forced-value, or transport identity.
