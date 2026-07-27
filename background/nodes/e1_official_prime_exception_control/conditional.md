# Retired finite-exhibit conditional

This implication is valid only for rows covered by the named folded
certificates. It is not a conditional proof of the current route-uniform
target and must not be used for status propagation; see `status_ruling.md`.

## Predicate nodes

- `e1_folded_certificate_soundness`
- `e1_official_typicality_or_certificate`
- `e1_open_cell_control_payload`

## Historical claim

Conditional on admissible-family typicality or completed named-exhibit folded
certificates, the E1 exceptional-set predicate holds.

## Finite-scope proof

The proved folded-certificate soundness predicate says that, for 2-power
rows, a complete folded search with no nonzero folded kernel vector excludes
all non-quotient E1 collisions beyond the cyclotomic/antipodal relations.

The `e1_official_typicality_or_certificate` predicate is now a conditional
assembly from route soundness and `e1_open_cell_control_payload`. That payload
is in turn conditional on the named folded-certificate manifest, which
supplies the row input needed to use the proved soundness: the folded
certificate procedure is completed for named exhibit fields and returns the
certified no-vector verdict.

On a row satisfying those finite premises, incidence with the non-quotient
exceptional set is controlled relative to the signed-core quotient count.
Nothing in this argument transports the conclusion to an arbitrary
pair-feasible admissible row, which is the quantifier in the current target.
