# Proof

The common pairs in cell `12` are `(b,-b),(c,-c)` with singleton `bc`.
Two distinct antipodal pairs force the negation involution.  In cell `13`
the pairs are `(b,c),(-b,-c)`; in cell `14` they are
`(b,-c),(-b,c)`.  Direct substitution gives `(KBZ433BP-1)`.

Every outside product is a signed monomial in `D,E,F`.  Choose a generator
of `F_(p^6)^*` compatible with the primitive base generator `3`.  A forced
mate plus three involution pairs gives four linear congruences in the three
logs of `D,E,F` modulo `p^6-1`.  For cell `12`, a pair `z=-y` uses a
difference of exponent rows; for cells `13,14`, a reciprocal pair uses their
sum.  Smith normal form decides every system and enumerates every isolated
solution.

For each solution, doubled target logs test equality up to sign and all
twelve product logs test Mobius-product injectivity.  The exact raw deleted
census per distinct `(b,c)` row is

```text
cell/type  raw systems  compatible  isolated  families  guarded
12/Z0          420          144         192       16         0
12/Z1         3360          512         896        0         0
13/Z0          420           50         208        0         0
13/Z4         1680          184         640        0         0
14/Z0          420           50         208        0         0
14/Z4         1680          184         640        0         0. (1)
```

The free `12/Z0` systems are not excluded by sampling: polynomial reduction
of target-square and product differences by each binomial ideal gives an
explicit target-square collision.  Thus `(1)` proves `(KBZ433BP-2)`.

For every complementary type, the same congruence replay produces at least
one exponent triple passing both guards over a representative common row.
This proves only that the product gate cannot delete those types.  The
finite common classifier shows that the 16 distinct `(b,c)` rows cover all
32 packets, completing the transport. QED.
