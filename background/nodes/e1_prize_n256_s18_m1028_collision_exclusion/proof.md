# Proof

The parent theorem says that a prize-row collision with `m=1028` must have
`V=10` or `V=18`. It also identifies

```text
v_2(m)=2=2^v_2(s-r),
```

where `r,s` are the singleton exponents. Thus `s-r=2q mod 128` for an odd
`q`. Multiplication by a monomial translates `r` to zero. An odd cyclotomic
automorphism, with multiplier inverse to `q` modulo 64, moves the other
singleton to position two. Folding exponents back into `0,...,127` changes
only coefficient signs. Finally multiply by `-1` if necessary. Every candidate
therefore has the normalized form

```text
F(X)=1+epsilon X^2+2 sum_(j=1)^4 epsilon_j X^(a_j),
epsilon,epsilon_j in {+1,-1},
{a_1,...,a_4} subset {0,...,127}\{0,2}.
```

The normalization need not be free: surjectivity onto the normalized search
space is all that an emptiness proof requires. The exact search size is

```text
binom(126,4)*2^5=10009125*32=320292000.              (1)
```

For each vector both engines form the exact negacyclic autocorrelations
`A_d` and compute

```text
E=sum_(d=1)^63 A_d^2,             V=2E.
```

The primary engine folds each of the 15 unordered coefficient pairs directly
to a positive lag. Its greedily balanced 32-shard census returns

```text
E=5: 0 vectors,
E=9: 16 vectors.
```

The audit engine instead forms the full 128-slot ordered-pair convolution,
checks `A_(128-d)=-A_d` and `A_64=0`, and shards lexicographic four-subsets by
their global index modulo 32. It independently returns the same exact totals.
Both scans cover (1) with no timeout or error.

It remains to exclude the 16 `E=9` vectors from the cofactor class. The element
`3` has order 256 in `F_257^*`, so

```text
Phi_256(X)=X^128+1=product_(u odd) (X-3^u) mod 257.
```

For an integral cyclotomic value,

```text
257 divides Norm(F(zeta))
  iff F(3^u)=0 mod 257 for some odd u.                (2)
```

Each engine tests all 128 odd exponents in (2) for every `E in {5,9}` vector.
None of the 16 `E=9` vectors vanishes, while `E=5` is empty. Therefore 257
does not divide any norm in the parent residual. But a collision with
`R=1028p` would have `257|R`, a contradiction.
