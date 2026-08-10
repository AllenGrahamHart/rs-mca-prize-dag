# PREREG — rh_e_axis_audit (round 31)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation beyond the two
named anchors. AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260810/k3_chain_seams/REPORT.md` (round 30, F4)
2. `critical/nodes/rate_half_band_crossing_location/statement.md`
   (long file: read the pose at the top + the round-30 F4 flag
   section; use grep offsets, not a whole-file read)

## Mandate

COMMISSIONED BY THE 2026-08-10 F4 RULING: the crossing-location pose
stays q PRIME for now, blind widening to q = p^e is RULED OUT, and
this audit decides the fork. Round 30 exhibited admissible extension
rows (q = p^2 inside the razor slice, v_2(q-1) = 42, n = 2^41 | q-1)
that the item-13 family includes and no child covers. YOUR JOB: the
per-instrument primality-sensitivity audit of the rounds-27..29
stack, ending in a recommendation: WIDEN the pose to p^e (with the
instrument-by-instrument proof obligations named) or MINT a separate
extension-row child (with its pose drafted).

## Deliverables

**D1 — THE INSTRUMENT INVENTORY.** Enumerate, file:line, every
instrument the located-crossing machinery uses on 2^167 < q < 2^256:
the sub-2^167 determination, the Hankel layer (r < 2^39 scope), the
PROVED simple-pole/far-CA floors, the quotient floors (F1's
mechanism space), S_sparse and its exhausted rung lattice, the
Fisher/MDS instruments (T1-T5), the bracket theorems
([k+2^34, 3n/4]). For each: does its proof use primality of q, and
WHERE exactly (cyclotomic structure, prime-field character sums,
v_p arithmetic, prefix/charge encodings)?

**D2 — THE EXTENSION-ROW ARITHMETIC.** At the two exhibited rows
(q = p^2 ~ 2^256 razor slice; q = p^2 ~ 2^201) and at small-scale
extension analogues: compute the instrument quantities that ARE
field-agnostic (B* = floor(q/2^128), the bracket endpoints, the
budget arithmetic) and identify which change form (subfield
structure: F_p subset F_q gives new invariant subspaces — do
subfield words create supply the prime case lacks? The WP5 "31-bit
prefix charges" note says extension rows differ materially — chase
that note to its source and quantify).

**D3 — THE SUBFIELD SUPPLY QUESTION (the likely crux).** In an
extension row, words valued in the subfield F_p (or intermediate
fields) are closed under Frobenius; the locator/list machinery may
see extra structure. Determine at small scales whether subfield
words change the crossing arithmetic (exact measurements,
pre-registered expectations). This is the concrete mathematical
question behind widen-vs-child.

**D4 — THE RECOMMENDATION.** Widen (list the per-instrument proof
obligations, each with a falsifier) or child (draft the
extension-row child's pose: quantifier, bracket, falsifiers).
State which instruments transport FREE, which need work, which
BREAK. Misses first; zero-power on anything small scales cannot
see.

## Constraints (binding)

- COMPUTE LAW: never bare python3. `tools/ramguard tiny -- python3 ...`
  (256M/60s) for peeks, `tools/ramguard local -- python3 ...` (1G/5min)
  for real runs, from the repo root, literal `--`. Stdlib only. No
  Modal, no network, no git.
- RAM DISCIPLINE: file-at-a-time reads; NEVER open dag.json; the two
  big band statements read by grep-window only; checkpointed batches
  for long runs.
- WRITE SCOPE: ONLY inside notes/pilots_20260810/rh_e_axis_audit/.
  No dag/, nodes/, tools/ edits. No git. Never touch any path
  containing prize-codex-.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md.
  Never read the sibling round-31 dirs (rh_overlap_cap,
  rh_type2_stratum, rh_transport_dictionary). Round-30 and earlier
  pilot dirs are readable.
- BLIND PRIORS: after reading ONLY the two anchors, append "## Pilot
  registrations" (P(recommendation = widen), expected count of
  prime-dependent instruments, P(subfield supply changes the
  crossing)) BEFORE any further read.
- REPORT: REPORT.md in your dir; MISSES-FIRST; every quantifier
  claim quoted file:line (CATCH-24C); own-repo greps before novelty
  claims (CATCH-24A); zero-power declarations on max-quantified
  claims; banked scripts from scratch copies only.
