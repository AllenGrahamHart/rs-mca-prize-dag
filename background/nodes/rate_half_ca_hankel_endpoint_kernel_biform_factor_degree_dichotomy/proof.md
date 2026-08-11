# Proof

The rational-normal kernel theorem gives exact parameter degree `m` and,
crucially, says that no projective parameter specializes `Q` to the zero
polynomial. Saturation rigidity says that `Q(Z,x)` is a nonzero parameter
polynomial for every domain point `x`.

Choose primitive polynomial representatives in `F_q[X][Z]` for the
irreducible factors in `(KFD2)`. Domain degree is additive under
multiplication, so

```text
sum_j d_j<=deg_X Q<=rho.                             (1)
```

Also `sum_j m_j=m).

Let `Gamma` be the `T` supported parameters. For a factor and supported
parameter, define

```text
n_(j,gamma)
 =#{x in D:Q_j(gamma,x)=0}.                         (2)
```

The polynomial `Q_j(gamma,X)` is not identically zero. Otherwise
`Z-gamma` divides `Q_j), hence `Q(gamma,X)=0`, contradicting the
rational-normal kernel map. Therefore

```text
sum_(gamma in Gamma)n_(j,gamma)<=T*d_j.             (3)
```

For a fixed domain point, `Q_j(Z,x)` is also nonzero; otherwise the product
`Q(Z,x)` would vanish identically, contrary to saturation rigidity. It has
parameter degree at most `m_j`, so

```text
sum_(gamma in Gamma)n_(j,gamma)<=N*m_j.             (4)
```

The content factor `c(X)` has no domain root for the same reason. Every
distinct domain root of `Q(gamma,X)` therefore comes from at least one
`Q_j). If `u_gamma` is the number of those roots, `(3)--(4)` give

```text
sum_gamma u_gamma
 <=sum_j min(T*d_j,N*m_j).                          (5)
```

By definition of the omission count,

```text
sum_gamma u_gamma=T*rho-O.                          (6)
```

Equations `(1)`, `(5)`, and `(6)` prove `(KFD4)`.

It remains to solve the integer inequality. A small factor satisfies

```text
(4m+1)d_j<16m*m_j,
```

and hence

```text
d_j<=4m_j-1.                                        (7)
```

Let `t` be the number of small factors and let `M_s` be their total
parameter degree. Bound the small-factor terms in `(KFD4)` using `(7)`
and the other terms by `N*m_j`. Since `O<=m-1`,

```text
(4m+1)t<=4M_s+1+O<=4M_s+m.                          (8)
```

If `t>=2`, then `(8)` forces

```text
4M_s>=7m+2,
```

contradicting `M_s<=m`. Thus `t<=1`.

If `t=0`, every factor is big. Since `m_j<=m`,

```text
(4m+1)d_j>=16m*m_j
  implies d_j>=4m_j.                                (9)
```

Summing `(9)` gives `sum d_j>=4m>rho`, contradicting `(1)). Therefore
`t=1) exactly.

Put `M_s=m_1) in `(8)`. Then

```text
4m+1<=4m_1+m,
```

which is `(KFD5)`. If all factors were parameter-linear, `m_1=1);
`(KFD5)` excludes this for `m>=2`. For `m=2,3,4`, the lower bound is
`m_1>=m), so the one factor already has the full parameter degree and
`Q` is irreducible over `F_q(X)). Finally,

```text
ceil((3*2^37+1)/4)=3*2^35+1=103079215105,
```

proving `(KFD6)`. QED.
