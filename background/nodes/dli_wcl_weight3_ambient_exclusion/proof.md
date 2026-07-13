# Proof certificate

Encode a negative coefficient at reduced exponent `e` by the full exponent
`e+256` in `Z/512`.  Translation by 256 changes global sign, so signed shift
and odd Galois dilation reduce to the affine action

```text
S -> aS+b,  a in (Z/512)^x, b in Z/256.
```

The generated certificate lists 254 representatives.  The independent
verifier constructs each full orbit, checks that its canonical key is unique,
and sums the orbit cardinalities.  The sum is
`C(256,3)*2^2=11,054,080`, the cardinality of the entire reduced signed
weight-3 universe, so the listed classes are disjoint and exhaustive.

For each representative, Modal/FLINT computes
`Res(X^256+1,P)`.  The local verifier does not trust those values: it chooses
deterministically enough primes `p=1 mod 512`, evaluates `P` at all 256 odd
powers of an exact order-512 root in `F_p`, and compares the resulting root
product with the claimed resultant modulo `p`.  The product of the moduli is
larger than `2*3^256`.  Since all 256 complex factors have absolute value at
most 3, this certifies each nonnegative resultant as an exact integer.

PARI supplies complete factorizations.  Their product is checked against each
certified resultant, and a shared recursive Pocklington certificate proves
every distinct factor prime.  Direct inspection of all factors then gives
zero factors `q<2^256` with `v_2(q-1)>=41`; the maximum is 18.

Finally, if an official-row weight-3 relation existed at an order-512 root
`omega in F_q`, then reduction of the integer resultant modulo `q` would
vanish, so `q` would divide one of the certified norms.  The official ambient
split requires `2^41 | q-1`, contradicting the exhaustive factor ledger.
