# Proof

Use the six standard monomials from the sextic quotient classifier.  For an
element `u`, reduce `u` times each basis monomial and use the six coordinate
columns as the multiplication matrix `M_u`.

The parent already gives

```text
det M_(D_c)=2^19.
```

Solve `M_(D_c)[c]=[b(bA+B)]`, where
`A=r^4-6r^2+1` and `B=(r^2+1)^2`.  In the representative row this gives
the coordinate vector

```text
(-1,1,-1/2,(i-1)/4,0,(1-i)/4),
```

which is `(KB41M-2)`.

Substitute that vector into `D_m=b^3-b^2c+3bc+c^2`.  Its multiplication
matrix has determinant `652` in the representative quotient.  Repeating
the same reduction in the other three sign rows gives `652` again.  Since
the deployed prime divides neither `2` nor `163`, `D_m` is a unit in every
row.

Finally solve

```text
M_(D_m)[m]=[-b(b^3+3b^2c-bc+c^2)].
```

The representative coordinate vector is

```text
(50-54i,87+54i,-126-54i,30+12i,-54+54i,12+30i)/163,
```

which proves `(KB41M-3)`.  All operations occur in the exact deployed-field
quotient, so the coordinate identities are certificate equalities, not
numerical approximations. QED.
