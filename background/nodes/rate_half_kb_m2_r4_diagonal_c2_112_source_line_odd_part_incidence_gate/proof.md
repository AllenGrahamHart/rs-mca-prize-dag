# Proof

Write the four pure stars over the internal orbit as

```text
e, f, tau(e), tau(f),
```

where `e,f` are the two stars over `z`; individual-star equivariance gives
the other two over `z^(-1)`. The saturated defect classifier leaves at most
one collision among all pure and mixed edges, and its mixed edges are
distinct. Hence the pure-edge collision defect is at most one.

If the internal orbit were the ramified source orbit, its two fibers would
give `e,e` and `tau(e),tau(e)`. Distinct vertices cost defect two; if
`e=tau(e)`, one vertex has weight four and costs six. Both contradict the
one-unit bound. Thus the internal orbit is unramified.

The edges `e,f` are distinct: equality would again make both `e` and
`tau(e)` doubled, or one fixed edge have weight four. If they were disjoint
on the four labels of `J_0`, then they would be either the two fixed
`tau`-edges or one nonfixed edge and its `tau`-partner. In both cases the
four-edge multiset contains two doubled vertices and costs defect two.
Therefore `e,f` share exactly one endpoint `a`. At source points `x,-x`
above `z`,

```text
H(a,x)=H(a,-x)=0.
```

Adding and subtracting `H=U+XV` proves `U(a,z)=V(a,z)=0`. Reciprocal source
symmetry gives the second pair of equations in `(KBOI-1)`.

Now let the forced square fiber be unramified. The square-fiber cut gives
`V(T,w) in <q>`. Evaluation at `w` is an isomorphism from the three-
dimensional reciprocal `V` space to the space of endpoint quadratics. If
`V(T,w)=0`, then `V=0`, so `H(T,X)=H(T,-X)` and the two source-deck
components coincide. Actual source reduction excludes this. Scale so that
`V(T,w)=(1-w^2)q(T)`.

Every reciprocal odd part has the form

```text
V=(f+gW)+h(1+epsilon W)T+epsilon(g+fW)T^2.
```

Solving its three coefficients at `W=w` gives

```text
f=F,       g=G,       h=M,
```

and proves `(KBOI-2)`. Direct substitution also gives
`V(T,w)=(1-w^2)q(T)` and
`T^2 W V(1/T,1/W)=epsilon V(T,W)`.

Evaluating `(KBOI-2)` at `(a,z)` rewrites `(KBOI-1)` as

```text
N_epsilon(a)+z D_epsilon(a)=0.                    (1)
```

If `D_epsilon(a)=0`, then `(1)` gives `N_epsilon(a)=0`, so the linear
polynomial `V(a,W)` vanishes identically. In particular `V(a,w)=0`, hence
`q(a)=0`. This is impossible because `a in J_0` while the roots of `q` are
the disjoint labels `J_1`. Therefore `D_epsilon(a)` is nonzero, and solving
`(1)` gives `(KBOI-3)`. QED.
