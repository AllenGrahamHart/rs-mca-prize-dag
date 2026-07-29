# E1 prize N=256 profile-(3,6) cofactor-256 exclusion

- **status:** PROVED
- **closure:** exact product ledger, dual radius census, and dual exact norms
- **scope:** prize-envelope `N=256`, profile `(3,6,S=18)`
- **dependency:** energy-adaptive product windows

There is no profile-`(3,6,S=18)` prize collision with norm cofactor

```text
m=256.
```

The parent leaves `E=2,...,23`. Exact parity and product certification leaves
45 possible `(E,q,L)` triples, all with `E<=20`. The complete multiplicity-eight
atlas has 5920 affine singleton-support orbits. Independent hash-bucket and
sorted-bucket radius engines find exactly 54 signed vectors in the 45 live
triples: 8 at `E=13`, 6 at `E=15`, 12 at `E=17`, and 28 at `E=19`.

FLINT and PARI/GP agree on all 54 cyclotomic norms. Every norm has 2-adic
valuation eight, and every quotient `Norm/256` is below the prize interval.

This removes cofactor `256`; six profile-`(3,6)` cofactors remain.
