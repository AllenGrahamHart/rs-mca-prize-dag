# Upstream crosswalk

Paper D v13.2 writes every balanced support-census element as

```text
(W,N)=A g_1+B g_2,
```

with degree caps from `thm:capfr1-near-rational-dichotomy(ii)` and removes
`W|N` using `lem:capfr1-autodiv`.  Its active endpoint asks for a
**primitive split-pencil family**, but the exact relationship between
primitivity and complete agreement is not printed there.

The present theorem supplies that relationship:

```text
complete agreement at level m  <=>  gcd(A,B)=1,
agreement excess              =   deg gcd(A,B).
```

Thus Paper D's raw `cen(U;m)` should be partitioned by coefficient content
before applying the L1 exact-shell consumer.  Nontrivial content is routed
once to its higher exact shell; only coprime `(A,B)` belongs to
`BC_exact_guarded`.  This is portable algebra and does not assert the open
base-field-normalized upper bound on the primitive locus.
