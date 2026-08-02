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
