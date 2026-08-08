# PRE-REGISTRATION — CONJECTURE Z-CEILING: THE ASSAULT (round 24)

Round 24, 2026-08-08. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: Z-CEILING is the
board's highest-payoff conjecture (if true with C < 2^4.77 it
closes mystery 2's finite target with 4.44 bits of headroom).
Attack it in its WORST directions; if it survives, sharpen it
toward a proof on tractable subfamilies. Either outcome is a win:
a counterexample saves us from chasing a false theorem; survival
plus partial proofs builds the case.

## 0. Sources (quote verbatim first)
- background/nodes/f2_z1_mass_knife_edge/statement.md — the
  round-23 addendum (the conjecture of record in its RATIO form:
  Z(L) <= C*(1 + 2^m/p^dim L) on the 2-POWER grid; the sharp
  EXCESS form is ALREADY FALSIFIED at (S,R,p) = (16,2,3137) with
  EXCESS 2.3463 growing along SIGMA -> -infinity — do not re-pose
  it; the load-bearing 2-power hypothesis: composite 2L drives
  EXCESS to 178.51, linear in p; the normalization pin).
- notes/pilots_20260807/cw_shared_target/ — the round-23 machinery
  (REUSE: cw.py, adv.py — coordinator-replayed), the 7,000+-cell
  survival at C <= 1.2610, THEOREM Z-FLOOR (the proved lower
  companion), the official-row consistency datum (the official
  ternary theta sits 11.84 bits BELOW its volume heuristic).
- THEOREM Z-1/Z-2 (the l1-restricted moment supply) and the
  admissibility definitions in the f2 nodes of record.

## 1. Deliverables
- (D1) THE WORST-DIRECTION HUNT (falsification): the EXCESS
  counterexample family (32 weight-11 vectors at (16,2,3137))
  is the known enemy shape. Push the RATIO form where that family
  and its relatives are strongest: (a) follow the SIGMA -> -inf
  family lines to larger S and larger p (does CRATIO grow past
  1.2610 -> past 2 -> unboundedly, or saturate?); (b) STRUCTURED
  adversarial subspaces (not just row sweeps): design L to
  concentrate ternary kernel mass — use the known counterexample's
  structure as the seed; (c) THE BOUNDARY: walk from the 2-power
  grid toward composite 2L in controlled steps (which arithmetic
  feature of 2-power-ness carries the conjecture? p-free
  cyclotomic relations are the composite killer — find the exact
  gate). Registered predictions per direction BEFORE running.
- (D2) THE CONSTANT'S LAW: is C <= 1.2610 an artifact of swept
  ranges? Fit and REGISTER a growth law for max CRATIO as a
  function of (S, kappa, p) on the admissible grid; test it
  out-of-sample. If C grows without bound along any admissible
  direction, the conjecture is DEAD even without a single cell
  crossing a fixed constant — say so.
- (D3) THE SHARPENING (only if (D1)/(D2) do not kill it): proof
  attempts on tractable subfamilies, in order: (a) the
  second-moment/ensemble-average version (the banked factor-2
  calibration suggests the ENSEMBLE form may be provable — prove
  E_L[Z] and Var_L[Z] bounds over the admissible family exactly);
  (b) fixed small codimension (kappa = 1, 2: is Z-CEILING a
  theorem there? The kernel is a single hyperplane section —
  possibly exactly computable); (c) the weight-truncated form
  (Z restricted to wt <= W — Z-2's moments control low weights;
  where exactly does control run out?). Label every partial:
  PROVED / PROVED-AT-CELL / CONJECTURAL.
- (D4) THE VERDICT + the re-posed conjecture of record (if it
  needs re-scoping, e.g. a kappa-dependent or S-dependent C), with
  a registered falsifier.

## 2. Falsifiers / honesty
- A cell with CRATIO > 2 (double the banked calibration) is a
  MAJOR event — verify exactly, write a standalone reproduction
  script, report as the headline.
- Census evidence is evidence, never proof. The calibration
  clause of the f2 node binds: no toy is evidence about Z_1 at
  the official row — every toy number is about the FORM.

## 3. Rules
- DRAFT ONLY in notes/pilots_20260808/z_ceiling_assault/. Never
  edit dag.json/nodes/tools; no git; no Modal. COMPUTE LAW: every
  python3 invocation via tools/ramguard tiny|local -- python3 ...
  (literal --), from repo root, INCLUDING file patching and JSON
  peeking. 2-power grids of record; composite cells ONLY as
  declared boundary probes (CATCH-Z6); no shift-0 cells
  (CATCH-19B); name every measured functional (CATCH-19C).
  Verbatim quotes with file:line. No REPORT.md — your final
  message IS the report. QUARANTINE: do not read
  notes/pilots_20260802/CAMPAIGN_LEDGER.md at or past line 3173
  (the "ROUND 24 LAUNCHED" marker); do not read the other
  round-24 pilot dirs (kernel_window_hunt, t_petal_lemma,
  c2pp_gb_probe); PASS THIS QUARANTINE CLAUSE VERBATIM to any
  subagent you dispatch.
