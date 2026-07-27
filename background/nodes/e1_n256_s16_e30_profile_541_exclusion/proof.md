# Proof

Let `O` be the symmetric set of the six distinct light-light differences.
In profile `(5,4,1)`, five positive classes have magnitude one, four have
magnitude two, and one has magnitude three. Thus the six odd classes are
exactly `O`. Choose the one class `P` promoted from magnitude one to three and
the four classes `E` outside `O` having magnitude two. The absolute
autocorrelation on the full cyclic group is

```text
b = 1_O + 2*1_(P union E).                            (1)
```

The exact mask atlas classifies all 280,720 normalized six-odd light supports
into 1,234 odd masks and proves that every mask has exactly one affine
light-support orbit. For each mask, (1) has `6*binom(57,4)` assignments.

The production relaxation enumerates normalized vertex triples and evaluates
the cubic trilinear expansion through a signed zero-sum kernel. The audit
independently enumerates positive circular gaps and constructs its kernel from
pair-sum tables. Their 64 shards agree row by row on all 2,924,654,040
assignments, the complete 1,456-entry exceptional list, and maximum 1278.
Every nonexceptional assignment has `M_3<=1087`, so the proved cubic-Hermite
criterion puts its norm below `2^250`.

The exceptional list occupies 321 odd masks and hence exactly 321 affine
light-support orbits. The folded-chord engine and independent direct-
negacyclic engine choose all heavy triples and 64 relative sign vectors for
each orbit. They agree on every row after 6,371,187,456 vectors per engine:

```text
profile vectors             45,846
M_3>1087                       440
M_3>1087, full conductor        86.
```

The proper-conductor theorem excludes the complementary 354 vectors. FLINT
and PARI independently compute exact resultants for the 86 full-conductor
vectors and agree on every norm. Their common maximum is the 247-bit integer
in the statement and satisfies `12*N_max<2^250`. Hence no exceptional vector
can vanish modulo a pair-feasible row prime. These cases exhaust profile
`(5,4,1)`. QED.
