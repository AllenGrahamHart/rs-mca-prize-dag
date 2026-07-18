# conditional proof: list_grand

- **status:** CONDITIONAL
- **closure:** proof

## Predicate nodes

- `s0_zero_open`
- `mixed_radix_frontier`
- `list_adjacency_closing`

## Evidence/support nodes

- `list_safe`
- `list_unsafe`

## Claim

Conditional on the predicate nodes, for each admissible code `C` and constant
interleaving arity `m`, the list grand challenge has an adjacent agreement
index where `|Lambda|` crosses `2^-128 |F|`.

## Proof

The node `list_adjacency_closing` already states the operational list-grand
content: for each admissible row and constant `m`, it exhibits adjacent
agreement indices satisfying

```text
sup_U |Lambda(U, delta - 1)| > eps*|F| >= sup_U |Lambda(U, delta)|.
```

Thus the safe and unsafe inequalities are not separate logical predicates at
this top layer; they are part of the closing node's conclusion.  The proved
node `s0_zero_open` supplies the object/axis convention needed to identify the
displayed crossing with the official list challenge, and
`mixed_radix_frontier` supplies the admissible-domain guard.

Therefore the list grand statement follows from the three predicate nodes
above.  The nodes `list_safe` and `list_unsafe` remain useful support and
diagnostic evidence for the lower-level route, but they are not additional
premises of this assembly implication.

## Ledger

WEAKENING 2026-07-06: `list_safe` and `list_unsafe` were demoted from logical
requirements to evidence.  This uses the already-repaired
`list_adjacency_closing` statement, whose conclusion includes both sides of
the adjacent crossing.  Same three-rate pivot applies (list side mirrors:
clean extras-zero margins at 1/4-1/16; the rate-1/2 band is a list-side
object).  The m-quantifier is carried by `list_adjacency_closing` through
`rules_m_reading`.

## WAVE-11 ADDENDUM (2026-07-18)

The rate-half low-budget list branches (B* in {1,2}) are delivered
unconditionally at every arity (all-arity crossing node + fail-closed
certificate generator, both PROVED, ev-wired). No status change.
