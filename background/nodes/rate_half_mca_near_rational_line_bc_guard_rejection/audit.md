# Audit

## Source custody

The source contract pins upstream `#1160` at its exact head and pins its
counterexample note, certificate manifest, and primary verifier blobs.  It
also pins the local cycle-19 candidate certificate schema used for the guard.

## Independent derivation

The proof does not trust the upstream manifest's recorded
`balanced_slope_count=0`.  It derives rejection from a support locator for
each displayed slope word.  Only an upper bound on the lattice minimum is
needed, so no weak-Popov basis or large-field computation is hidden.

## Scope discipline

This is a necessary-guard regression for a candidate relation.  The known
semantic criticism remains: that relation has not been proved equivalent to
the independently frozen BC first-match cell.  Passing this control therefore
does not establish soundness, coverage, or prize-ledger movement.

## Independence

The primary verifier validates the complete source contract and construction
arithmetic with mutation controls.  The audit verifier retypes only the
minimal constants and reconstructs the support/threshold contradiction by a
separate path.
