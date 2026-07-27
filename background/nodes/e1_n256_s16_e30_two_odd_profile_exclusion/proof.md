# Proof

The proved E30 profile/parity/light reduction classifies every two-odd light
support into 87 affine odd-unit orbits. Translation and multiplication by an
odd unit preserve the magnitude profile, `M_3`, cyclotomic norm, and conductor
class. For each representative, both census engines choose all three heavy
positions from the remaining 124 positions and all 64 relative sign vectors
after fixing one global sign. Thus each covers exactly

```text
87*binom(124,3)*64 = 1,726,770,432
```

representative vectors.

The production engine folds the 21 unordered chords directly. The audit
engine independently multiplies the coefficient vector by its negacyclic
reverse in `Z[x]/(x^128+1)` and checks the anti-palindromic identities before
extracting the positive half. They agree on every row count, conductor split,
and `M_3` maximum in the statement.

For `(1,5,1)`, every full-conductor vector has `M_3<=1068<1087`; the exact
cubic-Hermite theorem puts its norm below `2^250`. The conductor theorem
excludes the other 4,150 representative vectors.

For `(2,7)`, the cubic bound is not sharp enough. A folded-chord/FLINT engine
and an independent direct-negacyclic/PARI engine therefore compute exact
resultants for all 28,114 full-conductor vectors. They agree on every
per-template count and maximum, retain zero norms at or above `2^250`, and
have the unique global maximum printed in the statement. Its maximizing
vector is

```text
positions    (7,39,103,0,1,20,109),
coefficients (2,-2,-2,-1,1,1,1).
```

Exact integer comparison gives `7*N_max<2^250<8*N_max`. The conductor theorem
excludes the other 16,188 representative `(2,7)` vectors. Both two-odd
profiles are therefore impossible. QED.
