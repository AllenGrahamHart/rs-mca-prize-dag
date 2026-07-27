# E1 N=256 square-mass-16 autocorrelation-subfield exclusion

- **status:** PROVED
- **closure:** proof plus exact arithmetic

Let `F=sum_i c_i X^i` have folded profile `(3,4,0)` in the
`N=256,s=5` band. Write its positive-half negacyclic autocorrelation as
`A_d`, and suppose its exact variance is `V=76`. If

```text
A_d=0 whenever 4 does not divide d,                       (1)
```

then `F` cannot produce a pair-feasible row-prime collision.

Indeed, the exact slack recurrence gives `L=sum_d |A_d|<=22`, hence every
conjugate square is at most `16+2L<=60`. For a primitive 256-th root `zeta`,

```text
beta=F(zeta) conjugate(F(zeta))
```

belongs under (1) to `Q(zeta^4)=Q(zeta_64)`. If `R` is the nonzero
256-th cyclotomic norm of `F(zeta)` and `N` is the 64-th cyclotomic norm of
`beta`, then

```text
R^2=N^4,       0<|N|<=60^32<2^250.
```

Thus every rational prime divisor of `R` divides `N`, ruling out the
pair-feasible primes `p>=2^250`.

Consequently every unresolved `V=76` candidate has a nonzero
autocorrelation coefficient at some distance not divisible by four. This is
a route reduction, not an exclusion of all `V=76` candidates.
