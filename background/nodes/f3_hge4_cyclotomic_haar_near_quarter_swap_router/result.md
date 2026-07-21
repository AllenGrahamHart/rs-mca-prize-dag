# Result

For `h=m/4-d`, the official prime-size condition first bounds the squared
antipodal defect by

```text
L<4(d+1)log m.
```

Put `X=4(d+1)log m` and let `B` be the least power of two at least `X`.
Iterating the cyclotomic norm argument through dyadic Haar collapses forces
`L=0` whenever

```text
B<h,       BX<m^(1-(4d+8B)/m).
```

The convenient closed-form condition

```text
64(d+1)^2(log m)^2<m.
```

implies this exact test. Thus the free-stabilizer HGE4 class is absent in the
exact band. Even widths are empty, while odd widths route exactly to the
existing half-order perfect-square support problem. The exact band begins at
`m=2^15`, contains
`1<=d<=2` there, and contains `9223` widths at `m=2^41`. The closed-form
sub-band contains `6521` top-level widths.

The result does not count those odd swap supports or settle the deeper
lower-quarter aggregate.
