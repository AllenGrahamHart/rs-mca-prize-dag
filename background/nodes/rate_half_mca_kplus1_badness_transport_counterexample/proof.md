# Proof

The source contract has

```text
p=2130706433, n=2^21, k=2^20, m=1116048,
zeta=1213133211, e=67473.
```

Full factorization `p-1=127*2^24` and the recorded Pocklington witnesses
prove `p` prime.  Exact modular powers give `zeta^n=1` and
`zeta^(n/2)=-1`, so `zeta` has order exactly `n`.  Also
`e+m=1183521<n`; hence the exponent intervals defining `E` and `S` are
disjoint and `|S|=m`.

Let `u` be the indicator of `E` and let `v(x)=x^k` on `D`.  At slope zero,
`u+0v=u` vanishes on `S`, so the zero polynomial of degree less than `k`
is an explanation on that exact support.

Suppose a polynomial `g` of degree less than `k` explained the direction
word on `S`.  Then

```text
X^k-g(X)
```

would have all `m` points of `S` as roots.  It is a nonzero monic polynomial
of degree exactly `k`, while `m>k`.  This is impossible.  Thus no pair of
degree-less-than-`k` polynomials simultaneously explains `(u,v)` on `S`, and
the displayed slope-zero witness is support-wise MCA-bad for the actual code.

For the enlarged code of dimension `k+1`, both `0` and `X^k` have degree
less than `k+1`.  They agree with `(u,v)` on `S`, because `u=0` there and
`v=X^k` everywhere.  The identical slope and support therefore fail the
pair-noncontainment condition.  This proves the claimed change in badness.
