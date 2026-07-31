# KoalaBear m2 r4 coordinate negative two-loop 442 outside-product involution compiler

- **status:** PROVED
- **scope:** every injective root of the six q-compatible common-`K`
  product rows `(KB4P-3)--(KB4P-5)`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_exceptional_product_classifier`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_q_orientation_lift`,
  `rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate`,
  `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature`, and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_edge_skeleton_classifier`
- **consumer:** `rate_half_band_closure`

For a product pair `(y,z)`, put

```text
r(y,z)=[yz,-(y+z),-1].                            (KB44O-1)
```

The two complete antipodal pairs already in `K`, the singleton product,
and its missing source label are as follows:

```text
row    known product pairs                 singleton product   xi
H6     (-1,c),       (-b^2,tau bc)         b                   -1
H8-L   (b,c),        (-b^2,tau bc)        -1                   -l
H8-M   (b,tau bc),   (c,-1)               -b^2                -l. (KB44O-2)
```

For each of the two signs `tau`, let

```text
(Gamma,Alpha,Beta)=r(y_1,z_1) cross r(y_2,z_2),
Gamma yz-Alpha(y+z)-Beta=0.                       (KB44O-3)
```

The two rows in `(KB44O-2)` are independent and `(KB44O-3)` is the unique
nonsingular projective product involution through them.

The common-`K` Mobius map forces `p_xi=N/H`, where

```text
H6:
 N=b(b l^2+b-l^2+2l-1),
 H=b l^2-2bl+b-l^2-1;

H8-L:
 N=b(2b l^2+2b-l^2+2l-1),
 H=b l^2-2bl+b-2l^2-2;

H8-M:
 N=b(b l^2-2bl+b-2l^2-2),
 H=2b l^2+2b-l^2+2l-1.                           (KB44O-4)
```

Exact iterated resultants of `N/b` and `H` with the corresponding row
ideal are

```text
row       tau=-1             tau=+1
H6        49,49              1,1
H8-L      784,784            8464,8464
H8-M      784,784            8464,8464.           (KB44O-5)
```

Thus `p_xi` is finite and nonzero in every characteristic outside
`{2,7,23}`.  In particular this holds in the deployed KoalaBear field of
characteristic `2130706433`.  It is distinct from the five common products,
and the singleton-product pair in `(KB44O-2)` satisfies `(KB44O-3)`.

After the two pairs in `(KB44O-2)` and this forced singleton pair are
removed, the remaining six outside labels form three antipodal pairs.
Their product pairs all satisfy the same row-specific bilinear equation
`(KB44O-3)`.  Conversely, imposing that equation on those three pairs is
equivalent to the complete six-row paired-product rank gate.

If `xi=eta`, `(KB44O-4)` is the forced `eta` internal record.  Otherwise
`xi` lies in `L^c`; its record may be internal or one of the two colored
`C-I` records allowed by the complete edge skeleton.

This theorem does not choose the `eta` type, assign the remaining quotient
labels, prove full twelve-row Mobius interpolation, impose the remaining q
or colored-resultant equations, delete a common row or skeleton, close the
coordinate orientation, move an owner/payment, close a row, or prove either
Prize result.

## Falsifier

An injective root of a printed common row with a different sixth product,
a zero protected factor in deployed characteristic, a singular involution,
or an outside antipodal product pair violating `(KB44O-3)`.
