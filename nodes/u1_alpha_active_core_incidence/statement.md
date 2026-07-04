# u1_alpha_active_core_incidence

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/h1_u1_toy_harness.md']

## Statement

For a fixed base support `S0`, the sum over active cores
`Q subset S0`, `|Q| = t+1`, of the sporadic full-fiber counts `K_Q^sp` is at
most `n^2`.

## Attack surface

The only live estimate is the anchored non-toral PTE bound; X-10 identifies the
active-core incidence count with that anchored count after the full strip.

## Ledger

P-A observed rare active cores. X-10 reduced the A input exactly to
`anchored_nontoral_pte_bound`; the orbit argument is the transport.
