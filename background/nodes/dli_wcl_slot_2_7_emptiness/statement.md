# WCL slot (2,7) emptiness

- **status:** TARGET (minted 2026-07-19 at the WCL amber ceremony)
- **consumer:** `dli_wcl_zone_coverage` (req)

At every official row, no reduced signed weight-7 polynomial P has
P(w) = P(w^3) = 0 for w of exact order 1024 (the ell=2 window; sibling
slots (2,5)/(2,6) are CLOSED by the audited norm-gcd and recursive-norm
certificates — the same machinery is the natural attack here).
FALSIFIER: one official-admissible prime with such a double vanisher.
