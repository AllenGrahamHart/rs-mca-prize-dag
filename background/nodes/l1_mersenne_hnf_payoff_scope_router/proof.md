# Proof - L1 Mersenne HNF payoff-scope router

The checkpoint atlas leaves 16 rows with `m>=3`. The broad-checkpoint
periodicity theorem removes the seven rows for which `n-mp>16`; the nine
remaining rows have

```text
n=m(p+1),            m in {4,8,16},
row multiplicities   4,4,1.
```

A split-pencil pair uses at least two complete values, so `h>=2`. The
maximal-value complement theorem removes `h=m` on every one of the 16
`m>=3` rows. The complete `m=4,h=3` theorem removes the only
next-to-maximal `m=4` value. Consequently the remaining degree sets are

```text
m=4:  {2},
m=8:  {2,3,4,5,6,7},
m=16: {2,3,...,15}.
```

Multiplying by the row multiplicities gives `4`, `24`, and `14`, hence
(HPR1). The embedded two-fiber theorem says its normalized inner polynomial
is odd, so its split values occur in opposite pairs and its total value
degree is even. The even-cell count is

```text
4*1+4*3+1*7=23;
```

the remaining `42-23=19` cells are odd. The degrees `h=7` and `h=15`
occupy four and one rows respectively, proving (HPR2).

The J-zero guard compiler explicitly scopes itself to the exceptional
`J_*=0`, cubic `3+2+1` role branch of one retained `m=8,h=7` candidate.
That branch is a strict subset of the complete order-one `h=7` cell. An
emptiness theorem for a strict subset cannot establish emptiness of the
union until all sibling subsets are discharged. The order-zero reciprocal
theorem removes the order-zero chamber, not those order-one siblings. This
proves (HPR3).

For the census formula, the maximal split-value complement theorem uses

```text
u=n-hp,             ell_h=u-d+p.
```

Substitution of `n=m(p+1)` gives the definitions in (HPR4), and its pair
factor is exactly `binom(h,2)`. Substituting `(m,h)=(8,7)` and `(16,15)`
gives (HPR5).

After every owned `t=p` pair is removed, every remaining collision has
integer width at least `p+1`. The packing theorem uses `s=a-t+1`, yielding
the two caps in (HPR6). For the corresponding unfloored ratios,

```text
binom(n,s)/binom(a,s)
-------------------------------- = (n-s+1)/(a-s+1)
binom(n,s-1)/binom(a,s-1)
```

with `s=a-p+1`. This is `(n-a+p)/p`. Since `a>=0` and
`n=m(p+1)`, it is at most `(n+p)/p=m+m/p+1<m+2<=18`.
This proves (HPR6)--(HPR7). The cited packing and tail-distance theorems
already state that surviving wider widths and aggregate fiber payment remain
open, proving the final scope fence. QED.
