# xr_partial_tangent_band

- **status:** TARGET
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/e27_exceptional_pair_census.md']

## Statement

Distinct-slope aligned supports with core r in [k+1, A-2]: subtracting the two alignment identities gives (z1-z2) v = c1 - c2 on the core, so v agrees with a codeword on r >= k+1 points — the pair acquires depth-(r-k) tangent structure (one line, proved two-slope machinery). The work: design the GRADED tangent ledger charging depth-d partially-forced pairs (the s-ladder's worst-case face; #152's t=2 exchange packet is the proved base case), so that every band pair is either charged or upgraded toward the cascade threshold.

## Attack surface

iterate pairwise forcing up the depth grading; the tangent staircase's shape at each depth; E27's machinery calibrates band occupancy at toys

## Falsifier

a toy band family resisting both charge and upgrade (E27's pencil machinery extended to partial cores)

## Ledger (migrated notes)

THE FORCING MAP IS PROVED (X-3 wave): every distinct-slope pair with core r = k+d, 1 <= d <= t-2, forces u = U, v = V on the core — a genuine tangent-depth-d cell; the COMPLEMENTARITY IDENTITY d + s = t (tangent depth + qx13 fresh codim = t exactly). Remaining: the ledger design (charging). Boundary r = k proved to belong with the rank/spread core. | W2 (PR #12, 26,385 checks replayed): the graded ledger DESIGN packet — depth-cell charging table built on the proved forcing map, honest non-promotion (the final ledger bound remains open; the design is the scaffold for it). | A2 (#26, 10/10 replayed): CONDITIONAL-ROUTED, routing table COMPLETE (no extra pairwise/heavy-triangle object); the two occupancy accountings are the only remaining content (nodes added, one shared with A1).
