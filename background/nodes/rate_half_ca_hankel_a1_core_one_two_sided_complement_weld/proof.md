# Proof

The component norm theorem already proves `(TSW3)` and `(TSW5)`. It also
shows that at most one supported slope is deficient, so
`|Z_cl|=T-D_*` and `deg E_Z=D_*`.

For every `gamma in Z_cl`, the squarefree degree-`r` polynomial
`Q(gamma;X)` divides `G_X`. Interpolate the coefficients of

```text
A_gamma(X)=G_X/Q(gamma;X)
```

over the `T-D_*` clean slopes. This gives a biform `A` with parameter degree
less than `T-D_*` and `X`-degree `D_0-r`. The polynomial `QA-G_X` vanishes at
every clean slope, so it is divisible by `P_cl`; choosing the quotient sign
gives `(TSW4)`. Its parameter degree is at most

```text
e_*+(T-D_*-1),
```

so division by `P_cl` leaves parameter degree at most `e_*-1`. Its
`X`-degree is at most `D_0`, proving `(TSW6)`.

Use `P=P_cl E_Z` and `G_X=P_XB_X`. Multiply `(TSW3)` by `B` and `(TSW4)` by
`E_Z`, then eliminate the common term `P_cl B E_Z`. The result is

```text
Q(VB+AE_Z)+P_X(WB-B_XE_Z)=0.                          (1)
```

The irreducible component `Q` has positive parameter degree, so it is
coprime to the `X`-only polynomial `P_X`. Equation `(1)` therefore implies

```text
WB-B_XE_Z=QK
```

for a biform `K`; substitution back into `(1)` gives `(TSW8)`.

The first product in `(TSW7)` has `X`-degree at most
`(r-1)+D_0`, so division by the degree-`r` form `Q` leaves `X`-degree at most
`D_0-1`. Its parameter degree is at most `T+(e_*-1)`, leaving at most `T-1`
after division by `Q`. This proves `(TSW9)`. Finally `c<=C_*` follows because
every nonsaturated component row contributes at least one to `C_*`, and the
component norm theorem gives the expression in `(TSW10)`. QED.
