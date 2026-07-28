# E1 prize N=256 profile-(3,6) cofactor-512 exclusion

- **status:** PROVED
- **closure:** dual exact radius census plus dual exact norm ledger
- **scope:** prize-envelope `N=256`, profile `(3,6,S=18)`
- **dependency:** `e1_prize_n256_s18_profile_36_bounded_product_windows`

There is no profile-`(3,6,S=18)` prize collision with norm cofactor

```text
m=512.
```

Cofactor `512` forces singleton multiplicity `mu=9`. The bounded product
window leaves `E=V/2` in `{2,...,17}`. Two independent exact radius engines
reduce this complete chamber to four normalized vectors: two at `E=15` and
two at `E=17`. FLINT and PARI/GP agree on all four cyclotomic norms, and every
quotient `Norm/512` is below the prize interval.

This removes cofactor `512`; eight profile-`(3,6)` cofactors remain.
