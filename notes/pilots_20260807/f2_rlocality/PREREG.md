# PRE-REGISTRATION — MYSTERY 2 (F2): the 8.60 R-locality deficit (round 22)

Round 22, 2026-08-07. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: mystery 2's sharpest
open edge. The tail-count criterion of record binds at ZERO flat
margin (binding layer c* = 1/ln2 - 1), and the known local route
loses a factor 8.60 to R-locality. Diagnose whether that factor is
STRUCTURAL (a proved floor for R-local arguments) or an artifact of
the specific estimate — and in either case say what mystery 2
actually needs.

## 0. Sources (quote verbatim first — use the NODES OF RECORD, not
memory; constants have been force-corrected before)
- background/nodes/f2_z1_mass_knife_edge/ — statement + the three
  forced-correction addenda (CATCH-T3 constant 4.0; route-(b)
  sizing struck; the tail-count criterion of record with the
  binding layer c* = 1/ln2 - 1 at zero flat margin; the R-locality
  deficit factor 8.60). Quote the criterion and the deficit
  derivation with file:line.
- notes/pilots_20260806/tail_count/ — the round-20 pilot that
  normalized the criterion; its verifier is the baseline.
- background/nodes/f2_o1_status_split/ + addenda — the (O1) status
  of record (FALSE as posed; the finite target Z(L) <= 1 + N^3
  under calibration (C); the Z_1 window [2^17.98, 2^22.75]).
- notes/pilots_20260806/f2_repose/ — the re-pose of record.

## 1. Deliverables
- (D1) THE DEFICIT MADE EXACT: re-derive the 8.60 factor from the
  node of record. WHERE does R-locality lose it (which inequality,
  which layer)? Decompose the loss into named per-step factors
  whose product is 8.60; verify the decomposition numerically at
  the binding layer.
- (D2) THE SHARPENING ATTEMPT: attack the single lossiest step at
  toy rows (2-power grids, p = 1 mod N', NO shift-0 cells —
  CATCH-19B). Can any R-local improvement (longer windows, higher
  moments, better union structure — name each attempt) beat its
  factor? Prediction registered per attempt before computing.
- (D3) THE STRUCTURAL TEST: formulate the class of R-local
  arguments precisely (what "R-local" quantifies over — window
  length, moment order, locality radius), then either (a) exhibit
  an R-local estimate beating 8.60 at toy scale (the deficit is an
  artifact — quantify the best factor achieved), or (b) prove a
  toy-scale floor: NO estimate in the formalized class beats
  factor X > 1 (state X honestly; a floor at toy scale is evidence,
  a proved floor uniform in the row is a theorem — label which you
  get).
- (D4) THE GLOBAL INPUT: if the factor looks structural, name the
  weakest NON-local input that would close the gap (a global
  cancellation, a spectral bound, an ensemble average — with the
  exact statement it must have and what supplies it in the banked
  campaign, if anything). This becomes mystery 2's next brief.

## 2. Falsifiers / honesty
- Zero flat margin means ANY loss kills the route — but do not
  equate "this route dies" with "the criterion is false"; keep the
  criterion / route / factor distinction explicit throughout.
- If (D1) finds the 8.60 constant itself wrong (a forced
  correction), that is a first-class deliverable: derive the right
  constant, show the arithmetic, flag for the coordinator — do NOT
  edit the node.

## 3. Rules
- DRAFT ONLY in notes/pilots_20260807/f2_rlocality/. Never edit
  dag.json/nodes/tools; no git; no Modal. COMPUTE LAW: every
  python3 invocation via tools/ramguard tiny|local -- python3 ...
  (literal --), from repo root, INCLUDING file patching and JSON
  peeking. 2-power toy grids (CATCH-Z6); no shift-0 cells
  (CATCH-19B). Name every measured functional (CATCH-19C).
  Verbatim quotes with file:line. No REPORT.md — your final message
  IS the report. QUARANTINE: do not read
  notes/pilots_20260802/CAMPAIGN_LEDGER.md at or past line 2487
  (the "ROUND 22 LAUNCHED" marker); do not read the other round-22
  pilot dirs (l1_ell_sweep, ge_floor_falsifier, bb_nu_transport);
  PASS THIS QUARANTINE CLAUSE VERBATIM to any subagent you
  dispatch.
