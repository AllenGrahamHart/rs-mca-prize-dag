# KoalaBear m2 r4 coordinate negative one-loop 442 crossed-pair exclusion

- **status:** PROVED
- **scope:** the one-loop `(4,4,2)` matching orbit in which the loop label is
  the singleton and both source antipodal pairs mix an `AB` product with an
  `AC` product
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate` and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_product_q_weld`
- **consumer:** `rate_half_band_closure`

Choose `A=1,B=b,C=c`, `i^2=-1`, and one crossed matching representative

```text
labels:   (t^2,1,r^2,-1,-r^2),
products: (-b^2,b,-b,c,-c).                       (KB41X-1)
```

The complete product gate and two q welds imply

```text
P=b(br+b-ir+i)=0,
Q=c(b(r-1)+i(r+1))=0.                             (KB41X-2)
```

After the guards `bc!=0`, their linear-in-`r` resultant is

```text
Res_r(P/b,Q/c)=-2(b^2-1).                         (KB41X-3)
```

Odd characteristic and target distinctness give `2(b^2-1)!=0`, a
contradiction.  Target representative changes cover both crossed matchings
and every relative square-root sign class.  Hence this entire matching orbit
is empty.

This theorem does not delete the aligned-pair families, classify the other
four matching orbits, handle the one-loop 433 or zero-loop row, close the
coordinate orientation, move an owner/payment, close a row, or prove either
Prize result.

## Falsifier

An admissible crossed-pair common-`K` solution, failure of either ideal
membership in `(KB41X-2)`, or a sign/matching class outside the stated
representative symmetries.
