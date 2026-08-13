# Proof

The split-biform interpolation identity gives, for every `y in U_0`,

```text
Lambda(t)G(t,y)=L'(y)omega_y(t)Q(t,y).             (1)
```

For `0<=i<=d`, consider

```text
A_i(Y)=[Y^iG(t,Y)-x_*^iG(t,x_*)]/(Y-x_*).         (2)
```

This is a polynomial in `Y`, and

```text
deg_Y A_i<=i+p-4<=3p-5=n_0-3.                    (3)
```

The Lagrange leading-coefficient identity therefore gives

```text
sum_(y in U_0) A_i(y)/L'(y)=0.                    (4)
```

Also, evaluation of the constant polynomial `1` at `x_* notin U_0`
gives

```text
sum_(y in U_0)1/[(x_*-y)L'(y)]=1/L(x_*).          (5)
```

Expanding `(4)` and using `(5)` yields the exact barycentric sum

```text
sum_(y in U_0)y^iG(t,y)/[L'(y)(y-x_*)]
 =-x_*^iG(t,x_*)/L(x_*).                          (6)
```

Let

```text
U(t,X)=[Q(t,X)-Q(t,x_*)]/(X-x_*),
F_i(t)=sum_(y in U_0)omega_y(t)y^iU(t,y).          (7)
```

Substitute `(1)` into `(7)`, apply `(6)`, and use the definition of
`D_i`:

```text
F_i=-Lambda x_*^iG(t,x_*)/L(x_*)+Q(t,x_*)D_i.
                                                               (8)
```

Use `Lambda=J_*Lambda_0`, `g_*=J_*g_off`, and the two factorizations in
`(DCF1)`. They give

```text
F_i=H_NR[-Lambda_0 x_*^iT_(2+d_A)/L(x_*)
          +a_QS_B^2D_i].                           (9)
```

Equation `(9)` proves the common divisibility directly. Define `C_i` by
`F_i=H_NRC_i`; cancellation in the polynomial ring proves `(DCF4)`.

Each source weight is parameter-linear, so `deg_t D_i<=1`. Moreover,

```text
y^(i+1)/(x_*-y)=x_*y^i/(x_*-y)-y^i,               (10)
```

which proves the recurrence in `(DCF3)` after summing against `omega_y`.
The identity for `D_0` is immediate from

```text
B(t,X)=sum_y omega_y(t)L(X)/(X-y).                 (11)
```

Finally, `deg Lambda_0=3-d_A`, `deg T_(2+d_A)=2+d_A`,
`deg S_B^2=4`, and `deg D_i<=1`, so `(DCF4)` proves the quintic cap.
Substituting `(DCF3)` proves the recurrence in `(DCF5)`. At `tau`, the
`S_B^2D_i` term vanishes, while
`Lambda_0(tau)T_(2+d_A)(tau)L(x_*)` is nonzero. This proves the last line
of `(DCF5)`. QED.
