# deep_link_staircase

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/qx13_pair_rank_ledger.md']

## Statement

For a fixed pair and a fixed aligned support T0: bound the number of aligned supports (distinct slopes) overlapping T0 in the budget-relevant range (roughly (k/2, k) points) by poly(n) — expected staircase-linear. This single lemma rations BOTH heavy-triangle stagnations (beta-2b: every heavy triple contains such a partner pair) AND the total overlap budget for light-triangle stagnations (beta-3c: each stagnation spends k+1 budget, and the staircase bounds the family's total budget). Pairwise machinery is proved (the r < k plateau gives exact 2t-additivity); the staircase is about the POPULATION of near-k partners, the link of T0 at deep sub-cores — where the tangent staircase and top-core cap machineries both point. EVIDENCE-GATED: E33 (count near-k-overlap aligned partners at toys) runs before proof attempts, per the program's strategy.

## Attack surface

PROOF ROUTE SELECTED BY E33 (falsifier never fired, both rows): the link-population cap. Observed: max partner events per anchor 13 (< n) at the corridor row, 72 = 4.5n at the dense stress row — linear shape throughout; and THE key structural signal: partner events through any single fixed subcore max out at 5 on BOTH rows (density-independent). Proof shape: per-subcore rigidity (interpolation at near-k cores — the c(s,t) plateau's boundary) x occupied-subcore accounting. The derived-pencil recursion demotes to a transport tool — no super-linear growth exists for it to explain.

## Falsifier

a toy pair + support with super-linear near-k aligned partners (E33 directly)

## Ledger (migrated notes)

E33 (replayed green): 4096 + 512 anchor samples, observed/expected event counts consistent (870/910, 3734/3522), overlap spectrum concentrated at r = k-2, k-1; no all-slope support code in the near-k band. The lemma is now a shaped transfer target, not an open-ended question. | P1 (PR #13, 32/32 replayed): the E33 route is now ALGEBRAICALLY REDUCED to the named post-strip rich-line cap — the subcore reduction is proved; the raw pre-strip statement is false (rich lines are the paid families). Status stays TARGET pending p1_post_paid_subcore_richline_cap. | PROVABLE via assembly (P1 reduction + U3 charge + E33 constants) — unlocks beta-2b, beta-3c, and closes the rich-line chapter of face 4. | A1 (#24, 9/9): CONDITIONAL-ASSEMBLED — the fixed-subcore rich-line residue is CLOSED post-unified-strip (P1 reduction + F3 charge composed and verified); the one remaining step is the lower-overlap / occupied-subcore ACCOUNTING (how many subcores can be simultaneously occupied — a counting statement over the proved per-subcore cap). Face 4's rich-line chapter is one accounting lemma from done. | Status corrected PROVABLE -> CONDITIONAL: the occupancy accounting is now a formal open requirement (the validator caught the optimistic label).
