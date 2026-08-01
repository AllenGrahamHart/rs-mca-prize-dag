# Proof

The parent classifier's sixteen exact packets all satisfy
`4c^2=5b+6`; its primary verifier checks this identity before this node is
used.  The first relation in `(KB41BI-1)` is the parent's defining
`b` equation.

For a product pair `(Y,Z)`, the paired-product gate gives the row
`[YZ,-(Y+Z),-1]`.  The rows for `(KB41BI-2)` are

```text
[b^3,b^2+b,-1],          [-c^2,0,-1].
```

Their cross product is the negative of
`(Gamma,Alpha,Beta)` in `(KB41BI-3)`.  Direct substitution therefore
gives `Phi(-b^2,-b)=Phi(c,-c)=0`.  Moreover,

```text
Alpha^2+Gamma*Beta=(b-c)(b+c)(b^2-c)(b^2+c).
```

Every factor is a difference of two common products, so the parent guards
make it nonzero.  The two pair rows are independent and determine the
unique nonsingular projective involution.

Its trace-zero matrix sends

```text
Y |--> (Alpha*Y+Beta)/(Gamma*Y-Alpha).
```

At `Y=b`, the unsimplified mate is

```text
-b(b^3+bc^2+2c^2)/(2b^3+b^2+c^2).
```

Reducing by `(KB41BI-1)` gives

```text
2b^3+b^2+c^2=(9b+14)/4,
iota(b)=(18-5b)/22.
```

The resultant of `2b^2+3b+2` and `9b+14` is `176`, a deployed unit,
so no denominator branch is lost.  The corresponding resultants for
`18-5b` and `18-27b` are `968` and `3564`; hence `m!=0,b`.
Nonsingularity and the already fixed common pairs then imply that `m`
cannot equal another common product.

The singleton's antipodal source label lies among the seven outside labels,
so its product is `m`.  The other six outside labels form three
antipodal pairs and therefore three `Phi` pairs.  Conversely, assigning
one occurrence of `m` and the three `Phi` pairs to these four source
roles passes the product-multiset gate. QED.
