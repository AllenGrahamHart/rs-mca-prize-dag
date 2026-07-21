# conditional proof: list_grand

- **status:** CONDITIONAL
- **closure:** proof

## Predicate nodes

- `s0_zero_open`
- `mixed_radix_frontier`
- `list_large_m_scope_closure`

## Evidence/support nodes

- `list_safe`
- `list_unsafe`
- `list_adjacency_closing`

## Claim

Conditional on the predicate nodes, for each admissible code `C` and constant
interleaving arity `m`, the list grand challenge has an adjacent agreement
index where `|Lambda|` crosses `2^-128 |F|`.

## Proof

The node `list_large_m_scope_closure` states the operational list-grand
content: from the ordinary-code crossing supplied by
`list_adjacency_closing`, it proves for every constant `m` that the same
adjacent agreement indices satisfy

```text
sup_U |Lambda(U, delta - 1)| > eps*|F| >= sup_U |Lambda(U, delta)|.
```

The safe equality is supplied by the proved sub-square-root projection theorem,
and diagonal tuples preserve the unsafe witness. Thus the safe and unsafe
inequalities are not separate logical predicates at this top layer. The proved
node `s0_zero_open` supplies the object/axis convention needed to identify the
displayed crossing with the official list challenge, and
`mixed_radix_frontier` supplies the admissible-domain guard.

Therefore the list grand statement follows from the three predicate nodes
above. The nodes `list_adjacency_closing`, `list_safe`, and `list_unsafe`
remain useful support and diagnostic evidence at this layer. The first is
already a transitive requirement of `list_large_m_scope_closure`; the other
two are not additional premises of this assembly implication.

## Ledger

WEAKENING 2026-07-06: `list_safe` and `list_unsafe` were demoted from logical
requirements to evidence.

SCOPE REPAIR 2026-07-18: `list_adjacency_closing` was narrowed to the only
instance required by the corridor proof, `m=1`. The proved arity transport in
`list_large_m_scope_closure` is now the direct root predicate. This makes the
packet agree with the live DAG and removes arbitrary arity from the open
corridor mathematics.

## WAVE-11 ADDENDUM (2026-07-18)

The rate-half low-budget list branches (B* in {1,2}) are delivered
unconditionally at every arity (all-arity crossing node + fail-closed
certificate generator, both PROVED, ev-wired). No status change.
