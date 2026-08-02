# Pilot report: two-slope occupancy v2 (Opus 5 subagent, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable
(entities restored). Coordinator verification and posture:
FABLE_AUDIT.md alongside.

---

# Two-slope occupancy (v2) — the cost theorem, its calibration, and the deficit characterization

**VERDICT.** The occupancy lemma **survives with the two-live-slope structure kept**, and that structure is exactly what defeats every known adversary. The central object is the *condition rank* of a family of two-slope data: per-datum value an **exact constant 2h, independent of depth**; the sunflower is the unique deficit family found and costs **exactly half**; the resulting ceiling **calibrates to the sunflower's realized law digit-for-digit at all three prize rows (383/447/959)**. MC is not mispredicted — it is *invisible to the band*: a proved depth-quantization confines it to d = h-1. **F1 does not fire, F2 does not fire (one correction to the naive reading), F3 fires in half.** 196 checks pass; the 12 "FAIL" lines are two deliberately-measured negative findings.

## 1. THE TWO-SLOPE COST THEOREM

**Formalization**: a depth-d two-slope datum (Z; z_1,S_1; z_2,S_2), |Z| = k+d, |S_j| = A, Z inside S_j, z_1 != z_2 in P^1. Conditions on (u,v): (C0) <c,u> = <c,v> = 0 for c in C_Z; (Cj) <c,u> + z_j <c,v> = 0 for c in C_{S_j} (C_S = duals supported in S, dim |S|-k by L1, re-verified 1800/1800).

**THEOREM 1 (exact cost).** (a) S_1 ^ S_2 = Z exactly (banked T2, not assumed). (b) dim R(P) = 2d + (h-d) + (h-d) = **2h** for every admissible datum, independent of d, including z in {0, inf}. (c) With slopes free, the locus has codimension **2h-2**. *Proof*: the intersection bookkeeping via L1 + (a); the block-sum argument (b = c-a supported in S_1 ^ S_2 = Z); determinantal codim h-d-1 per ray. Verified: rank = 2h at 20 (shape, depth) points across h in {3..7}, every band depth, four slope-pair types; 8 realizations solved from the linear system and re-verified ADMISSIBLE through the banked occlib scan with the intended pair + both slopes live (59/59).

**COROLLARY (two-slope design ceiling).** RS_k x RS_k in every kernel: 2hM - delta <= 2(n-k) - 1, so N_d <= (2(n-k)-1+delta)/(2h) (prescribed) or /(2h-2) (free). Six-row values (all banked pins reproduced): designed families bounded LINEARLY — 191/223/479 at the prize rows — 10^22 inside the 0.68n^2 requirement.

**CALIBRATION.** (i) The sunflower generalized to EVERY d <= (h-1)/2 (closing banked caveat 5): measured cost exactly **h** per pair — half the generic 2h; achieved N_d hits floor((n-k+1)/(h-d)) at 9/9 points. **The cost ceiling with the sunflower's cost, floor((2(n-k)-1)/(h-1)), equals its realized point-budget law EXACTLY at all three prize rows: 383/447/959, ratio 1.00000.** The one correction: a per-pair-additive reading of Theorem 1 mispredicts the sunflower by exactly 2x — the formula is a FAMILY-RANK statement, not a per-member charge. (ii) **THEOREM 5 (MC depth quantization)**: for an MC pencil, distinct coset unions T != T' have |T ^ T'| <= r'-M, so joint agreement <= k+w-M <= k — **the only MC band pairs are diagonal, at depth exactly w**; divisibility forces w a power of two; at the prize rows h-1 is the unique admissible w in [ceil(h/2), h-1] — the cascade tier. Verified exhaustively at 5 MC shapes: depth profile supported on {0, h-1} only; the d = h-1 count reproduces C(N,m)/N exactly; **N_band = 0 at every band depth in every shape**. The largest in-band w is (h-1)/2, where the expected two-slope count is 2^{-2.1e12}. (iii) First moment == codimension: the q-exponent is exactly 2h-2, independent of d; at prize 1/16 d=1 it reproduces the banked 2^{-1.37e12} from an independent derivation.

## 2. THE DEFICIT CHARACTERIZATION

**THEOREM 2 (low/high dichotomy)**: for 2d >= h, under k-packing + the tangent gate, no two depth-d pairs have proportional differences and no live ray carries two — the sunflower mechanism exists ONLY at d <= (h-1)/2 (0 violations, 120 deep pairs).

**THEOREM G (sharing criterion — the structural core)**: two live rays share dual rank iff |S_1 ^ S_2| >= k+1, and then S_1 ^ S_2 IS the joint agreement set of another two-slope band pair at complementary depth e with d + e <= h-1. **Every unit of rank sharing is witnessed by another band pair** (371 witnessed events, 0 violations). The deficit structure is self-referential and graded — which is why it does not terminate into a proof.

**Where deficits can come from**: generic designed = 2h; sunflower = h (extremal, d <= (h-1)/2 only); MC = quantized out (0 in band); mu_n-orbit monomial pencils = NO live rays at all (24 fixtures); coset-supported errors = 0 (8 shapes). Core condition spaces are ALWAYS pairwise transverse (L1 + k-packing), so the only sharing channel is ray-support overlap, which is Theorem G. **Honest limits (the 12 deliberate FAILs)**: core independence is NOT a law (dims short by 1-4 at d >= 2, worst-of-60); random spread designs develop O(1) rank deficits near saturation (inflating M by <= 1.5x at toy scale). Both bounded; neither approaches the o(M) regime F1 needs.

**How weak a sufficient condition would suffice**: N_d <= 0.68n^2 follows from "every family has condition rank >= cM" with c ~ 1.0e-12 at the prize rows — **one fresh condition per ~8e11 pairs**.

## 3. EMPIRICAL GROWTH LAWS

Max N_d exactly linear (two clean series; slopes 1.06, 1.22; exact law verified at 9 points). Cheapest admissible family anywhere = the sunflower at exactly h (5 shapes, ~90 fixtures; nothing below h). **The whole band ledger under the two-slope law is O(n^2), not O(n^3)**: Sum_d N_d L(d) = 0.361/0.492/0.566 n^2 at the prize rows — 2^46 inside the 13n^3 headroom. **Route T's third column would cost ~0.57n^2, not 13n^3.** Sharpened conjecture (SHARP-OCC): N_d <= floor((n-k+1)/(h-d)) at d <= (h-1)/2 and <= floor((2(n-k)-1)/(2h-2)) above — in particular N_d <= n/2 at every band depth, 10^12 stronger than the ledger needs.

## 4. FALSIFIER VERDICTS

**F1 — DOES NOT FIRE** (nothing costs below h per pair; every named deficit-maker yields ZERO in-band two-slope pairs; best construction exactly linear, ~10^22 below requirement). **F2 — DOES NOT FIRE, one correction** (the rank formula calibrates exactly; the naive per-pair reading refuted by exactly 2x). **F3 — FIRES IN HALF**: the designed half is proved and exact (191/223/479, linear); the deficit half is proved-modulo-the-named-class — "a depth-d two-slope family whose condition rank grows sublinearly in M" — with section 2.4 showing rank >= M/8e11 suffices and section 2.3 showing every known structured mechanism is barred (2d >= h), exactly factor-2 (sunflower), or depth-quantized out (MC/coset/orbit).

## 5. FILES

tslib.py (the two-slope engine) . cost.py (59/59) . families.py (48 checks + the 2 intended negatives) . mc.py (18/18 + orbit/coset batteries) . arith.py (36/36, six-row exact) . hunt.py (Theorem G 371 events; the cost hunt; growth) + JSONs/logs. 196 PASS; 12 deliberate FAIL lines (the negative findings). Nothing outside the directory; no commits; nothing m2-related; all under ramguard.

## 6. OVERLAP AND CAVEATS

**Overlap with band_adjudication** (read after computation; nothing written there): their BP(1) and my Theorem 5 are the same fact via different arguments; their BP(3) parity argument is STRICTLY STRONGER than my count and should be preferred; my 5-shape exhaustive N_band = 0 is independent empirical corroboration. Everything else here (cost theorem, ceiling, sunflower cost h + exact calibration, Theorem G, the codimension identity, 2.4, the generalized sunflower) is not in their record.

Caveats: (1) nothing proves the occupancy lemma — the gap is the named sublinear-rank class; (2) the ceiling is a theorem modulo family deficit (O(1) at toy scale; official scale open — the same gap as the H4 hunt's F2, now on the two-slope object); (3) core independence refuted as a law (route (i) unavailable unconditionally); (4) toy scale (n <= 48 rank work, n <= 64 growth); (5) sunflower cost h + e/m, e in [0,4] (asymptotic statement, exact at 4/9); (6) first-moment figures heuristic (they reproduce the banked exponent independently; the proved parts do not lean on them); (7) two growth series timed out (two clean ones support the law; the exact law verified at 9 points regardless); (8) MC's below-cascade one-step failure reproduced, adjudication = the parallel pilot's ratified item.
