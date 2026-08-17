## Work cycle 407: rank-eleven rich-container incidence collisions

### Pins

- starting Codex pin: `9016d4a07`
- canonical Fable prize pin: `c31605f55`
- upstream main pin: `93fba1be3f3299b0ba4708d88715377bbb656e45`
- upstream rich-flat tip: PR `#1173` at `2788d5ec3`

### Finite route triage

The one-witness joint raw-clipped support-4/5/6 LP was tested only as a
floating-point route probe. Both HiGHS algorithms agree, but the estimated
repaired premium remains above the K'=88 leader by about
`5.088564702309253e45`. No exactification or larger finite scan is justified;
the result has no proof status.

### Result: PROVED structural compiler

The exact 508-container population from work cycle 404 now has a collision
compiler. Choose 42453 actual zero coordinates from each container. Discrete
convexity of coordinate incidence degrees gives:

```text
one coordinate in at least 21 containers;
one pair with at least 1640 common actual zeros;
one triple with at least 61 common actual zeros.
```

The pair span has dimension at most 6 and the triple span at most 9. Also,
254 containers have one common dimension `r in {2,3}`. In that typed
subfamily the thresholds are 11 containers through one coordinate, a pair
with 1562 common zeros and span dimension at most `2r`, and a triple with 52
common zeros and span dimension at most `3r`.

Primary and independent exact-integer verifiers reproduce every incidence
total and ceiling. No locator equality, global core, or chronology owner is
asserted.

### Burn-down

- critical node attacked: `rate_half_band_crossing_location`
- DAG delta: one background `PROVED` incidence-collision compiler
- critical status delta: none
- route delta: the 508-container target now emits explicit low-span pair and
  triple common-core inputs; the naive K'=88 finite carrier route is retired
- upstream delta: compact strengthening suitable for PR `#1173`
- new assumptions: none
- next route-deciding action: combine the dimension-at-most-six 1640-core
  pair and dimension-at-most-nine 61-core triple with a Wronskian or
  chronology-safe coalescence theorem; do not infer full locator
  synchronization from these intersections
