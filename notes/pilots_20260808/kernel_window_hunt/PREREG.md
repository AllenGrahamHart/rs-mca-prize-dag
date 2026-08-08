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

# PILOT REGISTRATIONS

Opus pilot, 2026-08-08, written BEFORE any computation (no python3
has been run in this session at the time of writing). Everything
below is binding; deviations must be recorded as self-corrections
in the final report.

## P0. The object, restated exactly (from the sources)

R = Z[x]/(x^h + 1), h = N'/2. For v in {-1,0,1}^{N'} in
K_p = {v : sum_j v_j zeta^j = 0 mod p}, the fold
w_i = v_i - v_{i+h} (0 <= i < h) lands in {-2..2}^h, has
||w||_1 = supp(v), and
`background/nodes/integer_code_distance_high_field_folded_box_exclusion/proof.md:3-14,52-55`
gives: v is CYCLOTOMIC (antipodal) iff w = 0. Hence

  **NON-CYCLOTOMIC TERNARY KERNEL VECTOR AT p, SUPPORT <= 2l'
   <=> nonzero w in {-2..2}^h with ||w||_1 <= 2l' and p | Norm(w).**

(Same reduction quoted at
`critical/nodes/integer_code_distance_cert/statement.md:53-57`.)

## P1. Rows and windows (file:line provenance)

- SPEC CAP: `|F| < 2^256`, `k <= 2^40` —
  `background/nodes/official_row_primes_pinning/proof.md:27-30`
  (as cited by `notes/pilots_20260807/ge_lattice_cert/REPORT.md:55`).
- NO FINITE REGISTRY:
  `background/nodes/official_row_primes_pinning/statement.md:8-10`
  and `critical/nodes/integer_code_distance_cert/statement.md:16-18`.
- QUOTIENT-ORDER CONDITION: an N'=128 row needs a zeta of exact
  order 128 in F_p, i.e. `p = 1 mod 128` —
  `.../integer_code_distance_high_field_folded_box_exclusion/statement.md:7-8`.
- PROVED CEILING: `p > 253^32` forces emptiness —
  same node `statement.md:17,20-25`; proof case 1 (some w_i odd,
  S <= 63*4+1 = 253) at `proof.md:35-40`, case 2 (all even,
  |N(B)| <= 64^32) at `proof.md:41-50`.

Registered windows (p always prime, p = 1 mod 128):

| name | definition | rationale |
|---|---|---|
| **W_TOP** | 2^244 <= p <= 253^32 | the coordinator's D1 window |
| **W_DEP** | 2^166 <= p <= 253^32 | at/above the smallest DEPLOYED Proth prize row (167 bits, `ge_lattice_cert/REPORT.md:68-71`) |
| **W_ADM** | 2^128 < p <= 253^32 | ADMISSIBLE-WEAK: N'=128 quotient exists, p < 2^256, and p > 2^128 so `eps* |F| = 2^-128 p > 1` is a meaningful list bound |
| **W_ALARM** | p > 253^32 | a hit here would CONTRADICT a PROVED node; treated as an alarm on my own pipeline, not a result |

STRONG-ADMISSIBLE (recorded per hit, not required): additionally
v_2(p-1) >= 41, i.e. p supports a power-of-two smooth domain of
the deployed size n = 2^41..2^44 (`ge_lattice_cert/REPORT.md:66-71`).
I register in advance that a W_ADM/W_DEP hit with only
v_2(p-1) >= 7 falsifies the family-uniform statement AS POSED in
this brief ("every admissible N'=128 row, p = 1 mod 128 in the
prize window"), and simultaneously that such a p supports the row
(F_p, L of order n = 2^{v_2(p-1)}, k = rho n) only for
n <= 2^{v_2(p-1)}; I will state that limitation explicitly rather
than claim deployed-scale falsification I have not earned.

## P2. Structural prediction registered BEFORE running (so the
##     outcome can falsify me, not just the conjecture)

Parseval over the 64 odd residues gives |Norm(w)|^2 <= S^h with
S = sum_i w_i^2, so log2|Norm| has a HARD ceiling 32 log2 S and,
under the standard random model (|w(zeta)|^2 ~ S * Exp(1),
32 conjugate pairs), a MEAN of 32(log2 S - gamma/ln 2) and an sd
of about 2*sqrt(32)*pi/(sqrt(6) ln 2) = 10.5 bits. Registered
consequences:

- (P2a) At h = 64 the largest ODD S is 253, so the mean of
  LOGNORM is 32(log2 253 - 0.8327) = **228.8 bits** while W_TOP
  starts at 244: **the h=64 hunt is a TAIL problem** (about
  +1.45 sd), and no choice of w moves the mean into W_TOP.
- (P2b) All-even w (S = 256, the AM-GM extremal) is USELESS for
  odd primes: Norm(2B) = 2^64 Norm(B) with |Norm(B)| <= 64^32 =
  2^192, so the odd part is capped 63 bits BELOW W_TOP. I
  therefore register the parity constraint as part of the
  sampling law rather than discovering it later.
- (P2c) At h = 128 (N'=256) S is free up to 509, so LOGNORM's
  MEAN can be TUNED onto any target band by choosing the support
  s (mean = 64(log2 s - 0.8327); s ~ 27 centres it on 2^250):
  **the N'=256 control is a MEAN problem, not a tail problem.**
- (P2d) Counting prediction: #(box classes) = 5^64 = 2^148.6, so
  for a FIXED p ~ 2^250 the expected witness count is 2^-101.4
  (consistent with E1-128 CERTIFIED EMPTY,
  `lattice_cone_certificate/statement.md:86-92`), while summed
  over the box the number of BAD primes in W_TOP is predicted
  ~2^139. I register the prediction that **witnesses exist in
  abundance and the only difficulty is exhibiting one**; if the
  hunt returns silence at the registered coverage, that silence
  falsifies THIS prediction and must be reported as such.

## P3. Sampling law (exact, seeded, reproducible)

PRNG: `random.Random(seed)` (stdlib Mersenne Twister); seeds
registered here: **20260808, 1729, 2718, 31415, 65537**. Every
family draws coordinates independently unless stated.

- **FAM-A (uniform box)** — w uniform in {-2..2}^64. Baseline for
  the measured LOGNORM distribution.
- **FAM-B (odd-extremal, S = 253)** — one uniformly chosen
  position gets a uniform sign in {+1,-1}; the other 63 get
  uniform signs in {+2,-2}. Maximal odd-norm shape (P2b).
- **FAM-C (S = 247)** — exactly three odd coordinates (+-1), rest
  +-2; diversity hedge against FAM-B degeneracy.
- **FAM-D (THRESHOLD CLIMB)** — start from FAM-B; repeatedly try
  single-coordinate moves (flip a sign; move the odd position;
  toggle a coordinate between +-2 and +-1 keeping the count of
  odd coordinates odd) and accept the first strictly
  LOGNORM-increasing move; stop when LOGNORM >= T = 244 or no
  improving move exists. CLIMBGAIN recorded.
- **FAM-E (LEVEL-SET WALK)** — from a FAM-D output, random
  single-coordinate perturbations, accepted iff LOGNORM stays
  >= T; used to generate MANY in-band vectors with decorrelated
  norms. Diversity is audited (DISTINCTNORMS).
- **FAM-F (h=8 maximiser lift)** — the exhaustively determined
  h=8 MAXNORM shapes, lifted to h=64 by (i) w(x) := u(x^8)
  (registered in advance as expected-useless: Norm_64(u(x^8)) =
  Norm_8(u)^8, a perfect 8th power, so its prime factors are
  <= 2^32-ish) and (ii) sign-pattern tiling with an odd-parity
  repair. Run as a structure probe, not as the main hunt.

## P4. Norm, factoring, cofactor bound, acceptance

- Norm by the coordinator-replayed exact 2-adic tower recursion
  `notes/pilots_20260807/ge_floor_falsifier/gelib.py:41-56`
  (`tower_norm`, exact integers, no floats). REUSED verbatim by
  import; not re-derived.
- **TRIAL BOUND B_TD = 131072 = 2^17** (registered widening of
  the brief's 2^12: strictly more inclusive, and I record the
  realised cofactor for every hit so the brief's c <= 2^12
  criterion can be read off). SMOOTHPART = product of all prime
  powers with prime < B_TD dividing |Norm(w)|;
  ROUGH = |Norm(w)| / SMOOTHPART.
- **ACCEPT (primary)** iff ROUGH is a probable prime and ROUGH
  lies in the target window. COFAC := |Norm(w)|/ROUGH is recorded
  and compared with 2^12.
- **ACCEPT (secondary)** if ROUGH is composite: Pollard-Brent rho
  with a registered budget of 2^20 iterations; any split factor
  that is a probable prime in the window is a hit. (Registered
  in advance as a long shot: a 250-bit semiprime will not split.)
- Primality labelling: **BPSW** = strong base-2 Fermat + strong
  Lucas (Selfridge parameters), plus 64 random-base Miller-Rabin
  rounds. Reported as **PROBABLE PRIME**, never "prime", unless a
  Pocklington/BLS certificate on p-1 is actually obtained (I
  attempt it: trial-factor p-1 to 10^7 and test whether the
  factored part exceeds p^{1/3}; registered as unlikely).

## P5. Independent verification required of every hit (fail-closed)

A hit is reported only if ALL of the following pass, the last
three using code paths INDEPENDENT of `tower_norm`:

1. w != 0 and w in {-2..2}^64; ||w||_1 recorded against 2l'.
2. p = 1 mod 128; bit length and window membership recorded.
3. BPSW + 64 MR on p.
4. |Norm(w)| mod p == 0 recomputed from the stored norm.
5. **KERNEL MEMBERSHIP** (independent of the tower recursion):
   find g with rho = g^((p-1)/128) mod p of exact order 128
   (rho^64 = -1 mod p), then exhibit an odd s with
   sum_i w_i rho^{s i} = 0 mod p. This is a direct certificate
   of a non-cyclotomic ternary kernel vector at (p, N'=128).
6. Standalone reproduction script with zero imports from my own
   library, printing PASS/FAIL from the literal constants.

## P6. Calibration (h = 8, N' = 16) — MANDATORY BEFORE ANY h=64 CLAIM

Ground truth quoted for comparison:
`notes/pilots_20260807/ge_floor_falsifier/REPORT.md:130` —
"536 bad primes, largest 463249. Density by dyadic window: 1.00
(<=2^12), 0.964 (2^12), 0.920 (2^13), 0.672 (2^14), 0.281 (2^15),
0.069 (2^16), 0.013 (2^17), 0.003 (2^18), 0.000 (2^19+)"; and
MAXNORM(h=8) = 614656 = 28^4 (`REPORT.md:134`);
TIGHTEMPTY(16,16) = 463249 attained
(`critical/nodes/lattice_cone_certificate/statement.md:30-34`).

Acceptance criteria, all required:
- **C1 (exhaustive re-derivation)** — my own exhaustive census of
  the 5^8 box reproduces: 536 bad primes, largest 463249,
  MAXNORM = 614656, and all nine dyadic densities EXACTLY.
- **C2 (pipeline recall)** — the h=8 run of the IDENTICAL sampling
  pipeline (same norm/trial-division/PRP/window code) must
  recover known bad primes in the h=8 analogue of W_TOP. The
  analogue is fixed by the same relative log position:
  ceiling_odd(h) = (4(h-1)+1)^{h/2}; at h=64 the W_TOP floor is
  244/log2(253^32) = 0.9552 of the ceiling, so at h=8 the floor
  is 0.9552 * log2(29^4) = 2^18.56. PASS iff (i) every prime the
  sampler reports is in the exhaustive bad set (ZERO false
  positives — a false positive is a hard FAIL), and (ii) the
  number recovered is within a Poisson 95% interval of the
  exhaustive per-vector hit rate times the sample budget.
- **C3 (density agreement)** — the sampler's estimate of
  BANDFRAC and of the per-vector hit rate agrees with the
  exhaustive value within a factor of 2.
- **C4 (planted fail-closed)** — a vector with a known bad prime
  is injected into the sampled stream and must be detected; and a
  deliberately corrupted norm must NOT be accepted.
- If C1-C4 do not all pass, **no h=64 statement is made at all**.

## P7. N' = 256 positive control (D3)

h = 128, box {-2..2}^128, p = 1 mod 256. Families **FAM-S(s)**:
support s (odd, so the norm is odd), positions uniform, entries
uniform in {+1,-1}, rest 0; registered s in {21, 27, 33, 41}
(predicted mean LOGNORM = 64(log2 s - 0.8327) = 231/250/265/278).
Same pipeline, same acceptance, same independent verification
with rho of order 256. Registered notes: ||w||_1 = s <= 66 also
satisfies the TIGHTEST declared clean-anchor support bound
2l' = 66 (rate 1/8, N'=256) from
`background/nodes/qfloor_clean_anchor_norm_threshold_route_cut/statement.md:9-13`,
so such a witness is inside the declared radius of a deployed
row, not merely inside the full box. Prior art acknowledged:
PRO_W3 already predicts ~2^48 witnesses at N'=256
(`background/nodes/e1_folded_no_vector_certificate_256_payload/PRO_W3_e1_density.md:26-27`);
the previous Modal campaign searched the LATTICE at a PINNED
prime and returned NO_WITNESS_WITHIN_SEARCH_BUDGET
(`.../falsification_report_20260726.md:44-49`). My direction is
the reverse (fix w, factor Norm) and produces a FREE prime, which
I will state plainly is a weaker object than a witness at the
pinned exhibit field.

## P8. Named functionals (CATCH-19C)

- **LOGNORM(w)** = log2 |Norm_{R/Q}(w)|.
- **S(w)** = sum_i w_i^2 (the Parseval/AM-GM budget).
- **ODDPART(w)** = |Norm(w)| / 2^{v_2(Norm(w))}.
- **SMOOTHPART(w), ROUGH(w)** at B_TD = 2^17 (P4).
- **COFAC(w,p)** = |Norm(w)| / p for an accepted p.
- **BANDFRAC(t)** = fraction of sampled w with LOGNORM >= t.
- **HITRATE(W)** = accepted hits in window W per sampled vector.
- **CLIMBGAIN** = LOGNORM(after FAM-D) - LOGNORM(before).
- **DISTINCTNORMS** = #distinct |Norm| among in-band samples
  (diversity audit for FAM-D/FAM-E).
- **BADDENS8(j)** = exhaustive h=8 fraction of primes = 1 mod 16
  in [2^j, 2^{j+1}) that divide some box norm.
- **RECALL8** = fraction of C2's expected recoveries achieved.
- **COVERAGE** = total number of DISTINCT box vectors whose norm
  was fully processed (the honest denominator of any silence
  claim), reported per family.

## P9. Rarity bound to be reported if the hunt is silent

If no hit: I report COVERAGE, the measured BANDFRAC, the measured
per-in-band-vector near-primality rate, and the resulting
one-sided 95% Poisson upper bound on HITRATE, plus the explicit
statement that this bounds only the SAMPLED region and says
nothing about the 2^148.6-size box. No silence is ever reported
as evidence for a theorem beyond that bound.

## P10. Process

Draft-only in `notes/pilots_20260808/kernel_window_hunt/`;
checkpoints to `./state/`; every python3 invocation through
`tools/ramguard tiny|local -- python3 ...` from the repo root
with a self-imposed soft wall below the profile wall; no git, no
Modal, stdlib only; no status flips; no edits to dag.json,
nodes/, or tools/.
