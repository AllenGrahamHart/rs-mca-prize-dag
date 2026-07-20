# Fiber-two cycle harmonic top-characteristic screen

Modal app `ap-PVTrzkKlh4j1B6qDmGU1Wf` completed all 16 preregistered shards.
The exact input was

```text
p=1+k*2^40,       29058991<=k<33554432,       k even,
3*2^128<=p^2<4*2^128.
```

Thus `p=1 mod 2^41`, the only field class in which a source lift of exact
order `2^41` can descend to `F_p`. Every one of the `2,247,720` even classes
was tested against

```text
c_0=4,       c_(j+1)=c_j^2-2 mod p,       c_39=0.
```

There were no hits, even before restricting the moduli to primes. Each shard
used one CPU and 512 MiB, and completed in at most 1.67 seconds. This was
well below the preregistered `$0.25` ceiling.

The earlier hash-pinned harmonic packet proves `c_j!=0` for `1<=j<=38` over
all congruence classes. The new field router proves that a doubled-order
harmonic survivor either descends to one of those levels or lies in the split
class and satisfies `c_39=0`. The two packets together therefore exclude the
harmonic outer ratio on the scoped matched cycle parity branch.
