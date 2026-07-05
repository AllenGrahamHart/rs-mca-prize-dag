# h4_sparse_norm_gate conditional proof

## Predicate nodes

- `a_universal_trade_variety`
- `a3_good_reduction_lemma`
- `a_closure_assembly`

## Claim

The h=4 sparse norm-gate residue, read in the x83-generalized window form used
by downstream consumers, is excluded at the official rows, conditional on the
assembly certificates and row GCD tests named by `a_closure_assembly`.

## Proof

The proved node `a_universal_trade_variety` puts the h-window trades on the
universal torsion variety `W_h`, so the h=4 residue is a fixed algebraic
problem rather than a row-by-row search problem. The proved node
`a3_good_reduction_lemma` says that any extra primitive residue modulo an
official-row prime must come from a finite computable exceptional set, detected
by the corresponding resultant/GCD divisibility tests.

For h=4, the x32 terminal dichotomy leaves exactly two branches: the antipodal
quotient branch, already paid by the existing ledger, and the top-level
8-sparse norm-gate branch. The proved x83 uniform obstruction gate is the same
dichotomy for every live h-window: after the paid full-fiber branch, any
remaining primitive event is a p-specific cleared obstruction norm. The
predicate `a_closure_assembly` asserts that the needed certificates exist and
that the official row primes pass the GCD tests. Under those predicates, the
exceptional set contributes zero primitive residue at the official rows.

Therefore the h=4 norm-gate node follows from the universal-variety,
good-reduction, and closure-assembly predicates.
