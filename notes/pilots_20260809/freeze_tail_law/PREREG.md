# PREREG — freeze_tail_law (round 26)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

Round 25 (c2pp_falsifier_redesign) made C2''-r3 measurable via the
telescoping lemma and left ONE named residual obstruction: **the
freeze-tail cutoff law** — the second census term is not a pure
q^{-T} power law; it steepens near freeze and terminates in an exact
integer cutoff (measured freeze scales 14.5, 15.5, 18, 21, 22, 34, 67
versus the naive n/T). Your job: fit it, then prove it. Sources to
read FIRST: notes/pilots_20260809/c2pp_falsifier_redesign/
{REPORT.md,FABLE_AUDIT.md,PREREG.md,ckpt.json (the phase-C level
census rows — file-at-a-time, it is 35KB)}; the round-25 addendum on
critical/nodes/dli_c2pp_joint_reserve/statement.md.

## Deliverables

**D1 — THE FIT.** From the banked 275 exact level-census rows (plus
new rows where the grid is thin — reuse c2lib.py/escalate.py phase
machinery, do not rewrite), characterize the excess
Zlev(q) - Zinf near freeze: the steepening exponent, the cutoff
location as a function of (n, t, lev, e), and the integer at which it
terminates. Register a candidate functional form BEFORE fitting;
report the fit residuals against it honestly.

**D2 — THE PROOF ATTEMPT.** The excess counts non-frozen strata; the
cutoff is where the LAST non-frozen stratum dies. Attempt an exact
characterization: which stratum is last, and why does its census hit
zero at an integer scale? (Round 25's e-periodic classification of
the FROZEN stratum is the template — the closed form came from
cyclotomic factorization; the near-freeze strata should factor the
same way.) A proved cutoff law would (i) close the named obstruction,
(ii) make PR-D's alpha = T an actual theorem on its domain, and
(iii) potentially extend G-c's licensed range from log2 q <= 232
toward 256 — state exactly how far, if it lands.

**D3 — S_inf = 1/ln 2 (mint candidate).** Round 25 found
S_inf = sum_{k>=1} 2^{-k}(2^k - log2 C(2^k, 2^{k-1})) = 1/ln 2 to
full double precision. Prove it (it smells like Stirling telescoping:
log2 C(2m, m) = 2m - (1/2)log2(pi m) + O(1/m), summed against 2^{-k}).
A three-line proof mints R3inf_full(n, n/2) -> 0.4427 n as a theorem.
If the proof needs more than elementary analysis, say so and bank the
partial.

**D4 — THE (232, 256] QUESTION.** Round 25's per-level freeze law
says only levels 0/1 matter in the undecidable band. Price exactly
what a targeted exact census there would cost with the telescoping
lemma + your cutoff law (state the census size as a function of
log2 q) — is the band reachable after all? A pricing, not a run.

## Escape tests (run before the main work)

- Replay escalate.py phase A (PR-A) from a fresh scratch checkpoint —
  the lemma your work builds on (coordinator got PASS; you must too).
- Reproduce the reserve-break scale 255.999999987544 and the ledger
  rebuild (analytic.py runs read-only in place).

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md at
  or below line 3872; do not read any other round-26 pilot dir
  (b_sparsity_pose, umin_spike_hunt, m7_falsifier_hunt). Pass this
  clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root —
  including file patching and JSON peeking. RAMGUARD_TIMEOUT may
  extend a wall; document it.
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no bulk
  loads; checkpoint long runs; background batches with results files
  for >10-min runs.
- DRAFT-ONLY: writes only in notes/pilots_20260809/freeze_tail_law/;
  read c2pp_falsifier_redesign/ freely but write NOTHING there; no
  dag/nodes/tools writes; no git; no Modal; stdlib only.
- Register predictions (incl. your candidate cutoff form) with
  numeric windows BEFORE computing; misses first. The symmetric
  not-evidence clause binds: toy silence is never official-row
  evidence in either direction; every official-scale number is
  labelled [law] with its licensed range.
- Your final message IS the report. End with a compliance paragraph.

## Pilot registrations (appended by the pilot before any computation)
