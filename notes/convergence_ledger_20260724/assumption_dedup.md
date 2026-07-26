# C3-3 — conditional assumption dedup: CLOSED with a negative (2026-07-26)

The ledger asked for `assumption_dedup.md`: *"every distinct assumption behind our
mathematical CONDITIONALs mapped against his six GF inputs, shared hypotheses
counted once, each with owner + route + falsifier."*

**Result: there is no such set to build on our side.** The 38 mathematical
CONDITIONALs carry **zero independent mathematical work**. Every one of them
discharges by pure gate propagation once the 24 TARGETs close. The dedup ledger
that C3-3 specified would have exactly 24 rows, and they are the TARGETs we
already track.

Artifact: `tools/verify_conditional_propagation.py` (fail-closed, 4 mutation
controls). Refreshed after the E1 and unsafe-at-crossing false-green
corrections: math orbit `242 = 180/38/24`.

## The three checks

1. **Propagation.** Grant every math-orbit TARGET; iterate "a CONDITIONAL
   discharges when all its req-parents are discharged" to a fixpoint.
   **38 / 38 discharge, fixpoint in 8 rounds.** Nothing is stuck.
2. **No off-orbit blocker.** No math-orbit CONDITIONAL has an open req-parent
   outside the math orbit. **0 external blockers** — nothing is hiding off-orbit.
3. **No unwired hypothesis.** The failure mode that would invalidate (1) is a
   hypothesis stated in a node's prose but never wired as a req edge. Every open
   node named in any CONDITIONAL's `statement` / `notes` / `conditional.md` was
   classified as ancestor (wired hypothesis), ev-parent (wired evidence), or
   descendant (benign consumer back-reference). **12 mentions fell outside those
   classes; all 12 were read and are benign**, and are pinned by name in the
   verifier so a *new* one forces a re-audit.

## The 12 audited mentions

| conditional | mentions | verdict |
|---|---|---|
| `xr_clean_residual_any_gate` | `rigidity_kernel` | node says verbatim: *"No use of the broader `rigidity_kernel` alternative is needed for this conditional route."* |
| `xr_smallcore_spread_count` | `rigidity_kernel`, `rk_rigidity_kernel` | node says: *"ev context on the predicates only (K2 instances by shape, not by consumed reduction)"* |
| `xr_smallcore_spread_count` | `shared_census_kernel` | names a *sibling* satellite's conditional (`f5_npb_conditional_close`), not its own hypothesis |
| `list_adjacency_closing` | `ww_row_envelope_clause` | node says verbatim: *"This argument does not consume `ww_row_envelope_clause`."* |
| `x4_exactlist_staircase_split`, `u1_x4_direct_column_budget` | `u1_pullback_dichotomy` | **stale prose, already banked as a DOC CORRECTION** in the node itself: *"the DAG edge and this n^3 form are authoritative."* Verified: `u1_pullback_dichotomy` has exactly one out-edge and it is `ev` (into `xr_smallcore_spread_count`) — it is a req-parent of nothing. |
| `knife_edge_census` | `census_dodge_selection` | parenthetical pointer (*"exhibited-row partials dodge entirely"*), not a hypothesis |
| `f2_conditional_close` | `f3_h3_officialrow_conditional_close`, `f5_npb_conditional_close` | parallel program satellites, listed as siblings |
| `aperiodic_zero_at_crossing`, `list_grand` | `rate_half_band_closure` | cross-references to an in-orbit TARGET already tracked on its own |

## Consequences

1. **The remaining mathematics is exactly the 24 TARGETs.** The census line
   `242 = 180/38/24` should be read as **24 units of work**, with the 38 as
   bookkeeping that resolves itself.
2. **The ledger's Definition of DONE has no independent conditional conjunct.**
   On our side discharge of the 38 mathematical conditionals is **implied by
   closing the 24 targets**. What survives of C3-3 is only the joint half —
   mapping our 24 against his six GF inputs.
3. **Effort allocation:** 100% of remaining mathematical effort belongs on the 24
   TARGETs. Any session spent "discharging conditionals" is spent on nothing.
4. **The original C3-3 result was a re-pricing, not progress.** The later E1
   and unsafe-at-crossing corrections changed statuses, but the propagation
   conclusion survived their fail-closed replay unchanged.

## Non-claims

- Says nothing about *his* inputs (S), (A), (E), list-completion, or whether our
  hypotheses dedup against his — that is the joint half of C3-3 and stays open.
- Does not assert the 24 TARGETs are independent of each other; they share
  machinery, and closing one may cascade. It asserts only that the CONDITIONALs
  add nothing beyond them.
- Propagation is a statement about the **wired** structure plus the prose audit in
  §3. It is only as good as the wiring, which is why the audit is pinned and
  fail-closed rather than done once and forgotten.
