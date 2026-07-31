# KoalaBear m2 r4 coordinate negative two-loop 433 outside-product involution compiler

- **status:** PROVED
- **scope:** every `M2` or `M3` common-`K` candidate retained by the exact
  `(4,3,3)` classifier
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_m2_m3_product_q_classifier`,
  `rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate`,
  and `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature`
- **consumer:** `rate_half_band_closure`

Use `epsilon=-1` for `M2` and `epsilon=+1` for `M3`, with the notation
`P_6,A,D,E` and the equations `(KB43M-3)` from the parent classifier.
The two complete antipodal pairs already inside `K` have product pairs

```text
M2: (b,-1),  (-b,bc),
M3: (b,bc),  (-b,-1).                             (KB43O-1)
```

They determine the common projective product involution

```text
Gamma yz-Alpha(y+z)-Beta=0,                       (KB43O-2)

Gamma=2b+epsilon(bc+1),
Alpha=b(bc-1),
Beta =epsilon b^2(bc+2epsilon c+1).               (KB43O-3)
```

It is nonsingular because

```text
Alpha^2+Gamma Beta
 =2b^2(b+epsilon)(c+epsilon)(bc+1) !=0.            (KB43O-4)
```

The singleton `K` label is `M`.  Since the invariant six-set `I` is
antipodal and contains `K`, its unique missing label is

```text
xi=-M.                                             (KB43O-5)
```

The product at this outside mate is forced by the common-`K` Mobius map:

```text
p_xi=N_epsilon/H_epsilon,
N_epsilon=epsilon b[b(M-1)^2-epsilon(M+1)^2],
H_epsilon=b(M+1)^2-epsilon(M-1)^2.                (KB43O-6)
```

For each sign, exact iterated resultants for both bracket factors in
`N_epsilon,H_epsilon` equal `2^32`.  Hence `(KB43O-6)` is finite and
nonzero over every odd characteristic on every root of `(KB43M-3)`.  It is
distinct from all five common-`K` products by Mobius injectivity, and the
pair `(-c^2,p_xi)` satisfies `(KB43O-2)`.

After the two pairs in `(KB43O-1)` and the singleton pair are removed, the
remaining six outside labels form three antipodal pairs.  Their product
pairs must all satisfy the same explicit bilinear equation `(KB43O-2)`.
Conversely, because the two rows in `(KB43O-1)` are independent, imposing
`(KB43O-2)` on those four remaining pairs is equivalent to the complete
six-row paired-product rank gate.

If `L=I`, then `xi=eta` and `(KB43O-6)` is the forced `eta` `I-I` record.
If `L!=I`, then `xi` lies in `L^c`; its record is `I-I` or `I-J`, and in
the latter case `xi` is one of the two roots of the colored divisor.

This theorem does not assign the remaining edge types, prove the full
twelve-row product interpolation, impose all q rows or colored resultants,
delete the `(4,3,3)` skeleton, close the coordinate orientation, move an
owner/payment, close a row, or prove either Prize result.

## Falsifier

An actual retained `M2/M3` packet with a different `xi` product, a singular
involution `(KB43O-3)`, or an outside product pair violating `(KB43O-2)`.
