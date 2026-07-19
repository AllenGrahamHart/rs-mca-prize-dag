# DLI ell=2 weight-3 ambient exclusion

- **status:** PROVED
- **closure:** computation

## Statement

Let

```text
P(X) = sum_(i=1)^3 s_i X^e_i,
```

where the `e_i` are distinct in `{0,...,511}` and `s_i in {+1,-1}`,
modulo global sign. Among all

```text
C(512,3) * 2^2 = 88,954,880
```

reduced signed weight-3 polynomials, no norm

```text
Res(X^512+1, P(X))
```

has a prime divisor `q<2^256` satisfying `v_2(q-1)>=41`.
Consequently no official DLI production row contains a primitive weight-3
relation at the `ell=2` level.

## Certificate

Every affine orbit has a representative containing full exponent zero. The
resulting normalized section has 521,220 keys and partitions into exactly 510
affine-Galois classes. The certificate gives one exact resultant and complete
factorization per class: 1,329 factor records, 1,141 distinct prime roots, no
ambient candidate, and maximum `v_2(q-1)=21` below the field cap. A shared
5,608-node recursive Pocklington graph proves every factor prime.

The independent verifier reconstructs the section and its complete orbit
partition. It recomputes every resultant modulo enough certified 31-bit split
primes that their product exceeds `2*3^512`, making the modular equality exact
under the root-product norm bound. A second verifier checks the full prime
graph.

## Nonclaims

This closes only weight 3 at `ell=2`. Weights 4 through 7 there, every other
level, and WCL-ZONE remain open.

## Falsifier

A missing normalized-section orbit, an incorrect resultant or factorization,
a composite certified factor, or one factor below `2^256` with
`v_2(q-1)>=41`.
