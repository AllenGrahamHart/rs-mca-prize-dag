# Codimension-three sparse circuits satisfy a completion dichotomy

- **status:** PROVED
- **ambient space:** `P_13=F[X]_<13`
- **correction dimension:** `10`
- **quotient dimension:** `3`
- **counted unit:** full-rank eleven-sets in one selected record support

Let `V<=P_13` have dimension ten and empty global common zero set on a set
`S` of `m` distinct field points.  Put `Lambda=V^perp`.  For every eleven-set
`T subset S` with `rank(ev_T|V)=10`, the line

```text
Lambda intersect E_T,       E_T=span{ev_x:x in T},
```

selects one circuit support `C_T`; write `c_T=|C_T|`.

For circuits with `2<=c_T<=5`, one of the following holds.

1. **Structured carrier.** Every such circuit support lies in one set `U`
   with `|U|<=7`.
2. **Two-completion branch.** Every independent `(c-1)`-set has at most two
   points which complete it to a support-`c` circuit, for every `2<=c<=5`.

Consequently the number of full-rank eleven-sets with `c_T<=5` is at most

```text
max{
  sum_(c=2)^5 C(7,c) C(m-c,11-c),
  sum_(c=2)^5 floor(2 C(m,c-1) C(m-c-1,11-c)/c)
}.                                                        (C3C)
```

At `m=67485`, the structured and two-completion caps are respectively

```text
1679076702065233864778823429158845084750,
99254447944649683780146155758753837527116020.
```

Thus the official per-record sparse-circuit cap is the second number.

## Falsifier

A support-one circuit despite the empty common zero set; four circuit
completions of one independent set; three completions which do not force all
sparse quotient labels into their carrier; a full-rank eleven-set containing
two completion labels; or a failure of the exact count `(C3C)`.
