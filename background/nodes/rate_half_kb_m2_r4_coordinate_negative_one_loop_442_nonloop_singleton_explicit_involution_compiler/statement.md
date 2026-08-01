# KoalaBear m2 r4 coordinate negative one-loop 442 nonloop-singleton explicit involution compiler

- **status:** PROVED
- **scope:** every complete packet over the finite common-`K` orbit
  `[9,10,12,13]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_degree12_gate`,
  `rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_complete_edge_skeleton_classifier`
- **consumer:** `rate_half_band_closure`

The two common source pairs have product pairs

```text
(-b^2,b),        (-b,-c),                         (KB41I-1)
```

while the common singleton has product `c`.  Define

```text
Gamma =c+2b-b^2,
Alpha =-b(c+b^2),
Beta  =b^2(c-b^2-2bc),                            (KB41I-2)

Phi(Y,Z)=Gamma*Y*Z-Alpha*(Y+Z)-Beta.
```

Then `Phi=0` is the unique projective product involution containing both
pairs in `(KB41I-1)`, and

```text
Alpha^2+Gamma*Beta
  =2b^2(b-1)(b+c)(b^2-c) !=0.                    (KB41I-3)
```

The outside product opposite the singleton is forced to be

```text
m=iota(c)
 =-b(b^3+3b^2c-bc+c^2)/(b^3-b^2c+3bc+c^2).      (KB41I-4)
```

For an actual complete packet the denominator in `(KB41I-4)` is nonzero.
Across each of `S0,S1,S2`, exactly one of the seven outside products equals
`m`, and the other six split into three pairs `(Y,Z)` satisfying
`Phi(Y,Z)=0`.  This is necessary and sufficient for the outside product
multiset to pass the paired-product gate.

This theorem does not enumerate those finite matchings, impose outside sum
equations or full interpolation, classify another common orbit, close the
coordinate orientation or a row, or prove either Prize result.

## Falsifier

An actual packet in the finite common orbit whose product involution is not
`(KB41I-2)`, whose singleton mate differs from `(KB41I-4)`, or whose outside
multiset passes without the stated forced value and three `Phi` pairs.
