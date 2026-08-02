# Pilot report: C2'' cross-junction nullity structure (Opus 5 subagent, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable
(HTML entities restored). Coordinator verification and adopted posture:
FABLE_AUDIT.md alongside.

---

# C2'' pilot — cross-junction nullity structure

**Headline:** the weighted cross-junction nullity has an **exact, field-independent structural law** — `delta_j = (L_j - |S_j|)^+` where `S_j` is the set of *unsaturated* level-(j+1) cells — and that law **kills the replacement currency**. The stratum `{delta = t}` is *exactly* the archived quotient-coset class (verified at 18/18 rows), so `E[q^delta]` re-derives the coset column that clause (i) already routes exactly, while the joint excess `R` is carried by the `delta = 0` stratum, where the invariant is identically 1. Both the identity `R = E_pi[q^delta]` and its dominating version **die with exact counterexamples**. F1 not triggered, **F2 triggered** (with the dominating class named on both sides), F3 not triggered.

## 1. The model

**Model A (abstract prototype, the audit's object).** Latent `U` uniform on `F_q^m`; junction `j` carries a row space `Lam_j` of local rank `r_j`; `Y_j = q^{r_j} 1[Lam_j(U)=0]` (mean one); `delta = sum_j r_j - rank(union_j Lam_j)`; `R = E[prod Y_j] = q^delta` (identity, brute-forced where feasible). Exact `F_q` RREF; exact Fractions. — `nullity.py`

**Model B (DLI-grounded, reconstructed from first principles).** `q` prime, `n = 2^s`, `n | q-1`; `A subset Z/n` is `t`-null iff `p_r(A)=0`, `r=1..t`. Dyadic descent `m_{j+1}(i) = m_j(i)+m_j(i+h_{j+1})`, `d_j(i) = m_j(i)-m_j(i+h_{j+1})`, `h_j = n/2^j`. Since `zeta_{h_j}^{r(i+h_{j+1})} = (-1)^r zeta_{h_j}^{ri}`, constraint `r` is consumed at level `v_2(r)`:

- **block j** owns `U_j = {odd u : u.2^j <= t}`, `L_j = |U_j| = ceil(floor(t/2^j)/2)` — *the pose's `ell_j`, DERIVED rather than assumed* (FX8c);
- its matrix columns are `v_i = (zeta_{h_j}^{u i})_{u in U_j}`, `i in Z/h_{j+1}`;
- the admissible domain makes the **effective support `S_j = {i : 0 < m_{j+1}(i) < 2^{j+1}}`** (the unsaturated cells; at j=0 this is exactly the archived singleton set G with domain {+-1}^G);
- `delta_j = L_j - rank{v_i : i in S_j}`, `delta = sum_j delta_j`.

**The seam (PP2.0 is open; this one is the pilot's, labelled).** `X = q^t Pr_x[t-null]`, `A = prod_j q^{L_j} Pr_x[block j holds]`, `R = X/A = Pr[intersection C_j]/prod_j Pr[C_j]` — the mean-field-normalised joint/product ratio, the only normalisation making every local factor mean-one. `pi_MF` = uniform x on {0,1}^n; `pi_NULL` = uniform on t-null x.

## 2. Fixture validation — 42/42 PASS, then 23/23 PASS

`fixtures.py` -> C2PP_NULLITY_FIXTURES: 42/42 PASS. Reproduced exactly: the four-wise trap (rank 11, delta=22, R=2^22 by EXHAUSTIVE 2^11 latent); the pairwise trap; the gate prime q = 3*2^41+1; the 32-wise moment-curve trap (rank 32, EVERY 32-subfamily rank 32 so delta=0 R=1, full family delta=1 R=q, all 33 subfamilies checked exactly at the gate prime; downscaled replicas brute-forced at q=5,7,11); circuit explosion (C(33,12)=354,817,320; 37^22); continuation amplification 2^31; rank-descriptor collision; information/nullity accounting; the official schedule (2^32,...,2,1,1 — 34 blocks/33 junctions, sum 2^33) with the INDEPENDENT derivation L_j = #{r<=t : v_2(r)=j} matching ell_j for every t in [1,129]; N_j = 256 ell_j = h_{j+1} for n=2^41 (support/constraint ratio exactly 256); reserve arithmetic (2^121, 1.554).

`validate_dli.py` -> C2PP_DLI_MODEL_VALIDATION: 23/23 PASS. V1: x is t-null <=> every block-j skew constraint holds (exhaustive over 2^16, 0 mismatches, t=2..8). V2: independent MITM census reproduces the banked (coset, noncoset) mu_32 ground truth (all 12 SCAN rows exact). V3: junction-0 DP equals brute force. V4: **RANK LAW** rank{v_i : i in S} = min(L_j, |S|) — 37 (row, junction) cells, 7194 supports, 0 violations, exhaustive wherever h_{j+1} <= 14, n up to 128, q in {97,193,257}.

Nothing else ran before these passed. **F3 not triggered.**

## 3. The structural law (the main finding)

**L1 (RANK LAW, exact).** `v_i = zeta_{h_j}^{i} . (1, w_i, ..., w_i^{L_j-1})` with `w_i = zeta_{h_{j+1}}^{i}` pairwise distinct — every junction matrix is a **diagonally scaled Vandermonde**. Hence rank = min(L_j, |S|) for every support, every field.

**L2 (NULLITY FORMULA).** `delta = sum_j (L_j - |S_j|)^+`. **delta is a purely combinatorial support-size functional: no field arithmetic, no q-dependence, no geometry.** Predictive features: junction arity and the saturation profile. Overlap pattern and weight profile are irrelevant.

**L3 (STRATUM LAW).** `{delta = t}` IS the archived coset class — verified at all 18 census rows. (delta = t <=> every cell saturated <=> x constant on residue classes mod h_{Lam+1} = the archived coset test verbatim.)

**O1 (t a power of two).** `delta > 0 <=> |S_0| < L_0`. The whole 33-junction nullity collapses to one number: the singleton count at level 1.

**Exact decomposition certificate.** `rho_j = q^{delta_j} + Rem_j`, the q^delta term being exactly the left-kernel contribution — certified EXACTLY in Z[zeta_q] (integer polynomial reduction): 24/24 PASS at (16,2,17), (16,3,17), (16,2,97).

## 4. Delta distributions and the tail law

Exact pi_MF histograms at n=32: Pr[delta > 0] = 2.6e-4 at t=4; the mass is a geometrically thinning intermediate band ending in the coset atom. Under pi_NULL at (32,4,97) the band is EMPTY: 160 solutions at delta=0 (all noncoset), 16 at delta=4 (all coset).

Measurement table (R and E[q^delta] exact rationals):

| n | t | q | R | E_MF[q^delta] | R/E_MF | delta=0 share of t-null | R from delta=0 |
|---|---|---|---|---|---|---|---|
| 32 | 2 | 97 | 0.99792 | 1.00202 | 0.996 | 99.84% | 0.9963 |
| 32 | 2 | 193 | 1.00759 | 1.00514 | 1.0024 | 99.62% | 1.0037 |
| 32 | 2 | 8353 | 2.39671 | 5.28572 | 0.453 | 55.56% | 1.3315 |
| 32 | 2 | 32801 | 3.76553 | 65.6275 | 0.057 | 0% | 0 |
| 32 | 3 | 97 | 1.03888 | 1.22083 | 0.851 | 88.84% | 0.9229 |
| 32 | 3 | 193 | 1.16066 | 2.04152 | 0.569 | 56.25% | 0.6529 |
| 32 | 4 | 97 | **2.59277** | **1.54723** | **1.676** | 90.91% | **2.3571** |
| 32 | 4 | 193 | 2.55613 | 7.18353 | 0.356 | 0% | 0 |

**Tail law:** E[q^delta] is dominated by the coset atom delta = t. **What delta cannot see:** junction-0 rho over the whole delta_0 = 0 stratum, where the invariant predicts rho = 1 exactly: NOT ONE of 65,535 states attains the prediction (rho in [0, 588x off]; the same run independently re-falsifies the archived profile-constancy conjecture at k = 3..14).

## 5. Candidate-law verdicts

SURVIVES: L1 rank law (7194 supports, 0 violations); L2 field-independent formula; L3 stratum = coset class (18/18); O1; L4 common-latent nullity degenerate (always 0); L9 the joint excess is carried by delta=0 (91% at (32,4,97)); L10 **the nullity is SEAM-DEPENDENT** (level-junction seam -> (L_j - |S_j|)^+; dual element seam -> (|S_j| - L_j)^+ = 255 L_j at the official ratio, i.e. delta' = 255t — the two canonical latent expansions of the SAME junction differ by q^{255t}); L13 **the residual is a NORM-DIVISIBILITY event in Z[zeta_n]** (every skew solution has q | Norm(sum eps_i zeta_n^i): 0 false negatives at q = 17, 97, 113; at q=97,113 exactly 1/8 = 1/phi(16) of norm-divisible sign patterns are solutions — one prime above q, exactly).

DIES: L5 identity R = E_MF[q^delta] (equality at 0/18 rows); L6 dominating form R <= E_MF[q^delta] (exact counterexamples: (32,4,97) R = 198158383604301824/76427240573639025 = 2.59277 > 12979091/8388608 = 1.54723; also (32,2,193)); L7 conditioned identity (overshoots by up to 7.15e16x); L11 trap-geometry circuits in the DLI tower (forbidden by L1+L4); L12 difference-multiset determinism (the F2 Delta analogue: 547/1064 classes carry >1 rho).

## 6. The traps through the surviving law

The traps all need a circuit straddling junctions; in the DLI tower the block row spaces are disjoint Vandermonde row groups (L4: sum of ranks = global rank, 0 defect) and every within-junction support has full rank (L1) — **no circuit of any support can exist**. The traps are exactly the configurations the dyadic-Vandermonde geometry forbids. What survives of them is the SEAM question (L10), not the geometry. Descriptor collision and continuation amplification live in the residual, which is arithmetic (L13), not linear-algebraic.

## 7. At the official schedule (exact arithmetic)

Pins: t = 2^33, ell = (2^32,...,2,1,1), N_j = 256 ell_j, n = 2^41, q = 1 + k.2^41 < 2^256 prime.

- **O2.** The coset stratum has exactly 2^128 block-constant supports (n/2^34 = 128 level-34 cells).
- **O3.** Its contribution to E_MF[q^delta] is 2^{2^33(log2 q - 256) + 128}: it exceeds the 21-bit reserve iff 256 - log2 q < 107/2^33. Concrete admissible exhibit: q = 2^256 - 191,315,023,233,023 (prime by BPSW), coset contribution = 2^{128 - O(2^-175)} — **107 bits above the reserve from one stratum**. At the small end (q = 6,597,069,766,657) the same term is 2^{-1.83e12}. E_MF[q^delta] tracks R at NEITHER end.
- **O4.** The per-block nullity main term q^{ell_j}/2^{256 ell_j} is verbatim the r_j of `dli_marginal_baseline100_coverage` — the nullity currency re-derives the 100-bit MARGINAL account, not the 21-bit joint reserve.

## 8. Falsifier verdicts

**F1 — NOT TRIGGERED** (delta is MORE structured than the trivial bound: exact closed form, field-independent, collapsing to |S_0| at the official schedule, top stratum = a named lane object).
**F2 — TRIGGERED, sharply.** Two dominating classes, neither the target: E[q^delta] is dominated by the coset stratum (already routed exactly by clause (i) and priced by the marginal-baseline node); the joint excess R is carried by delta=0, where the invariant is identically 1 and empirically NEVER correct. By the audit's own kill line ("if the first true multi-junction compiler cannot reproduce X/A through an exact or dominating rank-defect partition, the C2'' strategy is RETIRED, not rescued by descriptor refinement"): **the NUL0-NUL4 rank-defect route as posed is refuted at the level-junction seam**, on a compiler validated against every banked ground-truth row.
**F3 — NOT TRIGGERED** (42/42 + 23/23 exact reproduction).

## 9. What this hands the lane

1. **A validated true multi-junction exact compiler (PP2.1 delivered)**: independent MITM reproduces all 12 SCAN censuses; the block decomposition is proved exhaustively; ell_j DERIVED; N_j = 256 ell_j = h_{j+1} confirmed independently.
2. **Gate 0 is decisive, not merely unresolved**: two canonical latent expansions of the same junction give nullities 0 and 255t. No nullity statement is meaningful before PP2.0.
3. **The correct residual currency is ARITHMETIC, not linear-algebraic**: rho = q^delta + Rem certified exactly in Z[zeta_q]; in DLI the q^delta term is inert and Rem is a norm-divisibility event — routing C2'''s residual straight into machinery the lane already owns (dli_wcl_ell2_weight5_norm_gcd_exclusion, RESULTANT_GATE_SUMMARY, the archived Test-3 norm-gate picture) rather than into matroid/Bellman work.
4. **A named exhibit for the reserve arithmetic**: q = 2^256 - 191315023233023, where one nullity stratum alone is 2^128.

## 10. Files

`nullity.py` . `fixtures.py` (42) . `dli_model.py` . `validate_dli.py` (V1-V4) . `census.py` . `junctions.py` . `laws.py` (L4-L13) . `official.py`; `results/`: fixture_validation, dli_validation, rank_law, census_* (18 rows), junction0_rho, cyclotomic_split, laws, law_table, official_scale JSONs + logs. All under ramguard local; nothing outside the directory; no commits.

## 11. Honest caveats

- **The seam is the pilot's own** (PP2.0 open): L5-L7 verdicts are seam-relative; L1-L4, L10-L13, O1-O4 are not.
- **Scale**: exhaustive censuses to n = 32 (support/constraint ratio <= 16 vs official 256); rank law checked to n = 128; official-scale statements are analytic consequences validated at small n, not measured at 2^41.
- t = 2^33 used (matches the tower schedule); dyadic_profile_evaluation lists 2^33+1 for prize rows — off-by-one not reconciled, moves nothing structural.
- n = 2^41 inferred (forced by N_j = 256 ell_j = n/2^{j+1}), matching dyadic_profile_evaluation.
- Primality of the 256-bit exhibit is BPSW, not a certificate.
- L13 measured at n = 16, o = 1, three primes; the 1/phi(n) splitting ratio exact there, conjectural beyond.
- E_MF[q^delta] at official scale has a rigorous LOWER bound only (the coset atom) — sufficient for the falsification of "<= 2^21", no matching upper bound established.
- O1 uses L_j = L_0/2^j, exact for t a power of two (the official case).
