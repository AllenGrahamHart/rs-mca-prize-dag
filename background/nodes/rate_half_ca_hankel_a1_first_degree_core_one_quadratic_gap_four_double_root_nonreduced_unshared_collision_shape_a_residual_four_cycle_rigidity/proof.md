# Proof

Write the nonreduced correction as

```text
S_B=c ell_tau^2,       g_*(tau)!=0.                  (1)
```

The collision parameter is off the three center lines and `x_*` is not in
`U_0`. Hence `Lambda(tau)` and `L_U0(x_*)` are units. At a point `b` in the
support of `B`, write `m_b` for its coefficient in `B`. The normalized
contact calculation gives

```text
ord_b P_F=2m_b.                                      (2)
```

Restrict the Pade syzygy

```text
Q B_source-Lambda G=L_U0 P_F                         (3)
```

to the locator curve `Q=0`. Equations `(1)--(3)` and the two unit factors
give

```text
ord_b(G|_C)=2m_b.                                    (4)
```

The factorwise Bezout ledger places all four residual intersection units
at this collision, while the exact projective four-core has total degree
four and no loss at infinity. Since `deg B=2`, equation `(4)` accounts for
all four units. Therefore its pullback is

```text
Z_4=sum_b 2m_b b=2B,                                (5)
```

proving `(RFR4)`.

It remains to count sections. Put

```text
E_1=pi_*O_C(B),       E_2=pi_*O_C(2B).
```

Finite pushforward is exact, so `E_2/E_1` is a length-two positive
elementary modification supported at `x_*`. Let `u=X-x_*` be the base
uniformizer. From `(RFR2)`,

```text
u O_C(2B) subset O_C(B).                            (6)
```

Thus `u(E_2/E_1)=0` and

```text
E_1 subset E_2 subset E_1(x_*).                    (7)
```

The modification is represented by the two-dimensional subspace

```text
W=uE_2/uE_1 subset E_1/uE_1.                       (8)
```

Every class in `W` vanishes on the residual fibre divisor `R_*`: its
representatives have poles only along `B`, while multiplication by `u`,
whose divisor contains `R_*`, kills their values there. The constant class
is nonzero at every point of the nonempty divisor `R_*`. Consequently

```text
W intersect k*1=0.                                  (9)
```

Use `(RFR3)` to write `E_1=O direct_sum F`, where

```text
F=O(1-d)^2 direct_sum O(-d)^(e-3).                 (10)
```

Equation `(9)` makes the projection `W -> F|_(x_*)` injective. A bundle
map `F -> O` with prescribed value at `x_*` removes the `O`-components of
`W`. In this changed splitting, `(7)--(8)` give

```text
E_2 subset O direct_sum F(x_*),                    (11)

F(x_*)=O(2-d)^2 direct_sum O(1-d)^(e-3).
```

All summands in `F(x_*)` have negative degree because `d=3e-2>2`.
Therefore `(11)` gives `h^0(E_2)<=1`. The canonical effective-divisor
section of `O_C(2B)` is nonzero, so equality holds. Finite pushforward
preserves global sections, proving `(RFR5)`.

Finally, `(RFR2)` says that `(X-x_*)/s_F` is the canonical section of
`O_C(B)`. Its square spans the one-dimensional space in `(RFR5)`. QED.
