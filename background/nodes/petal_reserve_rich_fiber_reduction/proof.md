# Proof - petal reserve rich-fiber reduction

The core-defect reduction gives

```text
P=Q+L_(C\D)W,       deg W<=d.
```

If `W=0`, then `P=Q`. It agrees with the source only on the core and the
background, at most

```text
(k-1)+b < (k-1)+ell = k+sigma
```

points, so it is not listed. Hence `W` is nonzero.

At a background point, agreement is equivalent to `W(y)=0`. A nonzero
degree-at-most-`d` polynomial has at most `d` roots, so `r<=d`. The exact
core contributes `k-1-d` agreements. The list threshold therefore gives

```text
(k-1-d)+r+h >= k+ell-1,
h+r >= ell+d.
```

Combining this with `r<=d` yields `h>=ell`.

There are `M` petals. Pigeonhole gives one petal with at least
`ceil(h/M)>=ceil(ell/M)` agreements. On petal `T_i`, every agreement satisfies

```text
W(y)=c_iL_D(y),       R(y)=c_i.
```

Thus these points form one rational-value fiber. The non-planted per-petal
cap from the core-defect theorem is `|S_i|<=d`, proving `d>=m_rich`.

If all petal values of `R` are distinct, every petal contributes at most one
agreement, so `h<=M`. This contradicts `h>=ell` when `ell>M`.

Maximality gives

```text
M=floor((n-k+1)/ell) <= (n-k+1)/ell.
```

Therefore

```text
ell/M >= ell^2/(n-k+1).
```

At fixed rate and `ell>=C n/log_2 n`, the right side is
`Omega(n/log_2^2 n)`, while `ell/M` tends to infinity. In particular
`ell>M` for all sufficiently large rows.
