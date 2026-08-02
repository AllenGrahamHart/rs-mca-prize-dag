# Pilot report: P-B (H4) residual hunt (Opus 5 subagent, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable
(HTML entities restored). Coordinator verification and adopted posture:
FABLE_AUDIT.md alongside.

---

# (H4) BEYOND SPLIT-FIBRE — lane P-B

## HEADLINE

1. **The design space collapses to a single object, and it is exhaustible.** Only the top h coefficients of a monic degree-A pencil are visible to the witness condition: S is an exact-A witness at z iff e_j(S) = alpha_j + z beta_j (j = 1..h). The ENTIRE design space of degree-A pencils IS the space of affine lines of AG(h,q); the planted family is E^{-1}(L) for the moment map E(S) = (e_1..e_h)(S) — by Newton, the SUBSET-SUM MAP OF THE MOMENT CURVE. Multi-core variants, non-monomial multipliers, product/trace shapes, and design-driven placements are NOT distinct geometries — each only names a line. Searched EXHAUSTIVELY at five shapes (up to 89,451,363 lines each, exact arithmetic): **the richest admissible line is the split-fibre line, every time, and it carries Gamma_lo = 0 every time.**
2. **The counting theorem: proved in the design direction, REFUTED as a lane-closer.** Prescribing a spread family costs Mh independent linear conditions capped by 2(n-K) (RS_K x RS_K is always in the kernel); the enabling lemma is **dim(C_S ^ C_T) = max(0, |S^T| - K)** (verified 1599/1599). **DESIGN CEILING: M <= (2(n-K)-1)/(h-1) = 383/447/959/383/447/959 at the six rows — 2^23.1 to 2^117.4 BELOW 8n^3.** Measured exactly: ceiling 10 predicted and achieved (11 impossible), 12 within the free family, 15 the free-slope bound. **But the ceiling bounds only DESIGNED witnesses**; the random supply exceeds it, and a spread family of size 20 with rank deficit 29 and ZERO collision exists (the mu_n-orbit of the monomial pencil). **F2 fires.** The ceiling does not discharge (H4). The saving observation: that class produces DEFICIT WITHOUT EXCESS (40 witnesses vs 46.1 mean supply) — symmetry buys deficit, not over-supply.
3. **A generalization of (SF-SELFCOLLISION), plus a correction to it.** *Block dichotomy* (proved + verified): block moment vectors must be collinear; spread iff every block has size m >= h+1; for the only algebraically available blocks (cosets of mu_m — n a 2-power, q prime), beta_j = m lam_j e_m when m <= h (spread fails: A-m >= K) and beta_j = 0 when m > h (one slope, strip) — **spreadness and a live slope-direction are INCOMPATIBLE for every coset block geometry** (deriving SF-SELFCOLLISION's range m <= h < 2m rather than assuming it). Non-coset spread blocks: infeasible by 262-957 bits (RowC) / ~10^12 bits (prize) on first moment. **THE CORRECTION: Gamma_lo = 0 for split-fibre is a SELECTOR theorem, not an identity consequence** — adjacent partners live at OTHER slopes; under a UNIFORM selector Gamma_lo = q e^{-nu} (measured up to 1742/4993 slopes, matching to 10%), and official RowC 1/4 has nu = 3.0, so a uniform selector would leave ~5% of slopes = ~2^187 >> 8n^3. Under support-lex first-match: **Gamma_lo = 0 at 18/18 points** across nu in [0.05, 30].

## 1. THE DESIGN SPACE — enumerated and collapsed

Formalisation: in the word model, S is a witness iff the 2xh syndrome matrix has rank <= 1 (h-1 conditions + the ratio z); in the pencil model, (STAR): e_j(S) = alpha_j + z beta_j. Only degrees A-1..A-h of (U,V) enter; everything below K is INVISIBLE GAUGE.

Geometry verdicts: (a) multi-core = same line; (b) non-monomial multipliers collapse to split-fibre (W invisible above K for h < 2m); (b') subfield/trace structures UNAVAILABLE (q prime — no proper subfield at any official row); (b'') non-subgroup block systems (Dickson, dihedral) strictly worse than random; (c) design-driven placements: at most 2 supports prescribable in the pencil model (2(h-1) parameters / h-1 per point) — the adversary has NO algebraic leverage beyond choosing a line; (d) group-orbit (monomial) pencils: real and spread but NO EXCESS; (e) linear-algebra planting (word model): real, constructive, capped by the design ceiling; (f) spread block systems: the only residue — closed for cosets by the dichotomy, infeasible off cosets by the stated margins.

**Gate finding (scope correction for P-B):** T1/T3/T4 and "v nowhere zero" read off the WORDS are VACUOUS — invisible degree-<K terms toggle them without moving a witness. Gauge-invariant forms used throughout: (GI-strip) beta != 0; (GI-T3) L not invariant under diag(zeta^j) for any M > 1 | gcd(n,K). **The strip/genericity gates must be stated on (alpha, beta) — equivalently modulo RS_K — or they can be evaded for free.**

**Incidence distribution** (89.45M lines at A1): Poisson(mu) to three digits, plus a purely structural tail (fold/split-fibre orbits) that contributes ZERO to Gamma_lo.

## 2. THE COUNTING THEOREM — proof and the precise gap

**Lemma (L1)**: dim(C_S ^ C_T) = max(0, |S ^ T| - K); spread <=> pairwise-transverse condition spaces (dual distance K+1). **Theorem (DESIGN CEILING)**: rank = min(Mh, 2r) on transverse rows (r = n-K), non-codeword solution iff M <= (2r-1)/h (slopes prescribed) / (2r-1)/(h-1) (free). Measured: full rank at every random spread point; the split-fibre line at the same scale has 252 rows of rank 29 (deficit 223) WITH max core >= K — deficit via collision. **The F2 exhibit**: the monomial pencil U = X^A, V = -X^{A-1} at n=20, q=41 — mu_n-invariant witness set, a fully spread 20-member orbit, Gamma_lo = 20, rank 31 of 60 rows (deficit 29, ZERO collision, M = 20 > even the free-slope ceiling 15). **"Rank deficit forces self-collision" is FALSE.**

**Official corollary worth banking**: any P-B counterexample must be at least 1 - 2^-23 "forced" — at most ~960 of its > 8n^3 members can be independently designed.

**The exact (H4) constant, exhaustively**: lambda = max_L Gamma_lo(L)/mu = 4.9-10.8 at the toy shapes (small-mu artefact); the Gamma_lo-maximisers are ORDINARY POISSON LINES, never the rich ones. Refined **(H4')**: |Gamma_lo| <= mu + sqrt(4(h-1) mu ln q) + O(h log q); at RowC 1/16's worst admissible q the correction is 1 + 2^-11.2 — **the FRAGILE row's 0.77-bit slack is NOT consumed by the (H4) constant**. **The precise remaining gap**: (H4) <=> "the only rich lines are block-composition lines" (an equidistribution/Weil input, known false in general precisely because split-fibre is a 2^204-point collinear locus — the proof must carve out the block-composition locus first; the second half — block lines self-collide — is proved here; the first half is verified exhaustively at five shapes).

## 3. Constructions and obstructions

**CONSTRUCTED — linear-algebra planting** (genuinely non-split-fibre): M = 10 random spread supports at 10 prescribed slopes at n=20, q=241; exhaustive verification over all 77,520 subsets: the 10 planted supports are the ONLY witnesses (x7.5 over-supply), Gamma_lo(lex) = 10, planted-is-first-match 10/10; free-family scan raises to 12. **Spread planting off the split-fibre locus is real — and saturates at O(n/h).**

**OBSTRUCTED — block geometries**: the collinearity lemma, the spread threshold (m >= h+1), and the coset dichotomy (above). The sub-family trick is VOID: the one q-independent designed family found (pairs of mu_2-cosets, 66 = C(12,2) blocks at q = 73/241/1201 alike, genuinely spread) cannot be REALISED thinned — the carrying pencil is the split-fibre pencil whose full witness set includes the un-thinned coset family: 10/10 sub-family members have a core->=K partner at a DIFFERENT slope. E^{-1}(L) is closed under coset refinement.

## 4. THE SELECTOR CATCH — correction to the banked K1 closure

(SF-SELFCOLLISION)'s max core A-m >= K is attained ONLY by adjacent label sets, whose partners live at other slopes. Gamma_lo = 0 therefore requires the SELECTOR to pick adjacent supports at partner slopes. Control parameter nu = a(b-a).#slopes/C(b,a) (expected selected neighbours per member); official RowC 1/4: **nu = 3.0**. Measured (3 shapes x 6 nu values, up to 736,281 candidates over 144,729 slopes): support-lex first-match **Gamma_lo = 0 at 18/18**; colex 0-11; **uniform selector 249/1157/1742/622/15/0.3 — matching q e^{-nu} within 10%**. At the envelope pin lg nu = +58.9..+130.8 (selector irrelevant there); at the L1 floor lg nu = +1.18..+18.14. **Net: the banked K1-closed conclusion SURVIVES and is now verified at the official ratio — but its proof obligation is a JOINT identity-plus-support-keyed-selector statement, not the identity alone. The lane note and (PB-SUPPLY) skeleton must be amended; K1 re-couples to the PP4.0 A1 fork.**

## 5. Falsifier verdicts

- **F1 — DOES NOT FIRE.** No admissible pencil in the exhaustively searched design space plants a spread family above the random supply by more than lambda ~ 5-11 (small-mu); the richest lines are always split-fibre/fold with Gamma_lo = 0; constructive planting saturates at the design ceiling (<= 960 at official rows, 2^23-2^117 below budget). **P-B is not endangered by any construction found.**
- **F2 — FIRES, decisively.** The counting theorem is structurally false as a lane-closer: group-orbit pencils give rank deficit without self-collision (exhibited exactly). Saving fact: deficit != excess.
- **F3 — FIRES, quantified.** Designed placements: count 2 in the pencil model (q-independent — a line is two points); <= (2(n-K)-1)/(h-1) in the word model; the one q-independent designed family is void by coset-closure.

## 6. File inventory

core.py . expA.py (EXPA_A*.json — richest-line search + GI gate) . expB.py (EXPB_A*.json — exhaustive Gamma_lo maximisation over every affine line, 89.45M/case) . expC.py (EXPC_*.json — L1 1599/1599; rank ladder; the M=10 planted pencil vs all 77,520 subsets; the orbit F2 exhibit; the free-family scan) . expD.py (selector sweep) . expE.py (spread-block collinearity search) . expF.py (sub-family closure fixture) . official.py (six-row ceilings, margins, nu). Nothing outside the directory; imports read-only; no commits; nothing m2-related; all under ramguard.

## 7. Honest caveats

1. **EXPA/EXPB exhaust the degree-A PENCIL model (a 2h-dimensional slice); the word model (2(n-K)-dimensional) is covered only by the DOF/rank theorem + constructive fixtures.** A word-model exhaustive search is out of reach — the single largest gap in the "no other geometry" claim.
2. Toy-scale spread contamination suppresses Gamma_lo and could hide a spread-rich line; the spread-faithful case (n=24, q=2473) did not finish inside the compute law and is NOT in the record.
3. lambda measured only at small mu; the official extrapolation uses the Poisson-max law — the same equidistribution gap as (H4) itself.
4. The block dichotomy is proved for disjoint-block families with fixed core; core-varying and non-block families are covered only by the toy exhaustive search + the design ceiling.
5. The spread-block infeasibility is a first-moment count, not a theorem (split-fibre is the standing proof that first moments can be wrong by 2^170 on an exceptional locus).
6. **Gamma_lo = 0 for split-fibre is now a SELECTOR result** — it inherits every caveat of the PP4.0 A1 fork; if PP4.0 is written polynomial/codeword-keyed, K1 comes back at ~q e^{-nu}.
7. Nothing here is proved about P-B; the ceilings, L1, the dichotomy, and the exhaustive maxima are exact; the discharge of (H4) is not.
