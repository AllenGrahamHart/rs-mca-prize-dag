# Proof

For every root `x` of `P_X`, the exact incidence design gives precisely `e`
supported roots of the degree-`e` parameter polynomial `Q(z;x)`:

- at an exceptional root, they are `z=0` and all internal slopes except the
  slope cancelling its pair;
- at a triple point, they are all internal slopes;
- at any other saturated row, they are its `e` external incidences.

All roots are simple. Hence

```text
Q(z;x) divides P(z)                                  (1)
```

for every root `x` of `P_X`, and the quotient has parameter degree `3e+1`.
Interpolate each quotient coefficient over the `8e+6` distinct roots of
`P_X`. This gives `V` with the first line of bounds in `(CSC3)`. The biform
`P-QV` vanishes on every root of `P_X`, so it is divisible by `P_X`; define
`W=(P-QV)/P_X`. Its `X`-degree is at most

```text
r+(8e+5)-(8e+6)=r-1.                                (2)
```

This proves the first equation of `(CSC2)`.

At each root `z` of `P_cl`, the ordinary split locator `Q(z;X)` has `r`
roots, all among the roots of `P_X`. Thus

```text
Q(z;X) divides P_X(X),                               (3)
```

with quotient degree `8e+6-r=6e+5`. Interpolate the quotient coefficients
over the `4e` ordinary slopes. This gives `A_c` with the second line of
bounds in `(CSC3)`. The biform `P_X-QA_c` vanishes at every root of `P_cl`,
so division by `P_cl` defines `B_c` and proves the second equation of
`(CSC2)`. Since

```text
deg_z(QA_c)<=e+(4e-1),
```

the quotient has parameter degree at most `e-1`, as claimed.

The primitive generator `Q` is coprime to `P_cl`: a common factor would be
one of the ordinary-slope linear factors and would make the corresponding
nonzero split fiber vanish identically. Substitute the second equation of
`(CSC2)` into the first:

```text
Q(V+A_cW)=P_cl(z-B_cW).                              (4)
```

Coprimality shows that `Q` divides `z-B_cW`. Define

```text
K=(WB_c-z)/Q.                                        (5)
```

Equation `(4)` then gives `V+A_cW=-P_clK`. Using
`z=WB_c-QK` and the second equation of `(CSC2)`,

```text
V B_c+z A_c
 =B_c(V+A_cW)-Q A_cK
 =-(P_clB_c+QA_c)K
 =-P_XK.                                             (6)
```

This proves both weld identities.

The unique omitted row has no supported incidence, while the exceptional
fiber is the squarefree degree-`r-1` polynomial `A` and its roots are all
saturated. Therefore `(CSC2)--(CSC4)` is exactly the `b=0,D_*=1,c=z=1`
exceptional-only active system consumed by the proved factor-descent chain.
Applying that chain gives the corrected square and all later reciprocal
identities. QED.
