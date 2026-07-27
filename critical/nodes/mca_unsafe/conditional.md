# conditional proof: mca_unsafe

- **status:** CONDITIONAL
- **closure:** proved implication

## Predicate nodes

- `cap_theorem`
- `unsafe_at_crossing`

## Claim

At the candidate adjacent endpoint, `B_C(a_safe-1) > B*`.

## Proof

`cap_theorem` places the candidate inside the universal unsafe cap. The
row-specific adjacent inequality is supplied by `unsafe_at_crossing`. Together
they establish the printed unsafe-side claim. `zone_b` is one possible route
for constructing the crossing payload, but is not a third logical premise once
the universal row-specific witness theorem is assumed.
