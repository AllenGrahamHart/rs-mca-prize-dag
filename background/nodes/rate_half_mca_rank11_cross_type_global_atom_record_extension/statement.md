# Global atom record extension

- **status:** PROVED
- **scope:** the global-atom output of the cross-type weld gauge dichotomy

Assume at least two large pair types occur and every canonical pairwise weld
uses one normalized atom certificate `C_*`. Then exactly one of the following
holds:

1. some one-record replacement packet emits

   ```text
   chi>=2299571;
   ```

2. `C_*` certifies every record owned by every large pair type.

Indeed, fix a type `p`, another type `q`, and the canonical `p`-anchored
packet on edge `{p,q}`. Replacing one of its 18 fixed `p` records by any other
owned `p` record leaves an 18-anchor packet with the same represented types,
the same complete core, and 31 supports in common with the canonical packet.
The shared deck still contains 17 records of `p` and at least five records of
`q`. In the rational branch, pole-simple atom identity makes the replacement
certificate equal to `C_*`.

This is certificate coverage, not a cardinality payment for one global atom.

## Falsifier

A replacement packet losing the degree-18, common-core, pure-locator, or
pole-simple hypotheses; shared overlap below 31; fewer than three records of
either distinguished type; or a rational replacement certificate distinct
from `C_*`.
