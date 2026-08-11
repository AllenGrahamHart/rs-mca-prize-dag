# Proof

Let `b` be the point of the normalized curve over a root `tau` of `S_B`
on the correction divisor `B`. The separated heavy-quotient theorem uses
the exact divisor identities

```text
ord_b(X-x_*)=3,
ord_b(P_F|_C)=ord_b(s_F)=2.                         (1)
```

The second equality is valid at the finite heavy row because the fixed
domain-infinity factor relating `P_F|_C` and `s_F` is a unit there. Since
`S_B` is squarefree, `tau` is a simple parameter value at `b`.

Restrict the Pade syzygy to `Q=0`:

```text
-Lambda G=L_U0 P_F.                                (2)
```

The heavy row is external to `U_0`, so `L_U0(x_*)` is a unit at `b`. More
explicitly, the nonempty form `g_*` cuts out slopes where `x_*` is a
padded-heavy root, and the paired fiber theorem puts every padding root
outside `U_0`.
Moreover, a correction root is disjoint from `g_*`, and the three center
factors in `Lambda` are simple. Therefore `(1),(2)` give

```text
ord_b(G|_C)=2-c_tau.                               (3)
```

For a polynomial `V(t,X)`,

```text
G(t,X)-G(t,x_*)=(X-x_*)V(t,X).                     (4)
```

Pulling `(4)` to the normalized curve and using `(1)` shows that the moving
curve value and fixed-row value differ only in order at least three. The
order in `(3)` is one or two, so it cannot be changed by that difference.
Because the parameter is unramified at the squarefree correction point,

```text
ord_tau G(t,x_*)=2-c_tau.                          (5)
```

Finally `g_*` is a unit at `tau`, `S_B^2` has order two, and
`J=gcd(Lambda,g_*S_B^2)` has order `c_tau`. Hence

```text
ord_tau H=2-c_tau.                                 (6)
```

Comparing `(5),(6)` in `G=HT_j` gives `ord_tau T_j=0`. This holds at both
roots of the squarefree `S_B`, proving `(HCE3),(HCE4)`. The identity
`R_lambda=G(t,x_*)` for a passing candidate gives the last assertion. QED.
