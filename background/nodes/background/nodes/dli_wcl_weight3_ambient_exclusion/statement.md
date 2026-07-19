# DLI terminal weight-3 ambient exclusion

- **status:** PROVED
- **closure:** computation

## Statement

Let

```text
P(X) = s_1 X^e_1 + s_2 X^e_2 + s_3 X^e_3,
```

where the `e_i` are distinct elements of `{0,...,255}` and
`s_i in {+1,-1}`, modulo global sign.  Among all

```text
C(256,3) * 2^2 = 11,054,080
```

such reduced signed weight-3 polynomials, no cyclotomic norm

```text
Res(X^256+1, P(X))
```

has a prime divisor `q < 2^256` satisfying `v_2(q-1) >= 41`.

Consequently no official DLI production row can contain a primitive
weight-3 relation in either terminal `ell=1` level.  Such a relation would
require an ambient field prime with `2^41 | q-1`, and evaluation at its
order-512 root would force `q` to divide the displayed norm.

## Certificate

Signed shifts and odd Galois dilations act on the full exponent encoding by

```text
e -> a e + b mod 512,  a odd.
```

The exact orbit partition has 254 classes.  The certificate contains one
exact resultant and complete factorization per class, together with a shared
recursive Pocklington tree proving all 439 distinct factors prime.  The
largest splitting depth encountered below `2^256` is `v_2(q-1)=18`.

The verifier independently proves that the 254 disjoint orbits cover all
11,054,080 supports.  It also recomputes every resultant modulo enough
31-bit split primes that their product exceeds `2*3^256`; the root-product
bound `0 <= Res(X^256+1,P) <= 3^256` then makes the modular equality exact.

## Nonclaims

This closes only weight 3 at `ell=1`.  The weight-2 case is elementary, but
weights 4, 5, and 6 in the same WCL window remain open.  No other terminal
level, full WCL-ZONE inequality, `C1'`, or `C2''` statement follows.

## Falsifier

A missing or duplicate affine-Galois orbit, an incorrect resultant or
factorization, a composite certified factor, or one factor below `2^256`
with `v_2(q-1) >= 41`.
