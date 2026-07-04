# corridor_ledger

- **status:** TARGET
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/proof_sketch/s2_paid_ledger.md']

## Statement

Exhaustive over the three clean rates: with W = the current corridor widths (1.12-2.17 grid steps), the three eaters — acl_second_order (i), corridor_window_cleanup (ii), corridor_ext_crossing (iii) — jointly recover at least W(rate) - 1 grid steps, collapsing the bracket to adjacency. Pure arithmetic ONCE the eaters' numeric outputs exist (evidence-gated on them); this node is the future assembly implication of adjacency_closing. If the sum falls short at any rate: the determination lands bracket-grade there — the honest failure mode, priced.

## Attack surface

a three-row table; each entry an interval comparison

## Falsifier

any rate where the eater intervals cannot reach W - 1

## Ledger (migrated notes)

THE REQUIRED-MAGNITUDE TABLE (agent, exact, identity (i)+(ii)+(iii) = W-1 verified): X_acl(1/4) >= 0.367, X_acl(1/8) >= 0.023, X_acl(1/16) >= 0.304 grid steps. RATE 1/8 IS ~0.02 STEPS FROM ADJACENCY. The ledger is now pure arithmetic conditional on acl_second_order delivering these magnitudes.
