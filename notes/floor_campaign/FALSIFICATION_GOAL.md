# FALSIFICATION GOAL (floor campaign attack phase, set 2026-07-07)

**GOAL: subject every one of the seven floor conjectures to extensive,
pre-registered falsification attacks — threat-ordered — until each floor
either DIES (campaign event) or is HARDENED (has survived ≥ 3 genuinely
distinct attack families under its pre-registered standard). The user is
away; do not block on input. The purpose is early detection: a dead floor
found now saves months of work on a false region of the DAG; a hardened
floor is the true frontier.**

## The seven floors and their pre-registered falsifiers

All falsifier standards are ALREADY pre-registered in each node's dag
`falsifier` field and in notes/floor_campaign/ + REPOSE_B_WEAK.md — they
were fixed before data and are NOT to be reinterpreted mid-attack. Attack
queue (threat-ordered; re-derive if evidence shifts):

1. **F6 rate_half_band_closure (BAND-SAFETY)** — three consumers incl.
   mca_safe. Attack: exact corridor arithmetic at admissible top-slice
   rows (log2 q ∈ (255.900, 256)) across band radii σ ∈ (2^33, σ*];
   engineered adversarial radius/row selection; the existing Modal razor
   machinery (notes/verify_q_threshold_modal.py, verify_floor_depth_modal.py)
   extends directly.
2. **F2 u2c_giant_tnull_dichotomy (EXTRAS-BUDGET)** — extend
   experiments/u2c_tnull_boundary_scan.py toward the sub-balance boundary
   (Modal sweeps); engineered accident hunts INSIDE the sub-balance regime
   (norm/CRT selection — the dli round-5 pattern transported); the
   complementation lemma halves the search space.
3. **F7 worst_word_challenger_pricing (ROWWISE-ENVELOPE)** — FIRST: finish
   the canceled pre-registered census (notes/e22_census_modal.py, was
   130/135 cells); then envelope stress at bg ≤ 1 rows across q; then
   engineered challenger stacking (codim-σ coincidence selection).
4. **F4 petal_growth (PETAL-ESCAPE-BUDGET)** — extend
   experiments/amber_stress/petal_excess_local_scan.py to the top-defect
   band at scaled official-like rows; adversarial c-sweeps (the demoted
   uniformity-in-c is where the route died — attack the floor there too).
5. **F5 xr_smallcore_spread_count (16n³ per pair)** — E27 pencil-machinery
   searches for super-budget pairs at scaled rows; sunflower-free
   configuration engineering at intersection threshold k+t−1.
6. **F3 u1_x4_direct_column_budget (n³ direct column)** — boundary
   p ≡ 1 (mod n) slices beyond the probe's 60s-capped coverage (Modal
   sharding removes the cap); anchored PTE-family engineering at q ≥ n².
7. **F1 dli B-WEAK** — already survival +1; continue with experiment 2
   (engineered stacked towers — multi-level norm coincidences priced
   against the transported budget) and the n = 64 joint towers (sharded
   MITM redesign) when the queue permits.

## Attack protocol (per floor, per attack)

1. Design the attack at the floor's MOST REFUTABLE projection; write the
   attack script with the transported/scaled budget arithmetic fixed
   BEFORE running (pre-registration discipline).
2. Run on Modal (shard so every job < 60 s; local only for trivially
   small jobs — user directive, prevents crashes).
3. CLASSIFY BEFORE DECLARING (the B-WEAK experiment-1 lesson): any hot
   signal must have its population classified against the known structural
   columns and window-law populations before it counts as a refutation
   signal. A naive baseline manufactures false kills.
4. Bank: attack note + script + raw results in the node's folder (create
   critical/nodes/<id>/notes/ if absent); survival ledger +1 in the dag
   statement on absorption; commit via tools/dag_commit.sh + full ritual
   (fork sync allen/prize-dag-delta, artifact
   https://claude.ai/code/artifact/ebb725d6-96a0-4e31-bb9b-14522786c58c
   favicon 🗺️, ./tools/publish_site.sh) after every dag change; update
   the campaign memory at meaningful state changes.
5. Also PREPARE (do not send) one Pro brief per floor as attacks mature,
   in the established DLI-CLOSE format, published to the fork's
   pro_windows/ so the user can relay at will. Pro cannot be reached
   directly — the user relays.

## Death protocol (campaign event — the whole point)

If a pre-registered falsifier FIRES (verified, replayed, classified):
STOP the attack queue. Write the downstream-consequence analysis: which
ambers/conditional chains above the dead floor are invalidated, what
re-routes exist, what the consumer must now do differently. Update the
dag honestly (the floor's statement records the death; consumers'
conditional chains flagged). Report loudly in the session log and
PushNotification if available. Only then resume the queue.

## Hardening criterion and termination

- A floor is HARDENED when it has survived ≥ 3 genuinely distinct attack
  families (different mechanisms, not reruns), each executed under its
  pre-registered standard, with the survival ledger documenting each.
- The goal TERMINATES when every floor is either hardened or dead, OR
  when every remaining un-hardened floor has exhausted its known attack
  surface (then: final campaign report ranking the seven floors by
  evidence strength, naming the hardened frontier, listing the prepared
  Pro briefs, and recommending the next phase).
- Interrupts: a user-relayed Pro reply preempts everything (verify-first,
  replay exactly). DLI-CLOSE-6 remains open.

## Standing rules (non-negotiable, unchanged)

Verify-first; falsification-first; not-falsified ≠ true; honest labels;
no overclaiming; pre-registered standards are immutable mid-attack; route
and proxy failures never count against a floor. One-writer in canonical
prize/. Only allen/* branches; never touch others' branches/PRs or tex/
or Papers A-D. Commit trailer "Co-Authored-By: Claude Opus 4.8
<noreply@anthropic.com>"; push --force-with-lease only. Modal jobs < 60 s
sharded; local compute only for very small jobs; single process < 1.5 GB.
Self-paced wakeups: prefer long sleeps (1200 s+) over polling. Every
artifact replayable by a stranger.
