# Wave-40 audit — the positive atlas collapses to one representative

**Date:** 2026-08-02. **Planner:** Fable. **Range:** `74c54792..9e0b5dd2`
(12 Codex commits, 08-02 ~08:00-13:12, fetched from the
`prize-codex-resolution-v10-20260722` worker checkout, branch
`codex/full-prize-resolution-v10-20260722`). **Verdict: CLEAN —
integrated in full.**

```text
math orbit  241 = 179/38/24  ->  241 = 179/38/24  (unchanged)
nodes 1720 -> 1732 (+12 Codex; the sandwich mint carried through)
edges 4718 -> 4773 (+55)
new node verifiers 12/12 PASS      validators PASS post-merge
merged dag.json: canonical TRUE, dup ids 0, dup edges 0
```

## What fell

Five of the six remaining positive 433-1a representatives closed in one
wave, all by the guard-factorization template matured in the cell-five
program (wave 39):

- **[3,6]**: the genus-THREE plane-kernel reduction (the compact model
  whose degree-eight square-free right side has genus 3; FLINT
  denominator clearing + 16 pseudo-division steps), exceptional scale
  charts (every omitted univariate scale factored exactly, all deployed
  roots on printed guards), then the signed-pair guard factorization
  closes the orbit. Six raw rows.
- **[4,7]**: genus-ONE plane-kernel reduction; signed-pair projection
  reconstruction; exceptional coefficient projection decomposition +
  reconstruction colored exclusion + scale charts; main projection
  guard factorization. The heaviest cell of the wave (7 nodes).
- **[14]**: complete plane-reduced signed-pair resultant factors as
  `N0 D0^5 (w0+1)^2 (rd^2 w0 - rn^2)(rd^2 w0 + rn^2)`; degree-2752
  proportionality norm factored exactly; root-sign symmetry closes all
  four raw rows without colored elimination.
- **[12,13]**: analogous factorization with `(rd^2 w0 + rn^2)^2`; the
  one proper compact-scale root has exactly two deployed common points,
  replayed raw at both — only original guards. Eight raw rows.
- **[11]**: degree-2664 leading norm, one proper non-scale fiber whose
  twelve displayed roots are all original guards. Four raw rows.

**The positive frontier is now ONE representative / eight raw rows:
`[9,10]`** (compact cell 9, lex basis size eleven; closure transports
to cell 10). At wave 38 the atlas had 13 routes; at wave 39, six
representatives / 40 rows; now one.

## Operational notes

- Canonical writer discipline held (their dag.json canonical: True,
  no duplicate ids — the wave-38 regression stays fixed).
- The git auto-merge of dag.json happened to be textually clean this
  time; per standing procedure it was NOT trusted: the merged file was
  re-parsed and re-checked for counts (1732/4773 exact), id/edge
  uniqueness, canonical form, and presence of both lineages' nodes.
- Modal discipline continues (guard-saturated bases at the 250s cap
  retired with "no mathematical conclusion is drawn" — the [3,6]
  attack.md note); the genus-3 chart work explicitly fences dead
  timeout runs from conclusions.
- Codex's line branched from the wave-39 pin and does NOT carry our 16
  pilot-campaign commits (the five-lane audits, the mint, the ledger);
  it will pick those up at its next merge of master. Expect its
  planning to absorb: the sandwich mint (its lane-neighbor),
  the FM3/|Gamma| re-target, and the Route T fork memo.
- Export watch unchanged: #1143 last pushed "Complete positive 433-1a
  target elimination" (08-01 17:46, the rs-mca-codex-positive-three-loop
  checkout); the wave-40 cell closures are NOT yet exported upstream —
  next export nudge should include them. Diagonal-node watch stands.

## Verification

12/12 new node verifiers PASS (ramguard local, this session);
verify_prize_dag PASS (structure, refs, acyclicity, reachability,
status propagation; three pre-existing warnings unchanged);
ORBIT_CENSUS_PASS math=241(179/38/24) submission=256(191/40/25).
Frontier narrative cross-checked against the attack.md diff tail; the
three displayed resultant factorizations and the 2752/2664 degrees are
as printed in the node statements (spot-read).

## Assessment

The guard-factorization template is now a proven production line: five
representatives in one wave, each by the same pattern (complete
plane-reduced resultant -> exact factorization into printed guards ->
exceptional charts/fibers replayed raw -> symmetry closes raw rows).
One representative stands between the positive campaign and the
compose-stage of the (4,2) order-two row. After [9,10]: the diagonal
orientation (Scott's lane per the #1139 split — coordination watch),
the (8,1) row, and composition into rate_half_band_closure, which is
when the census finally moves.
