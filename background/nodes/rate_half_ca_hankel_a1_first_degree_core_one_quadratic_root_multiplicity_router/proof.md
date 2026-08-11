# Proof

The core-one scalar degree-two heavy-incidence identity is

```text
I_H+O=e-6.                                           (1)
```

Subtracting `(1)` from `2Delta=2e-4` proves `u+v=e+2`. The bounds
`u,v<=Delta` give `u>=4` and `O=Delta-v=u-4`. The ordinary-incidence charge
from the local cube theorem gives `I_0<=u`.

Write `I_E=I_H-I_0`. Since each row `x in E` contains `e-c_x`
distinguished incidences,

```text
I_E=r e-C_E=Delta-u-I_0=e-2-u-I_0.                  (2)
```

Solving `(2)` gives `(QRM3)`.

Let `C_tot` be the total excess-recurrence degree and let `t_tot` be the
number of its distinct roots outside the minimal locators. The omission
identity gives

```text
t_tot=C_tot-O.                                       (3)
```

The excess degree used on `E` is `I_E+epsilon_E`. The degree outside `E`
is therefore `C_tot-I_E-epsilon_E`, and it contains at most that many new
distinct roots. Hence

```text
t_E>=t_tot-(C_tot-I_E-epsilon_E)
   =I_E+epsilon_E-O
   =e+2-2u-I_0+epsilon_E,                            (4)
```

proving `(QRM4)`.

Fix a simple heavy residual-root row. At a distinguished incidence write
`r_gamma=1+s_gamma` for its excess multiplicity and let `b_gamma` indicate
overlap with the squarefree minimal locator. The horizontal multiplicity is
`m_gamma=b_gamma+r_gamma`. The simple-root cube identity is

```text
m_gamma+n_gamma=0 mod 3.                             (5)
```

Every supported point contributes at least one vertical degree. A new
point with `s_gamma=0` contributes at least two, and at most
`epsilon_x=sum s_gamma` new points can avoid that second unit. Thus the
supported vertical degree is at least

```text
(e-c_x)+max(t_x-epsilon_x,0).                        (6)
```

The complete fibre has degree `e`, so `(6)` gives `(QRM5)`.

If all rows in `E` are simple, sum `(QRM5)` and combine it with
`(QRM3),(QRM4)`:

```text
e+2-2u-I_0+epsilon_E
 <=t_E
 <=C_E+epsilon_E
 =(r-1)e+2+u+I_0+epsilon_E.                         (7)
```

Canceling common terms gives the first inequality in `(QRM6)`; the second
uses `I_0<=u`.

Now assume `5u<e`. Equation `(2)` and `I_0<=u` imply `I_E>0`, so at least
one residual root is heavy. If the quadratic is squarefree and only one
root is heavy, then `r=1` and `(QRM6)` gives `e<=5u`, a contradiction.
Thus both simple roots are heavy. If the quadratic is not squarefree, its
unique double root must be heavy because `I_E>0`. These are exactly the two
patterns in `(QRM8)`.

For the official `e=183251937963`, the integers satisfying `5u<e` are
`u<=36650387592`, proving `(QRM9)`. QED.
