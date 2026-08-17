# Audit

1. The proof selects exactly 508 containers, so no monotonicity assertion in
   the unknown larger bucket count is needed.
2. Excess zeros are discarded to reduce every selected set to size 42453;
   all resulting bounds remain lower bounds for the original intersections.
3. The convex incidence minimum uses integer degrees 20/21 for 508 sets and
   10/11 for the typed 254-set subfamily.
4. Pair and triple conclusions use ceilings of averages, not floors.
5. The same-dimension subfamily follows only from two possible dimensions;
   it does not assume whether dimension two or dimension three is dominant.
6. Vanishing passes to a sum of polynomial spaces only on the intersection
   of their actual zero sets. No union-of-cores claim is made.
