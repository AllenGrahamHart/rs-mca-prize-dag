# PRE-REGISTRATION — Z-CEILING AT N = 32, sigma ~ 0: THE ALGORITHM (round 25)

2026-08-09. Coordinator brief; pilot appends registrations BEFORE
any computation. MANDATE: round 24 named N = 32 at sigma in [-2, 2]
"the single highest-value next computation" for Z-CEILING — the
record (C >= 1.7681) lives at sigma ~ 0 and small N, and the
"C decays in N" claim rests on an N-ladder with no sigma-matched
N = 32 point. The MITM state count 3^16 = 43M exceeded the 1G
wall. Design an algorithm that reaches it; run it as far as
reachable.

## Sources
- notes/pilots_20260808/z_ceiling_assault/ (REUSE: zcore.py, the
  families M2/M4, the functionals; THEOREM RC — rc.py — the
  finite-max + p > N^{N/2} kill; the record cell's 3-way
  verification pattern).
- background/nodes/f2_z1_mass_knife_edge round-24 update (the
  conjecture of record + the admissible pinning).

## Deliverables
- (D1) THE ALGORITHM, registered with its cost model BEFORE
  implementation. Candidate routes to price (pick or beat):
  (i) RC-aided weight truncation — TMASS needs only weights
  U <= U*(p) by RC's UMIN >= p^{2/N} kill + a proved tail bound
  from the weight enumerator's Z-1/Z-2 moments; enumerate only
  the low-weight shells (sum_{U <= W} C(32,U) 2^U terms — priced
  per W); (ii) orbit quotients (the mu_2N symmetry: TMASS is
  root-choice-invariant — quotient the cube by the shift/negation
  group before hashing); (iii) a two-level MITM with disk-backed
  checkpointed buckets under the 1G ceiling (the wall is RAM, not
  time — 12-hour modal profile local wall is available with
  RAMGUARD_TIMEOUT); (iv) the character-sum route (SMOOTH =
  sum_u prod cos^2 — p^kappa terms, feasible when p^kappa < ~2^32
  — EXACT rational or error-bounded float with the bound proved).
- (D2) THE RUN: max CRATIO over the N = 32 admissible sigma in
  [-2, 2] band (p ~ 2^30-2^34 at kappa = 1... register the exact
  admissible (kappa, p) cells; the M4/RSET family kappa = 1 needs
  p = 1 mod 64 near 2^32 — enumerate the reachable cells). Every
  computed cell 2-way verified (two independent algorithms, the
  round-24 pattern).
- (D3) THE N-LADDER VERDICT: with the N = 32 sigma-matched point,
  does max CRATIO decay from N = 16's 1.7681 (supporting an
  absolute C) or grow (re-opening the conjecture's death
  direction)? State the honest scope of whatever grid was reached.

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
