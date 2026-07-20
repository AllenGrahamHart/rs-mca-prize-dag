# Claim contract

- **claim id:** `f3_hge4_near_third_belyi_necklace_bound`
- **status:** `PROVED`
- **mathematical statement:** every primitive non-full exact-level pair with
  `0<e=m-3h<h` produces a tame central-star Belyi map, and its ordered
  scaling orbit count is at most twice the binary-necklace number
- **scope:** dyadic `m`, field containing `mu_m`, characteristic zero or
  greater than `4h+e`; the official corridor satisfies this
- **dependencies:** `f3_hge4_complement_separator_defect_normal_form`,
  `tame_central_star_belyi_necklace_bound`
- **consumers:** `f3_hge4_near_third_dual_gap_exclusion`,
  `f3_hge4_norm_gate_count`
- **new open content:** near-third necklaces not fitting the level budget,
  every `e>=h` width, and the complete retained aggregate
- **falsifier:** an in-scope pair violating `(NTB1)--(NTB4)`, two unordered
  pair orbits above one geometric map, or a wrong debit in `(NTB5)--(NTB6)`
- **nonclaims:** necklace realizability, complete level payment, or primitive
  emptiness
- **replay:** `python3 background/nodes/f3_hge4_near_third_belyi_necklace_bound/verify.py`
  and `verify_audit.py`
