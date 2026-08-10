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

# PILOT REGISTRATIONS

Opus pilot, 2026-08-09, written BEFORE any computation (no python3 has
been run in this session at the time of writing; only file reads).
Everything below is binding; deviations are recorded as explicit
self-corrections in the final report.

## R0. The object and the one structural fact I will lean on

R = Z[x]/(x^h+1), h = N'/2, box B_h = {-2..2}^h.  Fold reduction
(quoted round-24, `notes/pilots_20260808/kernel_window_hunt/PREREG.md:107-111`):
a non-cyclotomic ternary kernel vector at p of support <= 2l' exists
iff some nonzero w in B_h with ||w||_1 <= 2l' has p | Norm(w).

STRUCTURAL FACT (registered as the spine of D3, to be proved, not
assumed): Norm(w) = Res(Phi_{N'}(x), w(x)); if an odd prime p divides
it then Phi_{N'} has a root mod p, that root has exact order N', hence
**p = 1 mod N'**.  Every odd prime factor of a box norm is = 1 mod N'.
So BAD PRIMES = the odd prime divisors of box norms, and their v_2 is
>= m := log2 N' by construction.  "Baseline" below always means m
(m = 4 at N'=16, 5 at N'=32, 7 at N'=128, 8 at N'=256), and EXCESS
e := v_2(p-1) - m is the only interesting coordinate.

## R1. The v_2-profile predictions (falsifiable, registered first)

- **(V1) CONDITIONAL-BADNESS INDEPENDENCE.**  At the h = 8 exhaustive
  ground truth, define BADFRAC8(v | window) = (# bad primes with
  v_2(p-1) = v in a dyadic window) / (# ALL primes = 1 mod 16 with
  v_2(p-1) = v in that window).  I predict this is INDEPENDENT of v
  within Poisson error at fixed window, i.e. large v_2 is rare among
  bad primes ONLY because it is rare among primes.  FALSIFIER: a
  monotone decline in BADFRAC8(v) over >= 3 consecutive v at fixed
  window, significant at 95% Poisson, would be real structural
  suppression and would SUPPORT option (c).
- **(V2) EXHIBITION AT THE TOY.**  I predict MAXV2BAD8 :=
  max v_2(p-1) over all h=8 bad primes is >= 12, specifically that
  **p = 12289 = 3*2^12+1 is bad** (`ge_floor_falsifier/REPORT.md:128`
  exhibits w with Norm = 12289 exactly), i.e. EXCESS >= 8 at the toy.
  Low-confidence sub-prediction (register ~7%, the measured 2^16
  density): 65537 is also bad (EXCESS 12).
- **(V3) THE LADDER LAW AT h = 64.**  From the banked round-24 shards
  (`state/v2hunt_*.json`, 1.22e6 samples / 170236 admissible hits) the
  profile is an EXCESS at exactly v_2 = 7 (P ~ 0.70) followed by a
  geometric tail.  I register the law
        P(v_2(p-1) >= v)  =  K * 2^-(v-7),  K ~ 0.64,  v >= 9,
  and predict every new rung matches it within a factor of 2 up to the
  coverage limit: **NO BEND**.  A sustained ratio outside [0.40, 0.60]
  over 3 consecutive rungs is a finding in either direction.
- **(V4) NORM-SIDE LAW.**  v_2(Norm(w) - 1) obeys the same law; the
  excess at 7 is predicted to be an artefact of the prime-factor
  count (N = prod (1 + 2^7 m_i)^{e_i} gives v_2(N-1) = 7 iff
  sum e_i m_i is odd), not a new 2-adic obstruction.
- **(V5) COVERAGE PREDICTION.**  With the compute available (14 cores,
  a few hours) the ladder reaches MAXV2HIT in [28, 33] and does NOT
  reach 41.  Registered in advance: that silence is coverage-bounded
  and is NOT evidence for (c).
- **(V6) THE DECISION NUMBER.**  Under the lattice-count heuristic the
  number of bad primes with v_2(p-1) >= v in W_ADM is ~2^(C - v) for a
  constant C I will compute and CALIBRATE against the h=8 (and h=16)
  exhaustive/sampled truth.  I predict C in [125, 150], hence the
  heuristic emptiness threshold v* = C is FAR above 41 and option (c)
  at threshold 41 is predicted **FALSE**, with ~2^(C-41) predicted
  counterexamples.  FALSIFIER: if the toy calibration shows the
  heuristic over-predicts badness by more than 2^40, v* could fall
  near 41 and (c) would be heuristically safe.

## R2. The graded-ladder sampling law (exact, seeded, reproducible)

PRNG `random.Random(seed)`; registered seeds
**20260809, 1009, 2029, 3049, 4099, 5119, 6143, 7177, 8191, 9209,
10243, 11261** (one per shard).  Families reused verbatim from
`notes/pilots_20260808/kernel_window_hunt/klib.py` (fam_A/fam_B/fam_C,
tower_norm, strip_small, is_probable_prime, kernel_membership).

- **LADDER RUNGS** (as the brief fixes them): L in {8, 12, 16, 24, 32,
  41}.  No rung at 7 (that is the trivial baseline; CATCH-19B: no
  shift-0 cell).  Budgets are powers of two (CATCH-Z6).
- **GATE (the speed-up, registered honestly with its bias).**  For each
  sampled w compute N = |Norm(w)| exactly, then g := v_2(N-1) at
  ZERO extra cost, and only run trial division + BPSW when g >= 8.
  BIAS REGISTERED IN ADVANCE: this gate finds exactly the COFACTOR-1
  witnesses (N = p), because for N = c*p with c = 1 + 128k > 1 one has
  v_2(N-1) = v_2(c p - 1) = 7 + v_2(k) generically, unrelated to
  v_2(p-1).  I therefore ALSO run an UNGATED control stream (full
  pipeline on every sample, no gate) to measure the c > 1 population
  and to confirm the gated ladder is not creating the geometric law it
  reports.  Both streams are reported separately.
- **ACCEPT**: ROUGH = N / SMOOTHPART(B_TD = 2^17) is a BPSW+64-MR
  probable prime, ROUGH = 1 mod 128, 2^128 < ROUGH <= 253^32, and
  v_2(ROUGH - 1) >= L.  COFAC = N/ROUGH recorded and compared to 2^12.
- **VERIFY (fail-closed, every reported hit)**: (1) w in {-2..2}^64,
  w != 0, ||w||_1 recorded; (2) p = 1 mod 2^L, bit length, window;
  (3) BPSW + 64 MR; (4) N mod p == 0 from an independently recomputed
  norm; (5) KERNEL MEMBERSHIP by the tower-independent route
  (rho of exact order 128, odd s with sum_i w_i rho^{si} = 0 mod p);
  (6) a standalone zero-import reproduction script printing PASS/FAIL.
  A hit at L >= 41 in the admissible window KILLS option (c) and
  outranks everything: I stop and report it.
- **CHECKPOINTING**: every shard writes `state/lad_<seed>.json` and
  resumes from it; every python3 through
  `tools/ramguard tiny|local -- python3 ...` from the repo root.

## R3. The mechanism-proof plan (D3), with the bar for PROVED

Three routes, run in order; PROVED means a complete argument I would
sign, with every constant checked numerically:
1. **ELEMENTARY NORMLAW.**  Norm(w) > 0 (K totally complex) and every
   odd prime factor is = 1 mod N' (R0) => Norm(w) = 1 mod N' whenever
   Norm(w) is odd.  This subsumes the conductor-128 local-reciprocity
   analogue and makes it two lines.
2. **LOCAL RECIPROCITY, THE REAL QUESTION.**  K_2 = Q_2(zeta_{2^m}) is
   totally ramified of degree 2^(m-1) over Q_2 and local CFT gives
   N(K_2^*) = <2> x (1 + 2^m Z_2), hence
   N(K_2^*) INTERSECT Z_2^* = 1 + 2^m Z_2 **exactly and surjectively**.
   If that is right, local reciprocity proves v_2(Norm - 1) >= m and
   PROVES THAT NOTHING MORE IS FORCED: there is no local obstruction to
   v_2(p-1) large.  I will verify the group-index arithmetic and test
   surjectivity numerically (hit every residue in 1 + 2^m Z_2 / 2^M by
   actual ring elements).  Registered in advance: I expect this route
   to KILL the mechanism rather than establish it.
3. **NEWTON/TRACE REFINEMENT.**  For w = 1 + 2v, N - 1 = sum_k 2^k c_k
   with c_k the char-poly coefficients of v; all power sums satisfy
   Tr(z) = 2^(m-1) z_0, so Newton's identities force v_2(2^k c_k) >= m
   with equality reachable at k = 1, 2.  If instead the identities
   force a LOWER BOUND that grows with some feature of w, that is a
   real theorem and (c) becomes theorem-backed.  Registered prediction:
   they do not; the bound is m, flat.
VERDICT VOCABULARY: **PROVED** (obstruction exists, (c) theorem-backed)
/ **PROVED ABSENT** (the route proves no obstruction can exist) /
**GAPPED** (argument incomplete, named gap) / **DEAD** (route refuted).

## R4. Named functionals (CATCH-19C)

- **V2P(p)** = v_2(p-1); **EXCESS(p)** = V2P(p) - m.
- **BADFRAC8(v | window)**, **BADFRAC16(v | window)** — R1(V1).
- **BADDENS(h, j)** = fraction of primes = 1 mod N' in [2^j, 2^(j+1))
  that divide some box norm (exhaustive at h=8, sampled at h=16).
- **HEURFRAC(h, j)** = the lattice-count prediction 5^h/(2h * 2^j) for
  the same cell; **OVERPRED(h, j)** = HEURFRAC/BADDENS (the calibration
  factor that enters V6).
- **LADCOUNT(L)** = accepted hits with V2P >= L; **LADRATIO(L)** =
  LADCOUNT(L+1)/LADCOUNT(L) (the suppression curve).
- **GATEFRAC(g)** = fraction of sampled w with v_2(Norm-1) >= g.
- **MAXV2HIT** = max V2P over all accepted hits; **MAXV2BAD8** =
  max V2P over the exhaustive h=8 bad-prime set.
- **COFAC1FRAC** = fraction of accepted hits with COFAC = 1.
- **CSTAR** = the calibrated constant C of V6; **VSTAR** = C (the
  heuristic emptiness threshold in v_2).
- **COVERAGE(L)** = number of distinct box vectors fully processed at
  rung L (the honest denominator of any silence).

## R5. Process

Draft-only in `notes/pilots_20260809/large_v2_hunt/`; checkpoints to
`./state/`; every python3 through `tools/ramguard tiny|local -- python3`
from the repo root; no git, no Modal, stdlib only; no status flips; no
edits to dag.json, nodes/, or tools/.  QUARANTINE HELD: I do not read
`notes/pilots_20260802/CAMPAIGN_LEDGER.md` at or past line 3731, and I
do not open the other round-25 pilot dirs
(c2pp_falsifier_redesign, m7_complement_repose, pr_harvest, z_n32_band);
this clause is passed verbatim to any subagent.
