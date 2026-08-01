# Proof

Fix a sign row and use the safe `c` reconstruction from the cubic-root
parent.  Adjoin in turn the sign cubic for `r`, one factor in `(KB41Q-1)`,
and the numerators of the remaining product minor and q weld.

For either cubic factor, exact deployed-field reduction gives a four-element
zero-dimensional basis containing

```text
t-epsilon_2*i*r.
```

Since `i^2=-1`, this implies `(KB41Q-2)`.  The common labels in this orbit
are `(1,-1,r^2,t^2,-r^2)`, so the branch violates label injectivity.  This
deletes both cubic factors in all four sign rows.

On `S(b)=0`, exact reduction gives six basis polynomials.  In the
representative row they are exactly `(KB41Q-4)`.  Their leading monomials in
grevlex order `(t,r,b)` are

```text
rb^2, b^3, t^2, tr, r^2, tb.
```

The monomials not divisible by these leaders are exactly `(KB41Q-3)`, so
the quotient rank is six.  Replaying the other three sign rows gives the
same leading monomials and rank.

Let `D=b(r^2+1)^2+r^4-6r^2+1` be the denominator used to reconstruct `c`.
Reduce `D` times each monomial in `(KB41Q-3)` and form the resulting `6 x 6`
multiplication matrix.  Its determinant is `524288=2^19` in all four sign
rows.  This is nonzero in the odd deployed field, so `D` is a unit and the
substitution has introduced no component.

The parent `F_41` witness has `b=10` on `S`, so retaining the sextic branch
is necessary. QED.
