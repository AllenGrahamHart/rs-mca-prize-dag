# Cross-type atom-weld gauge dichotomy

- **status:** PROVED
- **scope:** the complete graph of large triple-owner pair types in the
  no-high-complexity branch of the degree-18 atom-weld compiler

For each large type `p`, fix 18 owned anchor records and write its codeword
pair as `(a_p,b_p)`. Pairwise weld packets may be chosen to contain these
fixed anchor records. Their projective atom certificates admit one common
scalar normalization. Write the normalized certificate on edge `{p,q}` as

```text
C_pq=(Q_pq,A_pq,B_pq)
```

and put `T_p=(1,a_p,b_p)` over `F(X)`.

For every triple of distinct types `p,q,r`, there are polynomials
`D_p,D_q,D_r` such that

```text
C_pq-C_pr=D_p T_p,
C_pq-C_qr=D_q T_q,
C_pr-C_qr=D_r T_r,
D_q T_q=D_p T_p+D_r T_r.                            (GD1)
```

Consequently exactly one of the following structural outputs is available.

1. **Global atom.** Some triple has

   ```text
   det(T_p,T_q,T_r) != 0.
   ```

   Then every canonical edge certificate in the complete graph is the same
   normalized atom `C_*`.

2. **Rational pair pencil.** Every triple determinant vanishes, and

   ```text
   rank_(F(X)){T_p:p large} <= 2.                    (GD2)
   ```

The second output is a base pair-type split-pencil target. It is not a
payment. The first output identifies canonical pairwise welds, but does not
yet certify records outside their fixed packets or pay the atom.

## Falsifier

Two incident edge certificates with nonproportional scalar pairs despite
three common fixed anchor locators; failure of `(GD1)`; a nondegenerate
triangle with unequal edge atoms; failure of global propagation from one
nondegenerate triple; or all determinants zero with rational rank above two.
