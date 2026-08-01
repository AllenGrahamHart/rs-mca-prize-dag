# KoalaBear m2 r4 positive 433-1a common-kernel uniqueness

- **status:** PROVED
- **scope:** all fifteen common matching cells of the deployed-field route
  `433-1a -> O0b`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_product_base_rank_global_certificate`
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_pivot_chart_reduction`
- **consumer:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_quadratic_paired_product_resultant_interface`

Let `B` be the six-row common base: the five product rows and the loop sum
row.  The global product-base theorem gives `rank B=6` in every matching
cell.  Write `lambda_0` for the common loop label and `lambda_i` for any of
the four nonloop labels.  The last two coefficient entries of their sum
rows are

```text
Q_0: (lambda_0,lambda_0^2),
Q_i: (lambda_i,lambda_i^2).                        (KBPCU-1)
```

The product rows have zero in those entries.  Therefore the image `q_i` of
`Q_i` in `F^8/rowspan(B)` can vanish only if the two vectors in
`(KBPCU-1)` are proportional.  Their determinant is

```text
lambda_0 lambda_i (lambda_i-lambda_0) != 0.        (KBPCU-2)
```

Hence all four quotient images are nonzero everywhere.  The all-zero
branch `Z` of the pivot-chart theorem is empty.  On every common Vieta
survivor, whose full common matrix has rank at most seven, each nonloop row
raises the base rank from six to seven.  Consequently

```text
rank(common matrix)=7,                             (KBPCU-3)
```

its coefficient kernel is one-dimensional, and the survivor lies in all
four pivot charts simultaneously.  Thus the forms `A_2,A_0,B_1` are unique
up to one common nonzero scalar before outside rows are appended.

This theorem does not solve a pivot chart, prove leading support for an
arbitrary algebraic chart point, append an outside row, delete
`433-1a -> O0b`, close positive coordinate parity, K3, a Prize row, or
either Prize result.

## Falsifier

An admissible matching-cell point with `rank B<6`, a nonloop quotient image
equal to zero, or a rank-at-most-seven common survivor with kernel dimension
other than one.
