# Proof

The reciprocal Bezout normalization gives `(QBR1)`, so

```text
l_0P_cl=1-f_0a_minus.                                (1)
```

The triangular reconstruction stage is

```text
C_k^0+l_0P_cl rho_k-f_0s_k=0.                       (2)
```

Reduce `(2)` modulo `f_0`. Equation `(1)` gives

```text
rho_k=-C_k^0 mod f_0.                               (3)
```

The Euclidean division `(QBR2)` makes the canonical representative in `(3)`
equal to `-r_k`, proving the first formula in `(QBR3)`. Substitute
`C_k^0=f_0d_k+r_k`, `rho_k=-r_k`, and `(1)` into the numerator in `(2)`:

```text
C_k^0+l_0P_cl rho_k
 =f_0d_k+r_k+(1-f_0a_minus)(-r_k)
 =f_0(d_k+a_minus r_k).
```

This proves the formula for `s_k`. The preceding triangular theorem says
that a correction exists exactly when the canonical residue has degree at
most one. Since scalar negation preserves degree, this is `(QBR4)`. QED.
