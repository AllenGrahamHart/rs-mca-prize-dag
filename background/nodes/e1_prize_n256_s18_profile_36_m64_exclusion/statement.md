# E1 prize N=256 profile-(3,6) cofactor-64 exclusion

- **status:** PROVED
- **closure:** exact product ledger, dual complete radius census, and certified norm intervals
- **scope:** prize-envelope `N=256`, profile `(3,6,S=18)`
- **dependency:** energy-adaptive product windows

There is no profile-`(3,6,S=18)` prize collision with norm cofactor

```text
m=64.
```

Exact parity and product certification reduces the parent range
`E=2,...,65` to 255 possible `(E,q,L)` triples, all with `E<=46`. Separate
complete atlases cover 8256 primitive and 4480 all-one-parity singleton-support
orbits, for 12736 affine orbits in total.

Independent direct-triple and reverse hash-block radius engines find 7191566
product-live signed vectors. Certified 48-bit root intervals put 7191424
strictly below the allowable `64p` interval and 142 strictly above it; no
interval is unresolved.

This removes cofactor `64`; five profile-`(3,6)` cofactors remain.
