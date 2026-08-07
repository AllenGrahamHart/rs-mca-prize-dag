# PRE-REGISTRATION — MYSTERY 6 DIAGNOSIS: l1_mixed_petal_amplification (round 21)

Round 21, 2026-08-07. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: the full mystery
pipeline, first pass, for the newly promoted mystery 6. A separate
auditor is surveying Codex's v4 PMA campaign — do NOT read
notes/wave24_integration_20260727/PMA_* drafts (blind; the
coordinator reconciles at the bank).

## 0. Sources (quote verbatim first)
- critical/nodes/l1_mixed_petal_amplification/{statement.md,
  attack.md, v4_pma_crosswalk.md, notes/} — the statement, the
  retraction record (petal_growth/RETRACTION_MANIFEST.md: the naive
  induction dead, dim K grows with c — the residue-line growth IS
  the obstruction), catch #176's 4x mass, the N10 growth censuses
  (43/2879/109391 and 33/2857/108600, doubling factor ~38;
  experiments/prize_resolution/l1_balanced_mixed_growth_census_result.md).
- The consumer: imgfib (req) — what the image-fiber count needs,
  quantified.

## 1. Deliverables
- (D1) THE CONSUMER CONTRACT: what does imgfib need from this
  bucket — polynomial with WHICH exponent, at which rows, against
  which reserve? Quote and derive the weakest sufficient form.
- (D2) THE OBSTRUCTION MADE EXACT: formalize "dim K grows with c";
  compute the growth law on the banked census families; determine
  what a proof must control that the retracted induction did not.
- (D3) THE MECHANISM HUNT: the censuses resist the super-polynomial
  falsifier on two chart families with doubling factor ~38 — find
  the mechanism (what bounds mixed-petal mass?) or the danger (what
  would make an adversarial received word blow it up?). An
  adversarial construction attempt is MANDATORY: try to build a
  received word violating polynomial growth at reachable scale
  before believing the censuses.
- (D4) CROSS-LANE CHECK: the band lane's pencil/petal machinery
  (xr_pencil_forcing_t0, the L-A/L-B theorems, LEMMA R) and the
  ternary object — does any banked instrument transfer with exact
  hypothesis matching? (The round-19 discipline: matrix with
  applies/fails-because per cell, no vibes.)
- (D5) The weakest-form re-pose draft with a pre-registered
  falsifier.

## 2. Falsifiers / honesty
- If (D3)'s adversarial construction succeeds, the mystery's floor
  form must be re-posed around the witness — report with a
  reproduction script and stop the positive line.
- Census evidence is evidence, never proof; label throughout.

## 3. Rules
- DRAFT ONLY in notes/pilots_20260807/l1_pma_diag/. Never edit
  dag.json/nodes/tools; no git. COMPUTE LAW: tools/ramguard
  tiny|local -- python3 (including file patching and JSON peeking).
  Verbatim quotes with file:line. No REPORT.md — your final message
  IS the report. Do not read CAMPAIGN_LEDGER entries after the
  "ROUND 21 LAUNCHED" marker; PASS THE QUARANTINE CLAUSE to any
  subagent you dispatch.

---

# PILOT REGISTRATIONS (appended 2026-08-07, BEFORE any computation)

Author: Opus pilot, round 21. Everything below is registered before a
single line of code is run. Sources already READ at registration time:
the node's `node.json` / `statement.md` (lines 1-130) / `v4_pma_crosswalk.md`
/ `notes/upstream_july_wave_20260729.md`; `critical/nodes/petal_growth/
RETRACTION_MANIFEST.md`; `critical/nodes/imgfib/{statement.md,
conditional.md,notes/l1_upstream_crosswalk_20260713.md}`;
`experiments/prize_resolution/l1_balanced_mixed_growth_census_{result.md,
modal.py}`. NOTHING under notes/wave24_integration_20260727/PMA_* was read.

## R0. What I claim to have derived BY HAND before computing

Reading `l1_balanced_mixed_growth_census_modal.py` (the N10 generator)
by eye gives, for the balanced chart at scale n, k=n/2:

- layout(): |core| = k-1, one background point, t = k/2 two-point
  petals, k petal points (source: lines 123-138).
- The band threshold is `2*(t-2) = k-4` and the core-defect condition
  forces `core_count <= 3`; the agreement condition `>= k+1` then
  forces `omitted <= core_count + background - 1 <= 3`
  (lines 242, 256-268).
- Hence the CANDIDATE COUNT has the exact closed form
    Cand(k) = A1*[C(k-1,1) + 2C(k-1,2) + 2C(k-1,3)]
            + A2*[C(k-1,2) + 2C(k-1,3)]
            + A3*C(k-1,3),
    A1 = k, A2 = C(k,2) - k/2, A3 = C(k,3).
  PREDICTION P1: this reproduces 5,096 / 386,640 / 27,152,032 exactly.
- Leading term A3*C(k-1,3) ~ k^6/36 = n^6/2304.
  PREDICTION P2: the census's ambient enumeration domain is Theta(n^6)
  with degree EXACTLY 6.

## R1. Registered hypotheses (falsifiable, stated before compute)

- **H-BOX (D2/D3).** The registered super-polynomial falsifier is
  UNFIREABLE by the N10 instrument: retained <= Cand(k) = Theta(n^6) a
  priori. FALSIFIED IF P1 or P2 fails.
- **H-RANDOM (D3).** The retained counts are the plain random-word
  (Schwartz-Zippel) prediction and carry no mixed-petal signal:
    Retained_pred = sum_{m>=1} N_{k+m}(k) * q^{-m} * (1-1/q)^{n-k-m},
  where N_{k+m} is the closed-form count of candidates of support size
  k+m. PREDICTION P3: this matches all six banked numbers
  (43, 33, 2879, 2857, 109391, 108600) to within 10%, and predicts the
  agreement-(k+2) sub-counts (8, 7, 62, 53) to within a factor 2.
  PREDICTION P4: the "doubling factor about 38" is q-driven — the
  predicted 32->64 ratio equals (N_33/N_17)*(97/193)*correction and
  lands in [36,41]. FALSIFIED IF the observed numbers deviate from
  Retained_pred by more than 10% at n=32 or n=64.
- **H-RESERVE (D1).** The banked census mass sits BELOW the corrected
  reserve at its own parameters. Define sigma_min(n,k,q) = least sigma
  with sigma*log2 q >= (1+eps)*log2 C(n,k+sigma). PREDICTION P5:
  sigma_min >= 3 at (16,8,97) and sigma_min >= 5 at (32,16,97) and
  sigma_min >= 8 at (64,32,193) even at eps = 0, while every retained
  contributor has sigma in {1,2}. FALSIFIED IF sigma_min <= 2 at any
  of the three rows.

## R2. The MANDATORY adversarial construction attempt (D3)

The N10 census fixes ONE received word per (n, mode) — `chart_word`
(lines 140-163) builds U from t petal scalars. The legal word family
compatible with the SAME layout is s = (s_1..s_t) in F_q^t with the
s_j distinct and nonzero. The census sampled 2 points of that family.
I will search it.

- **A1 (replication gate).** Re-implement the census independently and
  reproduce 43 at (16,8,97,consec) and 2879 at (32,16,97,consec).
  NOTHING below is reported unless A1 passes.
- **A2 (linearization).** For a candidate support S of size k+m, the
  retention condition "some deg<k polynomial matches U on S" is m
  linear conditions on U; since U vanishes on core+background, they
  are m linear forms in s. Registered claim: retained(s) <=
  #{S : M_S s = 0}, computable without interpolation.
- **A3 (exhaustive worst word at n=16).** t=4, q=97: enumerate all
  (97^4-1)/96 = 922,180 projective s and maximize the A2 upper bound;
  then compute the EXACT retained count for the top words by the A1
  census. Let MAX16 be the result.
- **A4 (the distinguished minimal-degree word).** Within the family,
  the words of minimal degree are singled out: U must vanish on the 8
  core+background points, so U = W*h with deg h <= k-1; deg U = k+1
  forces (hand derivation) s_j proportional to (x_j^2 - x_bg^2), a
  UNIQUE word up to scale. Registered prediction P6: this word's
  retained count is governed by ONE subset-sum condition
  e_1(S) = const on the domain mu_n, and is NOT super-polynomially
  larger than the mean.
- **A5 (scale test).** Repeat a randomized/structured max-search at
  n=32 (t=8). Let MAX32 be the best found.
- **PRE-REGISTERED ADVERSARIAL FALSIFIER (the D3 escape test):**
  the construction SUCCEEDS, the mystery must be re-posed around the
  witness, and the positive line stops, IF
     MAX32 / MAX16 > 3 * (mean32 / mean16)
  i.e. if the worst-case-over-words growth ratio exceeds three times
  the mean-over-words growth ratio; OR if MAX16 > 10 * mean16 (a
  single-scale blow-up). Otherwise the construction FAILS and I report
  the mechanism that stopped it. Either outcome is reported verbatim.
  A NEGATIVE result here is evidence about this chart family ONLY and
  will be labelled as such.

## R3. Honesty pins

- Census evidence is evidence, never proof — labelled at every use.
- Anything I derive by hand and then verify is labelled DERIVED+CHECKED;
  anything only measured is labelled MEASURED.
- If my re-implementation disagrees with the banked 43/2879 I report the
  disagreement and stop, rather than adjusting.
