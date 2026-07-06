# list_adjacency_closing

- **status:** TARGET
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s7_list_side.md']

## Statement

For each admissible row and constant m: exhibit adjacent delta with sup_U |Lambda(U, delta-1)| > eps*|F| >= sup_U |Lambda(U, delta)| (per the official m-quantifier). The determination's list half, previously unpriced — the exact mirror of adjacency_closing.

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
