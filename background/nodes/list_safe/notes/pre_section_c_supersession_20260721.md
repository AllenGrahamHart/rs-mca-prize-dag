# Provenance snapshot (2026-07-21): statement.md + conditional.md immediately
# before the Section C list-corridor supersession (maintainer-ratified this
# date; wave-15 w15-C1). Preserved per custody #104.

## statement.md
# list_safe

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s7_list_side.md#5']

## Statement

#Lambda(C^{==m}, delta) <= 2^-128 |F| above the window: ImgFib bound + codegree conversion + m-handling per the official quantifier.

## conditional.md
# list_safe conditional proof

## Predicate nodes

- `imgfib`
- `codegree`
- `m_sweep`
- `m_handling`

## Claim

The list-safe bound

`#Lambda(C^{==m}, delta) <= 2^-128 |F|`

above the window follows from the four predicate nodes.

## Proof

The node `m_handling` fixes the official quantifier convention: the list
problem is resolved per constant `m`, and `m_sweep` identifies the affordable
constant range required by the campaign. Within that range, `imgfib` gives the
uniform image-fiber bound above the corrected reserve. The `codegree` reduction
is exactly the conversion from those image-fiber counts to the worst-word list
cardinality in the list-safe statement. Substituting the reserve inequality
from `imgfib` into the `codegree` conversion gives the stated
`2^-128 |F|` upper bound, with the `m` convention and range supplied by
`m_handling` and `m_sweep`.

Thus the local implication is proved; any remaining hypotheses are precisely
the predicate-node hypotheses already visible in the DAG.
