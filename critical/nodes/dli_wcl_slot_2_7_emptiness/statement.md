# WCL slot (2,7) emptiness

- **status:** TARGET (minted 2026-07-19 at the WCL amber ceremony)
- **consumer:** `dli_wcl_zone_coverage` (req)

At every official row, no reduced signed weight-7 polynomial P has
P(w) = P(w^3) = 0 for w of exact order 1024 (the ell=2 window; sibling
slots (2,5)/(2,6) are CLOSED by the audited norm-gcd and recursive-norm
certificates — the same machinery is the natural attack here).
FALSIFIER: one official-admissible prime with such a double vanisher.

The exact four-plus-three router has `94,652,815` affine candidate orbits.
Its two doubling recurrences give independent norm obstructions, but the
measured complete census remains out of scope. The prior `Norm(u)` saturation
gap is repaired embedding-by-embedding: every prime factor of the raw norm
gcd is tested through

```text
H_p^*=gcd(Phi_1024,F,G)/gcd(gcd(Phi_1024,F,G),u),
```

and only positive-degree survivors are reconstructed. In particular, a
rational prime shared with `Norm(u)` is not deleted merely because another
split embedding zeros `u`. This makes the router sound but does not exclude
any survivor, so the node remains `TARGET`.
