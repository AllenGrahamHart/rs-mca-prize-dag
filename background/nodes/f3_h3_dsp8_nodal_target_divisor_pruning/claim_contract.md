# Claim contract

- **claim id:** `f3_h3_dsp8_nodal_target_divisor_pruning`
- **mathematical statement:** positive nodal root overlap is exactly the
  six-value Mobius orbit `(NDP2)`; the target-zero divisor is contained in
  that overlap locus; and the target-one divisor is exactly `(NDP6)`
- **scope:** every official H3 row and every pair of nonnode parameters on a
  common singular trace
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **status:** `PROVED`
- **proved dependency:** the nodal trace parameter router
- **new open content:** bound the records surviving all positive and negative
  collision filters, `(NDP6)`, richness, class, and quotient-line weighting
- **falsifier:** a positive overlap outside `S(a)`, an orbit pair with
  different root multisets, a failure of `(NDP4)` or `(NDP5)`, or a
  signed-disjoint pair with target zero
- **nonclaims:** no irreducibility assertion for the identity divisor, no
  surviving-pair estimate, no DSP8 payment, and no deletion of smooth traces
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_dsp8_nodal_target_divisor_pruning/verify.py`
