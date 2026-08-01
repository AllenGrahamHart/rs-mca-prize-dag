# KoalaBear m2 r4 coordinate negative one-loop 442 AB-singleton product involution compiler

- **status:** PROVED
- **scope:** every complete packet over the finite common-`K` orbit
  `[3,6]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_ab_finite_classifier`,
  `rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_complete_edge_skeleton_classifier`
- **consumer:** `rate_half_band_closure`

The finite common atlas additionally satisfies

```text
2b^2+3b+2=0,          4c^2=5b+6.                 (KB41BI-1)
```

Its two common source pairs have product pairs

```text
(-b^2,-b),            (c,-c),                    (KB41BI-2)
```

and the common singleton has product `b`.  Define

```text
Gamma=b(b+1),       Alpha=-(b^3+c^2),
Beta=-b(b+1)c^2,
Phi(Y,Z)=Gamma*Y*Z-Alpha*(Y+Z)-Beta.              (KB41BI-3)
```

Then `Phi=0` is the unique nonsingular product involution containing both
pairs, because

```text
Alpha^2+Gamma*Beta
 =(b-c)(b+c)(b^2-c)(b^2+c) !=0.                  (KB41BI-4)
```

The outside product opposite singleton `b` is forced to be

```text
m=iota(b)=(18-5b)/22.                             (KB41BI-5)
```

Its denominator is nonzero in the deployed field, and `m` is finite,
nonzero, distinct from `b`, and distinct from all four paired common
products.  In every outside skeleton exactly one product must equal `m`;
the other six products split into three `Phi` pairs.

This theorem does not enumerate those outside templates, impose outside q
equations or full interpolation, classify `[4,5,7,8]`, close the
coordinate orientation or a row, or prove either Prize result.

## Falsifier

A finite common packet violating `(KB41BI-1)`, a different product
involution or singleton mate, a vanishing displayed denominator or
determinant, or a passing outside product multiset without the forced mate
and three `Phi` pairs.
