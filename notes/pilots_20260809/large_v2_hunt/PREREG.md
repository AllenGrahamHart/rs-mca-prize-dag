# PRE-REGISTRATION — THE LARGE-v2 WINDOW HUNT (round 25, narrowing decision support)

2026-08-09. Coordinator brief; pilot appends registrations BEFORE
any computation. MANDATE: the family-uniform emptiness is FALSE
(round 24); the pending narrowing choice is (a) exhibit-scoped /
(b) o(1)-sparsity / (c) large-v_2 restriction. Option (c) rests on
the measured dichotomy: generic witnesses have v_2(p-1) = 7 while
every deployed row has v_2 in [92, 200]. DECISION SUPPORT: hunt for
witnesses RESTRICTED to large-v_2 admissible rows. A witness kills
(c); calibrated silence + a mechanism supports it.

## Sources
- notes/pilots_20260808/kernel_window_hunt/ (REUSE the hunt
  machinery: klib.py, the calibration pattern, the witness
  protocol; the REPORT's v_2 findings + windows W_TOP/W_DEP/W_ADM).
- critical/nodes/integer_code_distance_cert round-24 board event
  (the witness of record; the narrowing options).
- The round-22 exhaustive h = 8 ground truth (ge_floor_falsifier
  sweep artifacts) for the v_2 profile calibration.

## Deliverables
- (D1) THE v_2 GROUND TRUTH at toys: the exact v_2(p-1)
  distribution of ALL bad primes at h = 8 (exhaustive — the
  round-22 sweep data has every bad prime; compute the profile).
  Is large v_2 rare among bad primes for a STRUCTURAL reason
  (heuristic: p = 1 mod 2^v is a 2^-(v-7)-density condition among
  p = 1 mod 128 — quantify the expected suppression) or does the
  norm structure actively favor/disfavor it?
- (D2) THE TARGETED HUNT at h = 64: witnesses with v_2(p-1) >= 41
  in the admissible window — i.e. Norm(w) = c * p with c <= 2^12,
  p = 1 mod 2^41. Register the sampling + structured families
  (adapt the round-24 law); the congruence makes hits ~2^-34
  rarer, so ALSO run the graded ladder v_2 >= 8, 12, 16, 24, 32
  to measure the suppression curve (does the empirical curve match
  the density heuristic? A deviation in EITHER direction is a
  finding).
- (D3) THE MECHANISM QUESTION: is there a STRUCTURAL obstruction
  to large-v_2 bad primes (e.g., the norm's 2-adic valuation
  structure — the round-24 NORMLAW observation Norm = 1 mod 128
  and its v_2(Norm - 1) refinement; does it EXTEND to a theorem
  "v_2(p-1) <= f(v_2-structure of w)"?) — a proved obstruction
  would make (c) a THEOREM-BACKED narrowing, the strongest
  possible outcome. Attempt the local-reciprocity proof route
  named in the round-24 report (the conductor-128 analogue).
- (D4) VERDICT for the narrowing decision: (c)-viable (silence +
  mechanism) / (c)-dead (witness found — protocol: verify exactly,
  reproduction script, headline) / undecided with the exact
  coverage achieved.

## Rules
QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md at
or past line 3731 (the "ROUND 25 LAUNCHED" marker); do not read the
other round-25 pilot dirs; PASS THIS CLAUSE VERBATIM to any subagent.
RAM DISCIPLINE (binding): file-at-a-time reads; never load dag.json
whole (grep it or read node.json shards); no bulk directory reads.
COMPUTE LAW: every python3 via tools/ramguard tiny|local -- python3
(literal --) from repo root, INCLUDING file patching and JSON
peeking; checkpoint long runs to YOUR OWN dir across the walls.
DRAFT ONLY in your own dir; never edit dag.json/nodes/tools; no git
writes; no Modal; stdlib only. Name every measured functional
(CATCH-19C); 2-power grids where yours to choose (CATCH-Z6); no
shift-0 cells (CATCH-19B). Verbatim quotes with file:line. No
REPORT.md — your final message IS the report.
