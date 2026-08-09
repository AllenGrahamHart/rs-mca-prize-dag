# Proof

Let `kappa=(A0,A1,A2,B0,B1,B2)` be the primitive cofactor kernel of the five
product rows, let `x=-1` be the `AB` source label, and put

```text
s=x(1-x)=-2,       gamma=q_AB(A0+A1*x+A2*x^2).
```

Then

```text
(s*A0,s*A1,s*A2,s*B0,s*B1,s*B2,-gamma,gamma)
```

annihilates the five product rows by definition.  The `LA` sum has zero
signed sum and label one, so its last two entries cancel.  On the `AB` row,
the first block contributes `s*gamma` and the last block contributes
`-s*gamma`, so the pairing is zero.  Exact gcd removal and scalar
normalization make this vector primitive.

The compiler constructs the vector independently in all four sign rows.  It
then reduces all ten row pairings by the exact global lex ideal with the full
route guard inverted.  The first seven pairings are identically zero, and all
ten recorded remainders are zero.  The six product-coordinate digests agree
in all rows.  The last two agree for fixed first sign and exchange when that
sign changes, exactly because `q_AB` changes sign. QED.
