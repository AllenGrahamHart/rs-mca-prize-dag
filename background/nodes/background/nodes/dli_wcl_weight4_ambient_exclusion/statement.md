# DLI terminal weight-4 ambient exclusion

- **status:** PROVED
- **closure:** computation

## Statement

Let

```text
P(X) = sum_(i=1)^4 s_i X^e_i,
```

where the `e_i` are distinct in `{0,...,255}` and `s_i in {+1,-1}`,
modulo global sign. Among all

```text
C(256,4) * 2^3 = 1,398,341,120
```

reduced signed weight-4 polynomials, no norm

```text
Res(X^256+1, P(X))
```

has a prime divisor `q<2^256` satisfying `v_2(q-1)>=41`.

Consequently no official DLI production row contains a primitive weight-4
relation in either terminal `ell=1` level.

## Certificate

Every affine orbit has a representative containing `{0,2^v}` for some
`0<=v<=7`: choose two non-antipodal terms, translate the first to zero, and
use an odd dilation to remove the odd part of their difference. The resulting
normalized section has 1,014,080 keys and partitions into exactly 24,979
affine-Galois classes.

The certificate contains one exact resultant and complete factorization per
class. There are 88,086 factor records and 44,599 distinct prime factors. A
154,086-node shared recursive Pocklington graph proves all factors prime.
There are no ambient candidates, and the largest splitting depth below the
cap is `v_2(q-1)=29`.

The independent ledger verifier reconstructs the normalized section and its
orbit partition. It also recomputes every resultant modulo enough certified
31-bit split primes that their product exceeds `2*4^256`; the bound
`0<=Res(X^256+1,P)<=4^256` then makes the modular equality exact. A separate
verifier checks the complete Pocklington graph.

## Nonclaims

This closes only weight 4 at `ell=1`. Together with the weight-3 exclusion and
the elementary weight-2 obstruction, the unresolved terminal window is now
weights 5 and 6. No other level or full WCL-ZONE inequality follows.

## Falsifier

A missing normalized orbit, a support outside the claimed partition, an
incorrect resultant or factorization, a composite certified factor, or one
factor below `2^256` with `v_2(q-1)>=41`.
