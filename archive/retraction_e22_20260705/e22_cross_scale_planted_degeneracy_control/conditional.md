# conditional: e22_cross_scale_planted_degeneracy_control

## Predicate nodes

- `e22_planted_profile_disjointness`
- `e22_cross_scale_duplicate_control`

## Claim

Conditional on cross-scale duplicate control, the E22 staircase parameters
have exactly the declared degeneracies and no hidden planted overlap.

## Proof

The proved planted-profile predicate shows that every planted sunflower
codeword has the one-petal planted profile: core agreements plus exactly one
full petal, with no background agreements and no second touched petal.
Therefore any nondegenerate staircase challenger in the mixed/full-petal
class is disjoint from the planted family.

The remaining duplicate-control predicate has now been reduced to a precise
cross-scale equivalence specification. Its proved root-set recovery component
shows that duplicate locators are equal supports recovered at two fixed
moduli; the open equivalence-specification component states that all such
equal-support recoveries are exactly the declared quotient-equivalence/
cross-scale degeneracies.

Together these two predicates prove this node.
