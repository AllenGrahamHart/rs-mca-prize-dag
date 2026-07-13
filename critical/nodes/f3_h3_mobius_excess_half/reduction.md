# Cutoff-18 reduction and weakening proof

## The former red premise implies the new one

For every integer `m>=0`,

```text
(m-18)_+ <= 17 + (m-35)_+.
```

Since `sum_(t!=1)R(t)=(n-1)(n-2)`, the former premise
`X_35<=n^2/2` gives

```text
X_18 <= 17(n-1)(n-2)+n^2/2,
17X_18 <= (595/2)n^2-867n+578 < 300n^2.
```

Thus the new critical target is strictly weaker than the old one.

## Non-swap sufficient theorem

Put

```text
D(t)=#{a in A:a^2=t},
S_ns=sum_(t!=1) [P(t)(P(t)-2)+D(t)]R(t).
S_ns^rich=sum_(t!=1,P(t)>=19) [P(t)(P(t)-2)+D(t)]R(t).
```

For every feasible product multiplicity `m` and fixed-point count `d`, parity
of the swap involution gives `d=m mod 2`, and

```text
68(m-18)_+ <= m(m-2)+d.                          (1)
```

For `m<=18` this is immediate. For `m>=19`, right minus left is

```text
(m-34)(m-36)+d,
```

which is nonnegative; the only interior case is `m=35`, where odd parity gives
`d>=1`. For `m<=18` the left side vanishes, so those nonnegative right-side
terms can be discarded. Multiplying (1) by `R(t)` and summing only over
`P(t)>=19` proves

```text
68X_18<=S_ns^rich<=S_ns.
```

Consequently the single estimate

```text
S_ns^rich<=1200n^2                                 (SNS18-1200)
```

implies `17X_18<=300n^2`. This is strictly weaker than the former full-moment
target `S_ns<=1200n^2`: all product fibers below the actual cutoff are now
discarded.
