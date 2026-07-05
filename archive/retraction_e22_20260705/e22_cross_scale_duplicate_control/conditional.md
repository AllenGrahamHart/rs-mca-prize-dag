# conditional: e22_cross_scale_duplicate_control

## Predicate nodes

- `e22_cross_scale_rootset_recovery`
- `e22_cross_scale_equivalence_specification`

## Claim

Conditional on the exact cross-scale equivalence specification, all duplicate
E22 staircase representations across different quotient moduli are declared
quotient-equivalence/cross-scale degeneracies.

## Proof

The proved `e22_cross_scale_rootset_recovery` node reduces any equality of two
staircase locators at different moduli to equality of one root set. It also
recovers, at each fixed modulus, the corresponding tail and selected quotient
fibers from that root set.

The predicate `e22_cross_scale_equivalence_specification` supplies the
remaining classification: every equal-support pair is represented by the
canonical support-scale data and is counted with the intended pricing
multiplicity.

Therefore an alleged undeclared duplicate would have to be an equal-support
pair not covered by the equivalence specification, contradicting that
predicate. Hence all cross-scale duplicates are exactly the declared
degeneracies.
