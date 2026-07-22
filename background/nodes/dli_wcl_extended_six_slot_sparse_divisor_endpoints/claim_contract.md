# Claim contract

- **claim id:** `dli_wcl_extended_six_slot_sparse_divisor_endpoints`
- **status:** `PROVED`
- **claim:** `(XW1)--(XW8)`, the six exact squared-root divisor reductions,
  pruned straight-line sizes, characteristic-zero unit ideals, and raw-route
  lower bounds in `statement.md`
- **consumers:** `dli_wcl_slot_1_7_emptiness`,
  `dli_wcl_slot_1_8_emptiness`, `dli_wcl_slot_2_8_emptiness`,
  `dli_wcl_slot_2_9_emptiness`, `dli_wcl_slot_4_10_emptiness`,
  `dli_wcl_slot_4_11_emptiness`, and `dli_wcl_zone_coverage`
- **new open content:** compute and independently check one nonzero integer
  certificate per slot, factor enough of it to exclude every compatible
  official characteristic, and retain the reduced-support correspondence
- **falsifier:** a reduced relation not transported by the displayed parity
  form; a divisor tuple whose reconstruction fails; a size-table mismatch;
  or a nonempty antipodal-free characteristic-zero root subset with zero sum
- **nonclaims:** no `Delta` is computed; no finite characteristic is excluded;
  fixed-dimensional does not imply cheap; none of the six target statuses
  changes

