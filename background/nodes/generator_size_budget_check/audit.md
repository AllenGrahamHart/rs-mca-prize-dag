# Audit

- The refutation does not dispute the raw integer count in `(GSB1)`.
- It distinguishes subset multiplicity from the all-pairs-distinct `e_1`
  centers consumed by `certified_valueset_lower`.
- The zero-sum padding identity holds in every characteristic because each
  padding block is exactly `{x,-x}`.
- The upper bound permits collisions between different signed cores; such
  collisions only reduce the number of centers further.
- The all-signs bound removes any dependence on the undocumented choice of
  the 19 sign patterns.
- This kills only the signed-8-core padding route. It does not refute the
  broader `generator_economy` construction target.
