# Proof

The core-free scalar incidence identity at `a=3` is

```text
I_H+O=3e-3.                                          (1)
```

Since `Delta=2e-1`, subtracting `(1)` from `2Delta` gives `(CRM2)`.
The triple-tangency budget gives `I_0<=u`.

Write `I_E=I_H-I_0`. Every row `x in E` has `e-c_x` distinguished
incidences, so

```text
I_E=r e-C_E=Delta-u-I_0.                             (2)
```

Solving `(2)` proves `(CRM3)`.

Let `C_tot` be the total excess-recurrence degree and let `t_tot` be the
total number of its distinct roots outside the minimal locators. Fibrewise
omission accounting gives

```text
t_tot=C_tot-O.                                       (3)
```

The excess degree used on `E` is `I_E+epsilon_E`. Hence the degree outside
`E` is `C_tot-I_E-epsilon_E`, and it can contain at most that many new
distinct roots. Therefore

```text
t_E>=t_tot-(C_tot-I_E-epsilon_E)
   =I_E+epsilon_E-O
   =v-u-I_0+epsilon_E
   =e+1-2u-I_0+epsilon_E,                            (4)
```

which is `(CRM4)`.

Now fix a simple heavy root row. At one of its distinguished incidences,
write `r_gamma=1+s_gamma` for the excess multiplicity. If the root overlaps
the minimal locator, its horizontal multiplicity is `2+s_gamma`; if it is
new, the multiplicity is `1+s_gamma`. For a simple residual root the local
cube identity says

```text
m_gamma+n_gamma=0 mod 3.                             (5)
```

Every supported point contributes at least one vertical degree. A new point
with `s_gamma=0` contributes at least two. At most `epsilon_x=sum s_gamma`
new points can avoid that second unit. Thus the supported part of the
vertical fibre has degree at least

```text
d_x+max(t_x-epsilon_x,0).                            (6)
```

Its complete degree is `e`, while `d_x=e-c_x`. Equation `(6)` gives
`t_x<=c_x+epsilon_x`, proving `(CRM5)`.

If every row in `E` is a simple residual root, sum `(CRM5)` and combine it
with `(CRM3),(CRM4)`:

```text
e+1-2u-I_0+epsilon_E
 <=t_E
 <=C_E+epsilon_E
 =(r-2)e+1+u+I_0+epsilon_E.                          (7)
```

Canceling common terms gives the first inequality in `(CRM6)`. The second
uses `I_0<=u`.

If `R_3` has a triple root, it has at most one distinct heavy root. Hence
`I_E<=e-1`. Using `(2)` gives

```text
2e-1-u-I_0<=e-1,
e<=u+I_0<=2u,                                        (8)
```

which proves `(CRM7)`.

Finally assume `5u<e`. Equation `(2)` and `I_E<=r(e-1)` rule out `r<=1`.
If `R_3` is squarefree, every heavy root is simple; `(CRM6)` rules out
`r=2`, so all three roots are heavy. If `R_3` is not squarefree, `(CRM7)`
rules out a triple root, leaving a double root and a simple root. Since
`r>=2`, both are heavy. This proves `(CRM9)`. QED.
