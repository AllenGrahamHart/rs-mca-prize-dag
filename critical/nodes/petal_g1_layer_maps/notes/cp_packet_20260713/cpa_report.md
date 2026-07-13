# cpa_report — fresh-context ADVERSARIAL AUDIT of the clause-(P) packet
# cp_packet_20260713 (petal_g1_layer_maps). Auditor, 2026-07-13.
# Companions: cpa_findings.md (catches cpa-C1..C5), cpa_checks.py
# (independent battery: stages A1-A6, 37 PASS 0 FAIL, all ramguard tiny).

## VERDICT: SOUND

Clause (P) of petal_g1_layer_maps, as posed by the bsr re-pose (floor band
d >= 2(t_ch - 2), official rows, layout-anchored, weighted census <=
(121/128) n^6), is PROVED by the packet. Every load-bearing link was
re-derived by hand and re-verified with independently written machinery
(different census method: k-subsets vs the packet's (k+1)-subsets;
Lagrange-only interpolation; a functional lift test; an independent
quotient-side lift recount). Zero mathematical defects found. The
adversarial construction attempts (uncovered contributor, off-by-one at
every boundary, fail-open verifier paths, consumer-semantics mismatch)
all failed to break the packet. Findings are confined to: two cosmetic
wording/hygiene repairs (cpa-C1, cpa-C2), one narrow per-cell verifier
window (cpa-C3), one dag-side text annotation for banking (cpa-C4), one
scope-mass observation (cpa-C5). Banking conditions (all already in the
packet's own surgery spec, now audit-confirmed): the #168 layout-anchoring
pin MUST land in the dag statement text, and the dag's #153/boundary-law
line must be relabelled per surgery item 3 + cpa-C4.

## Link-by-link table

| # | Claim audited | Verdict | Evidence |
|---|---------------|---------|----------|
| a1 | Lemma B rigidity (floor + full-petal + \|S\|>=k+1 => j <= J = k+3-2t_ch, m in {t_ch-1, t_ch}) | PASS | Hand re-derivation (2m >= d+2-s_r; ceil((2t_ch-3)/2) = t_ch-1); EXHAUSTIVE combinatorial verification over 1770 layout shapes n<=64, any k, b0<=1: 0 violations (cpa_checks A2) |
| a2 | No off-by-one at the boundaries | PASS | Corner (j=J, m=t_ch-1, s_r=0) sits at \|S\| = k+1 exactly in every shape (identity J+2(t-1) = k+1); m = t_ch-2 stratum arithmetically impossible (max reach k+b0-1); both strata and both retained flavors realized in vivo at (16,8,97) (A2, A4) |
| a3 | Boundary bookkeeping dispute vs bsra's printed "2k >= n-1" | PASS — packet is right | Operational t_ch = (n-k)/2 (re-derived from the layout construction; = len(petals) in bsr_check) gives 2k >= n-2; bsra's (n-k+1)/2 is the odd-k count. Decisive out-of-scope witness (10,4,11): printed law says empty, 3 aperiodic floor-band full-petal lifts REALIZE in vivo (A1). In scope both collapse to 2k >= n (parity, s=3..24 exhaustive) — immaterial, as the packet's #169 remark says |
| b1 | Official rows n = 2^42..2^44 (k = 2^40): J < 0, floor band EMPTY for all contributors | PASS | Recomputed: t_ch = 3*2^39 / 7*2^39 / 15*2^39; J = 3-2^41, 3-6*2^40, 3-14*2^40 < 0 (A1); d <= k-1 < thr makes the band empty for ANY scale — re-derived |
| b2 | Empty at rates 1/4, 1/8, 1/16 for all s = 13..44 | PASS | J < 0 at every such cell, exact integers (A1); in-vivo nonvacuous confirmation at (16,4,97): 51 contributor classes (recount agrees), floor 0 (A4) |
| c1 | Rate 1/2: J = 3 at every row size | PASS | J = 2k-n+3 = 3 identically at n = 2k; verified s = 3..44 (A3) |
| c2 | N_max = 2^{b0}(t_ch+1)S_J(k-1); S_J = sum_{i<=J} C(k-1,i); binding row exact | PASS | Definition matches cp_proof Lemma C (2^{b0} = retained-flavor factor); exact bigint recompute (own code): n = 2^41 gives log2 N_max = 157.4150, budget = 245.9189, margin = 88.5038 — the claimed 157.42/245.92/88.50 exact; all s = 3..44 fit, worst margin 2^12 at s = 3; N_max/(n^4/96) = 1.0000 (A3) |
| d1 | Atlas is word-independent and covers every floor-band full-petal contributor (aperiodic AND periodic) | PASS | A^prim depends only on (L); coverage is definitional (chart (Z\S, S cap B) always in the index when d >= thr) — adversarial scan at (16,8,97) complete census: 0 uncovered (A4); mutant index thr+2 DOES fail coverage (9 classes, A6/NM3), so the coverage notion has teeth |
| d2 | No missed contributor shape | PASS (scope verified) | \|S\| = k is not a contributor (needs >= k+sigma = k+1); both retained flavors in the atlas and realized; partial/mixed-petal is EXPLICITLY outside clause (P) AND outside petal_growth's top-band obligation (dag statement: separate obligations) — out-of-scope mass measured 43 at (16,8,97), recorded as cpa-C5 (observation, not a defect); periodic covered a fortiori (only aperiodic demanded) |
| e | Per-chart K4 m+1 line re-proved word-free; consistent with PROVED K4 | PASS | Support-counting is purely set-theoretic: disjoint petals => touched set recoverable from the union; NO distinct-petal-value assumption anywhere; the atlas charts satisfy K4's hypotheses (m_chi = t_ch >= 2, d >= 2(t_ch-2), \|R0\| <= 1 < ell) so PROVED K4 gives the same m+1 — the packet's line is a re-derivation at equal strength, not a weakening; in vivo per-chart max 3 <= 5 and 8 <= 9 (A4, A5) |
| f | Catch #168 layout anchoring vs consumer semantics (CRITICAL fidelity check) | PASS | petal_growth/conditional.md pin P1: band d >= M(t-2) with t = the carried layout's petal count (fixed-layout semantics); dag petal_growth statement same; census gate consumes the layout-free support-size band {k+2,k+4} via COL; K4 is chart-level. NO consumer needs the layout-existential form. The existential reading's refutation verified: kill arithmetic C(63,32) = 2^59.6686 > (121/128)128^6 = 2^41.9189 (A3); witness re-basing replayed (cp_verify P6). BANKING CONDITION: the #168 pin must land in the dag statement (packet surgery item 1) |
| g | Consumed-hypotheses table complete; no open hypothesis consumed | PASS | petal_g3_full_support_codeword_injectivity: PROVED in dag (one-line, checked); petal_top_band_tail_collapse: PROVED (cited for chart legality only; m+1 re-derived anyway); pin P1 = floor is the pinned POSING (decision-gate) with pre-registered tripwire (P)-3 intact; #168 is a semantics pin with a constructive refutation of the alternative; Lemmas A/B/C re-derived independently (A1/A2) — nothing else consumed; sections 4-5 analyses explicitly NOT consumed by Theorem P |
| h1 | cp_verify.py replay | PASS | 59 PASS 0 FAIL under ramguard tiny, output matches the packet record line for line |
| h2 | Fail-open audit (house catches #137/#165 in mind) | PASS with notes | Nonemptiness asserted at P1, P2, P3a/b (class census), P5 (contributors exist); P4 shuffled cell is vacuous but FLAGGED as such in cp_findings with the nonvacuous fiber_pairs cell alongside; findings: cpa-C1 (P1 atlas checks tautological — no false-PASS risk, but no discriminating power), cpa-C3 (P3b lacks a lift-subfamily nonemptiness assert — narrow per-cell window), cpa-C2 (M4's check name overstates: universal re-basability is proved by arithmetic, machine-checked only for one witness) |
| h3 | The 4 REQUIRED-TO-TRIP mutations exercise the load-bearing steps | PASS | M1 = band threshold (widen one petal -> 550 classes j=5), M2 = stratum inclusion (1 < 10), M3 = word-dependence of the census (83 -> 41), M4 = layout anchoring (re-basing demo + kill arithmetic) — each replayed |
| h4 | >= 2 NEW auditor mutations, must trip | PASS | NM1 (j <= J-1: 8 realized j=3 classes violate — J-boundary exercised from below), NM2 (drop m = t stratum: 9 < 10), NM3 (atlas index thr+2: 9 uncovered) — all trip (A6) |
| i | #170 consistency: is the #153 cap cited anywhere as a full-band account? | PASS with repair | bsr_check n_floor (lines 325-338) confirmed LIFT-ONLY — banked 53/48/8 are lift pins, as #170 states; my full-band recounts 10/83 strictly exceed the lift parts (A4/A5); grep of dag.json + repo: only the G1 statement's own surgery line carries the ambiguous "#153 both-subfamilies cap" apposition AND the wrong printed boundary constant "2k >= n-1" — repair cpa-C4 (matches the packet's surgery item 3, now audit-confirmed needed); the other dag "#153" (envelope node) is unrelated WP numbering |

## What would change the verdict

- Pin P1 resolved to the wide/per-member band without the odd-lift
  carve-out: clause (P) falls by the #145 arithmetic — this is the
  packet's own pre-registered tripwire (P)-3, NOT a defect; the packet is
  conditional on the pinned posing exactly as every pinned node is.
- The #168 pin dropped at banking: the un-pinned (ambiguous) statement
  admits a FALSE disambiguation — surgery item 1 is mandatory.

## Audit artifacts

- cpa_checks.py — 6 stages, 37 PASS 0 FAIL total, every stage under
  tools/ramguard tiny (largest ~15 s). Stage map: A1 boundary/emptiness
  (+ the (10,4,11) decisive witness), A2 exhaustive Lemma-B combinatorics
  (1770 shapes), A3 exact bigint budget/caps/kill, A4 independent
  complete censuses at (16,8,97) + (16,4,97), A5 independent (32,16,97)
  census + quotient recount, A6 new mutations NM1-NM3.
- cpa_findings.md — catches cpa-C1..C5 with severities; fidelity notes on
  #168/#170/#171/#138; DEFERRED: none (no Modal needed).
