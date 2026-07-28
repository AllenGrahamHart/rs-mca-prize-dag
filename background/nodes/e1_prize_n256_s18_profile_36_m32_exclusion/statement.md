# E1 prize N=256 profile-(3,6) cofactor-32 exclusion

- **status:** PROVED
- **closure:** exact product ledger, dual complete radius census, and certified norm intervals
- **scope:** prize-envelope `N=256`, profile `(3,6,S=18)`
- **dependency:** energy-adaptive product windows

There is no profile-`(3,6,S=18)` prize collision with norm cofactor

```text
m=32.
```

Exact parity and product certification reduces the parent range `E=2,...,85`
to 474 possible `(E,q,L)` triples, all with `E<=60`. Odd multiplicity five
forces a primitive singleton support, and a complete atlas covers 19,840
affine support orbits.

Independent forward and reverse complete radius engines find 239,131,808
product-live signed vectors. Certified 48-bit root intervals put 239,131,588
strictly below the allowable `32p` interval and 220 strictly above it; no
interval is unresolved.

This removes cofactor `32`; four profile-`(3,6)` cofactors remain.
