# PREREG — b_sparsity_pose (round 26)

Coordinator brief, written before dispatch. The pilot appends its own
registrations (predictions, thresholds, escape tests) BELOW the brief
BEFORE any computation.

## Mandate

The user ratified (2026-08-09) the mystery-5 narrowing: **(b)
o(1)-sparsity primary, (a) exhibit-scoped fallback, (c) withdrawn**
(decision record: critical/nodes/integer_code_distance_cert/statement.md,
final section). Your job: turn (b) from a slogan into a conjecture of
record that can be attacked, priced, and someday proved.

## Deliverables

**D1 — THE POSE.** State (b) in weakest usable form. Constraints:
- It must be exactly what the measured suppression law asserts and no
  more: bad-prime density o(1) in admissible windows, uniformly in
  v_2 (round-25 ground truth: BADFRAC flat across v_2 at h=8
  exhaustive; K=1 population law at h=64 after the LAW-2 cofactor
  split; W_TOP density ~2^-112). Sources to read FIRST:
  notes/pilots_20260809/large_v2_hunt/{REPORT.md,FABLE_AUDIT.md} and
  the round-25 addendum on integer_code_distance_cert.
- Name the quantifiers exactly (which windows, which h, what "o(1)"
  is measured against — vector count? prime count? orbit count?).
  Round 24's lesson (CATCH-24C): the filter bar must be named per
  consumer. State which consumer(s) of integer_code_distance_cert
  need which form, by reading their statements.
- PRE-REGISTER at least two falsifiers with power controls (the
  round-23 rule: an unpowered falsifier is not a falsifier). At
  least one must be reachable this round; run it.

**D2 — LAW 2 GENERAL-w (named gap 1).** Round 25 proved
Norm(1+2v) = 1 + 2h*v_{h/2} (mod 4h) for w = 1+2v (nodd = 1) by
Newton's identities. Attempt the general-w form (the nodd >= 3
strata). The machine-check harness exists
(notes/pilots_20260809/large_v2_hunt/d3_thm.py — reuse, do not
rewrite). A proved general form hardens the (b) instrument; a
counterexample to any natural generalization is equally bankable.
Register your candidate formula BEFORE testing it.

**D3 — BOX DEPTH (named gap 2).** Box realization of 2-adic norm
classes is measured only to depth 2^17. Push the depth as far as the
1G wall allows (register the target depth + the expected-if-uniform
class counts first). A gap between realized and available classes at
depth D would be STRUCTURE — exactly what (b)'s uniformity needs to
know about.

**D4 — VERDICT.** Is the pose self-consistent with every banked
measurement (h=8 exhaustive, h=64 ladder, the four Proth rows, the
E1-128 certificate)? Any tension is a finding, not a failure.

## Escape tests (run before the main work)

- Reproduce the h=8 pooled BADFRAC 0.1115 and the W_TOP 2^-112
  density from the banked data/scripts (calibration, not discovery).
- Verify the LAW-2 identity suite still passes (0 violations) before
  building on it.

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md at
  or below line 3872; do not read any other notes/pilots_20260809/
  round-26 pilot dir (b_sparsity_pose is yours; umin_spike_hunt,
  freeze_tail_law, m7_falsifier_hunt are not). Pass this clause to
  any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root
  /home/u2470931/smooth-read-solomin/prize — including file patching
  and JSON peeking. RAMGUARD_TIMEOUT may extend a wall; document it.
  Harness Write/Edit tools are fine for authoring.
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json (use
  node.json shards + grep); no bulk directory loads; checkpoint any
  run that could exceed its wall; background batches with results
  files for >10-min runs.
- DRAFT-ONLY: no edits outside notes/pilots_20260809/b_sparsity_pose/;
  no dag.json/nodes/tools writes; no git; no Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing; report
  misses first. Name every measured functional (CATCH-19C). No
  shift-0 cells (CATCH-19B). Own-repo grep before claiming any lemma
  is missing (CATCH-24A).
- Your final message IS the report (the coordinator persists it
  verbatim). End with a compliance paragraph.

## Pilot registrations (appended by the pilot before any computation)
