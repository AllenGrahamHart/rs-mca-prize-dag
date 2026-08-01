# Proof

The negative product matrix has rows `[-p,-pW,1,W]`.  The two product
minors obtained from the first three records and `BC+` or `BC-`, together
with the two one-loop q welds, are necessary and sufficient on the printed
guards by the parent Vieta and q-weld compilers.

For `(KB431A-1)`, strip the guarded factors `(b+1)(c+1)` from each q weld.
Their direct resultant in `r` is `(KB431A-2)`.  The factors `b^2-1` and
`c^2-1` are target collisions, so put `c=sigma*i/b`, where
`sigma in {+1,-1}`.  The common linear q factors give

```text
(epsilon_1,epsilon_2)   sigma=+1       sigma=-1
(+1,+1)                 r=b            r=1/b
(+1,-1)                 r=i/b          r=ib
(-1,+1)                 r=-ib          r=-i/b
(-1,-1)                 r=1/b          r=b.       (KB431A-4)
```

No denominator vanishes because `b` is a product guard.

Write `x=t^2`.  Substitute each row of `(KB431A-4)` and its value of `c`
into the two product minors, then eliminate `x`.  After removing only the
target-collision factors `b+/-1` and `b+/-i`, the residual is one of the
four monic quartics `(KB431A-3)`.  All four occur among the eight branches.

In centered deployed-field coefficients their irreducible factorizations
are

```text
P0=(b^2-16711424b-255)(b^2-256b-16711423),
P1=(b^2+16776958b+16711423)(b^2-65280b+255),
P2=(b^2+256b-16711423)(b^2+16711424b-255),
P3=(b^2+65280b+255)(b^2-16776958b+16711423).
```

The paired discriminants reduce to the four values in the statement.
Euler's criterion raises each to `(p-1)/2` and returns `p-1`, so every
quadratic is irreducible over the deployed base field.  Thus none of the
eight branches contains a valid `b`, proving the cell empty. QED.
