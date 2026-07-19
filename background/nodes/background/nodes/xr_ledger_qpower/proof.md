# xr_ledger_qpower proof

Let `S,T` be agreement supports of size `k+t`, and let their exchange
distance be `s`, so

```text
|S \ T| = |T \ S| = s,
|S cap T| = r = k + t - s.
```

For one support, the event that a word has a degree-`<k` explanation on that
support is a codimension-`t` linear condition.

## Same slope

For fixed slope, the two-support event asks for codeword explanations on
both `S` and `T`.

If `r >= k`, the two degree-`<k` explanations agree on at least `k` points,
so they are the same RS codeword. The word is then determined on
`S union T` by one codeword, and

```text
codim = |S union T| - k = (k+t+s) - k = t+s.
```

If `r < k`, the explanations need not coincide. Count compatible pairs of
degree-`<k` codewords agreeing on the `r` overlap points. This space has
dimension `2k-r`. Since

```text
|S union T| = 2(k+t) - r,
```

the codimension is

```text
2(k+t)-r - (2k-r) = 2t.
```

Together,

```text
codim = t + min(s,t).
```

Union over the `q` finite slopes gives same-slope mass

```text
q^(1 - t - min(s,t)).
```

## Distinct slopes

For distinct slopes `z != z'`, the pointwise change of variables

```text
(u,v) -> (u + z v, u + z' v)
```

is invertible. Therefore the two support-alignment events are independent
codimension-`t` conditions. For a fixed ordered pair of distinct slopes the
mass is `q^(-2t)`, and union over the `q(q-1)` ordered slope pairs gives

```text
q^(2 - 2t)
```

up to the standard lower-order exclusion of equal slopes.

## Ledger exponent

Relative to the first-moment slope scale `q^(1-t)`, the same-slope branch
saves `q^(-min(s,t))`, while the distinct-slope plateau saves `q^(-(t-1))`.
The net q-power ledger is therefore

```text
c(s,t) = min(s, t-1).
```

The linear reach to `t-1` is real; the plateau is exactly distinct-slope
independence, not a rank collapse.
