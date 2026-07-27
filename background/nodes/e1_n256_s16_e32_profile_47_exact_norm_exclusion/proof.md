# Proof

The `V=64` profile reduction and common four-odd router reduce profile `(4,7)`
to 148 affine odd-unit light-support representatives. For each representative,
the three magnitude-two coefficient positions are chosen from the remaining
124 positions. Fixing the first heavy sign positive modulo global negation
leaves 64 sign patterns, so the complete representative coverage is

```text
148 * binom(124,3) * 64 = 2,937,494,528.              (2)
```

Translation and odd cyclotomic automorphism preserve conductor, profile, and
the absolute norm. Negacyclic wrap signs are absorbed by the complete sign
ledger. The proved proper-conductor collision exclusion removes every vector
whose support differences have gcd greater than one with 256. It remains to
pay exactly the full-conductor vectors in (2).

The production engine forms signed folded chord sums and emits precisely the
full-conductor vectors with four magnitude-one, seven magnitude-two, and no
larger autocorrelation coefficients. Python FLINT computes

```text
abs Res_X(X^128+1,F(X))
```

for every emitted vector. It retains 60,148 vectors, finds none with norm at
least `2^250`, and gives the exact maximum `N_max` in (1), attained at

```text
positions     (5,7,9,0,1,2,12),
coefficients  (2,-2,-2,1,1,1,1).                     (3)
```

The audit engine is independent in both stages. It forms the full 128-term
negacyclic product `F(X)F(X^-1)`, checks the constant and antisymmetry
identities, and applies the profile predicate without folded-chord code. It
then sends each polynomial to PARI/GP's exact `polresultant`. It agrees on all
148 per-template counts and maxima, the 60,148-vector total, witness (3), and
the exact integer `N_max`.

Direct integer comparison gives `15*N_max<2^250`. The collision-norm criterion
says a pair-feasible row prime must divide this nonzero integral norm, while
every such prime satisfies `p>=2^250`. This is impossible. Together with the
proper-conductor theorem, all profile-`(4,7)` vectors are excluded. QED.
