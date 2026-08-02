# KoalaBear m2 r4 positive 433-1b product-rank-drop deployed rational classifier

- **status:** PROVED
- **scope:** deployed-field rational points on the finite exceptional common
  schemes of `433-1b -> O0a`
- **dependency:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_common_exception_classifier`
- **consumer:** `rate_half_band_closure`

Apply exact FGLM conversion to each of the forty zero-dimensional ideals
retained by the parent theorem.  Every resulting reduced lexicographic
basis is in shape position:

```text
g(b),  c-C(b),  r-R(b),  t-T(b),  z-Z(b).         (KBP1BRF-1)
```

Exact factorization of `g` over `F_2130706433` has the following degree
patterns in every root-sign row:

```text
cells 4,7:    3+3,          cells 5,8:   2+2+4,
cell 11:      2+2+2+2+3+3+3+3,
cells 12,13:  2+2+10,       cell 14:     3+3+3+3,
cells 9,10:   1+1+2+2+4+6.                       (KBP1BRF-2)
```

All factors are distinct and irreducible over the deployed field.  Hence
the 32 rows in cells

```text
4,5,7,8,11,12,13,14                             (KBP1BRF-3)
```

have no deployed-field rational point.  Each of the eight rows in cells 9
and 10 has exactly two rational points, reconstructed uniquely from the two
linear roots using `(KBP1BRF-1)`.  Thus the original sixty-row exceptional
branch has exactly sixteen guarded common points, all in cells 9 and 10.

Independent replay at every retained point gives

```text
rank(P)=4,       rank(M)=7,       z H=1.           (KBP1BRF-4)
```

This theorem classifies common Vieta points only.  It does not append the
seven outside rows, assert that any retained point lifts to a packet, solve
the principal product-rank-five branch, close `433-1b -> O0a`, K3, LIST,
MCA, or either Prize result.

## Falsifier

A deployed-field point in a row from `(KBP1BRF-3)`, a missing or additional
point in cells 9 or 10, a non-shape lex basis, an incorrect irreducible
factor degree, or failure of `(KBP1BRF-4)`.
