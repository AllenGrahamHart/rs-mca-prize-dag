# Proof: fixed-background FPC5 GRS shell payment

For each `R`, the fixed-background Hankel theorem identifies a chart with
`c=ell-1` rows. The GRS syndrome-shell theorem therefore has

```text
D=d+c=d+ell-1.
```

If `D>=N`, that theorem gives `|F_R|<=1`.

Suppose `D<N`. Any two distinct supports in `F_R` have size `d` and
intersection at most

```text
r_fix=d-c-1=d-ell.                                   (1)
```

Let `m_R=|F_R|`, and let `s_x` count its supports containing core point `x`.
Then

```text
sum_x s_x=m_R d,
sum_x binom(s_x,2)<=binom(m_R,2)r_fix.                (2)
```

Cauchy-Schwarz gives `sum_xs_x^2>=m_R^2d^2/N`. Combining this with `(2)`
yields

```text
m_R(d^2-Nr_fix)<=N(d-r_fix)=N ell.                   (3)
```

When `J_fix=d^2-Nr_fix>0`, equation `(3)` proves
`m_R<=Nell/J_fix`.

The exact fixed-background incidence identity gives

```text
|F|<=sum_(|R|=u)|F_R|.                               (4)
```

There are `binom(b,u)` choices of `R`. Applying the corresponding per-chart
bound in `(4)` proves `(FP2)--(FP3)`. If `min(u,b-u)<=C`, symmetry and the
elementary estimate `binom(b,u)<=b^C<=n^C` prove `(FP4)`.

Finally, with `r=2d-tell` and `u=d-(t-1)ell`, one has

```text
r-u=d-ell.
```

Therefore

```text
J_bg=b d^2+N u^2-Nbr
    =b(d^2-N(d-ell))-Nu(b-u),
```

which is `(FP5)`. QED.
