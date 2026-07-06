# mixed_radix_frontier

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['tex/proximity_blueprint_v3.tex']

## Statement

LIKELY VACUOUS — the standard reading of 'smooth' in the FRI/STARK proximity literature is 2-smooth (power-of-2 order), and every repo row is 2-power. The live prize page leaves it undefined, so the ePrint confirmation (Q0.1 freeze row) closes this. IF the official family were broader: (a) wp0_2's conservativity sketch — 2-power domains are the MOST quotient-rich, so the adverse analysis is conservative for broader smooth classes; (b) the residual work would be lattice-compatible restatements of chain-ordered tools (dedup, tower descent), a repair job priced by the E8 toy.

## Attack surface

audit which arguments used chain structure (first-match dedup ordering, tower descent, scale recursion composition) vs which are per-M and lattice-agnostic (periodic strata counts, f_scale_recursion, coset dynamics per M); the lattice-forced analogue of multi-scale resonance (E5/R1) is the danger zone

## Falsifier

the n=48 toy row (E8): any 2-power-verified invariant failing on the first mixed-radix row

## Ledger (migrated notes)

RESOLVED VACUOUS 2026-07-03: blueprint line 102 defines smooth DEFINITIVELY: 'a multiplicative coset of a subgroup of power-of-two order.' The family is 2-power only; this node is vacuously satisfied. E8 permanently canceled. One nuance recorded: domains are COSETS gamma*H, not just subgroups — harmless (x -> gamma*x is a degree-preserving substitution, code equivalent up to coordinate scaling) but conventions should note it. (rules_freeze req edge removed: the vacuity rests on the blueprint's definition, already quoted, not on the freeze artifact.)
