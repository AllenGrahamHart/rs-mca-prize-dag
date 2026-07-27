# conditional: e1_official_prime_exception_control

## Predicate nodes

- `e1_folded_certificate_soundness`
- `e1_official_typicality_or_certificate`
- `e1_open_cell_control_payload`

## Claim

Conditional on admissible-family typicality or completed named-exhibit folded
certificates, the E1 exceptional-set predicate holds.

## Proof

The proved folded-certificate soundness predicate says that, for 2-power
rows, a complete folded search with no nonzero folded kernel vector excludes
all non-quotient E1 collisions beyond the cyclotomic/antipodal relations.

The `e1_official_typicality_or_certificate` predicate is now a conditional
assembly from route soundness and `e1_open_cell_control_payload`. That payload
is in turn conditional on the named folded-certificate manifest, which
supplies the row input needed to use the proved soundness: the folded
certificate procedure is completed for named exhibit fields and returns the
certified no-vector verdict.

In either case, incidence with the non-quotient exceptional set is negligible
relative to the signed-core quotient count. That is exactly the statement
required here.
