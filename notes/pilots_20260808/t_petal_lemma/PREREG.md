# PRE-REGISTRATION — THE T-PETAL OVERLAP-CAP LEMMA: PROVE OR REFUTE (round 24)

Round 24, 2026-08-08. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: the board's highest
single-lemma leverage, doubly confirmed. THE LEMMA: for two
distinct primitive members (F, W), (F', W') of the t-petal slice,
|Z(F) cap Z(F')| <= e - 1 (e = 2d+1-t*ell the flat dimension
parameter). PROVED verbatim at t = 2 (the cofactor determinant,
2s = e-1) and t = 3 ((PJ2) via the mu-basis). If it lands at
t >= 4: the entire precomputed Johnson sieve becomes legal (408
residual rows -> the t < M, J > 0 cells removed at a stroke),
mystery 7's undecided red is decided, and red 3 gets its first
real instrument. If it is FALSE at some t >= 4: equally decisive —
the sieve is illegal and red 3's re-pose must route around it.

## 0. Sources (quote verbatim first)
- The two proved cases: the t = 2 cofactor determinant
  (l1_fpc5_ratehalf_m4_t2_joint_support_distance (JD1) and the
  two_full_petal slice reduction) and t = 3
  (pma_three_petal_projective_johnson_bound (PJ2) +
  pma_three_petal_mu_basis_reduction) — quote the proofs' actual
  mechanisms with file:line; identify EXACTLY what each uses that
  might not generalize (the mu-basis is a THREE-petal object; the
  cofactor determinant is a TWO-petal object).
- critical/nodes/l1_fpc5_large_source_payment/statement.md +
  round-23/23b addenda (the 408-row residual; the missing t >= 4
  injection; H3: t <= M always).
- notes/pilots_20260807/fpc5_diag/ (fpc5_exact.py — the sieve
  that consumes the lemma, coordinator-replayed) and
  notes/pilots_20260807/mf_wall_adversary/ (the 142/266 split).

## 1. Deliverables
- (D1) THE PROOF ATTEMPT, structured: (a) write the t-petal slice
  system explicitly (t congruences L_i | (W - c_i F) on (F, W),
  deg <= d); (b) attempt the syzygy/cofactor-determinant argument
  at general t — derive where the t = 2 mechanism (the resultant
  of the two cofactor relations) does or does not extend when
  there are C(t,2) pairwise relations; (c) attempt the mu-basis
  route — does a t-petal analogue of the 3-petal mu-basis exist
  (the module of syzygies of t forms — its expected rank/degrees
  by Hilbert arithmetic), and does (PJ2)'s argument only need the
  degree bound? Every step PROVED or labelled with the exact gap.
- (D2) THE REFUTATION ATTEMPT (mandatory, in parallel): exhaustive
  toy search for violating pairs at the smallest t = 4 cells
  (build the 4-petal slice explicitly at toy (ell, q) — the
  round-23 bucketing machinery adapts; REUSE rh_bucket.py /
  ls6_bucket.py); search pairs for |Z(F) cap Z(F')| >= e.
  Register the cells and the escape test in advance. A violating
  pair is a full falsification of the lemma — verify exactly,
  reproduction script, headline.
- (D3) THE PAYOFF EXECUTED (only if (D1) lands a proof): re-run
  the sieve (fpc5_exact.py) with the lemma flagged legal at the
  proved t range; print the NEW residual row count vs 408; state
  exactly which cells die. If the proof covers only some t range
  (e.g. t <= T0), print the residual under partial legality.
- (D4) THE VERDICT: PROVED (with the write-up at proof standard —
  the coordinator replays and mints) / REFUTED (witness + what
  red 3's re-pose must become) / PARTIAL (the exact t range +
  the named gap + the next decisive step).

## 2. Falsifiers / honesty
- The refutation search runs REGARDLESS of proof progress — a
  proof believed before the search completes is not banked.
- Toy search maxima are lower bounds; exhaustiveness claims only
  where the enumeration is complete (declare completeness class
  per cell).

## 3. Rules
- DRAFT ONLY in notes/pilots_20260808/t_petal_lemma/. Never edit
  dag.json/nodes/tools; no git; no Modal; stdlib only. COMPUTE
  LAW: every python3 invocation via tools/ramguard tiny|local --
  python3 ... (literal --), from repo root, INCLUDING file
  patching and JSON peeking. 2-power grids where yours to choose;
  official-arithmetic-shaped cells where the object demands
  (declare which); name every measured functional (CATCH-19C).
  Verbatim quotes with file:line. No REPORT.md — your final
  message IS the report. QUARANTINE: do not read
  notes/pilots_20260802/CAMPAIGN_LEDGER.md at or past line 3173
  (the "ROUND 24 LAUNCHED" marker); do not read the other
  round-24 pilot dirs (z_ceiling_assault, kernel_window_hunt,
  c2pp_gb_probe); PASS THIS QUARANTINE CLAUSE VERBATIM to any
  subagent you dispatch.
