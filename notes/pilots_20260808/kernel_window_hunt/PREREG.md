# PRE-REGISTRATION — THE FAMILY-UNIFORM EMPTINESS FALSIFIER: THE WINDOW HUNT (round 24)

Round 24, 2026-08-08. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: mystery 5's residue
(and the shared instrument of three other lanes) is the
FAMILY-UNIFORM conjecture: every admissible N' = 128 row
(p = 1 mod 128 in the prize window) has an EMPTY non-cyclotomic
ternary folded kernel. Per-row it is executed (E1-128 certified);
"no hidden finite registry" makes the uniform form the open
content. FALSIFY IT DIRECTLY: hunt for an admissible-window prime
that divides a box-vector norm. Either outcome is decisive: a
witness forces the consumer-narrowing decision NOW (saving the
campaign from chasing a false theorem); a well-quantified silence
is the first calibrated evidence FOR the uniform form.

## 0. Sources (quote verbatim first)
- critical/nodes/integer_code_distance_cert/statement.md — the
  round-22/23 addenda (the fold reduction: kernel nonempty iff
  p | Norm(w) for a nonzero w in {-2..2}^h; "no hidden finite
  registry"; the norm-instrument family cannot reach prize rows).
- critical/nodes/lattice_cone_certificate/statement.md round-23
  block (witness sets are full <sigma,-1>-orbits of size 2h; the
  corrected counts; the GS-FLOOR/AM-GM identity: max norm
  <= (4h)^{h/2} = 2^256 at h = 64 — THE KEY ARITHMETIC: a
  box-vector norm just below 2^256 with a prime factor above
  ~2^250 has cofactor <= ~2^6).
- notes/pilots_20260807/ge_lattice_cert/ + ge_floor_falsifier/ —
  REUSE the exact tower-norm machinery (gelib.py, latlib.py —
  coordinator-replayed); the window definition (log2 p ~ 250,
  p = 1 mod 128, |F| < 2^256); the round-22 exhaustive toy
  censuses (bad primes run up to TIGHTEMPTY with no gap — the h=8
  ground truth for calibrating the h=64 hunt).
- The spec's admissibility bounds (quote with file:line — which
  (p, N') pairs are actually admissible rows for the consumers).

## 1. Deliverables
- (D1) THE HUNT, registered before running: sample/structure
  full-weight and near-full-weight vectors w in {-2..2}^64
  (register the sampling law AND structured families — e.g.
  near-AM-GM-extremal shapes, the h = 8 maximizer shapes lifted);
  compute exact Norm(w) (tower recursion, exact integers); for
  each norm N in [2^244, 2^256], test all cofactors c <= 2^12
  dividing N: is N/c a probable-prime = 1 mod 128 inside the
  admissible window? Every hit gets EXACT verification (a real
  primality proof for the candidate — Pocklington/BPSW + a
  deterministic check within reach, labelled honestly) + the
  witness pair (w, p) with the full kernel-membership check.
- (D2) THE CALIBRATION (the h = 8 control, MANDATORY FIRST): run
  the identical hunt pipeline at h = 8 against the round-22
  exhaustive ground truth — the pipeline must FIND the known bad
  primes at their known densities before any h = 64 silence is
  believed. Then quantify: the measured norm distribution at
  h = 64 (where does the mass sit vs the 2^250 window floor?),
  the per-vector hit probability implied, and the total
  effective coverage of the hunt.
- (D3) THE N' = 256 POSITIVE CONTROL: at h = 128 witnesses are
  EXPECTED (~2^48 full-box per PRO_W3, reproduced round-23). Run
  the same hunt there — finding real (w, p) witnesses at
  N' = 256 validates the method end-to-end AND banks concrete
  witness rows for the manifest re-pose (which round 23 showed
  cannot close as written at that entry).
- (D4) THE VERDICT: WITNESS FOUND (the uniform conjecture is
  FALSE — headline, reproduction script, the consumer-narrowing
  decision surfaces to the coordinator) / SILENCE with the
  quantified rarity bound (evidence FOR; state exactly what
  coverage was achieved and what remains unsampled) / plus the
  honest statement of what neither outcome settles.

## 2. Falsifiers / honesty
- A verified (w, p) witness in the admissible window OUTRANKS
  EVERYTHING — stop and report.
- Sampling silence is a coverage-bounded statement, never a proof;
  the registry clause stays open either way. Label prime tests
  (probable vs proven) scrupulously.

## 3. Rules
- DRAFT ONLY in notes/pilots_20260808/kernel_window_hunt/. Never
  edit dag.json/nodes/tools; no git; no Modal; stdlib only.
  COMPUTE LAW: every python3 invocation via tools/ramguard
  tiny|local -- python3 ... (literal --), from repo root,
  INCLUDING file patching and JSON peeking; checkpoint long hunts
  to YOUR OWN dir across the 5-minute walls. Name every measured
  functional (CATCH-19C). Verbatim quotes with file:line. No
  REPORT.md — your final message IS the report. QUARANTINE: do
  not read notes/pilots_20260802/CAMPAIGN_LEDGER.md at or past
  line 3173 (the "ROUND 24 LAUNCHED" marker); do not read the
  other round-24 pilot dirs (z_ceiling_assault, t_petal_lemma,
  c2pp_gb_probe); PASS THIS QUARANTINE CLAUSE VERBATIM to any
  subagent you dispatch.
