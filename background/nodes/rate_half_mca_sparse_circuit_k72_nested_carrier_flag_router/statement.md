# K'=72 nested-carrier flag router

- **status:** PROVED
- **row:** `K'=72`, `q=62`
- **active maxima:** `(M_2,M_3,M_4,M_5)=(28,30,31,31)`

Let `B_c` be attaining support-`c` carriers in a ten-dimensional correction
space. Assume the support-two projective point is in the full-completion
position for supports three, four, and five, and assume the maximal overlap
positions

```text
B_3 subset B_4,       B_3 subset B_5.
```

Then

```text
|B_2|=29, |B_3|=32, |B_4|=34, |B_5|=35.
```

Put `R_4=B_4\B_3` and `R_5=B_5\B_3`, so `|R_4|=2` and `|R_5|=3`.
Exactly one of the following occurs.

1. `|R_4 intersect R_5|=2` is impossible.
2. `|R_4 intersect R_5|=1` and the common point is outside `F_3`. Then
   `F_4<=F_5`, and the six-dimensional space `H_5` vanishes on the
   36-point union `B_4 union B_5`.
3. `|R_4 intersect R_5|=1` and the common point lies in `F_3`. Then the
   eight-dimensional `H_3` vanishes on a 33-point extension of `B_3`, while
   the at-least-five-dimensional `H_4 intersect H_5` vanishes on the
   36-point union.
4. `R_4 intersect R_5` is empty. Then `H_4 intersect H_5` has dimension at
   least five and vanishes on a 37-point union. If `F_4<=F_5`, its dimension
   improves to six.

At the active cap vector, the nested `(36,6)` and `(37,6)` alternatives pay
the row. The nonnested `(37,5)` alternative misses by
`56143372060369458527589387786047131157221610` premium units. The
33/36 flag alternative is the leading unresolved carrier case.

## Falsifier

A 35-point nested union; a one-point residual overlap outside `F_3` without
`F_4<=F_5`; a wrong fixed union size or correction dimension; or a replayed
premium different from the printed exact values.
