# Locator-extension kernel reduction

- **status:** PROVED
- **closure:** dual Reed-Solomon interpolation criterion
- **consumer:** `rate_half_band_crossing_location`

Use the deficiency-aware notation `(DCK1)--(DCK6)`. Let `a=|W|`,

```text
sigma_W(X)=product_(x in W)(X-x),
Q_Y(x)=A_x(Y)R_x(Y),
R_x(Y)=sum_(t=0)^Delta_x r_(x,t)Y^t.                 (LEK1)
```

The locator curve has `X`-degree at most `rho`. Therefore, for every
parameter coefficient `0<=j<=m`, the values

```text
q_j(x)=[Y^j]Q_Y(x)
```

on `W` must extend to a polynomial of `X`-degree at most `rho`.

Define the locator-extension matrix `E_W` with the same columns `(x,t)` as
`M_W`, rows

```text
0<=i<a-rho-1,       0<=j<=m,
```

and entries

```text
E_W[(i,j),(x,t)]
 =x^i/sigma'_W(x) [Y^j](A_x(Y)Y^t).                 (LEK2)
```

If `a<=rho+1`, the row set is empty. Otherwise,

```text
E_W r=0                                                (LEK3)
```

is equivalent to coefficientwise extension of `(LEK1)` by polynomials
`q_j(X)` of degree at most `rho`.

Consequently every actual strict-endpoint failure supplies a blockwise
nonzero kernel vector for the strengthened matrix

```text
C_W = vertical_stack(M_W,E_W).                        (LEK4)
```

Full column rank of `C_W` excludes the failure pattern.

## Scope

The extension equations are necessary and exact on `W`. They do not enforce
the root sets of `Q_gamma` outside `W`, exact supported-slope cardinality,
Hankel rank, or column-farness. A kernel of `C_W` is still not by itself an
official pencil witness.
