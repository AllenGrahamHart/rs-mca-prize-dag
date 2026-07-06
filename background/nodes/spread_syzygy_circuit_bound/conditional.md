# spread_syzygy_circuit_bound conditional proof

## Predicate nodes

- `circuit_nongeneric`
- `circuit_locus_density`
- `circuit_pricing`

## Claim

The full-support minimal-circuit exception branch contributes within the
spread budget.

## Proof

By `circuit_nongeneric`, a full-support minimal circuit can occur only on the
explicit determinantal locus where the two syzygy identities have a
one-dimensional intersection kernel. Thus circuits are not a generic spread
family; they are confined to named algebraic exceptional cells.

By `circuit_locus_density`, those cells have q-suppressed density by
Schwartz-Zippel after summing over the relevant support choices. This gives
the FM-compatible count of circuit-carrying configurations.

Finally, `circuit_pricing` says each minimal circuit has only O(1) unpaid
slope contribution, unless it falls into the paid/structured branch of the
deficiency-one eliminant dichotomy. Multiplying the q-suppressed circuit count
by the O(1) per-circuit slope cost gives the required bound for the branch.

