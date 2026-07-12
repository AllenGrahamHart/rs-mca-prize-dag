# Interleaved support census and the high-arity `a=k` value

- **status:** PROVED
- **consumer:** `list_large_m_scope_closure`

Let `C=RS[F,L,k]` have length `n`, let `q=|F|`, and let `m>=1`. Write
`L_m(a)` for the worst `m`-interleaved common-support list size at agreement at
least `a`.

For every `a>=k`,

```text
L_m(a) <= binom(n,a).                              (SC)
```

For every `0<=a<=n`, the exact received-word average gives

```text
L_m(a) >= ceil(
  [sum_(s=a)^n binom(n,s)(q^m-1)^(n-s)] / q^(m(n-k))
).                                                  (AV)
```

Moreover, if

```text
q^m > binom(n,k+1),                               (HM)
```

then

```text
L_m(k) = binom(n,k).                              (EK)
```

Consequently the least `a>=max(k,ceil(n/2))` with
`binom(n,a)<=floor(q/2^128)` is a certified safe anchor for every arity, while
`(AV)` is an explicit lower staircase at every agreement. Under `(HM)`,
agreement `k` is an exact unsafe anchor whenever
`binom(n,k)>floor(q/2^128)`.
