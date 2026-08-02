# Flag adjudication 2026-08-02: generic-branch dichotomy non-exhaustive as written

**Status of this note: adjudicated defect, repair pending (joint edit).**

The 2026-08-01 pilot flag (see
`notes/pilots_20260802/pb_split_fibre_selector/FABLE_AUDIT.md`) was
adjudicated by a dedicated read-only pilot
(`notes/pilots_20260802/xr_bridge_semantics/REPORT.md`, coordinator
verification in `FABLE_AUDIT.md` alongside). Verdict, independently
spot-checked by the coordinator:

- **Genuine gap, inherited.** `proof.md:6-9` imports "all distinct
  selected support intersections at most K" from the strip rung, but the
  strip proves only the FORCING (core >= k+1 forces a codeword pair on
  >k points); the claimed removal of the band `[k+1, A-2]` is asserted,
  not proved (`xr_strip_classification_rungs/proof.md:20-21`). The only
  proved core-payment fires at `core >= A-1` (`xr_pencil_cascade`). A
  band pair triggers neither the tangent strip (single-slope agreement
  > A) nor this node's nongeneric branch (no A-support explanation need
  exist). Under `Gamma_hi = {core = K}` a band slope sits in neither
  class.
- **Repair forced: R2** — `Gamma_hi := {z : exists z' != z with
  |S_z intersect S_z'| >= K}` — jointly with widening P-A1's predicate
  in `xr_highcore_collision_count` from "size-`k` core" to "core of
  size >= k". This is already the semantics of the SHA-pinned verifier
  (`audit_p8p9_local_20260710.py:225`, `if J >= k`), of
  `F5_SKELETON.md:398`, and of P-B's banked `Gamma_lo` predicate
  (`<= K-1`), which is unchanged verbatim. R1 (strengthening the
  generic-branch hypothesis) is UNSAFE: it routes the band into P-A2,
  whose removal step requires `|T| <= n-A`
  (`xr_true_tangent_coordinate_injection`), and that widening is
  REFUTED (`background/nodes/xr_nondeep_tangent_supportwise_payment`).
- **PROVED status: repairable at statement level.** Under R2 the
  partition is disjoint-and-exhaustive by construction with no core-cap
  premise. As currently written the node is not sound.
- **Gate before the edit:** whether P-A1's banked partial payments
  survive `{core in [k, A-2]}` — cost pass running at
  `notes/pilots_20260802/p_a1_widening_cost/`. The edit lands as ONE
  coordinated change: this node + P-A1 + the strip node's item-3
  rewording (+ `xr_quotient_global_core_collision_router`'s routing
  sentence, which R2 repairs as a side effect).

**GATE RESULT (same day, cost pass banked):** the R2 edit on THIS node
is safe unconditionally (routing-only). The P-A1 widening is NOT a
re-pricing: the k-set-keyed moment layer and all core-agnostic charges
survive verbatim, but the frozen-kappa constants degrade (prize paid
ranks 15,15,14 -> 11,11,10; CLB3/4 dead) and the uniform-cell/Maxwell
shell-exclusion fan (~10 PROVED background nodes) breaks — its
contradictions need h < 4 (dead on five of six rows). Two repair
routes, SURFACED as a planner/maintainer decision: (W) widen + demote +
open `xr_band_core_slope_count` (<= 4n^3 from the 13n^3 headroom);
(T) resurrect the graded tangent band charge (archived
`xr_partial_tangent_band` mission), keeping P-A1 exact-k with zero
demotions. Both routes need the pencil-cascade payment audit first
(whether the A-2 ceiling's TANGENT-PENCIL charge actually fits inside
B_tan <= n-A+1). See
`notes/pilots_20260802/p_a1_widening_cost/{REPORT,FABLE_AUDIT}.md`.

**PAYMENT AUDIT RESULT (same day):** the cascade's "paid" is UNSOURCED
(see `xr_pencil_cascade/notes/PAYMENT_UNSOURCED_FLAG_20260802.md`).
The honest generic-branch ceiling is A-1, sourced independently
(core = A between exact-A selected supports => same support => joint
A-support explanation => nongeneric). Fork consequences: Route W
survives with the widened predicate moving to core in [k, A-1] (line
caps exactly x2; PSP unchanged; sourcing improves). Route T is
materially harder: it must charge up to A-1, its target column is
provably saturated by one cascade (|T| ratio 1.0000 on all six rows)
with multi-pencil overflow realized on the F_17 witness, so it forces
B_tan > n-A+1 — re-surgery trigger 4. Fork now TILTS TO ROUTE W;
final call awaits the graded-band-ledger pilot's report + maintainer
visibility. R2 on this node remains safe and unaffected (routing-only,
no ceiling needed). See
`notes/pilots_20260802/xr_cascade_payment_audit/{REPORT,FABLE_AUDIT}.md`.

**BAND-LEDGER RESULT (same day, final fork state): RECOMMENDATION =
ROUTE T**, redesigned as a THIRD generic column from the 13n^3
headroom — NOT a B_tan enlargement, so the payment audit's trigger-4
objection does not apply. T then strictly dominates W: same single
open input (the band occupancy lemma, N_d <= ~0.68n^2), zero
demotions, prize ranks unchanged; four new theorems proved (line cap
under J >= k; ray rigidity; the band interaction strip d_1+d_2 >= h
=> tangent event; two-column determinacy). Decision remains surfaced
(user/maintainer + Pro). See
`notes/pilots_20260802/xr_graded_band_ledger/{REPORT,FABLE_AUDIT}.md`
and CAMPAIGN_LEDGER.md section A.1.
