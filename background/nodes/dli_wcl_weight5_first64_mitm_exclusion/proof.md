# Proof certificate

Encode a negative reduced term `-X^e` by the full exponent `e+256` in
`Z/512`. A reduced signed weight-5 polynomial is therefore a five-set of full
exponents with no equal or antipodal pair. Its value at an order-512 root is
the sum of the five corresponding powers.

There are

```text
C(512,2)-256 = 130,560
```

legal unordered pairs. There are

```text
C(512,3)-256*510 = 22,108,160
```

legal unordered triples, because a three-set contains at most one antipodal
pair. Every legal five-set has a legal two/three split. The compiler stores
every pair by its field sum, enumerates every triple, and looks up the
negative triple sum. It then rejects pair/triple collisions that repeat an
exponent or introduce an antipodal pair. Hence a zero relation exists if and
only if the compiler reports one. The hash-pinned banked artifact records
complete pair and triple coverage and no relation on all 64 rows, so in
particular no primitive relation exists. The full search remains independently
executable through the registered remote launcher; the local batch checker
validates the artifact and its complete row/certificate ledger without
rerunning the roughly 1.4 billion triple checks.

The row-selection certificate is also complete. It gives one record for each
integer `1<=k<=996`. A composite record carries a proper divisor of
`k*2^41+1`. A prime record completely factors `q-1`; the factors are at most
996 and are checked by trial division. For each distinct prime divisor `r` of
`q-1`, the supplied base `a_r` satisfies

```text
a_r^(q-1) = 1 mod q,
gcd(a_r^((q-1)/r)-1,q) = 1.
```

Pocklington's criterion proves `q` prime. The supplied generator is nontrivial
at every prime quotient of `q-1`, so it is primitive. Thus the 64 listed rows
are exactly the first 64 split primes and the replayed order-512 roots are
valid.

[w7 audit: the search's primitivity filter discards candidates with
vanishing proper subsums; on these rows that loses nothing because
weight 1-4 relations are excluded by the exact-order argument and the
weight-3/4 ambient censuses, whose scope (v_2(q-1) >= 41, q < 2^256)
covers all 64 rows.]

[KB #107 harness repair: the former local verifier recompiled and replayed
all 64 MITM searches, causing recurrent batch timeouts under constrained
workers. The mathematical search and banked artifact are unchanged. The
local verifier now follows the accepted remote no-hit certificate policy:
fail-closed schema, coverage, Pocklington, primitive-generator, source,
launcher, result-hash, and mutation checks locally; exhaustive regeneration
only through the manifest-registered Modal launcher.]
