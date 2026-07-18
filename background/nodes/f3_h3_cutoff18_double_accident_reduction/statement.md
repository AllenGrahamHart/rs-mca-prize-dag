# C36' cutoff-18 double-accident reduction

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half`

Let `A=(1-H)\{0}` on an official row, so `|A|=n-1`, and put

```text
P(t)=#{(a,b) in A^2:ab=t},
R(t)=#{(c,d) in A^2:d/c=t},
Q_18(t)=max(P(t)-18,0).
```

Define

```text
X_18 = sum_(t!=1) Q_18(t)R(t),
A_18 = sum_(t!=1,R(t)>0) Q_18(t),
Y_18 = sum_(t!=1) Q_18(t)max(R(t)-1,0).
```

Then

```text
X_18=A_18+Y_18,                         (DA1)
A_18<=(n-1)^2.                          (DA2)
```

Consequently either estimate

```text
17Y_18 <= 283n^2+34n-17,                (DA3)
Y_18 <= 16n^2                            (DA4)
```

implies the critical C36' target

```text
17X_18<=300n^2.                          (DA5)
```

The exact residual budget is `(DA3)`; `(DA4)` is a convenient stronger
integer target with more than `11n^2` slack.

By nonidentity quotient uniqueness in characteristic zero, the factor
`max(R(t)-1,0)` removes the unique characteristic-zero quotient
representation. Thus every positive record in `Y_18` requires both a rich
finite-characteristic product fiber and an additional finite-characteristic
quotient collision. This interpretation uses
`f3_h3_shifted_product_sidon`; identities `(DA1)--(DA5)` are elementary.

This node does not bound `Y_18` and does not close C36'.
