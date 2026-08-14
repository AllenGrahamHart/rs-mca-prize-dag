# Proof

The first-degree marked-source frame expands the primitive kernel and its
apolar locator as

```text
q(t)=sum_(i=0)^e t^i q_i,
Qbar(t,X)=sum_(i=0)^e t^i Q_i(X),                  (1)
```

with the `q_i`, equivalently the coefficient polynomials `Q_i`, linearly
independent. The two-slope coefficient-rank theorem uses this same
`Qbar`. Hence

```text
sr(Qbar)=e+1,       deg_X Qbar=d=3e-2.             (2)
```

For every `x in U_0`, the dual-MDS construction defines

```text
H_x(t)=omega_x(t)Qbar(t,x)/Lambda_A(t),
H_x(t)=G(t,x)/L_U0'(x),                             (3)
```

where

```text
Lambda_A=ell_alpha ell_beta ell_theta.             (4)
```

Shape A is the `d_A=1` collision factor shape. The three-center source
partition therefore has no exceptional coordinate and gives `(SRA2)`. If
`x in M_gamma`, its source form is

```text
omega_x(t)=eta_x ell_gamma(t),       eta_x!=0.     (5)
```

Combining `(3)--(5)` gives

```text
Qbar(t,x)=eta_x^(-1)
  product_(gamma' in {alpha,beta,theta}\{gamma})ell_(gamma')(t) H_x(t).
                                                               (6)
```

Let

```text
V=span_F{H_x(t):x in U_0}.                          (7)
```

Evaluation on `U_0` is injective for polynomials in `X` of degree at most
`n`, because `R>n`. Multiplication by the nonzero scalars `L_U0'(x)` does
not change the span. Hence

```text
dim V=sr(G).                                        (8)
```

For each center `gamma`, multiplication by the fixed nonzero quadratic
form in `(6)` maps `V` into a space of dimension at most `dim V`. Since the
three classes partition `U_0`, equation `(6)` yields

```text
dim span_F{Qbar(t,x):x in U_0}<=3 dim V.           (9)
```

Evaluation on `U_0` is also injective through the locator degree, because

```text
R-d=(3e-3)/2>0.                                    (10)
```

Equations `(2),(9),(10)` therefore give

```text
e+1=sr(Qbar)
   =dim span_F{Qbar(t,x):x in U_0}
   <=3sr(G).                                       (11)
```

Taking ceilings proves `(SRA3)`. Substitution of the official value of `e`
gives `(SRA4)`. QED.
