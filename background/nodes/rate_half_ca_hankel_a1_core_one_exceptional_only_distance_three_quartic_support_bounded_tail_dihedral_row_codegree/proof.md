# Proof

The normalized pair-Lagrange formula is

```text
q_x(z)=Phi(z)+zB(x) sum_i alpha_i L_i(z)/D_i(x).    (1)
```

Fix a nonfixed outside orbit `{x,y}`. For a good pair locator, the two orbit
values satisfy

```text
D_i(y)=D_i(x)                         if y=-x,
D_i(y)=cD_i(x)/x^2                    if y=c/x.      (2)
```

With `(QBT3)--(QBT4)`, equation `(1)` therefore becomes

```text
q_x=Phi+z beta_x(G_x+T_x),
q_y=Phi+z beta_y(G_x+T_y),             (3)

G_x=sum_(i in G) alpha_iL_i/D_i(x),
T_x=sum_(j in T) alpha_jL_j/D_j(x),
T_y=sum_(j in T) alpha_jL_j/Dhat_j(y). (4)
```

At a common external root, `z` is nonzero and neither an internal slope nor
a zero of `Phi`. Eliminating `G_x` from the two equations in `(3)` gives
exactly

```text
(beta_x-beta_y)Phi+z beta_x beta_y(T_y-T_x)=0,      (5)
```

which is `(QBT5)`. The same implication remains valid when
`beta_x=beta_y`, without division by their difference.

At every good internal slope `xi_i`, both terms in `(QBT5)` vanish: `Phi`
vanishes there, and every tail Lagrange polynomial `L_j` does as well.
The roots are distinct, so `I_G|H_(x,y)`. Both `Phi` and every `zL_j` have
degree at most `e`, while `deg I_G=e-t`. This proves `(QBT6)`. External
slopes are disjoint from the roots of `I_G`; if `H_(x,y)` is nonzero, its
common external roots are therefore among the at most `t` roots of
`h_(x,y)`.

It remains to classify `H_(x,y)=0`. The polynomials

```text
Phi,       {zL_j:j in T}                             (6)
```

are linearly independent because they are a subset of the pair-Lagrange
parameter basis. Every displayed scalar is nonzero on an outside orbit.
Thus vanishing of `(QBT5)` forces

```text
beta_x=beta_y,
D_j(x)=Dhat_j(y)       for every j in T.             (7)
```

Equations `(2)` and `(7)` make every coefficient in `(3)` equal, so
`q_x=q_y` identically.

There is at most one such nonfixed orbit. In the antipodal case

```text
B(x)-B(-x)=2x(x^2+sigma_2),                          (8)
```

so `beta_x=beta_y` fixes the orbit coordinate `x^2=-sigma_2`. In the
constant-product case, division by the nonzero orbit members gives

```text
B(x)/x-B(c/x)/(c/x)
 =(x-c/x)(x+c/x-sigma_1+sigma_3/c).                 (9)
```

The nonfixed condition removes the first factor and fixes the unique orbit
coordinate in `(QBT7)`. The additional tail equations in `(7)` can only
remove that orbit, not create another. QED.
