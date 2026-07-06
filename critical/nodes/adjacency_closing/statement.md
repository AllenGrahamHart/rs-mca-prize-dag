# adjacency_closing

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

For each admissible row: the proved safe agreement a and proved unsafe agreement a-1 are ADJACENT — the bracket between the two sides collapses to one grid step. Current per-rate corridor widths are 1.12-2.17 grid steps: even with every mapped conjecture closed, the slack must be eaten by (i) the Acl second-order term (makes the quotient end a number), (ii) per-point window cleanup at the boundary, and (iii) the extension-crossing arithmetic — or the determination lands with a gap and only bracket-grade partials.

## Attack surface

rate-by-rate: compute which corridors provably collapse under acl_second_order alone (width 1.12 = rho 1/8 is closest); the 506/507 pinned row is the existence proof that adjacency IS achievable where tangent exactness rules

## Falsifier

a rate whose bracket provably CANNOT collapse to one step under the mapped mechanisms — would mean the prize needs a mechanism not yet on the map

## Ledger (migrated notes)

the assembly implication of mca_grand made explicit (same move as payment_completeness): the composite says 'adjacent' but nothing priced the meet until now. The least-clear remaining path on the map after the mixed-radix downgrade. | WIRING REPAIR (mca_grand referee audit 2026-07-04): rate_half_coverage_gap promoted ev -> req — an uncovered radius band at rate 1/2 BLOCKS the for-each-admissible-C quantifier; the list-side closing node already had it as req (asymmetry caught by the audit). | AUDITED TRUE RED (ring-1 sweep): the local content is the final quantitative corridor arithmetic — not promotable by referee argument; this is genuine open work. | DECOMPOSED (meaty-red program, 2026-07-04): the statement's own three eaters node-ified — (i) acl_second_order (existing), (ii) corridor_window_cleanup (evidence-gated finite computation), (iii) corridor_ext_crossing (arithmetic on proved components) — assembled by corridor_ledger (the per-rate W - 1 table, the node's future implication packet). The list mirror decomposes identically next pass. | CONDITIONAL (Codex critical pass): the local assembly implication is now explicit; the node remains blocked by its predicate nodes, especially rate_half_band_closure and the knife-edge/aperiodic corridor inputs.
