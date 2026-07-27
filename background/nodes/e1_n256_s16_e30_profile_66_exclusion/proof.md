# Proof

Let `O` be the symmetric set of the six distinct light-light differences. In
profile `(6,6)`, six positive classes have magnitude one and six have
magnitude two. Hence the six odd classes are exactly `O`, and choosing the six
magnitude-two classes `E` outside `O` gives the full cyclic absolute
autocorrelation

```text
b = 1_O + 2*1_E.                                  (1)
```

The proved six-odd atlas contains `280,720` normalized light supports and
exactly `1,234` odd masks, one affine light orbit per mask. For each mask,
(1) has `binom(57,6)=36,288,252` assignments.

The production scanner constructs the signed zero-sum cubic kernel and scores
each six-set incrementally. The audit constructs its coefficients directly
from cyclic base vectors and pair sums, then uses an independent three-plus-
three decomposition. They agree row by row on all

```text
1,234*binom(57,6) = 44,779,702,968
```

assignments, including every histogram, maximum, and maximizing witness.
Exactly `33,737` assignments on `1,191` masks exceed the proved cubic cutoff
`M_3=1087`; every other assignment has norm below `2^250` by the cubic-Hermite
criterion.

For each exceptional mask, the folded-chord engine and independent direct-
negacyclic engine enumerate all heavy triples and 64 relative sign vectors.
They agree row by row after `23,638,891,776` vectors per engine:

```text
profile vectors                         240,672
M_3>1087                                  6,244
M_3>1087, full conductor                  1,232.
```

The proper-conductor theorem excludes the complementary `5,012` vectors.
FLINT and PARI independently compute the exact resultants of all `1,232`
full-conductor vectors and agree entry by entry. Their common maximum is the
248-bit integer in the statement, with `4*N_max<2^250`. Therefore no primitive
exception can vanish modulo a pair-feasible row prime. These cases exhaust
profile `(6,6)`. QED.
