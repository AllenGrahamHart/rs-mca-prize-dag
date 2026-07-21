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

the hardness SWAPS sides vs MCA: unsafe witnesses are CONSTRUCTIVE (planted families = explicit codewords), the safe half is imgfib + integrality; the residue is worst-word extremality + exact planted arithmetic

## Falsifier

n/a (composite obligation)

## Weakening Applied 2026-07-06

The direct `worst_word_planted` input is support/evidence for this node, not a
separate logical premise.  The exact arithmetic child
`list_planted_arithmetic` already consumes worst-word extremality and challenger
pricing, then supplies the priced two-column crossing arithmetic used here.

## Ledger (migrated notes)

AUDITED TRUE RED (ring-1 sweep): the local content is the final quantitative corridor arithmetic — not promotable by referee argument; this is genuine open work.

## Scope repair 2026-07-18

The former statement quantified over every constant `m`, even though the
12 July arity theorem consumes only its `m=1` instance. Narrowing this node to
the ordinary crossing removes that redundant and unsupported burden while
preserving every consumer through `list_large_m_scope_closure`.
