# C1'-r3 F-ROUND 1 — REPORT

## VERDICT: **MIXED** (survived both refuting kill lines; the pre-registered
## amber watch tripped at two rows)

C1'-r3 (`c1r3_pose.md`: r2 conventions + official-admissibility gate v_2(q-1)>=41
/ analogue 20 + extended RAW ledger w<=L+7 + allowance 4 unchanged) was NOT
refuted: no in-hypothesis row violates E-1 <= 4r(1+W_ext) anywhere in the complete
33-row in-gate census below 2^28, and the trend does not extrapolate across the
allowance inside the hypothesis range. The K'>=1 amber line fired at two rows
(1.008, 1.025) — under the frozen pre-registration that makes the round MIXED,
not SURVIVED. Nothing was weakened mid-round.

## Kill-line outcomes (pre-registered in `c1r3_falsifiers.md`)

- **KILL-LITERAL (K'_r3 > 4) — NOT FIRED.** Worst K'_r3 = **1.024517293**
  (q=246415361, exact 1058880560632659/1033540934303744), a 3.9x margin. Every
  one of the 33 in-gate rows evaluated exactly.
- **KILL-AMBER (K'_r3 >= 1) — FIRED (2 rows):** q=81788929 (1.008154437) and
  q=246415361 (1.024517293), both with EMPTY extended ledger — bare-envelope
  fluctuations. => verdict MIXED per pre-registration.
- **KILL-TREND — NOT FIRED (literal).** Per-octave worsts monotone across 5
  octaves (0.3075 -> 0.4487 -> 0.5919 -> 1.0082 -> 1.0245) BUT the LS
  extrapolation crosses 4 at log2(q)=32.74 > 32; chord read 33.61; the last
  octave step collapsed to +0.015 bits/octave. The envelope saturates at the
  IID BASELINE (E-1)/r -> 1 (worst excess +2.45%), 4x under the allowance.
  Amber variant (crossing 1) already realized — subsumed by KILL-AMBER.
- **KILL-GATE-MIRROR — NOT FIRED; mirror PROVED at analogue scale.** Weight-3
  norm census (exact CRT, all 19,840 polys): max divisor depth v_2 = 16 < 20.
  Direct scan: weight-3/4/5 channels EMPTY at ALL 401 gated primes < 2^32;
  weight-6 nonempty at exactly one (918552577 — DEFERRED, below).

Positive controls: PC1 (r2 kills reproduced exactly, incl. E-1 fractions), PC2
(all three killers gate-excluded: v_2 = 7/7/6), PC3 (all three repriced below 4
by the extended ledger alone: K'_ext = 1.768/1.309/2.071), M1 (gate-drop mutation
fires), M2 (fired at all 33 rows), M3 (degraded to M2 as pre-registered — no
gated row even needs its ledger), DPX (two independent E paths agree), enumerator
cross-validation (verbatim w2..6 + banked w7 probe counts). ALL PASS.

## Worst K'_r3 observed per scale

| scale | rows | worst K'_r3 | at q |
|---|---|---|---|
| octave 2^22 | 1 | 0.307530 | 7340033 |
| octave 2^23 | 1 | 0.448742 | 13631489 |
| octave 2^24 | 3 | 0.591912 | 26214401 |
| octave 2^26 | 9 | 1.008154 (AMBER) | 81788929 |
| octave 2^27 | 19 | 1.024517 (AMBER) | 246415361 |
| aspect N=64 | 2 | <= 0.001410 (partial-ledger bound) | 7340033 |

## Are the r2 killers excluded/repriced under r3? (the two positive controls)

YES, both, independently: (1) EXCLUDED — v_2(q-1) = 7, 7, 6 at q = 63361, 65921,
204353, all below the gate 20 (officially: such accident primes are PROVABLY
absent — `dli_wcl_weight3_ambient_exclusion` max depth 18 < 41, weight-4 sibling
max 29 < 41, ell=2 nodes similarly); (2) REPRICED — with the gate ignored, the
extended ledger's w7/w8 orbits (131+510 / 119+470 / 45+128) pull K' to
1.768 / 1.309 / 2.071, all under the allowance. The r2 refutation is fully
neutralized by EITHER lever; r3 does not resurrect any refuted claim (ungated
rows stay refuted forever).

## Evidence weight

- Exact-rational verdict path; complete (not sampled) in-gate census below 2^28;
  complete accident scan to 2^32; controls anchored to banked r2/M2 fractions.
- The two ambers are exact and robust (both rows W_ext = 0, so no enumeration
  subtlety is involved — pure DP facts, mass-invariant checked).
- Scope honestly bounded: exact verdicts only to 2^28; L=2 in-gate empty at
  N=32; official aspect untouched as always.

## What the MIXED verdict means (recommendation, not surgery — I am a worker)

- The two amber trips sit AT the iid asymptote (E-1)/r -> 1: they are the
  gated bulk behaving like an iid spectrum, NOT accident-channel growth (finding
  c1r3-C5). The K'>=1 watch line — inherited from the r2 accident context —
  flags iid noise at near-balance rows and will do so forever as q -> 2^N.
  A watch line intended to detect ACCIDENT pressure should sit strictly above
  the iid baseline. This is a re-calibration finding for round 2; it was NOT
  applied mid-round (house law: no weakening — the frozen line's verdict stands).
- **No amber promotion of `dli_dyadic_k_core` follows from this round** (MIXED,
  and r3 has survived only this one round). The refuted r2 statement stays
  REFUTED; r3 is a live, so-far-unrefuted successor with one adversarial round
  of evidence at gated analogue scale.

## What the amber cascade needs next

1. **Round 2 of C1'-r3** with the amber line re-armed ABOVE the iid asymptote
   (proposal: K'_r3 >= 2, i.e. twice iid, still 2x under the allowance), the
   literal line unchanged at 4, plus a new pre-registered IID-EXCESS line (e.g.
   sustained per-octave excess (E-1)/r - 1 growing across 3 octaves). Nothing
   else about the pose moves.
2. **Price the deferred accident row q=918552577** (unique gated w<=6 carrier
   below 2^32; 32 weight-6 signed vanishers, v_2=22). Needs a segmented/mod-p DP
   (the q-array at 9.2e8 exceeds the 16GiB worker): block-cyclic segmented roll,
   or 2 x int32 residue DP — round-2 engineering item. Its W_ext is nonzero
   (w6 orbit mass 1 per orbit), so the prediction is K'_r3 well under 4; a
   violation there would be a genuine kill.
3. **Extend the exact slice toward 2^32** (the near-balance regime r -> 1 is
   where the envelope saturates): same segmented-DP machinery; the trend line's
   crossing at 32.74 makes the last two octaves (2^30..2^32) the decisive test —
   if saturation at ~1 holds there, the trend threat dies; if the envelope
   re-accelerates, KILL-TREND fires in round 2.
4. **L=2 in-gate at N=64** (gate rows q <= 2^32 satisfy q^2 <= 2^64): needs the
   projected/sharded (q,q) DP (the c1r2 report's round-3 item 4) — first
   nontrivial level-uniformity test of r3 in-gate.
5. **Official side:** if the maintainers adopt the L+7 window, the WCL-ZONE-ext
   obligation adds six emptiness slots (1,7),(1,8),(2,8),(2,9),(4,10),(4,11) to
   the existing four TARGETs — the weight-3/4 norm-census machinery is the
   natural attack (weight-5 first-64 MITM already covers part of (1,5)-adjacent
   ground). If instead the window stays L+5, r3's gate lever alone still
   neutralizes the r2 killers, but the gated-row repricing evidence (PC3, and
   the 4 would-be-amber rows repriced by w7/w8, finding c1r3-C6) argues for L+7.
6. **A proof lead for the bulk:** the iid-baseline convergence at gated rows is
   now an empirical regularity across 33 rows and 5 octaves. A proof that
   official-admissible (deep-split) rows have (E-1)/r <= C with C < 4 — i.e.
   a quantitative iid-approximation theorem under v_2(q-1) large — would close
   C1'-r3's bulk case outright, leaving only the (provably thin) accident
   spectrum to the ledger. This is the number-theoretic crux the r2 kill record
   asked for, now sharpened by the gate.

## Round-2 design sketch (pre-commitments to carry over)

Freeze: pose unchanged (gate 20 analogue / 41 official, window L+7, allowance 4).
Arm: literal K'>4 (unchanged); amber K'>=2 (re-calibrated, pre-registered with
the iid rationale BEFORE any new scan); iid-excess trend line on (E-1)/r - 1;
gate-mirror weight-4 census by factorization (upgrade the operative scan to the
theorem-grade form, mirroring `dli_wcl_weight4_ambient_exclusion`). Compute: the
segmented DP for q in [2^28, 2^32) incl. 918552577, >= 8 rows per octave where
the family allows; N=64 L=2 pilot. Kill standard: any literal row, or amber-2
plus a sustained iid-excess trend, or the deferred accident row violating.

## Deliverables on disk (scratchpad, prefix c1r3_)

`c1r3_pose.md`, `c1r3_falsifiers.md` (pre-registration), `c1r3_census_modal.py`,
`c1r3_pose_arith.py`, `c1r3_primecheck.py`, `c1r3_trendfit.py`, `c1r3_results.md`,
`c1r3_findings.md`, `c1r3_report.md`.
