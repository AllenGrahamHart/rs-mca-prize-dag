# list_safe conditional proof

## Predicate nodes

- `imgfib`
- `codegree`

Evidence retained for the superseded direct-arity route:

- `m_sweep`
- `m_handling`

## Claim

The list-safe bound

`#Lambda(C, delta) <= 2^-128 |F|`

above the window follows from the two predicate nodes.

## Proof

The node `imgfib` gives the uniform image-fiber bound above the corrected
reserve. The `codegree` reduction is exactly the conversion from those
image-fiber counts to the ordinary worst-word list cardinality in the
list-safe statement. Substituting the reserve inequality from `imgfib` into
the `codegree` conversion gives the stated `2^-128 |F|` upper bound.

No direct arbitrary-arity estimate is needed here. Once this safe value is
paired with the adjacent ordinary unsafe witness,
`list_large_m_scope_closure` transports the complete crossing to every
constant arity. The older `m_sweep` and `m_handling` packets remain evidence
for the superseded direct route, not hypotheses of this implication.

Thus the local implication is proved; any remaining hypotheses are precisely
the predicate-node hypotheses already visible in the DAG.
