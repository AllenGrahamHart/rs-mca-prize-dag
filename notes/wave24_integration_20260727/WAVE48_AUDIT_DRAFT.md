# WAVE-48 AUDIT (Codex delta: v11 cf4699f77..a55acc2fd + v12 to pin f7e850788)

Auditor: Fable, 2026-08-07. Delta: ~2,027 files, 47,546 insertions;
60 nodes added (50 PROVED / 8 TARGET / 2 CONDITIONAL), 6 status
changes, 0 removals; dag 1838 -> 1898 nodes. Codex census claim at
pin: math 231 = 167/36/28, submission 246 = 179/38/29 (recomputed on
my side at integration). Verify chain PASS in Codex's tree.

## VERDICT: ADOPT WHOLESALE BY MERGE, with the post-merge obligations
listed at the end. The wave's centerpiece is an honest, CORRECT
false-green catch on the Conjecture-F chain — verified against
canonical's own texts by this audit — plus a disciplined replacement
program (FPC5) whose new PROVED claims replay clean.

## 1. THE CONJECTURE-F FALSE-GREEN REPAIR — VERIFIED, ACCEPTED

Codex demoted conj_f, f_dim_induction, f_many_sparse_structure,
f_primitive_case PROVED -> CONDITIONAL (notes/CONJECTURE_F_FALSE_
GREEN_AUDIT_20260807.md). I verified the three claimed semantic gaps
against CANONICAL's texts myself:
- GAP 1 CONFIRMED: f_many_sparse_structure/conditional.md:29-30
  says higher-weight accumulation "is transported to the Face-4
  configuration machinery" — a ROUTING claim standing where a
  PAYMENT proof is needed; no owner-aware aggregate payment exists.
- GAP 2 CONFIRMED: f_spread_moment_count/proof.md:34 proves exactly
  #(P cap D_j) <= binom(n,r)/binom(j,r) — DIMENSION-DEPENDENT
  (n^r), not the absolute n^{B_F}; the campaign's own
  f_dim_induction/notes/pro_brief_packing.md names the open packing
  step. Auto-discharge promoted over it.
- GAP 3 (consumer set) CONFIRMED: canonical dag has exactly two req
  consumers of conj_f: imgfib and spi_point_counting — matching
  Codex's decomposition premise.
This is the "30 auto-discharged nodes" exposure flagged at the
wave-24 repricing, now landing on its largest target. The demotions
are correct; the repair leaves (f_higher_weight_sparse_payment,
f_global_packing_step TARGETs; f_prize_consumer_flat_scope PROVED
via the SPI Hankel descriptor) are properly scoped.

## 2. LIST ROUTE RETIREMENT + FPC5 EXPOSURE — ACCEPTED

The Conjecture-F subtree moves critical -> background; imgfib no
longer invokes conj_f (its unsupported prose edge replaced by two
exact direct L1 leaves: l1_full_petal_fpc5_payment (the below-band
full-petal branch, now a CONDITIONAL router) and the existing
l1_mixed_petal_amplification (the mixed/diffuse branch — mystery
6, untouched in substance). f_imgfib_consumer_descriptor is a
route-retirement/branch-partition theorem, not a flatness theorem
— correctly labelled. The FPC5 leaf (M>=4, d<ell(M-2), t<2M-4)
decomposes into three payment targets; rate-quarter M=4,t=2 is
PROVED with absolute bound 10 — proof spot-read and SOUND
(3k+1=4ell+b, b<ell => 2ell>k-1 => per-pair codeword uniqueness;
6 pairs + 4 first-layout anchors via the banked
l1_general_first_layout_domination). Critical reds 25 -> 28: the
three FPC5 payment leaves replace broad flatness assumptions with
exact official-cell obligations — honest repricing, same direction
as wave-24.

## 3. VERIFIER REPLAYS: 91 PASS / 8 FAIL, all 8 diagnosed benign

- 4 path staleness (critical/nodes/pma_ratehalf_*): the wave moved
  15 PMA reduction nodes background -> critical; their verify.py
  chain still imports siblings at background/ paths. FIX: repoint.
- 4 pin staleness (f2_conditional_close, f_imgfib_consumer_
  descriptor, f_prize_consumer_flat_scope, u1_x4_direct_column_
  budget): assert statuses/statement text that LATER same-wave
  commits moved (e.g. l1_full_petal_fpc5_payment TARGET ->
  CONDITIONAL router at the FPC5 decomposition). FIX: refresh pins
  preserving semantic intent (the leaf is red/open).

## 4. OTHER STREAMS — ACCEPTED

- Status changes beyond the F chain: u2c_giant_tnull_dichotomy
  CONDITIONAL -> TARGET ("born red: load-bearing hypothesis hidden
  in prose") — honest direction, u2c/F2 lane. f2_admissible_object
  REFUTED -> PROVED is Codex-branch history noise; v12 now matches
  canonical (PROVED).
- X4: two born-red declarations (x4_primitive_star_u1_coverage,
  x4_exactlist_summed_budget) + norm-gate/dyadic-fold suppliers.
- WCL weight-6 (ell=1) battery + weight-7 (ell=2) prime filter:
  verifiers pass locally; the first64 MITM exclusion's remote
  search script is notes-level, not load-bearing for verify.py.
- e1 N256 s16/s18 batteries: cleanly scoped PROVED exclusions
  (census + exact-resultant certificates), all replayed.
- F2 selector handoff (f8ad8cb5e): notes/crosswalk level.
- SP quotient-sieve crosswalk + LS6 determinant chart (v12
  cf7e51cff): manifest + statement level, verifiers pass.
- SECTIONED NODE SCHEMA: Codex's held sectioning landed —
  statement.md/attack.md now compiled from statement_sections/ +
  statement_addenda/ (document.json). My round-21 addenda were
  relocated INTO the schema (L1-MPA-w, F-w1, the 830,490 exhaustive
  numbers, THEOREM BB, the L1-N10-ELL swap: all verified present).
  Clobber checks: CATCH-P3 annotations intact in LIST.md/MCA.md;
  ledger intact; NO canonical content lost.

## 5. POST-MERGE OBLIGATIONS (the integration checklist)

1. Merge f7e850788 into master (base d3a5edba8; only canonical-side
   change since base is the round-22 launch commit — no overlap).
2. Fix the 8 stale verifiers (4 path repoints, 4 pin refreshes);
   re-run all 8.
3. Recompile dag + sectioned documents WITH THE MERGED TOOLS; full
   verify chain; rebuild orbit.
4. Recompute census on my side; update verify_orbit_census.py pins
   with wave-48 provenance comment.
5. Re-read the relocated round-21 addenda for verbatim fidelity
   (spot checks passed; do one full read).
6. Ledger entry + this draft finalized; commit; push; site +
   artifact refresh (census changes).
7. Memory updates: write-path (sectioned node schema is a
   write-path change), frontier (28 reds, the FPC5 program, the
   conj_f demotion), mystery-board accounting refresh (the 14/9/2
   needs re-deriving against 28 reds).

## HOLD: the merge executes AFTER round-22 pilots report — the wave
restructures l1_mixed_petal_amplification (being read by
l1_ell_sweep) and touches f2_z1_mass_knife_edge (being read by
f2_rlocality). Canonical stays byte-stable under running pilots.
