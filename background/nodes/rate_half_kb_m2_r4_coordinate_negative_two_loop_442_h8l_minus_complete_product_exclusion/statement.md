# KoalaBear m2 r4 coordinate negative two-loop 442 H8-L-minus complete-product exclusion

- **status:** PROVED
- **scope:** the four remaining invariant-product cells over the common row
  `H8-L,tau=-1`, with forced `xi` type `sigma DE` or `DF`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_product_invariance_router`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_signed_pair_matching_template_exclusion`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_h8l_minus_cd_cell_exclusion`
- **consumer:** `rate_half_band_closure`

All four cells are empty over the deployed KoalaBear field.  Together with
the parent colored-`xi` exclusion, this deletes the entire
`H8-L,tau=-1` common row at the complete-product gate.

Retain the one-parameter data `(KB44C-1)--(KB44C-2)`:

```text
P_4(b)=b^4-2b^3+b^2-2b+1=0,
c=(b-2)(b^2+1)/b,
G(uv+1)-A(u+v)=0.                                (KB44D-1)
```

For forced type `sigma DE`, put `a=cD` and `x=DF`.  The residual products
are

```text
V_DE=(a,sigma c^2/a,x,-x,
      sigma c^2 x/a^2,-sigma c^2 x/a^2).          (KB44D-2)
```

The signed-pair parent deletes three matchings.  Exact factor norms delete
the other twelve, using matching representatives `3,4,5,9,10,11` under
`F -> -F`.  The union of nonunit norm prime supports is

```text
sigma=-1: {2,5,7,17,31,47,89,223,463,1249,14057},
sigma=+1: {2,3,7,17,79,103,401,457}.              (KB44D-3)
```

For forced type `DF`, put `a=cD` and `q=cE`.  The residual products are

```text
V_DF=(a,q,sigma aq/c^2,-1,q/a,-q/a).              (KB44D-4)
```

The primary resultant chain has nonzero factor norms for twelve of the
fifteen matchings in each sign.  Their support unions are

```text
sigma=-1: {2,7,11,23,31,103,14057},
sigma=+1: {2,3,7,17,79,103}.                      (KB44D-5)
```

For indices `6,7,8`, the primary eliminant is identically zero, but the
full three-equation ideal with `P_4` has Groebner basis `[1]` directly over
`F_2130706433`, for both signs.  Independently, an alternate resultant chain
has nonzero factor norms for all fifteen matchings in both signs.

The deployed characteristic divides none of `(KB44D-3)--(KB44D-5)`.
Consequently all six cells above `H8-L,tau=-1` are empty.  The exact `442`
frontier drops from 34 to 30 cells and from six to five common rows; the
matching-subcase cap drops from 444 to 390.

This theorem does not delete another common row, impose full interpolation
or remaining q/colored-resultant equations on the 30 survivors, close the
coordinate orientation, move an owner/payment, close a Prize row, or prove
either Prize result.

## Falsifier

A guarded deployed-field complete-product packet above `H8-L,tau=-1`, a
zero factor norm at the deployed characteristic, or a nonunit deployed-field
ideal at one of the six exceptional chain indices.
