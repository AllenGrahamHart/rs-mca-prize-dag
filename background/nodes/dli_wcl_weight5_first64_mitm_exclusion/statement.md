# DLI terminal weight-5 first-64 split-prime exclusion

- **status:** PROVED
- **closure:** computation

## Statement

Let `q=k*2^41+1`. For the first 64 prime values of `q` in increasing
positive `k`, namely `3<=k<=996` and

```text
6,597,069,766,657 <= q <= 2,190,227,162,529,793,
```

there is no reduced signed weight-5 relation at an order-512 root in `F_q`.
In particular, none of these 64 ambient split-prime rows has a primitive
weight-5 orbit in either terminal `ell=1` level.

## Certificate

The artifact partitions every `1<=k<=996` into 64 certified prime rows and
932 composite rows carrying explicit proper divisors. For every prime row it
also gives a complete factorization of `q-1`, direct Pocklington witnesses,
and a certified primitive generator.

For each row the exact C++ meet-in-the-middle search builds all 130,560 legal
non-antipodal pairs and checks all 22,108,160 legal non-antipodal triples.
The independent verifier recompiles the pinned source and replays all 64
searches. All return zero relations.

## Nonclaims

This is a finite falsification-survival theorem, not an exhaustive ambient
weight-5 exclusion. No assertion is made for the remaining split primes below
`2^256`, for weight 6, for any other WCL level, or for WCL-ZONE itself.

## Falsifier

A skipped prime before `k=996`, an invalid composite divisor or primality
certificate, or one legal five-set whose order-512 roots sum to zero on any of
the 64 listed rows.
