# Proof

Let `M=floor(q/2^t)`. The defining floor inequalities are

```text
M 2^t <= q < (M+1) 2^t.
```

The pair-root cost is

```text
R(M,k) = M(M+1)k/2.
```

If `Mk>=2^(t+1)`, then

```text
R(M,k) >= (M+1)2^t > q,
```

so `R(M,k)<q-n` is impossible. Conversely, if
`R(M,k)<M2^t-n`, then `q>=M2^t` gives `R(M,k)<q-n` for every
field order in the budget interval. These are exact integer implications.

For RowC, `M=2^122`. At rates `1/4` and `1/8`, respectively,

```text
Mk = 2^130 and 2^129,
```

so the impossibility criterion fires. At rate `1/16`, `Mk=2^128`, and direct
integer evaluation gives

```text
R(M,64) < 2^250-1024 <= q-1024.
```

For every prize anchor, even the smallest dimension is `k=2^37`, while the
printed budget has 128 bits. Hence `Mk>2^(t+1)` and the impossibility
criterion fires on all three rows.

It remains to classify the prefix condition on RowC rate `1/16`. The unsafe
predecessor is `m=66`, so `w=m-k-1=1`. The strict condition is

```text
binom(1024,66) > b M.
```

Exact division therefore makes it equivalent to

```text
b <= floor((binom(1024,66)-1)/M).
```

The integer on the right is the printed cutoff. Together with the uniformly
passing pair-root premise and the proved containment `D subset F_b`, this is
exactly the hypothesis of `identity_prefix_flexible_budget_unsafe_floor`.
Finally, a full-field choice has `b=q>=M2^128=2^250`, whereas the cutoff has
227 bits, so that choice fails the prefix premise.
