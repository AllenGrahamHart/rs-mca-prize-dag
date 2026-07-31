# KoalaBear m2 r4 coordinate negative two-loop 442 H8-L-minus colored-xi cell exclusion

- **status:** PROVED
- **scope:** the two invariant-product cells with common row `H8-L`,
  `tau=-1`, forced `xi` type `cD`, and `sigma in {+1,-1}`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_outside_product_involution_compiler`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_product_invariance_router`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_signed_pair_matching_template_exclusion`
- **consumer:** `rate_half_band_closure`

Both cells are empty over the deployed KoalaBear field.

On `H8-L,tau=-1`, exact elimination and the row equation give

```text
P_4(b)=b^4-2b^3+b^2-2b+1=0,
c=(b-2)(b^2+1)/b,
p_xi=1.                                            (KB44C-1)
```

After a harmless common scaling, the product involution is

```text
G(uv+1)-A(u+v)=0,
G=b+c,
A=-bc(b-1).                                       (KB44C-2)
```

Put `a=cE` and `x=DF`.  The six residual products are exactly

```text
V_sigma=(a,sigma a/c^2,x,-x,ax,-ax).              (KB44C-3)
```

The parent template exclusion deletes the three matchings in which the
first two entries pair.  The other twelve matchings form six pairs under
`F -> -F`; use representatives `3,4,5,9,10,11` in the canonical fifteen-
matching order.

For each representative, clear denominators in its three copies of
`(KB44C-2)`, eliminate `x` twice and then `a`, factor the resulting
polynomial in `b`, and take every factor norm against `P_4`.  Every norm is
nonzero.  The prime support of all nonunit norms is

```text
sigma   matching   prime support
-1      3          {2,7,23,103}
-1      4          {2,7,31,97}
-1      5          {2,7,103,1223}
-1      9          {2,7,23,24137}
-1      10         {2,3,7,9479}
-1      11         {2,7,2377}
+1      3          {2,3,7}
+1      4          {2,7}
+1      5          {2,7}
+1      9          {2,7,239}
+1      10         {2,7,743}
+1      11         {2,7,137}.                    (KB44C-4)
```

The deployed characteristic `2130706433` divides none of these norms.
Thus no mixed matching exists, and the two cells are empty.  The exact
`442` invariant frontier drops from 36 to 34 cells; the matching-subcase cap
after the parent cut drops from 468 to 444.

This theorem does not delete the `H8-L,tau=-1` common row, treat its forced
types `sigma DE` or `DF`, treat another common row, impose full interpolation
or remaining q/colored-resultant equations, close the coordinate
orientation, move an owner/payment, close a row, or prove either Prize
result.

## Falsifier

A guarded deployed-field completion of either printed cell, or a zero
factor norm in `(KB44C-4)` at the deployed characteristic.
