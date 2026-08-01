# KoalaBear m2 r4 coordinate negative one-loop 442 aligned-pair classifier

- **status:** PROVED
- **scope:** the one-loop `(4,4,2)` matching orbit in which the loop label is
  the singleton and each doubled signed product pair occupies one antipodal
  common-`K` pair
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate` and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_product_q_weld`
- **consumer:** `rate_half_band_closure`

Choose target representatives `A=1,B=b,C=c`, let `i^2=-1`, and normalize
the source roots so that

```text
(x_L,x_AB+,x_AB-,x_AC+,x_AC-)=(t,1,i,r,ir).       (KB41A-1)
```

Thus the common labels and products are

```text
(t^2,1,-1,r^2,-r^2),
(-b^2,b,-b,c,-c).                                 (KB41A-2)
```

The complete common-`K` product gate and the two one-loop q welds hold if
and only if one of the following guarded families holds:

```text
A: r^2+r+1=0,       b=ir,       c=ir^2,     t^2=c;
B: ib^2+b-i=0,      c=-1/b,     r=-i/b,     t^2=-b. (KB41A-3)
```

In family A, `r` is a nontrivial cube root.  In family B, the displayed
quadratic selects the two roots of `b^3=i` other than the forbidden
`b=-i` root.  All common labels, target labels, products, and nonloop sums
are distinct/nonzero as required.

Changing either target representative sign normalizes every square-root
sign choice back to `(KB41A-1)`, so `(KB41A-3)` classifies the whole matching
orbit.

This theorem does not delete either family, impose the other seven source
fibers or paired products, classify another one-loop matching orbit, handle
zero-loop or positive parity, close the coordinate orientation, move an
owner/payment, close a row, or prove either Prize result.

## Falsifier

An admissible common-`K` solution in this matching orbit outside the two
families, a guarded failure of either converse, or a square-root sign class
not carried to `(KB41A-1)` by target representative changes.
