# E1 profile-(0,18) mod-257 singleton-completion no-go

- **status:** PROVED
- **closure:** exact finite-field bijection and explicit adversarial family
- **scope:** profile `(0,18,S=18)`, local valuation one

For a primitive root `g=3 mod 257`, the map

```text
(e,epsilon) -> epsilon*g^e,
0<=e<128, epsilon in {+1,-1},
```

is a bijection onto `F_257^*`. Thus any nonzero residual sum of 17 signed
singletons has a unique oriented singleton completion, unless its position
is already occupied.

More strongly, the explicit polynomial

```text
F_0(X)=sum_(e=0)^15 X^e + X^17 + X^78
```

has 18 distinct signed-singleton terms, exact local multiplicity one at
`X=1 mod 2`, and `F_0(3)=0 mod 257`. Galois transport gives a polynomial
with the same profile and local valuation vanishing at every primitive
256-th root modulo 257.

Therefore the mod-257 root equation plus local valuation one cannot remove
even one of the 128 split ideals. The example has autocorrelation energy
1478, so it is not a live cofactor-514 collision and does not falsify the
five-ideal target.
