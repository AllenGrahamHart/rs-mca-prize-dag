# E1 N=256 E=30 profile-(5,4,1) exclusion

- **status:** PROVED
- **closure:** exact structured relaxation, exceptional census, and norms

At `N=256`, folded profile `(3,4,0)`, and autocorrelation variance `V=60`,
the magnitude profile `(5,4,1)` cannot occur in a pair-feasible collision.

The exact six-odd mask atlas has 1,234 odd masks, each corresponding to one
affine light-support orbit. Two independent relaxations enumerate

```text
1234*6*binom(57,4) = 2,924,654,040
```

compatible magnitude-layer assignments. Exactly 1,456 assignments on 321
odd masks exceed the cubic cutoff `M_3=1087`; the maximum is 1278.

Independent folded-chord and direct-negacyclic engines each test

```text
321*binom(124,3)*64 = 6,371,187,456
```

representative signed vectors over those 321 affine light orbits. They agree
on 45,846 profile vectors, 440 above the cutoff, and 86 above-cutoff vectors
at full conductor. The proved proper-conductor theorem excludes the other
354 vectors.

FLINT and PARI/GP independently compute all 86 full-conductor norms. They
agree on 42 distinct values, none at or above `2^250`, with global maximum

```text
N_max = 147314768947604483837877250659211387932426327951806688176613401078756416516,
12*N_max < 2^250 < 13*N_max.
```

The cubic theorem excludes every nonexceptional assignment, and the exact
norm criterion excludes the 86 primitive exceptional vectors.
