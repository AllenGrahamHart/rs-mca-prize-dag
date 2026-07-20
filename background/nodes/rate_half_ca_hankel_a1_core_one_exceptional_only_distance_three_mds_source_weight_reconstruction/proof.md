# Proof

Taking the top `X`-coefficient in the pair-Lagrange formula gives `(SWR3)`,
because `A` has degree `r-1` and every `B A/D_i` is monic of degree `r`.

Fix an external slope `z`. Its monic locator is

```text
G_z(X)=Q(z;X)/(z q_bar(z)).                           (1)
```

The pair-Lagrange identity at a triple point gives

```text
G_z(t)/A(t)=Phi(z)/(z q_bar(z)).                     (2)
```

In the minimum-weight escape proof, the circuit scalar `Lambda_z` is
characterized by

```text
G_z(t)/A(t)=Lambda_z/(z Theta_2).                    (3)
```

Equations `(2)--(3)` prove `(SWR7)`.

Now let `a` belong to the pair indexed by `i`. Evaluation of the
pair-Lagrange formula at `a` leaves only one summand:

```text
Q(z;a)=z B(a)(lambda_i/xi_i)L_i(z)(A/D_i)(a).        (4)
```

Therefore

```text
G_z(a)=
 B(a)(lambda_i/xi_i)L_i(z)(A/D_i)(a)/q_bar(z).       (5)
```

The minimum-weight circuit is supported on the roots of
`A B G_z`. Its coefficient at `a` is

```text
Lambda_z/(A'(a)B(a)G_z(a)).                          (6)
```

Substitute `(SWR7)` and `(5)` into `(6)`. The factors `q_bar(z)` cancel,
leaving

```text
Theta_2 Phi(z) /
 (A'(a)B(a)^2(lambda_i/xi_i)L_i(z)(A/D_i)(a)).       (7)
```

By `(SWR1)`,

```text
Phi(z)/L_i(z)=(Delta_i/Delta_0)(z-xi_i).             (8)
```

Equations `(7)--(8)` give `K_a(z-xi_i)`. On the canonical source side this
circuit coefficient is `beta_a+z alpha_a`, so equality at any two external
slopes gives `(SWR6)`. There are `3e>=3` external slopes, and all displayed
expressions are already identities in `z`; hence

```text
alpha_a=K_a,       beta_a=-xi_iK_a.                  (9)
```

All factors in `(SWR4)` are nonzero: the roots and pairs are distinct,
`xi_i` and `lambda_i` are nonzero, and `A,B` have disjoint squarefree root
sets.

The triple coefficients are the barycentric weights from the quotient-
distance theorem. Combining them with `(9)` proves both source formulas in
`(SWR5)`. Uniqueness follows from Vandermonde independence of the `r-1`
exceptional columns for `h_0` and the `r+2<=2r+1` columns on `R_A union T`
for `h_1`.

## Contracted Hankel converse

Now start with pair-Lagrange data having the required external split fibers
and define the moments by `(SWR5)`. At an external slope, equations
`(SWR4)--(SWR7)` say that the canonical coefficients on `R_A union T` are
exactly the restriction of the unique minimum-weight circuit on
`R_A union T union G_z`. Moving its `G_z` part to the other side represents
`h(z)` on the `r` roots of `G_z`. Hence `Q(z;X)` annihilates the moment
sequence at every one of the `3e` external slopes.

Each coordinate of `M(z)q(z)` is a polynomial in `z` of degree at most
`e+1`: the moment pencil is affine and `q` has degree `e`. Since

```text
3e>e+1       for every e>=1,
```

all coordinates vanish identically. This proves `(SWR8)`.

At `z=0`, formula `(SWR5)` has exactly the `r-1` roots of `A` as its source
support, with all weights nonzero. At `z=xi_i`, `(SWR6)` deletes exactly the
two roots in pair `i`, while the other `r-3` exceptional roots and all three
triple roots have nonzero coefficients. At an external slope the circuit
representation on `G_z` has `r` nonzero coefficients. Vandermonde
factorization of the Hankel matrices therefore gives ranks `r-1,r,r` in the
three cases.

Over `F(z)`, the symmetric matrix `M` has rank `r` and primitive kernel
vector `q`. Thus

```text
adj M=s(z)q(z)q(z)^T                                 (10)
```

for a polynomial scalar `s`. Every `r x r` cofactor has parameter degree at
most `r=2e+1`, while `q q^T` has degree `2e`; hence `deg s<=1`. The
exceptional rank is `r-1`, so every cofactor vanishes at zero. Some
coordinate of `q(0)` is nonzero, forcing `s(0)=0`. Since the generic rank is
`r`, `s` is nonzero, and `(10)` becomes `(SWR9)`.

Finally, the first coefficient of `(SWR8)` gives
`M_0q_1+M_1u=0`. Pairing with the two exceptional kernel shifts gives the
two zero pairings. If the remaining `v^TM_1v` also vanished, the first-order
restriction of `M_1` to the exceptional kernel plane would be zero and every
cofactor would vanish to order at least two, contradicting the exact linear
factor in `(SWR9)`. Thus the final pairing is nonzero and the full
transversality gate follows. QED.
