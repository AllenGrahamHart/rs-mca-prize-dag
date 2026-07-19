# census_window_arithmetic

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: PROVABLE]
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

For each (rate, candidate A): undecided rows = {admissible q = 1 mod n : floor(q/2^128) in [L(n,A), K(n,A))} — explicit prime-counting windows. Deliverables: the window list, size estimates, and the dodge complement. As L -> K the windows vanish; the census OUTPUT is the map from certification strength to residual undecided rows.

## Ledger (migrated notes)

couples the census to certified_valueset_lower parametrically instead of blocking on it | IN FLIGHT: #195 | Family now definitively pinned (2-power cosets, k <= 2^40, |F| < 2^256): the exposure census is EXACT finite arithmetic — compute the actual number of knife-edge-exposed cells and their prime-window sizes per rate. Coset domains: collision structure identical (multiplication by gamma is a bijection mod p) — one-line lemma to include.
