# PREREG — umin_spike_hunt (round 26)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

Round 25 (z_n32_band) broke the N=32 wall and found the mechanism that
sets the band max: rare cells carrying low-weight mu_64-orbits (record
cells have UMIN = 9 against the typical 11; weights <= 12 supplied 48%
of the record's excess). Its 47-cell sample cannot see the tail of
~2.1e7 admissible kappa=1 primes, and the heuristic extrapolation puts
the band max at ~1.88 — ABOVE the N=16 record 1.7681. **Your job is
the named follow-on: hunt the spikes DIRECTLY. This is a
kill-or-confirm experiment on CONJECTURE Z-CEILING's decay direction.**
Sources to read FIRST: notes/pilots_20260809/z_n32_band/
{REPORT.md,FABLE_AUDIT.md,PREREG.md}; the round-25 addendum on
background/nodes/f2_z1_mass_knife_edge/statement.md.

## Deliverables

**D1 — THE TRIAGE INSTRUMENT.** wenum.py (in the z_n32_band dir —
REUSE, do not rewrite) computes exact AU[U] for U <= 12 at ~3x the
cost of a full BBM cell. Design and register a CHEAPER pre-filter if
one exists (e.g. AU[9] alone via truncated enumeration, or a
necessary condition on p for a weight-9 orbit to exist — think: when
does a norm equation Norm(w) = 0 mod p with |w|_1 = 9 have solutions?
An arithmetic characterization would replace enumeration entirely).
Price the instrument per prime BEFORE running. Register the triage
threshold (what AU profile promotes a cell to exact computation).

**D2 — THE HUNT.** Sweep as many admissible kappa=1 primes in
[2^30, 2^34] as the budget allows (register the target count from
your D1 pricing — the round-25 sample was 47; aim for orders of
magnitude more THROUGH THE FILTER, not exhaustively). Compute exact
CRATIO via BBM (reuse bbm.py + the 1402 checkpoint files — cells
already computed must not be recomputed) at every promoted cell.
Also register: the kappa=2 band deserves at least the 266-cell
exhaustive sweep round 25 declared post-hoc and never ran, if the
budget covers it (RC protection is weakest there and the official
row has kappa >> 1).

**D3 — THE VERDICT.** Three registered outcomes, decided in advance:
- Any cell with CRATIO > 2: Z-CEILING's C-form is DEAD (the ratio
  form's own bar). State it plainly.
- Any cell with CRATIO > 1.7681: the N-decay direction is REFUTED
  (the N=32 band max exceeds the exhaustive N=16 record); the
  round-24 repricing C >= 1.7681 moves up accordingly.
- Neither found through a filter that provably (or with measured
  recall) catches UMIN <= 10 cells: the strongest pro-decay evidence
  yet — quantify the filter's recall so the silence has a number.

**D4 — TWO-WAY VERIFICATION.** Every cell that enters the verdict
gets an independent re-derivation (BBM-ALT permutation/RBUCK variant,
as ver.py does). The round-25 standard: all verdict-bearing cells
two-way, disagreements = 0.

## Escape tests (run before the main work)

- Reproduce the record cell (p=4683696257: TNUM 11700545024, NKER
  392641, CRATIO 1.4210954721) and its AU profile (AU[9]=128,
  AU[10]=320, AU[11]=192, AU[12]=704) from the banked machinery.
- Verify your triage instrument FIRES on the two known UMIN=9 cells
  (p=4683696257, and the kappa=2 record p=63361) and stays silent on
  two known UMIN=11 cells — a power control on the filter itself.

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md at
  or below line 3872; do not read any other round-26 pilot dir
  (b_sparsity_pose, freeze_tail_law, m7_falsifier_hunt). Pass this
  clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root —
  including file patching and JSON peeking. RAMGUARD_TIMEOUT may
  extend a wall; document it.
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no bulk
  loads; checkpoint everything (extend ckpt/, do not duplicate);
  background batches with results files for >10-min runs. This box is
  shared — measure your throughput early and register the honest
  reachable count.
- DRAFT-ONLY: writes only in notes/pilots_20260809/umin_spike_hunt/
  (EXCEPTION: you may append new checkpoint files to
  notes/pilots_20260809/z_n32_band/ckpt/ since the format is shared —
  never modify existing ones); no dag/nodes/tools writes; no git; no
  Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing; misses
  first. Name every measured functional. The f2 calibration clause
  binds: all numbers are about the FORM of Z-CEILING, never about Z_1
  at the official row.
- Your final message IS the report. End with a compliance paragraph.

## Pilot registrations (appended by the pilot before any computation)

Pilot: Opus, codename umin_spike_hunt, round 26, 2026-08-09.
Everything below was written BEFORE any interpreter was run.  Sources
read first: z_n32_band/{REPORT.md,FABLE_AUDIT.md}, bbm.py, wenum.py,
ver.py, zcore.py, the six banked `log_wenum_*.txt` AU profiles, the
banked CELLS*.tsv leaderboards, and the round-24/25 addenda on
background/nodes/f2_z1_mass_knife_edge/statement.md (THEOREM RC).

### U0 — THE INSTRUMENT (D1).  RESSIEVE: an EXACT arithmetic
### characterization, not a filter.  Recall 1.0 by proof.

THEOREM RC (banked, round 24) already says: for a ternary kernel
vector f of weight U, `p | Res(Phi_2N, f)` and `1 <= Res <= U^{N/2}`.
I register its CONVERSE, which turns the necessary condition into an
IFF and therefore replaces enumeration by arithmetic:

**THEOREM RS (registered, to be proved + machine-checked this round).**
Fix N = 32 (so Phi_64 = x^32+1), p prime with 64 | p-1, and theta of
order 64 in F_p^* (the M4/I2-RSET row is [theta^j]_{j<32}).  Then:
p admits a ternary kernel vector of weight U  <==>  there is a ternary
f of degree < 32 and weight U with p | Res(x^32+1, f).
  (=>) is THEOREM RC.
  (<=) Res = prod_{k odd} f(theta^k) mod p, so p prime forces
       f(theta^k) = 0 for some odd k.  Put g(x) = f(x^k) mod (x^32+1).
       Since gcd(k,32) = 1 the map j -> jk mod 32 is a bijection of
       Z/32 and x^{jk} = (-1)^{floor(jk/32)} x^{jk mod 32}, so g is
       ternary of the SAME weight U, and g(theta) = f(theta^k) = 0. []
Corollary (also registered): the cell is independent of which
primitive 64th root theta is chosen (all 32 choices give
signed-permutation-equivalent kernels), so AU, NKER, TMASS, CRATIO are
well defined; and the same statement holds at N = 16 with Phi_32,
64 -> 32, and at kappa = 2 (M2, Lambda = {1,3}) with the condition
"exists odd k with f(theta^k) = f(theta^{3k}) = 0", for which
p^2 | Res is a cheap NECESSARY condition, verified directly at each
candidate p.

**Consequence: the sweep is over f, not over p.**  One enumeration of
low-weight ternary f decides EVERY prime in the band simultaneously.

Enumeration domain (registered): f normalized by the mu_64 negacyclic
group (32 shifts x global sign, order 64) — support required to be the
lex-min-gap-sequence cyclic representative containing 0, and eps_0 =
+1.  Every orbit keeps >= 1 representative (proof: rotate a support
element to 0, then fix the sign), so the enumeration is COMPLETE;
symmetric supports may keep more than one, which only duplicates hits.

Leaf counts L(U) = NC(32,U) * 2^{U-1}, NC = necklace count:
  U=4: 9,024   U=5: 100,688   U=6: 906,752   U=7: 6,731,712
  U=8: 42,080,768   U=9: 224,390,400
  cumulative U<=6: 1,016,464 ; U<=7: 7,748,176 ; U<=8: 49,828,944 ;
  U<=9: 274,219,344.
At N=16 (Phi_32, group order 32) the whole U<=12 enumeration is
1.13e6 leaves.

Norm evaluation (registered): Res = prod_{k odd} f(w^k) mod q for one
prime q ~ 2^61 with 64 | q-1; since 0 < Res <= U^16 <= 2^50.7 < q for
U <= 9, this recovers Res EXACTLY.  DFS keeps the 32-vector of partial
evaluations; a leaf costs 32 adds + 31 mulmods.

Band extraction (registered, and PROVED complete): let
Bmax = U^16 / 2^30.  Strip from Res every prime factor <= Bmax (one
math.gcd against a precomputed primorial, iterated), leaving R.  Then
p in [2^30, 2^34] divides Res  <==>  R is prime and R in [2^30,2^34].
  Proof: if p | Res with p >= 2^30 then Res/p <= U^16/2^30 = Bmax, so
  the whole cofactor is stripped and R = p.  Conversely R | Res.  And
  at most ONE band prime can divide Res because 2^60 > U^16 for U<=9.
CORRECTION MADE IN ADVANCE: my first draft of this step assumed every
odd prime factor of Res is = 1 mod 64.  That is FALSE — q | Res only
forces x^32+1 and f to share a factor of degree ord_64(q) over F_q, so
primes with q^2 = 1 mod 64 (31, 97, 127, ...) can divide.  The strip
therefore uses ALL primes <= Bmax, not just the 1 mod 64 ones.  Every
surviving hit is additionally re-verified directly by evaluating
f(theta^k) mod p, so the residue class of p is never assumed.

**Pricing (registered BEFORE running).**  Per-leaf budget <= 12 us on
one core (P-U7).  Predicted single-core walls: U<=7 93 s, U<=8 598 s,
U<=9 3,290 s (the last sharded 6 ways -> ~9 min wall).  Amortized cost
per admissible prime for the U<=7 census: 7.75e6 leaves / 2.1e7 primes
= 0.37 leaves = ~4.4 us of CPU per prime, against wenum's measured
174-297 s per prime — a factor ~5e7.  This is D1's "arithmetic
characterization that replaces enumeration entirely".

### U1 — TARGET SWEEP COUNT (D2), from the U0 pricing

- COMMITTED: the ENTIRE band — all ~2.1e7 admissible kappa=1 primes in
  [2^30, 2^34] — decided EXHAUSTIVELY for weights U <= 7.
  (Round 25's sample was 47 cells; this is 4.5e5 times more, and it is
  a census rather than a sample.)
- COMMITTED IF the measured leaf rate is >= 60,000 leaves/s/core:
  U <= 8 over the whole band.
- STRETCH if >= 100,000 leaves/s/core: U <= 9 over the whole band
  (which makes the brief's escape test on the two banked UMIN=9 and
  two banked UMIN=11 cells a native output of the instrument).
- N=16 GROUND-TRUTH ARM (validation, committed): the same census at
  U <= 12 over the whole N=16 band, compared cell-by-cell against the
  banked EXHAUSTIVE 1305-cell N=16 line.  This is where the filter's
  recall is MEASURED against truth rather than asserted.
- kappa=2 arm (committed): RESSIEVE over the 266 in-band M2 primes at
  U <= 9, then BBM on every promoted cell plus as much of the
  exhaustive 266 as the budget allows (committed floor: 60 cells;
  stretch: all 266 as a background job).

### U2 — TRIAGE THRESHOLD (what promotes a cell to exact BBM)

For each prime the sieve returns the EXACT low-weight profile
AU[U], U <= Umax (64 x number of orbits found, then re-verified).
Define
    H(p)     = (2^32 - 1) / p^kappa
    BONUS(p) = sum_{U <= Umax} AU[U] * 2^{-U}
    PREDCR(p)= 1 + BONUS(p) / (1 + H(p))
(justification registered: E[mass from weights > Umax] = H exactly, so
PREDCR is the conditional mean of CRATIO given the low-weight profile).

REGISTERED PROMOTION RULE: promote p to exact BBM iff
    PREDCR(p) >= 1.30      OR      UMIN(p) <= 6 .
BBM is run in DESCENDING PREDCR order so that if the wall cuts the
pass short, the cells the verdict rests on are the ones computed.
Budget: 24 promoted cells committed (stretch 48), plus 6 CONTROL cells
with BONUS = 0 drawn from the same sigma range to measure the body.
Every verdict-bearing cell gets the two-way re-derivation of D4.

### U3 — PREDICTIONS (numeric windows, registered before computing)

- P-U1 (escape/replay).  The banked record cell replays EXACTLY:
  TNUM 11700545024, NKER 392641, CRATIO 1.4210954721; and the RESSIEVE
  at U<=9 reproduces all SIX banked wenum low-weight profiles exactly
  — AU[9]=128 at p=4683696257, AU[9]=64 at 12148002497, nothing at
  U<=9 for 4294967681 and 6074003393 (UMIN=11), AU[9]=64 at the
  kappa=2 primes 63361 and 65921.  Predicted 6/6, 0 disagreements.
- P-U2 (recall on ground truth).  On the exhaustive 1305-cell N=16
  line: of the top-20 cells by EXACT CRATIO, >= 18 appear in the
  sieve's top-40 by PREDCR (recall >= 0.90); Spearman correlation
  between PREDCR (Umax=12) and exact CRATIO over all 1305 cells
  >= 0.85; and the N=16 record p=161761 has UMIN exactly 5.
- P-U3 (N=16 census).  Distinct in-band N=16 primes with UMIN <= 5 in
  [2, 60]; UMIN <= 6 in [20, 400]; UMIN <= 7 in [120, 900].
- P-U4 (N=32 census).  Distinct band primes carrying an orbit of
  weight <= 4 in [0, 5] (point estimate 0 — the norm cap 4^16 = 2^32
  makes it near-impossible); <= 5 in [10, 3000] (point 390); <= 6 in
  [300, 20000] (point 3900); <= 7 in [3000, 120000] (point 30000).
- P-U5 (THE VERDICT — I predict outcome 1, the kill).  At least one
  exactly-computed N=32 cell will have CRATIO > 2, killing the
  C-form's own bar.  Point estimate of the max over BBM'd cells 2.45,
  window [1.75, 3.05].  Mechanism registered in advance: a single
  weight-5 mu_64-orbit contributes 64*2^-5 = 2.0 to TMASS regardless
  of p, while the denominator 1 + H -> 1.25 at sigma = -2, so
  CRATIO -> 1 + 2.0/1.25 = 2.6; the same arithmetic at N=16 gives
  1 + 1.0/1.25 = 1.80, which is why the EXHAUSTIVE N=16 record is
  1.7681.  The ceiling therefore grows like 1 + 2N*2^{-Umin}/(1+2^sigma)
  — LINEAR IN N — and the round-25 "decay direction" is an artifact of
  sampling 47 cells out of 2.1e7.  FALSIFIER of my own prediction: if
  the weight-5 stratum is empty at p >= 2^32.5, the max will instead
  land in [1.35, 2.00] and Z-CEILING survives this round.
- P-U6 (argmax structure).  The argmax cell has UMIN in {5,6} and
  sigma in [-2.00, -0.80].
- P-U7 (throughput).  <= 12 us per leaf per core; the U<=7 N=32
  census finishes in <= 900 s on one core.
- P-U8 (predictor accuracy).  On promoted+BBM'd cells,
  |CRATIO_exact - PREDCR| <= 0.25 for >= 80% of cells, and
  CRATIO_exact >= PREDCR - 0.10 for >= 90%.
- P-U9 (two-way).  0 disagreements on every verdict-bearing cell.
- P-U10 (kappa=2).  Max CRATIO over kappa=2 cells computed in
  [1.30, 2.10]; number of the 266 in-band M2 primes with UMIN <= 7 in
  [0, 6].
- P-U11 (Z-FLOOR).  0 violations at every cell computed this round.

### U4 — VERIFICATION PLAN (D4)

1. Instrument vs. an independent algorithm: RESSIEVE's per-prime AU
   profile must equal wenum.py's (a completely different method:
   bucket-bisect MITM with packed weight-count vectors) on all six
   banked profiles, and on any new cell where a fresh wenum is run.
2. Every sieve hit is re-verified arithmetically at p: recompute
   theta = elt_of_order(p, 64) and check f(theta^k) = 0 mod p for the
   explicit k, and check p = 1 mod 64.  A hit that fails is discarded
   and reported.
3. Every verdict-bearing cell: exact BBM (identity split, RBUCK=256)
   AND BBM-ALT (even/odd permutation, RBUCK=181) — TNUM and NKER must
   agree as integers.  Round-25 standard: disagreements = 0.
4. Z-FLOOR checked at every cell.

### U5 — SCOPE / COMPLIANCE (binding)

Every number produced this round is about the FORM of CONJECTURE
Z-CEILING on the toy families (M4 = I2/RSET, M2 = negacyclic GRS) on
the 2-power grid.  Nothing here is a claim about Z_1 at the official
row; the f2 calibration clause binds.  Census evidence is evidence,
never proof.  Draft-only: my writes are confined to
notes/pilots_20260809/umin_spike_hunt/ plus NEW checkpoint files in
z_n32_band/ckpt/.  No dag/nodes/tools edits, no git, no Modal, stdlib
only, every interpreter run under tools/ramguard.  Quarantine
observed: CAMPAIGN_LEDGER.md at/below line 3872 and the other round-26
pilot directories are not read.

