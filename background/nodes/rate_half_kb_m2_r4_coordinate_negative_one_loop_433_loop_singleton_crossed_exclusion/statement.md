# KoalaBear m2 r4 coordinate negative one-loop 433 crossed loop-singleton exclusion

- **status:** PROVED
- **scope:** common matching cells `1,2` of the negative one-loop `(4,3,3)`
  skeleton, in all eight cell/root-sign rows
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate` and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_product_q_weld`
- **consumer:** `rate_half_band_closure`

Use the products and sums

```text
(-1,b,c,bc,-bc),       (0,1+b,1+c,b+c,b-c).       (KB431X-1)
```

The loop is the singleton.  Cell `1` has source antipodal pairs
`AB:BC+` and `AC:BC-`; cell `2` has `AB:BC-` and `AC:BC+`.

In every root-sign row, remove only explicit source/target guard factors
from the two one-loop q welds.  Both residual equations are linear in the
remaining root parameter `r`, and their direct resultant is, up to a
nonzero field scalar,

```text
epsilon_1=epsilon_2:       b(c^2-1),
epsilon_1!=epsilon_2:      c(b^2-1).               (KB431X-2)
```

The products are injective and the target signed pairs are distinct, so
`b,c` are nonzero and `b^2,c^2` are not one.  Every factor in `(KB431X-2)`
is therefore forbidden.  Cells `1,2` are empty before either product minor
or any outside record is used.

This theorem does not delete the other thirteen one-loop 433 matching
cells, build an outside skeleton, treat zero-loop or another parity, close
the coordinate orientation, close a Prize row, or prove either Prize
result.

## Falsifier

A guarded root-sign row whose stripped q equations are not linear, whose
resultant is not `(KB431X-2)`, or which has a simultaneous q-weld root.
