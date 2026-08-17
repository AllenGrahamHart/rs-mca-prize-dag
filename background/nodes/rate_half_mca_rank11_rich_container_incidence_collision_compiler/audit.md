# Audit

1. The proof selects exactly 508 containers, so no monotonicity assertion in
   the unknown larger bucket count is needed.
2. Excess zeros are discarded to reduce every selected set to size 42453;
   all resulting bounds remain lower bounds for the original intersections.
3. The universe is the anchor-good set `G_0`, not the code dimension `K`.
   The parent proves `|G_0|<=m=1116048`; padding to exactly `m` weakens the
   incidence conclusions and is therefore valid.
4. The convex incidence minimum uses integer degrees 19/20 for 508 sets and
   9/10 for the typed 254-set subfamily.
5. Pair and triple conclusions use ceilings of averages, not floors.
6. The same-dimension subfamily follows only from two possible dimensions;
   it does not assume whether dimension two or dimension three is dominant.
7. Vanishing passes to a sum of polynomial spaces only on the intersection
   of their actual zero sets. No union-of-cores claim is made.
