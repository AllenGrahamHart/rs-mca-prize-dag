# PRE-REGISTRATION — C2''-r3: A REACHABLE FALSIFIER + THE GB-5 ESCALATION (round 25)

2026-08-09. Coordinator brief; pilot appends registrations BEFORE
any computation. MANDATE: round 24 killed both registered C2''
falsifiers as tests (G-b vacuous by theorem; G-a at 2^203 states).
The pose needs a REACHABLE falsifier, and GB-5 (the first
non-stacked datapoint: R3_W = 11.34 bits over 4 junctions vs the
2.545-bit window-scaled reserve, 4.5x) needs escalation.

## Sources
- critical/nodes/dli_c2pp_joint_reserve (the round-23/24 addenda:
  C2''-r3's exact form; the vacuity theorem; the freeze law — the
  official row lives ENTIRELY pre-saturation, log2 q in [41, 256]
  vs n/t = 256; the census squaring law).
- notes/pilots_20260808/c2pp_gb_probe/ (REUSE: gb_probe.py the
  checkpointed instrument, verify_law.py, the J = 4 exact-depth
  scan; the middle-peaked shape; the closed-form saturation law).

## Deliverables
- (D1) THE REDESIGNED FALSIFIER, drafted with its power analysis:
  it must be (i) evidence-bearing under the binding symmetric
  not-evidence clause (genuine sequential conditioning, no
  stacking), (ii) REACHABLE (depth <= 4 exact, or an analytic
  form), (iii) POWERED (able to separate a true C2''-r3 world from
  a false one at reachable scale — run the power control on a
  synthetic pair BEFORE proposing). Candidate shapes to price:
  a pre-saturation GROWTH criterion at fixed depth (the freeze law
  confines the official q-range to pre-saturation — a depth-4 sum
  growing superlinearly in log q across >= 4 pre-saturation
  octaves at >= 2 tower shapes); an analytic bound on the
  junction sum via the U-induced skew law; a shape criterion
  (the middle-peak location drifting with q).
- (D2) THE GB-5 ESCALATION, executed: deeper/wider pre-saturation
  windows via the q-free structure — the round-24 instrument at
  J = 4 across MORE tower shapes (n, t) and MORE pre-saturation
  q-octaves; the target functional is R3_W vs the window-scaled
  reserve (registered: at what (n, t, q) grid does the 4.5x grow,
  saturate, or shrink?). NO J -> 33 transport; growth-shape
  evidence only.
- (D3) THE ANALYTIC ATTEMPT: the closed-form saturation law gave
  Z_j^inf exactly; attempt the PRE-saturation analogue (the
  binomial-skew census as a function of log2 q below n/t) — even
  a two-term expansion would make the official-row junction sum
  estimable for the first time.
- (D4) VERDICT: the falsifier of record (drafted + power-tested)
  for coordinator adoption; the escalated GB-5 dataset + its
  shape; the analytic form or its named obstruction.

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
