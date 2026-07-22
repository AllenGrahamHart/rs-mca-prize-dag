# Proof - L1 raw support-ledger exponential route fence

Because `j` is a power of two and `j>=16`, all quantities in `(RF1)--(RF2)`
are integers. Direct substitution gives

```text
N+b+Mell=(n/2-1)+1+(j/2)(n/j)=n.
```

Also `ell>=1`, `b=1<ell`, and

```text
r+h=n/4=ell+(n/4-ell)=ell+d.
```

Since `ell<=n/16`, one has `d=n/4-ell>=3ell`, so
`0<a_i=ell/2<=d`. Finally `h-d=ell>0`. This proves `(RF3)`.

The identities in `(RF4)` follow from `tell=Mell=n/2` and direct
substitution. In particular `0<e<=N`, so its binomial factor is nonzero.
Since `t=M`, the first binomial in
`(RF5)` is one, while the middle binomial is

```text
binom(tell,h)=binom(n/2,n/4).
```

For integers `m>=1`,

```text
binom(2m,m)=product_(i=1)^m (m+i)/i >=2^m,
```

because `m+i>=2i` for `i<=m`. Taking `m=n/4` proves `(RF6)`.

For the background-anchor exponent, `r=0` and every petal support has size
`ell/2`, so

```text
gamma=d-ell/2+1=n/4-3ell/2+1.
```

The inequality `ell<=n/16` gives

```text
gamma>=n/4-3n/32+1=5n/32+1>=n/8,
```

which proves `(RF7)`. Both raw numerical bounds therefore exceed every fixed
power of `n` along the displayed family. The conclusion concerns those raw
union-bound routes only; emptiness or collective algebraic dependence among
the formal support cells could still prove L1.
