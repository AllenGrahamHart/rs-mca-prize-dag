# E1 prize N=256 profile-(3,6) cofactor-514 exclusion

- **status:** PROVED
- **closure:** dual exact radius census plus dual exact norm ledger
- **scope:** prize-envelope `N=256`, profile `(3,6,S=18)`
- **dependency:** energy-adaptive product windows

There is no profile-`(3,6,S=18)` prize collision with norm cofactor

```text
m=514.
```

The parent leaves nine exact `(E,q)` chambers in `E=7,...,11`. A complete
123196-affine-orbit census finds only twelve normalized vectors: four at
`(E,q)=(8,4)` and eight at `(10,6)`. Exactly eight vanish at a primitive root
modulo 257. FLINT and PARI/GP agree on all eight cyclotomic norms, and every
quotient `Norm/514` is below the prize interval.

This removes cofactor `514`; seven profile-`(3,6)` cofactors remain.
