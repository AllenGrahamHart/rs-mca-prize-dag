# Proof

Fix a target `t`. The multiplicity of `t` in `Ucal_n` is `U(t)`, and the
multiplicity in `Delta_n` is `D(t)`. Both are smaller than `p`: an ordered
product fiber has at most `n-1` members, while `p>=n+1`, and `D(t)<=2`.
Lucas' theorem therefore makes every binomial coefficient
`binom(U(t),j)` with `0<=j<=U(t)` nonzero modulo `p`.

For a polynomial root of multiplicity `m<p`, the `j`th Hasse derivative has
root multiplicity `max(m-j,0)`. Taking the minimum over `0<=j<=12` gives

```text
ord_t(G_12)=max(U(t)-12,0).
```

The same argument with `Delta_n` and `j=0,1` gives

```text
ord_t(H_D)=max(D(t)-1,0).
```

This proves `(P24G3)`. Removing the full `T-1` power from `G_12` deletes
exactly the identity target and changes no other valuation.

Suppose `G_12^neq` divides `H_D`. If `t!=1` and `U(t)>=13`, then

```text
1<=U(t)-12<=D(t)-1<=1.
```

Hence `U(t)=13` and `D(t)=2`, so
`P(t)=2U(t)-D(t)=24`. If `U(t)<=12`, then
`P(t)<=2U(t)<=24`. Thus the first statement in `(P24G2)` holds.

Conversely, suppose every nonidentity target has `P(t)<=24`. If
`U(t)>=13`, then

```text
2U(t)-D(t)<=24,       D(t)<=2,
```

forcing `U(t)=13` and `D(t)=2`. Therefore every nonidentity root of `G_12`
has multiplicity one and occurs in `H_D` with multiplicity one. This is
exactly `G_12^neq|H_D`, proving `(P24G2)`. QED.
