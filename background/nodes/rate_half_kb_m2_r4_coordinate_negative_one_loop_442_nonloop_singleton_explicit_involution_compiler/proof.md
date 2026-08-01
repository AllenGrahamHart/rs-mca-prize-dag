# Proof

For a product pair `(Y,Z)`, the paired-product gate gives the row

```text
[YZ,-(Y+Z),-1]
```

against the kernel vector `(Gamma,Alpha,Beta)`.  The two rows from
`(KB41I-1)` are

```text
[-b^3,b^2-b,-1],       [bc,b+c,-1].              (1)
```

Their cross product is exactly `(KB41I-2)`.  Direct substitution therefore
gives `Phi(-b^2,b)=Phi(-b,-c)=0`.  Its determinant factor is

```text
Alpha^2+Gamma*Beta=2b^2(b-1)(b+c)(b^2-c).
```

Every factor is a parent product or target guard, and deployed
characteristic is odd, proving `(KB41I-3)`.  Thus the two rows are
independent and define the unique nonsingular involution.

The trace-zero matrix sends

```text
Y |--> (Alpha*Y+Beta)/(Gamma*Y-Alpha).
```

Substituting `Y=c` and simplifying gives `(KB41I-4)`.  In an actual complete
packet the singleton's antipodal source label is one of the seven
complementary labels, and the complete-fiber product map is finite there.
Hence the denominator in `(KB41I-4)` cannot vanish and that complementary
product equals `m`.

The other six complementary source labels form three antipodal pairs.
Applying the same involution to each gives `Phi(Y,Z)=0`.  Conversely, a
seven-value multiset with one value `m` and three such pairs can be assigned
to the singleton's mate and the three complementary antipodal source pairs,
so it passes the product-multiset part of the paired-product gate.

As a regression, the parent `F_41` witness `(b,c)=(10,5)` gives

```text
(Gamma,Alpha,Beta)=(7,16,16),       m=18.
```

The two common pairs satisfy `Phi=0`, the determinant is `40`, and applying
the displayed Mobius map to `c=5` gives `18` modulo 41. QED.
