# KoalaBear m2 r4 coordinate negative one-loop 442 nonloop-singleton cubic-root gate

- **status:** PROVED
- **scope:** the one-loop `(4,4,2)` common-`K` matching orbit in which an
  `AC` record is the singleton, the loop is paired with one `AB` record,
  and the other `AB` record is paired with the other `AC` record
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate` and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_product_q_weld`
- **consumer:** `rate_half_band_closure`

Normalize one cell by

```text
(x_L,x_AB+,x_AB-,x_AC+,x_AC-)=(1,epsilon_1*i,r,t,epsilon_2*i*r),
i^2=-1,                  epsilon_1,epsilon_2 in {+1,-1}. (KB41C-1)
```

Thus the labels and products are

```text
(1,-1,r^2,t^2,-r^2),       (-b^2,b,-b,c,-c).     (KB41C-2)
```

Every guarded common-`K` solution satisfies

```text
P_(epsilon_1,epsilon_2)(r)=0,                    (KB41C-3)

P_(e1,e2)(R)=R^3+(2e1e2+e1*i)R^2
                   +(-1-2e2*i)R-e1*i.
```

Moreover, with `x=r^2`, put

```text
A=x^2-6x+1,        B=(x+1)^2.
```

The same product equation has no guarded denominator branch and determines

```text
c=b(bA+B)/(bB+A).                                 (KB41C-4)
```

Target representative swaps carry the normalized cell and its four root
signs over the four-cell orbit `[9,10,12,13]`.  Thus the orbit is reduced to
at most three `r` values in each sign class before applying the second
product equation and q weld.

The orbit is not deleted.  A guarded full common-`K` witness exists over
`F_41`, so the remaining equation pair and the outside fibers are genuine
work.  This theorem does not classify those roots, impose outside products,
handle another common orbit, close the coordinate orientation or a row, or
prove either Prize result.

## Falsifier

A guarded common-`K` solution in the orbit with
`P_(epsilon_1,epsilon_2)(r)!=0`, a guarded solution on the excluded
denominator branch, or a sign/cell class not covered by the normalization.
