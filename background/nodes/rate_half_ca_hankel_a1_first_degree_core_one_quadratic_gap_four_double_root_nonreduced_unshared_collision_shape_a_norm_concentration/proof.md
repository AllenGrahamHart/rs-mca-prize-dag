# Proof

The complete companion exclusion leaves shape A, so `G` itself is the
single factor with parameter degree `m=e-2`. For each classified row
`x in U_0`, row saturation gives exactly `m` distinct roots in `Gamma`.
Therefore, multiplying the actual-support factors over all slopes gives

```text
product_(delta in Gamma)A_delta(X)=L_U0(X)^m.       (1)
```

The extremal three-center ledger gives

```text
sum_(all supported delta)r_delta=e-6,
sum_(delta in Gamma)a_delta=e.                     (2)
```

In the present `d_A=1` branch, the three line slopes consume exactly one
unit of padding. Hence

```text
sum_(delta in Gamma)r_delta=e-7.                   (3)
```

The center-adjusted heavy-row theorem supplies a squarefree degree-`e-7`
form `g_off`. Its roots are distinct slopes in `Gamma`, and at every one of
them `x_*` is a root of the corresponding monic padding factor `R_delta`.
Thus the product of all `R_delta` is divisible by `(X-x_*)^(e-7)`. Its
degree is exactly the left side of `(3)`, so monicity proves

```text
product_delta R_delta=(X-x_*)^(e-7).               (4)
```

Now multiply the all-excess identities `(SNC2)` over `Gamma`. Equations
`(1)` and `(4)` give

```text
product_delta G(delta,X)
 =c L_U0(X)^m(X-x_*)^(e-7) product_delta H_delta(X) (5)
```

for `c=product_delta zeta_delta!=0`. This proves `(SNC3)--(SNC4)` with
`T=product H_delta`.

The fiber-degree ledger says

```text
q_delta=a_delta-deg H_delta.                       (6)
```

Summing `(6)` and using `(2)` proves

```text
deg T=sum_delta deg H_delta
     =e-sum_delta q_delta<=e.                      (7)
```

The off-line norm theorem says that its quotient after removing
`L_U0^m` is coprime to `L_U0`. Since `x_* notin U_0`, equation `(5)` then
implies `gcd(T,L_U0)=1`.

Finally, at `x in U_0` the norm theorem gives

```text
[c(X-x_*)^(e-7)T(X)]_(X=x)
       =D_x(G)/L_U0'(x)^m.                         (8)
```

All denominators in `(SNC6)` are nonzero. Solving `(8)` proves that formula.
The official count `(9e-7)/2` is strictly larger than `e`, so Lagrange
interpolation on `U_0` reconstructs `T` uniquely. QED.
