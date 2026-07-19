# corridor_ledger

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: CONDITIONAL]
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/proof_sketch/s2_paid_ledger.md']

## Statement

Conditional assembly: the three-eater corridor ledger is fully numeric and
falls short at every clean rate; rate 1/8 has the sharp residual wedge of
0.00707 grid steps. If fourth_mechanism_rate8 supplies that wedge, the per-rate
ledger closes and adjacency_closing receives the corridor implication. Without
it, the three-eater result is honestly bracket-grade.

## Attack surface

a three-row table; each entry an interval comparison

## Falsifier

any rate where the eater intervals cannot reach W - 1

## Ledger (migrated notes)

Codex red-node pass (2026-07-04): reclassified from TARGET to CONDITIONAL on
fourth_mechanism_rate8. The three-eater arithmetic is complete and negative;
the only live corridor-ledger content is the explicit 0.00707-step
fourth-mechanism wedge. THE REQUIRED-MAGNITUDE TABLE (agent, exact, identity
(i)+(ii)+(iii) = W-1 verified): X_acl(1/4) >= 0.367, X_acl(1/8) >= 0.023,
X_acl(1/16) >= 0.304 grid steps. RATE 1/8 IS ~0.02 STEPS FROM ADJACENCY. The
ledger is now pure arithmetic conditional on acl_second_order delivering these
magnitudes. | LEDGER COMPLETE WITH VERDICT: (i)+(ii)+(iii) delivers LESS than
W-1 at all three clean rates -- bracket-grade under current mechanisms. THE
NEW SHARPEST TARGET: find ~0.007 grid steps (~0.9 bits) at rate 1/8 from a
FOURTH mechanism (cap-end sharpening, tau* reserve tightening, or knife-edge
census pinning) -- the smallest named quantity standing between the campaign
and its first full determination corridor.
