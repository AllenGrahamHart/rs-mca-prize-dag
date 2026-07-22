# list_adjacency_closing

- **status:** see dag.json (single source of truth; dag status CONDITIONAL) [header retrofit 2026-07-10, catch #69 — was: TARGET]
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s7_list_side.md']

## Statement

For each admissible row, for the ordinary code (`m=1`), exhibit adjacent
agreement indices `a0,a0+1` with

```text
L_1(a0) > floor(|F|/2^128) >= L_1(a0+1).
```

This is the exact remaining base-list closing obligation. The proved
conditional node `list_large_m_scope_closure` transports the same adjacent pair
to every constant interleaving arity; arbitrary `m` is not open content of
this node.

## Attack surface

Unsafe witnesses are constructive. The clean-rate safe half is the
`imgfib`/`codegree` bound behind `list_safe`; its live red input is
`l1_mixed_petal_amplification`. Rate one half has the separate
`rate_half_list_adjacent_crossing` input.

## Falsifier

n/a (composite obligation)

## W3 scope repair

The clean-rate crossing consumes the independent bound nodes directly:

```text
list_unsafe, list_safe, list_corridor_ledger.
```

`list_planted_arithmetic` and `worst_word_planted` are evidence only. Their
former route applied W3's upper inequality at an already unsafe spending
cell; `ww_spending_cell_fiber_layout_counterexample` refutes that all-cell
application, not W3's literal safe-side claim. The unsafe lower witness
remains valid, while the safe side was always supplied by `list_safe`. This
rewire removes the unnecessary dependency without weakening the
adjacent-crossing conclusion.

## Ledger (migrated notes)

Historical ring-1 audits treated the corridor arithmetic as open. The exact
`list_corridor_ledger` has since proved that arithmetic; the only open content
is now carried by the predicate nodes named above.

## Scope repair 2026-07-18

The former statement quantified over every constant `m`, even though the
12 July arity theorem consumes only its `m=1` instance. Narrowing this node to
the ordinary crossing removes that redundant and unsupported burden while
preserving every consumer through `list_large_m_scope_closure`.
