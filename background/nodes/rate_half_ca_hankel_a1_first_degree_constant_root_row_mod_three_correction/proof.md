# Proof

Cancel the heavy-row factor `B` from the scalar ambient identity:

```text
s_F^3 G_L/H=R_a|_C.                                  (1)
```

Fix a heavy root row `x` and let `z>=1` be its multiplicity in `R_a`.
Because `B` is squarefree and contains the row once, `G_L(x)` is nonzero.
It is therefore a unit at every point of the vertical fibre over `x`.

At a supported incidence `gamma`, let `m_gamma` and `n_gamma` be the
horizontal and vertical intersection multiplicities. Taking valuations in
`(1)` gives

```text
3k_gamma=m_gamma+z n_gamma.                          (2)
```

At an unsupported point of the same vertical fibre, `H` is a unit and the
corresponding equation is `3k=z n`.

Sum these equations over the complete vertical fibre. Its vertical degree
is `e`, so modulo three

```text
sum_(supported gamma)m_gamma+z e=0 mod 3.             (3)
```

The official first-degree integer is divisible by three, hence the first
sum in `(3)` is divisible by three.

Every heavy supported incidence belongs to the excess recurrence factor.
The minimal factor is squarefree, so

```text
m_gamma=b_gamma+r_gamma,
sum b_gamma=d_x-t_x,
sum r_gamma=d_x+epsilon_x.                            (4)
```

Using `d_x=e-c_x`, equations `(3),(4)` give

```text
0=sum m_gamma
 =2(e-c_x)+epsilon_x-t_x
 =c_x+epsilon_x-t_x mod 3,                           (5)
```

which is `(RMC3)`. Nonnegativity of `epsilon_x` gives `(RMC4)` and its
three-entry full-overlap table.

Finally, incidences on `E` consume one excess copy each plus the printed
`epsilon_x`. Every ordinary heavy incidence consumes at least two excess
degrees by the triple-tangency theorem. These charges are disjoint inside
the total regular-rank degree, proving `(RMC5)`. QED.
